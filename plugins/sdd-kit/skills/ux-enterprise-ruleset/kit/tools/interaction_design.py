#!/usr/bin/env python3
"""interaction_design — read an interaction design the way the kit's gate reads it.

The interaction design of an application is the document SDD-11 governs: written once for the
goals an increment of the application model carries, accepted by the owner, and named by the
model in its entry `model.interaction_design` by its path and its SHA-256 checksum. It is written
from the kit's template, `templates/spec/INTERACTION_DESIGN.md.tmpl`, which fixes how a row of a
decision table names the construct of the model it governs and which words the gate reads in each
column it compares (SDD-11, section 8.2, last paragraph). This module reads exactly that and
nothing else; `validate.py`'s rule L021 compares what it reads with the model.

What is read, from the document's Markdown:

  * the header table, whose heading row is `| Line | Entry |`, and in it the row whose Line cell
    reads `Version and status`: its status is the first of the words draft, reviewed and
    baselined its Entry cell holds, and a baselined document says, in the same cell,
    `accepted by <name> on <date>`, the date written `25 September 2026` or `2026-09-25`;
  * the table of the goals the document covers, whose heading row is
    `| Goal | Its description | Its screen record |`, each row naming its goal by the goal's
    identifier between backticks;
  * the five decision tables, each found by its heading row exactly as SDD-11 IXD-27 fixes it,
    one row for each thing decided.

An identifier is read only between single backticks, and only in the cells the template names.
A table is a run of lines beginning with `|`: its heading row, the separator row beneath it, and
the rows that follow until the first line that does not begin with `|`. A cell may hold a `|`
written `\\|`. A table the gate needs that is missing, or that stands twice, is reported; so is a
row whose number of cells is not its table's.

This module judges nothing. It reports what the document says, where it says it (the line
number of every row), and what it could not read.
"""
from __future__ import annotations

import dataclasses
import datetime
import hashlib
import pathlib
import re

# ---- the headings the gate finds its tables by (SDD-11, section 7 and IXD-27) ----------------
HEADER = ("Line", "Entry")
STATUS_LINE = "Version and status"
GOALS = ("Goal", "Its description", "Its screen record")
LISTS = ("List", "Kept where", "Members in force", "Maintained or fixed", "Maintained by",
         "First values from", "Code shown as label", "Depends on", "Categories", "Pattern")
REFERENCES = ("Place", "Record set", "How many", "Found by", "Searched by", "Result shows",
              "Fills", "Locks", "When nothing is found", "Pattern")
MOVES = ("Record", "From", "To", "Made by (goal, act)", "Role", "Button",
         "Guard, in the words shown")
READ_ONLY = ("Record", "State", "Values read-only in it")
ACTS = ("Act", "Stands on", "Carries", "Opens", "Filled and locked", "Returns to", "On a menu")

TABLES = {"header": HEADER, "goals": GOALS, "Lists": LISTS, "References": REFERENCES,
          "Moves": MOVES, "Read-only": READ_ONLY, "Acts": ACTS}

# ---- the words the gate reads ----------------------------------------------------------------
STATUS_WORDS = ("draft", "reviewed", "baselined")
NOT_IN_THE_MODEL = "not in the model"

_CODE = re.compile(r"`([^`]+)`")
_STATUS = re.compile(r"\b(draft|reviewed|baselined)\b", re.I)
_ACCEPTED = re.compile(r"accepted by\s+(.+?)\s+on\s+(\d{1,2}\s+[A-Za-z]+\s+\d{4}|\d{4}-\d{2}-\d{2})",
                       re.I)
_ACCEPTED_BY = re.compile(r"accepted by\s+(.+?)(?:\s+on\s+(.+?))?\s*$", re.I)
_SEPARATOR = re.compile(r"^:?-{3,}:?$")


def sha256_of(path: pathlib.Path) -> str:
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()


def identifiers(cell: str) -> list[str]:
    """The identifiers a cell names: the text between each pair of single backticks."""
    return [x.strip() for x in _CODE.findall(cell or "") if x.strip()]


def words(cell: str) -> str:
    """The cell's words for comparison: backticked identifiers removed, lower case, one space."""
    return " ".join(_CODE.sub(" ", cell or "").lower().split())


def first_of(cell: str, choices: tuple) -> str | None:
    """The first of `choices` that stands in the cell as a whole word (case not minded)."""
    text = words(cell)
    best = None
    for c in choices:
        m = re.search(r"(?<![a-z])" + re.escape(c) + r"(?![a-z])", text)
        if m and (best is None or m.start() < best[0]):
            best = (m.start(), c)
    return best[1] if best else None


def says_not_in_the_model(cell: str) -> bool:
    return NOT_IN_THE_MODEL in words(cell)


def reads_as(cell: str, phrase: str) -> bool:
    """The cell's words begin with `phrase`, as whole words (case not minded, backticked
    identifiers set aside): 'nothing: the applicant may correct either' reads as 'nothing'."""
    return re.match(re.escape(phrase) + r"(?![a-z0-9])", words(cell)) is not None


@dataclasses.dataclass
class Row:
    line: int                     # the line of the document the row stands on, counted from 1
    cells: dict                   # heading -> the cell's text, trimmed

    def ids(self, col: str) -> list[str]:
        return identifiers(self.cells.get(col, ""))

    def text(self, col: str) -> str:
        return self.cells.get(col, "")

    def label(self, width: int = 70) -> str:
        """The row's first cell, as the owner reads it, for a message that names the row."""
        first = next(iter(self.cells.values()), "")
        text = " ".join(str(first).split())
        return text if len(text) <= width else text[:width - 1].rstrip() + "…"


@dataclasses.dataclass
class Document:
    path: pathlib.Path
    sha256: str
    tables: dict                  # name -> [Row]
    table_lines: dict             # name -> the line of its heading row
    problems: list                # (table name, line, what could not be read)
    status: str | None = None
    status_entry: str = ""
    status_line: int | None = None
    accepted_by: str | None = None
    accepted_on: datetime.date | None = None
    accepted_on_text: str | None = None
    goals: list = dataclasses.field(default_factory=list)     # [(goal identifier, line)]

    def has(self, name: str) -> bool:
        return name in self.tables


def _cells(line: str) -> list[str]:
    body = line.strip()
    if body.startswith("|"):
        body = body[1:]
    if body.endswith("|") and not body.endswith("\\|"):
        body = body[:-1]
    parts = re.split(r"(?<!\\)\|", body)
    return [p.strip().replace("\\|", "|") for p in parts]


def _is_separator(line: str) -> bool:
    cells = [c.replace(" ", "") for c in _cells(line) if c.strip()]
    return bool(cells) and all(_SEPARATOR.match(c) for c in cells)


def _tables(lines: list[str]):
    """Every Markdown table of the document: (heading cells, heading line, [(line, cells)])."""
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.lstrip().startswith("|") and i + 1 < len(lines) \
                and lines[i + 1].lstrip().startswith("|") and _is_separator(lines[i + 1]):
            head = tuple(_cells(line))
            rows = []
            j = i + 2
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                rows.append((j + 1, _cells(lines[j])))
                j += 1
            out.append((head, i + 1, rows))
            i = j
            continue
        i += 1
    return out


def _date(text: str) -> datetime.date | None:
    for fmt in ("%d %B %Y", "%Y-%m-%d"):
        try:
            return datetime.datetime.strptime(" ".join(text.split()), fmt).date()
        except ValueError:
            continue
    return None


def read(path) -> Document:
    """Read the interaction design at `path` as the gate reads it."""
    path = pathlib.Path(path)
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    lines = text.splitlines()
    doc = Document(path=path, sha256=hashlib.sha256(raw).hexdigest(), tables={}, table_lines={},
                   problems=[])
    wanted = {head: name for name, head in TABLES.items()}
    for head, at, rows in _tables(lines):
        name = wanted.get(head)
        if name is None:
            continue
        if name in doc.tables:
            doc.problems.append((name, at, f"a second table with the headings of the {name} "
                                           f"table stands at line {at}; the first is at line "
                                           f"{doc.table_lines[name]}, and the gate reads one"))
            continue
        doc.table_lines[name] = at
        doc.tables[name] = []
        for ln, cells in rows:
            if len(cells) != len(head):
                doc.problems.append((name, ln, f"the row at line {ln} has {len(cells)} cells and "
                                               f"the {name} table has {len(head)} columns"))
                continue
            doc.tables[name].append(Row(line=ln, cells=dict(zip(head, cells))))

    # the header's status, and who accepted it when
    for row in doc.tables.get("header", []):
        if " ".join(row.text("Line").split()).lower() == STATUS_LINE.lower():
            entry = row.text("Entry")
            doc.status_entry, doc.status_line = entry, row.line
            m = _STATUS.search(_CODE.sub(" ", entry))
            doc.status = m.group(1).lower() if m else None
            a = _ACCEPTED.search(_CODE.sub(" ", entry))
            if a:
                doc.accepted_by = " ".join(a.group(1).split()).strip(" ,;")
                doc.accepted_on_text = a.group(2)
                doc.accepted_on = _date(a.group(2))
            else:                       # a name with no date the gate can read: say so, not "nobody"
                b = _ACCEPTED_BY.search(_CODE.sub(" ", entry))
                if b:
                    doc.accepted_by = " ".join(b.group(1).split()).strip(" ,;") or None
                    doc.accepted_on_text = " ".join((b.group(2) or "").split()) or None
            break

    # the goals it covers
    for row in doc.tables.get("goals", []):
        ids = row.ids("Goal")
        if not ids:
            doc.problems.append(("goals", row.line, f"the row at line {row.line} of the table of "
                                                    f"goals names no goal by its identifier "
                                                    f"between backticks"))
            continue
        doc.goals.append((ids[0], row.line))
    return doc


if __name__ == "__main__":                                   # a reader's own view, for a person
    import sys
    d = read(sys.argv[1])
    print(f"{d.path} · SHA-256 {d.sha256}")
    print(f"  status   {d.status} (line {d.status_line}); accepted by {d.accepted_by} "
          f"on {d.accepted_on_text}")
    print(f"  goals    {', '.join(g for g, _ in d.goals) or 'none'}")
    for name in TABLES:
        if name in ("header", "goals"):
            continue
        rows = d.tables.get(name)
        print(f"  {name:<11} {'missing' if rows is None else str(len(rows)) + ' rows'}"
              + (f" (line {d.table_lines[name]})" if name in d.table_lines else ""))
    for name, ln, what in d.problems:
        print(f"  cannot read ({name}, line {ln}): {what}")
