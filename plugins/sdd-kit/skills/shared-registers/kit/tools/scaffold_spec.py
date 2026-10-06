#!/usr/bin/env python3
"""scaffold_spec — the specification tree (`kit spec new`).

Creates one folder per thing SDD-01 section 4 names, numbered in the order they come into
existence, plus the seven support folders the method needs; writes every slot's README from
`templates/spec/slots.yaml`; carries named artefacts into their slots and proves the copies
byte-identical; and emits the planning commission, parameterised for this system.

    scaffold_spec.py <systemId> --name NAME --out DIR
                     [--carry SLOT=PATH ...] [--prior DIR] [--force]

`--carry` takes a slot number and a file OR a directory: `--carry 00=./spec.docx`,
`--carry 03=./model/`. A directory is carried whole, which is how a generated document
arrives with the source it is built from. Every carried path is checksummed on both sides
and the run refuses if a copy differs.

INVARIANT 1 — no domain literal lives in this tool or in its templates. The system name is
an argument. A slot description that only makes sense for one kind of system has leaked
testbed into product.

Exit: 0 written · 1 refused (output exists and --force not given; a carry that did not
verify; an unknown slot).
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import os
import pathlib
import shutil
import sys

import yaml

HERE = pathlib.Path(__file__).resolve().parent
TPL = HERE.parent / "templates" / "spec"

SUPPORT_ORDER = ["_conformance", "_amendments", "_findings", "_rulings",
                 "_sessions", "_machinery", "_reviews"]


def _md5(p: pathlib.Path) -> str:
    return hashlib.md5(p.read_bytes()).hexdigest()


def _fill(text: str, **kw) -> str:
    for k, v in kw.items():
        text = text.replace("{{%s}}" % k, str(v))
    return text


def _load_spec() -> dict:
    return yaml.safe_load((TPL / "slots.yaml").read_text())


_WORDS = ("zero one two three four five six seven eight nine ten eleven twelve thirteen "
          "fourteen fifteen sixteen seventeen eighteen nineteen twenty").split()


def _word(n) -> str:
    """A count as a word, as the templates write it ("twelve"); a figure past twenty."""
    return _WORDS[n] if isinstance(n, int) and 0 <= n < len(_WORDS) else str(n)


def _counts(spec: dict) -> dict:
    """The counts the templates print, read from the register's own `counts:` entry
    (METHOD-2026-09-25-12): the templates state no number of their own."""
    c = spec.get("counts") or {}
    things = c.get("things", len(spec.get("slots") or []))
    handovers = c.get("handovers", len(spec.get("handovers") or []))
    return {"THINGS": _word(things), "THINGS_CAP": _word(things).capitalize(),
            "HANDOVERS": _word(handovers),
            "SLOT_LIST": ", ".join(s["n"] for s in spec.get("slots") or [])}


def _parse_carry(items: list[str], slots: dict) -> list[tuple[str, pathlib.Path]]:
    out = []
    for it in items or []:
        if "=" not in it:
            print(f"refused: --carry needs SLOT=PATH, got {it!r}", file=sys.stderr)
            raise SystemExit(1)
        n, path = it.split("=", 1)
        n = n.strip()
        if n not in slots:
            print(f"refused: no slot {n!r}. Slots are {', '.join(sorted(slots))}",
                  file=sys.stderr)
            raise SystemExit(1)
        p = pathlib.Path(path).expanduser()
        if not p.exists():
            print(f"refused: {p} does not exist", file=sys.stderr)
            raise SystemExit(1)
        out.append((n, p))
    return out


def _carry(src: pathlib.Path, dest_dir: pathlib.Path) -> list[tuple[str, str, str]]:
    """Copy a file or a directory's contents into dest_dir. Returns (name, md5, verdict)."""
    rows = []
    pairs: list[tuple[pathlib.Path, pathlib.Path]] = []
    if src.is_dir():
        for s in sorted(src.rglob("*")):
            if s.is_file() and not s.name.startswith("."):
                pairs.append((s, dest_dir / s.relative_to(src)))
    else:
        pairs.append((src, dest_dir / src.name))
    for s, d in pairs:
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(s, d)
        a, b = _md5(s), _md5(d)
        rows.append((str(d.relative_to(dest_dir)), b, "identical" if a == b else "DIFFERS"))
    return rows


GENERATED_SUFFIXES = {".docx", ".pdf", ".pptx", ".xlsx", ".odt"}


def main() -> int:
    ap = argparse.ArgumentParser(prog="scaffold_spec.py")
    ap.add_argument("system_id")
    ap.add_argument("--name", help="human-readable system name (default: the id)")
    ap.add_argument("--out", type=pathlib.Path, required=True)
    ap.add_argument("--carry", action="append", metavar="SLOT=PATH")
    ap.add_argument("--prior", type=pathlib.Path,
                    help="an earlier attempt's folder, if there is one")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()

    name = a.name or a.system_id
    root = a.out
    date = datetime.date.today().isoformat()

    if root.exists() and any(root.iterdir()) and not a.force:
        print(f"refused: {root} exists and is not empty. Use --force to overwrite.",
              file=sys.stderr)
        return 1

    spec = _load_spec()
    slots = {s["n"]: s for s in spec["slots"]}
    carries = _parse_carry(a.carry, slots)
    carried_by_slot: dict[str, list] = {}
    warnings: list[str] = []

    root.mkdir(parents=True, exist_ok=True)

    # ---- pass one: make the slot folders and carry the material in.
    # Carrying happens BEFORE any README is written, because what is carried decides what
    # some of those READMEs have to say (the out-of-order note below).
    for s in spec["slots"]:
        d = root / f"{s['n']}_{s['dir']}"
        d.mkdir(parents=True, exist_ok=True)
        rows = []
        for n, src in carries:
            if n != s["n"]:
                continue
            rows += _carry(src, d)
            if src.is_file() and src.suffix.lower() in GENERATED_SUFFIXES:
                warnings.append(
                    f"slot {s['n']}: {src.name} was carried alone. If it is generated, "
                    f"carry the directory holding its build source instead — otherwise it "
                    f"can never be corrected except by hand, which the method forbids.")
        carried_by_slot[s["n"]] = rows

    filled = [s["n"] for s in spec["slots"] if carried_by_slot[s["n"]]]
    empty = [s["n"] for s in spec["slots"] if not carried_by_slot[s["n"]]]
    # out of order: carried into a slot above 00 while a slot beneath it is still empty
    out_of_order = [n for n in filled if n != "00"
                    and any(m < n for m in empty if m != "00")]

    OOO_NOTE = """

---

**This slot was filled out of order, and that must not be forgotten.** `SDD-01` §5 puts it
after the slots beneath it, for one reason: *a measure written after the thing it measures is
not a measure.* Here those measures will be written afterwards.

**So what is here is material, not a settled slot.** It is measured against the slots beneath
it once those exist, and every disagreement found then is recorded — never tidied away."""

    # ---- pass two: the slot READMEs
    slot_tpl = (TPL / "slot_README.md.tmpl").read_text()
    for s in spec["slots"]:
        d = root / f"{s['n']}_{s['dir']}"
        rows = carried_by_slot[s["n"]]
        holds = ("Nothing yet." if not rows else
                 ", ".join(f"`{r[0]}`" for r in rows[:6]) +
                 (f" and {len(rows) - 6} more files" if len(rows) > 6 else ""))
        if s["n"] == "10":
            # ADR-108 (a delivery's hand-off of 6 October 2026, item 7; a delivery's finding OM-9): the
            # build keeps its archive here; it said that nothing ever lands here
            holds = ("Nothing yet. **The build keeps here the archive it made (`<app>.jwa`) and "
                     "its admission record (`<app>.admission.yaml`), never edited.**")
        notes = s["notes"].rstrip()
        if s["n"] in out_of_order:
            notes += OOO_NOTE
        (d / "README.md").write_text(_fill(
            slot_tpl, SLOT_N=s["n"], SLOT_TITLE=s["title"], SLOT_WHO=s["who"],
            SLOT_GOVERNS=s["governs"], SLOT_WHEN=s["when"], SLOT_HOLDS=holds,
            SLOT_CHECKLIST=s["check"].get("checklist", "absent"), SLOT_NOTES=notes,
            **_counts(spec)))

    # ---- the support folders
    sup_tpl = (TPL / "support_README.md.tmpl").read_text()
    sup = {x["dir"]: x for x in spec["support"]}
    for dname in SUPPORT_ORDER:
        x = sup[dname]
        d = root / dname
        d.mkdir(parents=True, exist_ok=True)
        (d / "README.md").write_text(_fill(
            sup_tpl, DIR=dname, TITLE=x["title"], BODY=x["body"].rstrip()))

    # ---- the rendered blocks
    slot_table = ["| Slot | The thing | What governs it |", "|---|---|---|"]
    for s in spec["slots"]:
        slot_table.append(f"| `{s['n']}_{s['dir']}` | {s['title']} | {s['governs']} |")
    slot_table = "\n".join(slot_table)

    any_carried = any(carried_by_slot.values())
    if any_carried:
        lines = ["| Slot | File | md5 | Verified |", "|---|---|---|---|"]
        for s in spec["slots"]:
            for fname, digest, verdict in carried_by_slot[s["n"]]:
                lines.append(f"| `{s['n']}_{s['dir']}` | `{fname}` | `{digest}` | {verdict} |")
        carried_table = "\n".join(lines)
        carried_block = (
            "Every carried file was checksummed on both sides and proved identical.\n\n"
            + carried_table +
            "\n\n**Everything else in this tree is written here, through the standards.**")
    else:
        carried_table = "*Nothing was carried in. Every slot is empty and every one of them "\
                        "is written here, through the standards.*"
        carried_block = carried_table

    empty_line = (f"**Every other slot is empty** — {', '.join(empty)}. That is the point of "
                  "the layout: an empty slot is information."
                  if filled else "**Every slot is empty.**")

    if out_of_order:
        names = ", ".join(f"slot {n} ({slots[n]['title']})" for n in out_of_order)
        ooo = f"""### 3.1 Something arrived out of order

**{names} was carried in, and slots beneath it are empty.**

`SDD-01` §5 fixes the order for one reason above all others: *two of the documents exist to
be the measure of the others, and a measure written after the thing it measures is not a
measure.* Here the measures will be written after the thing they measure.

**So a carried artefact in that position is material, not a settled slot.** Your plan must
say how it is treated: what part of it is taken forward, what is re-derived, and at what
point it is measured against the slots beneath it once those exist. Every disagreement found
then is recorded, not tidied away — `SDD-01` §14: *where two signed documents contradict each
other, that is a decision for a person, not a defect to be tidied away.*

**The plan does not resolve this by declaring the carried artefact correct.**"""
    else:
        ooo = """### 3.1 Nothing arrived out of order

Nothing was carried into a slot whose measures are still empty, so the ratchet of `SDD-01` §5
holds from the start. **Say so on the page**, and say what would break it: any artefact
adopted later into a slot above an empty one re-opens this problem and must be recorded as
doing so."""

    if a.prior:
        # shown relative to the tree's own parent: an absolute path here is the path on
        # whatever machine scaffolded the folder, which is not where the reader is
        try:
            prior_shown = os.path.relpath(a.prior, root.parent)
        except ValueError:
            prior_shown = a.prior.name
        prior_block = f"""## D-1 — what this run may do with the earlier attempt

An earlier attempt exists at `{prior_shown}`, beside this folder. **It is untouched and stays where it is.** What
this run may do with it is a ruling the owner has not made. Three readings:

| | Reading |
|---|---|
| a | **Sealed.** The earlier folder may not be read at all |
| b | **Readable, but nothing crosses without re-derivation.** A figure, record or decision enters this folder only if it was re-derived here from the carried material through a standard. The earlier folder may be read to check a result and to find questions worth asking, and every agreement and disagreement is recorded |
| c | **Open.** Harvest what survives measurement against the standards |

**Reading (b) is in force as a stated default until the owner rules.** Every piece of work
records which reading it relied on, so that a later ruling can be applied rather than guessed
at, and the plan states in one place what changes under (a) and under (c).

The recommendation is (b): (a) buys a purer experiment at a price the programme has already
paid once, and (c) is close to what the earlier attempt already did, so it will not tell
anybody whether the standards work."""
    else:
        prior_block = ""

    # ---- the root README and the commission
    (root / "README.md").write_text(_fill(
        (TPL / "root_README.md.tmpl").read_text(),
        SYSTEM=name, SYSTEM_ID=a.system_id, DATE=date,
        SLOT_TABLE=slot_table, CARRIED_BLOCK=carried_block,
        PRIOR_BLOCK=prior_block, **_counts(spec)))

    commission = root / "_sessions" / "SPEC_PLAN_SESSION_PROMPT.md"
    commission.write_text(_fill(
        (TPL / "COMMISSION.md.tmpl").read_text(),
        SYSTEM=name, SYSTEM_ID=a.system_id, DATE=date, ROOT=root.name,
        CARRIED_TABLE=carried_table, EMPTY_SLOTS_LINE=empty_line,
        OUT_OF_ORDER_BLOCK=ooo,
        PRIOR_BLOCK=(prior_block + "\n\n---\n" if prior_block else ""), **_counts(spec)))

    # ---- report
    files = sorted(p for p in root.rglob("*") if p.is_file())
    print(f"kit spec new {a.system_id} → {root}")
    print(f"  {len(spec['slots'])} slots · {len(SUPPORT_ORDER)} support folders · "
          f"{len(files)} files")
    print(f"  commission: {commission.relative_to(root)}")
    bad = [r for rows in carried_by_slot.values() for r in rows if r[2] != "identical"]
    if carries:
        n = sum(len(v) for v in carried_by_slot.values())
        print(f"  carried: {n} file(s), {n - len(bad)} verified identical")
    for w in warnings:
        print(f"  WARNING  {w}")
    if bad:
        for fname, _, _ in bad:
            print(f"  REFUSED  copy differs from its source: {fname}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
