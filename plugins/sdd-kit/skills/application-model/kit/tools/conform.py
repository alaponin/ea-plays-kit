#!/usr/bin/env python3
"""conform — write the claim of conformance of one artifact, rule by rule, from its checklist.

    kit conform <n> <artifact> [--verdicts F] [--checklist F] [--slots F] [--kit-root D]

THE CLAIM. A file beside the artifact, `<artifact's folder>/_conformance/<artifact's file
name>_conformance.md` (the plan of the finish, PLAN.md section 3.1): a head naming the artifact
and its checksum, the standard, its edition, the document and its checksum as the checklist's
head gives them, the checklist, and when the claim was written; then one line for each rule of
the checklist, in the checklist's order, and no other line:

    RQR-3 · met · no program
    RQR-4 · not met · tools/validate.py

The verdict is one of `met`, `not met` and `not applicable`, the words section 3.1 fixes; the
third field is the check that decided it — a program of the kit, or `no program` when a person
answered the rule.

THE VERDICTS. They are the answers of the person, and of the programs, that checked the
artifact against the checklist's rules (01_PROCEDURE.md section 4, "check and claim"). They are
read from a YAML file of one entry per rule, by default
`_conformance/<artifact's file name>_verdicts.yaml` beside the artifact:

    RQR-3: met                                            # answered by a person
    RQR-4: {verdict: not met, check: tools/validate.py}   # answered by a program of the kit

THE REFUSALS (01_PROCEDURE.md section 5; plan M2). The claim is refused, nothing is written and
the program exits 1 when it would not be rule by rule — a rule of the checklist with no verdict,
a verdict for a rule the checklist does not carry, a rule answered twice, a verdict word other
than the three — and when a line cites a check no program performs: a program the checklist does
not name for that rule, or a program the kit does not hold. Running the program a line cites is
not this program's act; that the check exists and is the one the checklist names is.

THE CHECKLIST. The one the register's row names in its `check.checklist` cell; where the cell
names none, `templates/spec/checklists/<code>.md` under the kit; `--checklist` names another.
Its head is the YAML block of section 3.1 (standard, title, edition, document, sha256,
produced_by) and its rules are the table under `## Rules`, with the columns `rule`, `words` and
`program`. A row of the register that names no standard has nothing to conform to.

Exit: 0 written · 1 refused, nothing written · 2 could not run.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import pathlib
import re
import sys

import yaml

HERE = pathlib.Path(__file__).resolve().parent
KIT_ROOT = HERE.parent
SLOTS = KIT_ROOT / "templates" / "spec" / "slots.yaml"

VERDICTS = ("met", "not met", "not applicable")      # PLAN.md section 3.1
NO_PROGRAM = "no program"
SEP = " · "
HEAD_NEEDS = ("standard", "edition", "document", "sha256")


class CouldNotRun(Exception):
    """The program could not run: exit 2, and the message says why."""


def now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_of(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


# --------------------------------------------------------------------------- reading

def read_head(text: str):
    """The YAML block at the head of a file, between `---` fences or in a ```yaml fence as the
    first thing in it. Every value is read as text, so that an edition "2.10" stays "2.10".
    Returns (mapping or None, the number of lines the head takes, what went wrong or None)."""
    lines = text.splitlines()
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i == len(lines):
        return None, 0, "the file is empty"
    first = lines[i].strip()
    if first == "---":
        close = "---"
    elif first in ("```yaml", "```yml"):
        close = "```"
    else:
        return None, 0, "it does not open with a YAML block"
    for j in range(i + 1, len(lines)):
        if lines[j].strip() == close:
            try:
                data = yaml.load("\n".join(lines[i + 1:j]), Loader=yaml.BaseLoader)
            except yaml.YAMLError as exc:
                return None, 0, f"its head does not parse: {str(exc).splitlines()[0]}"
            if not isinstance(data, dict):
                return None, 0, "its head is not a mapping"
            return data, j + 1, None
    return None, 0, "its head is never closed"


def _cells(row: str) -> list[str]:
    s = row.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", s)]


def _bare(cell: str) -> str:
    return cell.replace("`", "").strip()


def rules_of(text: str) -> list[tuple[str, tuple[str, ...]]]:
    """The rules of a checklist, in its order, each with the programs its `program` column names
    (none when the column reads `none`). Read from the table or tables under `## Rules`."""
    out: list[tuple[str, tuple[str, ...]]] = []
    in_rules = False
    cols: dict[str, int] | None = None
    for line in text.splitlines():
        s = line.strip()
        m = re.match(r"^(#+)\s+(.*)$", s)
        if m:
            if len(m.group(1)) <= 2:
                in_rules = bool(re.match(r"^rules\b", m.group(2).strip(), re.I))
                cols = None
            continue
        if not in_rules or not s.startswith("|"):
            continue
        cells = _cells(s)
        low = [_bare(c).lower() for c in cells]
        at_rule = next((i for i, c in enumerate(low) if c.startswith("rule")), None)
        at_prog = next((i for i, c in enumerate(low) if c.startswith("program")), None)
        if at_rule is not None and at_prog is not None:
            cols = {"rule": at_rule, "program": at_prog}      # the header row of a table
            continue
        if all(re.fullmatch(r":?-{2,}:?", c.strip()) for c in cells if c.strip()):
            continue
        if cols is None:
            raise CouldNotRun("the checklist's `## Rules` table has no header row naming the "
                              "columns `rule` and `program` (PLAN.md section 3.1)")
        rule = _bare(cells[cols["rule"]]) if cols["rule"] < len(cells) else ""
        prog = _bare(cells[cols["program"]]) if cols["program"] < len(cells) else ""
        if not rule:
            continue
        progs = tuple(p.strip() for p in re.split(r"[,;]", prog)
                      if p.strip() and p.strip().lower() != "none")
        out.append((rule, progs))
    return out


class _NoDuplicates(yaml.BaseLoader):
    """BaseLoader that refuses a key given twice — a rule answered twice is not one claim."""


def _mapping(loader, node, deep=False):
    seen: dict[str, int] = {}
    for key_node, _ in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in seen:
            raise yaml.constructor.ConstructorError(
                None, None, f"the rule {key} is answered twice", key_node.start_mark)
        seen[key] = 1
    return yaml.BaseLoader.construct_mapping(loader, node, deep=deep)


_NoDuplicates.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)


def read_verdicts(path: pathlib.Path):
    """The verdicts file: {rule: verdict} or {rule: {verdict, check}}. Returns (mapping, the
    refusal a rule answered twice makes, or None)."""
    try:
        data = yaml.load(path.read_text(encoding="utf-8"), Loader=_NoDuplicates)
    except yaml.constructor.ConstructorError as exc:
        return None, str(exc.problem)
    except yaml.YAMLError as exc:
        raise CouldNotRun(f"the verdicts {path} do not parse: {str(exc).splitlines()[0]}")
    if data is None:
        data = {}
    if not isinstance(data, dict):
        raise CouldNotRun(f"the verdicts {path} are not a mapping of rule to verdict")
    return data, None


# --------------------------------------------------------------------------- the programs

_VERBS: set[str] | None = None


def kit_verbs() -> set[str]:
    """The verbs `kit` answers to, read from its own parser."""
    global _VERBS
    if _VERBS is None:
        if str(HERE) not in sys.path:
            sys.path.insert(0, str(HERE))
        import kit                                               # noqa: PLC0415
        _VERBS = set()
        for act in kit.build_parser()._actions:                  # noqa: SLF001
            if isinstance(act, argparse._SubParsersAction):      # noqa: SLF001
                _VERBS |= set(act.choices)
    return _VERBS


def held_by_the_kit(program: str, kit_root: pathlib.Path) -> bool:
    """Whether the kit holds the program a line cites: a file under the kit (or under its
    tools/), or `kit <verb>` for a verb the kit answers to."""
    p = program.strip()
    if p.startswith("kit "):
        parts = p.split()
        return len(parts) > 1 and parts[1] in kit_verbs()
    return (kit_root / p).is_file() or (kit_root / "tools" / p).is_file()


# --------------------------------------------------------------------------- the register

def row_of(slots_path: pathlib.Path, n: str) -> dict:
    try:
        spec = yaml.safe_load(slots_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise CouldNotRun(f"the register {slots_path} is not there")
    except yaml.YAMLError as exc:
        raise CouldNotRun(f"the register {slots_path} does not parse: {exc}")
    rows = {str(s.get("n")): s for s in (spec or {}).get("slots") or []}
    key = n if n in rows else (n.zfill(2) if n.isdigit() else n)
    if key not in rows:
        raise CouldNotRun(f"the register {slots_path} has no row {n!r}; its rows are "
                          f"{', '.join(rows)}")
    return rows[key]


def checklist_for(row: dict, code: str, kit_root: pathlib.Path) -> pathlib.Path:
    cell = (row.get("check") or {}).get("checklist")
    if isinstance(cell, str) and cell.strip() and not cell.strip().lower().startswith("absent"):
        return kit_root / cell.strip()
    default = kit_root / "templates" / "spec" / "checklists" / f"{code}.md"
    if default.exists():
        return default
    raise CouldNotRun(f"row {row.get('n')} names no checklist (its check.checklist reads "
                      f"{cell!r}) and {default} is not there; a claim is made from a checklist")


def _rel(path: pathlib.Path, kit_root: pathlib.Path) -> str:
    try:
        return path.resolve().relative_to(kit_root.resolve()).as_posix()
    except ValueError:
        return str(path.resolve())


# --------------------------------------------------------------------------- the claim

def judge(rules, verdicts: dict, kit_root: pathlib.Path) -> tuple[list[str], list[str]]:
    """The lines of the claim, in the checklist's order, and every refusal."""
    refusals: list[str] = []
    by_rule = dict(rules)
    for rule in verdicts:
        if rule not in by_rule:
            refusals.append(f"{rule}: a verdict for a rule the checklist does not carry")
    lines: list[str] = []
    for rule, programs in rules:
        if rule not in verdicts:
            refusals.append(f"{rule}: no verdict — the claim would not be rule by rule")
            continue
        v = verdicts[rule]
        if isinstance(v, str):
            word, check = v, ""
        elif isinstance(v, dict):
            word, check = v.get("verdict", ""), v.get("check", "")
        else:
            refusals.append(f"{rule}: {v!r} is not a verdict")
            continue
        word = " ".join(str(word).lower().split())
        check = " ".join(str(check or "").replace("`", "").split())
        if word not in VERDICTS:
            refusals.append(f"{rule}: {word!r} is not a verdict word of the claim — "
                            f"only {', '.join(VERDICTS)}")
            continue
        if not check or check.lower() == NO_PROGRAM:
            check = NO_PROGRAM
        elif not programs:
            refusals.append(f"{rule}: cites {check}, a check no program performs — the "
                            f"checklist names no program for {rule}")
            continue
        elif check not in programs:
            refusals.append(f"{rule}: cites {check}, a check no program performs for this "
                            f"rule — the checklist names {', '.join(programs)} for {rule}")
            continue
        elif not held_by_the_kit(check, kit_root):
            refusals.append(f"{rule}: cites {check}, a check no program performs — the kit "
                            f"does not hold {check}")
            continue
        lines.append(f"{rule}{SEP}{word}{SEP}{check}")
    return lines, refusals


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="kit conform", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("n", help="the row of the register, as it writes it: 01 to 09, or 08a")
    ap.add_argument("artifact", type=pathlib.Path)
    ap.add_argument("--verdicts", type=pathlib.Path,
                    help="default: _conformance/<artifact's file name>_verdicts.yaml beside it")
    ap.add_argument("--checklist", type=pathlib.Path,
                    help="default: the checklist the register's row names")
    ap.add_argument("--slots", type=pathlib.Path, default=SLOTS)
    ap.add_argument("--kit-root", type=pathlib.Path, default=KIT_ROOT)
    a = ap.parse_args(argv)

    try:
        return _run(a)
    except CouldNotRun as exc:
        print(f"kit conform: could not run: {exc}", file=sys.stderr)
        return 2


def _run(a) -> int:
    kit_root = a.kit_root.resolve()
    artifact = a.artifact
    if not artifact.is_file():
        raise CouldNotRun(f"the artifact {artifact} is not there")
    row = row_of(a.slots, a.n)
    st = row.get("standard") or {}
    code = st.get("code")
    if not code:
        reason = " ".join(str(st.get("absent", "")).split())
        raise CouldNotRun(f"row {row.get('n')} names no standard, so there is nothing to "
                          f"conform to{': ' + reason if reason else ''}")
    checklist = (a.checklist if a.checklist else checklist_for(row, code, kit_root))
    if not checklist.is_file():
        raise CouldNotRun(f"the checklist {checklist} is not there")
    text = checklist.read_text(encoding="utf-8")
    head, _, err = read_head(text)
    if head is None:
        raise CouldNotRun(f"the checklist {checklist} has no head in the form of PLAN.md "
                          f"section 3.1: {err}")
    missing = [k for k in HEAD_NEEDS if not str(head.get(k, "")).strip()]
    if missing:
        raise CouldNotRun(f"the checklist's head lacks {', '.join(missing)} (PLAN.md section 3.1)")
    if head["standard"] != code:
        raise CouldNotRun(f"the checklist {checklist} is the checklist of {head['standard']}; "
                          f"row {row.get('n')} names {code}")
    rules = rules_of(text)
    if not rules:
        raise CouldNotRun(f"the checklist {checklist} names no rule under `## Rules`; a claim "
                          f"of no rules is not written")
    seen: set[str] = set()
    twice = sorted({r for r, _ in rules if r in seen or seen.add(r)})
    if twice:
        raise CouldNotRun(f"the checklist {checklist} carries {', '.join(twice)} twice")

    out_dir = artifact.parent / "_conformance"
    verdicts_path = a.verdicts or out_dir / f"{artifact.name}_verdicts.yaml"
    if not verdicts_path.is_file():
        raise CouldNotRun(f"no verdicts at {verdicts_path}: a claim is written from the answer "
                          f"to each rule of the checklist, one entry per rule")
    verdicts, twice_refusal = read_verdicts(verdicts_path)
    out = out_dir / f"{artifact.name}_conformance.md"

    print(f"kit conform {row.get('n')} {artifact} at {now()}")
    print(f"  standard   {code} {head['edition']} — {head['document']}")
    standing = str(st.get("standing", ""))
    if "draft" in standing:
        print(f"  {code} is a {standing}: its rules are not rules in force")
    print(f"  checklist  {_rel(checklist, kit_root)}, {len(rules)} rules")
    print(f"  verdicts   {verdicts_path}")
    if twice_refusal:
        print(f"  REFUSED, nothing written: {twice_refusal}")
        return 1
    lines, refusals = judge(rules, verdicts, kit_root)
    if refusals:
        print(f"  REFUSED, nothing written — {len(refusals)} line(s) would not stand:")
        for r in refusals:
            print(f"    - {r}")
        return 1

    head_lines = [
        "---",
        f"artifact: {artifact.name}",
        f"artifact_sha256: {sha256_of(artifact)}",
        f"standard: {code}",
        f'edition: "{head["edition"]}"',
        f"document: {head['document']}",
        f"document_sha256: {head['sha256']}",
        f"checklist: {_rel(checklist, kit_root)}",
        f"written_by: kit conform at {now()}",
        "---",
    ]
    out_dir.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(head_lines + lines) + "\n", encoding="utf-8")
    counts = {w: sum(1 for ln in lines if ln.split(SEP)[1] == w) for w in VERDICTS}
    print(f"  written    {out}")
    print(f"             {len(lines)} rules: {counts['met']} met, {counts['not met']} not met, "
          f"{counts['not applicable']} not applicable; "
          f"{sum(1 for ln in lines if not ln.endswith(NO_PROGRAM))} decided by a program")
    return 0


if __name__ == "__main__":
    sys.exit(main())
