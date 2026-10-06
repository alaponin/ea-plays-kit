#!/usr/bin/env python3
"""Views projector (schema-0.2 primitives, G8.5) — realizes `effective_dating` and `views` so
they are NOT silently flattened (the §2.4 failure). Emits, deterministically + provenance-stamped:

 - per effective-dated entity: a *currently-effective* datalist realization — a JDBC binder whose
   SQL filters to rows valid as-at today (validity interval), i.e. temporal semantics, not two
   inert date fields;
 - per detail `view`: a composite 360 spec — the main form + child records as one detail surface,
   not disconnected forms.

    project_views.py <app.yaml> --out <dir>   ->  <dir>/views-spec.yaml
"""
from __future__ import annotations
import argparse
import hashlib
import pathlib
import sys

import yaml

import validate as l1
import custody

PROJECTOR = "project_views.py"
PROJECTOR_VERSION = "0.1.0"


def build(doc: dict) -> dict:
    out = {"effective_views": [], "detail_views": []}
    for e in doc.get("entities", []):
        ed = e.get("effective_dating")
        if not ed:
            continue
        frm, to = ed["from"], ed.get("to")
        table = e.get("table", e["id"])
        cond = f"c_{frm} <= CURRENT_DATE"
        if to:
            cond += f" AND (c_{to} IS NULL OR c_{to} >= CURRENT_DATE)"
        out["effective_views"].append({
            "id": f"list_{e['id']}_effective",
            "name": f"Currently-effective {e.get('name', e['id'])}",
            "realizes": "effective_dating",
            "entity": e["id"],
            "binder": {"type": "jdbc",
                       "sql": f"SELECT * FROM app_fd_{table} WHERE {cond}"},
        })
    for v in doc.get("views", []):
        if v.get("kind") != "detail":
            continue
        out["detail_views"].append({
            "id": v["id"], "name": v.get("name", v["id"]),
            "realizes": "composite_detail_view", "entity": v["entity"],
            "sections": v.get("sections", []),
        })
    return out


def provenance_header(doc, source_name, sha):
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
    a = ap.parse_args()
    schema = l1.load(a.schema)
    doc = l1.load(a.app)
    errs = l1.schema_errors(schema, doc)
    if errs:
        print(f"SCHEMA: {len(errs)} error(s) — refusing to project")
        [print(f"  - {e}") for e in errs]
        return 1
    print("SCHEMA: ok")
    spec = build(doc)
    sha = hashlib.sha256(a.app.read_bytes()).hexdigest()
    a.out.mkdir(parents=True, exist_ok=True)
    body = yaml.safe_dump(spec, sort_keys=False, allow_unicode=True, width=4096)
    (a.out / "views-spec.yaml").write_text(provenance_header(doc, a.app.name, sha) + custody.line(a.custody) + body,
                                           encoding="utf-8")
    print(f"views: {len(spec['effective_views'])} effective-dated + {len(spec['detail_views'])} "
          f"detail(360) realization(s) -> {a.out}/views-spec.yaml")
    return 0


if __name__ == "__main__":
    sys.exit(main())
