#!/usr/bin/env python3
"""Validate a Joget application-model document.

Two layers, matching the validation-layering design:
  1. Structural validation against application-model.schema.yaml (JSON Schema 2020-12).
  2. Cross-reference lint (L-rules) that JSON Schema cannot express.

Platform-delta rules (D-series, keyed on app.platform) run as a third layer:
model predicates that fire only when the model's platform matches, each citing its
register D-id (rules/JOGET-PLATFORM-DELTAS.md). Severity: error blocks generation
(joins exit 2), warn reports (does not change the exit code).

Before all of them runs rule L021, the interaction design gate (SDD-11, section 8;
METHOD-2026-09-25-12): the model must name, in `model.interaction_design`, the interaction design
the owner accepted, by its path and SHA-256 checksum, and agree with it. It is an error in every
custody mode and nothing turns it off; `kit gen`, `build_app.py` and the deploy run the same
function first (`admit_or_refuse`). See the section of this file headed L021.

After all of them, on a model every layer above admits, runs the projection layer (ADR-107):
every projector of `kit gen all` is tried over the model in a folder of its own
(tools/projection_trial.py), and each refusal a projector prints is an error, in the projector's
own words. A model this validator admits is a model `kit gen` generates.

Usage:
    validate.py <app.yaml> [--schema <schema.yaml>]

Exit codes: 0 valid (warnings allowed) · 1 schema errors · 2 lint / delta / contract errors, the
interaction design gate refusing, or a projector refusing.
"""
from __future__ import annotations

import argparse
import datetime
import pathlib
import re
import sys
import uuid

import yaml
from jsonschema import Draft202012Validator

HERE = pathlib.Path(__file__).resolve().parent
DEFAULT_SCHEMA = HERE.parent / "application-model.schema.yaml"
DEFAULT_MIRROR = HERE.parent / "contracts" / "registry-mirror.yaml"
ROLE_RE = re.compile(r"^role:([a-z][a-z0-9_]*)$")
SECRET_KEY_RE = re.compile(r"(api[_-]?key|secret|password|token|credential)", re.I)
ENV_REF_RE = re.compile(r"^\$\{env:[A-Z0-9_]+\}$")


def load(path: pathlib.Path):
    with open(path, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


# ---- a seeded row's identifier (project_seed.py) and the key a reference to it is read by ----
# Fixed namespace so a row's id is stable across runs and machines (idempotent load).
SEED_NS = uuid.UUID("6b6e5b8a-0000-4a00-8000-5eed5eed5eed")


def seed_row_id(eid: str, ent: dict, row: dict, i: int) -> str:
    """The deterministic identifier project_seed gives row `i` of entity `eid`'s seed: uuid5 of
    the entity and the row's unique attribute (its position when the entity has none)."""
    key = next((a["id"] for a in ent.get("attributes", []) if a.get("unique")), None)
    seed_key = row.get(key) if key else str(i)
    return str(uuid.uuid5(SEED_NS, f"{eid}:{seed_key}"))


def seed_rows(doc: dict, extra: list | None = None) -> dict:
    """entity id -> [(row id, row)] for every inline seed row of the model (and `extra` entries,
    a fixture's, in the same shape)."""
    ents = {e["id"]: e for e in doc.get("entities", [])}
    out: dict = {}
    for entry in list(doc.get("seed") or []) + list(extra or []):
        ent = ents.get(entry.get("entity"))
        if not ent:
            continue
        for i, row in enumerate(entry.get("rows") or []):
            out.setdefault(ent["id"], []).append((seed_row_id(ent["id"], ent, row, i), row))
    return out


def ref_key(target: dict) -> str | None:
    """The key a reference to `target` is stored under: the column its look-up reads
    (project_forms._lookup_for_ref) — the target's business key `pk.attr`, or None for the row's
    own identifier."""
    return (target.get("pk") or {}).get("attr") or None


def seed_ref_value(target_id: str, target: dict, rows: list, value):
    """The value a seeded reference to `target` must hold, given the value the model wrote: the
    look-up's key of the row it names (METHOD-2026-09-25-04, item 6; row 15). The model may name
    the row by that key, by its seeded row identifier, or — when the look-up reads the row
    identifier — by the row's unique attribute. None when it names no seeded row."""
    v = str(value)
    key = ref_key(target)
    uniq = next((a["id"] for a in target.get("attributes", []) if a.get("unique")), None)
    for rid, row in rows:
        if key:
            if str(row.get(key)) == v or rid == v:
                return row.get(key)
        elif rid == v or (uniq and str(row.get(uniq)) == v):
            return rid
    return None


# The names a query gives its columns: `... AS <name>` (METHOD-2026-09-28-07: a query that is a
# view names so each column a search reads, and a list's act names a column of its query so).
_AS_NAME = re.compile(r"\bAS\s+\"?([A-Za-z_][A-Za-z0-9_]*)\"?", re.I)


def query_columns(q: dict) -> list:
    """The column names a model's query gives with AS, in order, once each."""
    out: list = []
    for n in _AS_NAME.findall(str((q or {}).get("sql") or "")):
        if n not in out:
            out.append(n)
    return out


# ---- the records a list's acts carry (METHOD-2026-09-28-07, the kit's gaps G1 and G2) ----------
def chosen_act(doc: dict, act_id) -> tuple:
    """(the act on chosen rows whose `id` is `act_id`, the list it is taken on), or (None, None)."""
    for lst in doc.get("lists") or []:
        for ca in lst.get("chosen_actions") or []:
            if act_id and ca.get("id") == act_id:
                return ca, lst
    return None, None


def list_record_entity(lst: dict, doc: dict):
    """The entity whose records a list's rows are: its source entity; for a list sourced from an
    act on chosen rows, the entity whose records the act carries (row_act_carries over the list
    it is taken on); None for a query."""
    src = lst.get("source") or {}
    if src.get("entity"):
        return src["entity"]
    if src.get("act"):
        ca, acted = chosen_act(doc, src["act"])
        return row_act_carries(ca, acted, doc) if ca is not None and acted is not lst else None
    return None


def row_act_carries(act: dict, lst: dict, doc: dict):
    """The entity whose record a list's act carries: its `carries`; else the entity the row's
    attribute `record` refers to; else the row's own entity (None on a query list)."""
    if act.get("carries"):
        return act["carries"]
    eid = list_record_entity(lst, doc)
    rec = act.get("record")
    if rec and eid:
        ent = next((e for e in doc.get("entities") or [] if e.get("id") == eid), {}) or {}
        a = next((x for x in ent.get("attributes") or [] if x.get("id") == rec), {}) or {}
        if a.get("type") == "ref":
            return (a.get("ref") or {}).get("entity")
    return eid


# ---- the hash variables a list's first-paint scope may name (METHOD-2026-09-25-04, item 6) ----
SCOPE_HASH = re.compile(r"#([^#\s']+)#")
SCOPE_ADMITTED = re.compile(r"^(currentUser\.username|requestParam\.[A-Za-z_]\w*)(\?sql)?$")


def schema_version(schema: dict | None = None) -> str:
    """The single source of the current schema version — the const the model must pin.
    Callers (scaffold, test oracles) read this instead of hardcoding, so a bump is one edit."""
    schema = schema if schema is not None else load(DEFAULT_SCHEMA)
    return schema["properties"]["model"]["properties"]["schema_version"]["const"]


def schema_errors(schema: dict, doc: dict) -> list[str]:
    v = Draft202012Validator(schema)
    out = []
    for e in sorted(v.iter_errors(doc), key=lambda e: list(e.absolute_path)):
        loc = "/".join(str(p) for p in e.absolute_path) or "<root>"
        out.append(f"{loc}: {e.message}")
    return out


# --------------------------------------------------------------------------- #
# DD-01 — domain data dictionary (dd) loading + the semantic->control contract  #
# --------------------------------------------------------------------------- #
# The dd classifies every governed set by `kind`; the kind DRIVES the control the
# projector emits and the M-series gate enforces. One source of truth, shared by
# validate (the authoring gate) and project_forms (the derivation).
DD_KIND_CONTROL = {
    "typed.period":   "period_picker",   # the concrete W-12 fix: never a text field
    "md.registry":    "smart_search",    # partial-knowledge search -> ranked pick (owner-corrected)
    "md.directory":   "select",          # UserOptionsBinder via users: config
    "md.lookup":      "select",           # over the md_ entity
    "md.vocabulary":  "select",
    "typed.money":    "number",
    "typed.duration": "number",
}
# kinds for which a plain free-text primitive is a HARD authoring error (M-02 error tier).
DD_FREETYPE_FORBIDDEN_HARD = {"typed.period"}

def load_dd(doc: dict, app_path) -> dict:
    """Load the domain data dictionary named by model.dd_ref (relative to the app
    file). Returns {} when absent — the M-gate is then advisory-off. Never raises on
    a missing file; a broken dd_ref surfaces as an M-00 lint error instead."""
    ref = doc.get("dd_ref")
    if not ref or app_path is None:
        return {}
    try:
        dd_path = pathlib.Path(app_path).resolve().parent / ref
        return load(dd_path)
    except Exception:
        return {"__error__": str(ref)}

def dd_control_for(dd: dict, semantic: str):
    """Given a `dd:<id>` semantic, return (kind, control) from the dd, or (None, None)."""
    if not dd or not semantic or not semantic.startswith("dd:"):
        return None, None
    sid = semantic[3:]
    for st in dd.get("sets", []):
        if st.get("id") == sid:
            k = st.get("kind", "")
            return k, DD_KIND_CONTROL.get(k)
    return None, None


class Lint:
    def __init__(self, doc: dict, app_path=None):
        self.doc = doc
        self.errors: list[str] = []
        self.warnings: list[str] = []
        # ---- indexes -------------------------------------------------------
        self.entities = {e["id"]: e for e in doc.get("entities", [])}
        self.attrs = {eid: {a["id"] for a in e.get("attributes", [])}
                      for eid, e in self.entities.items()}
        self.vocabs = {v["id"] for v in doc.get("vocabularies", [])}
        self.roles = {r["id"] for r in doc.get("roles", [])}
        self.features = {f["id"] for f in doc.get("features", [])}
        self.requirements = {r["id"] for r in doc.get("requirements", [])}
        self.catalog = {c["component"] for c in doc.get("catalog", [])}
        self.forms = {f["id"]: f for f in doc.get("forms", [])}
        self.lists = {l["id"]: l for l in doc.get("lists", [])}
        self.queries = {q["id"]: q for q in doc.get("queries", [])}
        self.dashboards = {d["id"] for d in doc.get("dashboards", [])}
        self.reports = {r["id"] for r in doc.get("reports", [])}
        self.processes = {p["id"]: p for p in doc.get("processes", [])}
        self.fixtures = {f["id"]: f for f in
                         doc.get("acceptance", {}).get("fixtures", [])}
        # ---- DD-01: domain data dictionary (advisory-off when no dd_ref) ----
        self.app_path = app_path
        self.dd = load_dd(doc, app_path)
        self.dd_sets = {st["id"]: st for st in self.dd.get("sets", [])}
        # last-segment index for the M-02 name match (tax_period -> 'period')
        self.dd_by_tail = {}
        for sid in self.dd_sets:
            self.dd_by_tail.setdefault(sid.split("_")[-1], sid)
        # ---- CH-01 custody mode (WP-F): the sibling .kit.yaml drives U-series severity.
        # required => U-rules are errors (fail closed); stamp/absent => warnings (visible,
        # non-blocking — ADR-069 DP-2). Read exactly as build_app / gate_report do.
        self.custody_mode = "stamp"
        if app_path:
            ky = pathlib.Path(app_path).parent / ".kit.yaml"
            if ky.is_file():
                try:
                    self.custody_mode = (yaml.safe_load(ky.read_text()) or {}).get("custody", "stamp")
                except Exception:
                    self.custody_mode = "stamp"

    def err(self, rule: str, path: str, msg: str):
        self.errors.append(f"[{rule}] {path}: {msg}")

    def warn(self, rule: str, path: str, msg: str):
        self.warnings.append(f"[{rule}] {path}: {msg}")

    def _u(self, rule: str, path: str, msg: str):
        # WP-F: U-series requiredness is posture-driven (ADR-071) — an error in a
        # custody:required app, a visible warning in a stamp app.
        (self.err if self.custody_mode == "required" else self.warn)(rule, path, msg)

    def _operational(self, e: dict) -> bool:
        # UX-01 §3 / IDR-05: operational = unbounded, grows with operations. An explicit
        # scale wins; otherwise a lifecycle-bearing entity is operational by default.
        e = e or {}
        if e.get("scale"):
            return e["scale"] == "operational"
        return bool(e.get("lifecycle"))

    # ---- rule helpers -----------------------------------------------------
    def _entity(self, rule, path, eid):
        if eid not in self.entities:
            self.err(rule, path, f"unknown entity '{eid}'")
            return None
        return self.entities[eid]

    def _attr(self, rule, path, eid, aid):
        if eid in self.attrs and aid not in self.attrs[eid]:
            self.err(rule, path, f"attribute '{aid}' not defined on entity '{eid}'")

    def _role(self, rule, path, rid):
        if rid not in self.roles:
            self.err(rule, path, f"unknown role '{rid}'")

    def _feature(self, rule, path, obj):
        f = obj.get("feature")
        if f and f not in self.features:
            self.err(rule, path, f"unknown feature '{f}'")

    def _component(self, rule, path, cid):
        if cid and cid not in self.catalog:
            self.err(rule, path, f"component '{cid}' not declared in catalog")

    def _lifecycle(self, eid):
        e = self.entities.get(eid) or {}
        return e.get("lifecycle") or {}

    # ---- rules ------------------------------------------------------------
    def l001_unique_ids(self):
        for coll, key in [("entities", "id"), ("forms", "id"), ("lists", "id"),
                          ("vocabularies", "id"), ("roles", "id"), ("features", "id"),
                          ("requirements", "id"), ("processes", "id"), ("queries", "id"),
                          ("dashboards", "id"), ("reports", "id"),
                          ("bespoke_plugins", "id")]:
            seen = set()
            for i, item in enumerate(self.doc.get(coll, [])):
                v = item.get(key)
                if v in seen:
                    self.err("L001", f"{coll}[{i}]", f"duplicate id '{v}'")
                seen.add(v)
        seen = set()
        for i, s in enumerate(self.doc.get("acceptance", {}).get("scenarios", [])):
            if s["id"] in seen:
                self.err("L001", f"acceptance/scenarios[{i}]", f"duplicate id '{s['id']}'")
            seen.add(s["id"])

    def l002_l003_entities_and_attrs(self):
        for eid, e in self.entities.items():
            p = f"entities/{eid}"
            parent = e.get("parent")
            union = e.get("parent_union")
            if e.get("kind") in ("child", "junction") and not parent and not union:
                self.err("L002", p, "kind child/junction requires parent or parent_union")
            if parent and union:
                self.err("L002", p, "parent and parent_union are mutually exclusive (ADR-091)")
            if parent:
                pe = self._entity("L002", f"{p}/parent", parent["entity"])
                self._attr("L003", f"{p}/parent", eid, parent["fk_attr"])
            if union:
                up = f"{p}/parent_union"
                self._attr("L003", up, eid, union["discriminator"])
                self._attr("L003", up, eid, union["fk_attr"])
                seen = {}
                for i, mem in enumerate(union.get("members", [])):
                    self._entity("L002", f"{up}/members/{i}", mem["entity"])
                    if mem["when"] in seen:
                        self.err("L002", f"{up}/members/{i}",
                                 f"discriminator value '{mem['when']}' already maps to "
                                 f"'{seen[mem['when']]}' — a value selects at most one member")
                    seen[mem["when"]] = mem["entity"]
                # where the discriminator binds a vocabulary, every `when` must be one of its codes
                disc = next((a for a in e.get("attributes", [])
                             if a["id"] == union["discriminator"]), None)
                if disc and disc.get("type") == "enum":
                    voc = next((v for v in self.doc.get("vocabularies", [])
                                if v["id"] == disc.get("vocabulary")), None)
                    if voc:
                        codes = {r["code"] for r in (voc.get("rows") or [])}
                        for i, mem in enumerate(union.get("members", [])):
                            if mem["when"] not in codes:
                                self.err("L004", f"{up}/members/{i}",
                                         f"discriminator value '{mem['when']}' is not a code of "
                                         f"vocabulary '{disc.get('vocabulary')}'")
            pk = e.get("pk", {})
            if pk.get("attr"):
                self._attr("L003", f"{p}/pk", eid, pk["attr"])
            for a in e.get("attributes", []):
                ap = f"{p}/attributes/{a['id']}"
                if a["type"] == "enum" and a.get("vocabulary") not in self.vocabs:
                    self.err("L004", ap, f"unknown vocabulary '{a.get('vocabulary')}'")
                if a["type"] == "ref":
                    te = self._entity("L002", ap, a["ref"]["entity"])
                    if te and a["ref"].get("display"):
                        self._attr("L003", ap, a["ref"]["entity"], a["ref"]["display"])
            lc = e.get("lifecycle")
            if lc:
                self._attr("L003", f"{p}/lifecycle", eid, lc["status_attr"])
                if lc.get("engine", "status_framework") == "status_framework":
                    self._component("L007", f"{p}/lifecycle", "status-framework")

    def l004_vocab_parents(self):
        for v in self.doc.get("vocabularies", []):
            par = v.get("parent")
            if par and par not in self.vocabs:
                self.err("L004", f"vocabularies/{v['id']}", f"unknown parent vocabulary '{par}'")

    def l017_bound_vocabulary_values(self):
        """L017 (METHOD-2026-09-25-02): a vocabulary an attribute binds must carry its values —
        `rows`, or a `file` to load them from. With neither it deploys as an empty drop-down,
        whether the application maintains the list or carries it inline. Also: a list's
        `maintained_by` must name a declared role (L006), or its administration entry would be
        visible to no one."""
        binders: dict = {}
        for e in self.doc.get("entities", []):
            for a in e.get("attributes", []):
                if a.get("vocabulary"):
                    binders.setdefault(a["vocabulary"], f"entities/{e.get('id')}/attributes/{a.get('id')}")
        for v in self.doc.get("vocabularies", []):
            p = f"vocabularies/{v.get('id')}"
            if v.get("id") in binders and not v.get("rows") and not v.get("file"):
                self.err("L017", p, f"bound by {binders[v['id']]} but has no rows and no file — "
                                    f"it would deploy as an empty drop-down; give it its values")
            if v.get("maintained_by"):
                self._role("L006", f"{p}/maintained_by", v["maintained_by"])
        for e in self.doc.get("entities", []):
            if e.get("maintained_by"):
                self._role("L006", f"entities/{e.get('id')}/maintained_by", e["maintained_by"])

    def l018_acts(self):
        """L018 (METHOD-2026-09-25-04, item 3): every act a form declares resolves in the model —
        a move is a move a person makes on the form's own record (a user-triggered transition of
        its entity that names its roles, which is what gets a trigger form and a guard); a form
        act opens a form of the model and carries a record the form can name. An act that
        resolves nowhere would be a button leading nowhere. Error in every custody mode."""
        for fid, f in self.forms.items():
            ent = self.entities.get(f.get("entity") or "") or {}
            lc = ent.get("lifecycle") or {}
            moves = {t["id"] for t in lc.get("transitions", [])
                     if t.get("trigger", "user") == "user" and t.get("roles")}
            attrs = {a["id"]: a for a in ent.get("attributes", [])}
            placed = {x.get("attr") for s in f.get("sections", []) for x in s.get("fields", [])}
            for i, a in enumerate(f.get("acts") or []):
                p = f"forms/{fid}/acts/{i}"
                for r in a.get("roles", []):
                    self._role("L006", p, r)
                if a.get("transition"):
                    if a["transition"] not in moves:
                        self.err("L018", p,
                                 f"act '{a.get('label')}' makes the move '{a['transition']}', which "
                                 f"is not a move a person makes on '{ent.get('id')}' — a "
                                 f"user-triggered transition of the form's own entity that names "
                                 f"its roles (have: {sorted(moves) or 'none'})")
                    continue
                target = self.forms.get(a.get("form"))
                if target is None:
                    self.err("L018", p, f"act '{a.get('label')}' opens form '{a.get('form')}', "
                                        f"which is not in the model")
                    continue
                carries = a.get("carries") or ent.get("id")
                if carries not in self.entities:
                    self.err("L018", p, f"act '{a.get('label')}' carries a record of "
                                        f"'{carries}', which is not an entity of the model")
                elif carries != ent.get("id") and not any(
                        (attrs.get(x) or {}).get("type") == "ref"
                        and ((attrs.get(x) or {}).get("ref") or {}).get("entity") == carries
                        for x in placed):
                    self.err("L018", p, f"act '{a.get('label')}' carries a record of "
                                        f"'{carries}', and form '{fid}' shows no field that "
                                        f"refers to one — there is nothing on the page to carry")

    def l018_acts_on_records(self):
        """L018, continued (METHOD-2026-09-28-07, the kit's gaps G1 and G2): the acts the schema
        now states resolve in the model, as every act does.

        A list's row act that names the record it carries (`record`) names a column of the row —
        an attribute of the list's entity, or a column of its query — and on a query, whose
        columns name no entity, the entity it carries (`carries`); an act that opens a list names
        a list of the model and the address parameter it reads (`param`). An act on the rows
        chosen has a name no other such act has, opens a form of the model, and names the field
        of that form that receives the chosen records (`param`), which the form places. A list
        sourced from an act (`source.act`) names an act on chosen rows of a list sourced from an
        entity, and shows attributes of that entity. A form's act that stands on a value
        (`stands_on`) names a field the form places."""
        doc = self.doc
        names: dict = {}
        for lid, l in self.lists.items():
            src = l.get("source") or {}
            eid = list_record_entity(l, doc)
            q = self.queries.get(src.get("query") or "")
            cols = (({c.get("expr") for c in l.get("columns", []) if c.get("expr")}
                     | set(query_columns(q))) if q else set())
            attrs = {a["id"] for a in (self.entities.get(eid or "") or {}).get("attributes", [])}

            def column(p, rec, what):
                if rec is None:
                    return
                if q is not None and rec not in cols:
                    self.err("L018", p, f"{what} names the column '{rec}', which the list's query "
                                        f"'{src.get('query')}' does not give (an `expr` of the "
                                        f"list, or a name its SQL gives with AS)")
                elif q is None and eid and rec not in attrs:
                    self.err("L018", p, f"{what} names the column '{rec}', which is no attribute "
                                        f"of '{eid}', the record of the list's rows")

            for i, a in enumerate(l.get("actions") or []):
                p = f"lists/{lid}/actions/{i}"
                if a.get("type") not in ("open_form", "open_list"):
                    continue
                if a.get("type") == "open_list":
                    if a.get("list") not in self.lists:
                        self.err("L018", p, f"the act '{a.get('label')}' opens the list "
                                            f"'{a.get('list')}', which is not a list of the model")
                    if not a.get("param"):
                        self.err("L018", p, f"the act '{a.get('label')}' opens a list and names no "
                                            f"`param`, the address parameter that list reads")
                column(p, a.get("record"), f"the act '{a.get('label')}'")
                if a.get("carries") and a["carries"] not in self.entities:
                    self.err("L018", p, f"the act '{a.get('label')}' carries a record of "
                                        f"'{a['carries']}', which is not an entity of the model")
                if q is not None and a.get("record") and not a.get("carries"):
                    self.err("L018", p, f"the act '{a.get('label')}' carries the record the column "
                                        f"'{a['record']}' names, on a list sourced from a query, "
                                        f"whose columns name no entity — name it (`carries`)")
            for i, ca in enumerate(l.get("chosen_actions") or []):
                p = f"lists/{lid}/chosen_actions/{i}"
                if ca.get("id") in names:
                    self.err("L018", p, f"the act on chosen rows '{ca.get('id')}' is named twice "
                                        f"(also on {names[ca['id']]})")
                names.setdefault(ca.get("id"), f"lists/{lid}")
                for r in ca.get("roles", []):
                    self._role("L006", p, r)
                target = self.forms.get(ca.get("form"))
                if target is None:
                    self.err("L018", p, f"the act '{ca.get('label')}' opens form "
                                        f"'{ca.get('form')}', which is not in the model")
                else:
                    placed = {x.get("attr") or x.get("id") for s in target.get("sections", [])
                              for x in s.get("fields", [])}
                    if ca.get("param") not in placed:
                        self.err("L018", p, f"the act '{ca.get('label')}' carries the chosen "
                                            f"records in '{ca.get('param')}', which form "
                                            f"'{ca['form']}' does not place")
                column(p, ca.get("record"), f"the act '{ca.get('label')}'")
                if ca.get("carries") and ca["carries"] not in self.entities:
                    self.err("L018", p, f"the act '{ca.get('label')}' carries records of "
                                        f"'{ca['carries']}', which is not an entity of the model")
                if q is not None and not (ca.get("record") and ca.get("carries")):
                    self.err("L018", p, f"the act '{ca.get('label')}' is taken on the rows of a list "
                                        f"sourced from a query, whose columns name no entity — name "
                                        f"the column that holds each chosen record's key (`record`) "
                                        f"and the entity (`carries`)")
            if src.get("act"):
                p = f"lists/{lid}/source"
                ca, acted = chosen_act(doc, src["act"])
                if ca is None:
                    self.err("L018", p, f"the list is sourced from the act '{src['act']}', which "
                                        f"is no act on chosen rows of the model (chosen_actions)")
                elif not eid:
                    self.err("L018", p, f"the list is sourced from the act '{src['act']}', taken "
                                        f"on the list '{acted.get('id')}', and the act names no "
                                        f"entity whose records it carries (`carries`); the records "
                                        f"it was taken on cannot be read")
                else:
                    for c in l.get("columns", []):
                        if c.get("attr") not in attrs:
                            self.err("L018", f"lists/{lid}/columns",
                                     f"'{c.get('attr') or c.get('expr')}' is no attribute of "
                                     f"'{eid}', whose records the act was taken on")
        for fid, f in self.forms.items():
            placed = {x.get("attr") or x.get("id") for s in f.get("sections", [])
                      for x in s.get("fields", [])}
            for i, a in enumerate(f.get("acts") or []):
                p = f"forms/{fid}/acts/{i}"
                if a.get("stands_on") and a["stands_on"] not in placed:
                    self.err("L018", p, f"act '{a.get('label')}' stands on the value "
                                        f"'{a['stands_on']}', which form '{fid}' does not place")

    def l019_seed_references(self):
        """L019 (METHOD-2026-09-25-04, item 6; row 15 of the analysis's table 7.3): a seeded
        reference is written under the key its look-up reads. The look-up over a reference reads
        the target's business key (`pk.attr`) when it has one and the row's identifier when it
        has none (project_forms._lookup_for_ref); the seed writes what the model gives it, and
        project_seed turns a row named by its seeded identifier into that key. This rule
        compares the two: every seeded reference must name a seeded row of its target by a key
        the seed can write it under, and every form's look-up over that reference must read the
        same key — else the drop-down shows the stored value as empty (section 2.5, "the
        empties"). Error in every custody mode."""
        rows = seed_rows(self.doc)
        file_seeded = {e.get("entity") for e in self.doc.get("seed") or [] if e.get("file")}
        for entry in self.doc.get("seed") or []:
            ent = self.entities.get(entry.get("entity"))
            if not ent:
                continue
            refs = {a["id"]: a for a in ent.get("attributes", []) if a.get("type") == "ref"}
            for i, row in enumerate(entry.get("rows") or []):
                for aid, a in refs.items():
                    v = row.get(aid)
                    if v in (None, ""):
                        continue
                    tid = (a.get("ref") or {}).get("entity")
                    tgt = self.entities.get(tid)
                    if not tgt or tid in file_seeded:
                        continue
                    if seed_ref_value(tid, tgt, rows.get(tid, []), v) is None:
                        key = ref_key(tgt) or "its row identifier"
                        self.err("L019", f"seed/{ent['id']}/rows/{i}/{aid}",
                                 f"'{v}' names no seeded row of '{tid}' — neither by the key "
                                 f"its look-up reads ({key}) nor by a seeded row's identifier")
        seeded_refs = {(e.get("entity"), aid) for e in self.doc.get("seed") or []
                       for r in e.get("rows") or [] for aid, v in r.items() if v not in (None, "")}
        for fid, f in self.forms.items():
            ent = self.entities.get(f.get("entity") or "") or {}
            attrs = {a["id"]: a for a in ent.get("attributes", [])}
            for sec in f.get("sections", []):
                for fld in sec.get("fields", []):
                    a = attrs.get(fld.get("attr") or "")
                    if not a or a.get("type") != "ref" or (ent.get("id"), a["id"]) not in seeded_refs:
                        continue
                    lk = (fld.get("config") or {}).get("lookup") or {}
                    if not lk.get("idColumn"):
                        continue
                    tgt = self.entities.get((a.get("ref") or {}).get("entity")) or {}
                    wrote = ref_key(tgt) or "id"
                    reads = str(lk["idColumn"]).removeprefix("c_")
                    if reads != wrote:
                        self.err("L019", f"forms/{fid}/{sec.get('id')}/{a['id']}",
                                 f"the look-up reads '{reads}' and the seed writes '{a['id']}' "
                                 f"under '{wrote}' — the seeded records would show empty")

    def l020_default_scope(self):
        """L020 (METHOD-2026-09-25-04, item 6; row 16): a list's first-paint scope names the
        person signed in (`#currentUser.username#`) and the record of the page
        (`#requestParam.<name>#`), and no other hash variable — the two the projector quotes and
        escapes for SQL (project_datalists). Error in every custody mode."""
        for lid, l in self.lists.items():
            scope = str(l.get("default_scope") or "")
            for tok in SCOPE_HASH.findall(scope):
                if not SCOPE_ADMITTED.match(tok):
                    self.err("L020", f"lists/{lid}/default_scope",
                             f"'#{tok}#' is not admitted — a first-paint scope names the person "
                             f"signed in (#currentUser.username#) or the page's record "
                             f"(#requestParam.<name>#)")

    def u026_long_lists(self):
        """U026 (UX-01 IDR-05, amended 25 September 2026 on the owner's word; METHOD-2026-09-25-04,
        item 7): no step of a selection offers more than nine values. Refused, in every custody
        mode: a list bound by an attribute with more than nine values in force and no `groups`; a
        category holding more than nine values; a list of more than nine categories; and a divided
        list whose categories cannot be read — `groups` naming no vocabulary, a row naming no
        category or one its categories do not hold, or either list `fixed` (a divided list and its
        categories are both lists the application maintains)."""
        import lov
        vocabs = {v["id"]: v for v in self.doc.get("vocabularies", [])}
        bound = {a.get("vocabulary") for e in self.entities.values()
                 for a in e.get("attributes", []) if a.get("type") == "enum"}

        def rows(v):
            try:
                return lov.rows_of(v, self.app_path)
            except lov.LovError:
                return list(v.get("rows") or [])

        most = lov.MOST
        for vid, v in vocabs.items():
            p = f"vocabularies/{vid}"
            rs = rows(v)
            g = v.get("groups")
            if not g:
                if vid in bound and len(rs) > most:
                    self.err("U026", p,
                             f"offers {len(rs)} values in force and is not divided — a list of "
                             f"more than {most} values names its `groups`, categories of no more "
                             f"than {most}, and the person chooses the category, then the value "
                             f"(UX-01 IDR-05)")
                continue
            gv = vocabs.get(g)
            if gv is None or g == vid:
                self.err("U026", p, f"groups names '{g}', which is not another vocabulary of "
                                    f"the model")
                continue
            if v.get("fixed") or gv.get("fixed"):
                self.err("U026", p, f"'{vid}' is divided into the categories of '{g}', and a "
                                    f"divided list and its categories are both lists the "
                                    f"application maintains — neither may be `fixed`")
            cats = [r.get("code") for r in rows(gv)]
            held: dict = {}
            for i, r in enumerate(rs):
                c = r.get("group")
                if not c:
                    self.err("U026", f"{p}/rows/{i}", f"'{r.get('code')}' names no category "
                                                      f"(`group`, a row of '{g}')")
                elif c not in cats:
                    self.err("U026", f"{p}/rows/{i}", f"'{r.get('code')}' names the category "
                                                      f"'{c}', which is not a row of '{g}'")
                else:
                    held[c] = held.get(c, 0) + 1
            for c in sorted(held):
                if held[c] > most:
                    self.err("U026", p, f"the category '{c}' holds {held[c]} values — no step "
                                        f"of a selection offers more than {most} (UX-01 IDR-05)")
            if len(cats) > most:
                self.err("U026", f"vocabularies/{g}",
                         f"holds {len(cats)} categories of '{vid}' — a list of categories holds "
                         f"no more than {most}; the further level the house rule adds is not "
                         f"realized by the kit (UX-01 IDR-05)")

    def l005_lifecycles(self):
        for eid, e in self.entities.items():
            lc = e.get("lifecycle")
            if not lc:
                continue
            p = f"entities/{eid}/lifecycle"
            states = {s["id"]: s for s in lc.get("states", [])}
            initials = [s for s in states.values() if s.get("initial")]
            if len(initials) != 1:
                self.err("L005", p, f"expected exactly one initial state, found {len(initials)}")
            outgoing = set()
            for t in lc.get("transitions", []):
                tp = f"{p}/transitions/{t['id']}"
                for end in ("from", "to"):
                    if t[end] not in states:
                        self.err("L005", tp, f"{end}-state '{t[end]}' not declared")
                outgoing.add(t["from"])
                for r in t.get("roles", []):
                    self._role("L006", tp, r)
                for eff in t.get("effects", []):
                    if eff.get("type") == "set_attr":
                        self._attr("L003", tp, eid, eff["attr"])
                    if eff.get("component"):
                        self._component("L007", tp, eff["component"])
            for sid, s in states.items():
                if s.get("terminal") and sid in outgoing:
                    self.err("L005", f"{p}/states/{sid}", "terminal state has outgoing transitions")

    def l006_l009_forms_lists_nav(self):
        for fid, f in self.forms.items():
            p = f"forms/{fid}"
            e = self._entity("L002", p, f["entity"])
            self._feature("L008", p, f)
            for r in f.get("permissions", {}).get("roles", []):
                self._role("L006", p, r)
            if f.get("prefill"):
                self._component("L007", p, f["prefill"].get("component"))
            lk = f.get("lookup")
            if lk:
                self._component("L007", p, lk.get("component"))
                # every coordinate of a live lookup must resolve in the model. A lookup
                # wired to a name that is not there renders as a permanently blank field,
                # which reads as "nobody filled that in" — the projector refuses it, and
                # so does this, so the model is refused before anything is emitted.
                le = self._entity("L002", f"{p}/lookup", lk.get("entity"))
                if le:
                    self._attr("L003", f"{p}/lookup/match", lk["entity"], lk.get("match"))
                    for m in lk.get("mappings", []):
                        self._attr("L003", f"{p}/lookup/from", lk["entity"], m.get("from"))
                if e:
                    self._attr("L003", f"{p}/lookup/watch", f["entity"], lk.get("watch"))
                    for m in lk.get("mappings", []):
                        self._attr("L003", f"{p}/lookup/to", f["entity"], m.get("to"))
            for sec in f.get("sections", []):
                for fld in sec.get("fields", []):
                    fp = f"{p}/{sec['id']}/{fld.get('attr') or fld.get('id')}"
                    if fld.get("attr") and e:
                        self._attr("L003", fp, f["entity"], fld["attr"])
                    child = fld.get("child")
                    if child:
                        ce = self._entity("L002", fp, child["entity"])
                        cf = self.forms.get(child.get("form"))
                        # forms the lifecycle projector EMITS with every lifecycle app (mm suite):
                        # a grid may bind them (e.g. the AUD-03 history grid over statusEvent)
                        # even though they are not authored in the L1 forms list.
                        MM_EMITTED = {"statusEvent", "mmEntityState", "mmEntityTransition"}
                        if not cf and child.get("form") not in MM_EMITTED:
                            self.err("L015", fp, f"grid child form '{child.get('form')}' not defined")
                        elif cf and cf["entity"] != child["entity"]:
                            self.err("L015", fp, "grid child form is not bound to the child entity")
                        if ce:
                            for col in child.get("columns", []):
                                self._attr("L003", fp, child["entity"], col)
            for pa in f.get("post_actions", []):
                if pa.get("component"):
                    self._component("L007", p, pa["component"])
                if pa.get("process") and pa["process"] not in self.processes:
                    self.err("L010", p, f"unknown process '{pa['process']}'")

        for lid, l in self.lists.items():
            p = f"lists/{lid}"
            self._feature("L008", p, l)
            src = l.get("source", {})
            eid = src.get("entity")
            if eid:
                self._entity("L002", p, eid)
            if src.get("query") and src["query"] not in self.queries:
                self.err("L011", p, f"unknown query '{src['query']}'")
            for c in l.get("columns", []):
                if c.get("attr") and eid:
                    self._attr("L003", f"{p}/columns", eid, c["attr"])
            for flt in l.get("filters", []):
                if flt.get("attr") and eid:
                    self._attr("L003", f"{p}/filters", eid, flt["attr"])
            for a in l.get("actions", []):
                if a.get("form") and a["form"] not in self.forms:
                    self.err("L009", f"{p}/actions", f"unknown form '{a['form']}'")
                if a.get("process") and a["process"] not in self.processes:
                    self.err("L010", f"{p}/actions", f"unknown process '{a['process']}'")
                for r in a.get("roles", []):
                    self._role("L006", f"{p}/actions", r)
            for r in l.get("permissions", {}).get("roles", []):
                self._role("L006", p, r)

        nav = self.doc.get("navigation")
        if nav:
            targets = {"form": self.forms, "list": self.lists,
                       "dashboard": self.dashboards, "report": self.reports,
                       "entity": self.entities}
            need = {"form": "form", "list": "list", "dashboard": "dashboard",
                    "report": "report", "crud": "entity"}
            for cat in nav.get("categories", []):
                p = f"navigation/{cat['id']}"
                for r in cat.get("roles", []):
                    self._role("L006", p, r)
                for m in cat.get("menus", []):
                    mp = f"{p}/{m.get('label')}"
                    for r in m.get("roles", []):
                        self._role("L006", mp, r)
                    k = need.get(m["type"])
                    if k:
                        ref = m.get(k)
                        if not ref:
                            self.err("L009", mp, f"menu type '{m['type']}' requires '{k}'")
                        elif ref not in targets[k]:
                            self.err("L009", mp, f"unknown {k} '{ref}'")

    def l010_processes(self):
        for pid, pr in self.processes.items():
            p = f"processes/{pid}"
            self._feature("L008", p, pr)
            e = self._entity("L002", p, pr["entity"])
            lc = self._lifecycle(pr["entity"])
            transitions = {t["id"] for t in lc.get("transitions", [])}
            participants = {pt["id"] for pt in pr.get("participants", [])}
            for pt in pr.get("participants", []):
                m = ROLE_RE.match(pt.get("map", ""))
                if m:
                    self._role("L006", f"{p}/participants", m.group(1))
            acts = {a["id"] for a in pr.get("activities", [])}
            for a in pr.get("activities", []):
                ap = f"{p}/activities/{a['id']}"
                if a["kind"] == "human":
                    if a.get("participant") not in participants:
                        self.err("L010", ap, f"unknown participant '{a.get('participant')}'")
                    if a.get("form") not in self.forms:
                        self.err("L010", ap, f"unknown form '{a.get('form')}'")
                if a["kind"] == "tool":
                    self._component("L007", ap, a.get("component"))
                for o in a.get("outcomes", []):
                    if o["transition"] not in transitions:
                        self.err("L010", ap, f"outcome '{o['id']}' maps to unknown "
                                             f"transition '{o['transition']}' on entity '{pr['entity']}'")
            for r in pr.get("routing", []):
                for k in ("after", "goto"):
                    if r[k] not in acts:
                        self.err("L010", f"{p}/routing", f"unknown activity '{r[k]}'")
            for d in pr.get("deadlines", []):
                if d["on"] not in acts:
                    self.err("L010", f"{p}/deadlines", f"unknown activity '{d['on']}'")
                m = ROLE_RE.match(d.get("escalate_to", "") or "")
                if d.get("escalate_to") and not m:
                    self.err("L006", f"{p}/deadlines", "escalate_to must be role:<id>")
                elif m:
                    self._role("L006", f"{p}/deadlines", m.group(1))
            if pr["realization"] == "approval_service":
                self._component("L007", p, "approval-service")

    def l008_features(self):
        for f in self.doc.get("features", []):
            p = f"features/{f['id']}"
            for r in f.get("requirements", []):
                if r not in self.requirements:
                    self.err("L008", p, f"unknown requirement '{r}'")
            for d in f.get("depends_on", []):
                if d not in self.features:
                    self.err("L008", p, f"unknown feature dependency '{d}'")
        for coll in ("entities", "processes", "dashboards", "reports", "bespoke_plugins"):
            for item in self.doc.get(coll, []):
                self._feature("L008", f"{coll}/{item.get('id')}", item)

    def l011_queries(self):
        for d in self.doc.get("dashboards", []):
            for t in d.get("tiles", []):
                q = t.get("query")
                if q and q not in self.queries:
                    self.err("L011", f"dashboards/{d['id']}", f"unknown query '{q}'")
        for r in self.doc.get("reports", []):
            q = r.get("query")
            if q not in self.queries:
                self.err("L011", f"reports/{r['id']}", f"unknown query '{q}'")
                continue
            qparams = {pp["id"] for pp in self.queries[q].get("params", [])}
            for pid in r.get("params", []):
                if pid not in qparams:
                    self.err("L011", f"reports/{r['id']}", f"param '{pid}' not defined on query '{q}'")
        # options_query (METHOD-2026-09-25-04, item 6; row 4): the options of a drop-down read by
        # one of the model's queries over the record the form is opened with.
        for fid, f in self.forms.items():
            carried = any(str(k.get("source", "")).lower() == "requestparam" and k.get("name")
                          for k in (f.get("prefill") or {}).get("keySources") or [])
            for sec in f.get("sections", []):
                for fld in sec.get("fields", []):
                    q = fld.get("options_query")
                    if not q:
                        continue
                    p = f"forms/{fid}/{sec.get('id')}/{fld.get('attr') or fld.get('id')}"
                    if q not in self.queries:
                        self.err("L011", p, f"options_query names unknown query '{q}'")
                        continue
                    n = len(self.queries[q].get("params") or [])
                    if n != 1:
                        self.err("L011", p, f"options_query '{q}' must take exactly one "
                                            f"parameter, the carried record's identifier "
                                            f"(it declares {n})")
                    if fld.get("control") not in (None, "select", "radio"):
                        self.err("L011", p, f"options_query gives the options of a drop-down "
                                            f"or radio buttons, not of '{fld.get('control')}'")
                    if not carried:
                        self.err("L011", p, f"options_query '{q}' reads the record the form is "
                                            f"opened with, and form '{fid}' carries none — give "
                                            f"it a prefill whose keySources read it from the "
                                            f"address (requestParam)")

    def l012_tables(self):
        seen = {}
        for eid, e in self.entities.items():
            t = e["table"]
            if t in seen:
                self.err("L012", f"entities/{eid}", f"table '{t}' already used by entity '{seen[t]}'")
            seen[t] = eid

    def l013_secrets(self):
        def scan(mapping, path):
            # invariant 8: a config value that looks secret-bearing must be an ${env:NAME}
            # reference, never a committed literal. Document-wide (D1/WP-D), not just outbound.
            if isinstance(mapping, dict):
                for k, v in mapping.items():
                    if SECRET_KEY_RE.search(k) and isinstance(v, str) and not ENV_REF_RE.match(v):
                        self.err("L013", path,
                                 f"config key '{k}' looks secret-bearing but is not an ${{env:NAME}} reference")
        for io in self.doc.get("interfaces", {}).get("outbound", []):
            self._component("L007", f"interfaces/outbound/{io['id']}", io.get("component"))
            scan(io.get("config"), f"interfaces/outbound/{io['id']}")
        for ii in self.doc.get("interfaces", {}).get("inbound", []):
            scan(ii.get("config"), f"interfaces/inbound/{ii['id']}")
            ex = ii.get("exposes") or {}
            eid = ex.get("entity")
            if eid:
                self._entity("L002", f"interfaces/inbound/{ii['id']}", eid)
                for a in ex.get("attrs", []):
                    self._attr("L003", f"interfaces/inbound/{ii['id']}", eid, a)
        # the rest of invariant 8's surface: form field config, form prefill, catalog config.
        for frm in self.doc.get("forms", []):
            fid = frm.get("id")
            for sec in frm.get("sections", []):
                for fld in sec.get("fields", []):
                    scan(fld.get("config"), f"forms/{fid}/fields/{fld.get('attr') or fld.get('id')}")
            scan(frm.get("prefill"), f"forms/{fid}/prefill")
            scan(frm.get("lookup"), f"forms/{fid}/lookup")
        for cat in self.doc.get("catalog", []):
            scan(cat.get("config"), f"catalog/{cat.get('component') or cat.get('id') or '?'}")

    def l014_acceptance(self):
        for s in self.doc.get("acceptance", {}).get("seed", []):
            pass
        for sd in self.doc.get("seed", []):
            self._entity("L002", "seed", sd["entity"])
        aliases_by_fixture = {}
        for fid, fx in self.fixtures.items():
            p = f"acceptance/fixtures/{fid}"
            aliases = set()
            for rec in fx.get("records", []):
                e = self._entity("L002", p, rec["entity"])
                if rec.get("alias"):
                    aliases.add(rec["alias"])
                st = rec.get("state")
                if st and e:
                    states = {x["id"] for x in self._lifecycle(rec["entity"]).get("states", [])}
                    if states and st not in states:
                        self.err("L014", p, f"state '{st}' not in lifecycle of '{rec['entity']}'")
            aliases_by_fixture[fid] = aliases
        for s in self.doc.get("acceptance", {}).get("scenarios", []):
            p = f"acceptance/scenarios/{s['id']}"
            self._feature("L008", p, s)
            fx = s.get("given", {}).get("fixture")
            if fx and fx not in self.fixtures:
                self.err("L014", p, f"unknown fixture '{fx}'")
            aliases = set(aliases_by_fixture.get(fx, set()))
            for _st in s.get("when", []):   # `when` submit_form steps create aliases too (WP-3 runner)
                if _st.get("alias"):
                    aliases.add(_st["alias"])
            actor = s.get("given", {}).get("actor")
            if actor:
                m = ROLE_RE.match(actor)
                if m:
                    self._role("L006", p, m.group(1))
            for step in list(s.get("when", [])) + list(s.get("then", [])):
                eid = step.get("entity")
                if eid:
                    self._entity("L002", p, eid)
                if step.get("on") and step["on"] not in aliases:
                    self.err("L014", p, f"alias '{step['on']}' not created by fixture '{fx}'")
                tr = step.get("transition")
                if tr and eid:
                    trs = {t["id"] for t in self._lifecycle(eid).get("transitions", [])}
                    if tr not in trs:
                        self.err("L014", p, f"unknown transition '{tr}' on '{eid}'")
                st = step.get("state")
                if st and eid:
                    sts = {x["id"] for x in self._lifecycle(eid).get("states", [])}
                    if st not in sts:
                        self.err("L014", p, f"unknown state '{st}' on '{eid}'")
                if step.get("action") == "complete_activity":
                    pr = self.processes.get(step.get("process"))
                    if not pr:
                        self.err("L014", p, f"unknown process '{step.get('process')}'")
                    else:
                        acts = {a["id"]: a for a in pr.get("activities", [])}
                        act = acts.get(step.get("activity"))
                        if not act:
                            self.err("L014", p, f"unknown activity '{step.get('activity')}'")
                        elif step.get("outcome") and step["outcome"] not in {o["id"] for o in act.get("outcomes", [])}:
                            self.err("L014", p, f"unknown outcome '{step['outcome']}'")
                if step.get("form") and step["form"] not in self.forms:
                    self.err("L014", p, f"unknown form '{step['form']}'")

    def l016_bespoke(self):
        for bp in self.doc.get("bespoke_plugins", []):
            p = f"bespoke_plugins/{bp['id']}"
            req = bp.get("justification", {}).get("requirement")
            if req and req not in self.requirements:
                self.err("L016", p, f"justification requirement '{req}' not in requirements register")
            for eid in list(bp.get("reads", [])) + list(bp.get("writes", [])):
                self._entity("L002", p, eid)

    # ---- U-series: mechanized UX-01 rules (Enterprise UX Standard, Annex B.1; ADR-067).
    # Only the subset expressible against schema 0.1.6 lives here; U001-U004/U008-U010
    # need the schema-0.2 fields (provenance, created_from, persona/trigger) - ADR-067.
    def u_series_ux(self):
        # U006 (STA-05): no physical delete on records of legal record. A crud menu over
        # a lifecycle-bearing entity must set delete: false - cancellation is a lifecycle
        # transition with a reason, never a row delete.
        nav = self.doc.get("navigation") or {}
        for cat in nav.get("categories", []):
            for m in cat.get("menus", []):
                if m.get("type") != "crud":
                    continue
                ent = self.entities.get(m.get("entity") or "")
                if ent and ent.get("lifecycle") and m.get("delete") is not False:
                    self.err("U006", f"navigation/{cat['id']}/{m.get('label')}",
                             f"crud menu over lifecycle entity '{ent['id']}' must set "
                             f"delete: false - records of legal record are cancelled by "
                             f"transition, never deleted (UX-01 STA-05)")
        # U007 (STA-03): status is rendered from the state model, never an editable field — and,
        # since METHOD-2026-09-25-04 (items 2 and 8; the design round's report, "Found, not
        # fixed", item 3), never as any control but the state's badge: the projector draws the
        # badge for a status field that names no control or `select` (the legacy spelling), and a
        # hidden one is not shown at all. Any other control — a text box, radio buttons, a
        # platform element carried verbatim — is refused. Error in every custody mode.
        BADGE_CONTROLS = (None, "select", "hidden")
        for fid, f in self.forms.items():
            ent = self.entities.get(f.get("entity") or "")
            status_attr = ((ent or {}).get("lifecycle") or {}).get("status_attr")
            if not status_attr:
                continue
            for sec in f.get("sections", []):
                for fld in sec.get("fields", []):
                    if fld.get("attr") != status_attr:
                        continue
                    ctrl = fld.get("control")
                    if ctrl not in BADGE_CONTROLS:
                        self.err("U007", f"forms/{fid}/{sec.get('id')}",
                                 f"status attribute '{status_attr}' placed as control "
                                 f"'{ctrl}' - the state is shown as its badge, carrying its "
                                 f"tone, never as another control (UX-01 STA-03)")
                    elif not (fld.get("readonly") or sec.get("readonly")) and ctrl != "hidden":
                        self.err("U007", f"forms/{fid}/{sec.get('id')}",
                                 f"status attribute '{status_attr}' placed as an editable "
                                 f"field - status is rendered from the state model, never "
                                 f"edited (UX-01 STA-03)")

        # U025 (CTX-01; METHOD-2026-09-25-04, item 4): a form that belongs to a record — its
        # trigger is `record_action` — opens from that record and never from the menu: it stands
        # only in a category with `hidden: true`. On a visible menu it opens on nothing, as the
        # owner found "Choose the enforcement acts" and "Request a write-off". Error, every mode.
        rec_forms = {fid for fid, f in self.forms.items()
                     if (f.get("trigger") or {}).get("kind") == "record_action"}
        for cat in nav.get("categories", []):
            if cat.get("hidden"):
                continue
            for m in cat.get("menus", []):
                opened = {m.get("form"), m.get("edit_form")} if m.get("type") in ("form", "crud") \
                    else set()
                for fid in sorted(x for x in opened & rec_forms if x):
                    self.err("U025", f"navigation/{cat['id']}/{m.get('label')}",
                             f"form '{fid}' belongs to a record (trigger: record_action) and "
                             f"stands on a visible menu, where it opens on nothing — place its "
                             f"menu in a category with `hidden: true`, and open it from the "
                             f"record's act (UX-01 CTX-01)")

        # ---- schema-0.2 U-series (WP-F; ADR-071 / UX-01 B.1; Appendix D.2) ------
        # Severity is posture-driven via _u (required=error, stamp=warn). U-PK is a
        # wiring-integrity error in BOTH modes; U009/U010 warn in v1.
        DISCRETIONARY = ("hold", "unhold", "reopen", "waive", "reassign",
                         "override", "cancel", "revoke", "write_off", "writeoff")
        # provenance is implied by these controls, so U002 does not demand it there.
        PROV_EXEMPT = {"id_generator", "calculation", "concat", "grid",
                       "embedded_list", "custom_html"}
        BOUNDED_CTRL = {"select", "radio", "checkbox"}

        for fid, f in self.forms.items():
            fp0 = f"forms/{fid}"
            ent = self.entities.get(f.get("entity") or "") or {}
            eattrs = {a["id"]: a for a in ent.get("attributes", [])}
            trig = f.get("trigger") or {}

            # U008 (CTX-01, Q1-Q2): every screen declares persona AND trigger.
            miss = [k for k in ("persona", "trigger") if not f.get(k)]
            if miss:
                self._u("U008", fp0,
                        f"form must declare {' and '.join(miss)} "
                        f"(UX-01 CTX-01 / Screen Design Protocol Q1-Q2)")

            # U003 (PRE-03, CTX-01): a create form over a case-kind (lifecycle-bearing)
            # entity is created FROM its source; a menu trigger is the justified exception.
            if f.get("purpose") == "create" and ent.get("lifecycle"):
                ok = bool(f.get("created_from")) or (
                    trig.get("kind") == "menu" and trig.get("justification"))
                if not ok:
                    self._u("U003", fp0,
                            f"create form over case-kind entity '{ent.get('id')}' must "
                            f"declare created_from, or trigger.kind: menu with a "
                            f"justification (UX-01 PRE-03 / CTX-01)")

            for sec in f.get("sections", []):
                for fld in sec.get("fields", []):
                    aid = fld.get("attr")
                    fp = f"{fp0}/{sec.get('id')}/{aid or fld.get('id')}"
                    ctrl = fld.get("control")
                    prov = fld.get("provenance")
                    a = eattrs.get(aid or "", {})

                    # U002 (PRE-01/02): every value field declares provenance; 'entered'
                    # justifies itself. Container / auto-provenance controls are exempt.
                    if ctrl not in PROV_EXEMPT:
                        if not prov:
                            self._u("U002", fp, "field must declare provenance (UX-01 PRE-01)")
                        elif prov == "entered" and not fld.get("justification"):
                            self._u("U002", fp,
                                    "provenance 'entered' requires a justification "
                                    "(UX-01 PRE-02, once-only)")

                    # U004 (PRE-04): a pre-filled / derived value is read-only in the model.
                    if prov in ("derived", "source", "master") and not fld.get("readonly"):
                        self._u("U004", fp,
                                f"field with provenance '{prov}' must be readonly: true "
                                f"(UX-01 PRE-04; mastered values corrected at the owner, MDM-07)")

                    # U001 / U-PK: a reference-kind field.
                    if a.get("type") == "ref":
                        tgt = (a.get("ref") or {}).get("entity")
                        te = self.entities.get(tgt or "") or {}
                        op = self._operational(te)
                        # U001 (IDR-05): a growing set is a search-select, never a dropdown —
                        # unless the options are the model's query over the carried record
                        # (options_query), which bounds them to that record's own.
                        # ERROR in every custody mode (METHOD-2026-09-25-04, item 8): as a
                        # warning under `custody: stamp` it let drop-downs over whole tables
                        # pass into one application (the design round's report,
                        # "Found, not fixed", item 2).
                        if op and ctrl in BOUNDED_CTRL and not fld.get("options_query"):
                            self.err("U001", fp,
                                    f"reference to operational entity '{tgt}' uses '{ctrl}' "
                                    f"- an unbounded set must be a search-select "
                                    f"(lookup / smart_search), not a dropdown (UX-01 IDR-05)")
                        # U-PK: an editable ref to an operational entity is unwireable unless
                        # that entity declares a pk (a failure seen in an earlier exploration). Hard, both modes.
                        if op and not fld.get("readonly") and not (te.get("pk") or {}).get("attr"):
                            self.err("U-PK", fp,
                                     f"editable reference to operational entity '{tgt}' "
                                     f"requires '{tgt}' to declare a pk - without it the FK "
                                     f"cannot be stored (CH-01 wiring integrity)")

        # U005 (WRK-02/03/04): every list is server-side, sorted, and scoped by default.
        for lid, l in self.lists.items():
            miss = []
            if "page_size" not in l:
                miss.append("page_size")
            if "sort" not in l:
                miss.append("sort")
            if not (l.get("default_scope") or "x-scope-waiver" in l):
                miss.append("default_scope (or an explicit x-scope-waiver)")
            if miss:
                self._u("U005", f"lists/{lid}",
                        f"list must declare {', '.join(miss)} "
                        f"(UX-01 WRK-02/03/04 - no unbounded, unsorted, or empty-open list)")

        # U011 (ADR-094): a decision must be REACHABLE. A `trigger: process` transition is
        # taken in a workflow activity, never from a form's action select, so a human only
        # gets to it through an assignment — and an assignment exists only if something
        # started an instance of the process that owns the activity. taxRegistration shipped
        # for weeks with a reg_review definition, a start whitelist, and no caller: a
        # registration could be created, submitted and put under verification, and from there
        # only bounce to pending_documents and back. Nothing said so, because the API suite
        # applies transitions directly and never asks whether a person could reach one.
        # ERROR, not warning: the alternative is an app whose terminal decisions cannot be
        # taken, which is worse than one that refuses to build.
        started = {e.get("process") for ent in self.entities.values()
                   for t in (ent.get("lifecycle") or {}).get("transitions", [])
                   for e in (t.get("effects") or [])
                   if e.get("type") == "start_process"}
        proc_ids = {p.get("id") for p in self.doc.get("processes", [])}
        for eid, ent in self.entities.items():
            for t in (ent.get("lifecycle") or {}).get("transitions", []):
                for e in (t.get("effects") or []):
                    if e.get("type") == "start_process" and e.get("process") not in proc_ids:
                        self.err("U011", f"entities/{eid}/lifecycle/transitions/{t.get('id')}",
                                 f"start_process names '{e.get('process')}', which is not a "
                                 f"declared process (have: {sorted(proc_ids) or 'none'})")
        for p in self.doc.get("processes", []):
            ent = self.entities.get(p.get("entity")) or {}
            drives = [t.get("id") for t in (ent.get("lifecycle") or {}).get("transitions", [])
                      if t.get("trigger") == "process"]
            if drives and p.get("id") not in started:
                self.err("U011", f"processes/{p.get('id')}",
                         f"nothing starts this process, yet {p.get('entity')} reaches "
                         f"{', '.join(drives)} only through it — those decisions are "
                         f"unreachable by any human. Add a start_process effect to the "
                         f"transition that arrives at the state they leave from.")

        # U009 (AUD-02): a discretionary transition captures a coded reason. Warn in v1
        # until reason vocabularies are seeded (Appendix D.2).
        for eid, ent in self.entities.items():
            for t in (ent.get("lifecycle") or {}).get("transitions", []):
                tid = t.get("id", "")
                if t.get("roles") and any(v in tid for v in DISCRETIONARY) and not t.get("reason"):
                    self.warn("U009", f"entities/{eid}/lifecycle/transitions/{tid}",
                              "discretionary transition should capture a coded, "
                              "vocabulary-backed reason (UX-01 AUD-02)")

        # U010 (TRM-04): a custody:required app registers its language resources. Warn;
        # generator realization is deferred (0.2 registration-only, ADR-071).
        if self.custody_mode == "required" and not (self.doc.get("app") or {}).get("i18n"):
            self.warn("U010", "app",
                      "custody:required app should declare app.i18n {resources} "
                      "(UX-01 TRM-04 - no user-facing literal outside language resources)")

    def m_series_dd_gate(self):
        """DD-01 M-series: the AUTHORING gate that makes a naive control unauthorable.
        Active only when model.dd_ref resolves. M-00 broken ref; M-01 semantic that
        names no dd set; M-02 an attribute that matches a governed set but is left an
        unbound primitive (HARD error for typed.period — the period-as-text defect;
        advisory warning for the softer kinds)."""
        if not self.dd:
            return
        if self.dd.get("__error__"):
            self.err("M-00", "model/dd_ref",
                     f"dd_ref '{self.dd['__error__']}' could not be loaded")
            return
        PRIMITIVE = {"string", "text", "date", "datetime", "integer", "decimal"}
        for eid, ent in self.entities.items():
            for a in ent.get("attributes", []):
                aid = a["id"]
                sem = a.get("semantic")
                path = f"entities/{eid}/attributes/{aid}"
                if sem:                                       # M-01: must name a real set
                    if sem[3:] not in self.dd_sets:
                        self.err("M-01", path,
                                 f"semantic '{sem}' names no set in the data dictionary")
                    continue
                # M-02: unbound attribute that matches a governed set by name
                match = (aid if aid in self.dd_sets else self.dd_by_tail.get(aid))
                if not match:
                    continue
                kind = self.dd_sets[match].get("kind", "")
                if a.get("type") not in PRIMITIVE:
                    continue                                  # refs/enum handled elsewhere
                if kind in DD_FREETYPE_FORBIDDEN_HARD:
                    self.err("M-02", path,
                             f"attribute matches governed set dd:{match} ({kind}) but is a "
                             f"free-typed '{a.get('type')}' - bind `semantic: dd:{match}` "
                             f"(the projector renders {DD_KIND_CONTROL.get(kind)}), or rename")
                else:
                    # advisory: name matches a governed set; classification recommended
                    self.warnings.append(
                        f"[M-02w] {path}: attribute name matches governed set dd:{match} "
                        f"({kind}); consider `semantic: dd:{match}` (advisory)")

    def run(self) -> list[str]:
        self.l001_unique_ids()
        self.l002_l003_entities_and_attrs()
        self.l004_vocab_parents()
        self.l017_bound_vocabulary_values()
        self.l018_acts()
        self.l018_acts_on_records()
        self.l005_lifecycles()
        self.l006_l009_forms_lists_nav()
        self.l010_processes()
        self.l008_features()
        self.l011_queries()
        self.l012_tables()
        self.l013_secrets()
        self.l014_acceptance()
        self.l016_bespoke()
        self.l019_seed_references()
        self.l020_default_scope()
        self.u026_long_lists()
        self.u_series_ux()
        self.m_series_dd_gate()
        return self.errors


# Controls whose generator element is Enterprise-only (edition=community lacks them).
ENTERPRISE_CONTROLS = {
    "grid": "FormGrid", "calculation": "CalculationField", "concat": "ConcatField",
    "embedded_list": "EmbeddedDatalist", "smart_search": "SmartSearchElement",
}
UPPER_RE = re.compile(r"[A-Z]")
# D-063: a pg/pg_*/pr-shaped table alias — after FROM/JOIN <table>, or an explicit AS <alias>.
PG_ALIAS_RE = re.compile(r"\b(?:from|join)\s+[a-z_][\w.]*\s+(?:as\s+)?(pg|pg_\w+|pr)\b"
                         r"|\bas\s+(pg|pg_\w+|pr)\b", re.I)
# D-046: an extra_condition that leads with a SQL connector Joget already supplies.
BARE_COND_RE = re.compile(r"^\s*(where|and|or)\b", re.I)
# D-038: a request parameter a query reads in its own SQL (#requestParam.<name>#, or with ?sql).
REQUEST_PARAM_RE = re.compile(r"#requestParam\.([A-Za-z_]\w*)(?:\?\w+)?#")


class PlatformRules:
    """Platform-delta rules (D-series) — model predicates keyed on `app.platform`.

    Each rule fires only when the model's platform (dx / edition / db) matches the
    delta's key, and every finding cites its register D-id (the source of authority,
    ADR-010). Severity discipline (S2C-22): `error` blocks generation and joins the
    exit-2 set; `warn` reports without changing the exit code. Every rule is covered
    by a fixture pair in tests/test_drules.py — one model that must trip it, one that
    must not.
    """

    def __init__(self, doc: dict):
        self.doc = doc
        plat = (doc.get("app") or {}).get("platform") or {}
        self.dx = str(plat.get("dx", ""))
        self.dx_major = self.dx.split(".")[0] if self.dx else ""
        self.edition = plat.get("edition", "")
        self.db = plat.get("db", "")
        self.entities = {e["id"]: e for e in doc.get("entities", [])}
        self.forms = list(doc.get("forms", []))
        self.forms_by_id = {f["id"]: f for f in self.forms}
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def _add(self, severity: str, rule: str, path: str, msg: str):
        line = f"[{rule}] {path}: {msg}"
        (self.errors if severity == "error" else self.warnings).append(line)

    def _fields(self):
        for f in self.forms:
            for sec in f.get("sections", []):
                for fld in sec.get("fields", []):
                    yield f, sec, fld

    # ---- edition gate: Enterprise-only realizations on Community --------------
    def d053_enterprise_controls(self):
        """D-053 — a form control/wizard that realizes as an Enterprise-only element."""
        if self.edition != "community":
            return
        for f, sec, fld in self._fields():
            ctrl = fld.get("control")
            if ctrl in ENTERPRISE_CONTROLS:
                fid = fld.get("attr") or fld.get("id")
                self._add("error", "D-053", f"forms/{f['id']}/{sec['id']}/{fid}",
                          f"control '{ctrl}' realizes as the Enterprise-only element "
                          f"{ENTERPRISE_CONTROLS[ctrl]} — absent on edition=community")
            if fld.get("options_query"):
                fid = fld.get("attr") or fld.get("id")
                self._add("error", "D-053", f"forms/{f['id']}/{sec['id']}/{fid}",
                          "options_query realizes as the Enterprise-only JdbcOptionsBinder — "
                          "absent on edition=community")
        for v in self.doc.get("vocabularies", []):
            if v.get("groups"):
                self._add("error", "D-053", f"vocabularies/{v['id']}",
                          "a divided list (groups) is read with its categories by the "
                          "Enterprise-only JdbcOptionsBinder — absent on edition=community")
        for f in self.forms:
            if f.get("purpose") == "wizard" or f.get("wizard"):
                self._add("error", "D-053", f"forms/{f['id']}",
                          "wizard realizes as the Enterprise-only MultiPagedForm — "
                          "absent on edition=community")

    def d043_dashboards_enterprise(self):
        """D-043 — dashboards realize as Enterprise SqlChartMenu/DashboardMenu."""
        if self.edition != "community":
            return
        for d in self.doc.get("dashboards", []):
            self._add("error", "D-043", f"dashboards/{d['id']}",
                      "dashboards realize as Enterprise SqlChartMenu/DashboardMenu — "
                      "absent on edition=community (no scripted-HTML fallback, D-043)")

    def d042_jasper_enterprise(self):
        """D-042 — jasper reports realize as the Enterprise JasperReportsMenu."""
        if self.edition != "community":
            return
        for r in self.doc.get("reports", []):
            if r.get("engine") == "jasper":
                self._add("error", "D-042", f"reports/{r['id']}",
                          "jasper reports realize as the Enterprise JasperReportsMenu — "
                          "absent on edition=community")

    # ---- seeds & tables ------------------------------------------------------
    def d049_md_lookup_seed_needs_form(self):
        """D-049 — an md_lookup seeded without a form: no app_fd_* for the API to fill.
        Since METHOD-2026-09-25-02 the kit generates a form for every md_lookup the application
        maintains (tools/lov.py), so only a `fixed` one can still arrive with none."""
        formed = {f.get("entity") for f in self.forms}
        for sd in self.doc.get("seed", []):
            eid = sd.get("entity")
            e = self.entities.get(eid) or {}
            if e.get("kind") == "md_lookup" and e.get("fixed") and eid not in formed:
                self._add("error", "D-049", f"seed/{eid}",
                          f"md_lookup entity '{eid}' is seeded but has no form — the "
                          f"form-data API needs a deployed form to create app_fd_{e.get('table', eid)} "
                          f"before its rows load")

    def d062_postgres_folding(self):
        """D-062 — camelCase ids fold to lowercase columns on Postgres."""
        if self.db != "postgres":
            return
        for eid, e in self.entities.items():
            for a in e.get("attributes", []):
                if UPPER_RE.search(a["id"]):
                    self._add("warn", "D-062", f"entities/{eid}/attributes/{a['id']}",
                              f"camelCase id '{a['id']}' folds to column c_{a['id'].lower()} on "
                              f"Postgres — camelCase reads and seed-payload keys must match the "
                              f"field id, not the folded column")
        for f, sec, fld in self._fields():
            if "attr" not in fld and "id" in fld and UPPER_RE.search(fld["id"]):
                self._add("warn", "D-062", f"forms/{f['id']}/{sec['id']}/{fld['id']}",
                          f"camelCase field id '{fld['id']}' folds to lowercase on Postgres")

    # ---- wizard --------------------------------------------------------------
    def d065_wizard_partial_store(self):
        """D-065 — wizard partial-store does not propagate the parent key to subforms."""
        if self.edition != "enterprise":
            return
        for f in self.forms:
            wiz = f.get("wizard")
            if not (f.get("purpose") == "wizard" or wiz):
                continue
            if not (wiz or {}).get("partial_store", True):
                continue
            for step in (wiz or {}).get("steps", []):
                # steps carry either a bare form id or the rich object (2026-08-08)
                sid = step if isinstance(step, str) else (step or {}).get("form")
                sf = self.forms_by_id.get(sid)
                if sf and any(fl.get("control") == "grid"
                              for s in sf.get("sections", []) for fl in s.get("fields", [])):
                    self._add("warn", "D-065", f"forms/{f['id']}",
                              f"wizard with partial_store and a grid in step '{sid}': the "
                              f"parent key is not propagated to tab subforms until the final "
                              f"save — server-side cross-subform flow no-ops on first visit")
                    break

    # ---- queries & lists -----------------------------------------------------
    def d063_pg_sql_alias(self):
        """D-063 — pg/pg_*-shaped SQL table aliases throw an opaque PSQLException through
        Joget's pgjdbc pool (the same query runs fine in psql). Rename the alias."""
        if self.db and self.db != "postgres":
            return
        for q in self.doc.get("queries", []):
            m = PG_ALIAS_RE.search(q.get("sql", ""))
            if m:
                alias = m.group(1) or m.group(2)
                self._add("warn", "D-063", f"queries/{q['id']}",
                          f"SQL table alias '{alias}': pg/pg_*-shaped aliases throw an opaque "
                          f"PSQLException through Joget's pgjdbc pool though the query runs in "
                          f"psql — rename the alias (e.g. t, x)")

    def d038_jdbc_single_param_filter(self):
        """D-038 — a JDBC (query-source) list honours only ONE #requestParam per request INSIDE
        its query: a second `#requestParam.<name>#` the query's own SQL reads resolves to '' and
        its guard no-ops.

        Narrowed on 6 October 2026 (ADR-108; a delivery's hand-off of 6 October 2026, item 4,
        F-B2-10). The rule warned on any query list that declared two filters. A filter the
        list declares is a filter type the binder wraps around the query (gen_datalists:
        TextField-, SelectBox- and DateRangeDataListFilterType, each narrowing by its own
        column), and the platform honours every one: on jdx12 both filters of nine lists
        narrowed, together giving the rows that satisfy both (one delivery's build, 9 of
        9). What the delta records is a request parameter the query reads itself, so the rule
        counts those."""
        queries = {q.get("id"): q for q in self.doc.get("queries", [])}
        for lst in self.doc.get("lists", []):
            qid = (lst.get("source") or {}).get("query")
            if not qid:
                continue
            sql = str((queries.get(qid) or {}).get("sql") or "")
            params = sorted(set(REQUEST_PARAM_RE.findall(sql)))
            if len(params) > 1:
                self._add("warn", "D-038", f"lists/{lst['id']}",
                          f"the query '{qid}' reads {len(params)} request parameters in its own SQL "
                          f"({', '.join('#requestParam.' + p + '#' for p in params)}), but a "
                          f"JdbcDataListBinder honours only ONE #requestParam inside a query per "
                          f"request — the 2nd+ no-op; read one, and narrow by the rest with the "
                          f"list's filters, which the binder wraps around the query and honours")

    def d046_extracondition_bare(self):
        """D-046/D-058 — a form-row list `extra_condition` is appended after Joget's own WHERE,
        verbatim; a leading WHERE/AND/OR breaks the generated SQL."""
        for lst in self.doc.get("lists", []):
            ec = lst.get("extra_condition")
            if ec and BARE_COND_RE.match(ec):
                self._add("warn", "D-046", f"lists/{lst['id']}",
                          f"extra_condition must be the BARE predicate — Joget prepends its own "
                          f"WHERE and appends this verbatim; the leading "
                          f"'{ec.split()[0]}' breaks the SQL (D-046/D-058)")

    # ---- validator budget ----------------------------------------------------
    def d013_unrealizable_validation(self):
        """D-013 — pattern/uniqueness the DefaultValidator can't express, un-budgeted.

        D-066: id_generator produces FORMATTED ids, not uniqueness — its counter state is
        instance-local, so re-imports and concurrency collide (observed: two DC-000001 on
        a reference build). A pk that uses id_generator is therefore NOT self-enforcing, so a unique
        attr does not earn the pk exemption. An unenforced `unique:` is an ERROR (a silent
        key collision corrupts record identity — DP-7 corruption class); an unenforced
        `pattern:` stays a warning."""
        covered = set()
        for bp in self.doc.get("bespoke_plugins", []):
            for eid in list(bp.get("reads", [])) + list(bp.get("writes", [])):
                covered.add(eid)
        for eid, e in self.entities.items():
            if eid in covered:
                continue
            pk = e.get("pk") or {}
            pk_attr = pk.get("attr")
            # the pk self-enforces uniqueness ONLY when the platform guarantees it; an
            # id_generator pk does not (D-066), so it earns no exemption.
            pk_self_enforcing = pk_attr is not None and pk.get("strategy") != "id_generator"
            # An entity-level `uniqueness` declaration carries the enforcement for the attrs it
            # names, in one of three clearing states (ADR-076 §6 / WP-2 steps 4-5): guard|validator
            # -> unique-guard prevention (emitted by project_forms, A006 verifies it); detection +
            # waiver -> consciously budgeted (WATCHED via an integrity scenario + admin datalist,
            # prevention deferred). The waiver is MANDATORY — detection without it is a silent
            # waive -> error; an unknown enforcement is an error. The DB index stays escalation-only.
            cleared = set()
            for u in (e.get("uniqueness") or []):
                enf = (u.get("enforcement") or "guard").lower()
                uattrs = [str(x) for x in (u.get("attrs") or [])]
                if enf in ("guard", "validator"):
                    cleared.update(uattrs)
                elif enf == "detection":
                    if str(u.get("waiver") or "").strip():
                        cleared.update(uattrs)
                    else:
                        self._add("error", "D-013", f"entities/{eid}/uniqueness",
                                  f"enforcement: detection on {uattrs} requires an explicit `waiver` "
                                  f"— the conscious-budget ruling that prevention is deferred "
                                  f"(ADR-076 §6 / WP-2 step 5); D-013 never clears on a silent waive")
                else:
                    self._add("error", "D-013", f"entities/{eid}/uniqueness",
                              f"unknown uniqueness enforcement '{enf}' on {uattrs} — "
                              f"expected guard | validator | detection")
            for a in e.get("attributes", []):
                exempt = (a["id"] == pk_attr and pk_self_enforcing) or a["id"] in cleared
                if a.get("unique") and not exempt:
                    self._add("error", "D-013", f"entities/{eid}/attributes/{a['id']}",
                              f"unique on '{a['id']}' is declared but not enforced: the "
                              f"DefaultValidator cannot express it and id_generator pks do not "
                              f"guarantee uniqueness (D-066) — no bespoke validator (or unique-guard) "
                              f"covers '{eid}'; a silent collision corrupts record identity")
                elif a.get("pattern"):
                    self._add("warn", "D-013", f"entities/{eid}/attributes/{a['id']}",
                              f"pattern on '{a['id']}' is not expressible in the generator's "
                              f"DefaultValidator and no bespoke validator reads '{eid}' — "
                              f"budget one in bespoke_plugins")

    def run(self):
        self.d053_enterprise_controls()
        self.d043_dashboards_enterprise()
        self.d042_jasper_enterprise()
        self.d049_md_lookup_seed_needs_form()
        self.d062_postgres_folding()
        self.d065_wizard_partial_store()
        self.d063_pg_sql_alias()
        self.d038_jdbc_single_param_filter()
        self.d046_extracondition_bare()
        self.d013_unrealizable_validation()
        return self.errors, self.warnings


def load_mirror(path: pathlib.Path = DEFAULT_MIRROR):
    """Load the component config-contract mirror (ADR-009); None if absent."""
    try:
        return load(path)
    except FileNotFoundError:
        return None


class ContractRules:
    """Validate model `config`/`prefill` blocks against each catalog component's
    published contract (the registry mirror, ADR-009/016) — no Java imported.

    A component with a rich `config_schema` (form-prefill) is validated structurally:
    unknown keys and bad enum values are ERRORS (the schema is source-grounded). A
    component with only a `config_keys` allow-list gets a WARN on unknown keys (the
    list may be non-exhaustive). A component not in the mirror is skipped (no
    published contract yet). Structural components (config_keys: []) carry no raw
    model config block — they are validated by schema + L-rules, not here.
    """

    def __init__(self, doc: dict, mirror: dict | None):
        self.doc = doc
        self.mirror = mirror or {}
        self.aliases = (self.mirror.get("catalog_aliases") or {})
        self.components = (self.mirror.get("components") or {})
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def _contract(self, component: str):
        if not component:
            return None
        rid = self.aliases.get(component, component)
        return self.components.get(rid)

    def _check(self, component: str, body: dict, path: str):
        c = self._contract(component)
        if c is None or not isinstance(body, dict):
            return
        schema = c.get("config_schema")
        if schema:
            v = Draft202012Validator(schema)
            for e in sorted(v.iter_errors(body), key=lambda e: list(e.absolute_path)):
                loc = "/".join(str(p) for p in e.absolute_path) or "<config>"
                self.errors.append(
                    f"[C001] {path}: component '{component}' config invalid at {loc}: {e.message}")
            return
        keys = c.get("config_keys") or []
        if keys:
            for k in body:
                if k not in keys:
                    self.warnings.append(
                        f"[C002] {path}: config key '{k}' is not in the published contract "
                        f"for component '{component}' (may be silently ignored)")

    def run(self):
        for f in self.doc.get("forms", []):
            pf = f.get("prefill")
            if pf:
                body = {k: v for k, v in pf.items() if k != "component"}
                self._check(pf.get("component"), body, f"forms/{f['id']}/prefill")
            for pa in f.get("post_actions", []):
                if pa.get("config"):
                    self._check(pa.get("component"), pa["config"],
                                f"forms/{f['id']}/post_actions")
        for c in self.doc.get("catalog", []):
            comp = c.get("component")
            contract = self._contract(comp)
            if contract and contract.get("maturity") == "provisional":   # ADR-050 maturity ladder
                self.warnings.append(
                    f"[C003] catalog/{comp}: component is PROVISIONAL (proven in one context, "
                    f"ADR-050) — pin its version and expect possible breaking changes until it "
                    f"graduates to stable")
            if c.get("config"):
                self._check(comp, c["config"], f"catalog/{comp}")
        for io in self.doc.get("interfaces", {}).get("outbound", []):
            if io.get("config"):
                self._check(io.get("component"), io["config"],
                            f"interfaces/outbound/{io['id']}")
        return self.errors, self.warnings


def delta_contract(doc: dict, mirror: dict | None = None) -> tuple[list[str], list[str]]:
    """Combined DELTA + CONTRACT findings — the layers a projector must also honour.

    Returns (errors, warnings). Errors block generation (the projectors refuse on them,
    ADR-015/016); warnings are advisory. Schema + lint are validated separately, first.
    """
    derrs, dwarns = PlatformRules(doc).run()
    cerrs, cwarns = ContractRules(doc, mirror if mirror is not None else load_mirror()).run()
    return derrs + cerrs, dwarns + cwarns


# =========================================================================== #
# L021 — the interaction design gate (SDD-11, section 8; METHOD-2026-09-25-12)  #
# =========================================================================== #
# The owner's word of 25 September 2026 is that the interaction design step is not to be
# skipped. A step that rests on a person remembering it can be skipped by a person forgetting
# it, so it is closed here, by a program, at the one point every application passes: the
# admission of its model to generation. The model names the document the owner accepted, in
# `model.interaction_design`, by its path relative to the model and its SHA-256 checksum; this
# rule refuses the model on any of nine checks. It is an ERROR IN EVERY CUSTODY MODE: it reads
# no `.kit.yaml`, no key of the model, no flag and no environment variable, so nothing turns it
# off. It runs first in `kit validate` (main, below), and the same function runs first in
# `kit gen`, `tools/build_app.py`, `kit deploy` and `tools/deploy_dx9.py` (admit_or_refuse), so
# that a check made by one command is not skipped by calling another. It is deliberately not a
# method of Lint: the projectors call Lint on a model they hold in memory, with no path to find
# the document by, and a projector called on its own writes files that reach no server without
# the build and the deploy (the plan of the step, section 5.1).
#
# The document is read by tools/interaction_design.py, as the kit's template of its form fixes
# (templates/spec/INTERACTION_DESIGN.md.tmpl): a row names the construct it governs by the
# model's identifier between backticks, and the gate reads only the words the template names.

IXD_RULE = "L021"
IXD_QUESTION = "TO ANSWER"          # what `kit new` writes in the entry until it is answered
IXD_DROPDOWNS = {"select": "a drop-down", "lookup": "a drop-down", "radio": "a group of radio buttons",
                 "checkbox": "a group of check-boxes"}
IXD_MOST = 9                         # a list of more than nine is chosen by category (IDR-05)


def _ixd_populate_targets(value) -> set:
    """The fields a smart search's `populate` fills: "src:dst,src:dst" or a mapping."""
    if isinstance(value, dict):
        return {str(v).strip() for v in value.values() if str(v).strip()}
    out = set()
    for pair in [p for p in str(value or "").split(",") if p.strip()]:
        _, _, dst = pair.partition(":")
        if dst.strip():
            out.add(dst.strip())
    return out


def _ixd_control(fld: dict, attr: dict, dd: dict) -> str:
    """The control a placed field takes, as the forms projector derives it: the model's own
    `control`, else the data dictionary's control for the attribute's governed set, else the
    attribute type's default (project_forms.ATTR_TYPE_MAP: an enum and a reference are drop-downs)."""
    if fld.get("control"):
        return str(fld["control"])
    _, dctl = dd_control_for(dd, attr.get("semantic")) if attr.get("semantic") else (None, None)
    if dctl:
        return dctl
    return {"enum": "select", "ref": "select", "boolean": "checkbox"}.get(attr.get("type"), "text")


def _ixd_searches(form: dict, entities: dict, lists: dict, dd: dict) -> dict:
    """METHOD-2026-09-28-01: {the list that is a search's result: the record it looks in} for each
    search the form places — an editable reference the forms projector realises as the library's
    smart search (its control, derived from the data dictionary), whose result is the list
    `config.search_list` names, else the one list of the record, as the projector finds it."""
    ent = entities.get(form.get("entity")) or {}
    attrs = {a.get("id"): a for a in ent.get("attributes") or []}
    out = {}
    for sec in form.get("sections") or []:
        for f in sec.get("fields") or []:
            a = attrs.get(f.get("attr")) or {}
            if a.get("type") != "ref" or f.get("readonly") or a.get("readonly") or sec.get("readonly") \
                    or _ixd_control(f, a, dd) != "smart_search":
                continue
            rec = (a.get("ref") or {}).get("entity")
            lid = (f.get("config") or {}).get("search_list")
            if not lid:
                of = [i for i, lst in lists.items() if (lst.get("source") or {}).get("entity") == rec]
                lid = of[0] if len(of) == 1 else None
            if lid:
                out[lid] = rec
    return out


# The kit's own register of its gaps (METHOD-2026-09-26-02, point 19 (b)): a disagreement the model
# records as a loss is admitted only where the loss names an entry of this register, whose round is
# open while the entry stands. The kit's file, read from the kit and from no other place: no key,
# setting, flag or variable names another register (ADR-105; ADR-106).
KIT_GAPS = pathlib.Path(__file__).resolve().parent.parent / "templates" / "spec" / "kit-gaps.yaml"
# The engagement's own kinds, which are never gaps of the kit.
NOT_KIT_GAPS = ("the design's words", "the model's source", "starting data")

# The kinds of disagreement rule L021 tells apart (METHOD-2026-09-26-02, version 3, gap 1): for each
# of the checks 6 to 9, the comparison that fails, in words. Every disagreement of those checks is
# of one kind. An entry of the kit's register names, in `admits`, the kind of disagreement it
# admits, and where its gap is narrower than the kind, the conditions (IXD_WHERE) that hold of the
# element the disagreement is about; L021 admits a disagreement on a loss only when it is of a kind,
# and under the conditions, the loss's entry names.
IXD_KINDS = {
    6: {"list-absent": "the row names a list the model does not hold",
        "maintained-or-fixed": "the list is maintained in the application in one of the two and fixed "
                               "in the other",
        "maintained-by": "the model's list is maintained by another role than the row decides",
        "code-shown": "the list shows its code as its label in one of the two and its label in the "
                      "other",
        "categories": "the model's list is divided into other categories than the row decides, or "
                      "into none",
        "category-members": "the model's list of categories holds other categories than the row "
                            "gives",
        "long-list-undivided": "the row counts more than nine members in force and the model's list "
                               "is not divided into categories"},
    7: {"place-absent": "the row names a place that is no form's field and no list of the model",
        "value-not-placed": "the row names a value the form does not place",
        "search-as-drop-down": "a record the row finds by a search is chosen in the model from a "
                               "drop-down",
        "fills": "the choice fills other values in the model than the row says",
        "locks": "the choice locks other values in the model than the row says"},
    8: {"record-absent": "the row names a record that is no entity of the model",
        "move-absent": "the row names a move that is no move of the record's lifecycle",
        "move-states": "the model's move goes between other states than the row says",
        "button-offered": "the model offers a button for a move the row says no act of this "
                          "increment makes",
        "button-absent": "no form of the record in the model offers the button the row names",
        "button-roles": "the model gives the button to other roles than the row does",
        "button-unlisted": "the model offers a button for a move the Moves table lists as no "
                           "person's"},
    9: {"stands-on-absent": "the row's act stands on an element that is no form, list or category "
                            "of the model",
        "stands-on-two": "the row's act stands on an identifier that names two elements of the model "
                         "at once",
        "act-absent": "an act the row names is one the model lacks: the element it stands on has no "
                      "act that opens what the row says it opens",
        "carries": "the model's act carries another record than the row says",
        "on-a-menu": "what the act opens stands on a visible menu of the model, and the row says it "
                     "stands on none"},
}
# The conditions that narrow a kind to the element a disagreement is about, by kind.
IXD_WHERE = {
    "maintained-or-fixed": {
        "maintained-in-the-model-fixed-in-the-row": "the model maintains the list and the row fixes "
                                                    "it",
        "fixed-in-the-model-maintained-in-the-row": "the model fixes the list and the row maintains "
                                                    "it",
        "divided-into-categories": "the model's list is divided into categories (it names "
                                   "`groups`)"},
    "act-absent": {
        "stands-on-a-form": "the row's act stands on a form",
        "stands-on-a-list": "the row's act stands on a list",
        "stands-on-a-category": "the row's act stands on a category of the menu",
        "opens-the-form-it-stands-on": "the row's act opens the very form it stands on, that is "
                                       "another record of it"},
    "fills": {"some-but-not-all": "the model's choice fills some of the values the row names, and "
                                  "not all of them"},
    "locks": {"some-but-not-all": "the model's choice locks some of the values the row names, and "
                                  "not all of them"},
}


def ixd_kind_words(check: int, kind: str, where=()) -> str:
    """A kind of disagreement, and the conditions named with it, in words, then in L021's terms."""
    words = IXD_KINDS.get(check, {}).get(kind, kind)
    conds = [IXD_WHERE.get(kind, {}).get(w, w) for w in where]
    return (words + "".join(f", and {c}" for c in conds)
            + f" (check {check}, {kind}" + (": " + ", ".join(where) if where else "") + ")")


class KitGapsError(Exception):
    """The register of the kit's gaps cannot be read, or holds an entry that is not the kit's."""


def kit_gaps(path=None) -> dict:
    """{entry id: entry} of the kit's register of its gaps. Refuses a register whose entry is not
    the kit's (`owner: kit`), or names the engagement's own kinds, or touches no check of 6 to 9,
    or names no kind of disagreement it admits in L021's terms (`admits`: a check the entry
    touches, a kind of IXD_KINDS for that check, and conditions of IXD_WHERE for that kind)."""
    p = pathlib.Path(path or KIT_GAPS)
    try:
        reg = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    except Exception as exc:                                    # noqa: BLE001
        raise KitGapsError(f"the register of the kit's gaps, {p}, cannot be read: {exc}")
    out = {}
    for g in reg.get("gaps") or []:
        gid = str(g.get("id") or "")
        words = str(g.get("gap") or "").lower()
        if not gid or g.get("owner") != "kit" or any(k in words for k in NOT_KIT_GAPS):
            raise KitGapsError(f"the register of the kit's gaps, {p}, holds the entry "
                               f"'{gid or '?'}', which is not a gap of the kit (owner: kit; the "
                               f"design's words, the model's source and its starting data are "
                               f"the engagement's own)")
        checks = [c for c in g.get("checks") or [] if c in (6, 7, 8, 9)]
        if not checks:
            raise KitGapsError(f"the register of the kit's gaps, {p}: the entry '{gid}' touches "
                               f"none of the checks 6 to 9 of rule L021")
        admits = []
        for a in g.get("admits") if isinstance(g.get("admits"), list) else []:
            a = a if isinstance(a, dict) else {}
            chk, kind = a.get("check"), str(a.get("disagreement") or "")
            where = a.get("where") or []
            where = where if isinstance(where, list) else [where]
            where = [str(w) for w in where]
            if chk not in checks or kind not in IXD_KINDS.get(chk, {}):
                raise KitGapsError(
                    f"the register of the kit's gaps, {p}: the entry '{gid}' admits "
                    f"'{kind or '?'}' on check {chk}, which is not a kind of disagreement L021 "
                    f"tells apart on a check the entry touches ({', '.join(map(str, checks))}); "
                    f"the kinds of check {chk} are "
                    f"{', '.join(IXD_KINDS.get(chk, {})) or 'none, since L021 reads no such check'}")
            unknown = [w for w in where if w not in IXD_WHERE.get(kind, {})]
            if unknown:
                raise KitGapsError(
                    f"the register of the kit's gaps, {p}: the entry '{gid}' narrows the kind "
                    f"'{kind}' by {', '.join(unknown)}, which L021 does not read of it; it reads "
                    f"{', '.join(IXD_WHERE.get(kind, {})) or 'no condition of that kind'}")
            admits.append({"check": chk, "disagreement": kind, "where": where})
        if not admits:
            raise KitGapsError(f"the register of the kit's gaps, {p}: the entry '{gid}' names no "
                               f"kind of disagreement it admits (`admits`), and a loss on it could "
                               f"admit any disagreement of its checks")
        out[gid] = dict(g, checks=checks, admits=admits)
    return out


def ixd_admits(gap: dict, check: int, kind, facts) -> bool:
    """Whether the register's entry `gap` admits a disagreement of `check` and `kind`, of which
    the conditions `facts` hold: one of its `admits` names that check and kind, and every
    condition it names holds."""
    return any(a["check"] == check and a["disagreement"] == kind and set(a["where"]) <= set(facts)
               for a in gap.get("admits") or [])


def interaction_design_gate(doc: dict, app_path, warnings: list | None = None) \
        -> tuple[list[str], str | None]:
    """L021: the nine checks of SDD-11, section 8.2. Returns (errors, the admission line), and
    appends to `warnings` each disagreement admitted as a recorded loss on a gap of the kit.

    1 the model names no interaction design; 2 it names a file that is not there; 3 the
    checksum is not the file's; 4 the document's header does not stand at baselined with a name
    and a date; 5 the document does not cover a goal the model's forms and lists name in their
    `use_case`; 6 to 9 the model's lists, references, moves and acts disagree with the Lists,
    References, Moves and Acts tables. Checks 1 to 3 stop the reading: past a failed one there
    is no document, or not the one the model names. Checks 4 to 9 are all reported.

    METHOD-2026-09-26-02, point 19 (b), and its version 3 (gap 1): a disagreement of checks 6 to 9
    that arises from a row of the document which a loss of `model.interaction_design.losses`
    covers is admitted, printed as a warning naming the loss, the entry and its round, only when
    it is of the kind the loss's entry of the kit's register of its gaps (KIT_GAPS) names in
    `admits` — its check, its kind of IXD_KINDS, and the conditions of IXD_WHERE the entry names.
    Every other disagreement stands; a loss naming no entry or an entry the register does not
    hold, covering a row on which no disagreement arises, or covering a row whose disagreement is
    of another kind than its entry admits, is refused, in words that name both kinds."""
    import interaction_design as ixd

    errs: list[str] = []
    # per error: (check, the document's line or None, its kind, the conditions that hold of it)
    err_rows: list = []
    current = {"row": None}                      # the row of the table being read, if any

    def e(check: int, where: str, msg: str, form: bool = False, kind: str | None = None,
          facts=()):
        errs.append(f"[{IXD_RULE}] {where}: check {check} — {msg}")
        # a row the gate cannot read is not a disagreement with it, and no loss admits it; a
        # disagreement with a row is of one kind that L021 tells apart (IXD_KINDS), and one
        # of no kind is admitted by no entry
        err_rows.append((check, None if form else current["row"],
                         kind if kind in IXD_KINDS.get(check, {}) else None, frozenset(facts)))

    def ef(check: int, where: str, msg: str):
        e(check, where, msg, form=True)

    model = doc.get("model") if isinstance(doc.get("model"), dict) else {}
    entry = model.get("interaction_design")
    here = "model/interaction_design"

    # ---- check 1: the model names an interaction design ---------------------------------
    if not isinstance(entry, dict) or not str(entry.get("path") or "").strip() \
            or not str(entry.get("sha256") or "").strip():
        harvested = str(model.get("spec_version") or "").endswith("-harvest")
        e(1, here, "the model names no interaction design. An application model is admitted to "
                   "generation only when its entry model.interaction_design names the interaction "
                   "design the owner accepted, by its path relative to the model and its SHA-256 "
                   "checksum (SDD-11, section 8.1). Write the interaction design of the goals this "
                   "model carries, have the owner accept it, and name it here."
                   + (" This model was harvested from a deployed application (spec_version "
                      f"{model.get('spec_version')}): it is a draft of an application nobody has "
                      "yet designed this way, and it is refused as every model is until its "
                      "interaction design is written and accepted." if harvested else ""))
        return errs, None
    path_s = str(entry["path"]).strip()
    sha = str(entry["sha256"]).strip().lower()
    if path_s.upper().startswith(IXD_QUESTION) or sha.upper().startswith(IXD_QUESTION):
        e(1, here, "the entry model.interaction_design is still the question `kit new` wrote, and "
                   "it is not answered: name the interaction design the owner accepted, by its "
                   "path relative to the model and its SHA-256 checksum (SDD-11, section 8.1).")
        return errs, None

    # ---- check 2: the file is there -----------------------------------------------------
    if app_path is None:
        e(2, here, f"the model names the interaction design '{path_s}', and the model's own "
                   f"location is not known, so the file cannot be found. The gate reads a model "
                   f"from its file.")
        return errs, None
    rel = pathlib.Path(path_s)
    if rel.is_absolute():
        e(2, here, f"the model names the interaction design by the absolute path '{path_s}'; the "
                   f"entry names it by its path relative to the model, so that the two travel "
                   f"together.")
        return errs, None
    target = (pathlib.Path(app_path).resolve().parent / rel)
    if not target.is_file():
        e(2, here, f"the model names the interaction design '{path_s}', and there is no file at "
                   f"{target}.")
        return errs, None

    # ---- check 3: the checksum is the file's ---------------------------------------------
    actual = ixd.sha256_of(target)
    if actual != sha:
        e(3, here, f"the model names the interaction design '{path_s}' with the checksum {sha}, "
                   f"and the file's SHA-256 checksum is {actual}. The document is not the one the "
                   f"model names: a document changed after it was accepted is accepted again, and "
                   f"the model names it again, before a model is admitted (SDD-11, IXD-29).")
        return errs, None

    d = ixd.read(target)
    check_of = {"header": 4, "goals": 5, "Lists": 6, "References": 7, "Moves": 8, "Acts": 9}
    for name, ln, what in d.problems:
        if name in check_of:
            e(check_of[name], f"{path_s}, line {ln}", what)
    for name in ("header", "goals", "Lists", "References", "Moves", "Acts"):
        if not d.has(name):
            cols = " · ".join(ixd.TABLES[name])
            what = {"header": "the table of its header", "goals": "the table of the goals it covers"}
            e(check_of[name], path_s,
              f"the document holds no {what.get(name, 'table ' + name)} with the headings "
              f"{cols}, written exactly so, which the gate reads (the kit's template "
              f"templates/spec/INTERACTION_DESIGN.md.tmpl)")

    def at(row) -> str:
        return f"{path_s}, line {row.line}"

    def rowname(table: str, row) -> str:
        return f"the {table} table's row '{row.label()}' (line {row.line})"

    # ---- check 4: the document stands at baselined, with a name and a date ------------------
    if d.has("header"):
        where4 = f"{path_s}, line {d.status_line}" if d.status_line else path_s
        if d.status_line is None:
            e(4, path_s, f"the table of its header has no row '{ixd.STATUS_LINE}', so the document "
                         f"states no status")
        elif d.status is None:
            e(4, where4, f"the row '{ixd.STATUS_LINE}' names none of the three status words, "
                         f"draft, reviewed or baselined")
        elif d.status != "baselined":
            e(4, where4, f"the interaction design stands at '{d.status}', and a model is written "
                         f"only from one the owner has accepted: baselined, with the name of the "
                         f"person who accepted it and the date (SDD-11, IXD-4)")
        else:
            name = d.accepted_by or ""
            placeholder = (not name or any(c in name for c in "<>{}")
                           or name.upper().startswith(("TODO", IXD_QUESTION)))
            if placeholder:
                e(4, where4, "the interaction design reads baselined and names nobody who accepted "
                             "it: the row says 'accepted by <the name> on <the date>' (SDD-11, "
                             "IXD-4)")
            elif d.accepted_on is None:
                e(4, where4, f"the interaction design reads baselined, accepted by {name}, and "
                             f"gives no date the gate can read: it is written '25 September 2026' "
                             f"or '2026-09-25'"
                             + (f" (it reads '{d.accepted_on_text}')" if d.accepted_on_text else ""))
            elif d.accepted_on > datetime.date.today() + datetime.timedelta(days=1):
                e(4, where4, f"the interaction design reads accepted by {name} on "
                             f"{d.accepted_on_text}, a day that has not yet come")

    # ---- check 5: every goal the model's forms and lists name is covered ---------------------
    goals = {g for g, _ in d.goals}
    if d.has("goals"):
        gl = d.table_lines.get("goals")
        for coll in ("forms", "lists"):
            for obj in doc.get(coll) or []:
                uc = str(obj.get("use_case") or "").strip()
                if not uc:
                    continue
                gid = uc.split("/")[0].strip()
                if gid not in goals:
                    e(5, f"{coll}/{obj.get('id')}",
                      f"the {coll[:-1]} '{obj.get('name') or obj.get('id')}' realises the goal "
                      f"{gid}, and the interaction design does not cover it: its table of goals "
                      f"(line {gl}) names {', '.join(sorted(goals)) or 'none'}")

    entities = {x.get("id"): x for x in doc.get("entities") or []}
    forms = {x.get("id"): x for x in doc.get("forms") or []}
    lists = {x.get("id"): x for x in doc.get("lists") or []}
    vocabs = {x.get("id"): x for x in doc.get("vocabularies") or []}
    cats = {c.get("id"): c for c in ((doc.get("navigation") or {}).get("categories") or [])}

    # ---- check 6: the lists -------------------------------------------------------------
    import lov

    def vrows(v):
        try:
            return lov.rows_of(v, app_path)
        except lov.LovError:
            return list(v.get("rows") or [])

    for row in d.tables.get("Lists", []):
        current["row"] = row.line                     # a disagreement here arises from this row
        ids = row.ids("List")
        if not ids:
            if not ixd.says_not_in_the_model(row.text("List")):
                ef(6, at(row), f"{rowname('Lists', row)} names no list of the model: its List cell "
                              f"carries no identifier between backticks and does not read "
                              f"'{ixd.NOT_IN_THE_MODEL}'")
            continue
        if len(ids) > 1:
            ef(6, at(row), f"{rowname('Lists', row)} names {len(ids)} lists ({', '.join(ids)}); a row "
                          f"names one")
            continue
        vid = ids[0]
        v = vocabs.get(vid)
        if v is None:
            e(6, at(row), f"{rowname('Lists', row)} names the list {vid}, which is not a list of the "
                          f"model (vocabularies)", kind="list-absent")
            continue
        vname = f"the list {v.get('name') or vid} ({vid})"
        mf = ixd.first_of(row.text("Maintained or fixed"), ("maintained", "fixed"))
        fixed = bool(v.get("fixed"))
        if mf is None:
            ef(6, at(row), f"{rowname('Lists', row)} does not say whether {vname} is maintained or "
                          f"fixed")
        elif (mf == "fixed") != fixed:
            e(6, f"vocabularies/{vid}",
              f"{vname} is {'fixed' if fixed else 'maintained in the application'} in the model, "
              f"and {rowname('Lists', row)} decides it is {mf}", kind="maintained-or-fixed",
              facts=["fixed-in-the-model-maintained-in-the-row" if fixed else
                     "maintained-in-the-model-fixed-in-the-row"]
              + (["divided-into-categories"] if v.get("groups") else []))
        if mf == "maintained":
            roles = row.ids("Maintained by")
            model_role = v.get("maintained_by") or lov.admin_role(doc)
            if not roles:
                ef(6, at(row), f"{rowname('Lists', row)} names no role that maintains {vname}: its "
                              f"Maintained by cell carries no role identifier between backticks")
            elif len(roles) > 1:
                ef(6, at(row), f"{rowname('Lists', row)} names {len(roles)} roles that maintain "
                              f"{vname}; a list is maintained by one role")
            elif roles[0] != model_role:
                e(6, f"vocabularies/{vid}",
                  f"{vname} is maintained in the model by {model_role or 'no role'}"
                  f"{'' if v.get('maintained_by') else ' (the administrator, as the model names none)'}"
                  f", and {rowname('Lists', row)} decides it is maintained by {roles[0]}",
                  kind="maintained-by")
        yn = ixd.first_of(row.text("Code shown as label"), ("yes", "no"))
        dc = bool(v.get("display_code"))
        if yn is None:
            ef(6, at(row), f"{rowname('Lists', row)} reads neither yes nor no in its Code shown as "
                          f"label cell")
        elif (yn == "yes") != dc:
            e(6, f"vocabularies/{vid}",
              f"{vname} shows {'its code' if dc else 'its label'} in the model (display_code "
              f"{str(dc).lower()}), and {rowname('Lists', row)} decides "
              f"{'its code is shown as its label' if yn == 'yes' else 'its label is shown'}",
              kind="code-shown")
        m = re.match(r"\s*(\d+)\b", row.text("Members in force"))
        members = int(m.group(1)) if m else len(vrows(v))
        cat_ids = row.ids("Categories")
        groups = v.get("groups")
        if cat_ids:
            gvid, codes = cat_ids[0], cat_ids[1:]
            if groups != gvid:
                e(6, f"vocabularies/{vid}",
                  f"{rowname('Lists', row)} divides {vname} into the categories of {gvid}, and "
                  f"the model's list names {('the categories of ' + groups) if groups else 'no categories'}",
                  kind="categories")
            elif codes:
                have = [str(r.get("code")) for r in vrows(vocabs.get(gvid) or {})]
                if set(codes) != set(have):
                    e(6, f"vocabularies/{gvid}",
                      f"{rowname('Lists', row)} gives {vname} the categories "
                      f"{', '.join(codes)}, and the model's list {gvid} holds "
                      f"{', '.join(have) or 'none'}", kind="category-members")
        elif ixd.reads_as(row.text("Categories"), "none"):
            if groups:
                e(6, f"vocabularies/{vid}",
                  f"{rowname('Lists', row)} gives {vname} no categories, and the model divides it "
                  f"into the categories of {groups}", kind="categories")
        else:
            ef(6, at(row), f"{rowname('Lists', row)} names no list of categories between backticks "
                          f"in its Categories cell, and does not read none")
        if members > IXD_MOST and not groups:
            e(6, f"vocabularies/{vid}",
              f"{rowname('Lists', row)} counts {members} members in force, more than nine, and "
              f"the model's {vname} carries no `groups`: a list of more than nine values is chosen "
              f"by category (UX-01 IDR-05; the ruling on long lists)", kind="long-list-undivided")

    # ---- check 7: the references ----------------------------------------------------------
    current["row"] = None
    dd = load_dd(doc, app_path)
    for row in d.tables.get("References", []):
        current["row"] = row.line
        ids = row.ids("Place")
        if not ids:
            if not ixd.says_not_in_the_model(row.text("Place")):
                ef(7, at(row), f"{rowname('References', row)} names no place of the model: its Place "
                              f"cell carries neither a form's field (form.field) nor a list between "
                              f"backticks, and does not read '{ixd.NOT_IN_THE_MODEL}'")
            continue
        if len(ids) > 1:
            ef(7, at(row), f"{rowname('References', row)} names {len(ids)} places ({', '.join(ids)}); "
                          f"a row names one")
            continue
        pid = ids[0]
        if "." not in pid:
            if pid not in lists:
                e(7, at(row), f"{rowname('References', row)} names {pid}, which is neither a form's "
                              f"field, written form.field, nor a list of the model",
                  kind="place-absent")
            continue
        fid, fld_id = pid.split(".", 1)
        form = forms.get(fid)
        if form is None:
            e(7, at(row), f"{rowname('References', row)} names the form {fid}, which is not a form "
                          f"of the model", kind="place-absent")
            continue
        ent = entities.get(form.get("entity")) or {}
        attrs = {a.get("id"): a for a in ent.get("attributes") or []}
        placed = {}
        ro = set()
        for sec in form.get("sections") or []:
            for f in sec.get("fields") or []:
                key = f.get("attr") or f.get("id")
                placed[key] = f
                if f.get("readonly") or sec.get("readonly"):
                    ro.add(key)
        fld = placed.get(fld_id)
        if fld is None:
            e(7, at(row), f"{rowname('References', row)} names the value {fld_id} of the form "
                          f"{fid}, and the form places no such field", kind="value-not-placed")
            continue
        where7 = f"forms/{fid}/{fld_id}"
        ctrl = _ixd_control(fld, attrs.get(fld.get("attr")) or {}, dd)
        if ixd.reads_as(row.text("Found by"), "a search") and ctrl in IXD_DROPDOWNS:
            e(7, where7, f"{rowname('References', row)} finds the record by a search, and the model "
                         f"places {fld_id} on the form {fid} as {IXD_DROPDOWNS[ctrl]} (control "
                         f"'{ctrl}'): a record found by a search is never chosen from a drop-down "
                         f"(UX-01 IDR-05)", kind="search-as-drop-down")
        fills: set = set()
        locks: set = set()
        pf = form.get("prefill") or {}
        if any(str(ks.get("source", "")).lower() == "currentfield" and ks.get("name") == fld_id
               for ks in pf.get("keySources") or []):
            fills |= {str(m.get("to")) for m in pf.get("mappings") or [] if m.get("to")}
        lk = form.get("lookup") or {}
        if lk.get("watch") == fld_id:
            fills |= {str(m.get("to")) for m in lk.get("mappings") or [] if m.get("to")}
        locks |= fills & ro
        pop = _ixd_populate_targets((fld.get("config") or {}).get("populate"))
        fills |= pop
        locks |= pop                                  # the kit locks what a search fills
        t_fills = set(row.ids("Fills"))
        if not t_fills and not ixd.reads_as(row.text("Fills"), "nothing"):
            ef(7, at(row), f"{rowname('References', row)} names in its Fills cell no value of the "
                          f"form between backticks, and does not read nothing")
            continue
        if t_fills != fills:
            e(7, where7, f"the choice at {fld_id} on the form {fid} fills "
                         f"{', '.join(sorted(fills)) or 'nothing'} in the model, and "
                         f"{rowname('References', row)} says it fills "
                         f"{', '.join(sorted(t_fills)) or 'nothing'}", kind="fills",
              facts=["some-but-not-all"] if fills and fills < t_fills else [])
        t_locks = set(row.ids("Locks"))
        if not t_locks:
            if ixd.reads_as(row.text("Locks"), "everything it fills"):
                t_locks = set(t_fills)
            elif not ixd.reads_as(row.text("Locks"), "nothing"):
                ef(7, at(row), f"{rowname('References', row)} names in its Locks cell no value "
                              f"between backticks, and reads neither nothing nor everything it "
                              f"fills")
                continue
        if t_locks != locks:
            e(7, where7, f"the choice at {fld_id} on the form {fid} locks "
                         f"{', '.join(sorted(locks)) or 'nothing'} in the model, and "
                         f"{rowname('References', row)} says it locks "
                         f"{', '.join(sorted(t_locks)) or 'nothing'}", kind="locks",
              facts=["some-but-not-all"] if locks and locks < t_locks else [])

    # ---- check 8: the moves ----------------------------------------------------------------
    current["row"] = None
    import acts as acts_mod
    offered = []                                       # (entity, move, label, roles, form)
    for fid, form in forms.items():
        ent = entities.get(form.get("entity"))
        if not ent:
            continue
        for a in acts_mod.acts_of(form, ent):
            if a.get("kind") == "move":
                offered.append((ent.get("id"), a.get("transition"), str(a.get("label")),
                                frozenset(a.get("roles") or []), fid))
    listed: set = set()                                # (entity, move, button) the table lists
    for row in d.tables.get("Moves", []):
        current["row"] = row.line
        rec = row.ids("Record")
        made = row.ids("Made by (goal, act)")
        if not made and ixd.says_not_in_the_model(row.text("Made by (goal, act)")):
            continue
        if len(rec) != 1:
            ef(8, at(row), f"{rowname('Moves', row)} names {'no record' if not rec else str(len(rec)) + ' records'} "
                          f"of the model in its Record cell; a row names the record's entity "
                          f"between backticks")
            continue
        if len(made) != 1:
            ef(8, at(row), f"{rowname('Moves', row)} names {'no move' if not made else str(len(made)) + ' moves'} "
                          f"of the model in its Made by cell; a row names the move's identifier "
                          f"between backticks, or reads '{ixd.NOT_IN_THE_MODEL}'")
            continue
        eid, tid = rec[0], made[0]
        ent = entities.get(eid)
        if ent is None:
            e(8, at(row), f"{rowname('Moves', row)} names the record {eid}, which is not an entity "
                          f"of the model", kind="record-absent")
            continue
        trans = {t.get("id"): t for t in ((ent.get("lifecycle") or {}).get("transitions") or [])}
        t = trans.get(tid)
        if t is None:
            e(8, at(row), f"{rowname('Moves', row)} names the move {tid}, which is not a move of the "
                          f"lifecycle of {eid}", kind="move-absent")
            continue
        frm, to = row.ids("From"), row.ids("To")
        if frm[:1] != [t.get("from")] or to[:1] != [t.get("to")]:
            e(8, f"entities/{eid}/lifecycle/transitions/{tid}",
              f"{rowname('Moves', row)} moves {eid} from {frm[0] if frm else '(no state named)'} to "
              f"{to[0] if to else '(no state named)'}, and the model's move {tid} goes from "
              f"{t.get('from')} to {t.get('to')}", kind="move-states")
        btext = " ".join(row.text("Button").split())
        buttons = [] if ixd.reads_as(btext, "none") else \
            [b.strip().strip('"“”‘’\'').strip() for b in btext.split(";") if b.strip()]
        roles = frozenset(row.ids("Role"))
        here_acts = [o for o in offered if o[0] == eid and o[1] == tid]
        if not buttons:
            for o in here_acts:
                e(8, f"forms/{o[4]}",
                  f"{rowname('Moves', row)} says no act of this increment makes the move {tid} of "
                  f"{eid}, and the model's form {o[4]} offers it as the button '{o[2]}'",
                  kind="button-offered")
            continue
        if not roles:
            ef(8, at(row), f"{rowname('Moves', row)} names no role between backticks in its Role "
                          f"cell")
        for b in buttons:
            listed.add((eid, tid, b))
            match = [o for o in here_acts if o[2] == b]
            if not match:
                have = sorted({o[2] for o in here_acts})
                e(8, f"entities/{eid}/lifecycle/transitions/{tid}",
                  f"{rowname('Moves', row)} makes the move {tid} of {eid} by the button '{b}', and "
                  f"no form of {eid} in the model offers that button for it"
                  + (f" (the model's buttons for it read {', '.join(repr(x) for x in have)})"
                     if have else " (the model offers no button for it)"), kind="button-absent")
                continue
            for o in match:
                if roles and o[3] != roles:
                    e(8, f"forms/{o[4]}",
                      f"the button '{b}' on the form {o[4]} makes the move {tid} for "
                      f"{', '.join(sorted(o[3])) or 'no role'}, and {rowname('Moves', row)} gives "
                      f"the move to {', '.join(sorted(roles))}", kind="button-roles")
    current["row"] = None                             # read the other way: from no row
    for o in offered:
        if (o[0], o[1], o[2]) not in listed:
            e(8, f"forms/{o[4]}",
              f"the model's form {o[4]} offers the button '{o[2]}', which makes the move {o[1]} of "
              f"{o[0]}, and the Moves table lists no such act as a person's",
              kind="button-unlisted")

    # ---- check 9: the acts that open a form --------------------------------------------------
    def on_the_menu(mn: dict, o_id) -> bool:
        """Whether the menu `mn` puts `o_id` on the menu (METHOD-2026-09-26-02, point 18). A CRUD
        menu shows its list from the menu, and puts its form there only through its New button:
        with the button off (`add: false`) the form, and an `edit_form` always, is opened from the
        list's rows and stands on no menu. A form menu puts its form there, a list menu its list."""
        if mn.get("type") == "crud":
            return o_id == mn.get("list") or (o_id == mn.get("form") and mn.get("add") is not False)
        return o_id in (mn.get("form"), mn.get("list"))

    for row in d.tables.get("Acts", []):
        current["row"] = row.line
        by_search = False                                 # the act is a search's choice (below)
        stands, opens = row.ids("Stands on"), row.ids("Opens")
        if not stands and not opens and (ixd.says_not_in_the_model(row.text("Stands on"))
                                         or ixd.says_not_in_the_model(row.text("Opens"))):
            continue
        if len(stands) != 1 or len(opens) != 1:
            ef(9, at(row), f"{rowname('Acts', row)} names {len(stands)} places in its Stands on cell "
                          f"and {len(opens)} in its Opens cell; a row names, between backticks, the "
                          f"one form, list or category of the model the act stands on and the one "
                          f"form it opens")
            continue
        s_id, o_id = stands[0], opens[0]
        kinds = [k for k, coll in (("form", forms), ("list", lists), ("category", cats)) if s_id in coll]
        if len(kinds) != 1:
            e(9, at(row), f"{rowname('Acts', row)} stands on {s_id}, which "
                          + ("is no form, list or category of the model" if not kinds else
                             f"names a {' and a '.join(kinds)} of the model at once"),
              kind="stands-on-two" if kinds else "stands-on-absent")
            continue
        kind = kinds[0]
        carried: list = []                                # what each act found there carries
        if kind == "form":
            host = forms[s_id]
            ent = entities.get(host.get("entity")) or {"id": host.get("entity")}
            # METHOD-2026-09-28-07 (the kit's gap G1, removed): an act that opens the very form it
            # stands on, for another record of it, is an act that stands on a value of the form
            # naming that record (`stands_on`); one that names no value opens the record already
            # open, and is no such act
            carried = [a.get("carries") for a in acts_mod.acts_of(host, ent)
                       if a.get("kind") == "form" and a.get("form") == o_id
                       and (s_id != o_id or a.get("stands_on"))]
        elif kind == "list":
            lst = lists[s_id]
            row_ent = list_record_entity(lst, doc) or (forms.get(o_id) or {}).get("entity")
            # METHOD-2026-09-28-07 (the kit's gap G1, removed): a row's act carries the record its
            # column names (`record`, `carries`), and opens a form or a list; an act on the rows
            # chosen (`chosen_actions`) carries the chosen rows' records
            for a in lst.get("actions") or []:
                if (a.get("type") == "open_form" and a.get("form") == o_id) or \
                        (a.get("type") == "open_list" and a.get("list") == o_id):
                    carried.append(row_act_carries(a, lst, doc) or row_ent)
            for a in lst.get("chosen_actions") or []:
                if a.get("form") == o_id:
                    carried.append(row_act_carries(a, lst, doc) or row_ent)
            # METHOD-2026-09-28-01 (the kit's gap G4, removed): a list that is the result of a
            # search the form it opens places is chosen from by that search, and the choice is the
            # act — it carries the record the search looks in. The form is already open where the
            # search stands, so what the act opens stands on no menu of its own: the row's On a
            # menu cell is not read against the form's place on the menu.
            found_in = _ixd_searches(forms.get(o_id) or {}, entities, lists, dd).get(s_id)
            if not carried and found_in:
                carried, by_search = [found_in], True
        else:
            for mn in cats[s_id].get("menus") or []:
                if mn.get("type") == "crud" and o_id == (mn.get("edit_form") or mn.get("form")):
                    carried.append(mn.get("entity"))
                elif mn.get("type") in ("form", "crud") and o_id in (mn.get("form"), mn.get("edit_form")):
                    carried.append(None)
                elif mn.get("type") in ("list", "crud") and mn.get("list") == o_id:
                    # point 18: a CRUD menu shows its list from the menu, as a list menu does,
                    # and the act that opens the list carries nothing
                    carried.append(None)
        if not carried:
            e(9, at(row), f"{rowname('Acts', row)} has an act on the {kind} {s_id} that opens "
                          f"{o_id}, and the model's {kind} {s_id} has no act that opens it",
              kind="act-absent",
              facts=[f"stands-on-a-{kind}"]
              + (["opens-the-form-it-stands-on"] if kind == "form" and s_id == o_id else []))
            continue
        c_ids = row.ids("Carries")
        if c_ids:
            for c in carried:
                if c != c_ids[0]:
                    e(9, f"{kind}s/{s_id}" if kind != "category" else f"navigation/{s_id}",
                      f"the act on the {kind} {s_id} that opens {o_id} carries "
                      f"{('a record of ' + str(c)) if c else 'no record'} in the model, and "
                      f"{rowname('Acts', row)} says it carries a record of {c_ids[0]}",
                      kind="carries")
        elif not ixd.reads_as(row.text("Carries"), "nothing"):
            ef(9, at(row), f"{rowname('Acts', row)} names in its Carries cell no record between "
                          f"backticks, and does not read nothing")
        menu = ixd.first_of(row.text("On a menu"), ("yes", "no"))
        if menu is None:
            ef(9, at(row), f"{rowname('Acts', row)} reads neither yes nor no in its On a menu cell")
        elif menu == "no" and not by_search:
            for cid, cat in cats.items():
                if cat.get("hidden"):
                    continue
                for mn in cat.get("menus") or []:
                    if on_the_menu(mn, o_id):
                        e(9, f"navigation/{cid}/{mn.get('label')}",
                          f"{o_id} stands on the visible menu '{mn.get('label')}' of the category "
                          f"'{cat.get('label') or cid}', and {rowname('Acts', row)} says the form "
                          f"it opens stands on no menu", kind="on-a-menu")
    current["row"] = None

    # ---- the losses the model records on the kit's own gaps (METHOD-2026-09-26-02, point 19 (b))
    decision_rows = {r.line for t in ("Lists", "References", "Moves", "Acts")
                     for r in d.tables.get(t, [])}
    losses = entry.get("losses") if isinstance(entry.get("losses"), list) else []
    admitted_idx: dict = {}                      # error index -> (loss id, gap id)
    loss_errs: list = []
    if losses:
        try:
            register = kit_gaps()
        except KitGapsError as exc:
            register = None
            loss_errs.append(f"[{IXD_RULE}] {here}/losses: the recorded losses — {exc}")
        seen_ids: set = set()
        for n, loss in enumerate(losses):
            loss = loss if isinstance(loss, dict) else {}
            lid = str(loss.get("id") or f"#{n + 1}")
            where = f"{here}/losses/{lid}"
            gid = str(loss.get("gap") or "").strip()
            rows = [r for r in loss.get("rows") or [] if isinstance(r, int)]
            if lid in seen_ids:
                loss_errs.append(f"[{IXD_RULE}] {where}: the recorded losses — the loss {lid} is "
                                 f"recorded twice")
                continue
            seen_ids.add(lid)
            if not gid:
                loss_errs.append(f"[{IXD_RULE}] {where}: the recorded losses — the loss {lid} "
                                 f"names no entry of the kit's register of its gaps; a disagreement "
                                 f"is admitted only on a gap the kit names as its own, while the "
                                 f"estate's round that removes it is open")
                continue
            if register is None:
                continue
            gap = register.get(gid)
            if gap is None:
                loss_errs.append(f"[{IXD_RULE}] {where}: the recorded losses — the loss {lid} "
                                 f"names {gid}, which is not an entry of the kit's register of its "
                                 f"gaps (templates/spec/kit-gaps.yaml); the register holds "
                                 f"{', '.join(sorted(register)) or 'none'}. An "
                                 f"entry leaves the register when the round that removes the gap "
                                 f"is done, and the model then agrees with the document")
                continue
            if not rows:
                loss_errs.append(f"[{IXD_RULE}] {where}: the recorded losses — the loss {lid} "
                                 f"covers no row of the document")
                continue
            for r in rows:
                # the disagreements that arise from the row and no other loss has admitted
                there = [i for i, x in enumerate(err_rows) if x[1] == r and i not in admitted_idx]
                if r not in decision_rows or not there:
                    loss_errs.append(
                        f"[{IXD_RULE}] {where}: the recorded losses — the loss {lid} covers the "
                        f"document's line {r}, and no disagreement "
                        + ("arises there that its entry " if r in decision_rows else
                           "can arise there, since it is no row of the Lists, References, Moves "
                           "or Acts tables, that its entry ")
                        + f"{gid} (checks {', '.join(map(str, gap['checks']))}) may admit: a loss "
                          f"covers only the rows whose disagreement it records")
                    continue
                # version 3, gap 1: only a disagreement of the kind its entry names is admitted
                took = [i for i in there if err_rows[i][0] in gap["checks"]
                        and ixd_admits(gap, err_rows[i][0], err_rows[i][2], err_rows[i][3])]
                other = [i for i in there if i not in took]
                if other:
                    kinds_there = []
                    for i in other:
                        chk, _, knd, facts = err_rows[i]
                        words = (ixd_kind_words(chk, knd, sorted(facts & set(IXD_WHERE.get(knd, {}))))
                                 if knd else f"of no kind L021 tells apart (check {chk})")
                        if words not in kinds_there:
                            kinds_there.append(words)
                    loss_errs.append(
                        f"[{IXD_RULE}] {where}: the recorded losses — the loss {lid} covers the "
                        f"document's line {r}, where the disagreement"
                        + (" is: " if len(other) == 1 else f"s ({len(other)}) are: ")
                        + "; and ".join(kinds_there)
                        + f". Its entry {gid} (checks {', '.join(map(str, gap['checks']))}) "
                          f"admits only: "
                        + "; or ".join(ixd_kind_words(a["check"], a["disagreement"], a["where"])
                                       for a in gap["admits"])
                        + ". A loss admits only the kind of disagreement its entry names, and "
                          + ("this one stands" if len(other) == 1 else
                             f"these {len(other)} stand"))
                for i in took:
                    admitted_idx[i] = (lid, gid)
        for i, (lid, gid) in sorted(admitted_idx.items()):
            if warnings is not None:
                warnings.append(f"{errs[i]} — admitted as the recorded loss {lid}, on the kit's "
                                f"gap {gid}, which the estate's round names open: "
                                f"{' '.join(str(register[gid].get('round', '')).split())}")
    errs = [x for i, x in enumerate(errs) if i not in admitted_idx] + loss_errs

    if errs:
        return errs, None
    n_rows = sum(len(d.tables.get(t, [])) for t in ("Lists", "References", "Moves", "Acts"))
    return [], (f"admitted — {path_s}, baselined, accepted by {d.accepted_by} on "
                f"{d.accepted_on_text}; SHA-256 {actual[:12]}…; {len(goals)} goal(s) covered, "
                f"{n_rows - len({err_rows[i][1] for i in admitted_idx})} row(s) of its Lists, "
                f"References, Moves and Acts tables agree with the model"
                + (f", and {len(admitted_idx)} disagreement(s) on "
                   f"{len({err_rows[i][1] for i in admitted_idx})} row(s) are admitted as "
                   f"recorded losses on the kit's own gaps" if admitted_idx else ""))


def interaction_design_report(doc: dict, app_path, out=print) -> list[str]:
    """Print the gate's verdict in the words every entry point uses. Returns the errors. Each
    disagreement admitted as a recorded loss on a gap of the kit is printed under the verdict, as
    a warning (`~`), before the errors that stand (`-`) (METHOD-2026-09-26-02, point 19 (b))."""
    warns: list = []
    errs, admitted = interaction_design_gate(doc, app_path, warns)
    if errs:
        out(f"INTERACTION DESIGN: refused — {len(errs)} error(s) ({IXD_RULE}, SDD-11 section 8; an "
            f"error in every custody mode, and nothing turns it off)"
            + (f"; {len(warns)} disagreement(s) admitted as recorded losses" if warns else ""))
    else:
        out(f"INTERACTION DESIGN: {admitted}")
    for w in warns:
        out(f"  ~ {w}")
    for x in errs:
        out(f"  - {x}")
    return errs


def admit_or_refuse(app_path, verb: str) -> int:
    """The gate as `kit gen`, `build_app.py`, `kit deploy` and `deploy_dx9.py` run it, before
    anything else: 0 when the model at `app_path` is admitted, 2 when it is refused (and the
    caller does nothing more). The same function as `kit validate` runs, so that a refusal in
    one verb is a refusal in every other."""
    p = pathlib.Path(app_path)
    try:
        doc = load(p)
    except Exception as exc:                                    # noqa: BLE001
        print(f"{verb}: REFUSED — the model {p} cannot be read: {exc}")
        return 2
    if not isinstance(doc, dict):
        print(f"{verb}: REFUSED — {p} holds no application model")
        return 2
    errs = interaction_design_report(doc, p)
    if errs:
        print(f"{verb}: REFUSED by the interaction design gate — nothing was done. The model "
              f"{p.name} is admitted only when it names the interaction design the owner "
              f"accepted and agrees with it (SDD-11, section 8).")
        return 2
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("app", type=pathlib.Path)
    ap.add_argument("--schema", type=pathlib.Path, default=DEFAULT_SCHEMA)
    args = ap.parse_args()

    schema = load(args.schema)
    doc = load(args.app)

    # L021 first: the interaction design gate (SDD-11 section 8), an error in every custody
    # mode. It is printed before everything else, and validation then goes on so that the
    # writer sees every other finding too; the exit is never 0 while the gate refuses.
    gate = interaction_design_report(doc if isinstance(doc, dict) else {}, args.app)

    errs = schema_errors(schema, doc)
    if errs:
        print(f"SCHEMA: {len(errs)} error(s)")
        for e in errs:
            print(f"  - {e}")
        return 1
    print("SCHEMA: ok")

    linter = Lint(doc, args.app)
    lint = linter.run()
    if lint:
        print(f"LINT:   {len(lint)} error(s)")
        for e in lint:
            print(f"  - {e}")
        return 2
    for w in linter.warnings:
        print(f"  ~ {w}")
    print("LINT:   ok")

    derrs, dwarns = PlatformRules(doc).run()
    for w in dwarns:
        print(f"  ~ {w}")
    if derrs:
        print(f"DELTA:  {len(derrs)} error(s)" + (f", {len(dwarns)} warning(s)" if dwarns else ""))
        for e in derrs:
            print(f"  - {e}")
        return 2
    print("DELTA:  ok" + (f" ({len(dwarns)} warning(s))" if dwarns else ""))

    cerrs, cwarns = ContractRules(doc, load_mirror()).run()
    for w in cwarns:
        print(f"  ~ {w}")
    if cerrs:
        print(f"CONTRACT: {len(cerrs)} error(s)" + (f", {len(cwarns)} warning(s)" if cwarns else ""))
        for e in cerrs:
            print(f"  - {e}")
        return 2
    print("CONTRACT: ok" + (f" ({len(cwarns)} warning(s))" if cwarns else ""))
    ne = len(doc.get("entities", []))
    print(f"MODEL:  {ne} entities · {len(doc.get('forms', []))} forms · "
          f"{len(doc.get('lists', []))} lists · {len(doc.get('processes', []))} processes · "
          f"{len(doc.get('acceptance', {}).get('scenarios', []))} scenarios")
    if gate:
        print(f"REFUSED: the interaction design gate ({IXD_RULE}) refuses this model — "
              f"{len(gate)} error(s), printed first above")
        return 2

    # PROJECTION (ADR-107; a delivery's hand-off of 5 October 2026, item 1): a model admitted is one
    # the kit can generate. Every projector of `kit gen all` is tried over the model, as `kit gen`
    # runs it, in a folder of its own, and each refusal it prints is an error here, in its own
    # words. The layer runs last, on a model every layer above admits, because a projector refuses
    # an invalid model before it projects and `kit gen` projects nothing L021 refuses. Until this
    # layer, the validator admitted one application's model (exit 0) while the form projector refused
    # 28 of its constructs (one delivery's commission); the projectors refused 152 of a trial of
    # another application's model, of four kinds the validator could have stated from the model alone.
    import projection_trial
    found = projection_trial.refusals(args.app)
    if found:
        print(f"PROJECTION: {len(found)} error(s) — the kit's projectors refuse what this model "
              f"declares, and `kit gen` writes nothing for it")
        for target, sentence in found:
            print(f"  - {target}: {sentence}")
        return 2
    print(f"PROJECTION: ok ({len(projection_trial.GEN_SCRIPTS)} projectors)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
