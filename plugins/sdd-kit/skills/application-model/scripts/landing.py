#!/usr/bin/env python3
"""landing.py — the landing tables read at the moment of use, and a check of where each thing landed.

    python3 landing.py tables [--kit K] [--standards E]
    python3 landing.py check <landing.yaml> [--kit K] [--standards E]

WHAT IT READS. The register of the delivery kit, `templates/spec/slots.yaml` under the kit's root
`K`, row 09 (the application model), and in it the crossing from row 06 (the use case written out
in full): the cell `how.stated` of that crossing names, as `SDD-nn §n`, the sections of the
standards that say where each thing the model is written from lands. Each standard is the document
the register's row for it names, in the standards root `E`; its text is extracted at the moment of
use with the kit's own reader (`tools/slot.py`, `Document`). Nothing of any table is held here:
a row is whatever the standard's text carries at the moment the program runs.

A ROW. In each named section, every line of a table under a numbered sub-heading, the table's
heading line excepted. Its first cell is the thing; its last three cells are, in order, where it
lands, whether the landing is mechanical or a judgement, and where it cannot land. `tables`
prints every row it read, one line each, so that the person and the ledger use the same words.

THE LEDGER. `landing.yaml`, written by the person beside the model, records every thing the model
is written from, in three lists:

    model: <the model's file, relative to the ledger>
    loss_report: <the loss report's file, relative to the ledger>
    items:        # a thing the tables land in the model, or that could not land
      - {thing: ..., source: <document and section>, row: <the row's first cell>, table: <optional>,
         ref: <collection.id[.part...] in the model>, assumption: <the decision in one sentence>,
         ground: <identifier and section>, why_mechanical: <one sentence>, loss: <loss id>}
    carried:      # a thing its row lands nowhere, carried by its own document
      - {thing: ..., source: ..., row: ...}
    outside:      # a thing no row of the tables covers
      - {thing: ..., source: ..., ref: ..., assumption: ..., ground: ..., amendment: <file>}

WHAT IT CHECKS, reporting every finding and stopping nothing:
  1  every `row` names a row the tables carry, once (with `table` where two tables share it);
  2  an item under a row whose landing reads a judgement, and nothing mechanical, carries
     `assumption` and `ground`;
  3  an item under a row that reads both (mechanical for one part, a judgement for another, or
     mechanical with a condition), or that reads mechanical and offers more than one place (its
     landing cell names a second section after "or"), carries either `assumption` with `ground`,
     or `why_mechanical`, one sentence saying why the judgement does not arise;
  4  an item's `ref` resolves in the model; an item carries a `ref`, a `loss`, or both;
  5  an item carrying a `loss` stands under a row whose last cell does not read never, and the
     loss is an entry of the loss report; every entry of the loss report is named by an item;
  6  the loss report passes the kit's own refusal of an unnamed loss (`tools/compile_l1.py`,
     `check_loss_report`), each entry naming what it asked for, how it landed and what it needs;
  7  a `carried` entry stands under a row whose landing cell reads nowhere and whose last cell
     reads that the thing is not a loss; an item under a row whose landing reads nowhere records
     a loss;
  8  an `outside` entry carries `ref`, `assumption`, `ground` and an `amendment` that exists.

WHAT IT DOES NOT SEE. Whether the ledger lists every thing the upstream documents carry: it
reads the ledger, not the documents. The person walks each document against the tables.

Exit: 0 nothing to report · 1 something to report · 2 could not run.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

import yaml

# sdd-kit: this file is at skills/application-model/scripts/; the skill's own folder, one up, carries its copy of the
# kit and the standards (scripts/sync-skills.sh), so the skill works when installed on its own.
PLUGIN_ROOT = pathlib.Path(__file__).resolve().parents[1]
KIT = PLUGIN_ROOT / "kit"
STANDARDS = PLUGIN_ROOT / "standards"
SECTION_REF = re.compile(r"(SDD-\d\d)\s+§(\d+)\b")
HEADING = re.compile(r"^[ \t]*(\d+(?:\.\d+)*)[.):]?[ \t]+(\S.*)$")


class CouldNotRun(Exception):
    pass


def norm(s) -> str:
    return " ".join(str(s or "").split()).strip().lower()


def load_kit(kit: pathlib.Path):
    tools = kit / "tools"
    if not (tools / "slot.py").is_file():
        raise CouldNotRun(f"the kit's reader is not at {tools / 'slot.py'}")
    if str(tools) not in sys.path:
        sys.path.insert(0, str(tools))
    import slot  # noqa: E402  the kit's own reader of a standard
    import compile_l1  # noqa: E402  the kit's own refusal of an unnamed loss
    return slot, compile_l1


def named_sections(kit: pathlib.Path) -> list:
    """(code, section) as the register's crossing from row 06 into row 09 names them."""
    reg = yaml.safe_load((kit / "templates" / "spec" / "slots.yaml").read_text(encoding="utf-8"))
    rows = {str(r.get("n")): r for r in reg.get("slots") or []}
    if "09" not in rows:
        raise CouldNotRun("the register carries no row 09")
    takes = ((rows["09"].get("seams") or {}).get("takes")) or []
    cross = [t for t in takes if str(t.get("from")) == "06"]
    if len(cross) != 1:
        raise CouldNotRun(f"row 09 of the register carries {len(cross)} crossings from row 06, not one")
    how = cross[0].get("how") or {}
    text = how.get("stated") if isinstance(how, dict) else None
    if not text:
        raise CouldNotRun("the crossing from row 06 into row 09 states no section in its how cell")
    out = []
    for code, sec in SECTION_REF.findall(text):
        if (code, sec) not in out:
            out.append((code, sec))
    files = {}
    for r in rows.values():
        st = r.get("standard") or {}
        if isinstance(st, dict) and st.get("code") and st.get("file"):
            files[st["code"]] = st["file"]
    return [(c, s, files.get(c)) for c, s in out]


def md_as_docx_lines(lines: list) -> list:
    """A standard bundled as Markdown, read as the kit's reader reads the Word edition: a
    heading without its #, a table row as `cell | cell` without the outer pipes and without its
    separator row, and no emphasis marks."""
    out = []
    for ln in lines:
        s = ln.strip()
        if s.startswith("|") and set(s) <= set("|:- "):
            continue
        s = re.sub(r"^#{1,6}\s+", "", s)
        if s.startswith("|") and s.endswith("|"):
            s = " | ".join(c.strip() for c in s[1:-1].split("|"))
        s = s.replace("**", "").replace("`", "")
        out.append(s)
    return out


def read_rows(slot, standards: pathlib.Path, code: str, sec: str, file: str) -> list:
    if not file:
        raise CouldNotRun(f"no row of the register names the document of {code}")
    path = standards / file
    if not path.is_file():
        raise CouldNotRun(f"{code}: the register names {file}, which is not in {standards}")
    lines = slot.Document(path).text.splitlines()
    if path.suffix.lower() == ".md":
        lines = md_as_docx_lines(lines)
    heads = [i for i, ln in enumerate(lines)
             if " | " not in ln and (m := HEADING.match(ln)) and m.group(1) == sec]
    if not heads:
        raise CouldNotRun(f"{code}: no heading numbered {sec} in {file}")
    start = heads[-1]
    rows, sub, header_seen = [], sec, False
    for ln in lines[start + 1:]:
        m = HEADING.match(ln) if " | " not in ln else None
        if m:
            num = m.group(1)
            if num.split(".")[0] != sec:
                break
            sub, header_seen = num, False
            continue
        if " | " not in ln:
            continue
        if not header_seen:
            header_seen = True
            continue
        cells = [c.strip() for c in ln.split(" | ")]
        if len(cells) < 4:
            continue
        rows.append({"table": f"{code} {sub}", "thing": cells[0], "lands": cells[-3],
                     "how": cells[-2], "cannot": cells[-1]})
    if not rows:
        raise CouldNotRun(f"{code}: section {sec} of {file} carries no table rows")
    return rows


def all_rows(kit, standards):
    slot, compile_l1 = load_kit(kit)
    rows = []
    for code, sec, file in named_sections(kit):
        rows += read_rows(slot, standards, code, sec, file)
    return rows, compile_l1


def resolve(model, ref: str) -> bool:
    node = model
    for part in str(ref).split("."):
        if isinstance(node, dict):
            if part not in node:
                return False
            node = node[part]
        elif isinstance(node, list):
            hit = [x for x in node if isinstance(x, dict)
                   and part in (str(x.get("id")), str(x.get("attr")), str(x.get("component")))]
            if len(hit) != 1:
                return False
            node = hit[0]
        else:
            return False
    return True


def cmd_tables(a) -> int:
    rows, _ = all_rows(a.kit, a.standards)
    for r in rows:
        print(f"{r['table']} · {r['thing']} · lands: {r['lands']} · {r['how']} · cannot land: {r['cannot']}")
    print(f"{len(rows)} rows read at this moment from "
          + ", ".join(sorted({r['table'].split()[0] + ' §' + r['table'].split()[1].split('.')[0]
                              for r in rows})))
    return 0


def cmd_check(a) -> int:
    rows, compile_l1 = all_rows(a.kit, a.standards)
    ledger_path = pathlib.Path(a.ledger)
    if not ledger_path.is_file():
        raise CouldNotRun(f"no ledger at {ledger_path}")
    base = ledger_path.resolve().parent
    led = yaml.safe_load(ledger_path.read_text(encoding="utf-8")) or {}
    model_p = base / str(led.get("model") or "")
    loss_p = base / str(led.get("loss_report") or "")
    if not led.get("model") or not model_p.is_file():
        raise CouldNotRun(f"the ledger names no model that exists ({led.get('model')!r})")
    if not led.get("loss_report") or not loss_p.is_file():
        raise CouldNotRun(f"the ledger names no loss report that exists ({led.get('loss_report')!r}); "
                          f"an empty one is written `losses: []`")
    model = yaml.safe_load(model_p.read_text(encoding="utf-8")) or {}
    loss = yaml.safe_load(loss_p.read_text(encoding="utf-8")) or {}
    loss_ids = [str(x.get("id")) for x in loss.get("losses") or []]
    out: list[str] = []

    def find(e, where):
        cand = [r for r in rows if norm(r["thing"]) == norm(e.get("row"))
                and (not e.get("table") or norm(r["table"]) == norm(e.get("table")))]
        if len(cand) != 1:
            out.append(f"{where}: the row {e.get('row')!r} is "
                       + ("no row of the tables" if not cand else
                          f"a row of {len(cand)} tables; name one with `table`"))
            return None
        return cand[0]

    named_losses = set()
    for i, e in enumerate(led.get("items") or []):
        where = f"items[{i}] {e.get('thing')!r}"
        r = find(e, where)
        if r is None:
            continue
        how, lands = norm(r["how"]), norm(r["lands"])
        if lands.startswith("nowhere") and not e.get("loss"):
            out.append(f"{where}: its row lands the thing nowhere; it belongs under `carried`, or "
                       f"records a loss")
            continue
        has_asm = bool(str(e.get("assumption") or "").strip()) and bool(str(e.get("ground") or "").strip())
        mixed = "judgement" in how and "mechanical" in how
        if "judgement" in how and not mixed and not has_asm:
            out.append(f"{where}: its row ({r['table']}) reads a judgement, and the item carries no "
                       f"assumption with its ground")
        elif (mixed or (how.startswith("mechanical") and re.search(r"\bor §", lands))) \
                and not has_asm and not str(e.get("why_mechanical") or "").strip():
            why = "reads both mechanical and a judgement" if mixed else "offers more than one place"
            out.append(f"{where}: its row ({r['table']}) {why}; the item carries neither an assumption "
                       f"with its ground nor why_mechanical")
        if not e.get("ref") and not e.get("loss"):
            out.append(f"{where}: it carries neither a ref in the model nor a loss")
        if e.get("ref") and not resolve(model, e["ref"]):
            out.append(f"{where}: its ref {e['ref']!r} does not resolve in the model")
        if e.get("loss"):
            named_losses.add(str(e["loss"]))
            if norm(r["cannot"]).startswith("never"):
                out.append(f"{where}: it records the loss {e['loss']}, and its row reads that the "
                           f"thing never fails to land")
            if str(e["loss"]) not in loss_ids:
                out.append(f"{where}: its loss {e['loss']} is no entry of the loss report")
    for i, e in enumerate(led.get("carried") or []):
        where = f"carried[{i}] {e.get('thing')!r}"
        r = find(e, where)
        if r is not None and not norm(r["lands"]).startswith("nowhere"):
            out.append(f"{where}: its row lands the thing in the model; it belongs under `items`")
        elif r is not None and "not a loss" not in norm(r["cannot"]):
            out.append(f"{where}: its row records the thing as a loss; it belongs under `items`, "
                       f"with its loss")
    for i, e in enumerate(led.get("outside") or []):
        where = f"outside[{i}] {e.get('thing')!r}"
        for k in ("ref", "assumption", "ground", "amendment"):
            if not str(e.get(k) or "").strip():
                out.append(f"{where}: it carries no {k}")
        if e.get("ref") and not resolve(model, e["ref"]):
            out.append(f"{where}: its ref {e['ref']!r} does not resolve in the model")
        if e.get("amendment") and not (base / str(e["amendment"])).is_file():
            out.append(f"{where}: its amendment {e['amendment']} is not there")
    for lid in loss_ids:
        if lid not in named_losses:
            out.append(f"the loss report: the entry {lid} is named by no item")
    for f in compile_l1.check_loss_report(loss, None):
        out.append(f"the loss report: {f}")

    n_i, n_c, n_o = (len(led.get(k) or []) for k in ("items", "carried", "outside"))
    n_a = sum(1 for e in (led.get("items") or []) if str(e.get("assumption") or "").strip())
    print(f"landing tables: {len(rows)} rows read at this moment")
    print(f"ledger: {n_i} items ({n_a} with an assumption, {len(named_losses)} losses named) · "
          f"{n_c} carried by their own document · {n_o} outside every row")
    for f in out:
        print(f"  FINDING  {f}")
    print("nothing to report" if not out else f"{len(out)} finding(s)")
    return 1 if out else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("act", choices=("tables", "check"))
    ap.add_argument("ledger", nargs="?")
    ap.add_argument("--kit", type=pathlib.Path, default=KIT)
    ap.add_argument("--standards", type=pathlib.Path, default=STANDARDS)
    a = ap.parse_args(argv)
    try:
        if a.act == "tables":
            return cmd_tables(a)
        if not a.ledger:
            raise CouldNotRun("check takes the ledger's path")
        return cmd_check(a)
    except CouldNotRun as exc:
        print(f"landing.py: could not run: {exc}", file=sys.stderr)
        return 2
    except (OSError, yaml.YAMLError) as exc:
        print(f"landing.py: could not run: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
