#!/usr/bin/env python3
"""listings.py — the four listings of an interaction design, produced from the accepted screen
records of its goals and compared with those records as sets.

    python3 listings.py --form <form.yaml> [--out <dir>] [--appendix <document>]
                        [--expect <expected.yaml>] <screen record> [<screen record> ...]

WHAT IT READS. The screen records of the goals one writing of the application model carries,
each a Markdown file, in the form the application writes its screen records in. That form is
the application's own. This program does not know it: it reads it from the form file, which the
application keeps beside this program among its other programs. The form file names, in the
words the records themselves use:

  record.status   the table (its heading row), the row and the column where a record states
                  its status, who accepted it and when
  screen.opens    a pattern the line opening a screen matches, whose group `id` is the screen's
                  identifier
  values          the heading row of a screen's table of values; which of its columns holds the
                  value's identifier, its name, the record and attribute it shows, the other
                  record it points at, and the list it draws on; the pattern of a value's
                  identifier; the pattern a reference cell matches when the person picks the
                  record; the pattern an attribute cell matches when the value is a record's
                  state; and the pattern whose group `record` names the record in that cell
  acts            the heading row of a screen's table of acts; which of its columns holds the
                  act's identifier, its words, where it stands and where it leads; and the
                  pattern of an act's identifier
  none            the words a cell holds when it has nothing to say

WHAT IT REFUSES. It lists only records that stand accepted, as SDD-11 section 2 defines the
word, read with the words the kit's reader of an interaction design reads in a header
(tools/interaction_design.py in the kit): the status word `baselined`, and `accepted by <name>
on <date>`. Any other record is refused, by name, and nothing is written.

THE FOUR LISTINGS.
  1. every coded value, with the list it draws on
  2. every value that points at another record, with whether the person picks it
  3. every record whose state a screen shows, with the screens that show it
  4. every act, with where it stands and where it leads

THE COMPARISON, AS SETS. The listings are made by the first reading, and each is compared, as a
set of whole entries and never by counts, with the same listing made by a second reading of the
same records. The first reading reads each table by its heading row, its separator row and its
cells, takes a column by its name, and matches the form's patterns against the lines and cells
as they stand, with regard to case (the function classify decides what each row is). The second
reading calls none of this program's functions that the first reading calls: it reads the raw
lines, takes a line as a value or an act when its first cell matches that kind's identifier
pattern, wherever the line stands, takes its columns at the places the form file gives them, and
decides for itself what each row is. It matches every pattern of the form, the one for the line
that opens a screen as well as those for a row's cells, against the words of the line or the
cell as a person reads them: without regard to case, with the marks ` and * removed and a run of
white space read as one space. What the two readings have in common is the form file, read
once, the lines of the records, and the names of the four listings. Every entry one reading
finds and the other does not is printed, and the run exits 1: a row that one reader reads and
the other does not, or a cell whose place in a listing depends on how its words are typed, such
as `loan · State` where the form's pattern reads `· state`.

WHAT THE COMPARISON DOES NOT SEE. Both readings take the form file as the only statement of what
makes a value a coded value, a reference or a record's state. A cell written in other words than
the form's, such as `loan · status` where the form's pattern reads `· state`, is left out of the
listing by both readings, and the comparison is equal. So the program also prints every value it
placed in no listing; the person reads each of them against the four listings, and where one
belongs to a listing, the record's cell or the form file is corrected, never the listing, and the
program is run again.

With --expect, each listing is also compared, as a set, with the entries a file of expected
listings gives.

WHAT IT WRITES. listings.md (the listings and the comparison, as tables) and listings.json (the
same, with the values placed in no listing) into --out. With --appendix, the same tables into the
document below its appendix heading, replacing whatever stood there, and the document's header
row `The program of its listings` rewritten to name this program and the form file by path and
checksum. It writes no time, so that two runs over the same files write the same bytes.

Exit: 0 written, and every comparison equal · 1 refused, or a comparison unequal, or a row that
could not be read · 2 could not run.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import pathlib
import re
import sys

try:
    import yaml
except ImportError:                                            # pragma: no cover
    print("listings.py: could not run: the Python package yaml is not installed", file=sys.stderr)
    sys.exit(2)

HEADER_ROW = "The program of its listings"     # the kit's template of the document, its header
APPENDIX = re.compile(r"^## 7\.")               # the kit's template: part 7, the appendix
STATUS = re.compile(r"\b(draft|reviewed|baselined)\b", re.I)
ACCEPTED = re.compile(r"accepted by\s+(.+?)\s+on\s+(\d{1,2}\s+[A-Za-z]+\s+\d{4}|\d{4}-\d{2}-\d{2})",
                      re.I)
SEPARATOR = re.compile(r"^:?-{3,}:?$")
KINDS = ("coded", "references", "states", "acts")
TITLES = {
    "coded": "Every coded value, with the list it draws on",
    "references": "Every value that points at another record, with whether the person picks it",
    "states": "Every record whose state a screen shows",
    "acts": "Every act, with where it stands and where it leads",
}
COLUMNS = {
    "coded": ("Screen", "Value", "Name", "List"),
    "references": ("Screen", "Value", "Name", "Record · attribute", "Picked by the person"),
    "states": ("Record", "Screen", "Value"),
    "acts": ("Screen", "Act", "Words", "Stands on", "Leads to"),
}


class CouldNotRun(Exception):
    pass


def sha256_of(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


# --------------------------------------------------------------------------- the form file

def read_form(path: pathlib.Path) -> dict:
    try:
        form = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError) as exc:
        raise CouldNotRun(f"the form file {path} could not be read: {exc}")
    need = {"record": ["status"], "screen": ["opens"],
            "values": ["heading", "id", "id_pattern", "name", "attribute", "reference", "list",
                       "picked", "state", "record_of"],
            "acts": ["heading", "id", "id_pattern", "words", "stands_on", "leads_to"]}
    missing = [f"{part}.{key}" for part, keys in need.items() for key in keys
               if key not in (form.get(part) or {})]
    for key in ("table", "row", "column"):
        if key not in ((form.get("record") or {}).get("status") or {}):
            missing.append(f"record.status.{key}")
    if missing:
        raise CouldNotRun(f"the form file {path} does not say {', '.join(missing)}")
    for part in ("values", "acts"):
        heading = [str(c) for c in form[part]["heading"]]
        for key, col in form[part].items():
            if key in ("heading", "id_pattern", "picked", "state", "record_of"):
                continue
            if str(col) not in heading:
                raise CouldNotRun(f"the form file {path}: {part}.{key} names the column {col!r}, "
                                  f"which its heading row {heading} does not hold")
    form.setdefault("none", ["—", "-", "none", ""])
    form["none"] = [str(x).strip().lower() for x in form["none"]]
    return form


def is_none(cell: str, form: dict) -> bool:
    return cell.strip().strip("`").strip().lower() in form["none"]


def record_of(cell: str, form: dict) -> str:
    m = re.search(form["values"]["record_of"], cell)
    return (m.group("record") if m else cell).strip()


# --------------------------------------------------------------------------- the first reading

def cells_escaped(line: str) -> list[str]:
    body = line.strip()
    if body.startswith("|"):
        body = body[1:]
    if body.endswith("|") and not body.endswith("\\|"):
        body = body[:-1]
    return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", body)]


def tables_of(lines: list[str]):
    """Every table: (heading cells, its line, [(line, cells)]); a heading row counts only with a
    separator row beneath it."""
    out, i = [], 0
    while i < len(lines):
        if (lines[i].lstrip().startswith("|") and i + 1 < len(lines)
                and lines[i + 1].lstrip().startswith("|")
                and all(SEPARATOR.match(c.replace(" ", "")) for c in cells_escaped(lines[i + 1])
                        if c.strip())):
            head, rows, j = tuple(cells_escaped(lines[i])), [], i + 2
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                rows.append((j + 1, cells_escaped(lines[j])))
                j += 1
            out.append((head, i + 1, rows))
            i = j
        else:
            i += 1
    return out


def screen_at(lines: list[str], form: dict) -> list:
    """The screen each line stands in: the identifier of the last opening line above it."""
    opens, cur, where = re.compile(form["screen"]["opens"]), None, []
    for ln in lines:
        m = opens.search(ln)
        if m:
            cur = m.group("id")
        where.append(cur)
    return where


def status_of(lines: list[str], form: dict) -> tuple[str | None, str]:
    st = form["record"]["status"]
    for head, _, rows in tables_of(lines):
        if list(head) != [str(c) for c in st["table"]]:
            continue
        for _, cells in rows:
            row = dict(zip(head, cells))
            first = row.get(str(head[0]), "")
            if " ".join(first.split()).lower() == str(st["row"]).lower():
                entry = row.get(str(st["column"]), "")
                m = STATUS.search(entry)
                return (m.group(1).lower() if m else None), " ".join(entry.split())
    return None, ""


def first_reading(name: str, lines: list[str], form: dict, problems: list) -> dict:
    """The listings, and under `values` every value row read, whatever listing it went to."""
    where = screen_at(lines, form)
    sets = {k: set() for k in KINDS + ("values",)}
    seen: dict = {}
    for part in ("values", "acts"):
        spec = form[part]
        heading = tuple(str(c) for c in spec["heading"])
        idp = re.compile(spec["id_pattern"])
        for head, at, rows in tables_of(lines):
            if head != heading:
                continue
            for ln, cells in rows:
                if len(cells) != len(head):
                    problems.append(f"{name}, line {ln}: the row has {len(cells)} cells and its "
                                    f"table has {len(head)}")
                    continue
                row = dict(zip(head, cells))
                vid, screen = row[str(spec["id"])], where[ln - 1]
                if not idp.match(vid):
                    problems.append(f"{name}, line {ln}: {vid!r} is not an identifier of the "
                                    f"form's {part}")
                    continue
                if screen is None:
                    problems.append(f"{name}, line {ln}: {vid} stands before any screen opens")
                    continue
                key = (part, screen, vid)
                if key in seen:
                    problems.append(f"{name}, line {ln}: {screen} {vid} is written twice (first at "
                                    f"line {seen[key]})")
                    continue
                seen[key] = ln
                classify(part, screen, vid, row, spec, form, sets)
                if part == "values":
                    sets["values"].add((screen, vid, row[str(spec["name"])],
                                        row[str(spec["attribute"])]))
    return sets


def classify(part: str, screen: str, vid: str, row: dict, spec: dict, form: dict,
             sets: dict) -> None:
    if part == "acts":
        sets["acts"].add((screen, vid, row[str(spec["words"])], row[str(spec["stands_on"])],
                          row[str(spec["leads_to"])]))
        return
    name, attr = row[str(spec["name"])], row[str(spec["attribute"])]
    if not is_none(row[str(spec["list"])], form):
        sets["coded"].add((screen, vid, name, row[str(spec["list"])]))
    ref = row[str(spec["reference"])]
    if not is_none(ref, form):
        picked = "yes" if re.search(spec["picked"], ref) else "no"
        sets["references"].add((screen, vid, name, attr, picked))
    if re.search(spec["state"], attr):
        sets["states"].add((record_of(attr, form), screen, vid))


# --------------------------------------------------------------------------- the second reading

MARKS = str.maketrans("", "", "`*")


def as_read(text: str) -> str:
    """The words of a line or a cell as a person reads them: the marks ` and * removed, a run of
    white space one space. The second reading matches every pattern of the form against these,
    without regard to case."""
    return " ".join(text.translate(MARKS).split())


def second_reading(lines: list[str], form: dict) -> dict:
    """The raw lines, with no table reader and none of the functions the first reading calls: a
    line whose first cell matches a kind's identifier pattern is an entry of that kind, its columns
    are taken at the places the form gives, and what the entry is — a coded value, a reference,
    whether the person picks it, a record's state and which record's — is decided here, by the
    form's patterns matched against the words of each line and cell as a person reads them
    (as_read) and without regard to case."""
    fold = re.IGNORECASE
    opens, screen = re.compile(form["screen"]["opens"], fold), None
    nothing = {as_read(str(w)).casefold() for w in form["none"]}
    sets = {k: set() for k in KINDS}
    columns = {part: [str(c) for c in form[part]["heading"]] for part in ("values", "acts")}
    at = {part: {key: columns[part].index(str(form[part][key])) for key in keys}
          for part, keys in (("values", ("id", "name", "attribute", "reference", "list")),
                             ("acts", ("id", "words", "stands_on", "leads_to")))}
    for raw in lines:
        m = opens.search(as_read(raw))
        if m:
            screen = m.group("id")
            continue
        if not raw.strip().startswith("|") or screen is None:
            continue
        parts = [p.strip() for p in raw.strip().strip("|").split("|")]
        for part in ("values", "acts"):
            spec = form[part]
            if (len(parts) < len(columns[part])
                    or not re.match(spec["id_pattern"], as_read(parts[0]), fold)):
                continue
            cell = {key: parts[i] for key, i in at[part].items()}
            if part == "acts":
                sets["acts"].add((screen, cell["id"], cell["words"], cell["stands_on"],
                                  cell["leads_to"]))
                continue
            if as_read(cell["list"]).casefold() not in nothing:
                sets["coded"].add((screen, cell["id"], cell["name"], cell["list"]))
            if as_read(cell["reference"]).casefold() not in nothing:
                picked = re.search(spec["picked"], as_read(cell["reference"]), fold)
                sets["references"].add((screen, cell["id"], cell["name"], cell["attribute"],
                                        "yes" if picked else "no"))
            if re.search(spec["state"], as_read(cell["attribute"]), fold):
                owner = re.search(spec["record_of"], as_read(cell["attribute"]), fold)
                sets["states"].add(((owner.group("record") if owner
                                     else as_read(cell["attribute"])).strip(), screen, cell["id"]))
    return sets


# --------------------------------------------------------------------------- writing

def table(cols, rows) -> list[str]:
    out = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for r in rows:
        out.append("| " + " | ".join(str(c).replace("|", "\\|") for c in r) + " |")
    if not rows:
        out.append("| " + " | ".join(["none"] + [""] * (len(cols) - 1)) + " |")
    return out


def render(listings, comparison, inputs, program, form_file, base) -> str:
    def shown(p):
        return os.path.relpath(os.path.realpath(p), base)
    out = [f"The four listings below were produced by `{shown(program)}`, SHA-256 "
           f"`{sha256_of(program)}`, from the screen records named here, read in the form the "
           f"application declares in `{shown(form_file)}`, SHA-256 `{sha256_of(form_file)}`. "
           "Each listing is made by a first reading of the records and compared, as a set of whole "
           "entries, with the same listing made by a second reading, which calls none of the "
           "program's functions that the first calls and matches the form's patterns against "
           "the records' words without regard to case, to backticks and asterisks, or to runs of "
           "white space; the last table gives the comparison. The two readings have the form in "
           "common, so a value whose cell is written in other words than the form's is left out "
           "of a listing by both, and the comparison does not see it; each run of the program "
           "names every value it placed in no listing, to be read against the four listings.",
           ""]
    out += table(("Screen record", "SHA-256", "Its status, as it reads"),
                 [(f"`{shown(p)}`", f"`{h}`", s) for p, h, s in inputs])
    for n, kind in enumerate(KINDS, 1):
        out += ["", f"### 7.{n} {TITLES[kind]}", ""]
        out += table(COLUMNS[kind], sorted(listings[kind]))
    out += ["", "### 7.5 The comparison with a second reading of the screen records, as sets", ""]
    rows = []
    for kind in KINDS:
        c = comparison[kind]
        rows.append((TITLES[kind], c["first"], c["second"], c["both"],
                     "; ".join(" · ".join(e) for e in c["only_first"]) or "none",
                     "; ".join(" · ".join(e) for e in c["only_second"]) or "none",
                     "yes" if c["equal"] else "**no**"))
    out += table(("Listing", "First reading", "Second reading", "In both", "Only in the first",
                  "Only in the second", "Equal as sets"), rows)
    return "\n".join(out) + "\n"


def write_appendix(doc: pathlib.Path, body: str, program: pathlib.Path,
                   form_file: pathlib.Path) -> None:
    lines = doc.read_text(encoding="utf-8").split("\n")
    at = next((i for i, ln in enumerate(lines) if APPENDIX.match(ln)), None)
    if at is None:
        raise CouldNotRun(f"the document {doc} has no appendix heading (a line beginning `## 7.`)")
    base = os.path.realpath(doc.parent)
    entry = (f"`{os.path.relpath(os.path.realpath(program), base)}`, SHA-256 "
             f"`{sha256_of(program)}`; the form it reads, "
             f"`{os.path.relpath(os.path.realpath(form_file), base)}`, SHA-256 "
             f"`{sha256_of(form_file)}`")
    for i, ln in enumerate(lines[:at]):
        cells = cells_escaped(ln) if ln.lstrip().startswith("|") else []
        if cells and cells[0] == HEADER_ROW:
            lines[i] = f"| {HEADER_ROW} | {entry} |"
    doc.write_text("\n".join(lines[:at + 1] + ["", body.rstrip("\n"), ""]), encoding="utf-8")


# --------------------------------------------------------------------------- the run

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="listings.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--form", type=pathlib.Path, required=True)
    ap.add_argument("--out", type=pathlib.Path)
    ap.add_argument("--appendix", type=pathlib.Path)
    ap.add_argument("--expect", type=pathlib.Path)
    ap.add_argument("records", type=pathlib.Path, nargs="+")
    a = ap.parse_args(argv)
    try:
        return run(a)
    except CouldNotRun as exc:
        print(f"listings.py: could not run: {exc}", file=sys.stderr)
        return 2


def run(a) -> int:
    form = read_form(a.form)
    program = pathlib.Path(__file__).resolve()
    refused, problems, inputs = [], [], []
    first = {k: set() for k in KINDS + ("values",)}
    second = {k: set() for k in KINDS}
    for path in sorted(a.records, key=lambda p: str(p)):
        if not path.is_file():
            raise CouldNotRun(f"the screen record {path} is not there")
        text = path.read_text(encoding="utf-8")
        lines = text.split("\n")
        status, entry = status_of(lines, form)
        if status != "baselined" or not ACCEPTED.search(entry):
            refused.append(f"{path}: it reads {entry or 'no status'!r}, which is not baselined "
                           f"with `accepted by <name> on <date>`")
            continue
        inputs.append((path.resolve(), sha256_of(path), entry))
        for k, v in first_reading(path.name, lines, form, problems).items():
            first[k] |= v
        for k, v in second_reading(lines, form).items():
            second[k] |= v
    if refused:
        print("listings.py: REFUSED, nothing written — a record that is not accepted is not read:")
        for r in refused:
            print(f"  - {r}")
        return 1
    comparison = {}
    for k in KINDS:
        both = first[k] & second[k]
        comparison[k] = {"first": len(first[k]), "second": len(second[k]), "both": len(both),
                         "only_first": sorted(first[k] - second[k]),
                         "only_second": sorted(second[k] - first[k]),
                         "equal": first[k] == second[k]}
    placed = ({(e[0], e[1]) for k in ("coded", "references") for e in first[k]}
              | {(e[1], e[2]) for e in first["states"]})
    unlisted = sorted(e for e in first["values"] if (e[0], e[1]) not in placed)
    base = (os.path.realpath(a.appendix.parent) if a.appendix
            else os.path.realpath(os.getcwd()))
    body = render(first, comparison, inputs, program, a.form.resolve(), base)
    if a.out:
        a.out.mkdir(parents=True, exist_ok=True)
        (a.out / "listings.md").write_text(body, encoding="utf-8")
        (a.out / "listings.json").write_text(json.dumps(
            {"program": {"path": str(program), "sha256": sha256_of(program)},
             "form": {"path": str(a.form.resolve()), "sha256": sha256_of(a.form)},
             "records": [{"path": str(p), "sha256": h, "status": s} for p, h, s in inputs],
             "listings": {k: [list(e) for e in sorted(first[k])] for k in KINDS},
             "comparison": comparison, "problems": problems,
             "in_no_listing": [list(e) for e in unlisted]},
            indent=1, ensure_ascii=False, default=list) + "\n", encoding="utf-8")
    if a.appendix:
        write_appendix(a.appendix, body, program, a.form.resolve())
    print(f"listings.py: {len(inputs)} accepted screen records read, in the form of {a.form}")
    for k in KINDS:
        c = comparison[k]
        print(f"  {TITLES[k]}: {c['first']} entries; the second reading {c['second']}; "
              f"{'equal as sets' if c['equal'] else 'NOT EQUAL as sets'}")
        for e in c["only_first"]:
            print(f"      only in the first reading:  {' · '.join(e)}")
        for e in c["only_second"]:
            print(f"      only in the second reading: {' · '.join(e)}")
    print(f"  Values placed in no listing, each to be read against the four listings, since the "
          f"comparison does not see a cell written in other words than the form's: {len(unlisted)}")
    for e in unlisted:
        print(f"      {' · '.join(e)}")
    for p in problems:
        print(f"  cannot read: {p}")
    bad = bool(problems) or not all(c["equal"] for c in comparison.values())
    if a.expect:
        expected = yaml.safe_load(a.expect.read_text(encoding="utf-8")) or {}
        for k in KINDS:
            want = {tuple(str(x) for x in e) for e in (expected.get(k) or [])}
            got = {tuple(str(x) for x in e) for e in first[k]}
            same = want == got
            bad = bad or not same
            print(f"  against {a.expect.name}, {k}: {len(got)} listed, {len(want)} expected; "
                  f"{'equal as sets' if same else 'NOT EQUAL as sets'}")
            for e in sorted(got - want):
                print(f"      listed, not expected: {' · '.join(e)}")
            for e in sorted(want - got):
                print(f"      expected, not listed: {' · '.join(e)}")
    if a.out:
        print(f"  written    {a.out / 'listings.md'} and {a.out / 'listings.json'}")
    if a.appendix:
        print(f"  written    the appendix and the header row of {a.appendix}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
