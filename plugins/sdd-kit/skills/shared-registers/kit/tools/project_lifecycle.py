#!/usr/bin/env python3
"""Lifecycle projector — entities[].lifecycle (L1) → StatusManager runtime seed (G2).

Closes Gap 3 (S2C-01 §2.4): emits the state machine as DATA — deterministic, provenance-
stamped seed rows for the StatusManager metamodel tables `mmEntityState` and
`mmEntityTransition` (read at runtime via MmConfigService / StatusManager). See
tools/MAPPING-lifecycle.md for the field-by-field contract. Only entities whose
`lifecycle.engine == status_framework` produce a seed (`native` = plain field updates, skipped).

Pure: same model → byte-identical seed. Refuses invalid input (transition to/from an unknown
state; no initial state).

    project_lifecycle.py <app.yaml> --out <dir>   ->  <dir>/lifecycle-seed.yaml
"""
from __future__ import annotations
import argparse
import hashlib
import pathlib
import sys
import uuid

import yaml

import validate as l1
import custody

PROJECTOR = "project_lifecycle.py"
PROJECTOR_VERSION = "0.1.0"
SCOPE_DEFAULT = "DEFAULT"


def _bool(v) -> str:
    return "true" if v else ""


def build_seed(doc: dict) -> tuple[dict, list[str]]:
    """Return ({mmEntityState:[...], mmEntityTransition:[...]}, errors)."""
    states_out: list[dict] = []
    trans_out: list[dict] = []
    errs: list[str] = []
    for e in doc.get("entities", []):
        lc = e.get("lifecycle")
        if not lc or lc.get("engine", "status_framework") != "status_framework":
            continue
        eid = e["id"]
        state_ids = {s["id"] for s in lc.get("states", [])}
        if not any(s.get("initial") for s in lc.get("states", [])):
            errs.append(f"entity '{eid}': lifecycle has no initial state")
        for s in lc.get("states", []):
            states_out.append({
                "entity": eid, "scope": SCOPE_DEFAULT, "code": s["id"],
                "name": s.get("name") or s["id"].replace("_", " ").capitalize(),
                "isInitial": _bool(s.get("initial")), "isTerminal": _bool(s.get("terminal")),
            })
        for t in lc.get("transitions", []):
            for end in ("from", "to"):
                if t[end] not in state_ids:
                    errs.append(f"entity '{eid}': transition '{t['id']}' {end} '{t[end]}' "
                                f"is not a declared state")
            audited = any((ef.get("type") == "audit") for ef in t.get("effects", []))
            trans_out.append({
                "entity": eid, "scope": SCOPE_DEFAULT,
                "fromStatus": t["from"], "toStatus": t["to"],
                "transitionCode": t["id"], "roles": ",".join(t.get("roles", []) or []),
                "event": _bool(audited),
            })
    return {"mmEntityState": states_out, "mmEntityTransition": trans_out}, errs



# Invariant metamodel/event storage forms — same for every lifecycle app; emitted so build_app
# packages them and FormDataDao/StatusManager can resolve them.
MM_FORMS = {
    "mmEntityState": ["entity", "scope", "code", "name", "isInitial", "isTerminal"],
    "mmEntityTransition": ["entity", "scope", "fromStatus", "toStatus", "transitionCode", "roles", "event"],
    "statusEvent": ["caseId", "seq", "eventType", "actor", "eventTime", "prevHash", "hash", "payload"],
}
_SEED_NS = uuid.UUID("5eed11fe-c1c1-4a00-8000-5eed5eed5eed")


def mm_form_specs() -> dict:
    """The fixed mm/event storage forms as gen_forms L2 specs."""
    return {fid: {"form": {"id": fid, "name": fid, "table": fid},
                  "sections": [{"label": fid, "columns": 1,
                                "fields": [{"id": f, "type": "textfield", "label": f} for f in fields]}]}
            for fid, fields in MM_FORMS.items()}


def mm_seed_specs(seed: dict) -> dict:
    """mmEntityState/mmEntityTransition rows as project_seed L2 specs (deploy_dx9 --seed loads them).
    Deterministic id per row -> idempotent by id."""
    out = {}
    for table in ("mmEntityState", "mmEntityTransition"):
        rows = []
        for r in seed[table]:
            rid = str(uuid.uuid5(_SEED_NS, table + "|" + "|".join(f"{k}={r[k]}" for k in sorted(r))))
            rows.append({"id": rid, "columns": {"c_" + k: v for k, v in r.items()}})
        out[table] = {"seed": {"entity": table, "table": "app_fd_" + table, "order": 5, "rows": rows}}
    return out


def _emit_yaml(spec: dict, header: str, path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    body = yaml.safe_dump(spec, sort_keys=False, default_flow_style=False, allow_unicode=True, width=4096)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(header); fh.write(body)


def provenance_header(doc: dict, source_name: str, sha: str) -> str:
    m = doc.get("model", {})
    return (
        "# =============================================================================\n"
        "# GENERATED — do not edit. Projected from the Layer-1 application model.\n"
        f"# projector:      {PROJECTOR} v{PROJECTOR_VERSION} (the spec kit)\n"
        f"# schema_version: {m.get('schema_version')}\n"
        f"# spec_version:   {m.get('spec_version')}\n"
        f"# source_model:   {source_name}\n"
        f"# source_sha256:  {sha}\n"
        "# =============================================================================\n")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("app", type=pathlib.Path)
    ap.add_argument("--out", type=pathlib.Path, required=True)
    ap.add_argument("--schema", type=pathlib.Path, default=l1.DEFAULT_SCHEMA)
    custody.add_arg(ap)
    args = ap.parse_args()

    schema = l1.load(args.schema)
    doc = l1.load(args.app)
    errs = l1.schema_errors(schema, doc)
    if errs:
        print(f"SCHEMA: {len(errs)} error(s) — refusing to project")
        [print(f"  - {e}") for e in errs]
        return 1
    print("SCHEMA: ok")
    lint = l1.Lint(doc).run()
    if lint:
        print(f"LINT:   {len(lint)} error(s) — refusing to project")
        [print(f"  - {e}") for e in lint]
        return 2
    print("LINT:   ok")

    seed, serrs = build_seed(doc)
    if serrs:
        print(f"LIFECYCLE: {len(serrs)} error(s) — refusing to project")
        [print(f"  - {e}") for e in serrs]
        return 3

    sha = hashlib.sha256(args.app.read_bytes()).hexdigest()
    header = provenance_header(doc, args.app.name, sha)
    header += custody.line(args.custody)
    args.out.mkdir(parents=True, exist_ok=True)
    out = args.out / "lifecycle-seed.yaml"
    body = yaml.safe_dump(seed, sort_keys=False, default_flow_style=False,
                          allow_unicode=True, width=4096)
    with open(out, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(header)
        fh.write(body)
    print(f"lifecycle: {len(seed['mmEntityState'])} state(s), "
          f"{len(seed['mmEntityTransition'])} transition(s) -> {out}")
    for fid, spec in mm_form_specs().items():
        _emit_yaml(spec, header, args.out / "forms" / f"F-{fid}.spec.yml")
    for table, spec in mm_seed_specs(seed).items():
        _emit_yaml(spec, header, args.out / "_seed" / f"DS-{table}.spec.yml")
    print(f"  + mm-forms ({len(MM_FORMS)}) -> {args.out}/forms ; mm-seed (2) -> {args.out}/_seed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
