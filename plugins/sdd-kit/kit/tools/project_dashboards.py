#!/usr/bin/env python3
"""Project the neutral dashboard spec from a Layer-1 model's `dashboards`.

Pure, deterministic projection under the standard projector contract (validate first incl.
delta/contract, byte-identical output, provenance-stamped, totality-refuses the unrealizable).
Target: the project-neutral reference generator
`joget-platform-plugins/reference-app/generators/gen_dashboards.py` (ADR-023) — SqlChartMenu
charts (server-side SQL → Apache ECharts), the native Joget way.

    dashboards (L1)  ->  <out>/<dashboardId>.dash.yml  ->  gen_dashboards  ->  chart-menu JSON

Scope (v0.1): CHART tiles → SqlChartMenu. `kpi` tiles (RAG cards) and `table` charts are
refused (totality, DB-series) — the KPI-card surface is a separate CustomHTML/API concern.

Usage:
    project_dashboards.py <app.yaml> --out <dir> [--schema <schema.yaml>]

Exit codes: 0 ok · 1 schema errors · 2 lint errors · 3 projection errors.
"""
from __future__ import annotations

import argparse
import hashlib
import pathlib
import sys

import yaml

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import validate as l1
import custody

PROJECTOR = "project_dashboards.py"
PROJECTOR_VERSION = "0.1.0"

# L1 chart_type -> SqlChartMenu chartType. `table` is not a chart (refused).
CHART_TYPES = {"bar": "bar", "line": "line", "pie": "pie", "area": "area"}


class ProjectionError(Exception):
    """A valid L1 construct this projector cannot (yet) realize in the neutral generator."""


def project_chart(tile: dict, queries: dict, path: str) -> dict:
    if tile.get("kind") != "chart":
        raise ProjectionError(
            f"{path}: only chart tiles are realized as SqlChartMenu; kind "
            f"'{tile.get('kind')}' (kpi/RAG card) has NO native single-value/threshold menu on "
            f"the platform (jw-enterprise ships only SqlChartMenu + DashboardMenu) — a KPI card "
            f"is a fragile CustomHTML/API surface, deliberately out of scope (totality, DB-02)")
    ct = tile.get("chart_type")
    if ct not in CHART_TYPES:
        raise ProjectionError(
            f"{path}: chart_type '{ct}' has no SqlChartMenu realization "
            f"(bar/line/pie/area; 'table' is not a chart — totality, DB-02)")
    for k in ("key", "value"):
        if not tile.get(k):
            raise ProjectionError(f"{path}: a chart tile needs '{k}' (the query column alias)")
    q = queries.get(tile.get("query"))
    if not q:
        raise ProjectionError(f"{path}: unknown query '{tile.get('query')}'")
    if not q.get("sql"):
        raise ProjectionError(f"{path}: query '{tile['query']}' has no sql")
    return {"id": tile["query"], "label": tile.get("label", tile["query"]),
            "chartType": CHART_TYPES[ct], "keyName": tile["key"], "value": tile["value"],
            "sql": q["sql"]}


def project_dashboard(dash: dict, queries: dict) -> dict:
    path = f"dashboards/{dash['id']}"
    charts = [project_chart(t, queries, f"{path}/tiles/{i}")
              for i, t in enumerate(dash.get("tiles", []))]
    return {"dashboard": {"id": dash["id"], "name": dash.get("name", dash["id"]), "charts": charts}}


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

    queries = {q["id"]: q for q in doc.get("queries", [])}
    projected, errors = [], []
    for dash in doc.get("dashboards", []):
        try:
            spec = project_dashboard(dash, queries)
        except ProjectionError as exc:
            errors.append(str(exc))
            continue
        projected.append((pathlib.Path(f"{dash['id']}.dash.yml"), spec))

    if errors:
        print(f"PROJECT: {len(errors)} error(s) — nothing emitted")
        for e in errors:
            print(f"  - {e}")
        return 3

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
    print(f"{len(projected)} dashboard spec(s) projected -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
