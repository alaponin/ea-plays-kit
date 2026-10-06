#!/usr/bin/env python3
"""Project Layer-2 seed specs (deploy_dx9 --seed input) from a Layer-1 application model.

Pure, deterministic projection:
    validated application model (L1)  ->  <out>/_seed/DS-<entity>.spec.yml (L2)

Same contract as the other projectors: validate first, pure function of the document
(byte-identical output for identical input — including a DETERMINISTIC row id via uuid5, no
clock), provenance-stamped, totality-guarded. An L1 `seed[]` entry names an entity and rows of
attribute→value; this projector resolves the Joget form-data table (app_fd_<table>), maps each
attribute to its `c_<attr>` column, derives the idempotency key from the entity's unique
attribute, and stamps a deterministic id per row. deploy_dx9 --seed then loads it (adding the
load-time system columns), idempotently, after import+restart.

Usage:
    project_seed.py <app.yaml> --out <dir> [--schema <schema.yaml>]

Exit codes: 0 ok · 1 schema errors · 2 lint errors · 3 projection errors.
"""
from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import sys
import uuid

import yaml

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import validate as l1
import custody  # tools/validate.py — the single validation entry point
import lov  # the administration of lists of values (METHOD-2026-09-25-02)

PROJECTOR = "project_seed.py"
PROJECTOR_VERSION = "0.1.0"
# Fixed namespace so a row's id is stable across runs and machines (idempotent load); one
# definition, in validate.py, which the lint that compares a reference with its row (L019) shares.
NS = l1.SEED_NS


class ProjectionError(Exception):
    """A valid L1 construct this projector cannot (yet) realize in L2."""


def project_seed(entry: dict, entities: dict, seeded: dict | None = None) -> dict:
    """`seeded` is validate.seed_rows(...) over every inline row the deploy loads (the model's
    and a fixture's): a reference is written under the key its look-up reads (item 6)."""
    eid = entry["entity"]
    path = f"seed/{eid}"
    ent = entities.get(eid)
    if not ent:
        raise ProjectionError(f"{path}: seed references unknown entity '{eid}'")
    if entry.get("file"):
        raise ProjectionError(f"{path}: file-seeded rows are not realized (inline rows only — "
                              f"totality register)")
    attrs = {a["id"]: a for a in ent.get("attributes", [])}
    rows_out = []
    for i, row in enumerate(entry.get("rows", [])):
        cols = {}
        for k, v in row.items():
            if k not in attrs:
                raise ProjectionError(f"{path}/rows/{i}: '{k}' is not an attribute of entity '{eid}'")
            if isinstance(v, (dict, list)):
                raise ProjectionError(f"{path}/rows/{i}/{k}: seed values must be scalar")
            if attrs[k].get("type") == "ref" and v not in (None, "") and seeded is not None:
                v = _ref_under_lookup_key(attrs[k], v, entities, seeded, f"{path}/rows/{i}/{k}")
            cols["c_" + k] = v
        rid = l1.seed_row_id(eid, ent, row, i)
        rows_out.append({"id": rid, "columns": cols})
    out = {"entity": eid, "table": "app_fd_" + ent["table"], "order": entry.get("order", 100),
           "rows": rows_out}
    key = next((a["id"] for a in ent.get("attributes", []) if a.get("unique")), None)
    if key:
        out["key_column"] = "c_" + key
    return {"seed": out}


def project_view(q: dict, entities: dict) -> dict:
    """METHOD-2026-09-28-07 (the kit's gap G5): a query the model names as a view of the database
    (`queries[].view`) — its name, its statement, and the tables of the model it reads, each with
    the columns of its entity, so that deploy_dx9 can make sure of the tables before it makes the
    view (a form's table exists only once the platform or the seed has written it)."""
    sql = " ".join(str(q.get("sql") or "").split()).rstrip(";")
    if not sql:
        raise ProjectionError(f"queries/{q.get('id')}: the view {q.get('view')} has no statement")
    if q.get("params"):
        raise ProjectionError(f"queries/{q.get('id')}: the view {q.get('view')} takes parameters; "
                              f"a view of the database takes none")
    low = sql.lower()
    tables = {}
    for e in sorted(entities.values(), key=lambda x: x["id"]):
        t = "app_fd_" + str(e.get("table") or "")
        if len(t) > 7 and re.search(rf"\b{re.escape(t.lower())}\b", low):
            tables[t] = sorted("c_" + a["id"] for a in e.get("attributes", []))
    return {"view": {"query": q["id"], "name": q["view"], "sql": sql, "tables": tables}}


def _ref_under_lookup_key(attr: dict, value, entities: dict, seeded: dict, path: str):
    """METHOD-2026-09-25-04, item 6 (row 15): the seed writes a reference under the key its
    look-up reads — the target's business key (`pk.attr`), else the row's identifier. A model
    that names the row by its seeded identifier (as one application's does, while its look-ups read the
    business key) is written under the key; one that names it by the key is written as it
    stands. A reference that names no seeded row is refused (lint L019 refuses it in the model;
    this catches a fixture's)."""
    tid = (attr.get("ref") or {}).get("entity")
    tgt = entities.get(tid)
    if not tgt:
        raise ProjectionError(f"{path}: refers to unknown entity '{tid}'")
    out = l1.seed_ref_value(tid, tgt, seeded.get(tid, []), value)
    if out is None:
        raise ProjectionError(
            f"{path}: '{value}' names no seeded row of '{tid}' — neither by the key its look-up "
            f"reads ({l1.ref_key(tgt) or 'its row identifier'}) nor by a seeded row's "
            f"identifier (L019)")
    return out


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
    ap.add_argument("--feature")   # accepted for kit-gen uniformity; seed is not per-feature
    ap.add_argument("--fixture", type=pathlib.Path,
                    help="an ADDITIONAL seed source outside the model — deployment scenery "
                         "(e.g. the rows kit ui-probe needs to be able to prove anything). "
                         "Same shape as the model's seed[]; projected the same way; NOT part "
                         "of the shipped app, because a fixture row in a production register "
                         "is a defect rather than a convenience.")
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

    source_sha256 = hashlib.sha256(args.app.read_bytes()).hexdigest()
    header = provenance_header(doc, args.app.name, source_sha256)
    header += custody.line(args.custody)
    try:
        doc = lov.augment(doc, args.app)    # the first values of every maintained list (lov.py)
    except lov.LovError as exc:
        print("PROJECT: 1 error(s) — nothing emitted")
        print(f"  - lists of values: {exc}")
        return 3
    entities = {e["id"]: e for e in doc.get("entities", [])}

    sources = [(entry, False) for entry in doc.get("seed", [])]
    if args.fixture:
        if not args.fixture.is_file():
            print(f"FIXTURE: not found: {args.fixture}")
            return 3
        fx = yaml.safe_load(args.fixture.read_text(encoding="utf-8")) or {}
        sources += [(entry, True) for entry in (fx.get("seed") or [])]
        print(f"FIXTURE: {sum(len(e.get('rows') or []) for e in (fx.get('seed') or []))} row(s) "
              f"from {args.fixture.name} — scenery, not part of the app")

    projected, errors = [], []
    seeded = l1.seed_rows(doc, [entry for entry, is_fixture in sources if is_fixture])
    for entry, is_fixture in sources:
        try:
            spec = project_seed(entry, entities, seeded)
        except ProjectionError as exc:
            errors.append(str(exc))
            continue
        # A fixture entity may also be seeded by the model; keep them apart so neither can
        # silently overwrite the other, and so a deploy can load one without the other.
        stem = ("DF-" if is_fixture else "DS-") + entry["entity"]
        rel = pathlib.Path("_seed") / f"{stem}.spec.yml"
        if is_fixture:
            spec["seed"]["fixture"] = True
        projected.append((rel, spec))
    # the model's queries that are views of the database (METHOD-2026-09-28-07), made after the
    # starting rows are loaded
    for q in doc.get("queries", []):
        if not q.get("view"):
            continue
        try:
            projected.append((pathlib.Path("_seed") / f"DV-{q['id']}.spec.yml",
                              project_view(q, entities)))
        except ProjectionError as exc:
            errors.append(str(exc))

    if errors:
        print(f"PROJECT: {len(errors)} error(s) — nothing emitted")
        for e in errors:
            print(f"  - {e}")
        return 3

    for rel, spec in projected:
        emit(spec, header, args.out / rel)
        print(f"  + {rel.as_posix()}")
    print(f"{len(projected)} seed spec(s) projected -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
