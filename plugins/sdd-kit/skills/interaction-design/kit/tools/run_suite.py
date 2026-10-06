#!/usr/bin/env python3
"""run_suite.py — the project-neutral acceptance runner (CH-01 · CC-01 WP-1 · ADR-077).

The kit's own KIT_TEST_CMD engine: it executes a model's `acceptance` block (fixtures +
given/when/then scenarios) against the DEPLOYED app on a live instance, so an enforcement
claim can be BACKED by an observed refusal instead of a static binding. It generalises the
proven reference-build harness to every action and
assert in the schema, resolving the instance (base URL, DB, data-API) from instances.yaml.

Behavioural honesty (nothing under test is faked):
  · every `when` step goes through the DEPLOYED FormService via the generated data API
    (POST /api/form/<formId>/saveOrUpdate) — validators and postProcessors run (D-009:
    HTTP 200 + {"errors":{...}} on a validation refusal; the runner reads the body).
  · every `then` assert reads the row back (read-only SQL) or inspects the submit response.

D-024 discipline: cold-start clean(), per-run unique fixture ids (RUN_TOKEN — id reuse after
a delete trips Hibernate's stale-object cache), non-overlapping ids scoped to this run. clean()
also runs once more when the run ends, so the last scenario's records do not stay behind, and it
removes the status chain's entries the application wrote for the runner's records
(METHOD-2026-09-25-01, item 15).

Instance resolution:
  base + the database's address from ~/.joget/instances.yaml (shared with deploy_dx9), the
  database password reaching psql through its environment (PGPASSWORD), never its arguments,
  which the process list shows (METHOD-2026-09-25-01, item 3); data-API credential
  is api_id = "API-<appId>-data" (the .jwa carries the definition) + an api_key resolved from
  --api-key, else env KIT_API_KEY_<appId>, else KIT_API_KEY (tools/register_api_key.py <appId>
  --instance <name> binds the key KIT_API_KEY_<appId> holds on the server, never showing it).

    run_suite.py <app.yaml> --instance jdx7 [--api-key KEY] [--feature F] [--out result.yaml]

Exit 0 = all executed scenarios pass · 1 = any failure or setup error (a publishable outcome).
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from collections import deque
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("run_suite.py needs pyyaml (pip install pyyaml)")

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import deploy_dx9 as dep  # instance resolution, the database's address and psql's environment

RUN_PREFIX = "SCN"
RUN_TOKEN = format(int(time.time()) % 46656, "03x")   # unique per run (D-024)
# The status chain the transition guard writes (joget-transition-guard, EVENT_FORM; the kit's
# storage form tools/project_lifecycle.py MM_FORMS): one row per move, keyed on the record's id.
STATUS_EVENT_TABLE = "app_fd_statusEvent"


# ------------------------------------------------------------------ db + api
class Db:
    """How psql reaches the instance's database: the connection string WITHOUT the password
    (deploy_dx9._pg_url) and the password in the environment psql reads (deploy_dx9._pg_env,
    PGPASSWORD). A password in psql's arguments stands in the process list for as long as psql
    runs (METHOD-2026-09-25-01, item 3)."""

    def __init__(self, url: str, env: dict | None = None):
        self.url, self.env = url, env

    @classmethod
    def of(cls, inst: dict) -> "Db":
        return cls(dep._pg_url(inst), dep._pg_env(inst))


def _sql(db: Db, q: str) -> str:
    r = subprocess.run(["psql", db.url, "-tAF", "|", "-v", "ON_ERROR_STOP=1", "-c", q],
                       capture_output=True, text=True, env=db.env)
    if r.returncode != 0:
        raise RuntimeError(f"psql: {r.stderr.strip()[-300:]}")
    return r.stdout.strip()


def _qv(v) -> str:
    return "'" + str(v).replace("'", "''") + "'"


class Api:
    """The deployed app's generated data API (API Builder). saveOrUpdate runs FormService."""
    def __init__(self, base: str, api_id: str, api_key: str):
        self.base = base.rstrip("/")
        self.h = {"Content-Type": "application/json", "Accept": "application/json",
                  "api_id": api_id, "api_key": api_key}

    def save(self, form_id: str, payload: dict) -> tuple[int, dict]:
        req = urllib.request.Request(f"{self.base}/api/form/{form_id}/saveOrUpdate",
                                     data=json.dumps(payload).encode(), method="POST")
        for k, v in self.h.items():
            req.add_header(k, v)
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                body = r.read().decode()
                code = r.status
        except urllib.error.HTTPError as e:
            body, code = e.read().decode(), e.code
        try:
            return code, (json.loads(body) if body.strip() else {})
        except json.JSONDecodeError:
            return code, {"_raw": body[:300]}


# --------------------------------------------------------------------- model
class Model:
    def __init__(self, path: Path):
        self.doc = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
        self.app_id = (self.doc.get("app") or {}).get("id") or Path(path).stem
        self.entities = {e["id"]: e for e in self.doc.get("entities", [])}
        self.forms = self.doc.get("forms", []) or []
        acc = self.doc.get("acceptance", {}) or {}
        self.fixtures = {f["id"]: f for f in acc.get("fixtures", []) or []}
        self.scenarios = acc.get("scenarios", []) or []

    def table(self, ent: str) -> str:
        return "app_fd_" + self.entities[ent]["table"]

    def lifecycle(self, ent: str) -> dict:
        return self.entities[ent].get("lifecycle") or {}

    def initial_state(self, ent: str):
        return next((s["id"] for s in self.lifecycle(ent).get("states", []) if s.get("initial")), None)

    def state_column(self, ent: str) -> str:
        """The column holding the record's state: the attribute its lifecycle names
        (`lifecycle.status_attr`; `state` in one application, `status` in the worked reference).
        It was always c_status, so a model whose state is another attribute had its state
        asserted as that other column's value (METHOD-2026-09-25-01, item 14)."""
        return "c_" + (self.lifecycle(ent).get("status_attr") or "status")

    @staticmethod
    def _pascal(ent: str) -> str:
        return "".join(w.capitalize() for w in ent.split("_"))

    def create_form(self, ent: str) -> str:
        """The form that creates a row for `ent`: prefer a purpose:create form bound to the
        entity/table, else the first bound form, else the frm<Pascal> convention. A fixture
        record may override with an explicit `form` key."""
        etable = self.entities[ent].get("table")
        cands = [f for f in self.forms
                 if (f.get("entity") == ent or f.get("table") == etable) and (f.get("id") or f.get("form"))]
        for f in cands:
            if f.get("purpose") in ("create", "add", "new", "open"):
                return f.get("id") or f.get("form")
        if cands:
            return cands[0].get("id") or cands[0].get("form")
        return "frm" + self._pascal(ent)

    def activity_outcome(self, proc_id: str, act_id: str, outcome_id: str):
        """(entity, form, transition) for a process activity's declared outcome.
        The model states the mapping; the runner never guesses it."""
        proc = next((p for p in self.doc.get("processes", []) or []
                     if p["id"] == proc_id), None)
        if proc is None:
            raise RuntimeError(f"complete_activity: no process {proc_id!r} in the model")
        act = next((a for a in proc.get("activities", []) or []
                    if a["id"] == act_id), None)
        if act is None:
            raise RuntimeError(f"complete_activity: process {proc_id!r} has no activity {act_id!r}")
        out = next((o for o in act.get("outcomes", []) or []
                    if o["id"] == outcome_id), None)
        if out is None:
            have = ", ".join(o["id"] for o in act.get("outcomes", []) or [])
            raise RuntimeError(f"complete_activity: activity {act_id!r} has no outcome "
                               f"{outcome_id!r} (declared: {have})")
        return proc.get("entity"), act.get("form"), out.get("transition")

    def events_form(self, ent: str) -> str:
        return "frm" + self._pascal(ent) + "Events"     # ADR-066 engine surface

    def path_to(self, ent: str, target: str) -> list[str]:
        lc, start = self.lifecycle(ent), self.initial_state(ent)
        if target == start or not target:
            return []
        adj: dict[str, list] = {}
        for t in lc.get("transitions", []):
            adj.setdefault(t["from"], []).append((t["id"], t["to"]))
        q, seen = deque([(start, [])]), {start}
        while q:
            state, path = q.popleft()
            for tid, to in adj.get(state, []):
                if to in seen:
                    continue
                if to == target:
                    return path + [tid]
                seen.add(to)
                q.append((to, path + [tid]))
        raise RuntimeError(f"no transition path {start} -> {target} for {ent}")


# -------------------------------------------------------------------- runner
class Runner:
    def __init__(self, model: Model, api: Api, db: Db):
        self.m, self.api, self.db = model, api, db
        self.log: list[str] = []

    def say(self, s: str):
        self.log.append(s)
        print(s, flush=True)

    def _col(self, ent, rid, col):
        return _sql(self.db, f"select {col} from {self.m.table(ent)} where id={_qv(rid)}")

    # ---- fixtures (D-024 cold start) --------------------------------------
    def clean(self):
        """Remove every record the runner made (its ids begin RUN_PREFIX) and the status chain's
        entries the application wrote for them. Run at the start of each scenario and once more
        when the run ends (METHOD-2026-09-25-01, item 15)."""
        for ent in self.m.entities:
            try:
                _sql(self.db, f"delete from {self.m.table(ent)} where id like '{RUN_PREFIX}%'")
            except RuntimeError:
                pass                                    # config entity — no app_fd_ table
        if any(self.m.lifecycle(ent) for ent in self.m.entities):
            try:
                _sql(self.db, f"delete from {STATUS_EVENT_TABLE} where c_caseId like '{RUN_PREFIX}%'")
            except RuntimeError:
                pass                                    # no move made yet — no chain table

    def build_fixture(self, fx: dict, sid: str, ids: dict):
        for rec in fx.get("records", []):
            ent, alias = rec["entity"], rec.get("alias", rec["entity"])
            rid = f"{RUN_PREFIX}{RUN_TOKEN}-{sid}-{alias}"
            ids[alias] = rid
            form = rec.get("form") or self.m.create_form(ent)
            vals = {}
            for k, v in (rec.get("values") or {}).items():
                vals[k] = ids.get(v[1:], v) if isinstance(v, str) and v.startswith("@") else v
            # create THROUGH the real form (values in the payload) so required-field validators
            # pass; a create-form guard sees count=0 for a first record and allows it.
            st, body = self.api.save(form, {"id": rid, **vals})
            if st != 200 or body.get("errors"):
                raise RuntimeError(f"fixture create {ent}/{alias}: HTTP {st} {body}")
            # then SQL-set the same values so engine-owned columns not on the form also land
            # (harness AS the upstream engine — the D-024 declared surrogate).
            sets = [f"c_{k}={_qv(v)}" for k, v in vals.items()]
            if sets:
                _sql(self.db, f"update {self.m.table(ent)} set {', '.join(sets)} where id={_qv(rid)}")
            target = rec.get("state")
            if target:
                for tid in self.m.path_to(ent, target):
                    self.transition(ent, rid, tid)
            if self.m.lifecycle(ent):
                got, want = (self._col(ent, rid, self.m.state_column(ent)),
                             target or self.m.initial_state(ent))
                if got != want:
                    raise RuntimeError(f"fixture state {ent}/{alias}: wanted {want}, got '{got}'")
            self.say(f"    fixture {alias} = {ent}" + (f" @ {target}" if target else ""))

    # ---- the engine path ---------------------------------------------------
    def transition(self, ent, rid, tid) -> str:
        st, body = self.api.save(self.m.events_form(ent), {"id": rid, "lc_action": tid})
        if st != 200:
            raise RuntimeError(f"transition {tid} on {ent}/{rid}: HTTP {st} {body}")
        res = self._col(ent, rid, "c_transition_result")
        if not (res or "").startswith("OK"):
            raise RuntimeError(f"transition {tid} on {ent}/{rid}: {res or '(no result)'}")
        return res

    # ---- when actions ------------------------------------------------------
    def do_when(self, step: dict, ids: dict, sid: str = "w") -> dict:
        act = step.get("action")
        if act == "submit_form":
            form = step["form"]
            payload = {}
            for k, v in (step.get("values") or {}).items():
                payload[k] = ids.get(v[1:], v) if isinstance(v, str) and v.startswith("@") else v
            alias = step.get("alias")
            if step.get("on"):
                payload["id"] = ids.get(step["on"], step["on"])
            elif alias:
                # an accepted create gets an SCN-scoped id so clean() reclaims it across runs
                # (D-024) and later `then` clauses can reference it (the Appendix-E alias).
                payload["id"] = f"{RUN_PREFIX}{RUN_TOKEN}-{sid}-{alias}"
            st, body = self.api.save(form, payload)
            errs = body.get("errors") or {}
            self.say(f"    when submit_form {form}: HTTP {st} errors={list(errs.keys()) or 'none'}")
            if alias and st == 200 and not errs:
                ids[alias] = payload.get("id") or body.get("id")
            return {"status": st, "errors": errs, "body": body}
        if act == "execute_transition":
            ent, rid = step["entity"], ids[step["on"]]
            if step.get("expect") == "refused":
                # tolerate a guard refusal: a refused move leaves the status unchanged and
                # writes a non-OK result — the `then` clause asserts the block held.
                st, body = self.api.save(self.m.events_form(ent), {"id": rid, "lc_action": step["transition"]})
                res = self._col(ent, rid, "c_transition_result")
                refused = not (res or "").startswith("OK")
                self.say(f"    when {step['transition']} (expect refused): {res or '(none)'}  {'refused OK' if refused else 'ACCEPTED'}")
                return {"transition_result": res, "refused": refused}
            res = self.transition(ent, rid, step["transition"])
            self.say(f"    when {step['transition']}: {res}")
            return {"transition_result": res}
        if act == "run_component":
            ent, rid = step["entity"], ids[step["on"]]
            sets = ", ".join(f"c_{k}={_qv(v)}" for k, v in (step.get("values") or {}).items())
            if sets:
                _sql(self.db, f"update {self.m.table(ent)} set {sets} where id={_qv(rid)}")
            self.say(f"    when [{step.get('component','component')} surrogate] {ent}: {step.get('values', {})}")
            return {}
        if act == "complete_activity":
            # SURROGATE, and labelled as one: this drives the LIFECYCLE the model says the
            # outcome fires, not the workflow engine's assignment queue. A project engine
            # wired through KIT_TEST_CMD completes the real assignment; the kit's own runner
            # asserts that the declared outcome->transition mapping holds and that the
            # activity form's validation stands in the way when it should.
            ent, form, tid = self.m.activity_outcome(step["process"], step["activity"],
                                                     step["outcome"])
            rid = ids[step["on"]]
            vals = step.get("values")
            if vals is not None:
                # the activity form is submitted first, so a required field left empty
                # fails HERE — which is what `assert validation_error` is looking for
                # completing an activity WITH an outcome means the form is submitted carrying
                # it — without that the form's conditional validations cannot fire
                payload = {"id": rid, "lc_action": tid}
                payload.update({k: ("" if v is None else v) for k, v in vals.items()})
                st, body = self.api.save(form, payload)
                errs = body.get("errors") or {}
                self.say(f"    when [activity surrogate] {step['activity']}/{step['outcome']} "
                         f"submit {form}: HTTP {st} errors={list(errs.keys()) or 'none'}")
                if errs:
                    # the outcome is blocked; the transition must NOT fire
                    return {"status": st, "errors": errs, "body": body}
            res = self.transition(ent, rid, tid)
            self.say(f"    when [activity surrogate] {step['activity']}/{step['outcome']} "
                     f"-> {tid}: {res}")
            return {"transition_result": res}
        raise RuntimeError(f"unsupported when action {act!r}")

    # ---- then asserts ------------------------------------------------------
    def do_then(self, a: dict, ids: dict, last: dict):
        kind = a.get("assert")
        if kind == "validation_error":
            errs = (last or {}).get("errors") or {}
            if not errs:
                raise RuntimeError("assert validation_error: submit was ACCEPTED (no errors)")
            self.say(f"    then validation_error: refused ({', '.join(errs.keys())})  ✓")
            return
        if kind == "entity_state":
            ent, rid, want = a["entity"], ids[a["on"]], a["state"]
            got = self._col(ent, rid, self.m.state_column(ent))
            if got != want:
                raise RuntimeError(f"assert entity_state: wanted {want}, got '{got}'")
            self.say(f"    then {ent} state = {got}  ✓")
            return
        if kind == "field_value":
            ent, rid = a["entity"], ids[a["on"]]
            got = self._col(ent, rid, f"c_{a['attr']}")
            if str(got) != str(a.get("equals")):
                raise RuntimeError(f"assert field_value {a['attr']}: wanted {a.get('equals')!r}, got '{got}'")
            self.say(f"    then {ent}.{a['attr']} = {got}  ✓")
            return
        if kind == "record_count":
            ent = a["entity"]
            conds = []
            # `scope: run` counts only what THIS run created. A bare count over a shared
            # instance asserts that nobody has ever touched the app by hand, which is not a
            # property of the system under test — it is a property of who used the browser
            # last. Found 2026-08-02: driving the UI to prove the screens work broke t10 and
            # t15, and the honest reading is that the scenarios meant "one for this run".
            if a.get("scope") == "run":
                conds.append(f"id like '{RUN_PREFIX}{RUN_TOKEN}-%'")
            for k, v in (a.get("where") or {}).items():
                if isinstance(v, str) and v.startswith("!"):
                    conds.append(f"c_{k} <> {_qv(v[1:])}")
                else:
                    conds.append(f"c_{k} = {_qv(v)}")
            where = (" where " + " and ".join(conds)) if conds else ""
            got = int(_sql(self.db, f"select count(*) from {self.m.table(ent)}{where}") or "0")
            want = int(a.get("equals", 0))
            if got != want:
                raise RuntimeError(f"assert record_count {ent}: wanted {want}, got {got}")
            self.say(f"    then count({ent}{where}) = {got}  ✓")
            return
        if kind == "custom_sql":
            got = _sql(self.db, a["sql"])
            want = str(a.get("equals", ""))
            if str(got) != want:
                raise RuntimeError(f"assert custom_sql: wanted {want!r}, got '{got}'")
            self.say(f"    then custom_sql = {got}  ✓")
            return
        if kind == "distinct":
            ent, attr = a["entity"], a["attr"]
            vals = [self._col(ent, ids[al], f"c_{attr}") for al in a["of"]]
            if any(v is None or str(v) == "" for v in vals):
                raise RuntimeError(f"assert distinct {ent}.{attr}: an empty value ({vals})")
            if len(set(vals)) != len(vals):
                raise RuntimeError(f"assert distinct {ent}.{attr}: values collide ({vals})")
            self.say(f"    then distinct {ent}.{attr} = {vals}  OK")
            return
        raise RuntimeError(f"unsupported then assert {kind!r}")

    # ---- one scenario ------------------------------------------------------
    def run_scenario(self, sc: dict) -> tuple[bool, str]:
        sid = sc["id"]
        self.say(f"  {sid} — {sc.get('name', '')}")
        self.clean()
        ids, last, t0 = {}, {}, time.time()
        try:
            fixture_id = (sc.get("given") or {}).get("fixture")
            if fixture_id:
                self.build_fixture(self.m.fixtures[fixture_id], sid, ids)
            for step in sc.get("when", []):
                last = self.do_when(step, ids, sid)
            for a in sc.get("then", []):
                self.do_then(a, ids, last)
            self.say(f"  PASS ({time.time()-t0:.1f}s)")
            return True, ""
        except Exception as e:   # noqa: BLE001 — a failing scenario is a normal, publishable outcome
            self.say(f"  FAIL — {e}")
            return False, str(e)


# ----------------------------------------------------------------------- cli
def _api_key(app_id: str, arg: str | None) -> str:
    if arg:
        return arg
    for var in (f"KIT_API_KEY_{app_id}", "KIT_API_KEY"):
        if os.environ.get(var):
            return os.environ[var]
    sys.exit(f"run_suite.py: no data-API key — set KIT_API_KEY_{app_id} to the key bound on the "
             f"server, or pass --api-key (tools/register_api_key.py {app_id} --instance <name> "
             f"binds the key that variable holds)")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("app", type=Path)
    ap.add_argument("--instance", required=True)
    ap.add_argument("--instances", default=os.environ.get("JOGET_INSTANCES", "~/.joget/instances.yaml"))
    ap.add_argument("--api-key")
    ap.add_argument("--feature", help="run only scenarios whose feature matches")
    ap.add_argument("--out", type=Path, help="machine result file (default: design/acceptance-result.yaml "
                                             "beside the model, where the gate report reads it)")
    a = ap.parse_args()

    if not a.app.exists():
        sys.exit(f"run_suite.py: app not found: {a.app}")
    model = Model(a.app)
    inst, base = dep.load_instance(a.instance, a.instances)
    api = Api(base, f"API-{model.app_id}-data", _api_key(model.app_id, a.api_key))
    db = Db.of(inst)

    scenarios = [s for s in model.scenarios if not a.feature or s.get("feature") == a.feature]
    r = Runner(model, api, db)
    r.say(f"{model.app_id} acceptance — {len(scenarios)} scenario(s) against {base} "
          f"(data API API-{model.app_id}-data; deployed FormService path)")
    try:
        results = [(s["id"], s.get("name", ""), s.get("feature"), *r.run_scenario(s))
                   for s in scenarios]
    finally:
        # each scenario cleans at its start, so without this the last one's records, and the
        # status entries the application made for them, stay on the instance (item 15)
        r.clean()
        r.say("cleaned: the runner's records and their status entries removed")
    passed = sum(1 for x in results if x[3])
    r.say(f"RESULT: {passed}/{len(results)} passed")

    out = a.out or (a.app.parent / "design" / "acceptance-result.yaml")
    out.parent.mkdir(parents=True, exist_ok=True)
    result = {"acceptance_result": {
        "app": model.app_id, "instance": a.instance,
        "model_sha256": hashlib.sha256(a.app.read_bytes()).hexdigest(),
        "ran_at": _dt.datetime.now().isoformat(timespec="seconds"),
        "run_token": RUN_TOKEN, "feature": a.feature,
        "total": len(results), "passed": passed, "exit": 0 if passed == len(results) else 1,
        "cases": [{"id": sid, "name": nm, "feature": ft, "passed": ok, "note": note}
                  for sid, nm, ft, ok, note in results],
    }}
    out.write_text("# Computed by `kit test` (run_suite.py) — behavioural evidence for the gate-report.\n"
                   + yaml.safe_dump(result, sort_keys=False, allow_unicode=True), encoding="utf-8", newline="\n")
    print(f"result -> {out}")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
