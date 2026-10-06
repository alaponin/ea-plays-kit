#!/usr/bin/env python3
"""Project the workflow spec (gen_workflow input) from a Layer-1 model's `processes`.

Pure, deterministic projection under the standard projector contract (validate first incl.
delta/contract, byte-identical output, provenance-stamped, totality-refuses the unrealizable).
The target `gen_workflow` (XPDL 1.0 + the three packageActivity maps) is project-neutral —
structure driven entirely by the spec — so it is the round-trip oracle directly (like
gen_forms / gen_datalists), located via GEN_SCRIPTS_DIR.

    processes (realization: xpdl)  ->  <out>/WF-<id>.spec.yml  ->  gen_workflow  ->  package.xpdl

Scope (v0.1): human activities → manual (performer + form), `routing` → activity transitions,
participants (`role:X` → group) plus the required `processStartWhiteList`. Refused (WF-series):
`tool` activities (need the catalog component→plugin-class contract), `deadlines`, and
`realization: approval_service` (a separate DAS-config emitter, ADR-002).

Usage:
    project_workflow.py <app.yaml> --out <dir> [--schema <schema.yaml>]

Exit codes: 0 ok · 1 schema errors · 2 lint errors · 3 projection errors.
"""
from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import sys

import yaml

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import validate as l1
import custody

PROJECTOR = "project_workflow.py"
PROJECTOR_VERSION = "0.1.0"
ROLE_RE = re.compile(r"^role:([a-z][a-z0-9_]*)$")


class ProjectionError(Exception):
    """A valid L1 construct this projector cannot (yet) realize in gen_workflow."""


def project_participant(pt: dict, path: str) -> dict:
    m = ROLE_RE.match(pt.get("map", ""))
    if not m:
        raise ProjectionError(
            f"{path}: participant map '{pt.get('map')}' is not a 'role:<id>' — only role "
            f"participants are realized (as a directory group; D-020)")
    # D-020: org roles resolve as type=group (type=role is adminUser/loggedInUser only).
    return {"id": pt["id"], "name": pt["id"], "resolve": {"type": "group", "value": m.group(1)}}


def project_activity(a: dict, path: str) -> dict:
    if a["kind"] == "tool":
        raise ProjectionError(
            f"{path}: tool activities need the catalog component→plugin-class contract "
            f"(MultiTools wrapper) — not derivable in v{PROJECTOR_VERSION} (totality, WF-02)")
    if a["kind"] != "human":
        raise ProjectionError(f"{path}: unsupported activity kind '{a['kind']}'")
    return {"id": a["id"], "name": a.get("name", a["id"]), "type": "manual",
            "performer": a["participant"], "form": a["form"]}


def project_process(proc: dict) -> dict:
    pid = proc["id"]
    path = f"processes/{pid}"
    if proc.get("realization") != "xpdl":
        raise ProjectionError(
            f"{path}: realization '{proc.get('realization')}' is not xpdl — the "
            f"approval_service realization is a separate DAS-config emitter (ADR-002, WF-02)")
    if proc.get("deadlines"):
        raise ProjectionError(f"{path}: deadlines are not realized in v{PROJECTOR_VERSION} "
                              f"(escalation/timeout config; totality, WF-02)")
    participants = [project_participant(p, f"{path}/participants/{p['id']}")
                    for p in proc.get("participants", [])]
    participants.append({"id": "processStartWhiteList", "name": "processStartWhiteList",
                         "resolve": {"type": "requester"}})   # Joget start-whitelist convention
    activities = [project_activity(a, f"{path}/activities/{a['id']}")
                  for a in proc.get("activities", [])]
    act_ids = {a["id"] for a in activities}
    transitions = []
    for r in proc.get("routing", []):
        if r["after"] not in act_ids or r["goto"] not in act_ids:
            raise ProjectionError(f"{path}/routing: '{r['after']}'→'{r['goto']}' references an "
                                  f"activity that is not a projected (human) activity")
        transitions.append({"from": r["after"], "to": r["goto"]})
    return {"package": {"id": pid, "name": proc["name"]},
            "participants": participants, "variables": [],
            "processes": [{"id": pid, "name": proc["name"],
                           "activities": activities, "transitions": transitions}]}


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
        for e in errs:
            print(f"  - {e}")
        return 1
    print("SCHEMA: ok")
    if l1.Lint(doc).run():
        print("LINT:   errors — refusing to project (run kit validate)")
        return 2
    print("LINT:   ok")
    derrs, dwarns = l1.delta_contract(doc)
    for w in dwarns:
        print(f"  ~ {w}")
    if derrs:
        print(f"DELTA/CONTRACT: {len(derrs)} error(s) — refusing to project")
        for e in derrs:
            print(f"  - {e}")
        return 2
    print("DELTA/CONTRACT: ok" + (f" ({len(dwarns)} warning(s))" if dwarns else ""))

    all_procs = doc.get("processes", [])
    xpdl_procs = [p for p in all_procs if p.get("realization") == "xpdl"]
    # Make catalog-realized processes visible so "no xpdl" never reads as "forgot the workflow".
    for p in all_procs:
        if p.get("realization") != "xpdl":
            print(f"  ~ process '{p['id']}': realization '{p.get('realization')}' is "
                  f"catalog-realized (not xpdl) — handled by its component, no package emitted")
    projected, errors = [], []
    for proc in xpdl_procs:
        try:
            spec = project_process(proc)
        except ProjectionError as exc:
            errors.append(str(exc))
            continue
        projected.append((pathlib.Path(f"WF-{proc['id']}.spec.yml"), spec))

    if errors:
        print(f"PROJECT: {len(errors)} error(s) — nothing emitted")
        for e in errors:
            print(f"  - {e}")
        return 3
    if not projected:
        print("PROJECT: no xpdl processes to project")
        return 0

    sha = hashlib.sha256(args.app.read_bytes()).hexdigest()
    header = provenance_header(doc, args.app.name, sha)
    header += custody.line(args.custody)
    for rel, spec in projected:
        out_path = args.out / rel
        out_path.parent.mkdir(parents=True, exist_ok=True)
        body = yaml.safe_dump(spec, sort_keys=False, default_flow_style=False,
                              allow_unicode=True, width=4096)
        out_path.write_text(header + body, encoding="utf-8", newline="\n")
        print(f"  + {rel.as_posix()}")
    print(f"{len(projected)} workflow spec(s) projected -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
