#!/usr/bin/env python3
"""Project Layer-2 report specs (gen_reports input) from a Layer-1 application model.

Pure, deterministic projection:
    validated application model (L1)  ->  <out>/<feature>/reports/DR-<reportId>.spec.yml (L2)

Same contract as the other projectors (project_forms.py / project_datalists.py): validate
first (refuse invalid input), pure function of the document (byte-identical output for identical
input), provenance-stamped, and valid L1 constructs with no realization in gen_reports are
refused loudly (totality rule) — never silently dropped.

An L1 `reports[]` entry (engine: jasper) references a `queries[]` entry; this projector resolves
the query's SQL + params, derives the report FIELDS from the SQL SELECT list, and maps the L1
`output` to the JasperReportsMenu `export` string. gen_reports then emits the .jrxml + the
JasperReportsMenu that carries it.

Usage:
    project_reports.py <app.yaml> --out <dir> [--feature <id>] [--schema <schema.yaml>]

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
import custody  # tools/validate.py — the single validation entry point

PROJECTOR = "project_reports.py"
PROJECTOR_VERSION = "0.1.0"

# L1 output token -> JasperReportsMenu export token (rule 4: a ';'-joined string).
EXPORT_MAP = {"pdf": "pdf", "xlsx": "xls", "docx": "docx"}
# L1 query param type -> Jasper parameter class.
PARAM_CLASS = {"string": "java.lang.String", "integer": "java.lang.Integer",
               "decimal": "java.math.BigDecimal", "date": "java.lang.String",
               "datetime": "java.lang.String", "boolean": "java.lang.Boolean"}

_ABBR = {"tin": "TIN", "id": "ID", "nid": "NID", "no": "No.", "vat": "VAT",
         "paye": "PAYE", "ltu": "LTU", "url": "URL", "api": "API", "at": "at"}


class ProjectionError(Exception):
    """A valid L1 construct this projector cannot (yet) realize in L2."""


def humanize(col: str) -> str:
    s = col[2:] if col.startswith("c_") else col
    return " ".join(_ABBR.get(w.lower(), w[:1].upper() + w[1:]) for w in s.split("_"))


def select_fields(sql: str, path: str) -> list[str]:
    """Derive the field names from the top-level SELECT list. Refuse `*` and any item that
    is not a bare column / has no alias (a field name must be derivable — totality)."""
    m = re.search(r"\bselect\b(.*?)\bfrom\b", sql, re.I | re.S)
    if not m:
        raise ProjectionError(f"{path}: cannot find a SELECT ... FROM to derive report fields")
    body, depth, cur, items = m.group(1), 0, "", []
    for ch in body:                                   # split on top-level commas only
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == "," and depth == 0:
            items.append(cur); cur = ""
        else:
            cur += ch
    items.append(cur)
    fields = []
    for it in items:
        it = it.strip()
        if it == "*":
            raise ProjectionError(f"{path}: SELECT * cannot derive named report fields — "
                                  f"list explicit columns (totality register)")
        alias = re.split(r"\s+as\s+", it, flags=re.I)[-1].strip().strip('"')
        if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", alias):
            raise ProjectionError(f"{path}: SELECT item {it!r} has no simple column/alias to "
                                  f"become a report field — add an AS alias (totality register)")
        fields.append(alias)
    return fields


def project_report(rep: dict, queries: dict) -> dict:
    rid = rep["id"]
    path = f"reports/{rid}"
    if rep["engine"] != "jasper":                     # schema pins enum, kept for totality
        raise ProjectionError(f"{path}: engine '{rep['engine']}' has no realization "
                              f"(only jasper — totality register)")
    q = queries.get(rep["query"])
    if not q:
        raise ProjectionError(f"{path}: unknown query '{rep['query']}'")
    if not q.get("sql"):
        raise ProjectionError(f"{path}: query '{rep['query']}' has no sql")
    qparams = {p["id"]: p for p in q.get("params", [])}
    params = []
    for pid in rep.get("params", []):
        if pid not in qparams:
            raise ProjectionError(f"{path}: report param '{pid}' is not a parameter of query "
                                  f"'{rep['query']}' (query params: {sorted(qparams)})")
        ptype = qparams[pid].get("type", "string")
        params.append({"name": pid, "class": PARAM_CLASS.get(ptype, "java.lang.String"),
                       "request_param": pid})
    outs = rep.get("output", ["pdf"])
    for o in outs:
        if o not in EXPORT_MAP:
            raise ProjectionError(f"{path}: output '{o}' is not a JasperReportsMenu export "
                                  f"(pdf/xlsx/docx — totality register)")
    export = ";".join(dict.fromkeys(EXPORT_MAP[o] for o in outs))   # order-preserving unique
    fields = [{"name": c, "label": humanize(c), "class": "java.lang.String"}
              for c in select_fields(q["sql"], path)]
    return {"report": {"id": rid, "name": rep["name"], "sql": q["sql"],
                       "params": params, "fields": fields, "export": export}}


def provenance_header(doc: dict, source_name: str, source_sha256: str) -> str:
    m = doc.get("model", {})
    return (
        "# =============================================================================\n"
        "# GENERATED — do not edit. Projected from the Layer-1 application model.\n"
        f"# projector:      {PROJECTOR} v{PROJECTOR_VERSION} (the spec kit)\n"
        f"# schema_version: {m.get('schema_version')}\n"
        f"# spec_version:   {m.get('spec_version')}\n"
        f"# source_model:   {source_name}\n"
        f"# source_sha256:  {source_sha256}\n"
        "# =============================================================================\n")


def emit(spec: dict, header: str, out_path: pathlib.Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    body = yaml.safe_dump(spec, sort_keys=False, default_flow_style=False,
                          allow_unicode=True, width=4096)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(header)
        fh.write(body)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("app", type=pathlib.Path)
    ap.add_argument("--out", type=pathlib.Path, required=True)
    ap.add_argument("--feature")
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
    lint = l1.Lint(doc).run()
    if lint:
        print(f"LINT:   {len(lint)} error(s) — refusing to project")
        for e in lint:
            print(f"  - {e}")
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

    source_sha256 = hashlib.sha256(args.app.read_bytes()).hexdigest()
    header = provenance_header(doc, args.app.name, source_sha256)
    header += custody.line(args.custody)
    queries = {q["id"]: q for q in doc.get("queries", [])}

    reports = doc.get("reports", [])
    if args.feature:
        reports = [r for r in reports if r.get("feature") == args.feature]

    projected, errors = [], []
    for rep in reports:
        try:
            spec = project_report(rep, queries)
        except ProjectionError as exc:
            errors.append(str(exc))
            continue
        feature_dir = rep.get("feature") or "_app"
        rel = pathlib.Path(feature_dir) / "reports" / f"DR-{rep['id']}.spec.yml"
        projected.append((rel, spec))

    if errors:
        print(f"PROJECT: {len(errors)} error(s) — nothing emitted")
        for e in errors:
            print(f"  - {e}")
        return 3

    for rel, spec in projected:
        emit(spec, header, args.out / rel)
        print(f"  + {rel.as_posix()}")
    print(f"{len(projected)} report spec(s) projected -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
