#!/usr/bin/env python3
"""screens_walk — the clickable walk-through produced from a screen record (SDD-07 section 8).

    kit screens walk <screen record> [--out D] [--template F]

Reads one screen record — the screens of one use case, written as a filled copy of the kit's
template `templates/spec/artefacts/07_screen_record.md` (SDD-07 sections 5 and 11) — and writes
the walk-through as plain web pages into one folder: an index, one page for every screen, one page
for every variation carried on a screen, and one page for every ending. The pages open in an
ordinary web browser with nothing to install and nothing fetched from anywhere else: no script, no
file outside the folder. Every page carries, on one line, the record's identifier, its version and
its status, and the screen, step or variation the page serves (SDD-07 section 8, last paragraph).

Nothing appears on a page that the record does not carry. Nothing is calculated and nothing is
stored. A defect is corrected in the record and the pages are produced again; the pages are never
edited by hand (rule 23). The drawing's sizes, weights and colours are this program's, the same
for every set it produces, and are recorded against no screen (rule 26).

THE RECORD'S FORM. The record is a copy of the template with its Answer cells filled:
  - its first lines are the template's comment block, naming the standard it was written to;
  - its headings are the template's headings, in the template's order, and no others;
  - under the heading of the record header, and under "For each screen", the template's one table
    is written once for each screen, in the same order of screens under both headings; under every
    other heading the template's tables stand once each;
  - every table keeps the template's columns and lines; only the Answer cells differ.
A record outside that form is refused, naming the first departure.

INSIDE AN ANSWER. Identifiers are written between backticks. Several entries in one cell are
separated by <br>. An answer that begins with "None" has no entries.
  Status and version     "Draft, version 0.4" — one of draft, reviewed or baselined, and the
                         version. Every screen states it, and all of them state the same: the set
                         is versioned as a whole (SDD-07 section 1).
  Identifier             "`S2`" — the screen's identifier.
  Use cases              "`UC-X` <name>, version 1.0: steps 2 and 3; variations 2b and 4a".
  For a variation        "`2b` A variation of this screen, because …; it carries …" or
                         "`2a` A screen of its own, because …" — one entry for each variation.
  Where a value came from  "`S2.V1` <the value's name> — <where it came from, and the rest>".
  What the screen demands  "`S2.V1` <the least it demands and the most it admits>", one for
                         every value of the line above.
  Every rule cited       "`BR-1` at `S2.V4`: <its effect there>" — attached to every value of this
                         screen it names, otherwise to the screen.
  The acts               "<the act> → <target>", where the target is "`S3`", "`S2` with `2b`",
                         "raises `4a`" (this screen, with that variation) or "the use case ends in
                         success" (any words after "ends"). An act that belongs to a variation of
                         this screen begins "In `4a`: ".

WHAT THE PAGES OFFER. A screen's page offers the acts the record states for the screen. The page of
a variation carried on a screen shows that screen with what the variation carries, and offers only
the acts the record states for that variation, with a link back to the screen as it stands without
it. The record is refused when it leaves the person on a screen or in a variation with no act, when
an act leads to no screen of the record, and when a screen, a variation or an ending cannot be
reached from the first screen or cannot reach an ending.

THE RECORD'S IDENTIFIER is its file name without the extension: the template carries no line for
the set's own identifier, version and status (SDD-07 sections 5 and 11 name none), though section 8
and rule 27 require every page to carry them. The version and the status are the ones every screen
states.

EXIT CODES. 0 the pages are written; 1 the record is refused and nothing is written; 2 the program
could not run (a missing file, a template it cannot read, an output folder holding files it did
not write); 3 a defect of this program, found by its own check of the pages before any is written.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import pathlib
import re
import sys
from dataclasses import dataclass, field

HERE = pathlib.Path(__file__).resolve().parent
KIT_ROOT = HERE.parent
TEMPLATE = KIT_ROOT / "templates" / "spec" / "artefacts" / "07_screen_record.md"
GENERATOR = "kit screens walk"
GENERATOR_META = f'<meta name="generator" content="{GENERATOR}">'
STATUSES = ("draft", "reviewed", "baselined")

# The lines of the template this program reads, found by these words in the line's own text.
HEADER_LINES = ("Identifier", "Name", "Use cases", "Primary actor", "Entities",
                "Requirements realised", "Business rules cited", "Quality requirements cited",
                "Status and version")
PER_SCREEN = {"first": "the identifier, unique across the set",
              "variation": "for a variation",
              "origin": "for every value, where it came from",
              "demand": "the least the screen demands",
              "rules": "for every rule cited",
              "acts": "which act takes the person",
              "status": "the status and the version"}
PER_SET = {"produced": "how the walk-through is produced",
           "notation": "which notation is used",
           "commitment": "what agreeing to the walk-through commits"}


class Refusal(Exception):
    """The record is refused: exit 1, and nothing is written."""


class CannotRun(Exception):
    """The program could not run: exit 2, and nothing is written."""


# ------------------------------------------------------------------------------ reading markdown

_HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
_SEPARATOR = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$")
_BR = re.compile(r"<br\s*/?>", re.I)
_LEADING_ID = re.compile(r"^`([^`]+)`\s*(.*)$", re.S)


def norm(s: str) -> str:
    return " ".join(s.replace("\\|", "|").split())


def cells(line: str) -> list[str]:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", s)]


@dataclass
class Table:
    under: int                      # index of the heading it stands under; -1 before any heading
    header: list[str]
    rows: list[list[str]]
    line: int                       # line number of its header row


@dataclass
class Doc:
    head: dict
    headings: list                  # (level, text, line number)
    tables: list


def parse(text: str) -> Doc:
    lines = text.splitlines()
    head: dict = {}
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and lines[i].strip().startswith("<!--"):
        j = i
        while j < len(lines) and "-->" not in lines[j]:
            j += 1
        for ln in lines[i:j + 1]:
            inner = ln.strip()
            inner = inner[4:] if inner.startswith("<!--") else inner
            inner = inner[:-3] if inner.endswith("-->") else inner
            m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", inner.strip())
            if m:
                value = m.group(2).strip()
                if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                    value = value[1:-1]
                head[m.group(1)] = value
        i = j + 1
    headings: list = []
    tables: list = []
    fenced = False
    k = i
    while k < len(lines):
        ln = lines[k]
        if ln.strip().startswith("```"):
            fenced = not fenced
            k += 1
            continue
        if fenced:
            k += 1
            continue
        m = _HEADING.match(ln)
        if m:
            headings.append((len(m.group(1)), norm(m.group(2)), k + 1))
            k += 1
            continue
        if ln.lstrip().startswith("|") and k + 1 < len(lines) and _SEPARATOR.match(lines[k + 1]):
            header, start = cells(ln), k + 1
            rows = []
            k += 2
            while k < len(lines) and lines[k].lstrip().startswith("|"):
                rows.append(cells(lines[k]))
                k += 1
            tables.append(Table(len(headings) - 1, header, rows, start))
            continue
        k += 1
    return Doc(head, headings, tables)


# ------------------------------------------------------------------------ the template's form

@dataclass
class Form:
    standard: str
    edition: str
    headings: list                  # (level, text)
    tables: dict                    # heading index -> list of template tables under it
    header_at: int                  # the heading the record header stands under
    screen_at: int                  # the heading "For each screen"
    set_at: int                     # the heading "For the set as a whole"


def form_of(template: Doc, where: pathlib.Path) -> Form:
    if not template.head.get("standard"):
        raise CannotRun(f"the template {where} carries no comment block naming its standard")
    by_heading: dict = {}
    for t in template.tables:
        by_heading.setdefault(t.under, []).append(t)
    for t in template.tables:
        if [norm(c) for c in t.header].count("Answer") != 1:
            raise CannotRun(f"the template {where}: the table at line {t.line} has no single "
                            "column headed Answer")

    def the(test, what):
        found = [n for n, (lvl, text, _l) in enumerate(template.headings) if test(text)]
        if len(found) != 1 or len(by_heading.get(found[0], [])) != 1:
            raise CannotRun(f"the template {where} has no single table under {what}; "
                            "this program must be brought to the template")
        return found[0]

    return Form(standard=template.head["standard"], edition=template.head.get("edition", ""),
                headings=[(lvl, text) for lvl, text, _l in template.headings],
                tables=by_heading,
                header_at=the(lambda t: "record header" in t.lower(), "the record header"),
                screen_at=the(lambda t: t.lower() == "for each screen", "'For each screen'"),
                set_at=the(lambda t: t.lower() == "for the set as a whole",
                           "'For the set as a whole'"))


def answer_of(table: Table) -> int:
    """The column of a table's Answer cells."""
    return [norm(c) for c in table.header].index("Answer")


def _same_table(rec: Table, tpl: Table) -> str | None:
    """None if the record's table keeps the template's columns and lines; else the departure."""
    if [norm(c) for c in rec.header] != [norm(c) for c in tpl.header]:
        return f"the table at line {rec.line} has the columns {rec.header}, not {tpl.header}"
    answer = answer_of(tpl)
    where = f"the table at line {rec.line} ({len(rec.rows)} lines; the template's has {len(tpl.rows)})"
    for n in range(max(len(rec.rows), len(tpl.rows))):
        r = rec.rows[n] if n < len(rec.rows) else None
        t = tpl.rows[n] if n < len(tpl.rows) else None
        if t is None:
            return f"{where} has a line the template does not: '{norm(r[0])}'"
        if r is None or (len(rec.rows) < len(tpl.rows) and norm(r[0]) != norm(t[0])):
            return f"{where} lacks the template's line '{norm(t[0])}'"
        if len(r) != len(tpl.header):
            return f"line {n + 1} of {where} has {len(r)} cells, not {len(tpl.header)}"
        for c, (rc, tc) in enumerate(zip(r, t)):
            if c != answer and norm(rc) != norm(tc):
                return (f"line {n + 1} of {where} reads '{norm(rc)}' where the template reads "
                        f"'{norm(tc)}'")
    return None


def check_form(record: Doc, form: Form) -> tuple[list, list, Table]:
    """Refuse a record outside the template's form; return its header tables, its per-screen
    tables and its table for the set as a whole."""
    out = "outside the template's form: "
    if record.head.get("standard") != form.standard:
        raise Refusal(out + f"the record does not begin with the template's comment block naming "
                            f"{form.standard} (a filled copy of the template keeps its first lines)")
    got = [(lvl, text) for lvl, text, _l in record.headings]
    for n in range(max(len(got), len(form.headings))):
        mine = got[n] if n < len(got) else None
        theirs = form.headings[n] if n < len(form.headings) else None
        if mine != theirs:
            if mine is None:
                raise Refusal(out + f"the record lacks the heading '{'#' * theirs[0]} {theirs[1]}'")
            line = record.headings[n][2]
            if theirs is None:
                raise Refusal(out + f"the heading at line {line}, '{mine[1]}', is not in the template")
            raise Refusal(out + f"the heading at line {line} is '{'#' * mine[0]} {mine[1]}'; the "
                                f"template has '{'#' * theirs[0]} {theirs[1]}' there")
    mine_by: dict = {}
    for t in record.tables:
        mine_by.setdefault(t.under, []).append(t)
    for under, tables in mine_by.items():
        if under not in form.tables:
            where = "before the first heading" if under < 0 else f"under '{form.headings[under][1]}'"
            raise Refusal(out + f"the table at line {tables[0].line} stands {where}, where the "
                                "template has none")
    for under, tpl_tables in form.tables.items():
        tables = mine_by.get(under, [])
        name = form.headings[under][1] if under >= 0 else "the top"
        if under in (form.header_at, form.screen_at):
            if not tables:
                raise Refusal(out + f"there is no table under '{name}'")
            expected = [tpl_tables[0]] * len(tables)
        else:
            if len(tables) != len(tpl_tables):
                raise Refusal(out + f"under '{name}' the record has {len(tables)} table(s); the "
                                    f"template has {len(tpl_tables)}")
            expected = tpl_tables
        for rec, tpl in zip(tables, expected):
            departure = _same_table(rec, tpl)
            if departure:
                raise Refusal(out + departure)
    headers, screens = mine_by[form.header_at], mine_by[form.screen_at]
    if len(headers) != len(screens):
        raise Refusal(out + f"the record header is written {len(headers)} time(s) and 'For each "
                            f"screen' {len(screens)} time(s); both are written once for each screen")
    return headers, screens, mine_by[form.set_at][0]


def line_index(table: Table, words: str, *, exact: bool = False) -> int:
    for n, row in enumerate(table.rows):
        first = norm(row[0])
        if (first == words) if exact else (words in first.lower()):
            return n
    raise CannotRun(f"the template carries no line '{words}'; this program must be brought to "
                    "the template")


# ------------------------------------------------------------------------ what the record says

@dataclass
class Value:
    id: str
    name: str
    origin: str
    demand: str = ""
    rules: list = field(default_factory=list)       # (rule id, what the record says there)


@dataclass
class Act:
    words: str
    scope: str | None               # the variation of this screen the act belongs to, or None
    screen: str | None = None       # the target screen
    variation: str | None = None    # the variation of the target screen
    ending: str | None = None       # the ending's words, "ends in success"


@dataclass
class Screen:
    position: int
    id: str
    name: str
    header: list                    # (line, answer) of the record header, in the template's order
    lines: list                     # (line, answer) of "For each screen", in the template's order
    status: str
    version: str
    use_cases: str
    serves: list
    variations: dict = field(default_factory=dict)  # id -> ("of" | "own", what it carries)
    values: list = field(default_factory=list)
    rules: list = field(default_factory=list)       # the rules cited at the screen, not at a value
    acts: list = field(default_factory=list)


@dataclass
class Record:
    path: pathlib.Path
    id: str
    version: str
    status: str
    edition: str
    screens: list
    set_lines: list                 # (line, answer) of "For the set as a whole"
    notation: str
    commitment: str
    produced: str
    keys: dict = field(default_factory=dict)        # the line of "For each screen" each key names


def entries(answer: str) -> list[str]:
    """The entries of one Answer cell: none when it begins with 'None'."""
    text = answer.strip()
    if not text or re.match(r"^none\b", text, re.I):
        return []
    return [e.strip() for e in _BR.split(text) if e.strip()]


def leading_id(entry: str, what: str, sid: str) -> tuple[str, str]:
    m = _LEADING_ID.match(entry)
    if not m:
        raise Refusal(f"`{sid}`, {what}: the entry '{entry}' does not begin with an identifier "
                      "written between backticks")
    return m.group(1).strip(), m.group(2).strip()


def serves_of(use_cases: str) -> list[str]:
    """'`UC-X` name, version 1.0: steps 2 and 3; variations 2b and 4a' -> ['UC-X#2', …]."""
    out: list[str] = []
    for entry in _BR.split(use_cases):
        m = re.search(r"`([^`]+)`", entry)
        if not m or ":" not in entry[m.end():]:
            continue
        uc = m.group(1).strip()
        for clause in entry[m.end():].split(":", 1)[1].split(";"):
            c = clause.strip().lower()
            if c.startswith("step"):
                for a, b in re.findall(r"\b(\d+)\s+to\s+(\d+)\b", c):
                    out += [f"{uc}#{n}" for n in range(int(a), int(b) + 1)]
                c = re.sub(r"\b\d+\s+to\s+\d+\b", " ", c)
                out += [f"{uc}#{n}" for n in re.findall(r"\b(\d+)\b", c)]
            elif c.startswith("variation"):
                out += [f"{uc}#{v}" for v in re.findall(r"(\d+[a-z]+|\*[a-z]+)\b", c)]
    return list(dict.fromkeys(out))


def status_and_version(answer: str) -> tuple[str | None, str | None]:
    v = re.search(r"\bversion\s+([0-9]+(?:\.[0-9]+)*)\b", answer, re.I)
    s = [w for w in STATUSES if re.search(rf"\b{w}\b", answer, re.I)]
    return (s[0] if len(s) == 1 else None), (v.group(1) if v else None)


def parse_act(entry: str, sid: str) -> Act:
    scope = None
    m = re.match(r"^in\s+`([^`]+)`\s*:\s*(.*)$", entry, re.I | re.S)
    if m:
        scope, entry = m.group(1).strip(), m.group(2).strip()
    parts = re.split(r"\s*(?:→|->)\s*", entry, maxsplit=1)
    if len(parts) != 2 or not parts[0].strip() or not parts[1].strip():
        raise Refusal(f"`{sid}`, the acts: '{entry}' is not written as '<the act> → <target>'")
    words, target = parts[0].strip(), parts[1].strip().rstrip(".").strip()
    act = Act(words, scope)
    if (m := re.match(r"^the use case (ends\b.*)$", target, re.I)):
        act.ending = norm(m.group(1)).lower()
    elif (m := re.match(r"^raises\s+`([^`]+)`$", target, re.I)):
        act.screen, act.variation = sid, m.group(1).strip()
    elif (m := re.match(r"^`([^`]+)`(?:\s+with\s+`([^`]+)`)?$", target)):
        act.screen = m.group(1).strip()
        act.variation = m.group(2).strip() if m.group(2) else None
    else:
        raise Refusal(f"`{sid}`, the act '{words}': the target '{target}' is none of '`screen`', "
                      "'`screen` with `variation`', 'raises `variation`' or 'the use case ends …'")
    return act


def read_record(path: pathlib.Path, form: Form) -> Record:
    try:
        doc = parse(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError) as exc:
        raise CannotRun(f"cannot read {path}: {exc}")
    header_tables, screen_tables, set_table = check_form(doc, form)
    def answers(table: Table) -> list:
        a = answer_of(table)
        return [(norm(row[0]), row[a].strip()) for row in table.rows]

    tpl_header = form.tables[form.header_at][0]
    tpl_screen = form.tables[form.screen_at][0]
    tpl_set = form.tables[form.set_at][0]
    h = {name: line_index(tpl_header, name, exact=True) for name in HEADER_LINES}
    p = {key: line_index(tpl_screen, words) for key, words in PER_SCREEN.items()}
    s = {key: line_index(tpl_set, words) for key, words in PER_SET.items()}
    ah, ap = answer_of(tpl_header), answer_of(tpl_screen)

    # The version and the status first: a record that states no version is refused as such.
    states = [status_and_version(t.rows[h["Status and version"]][ah]) for t in header_tables]
    versions = {v for _s, v in states if v}
    if not versions:
        raise Refusal("the record states no version: no screen's 'Status and version' names one "
                      "(write, for example, 'Draft, version 0.1')")
    for n, (st, v) in enumerate(states, start=1):
        if not v:
            raise Refusal(f"the record states no version for its screen {n}: its 'Status and "
                          "version' names none")
        if not st:
            raise Refusal(f"screen {n}: its 'Status and version' does not name exactly one of "
                          "draft, reviewed or baselined")
    if len(versions) != 1 or len({st for st, _v in states}) != 1:
        raise Refusal("the screens state different statuses or versions "
                      f"({sorted({f'{st} {v}' for st, v in states})}); the set is versioned as a "
                      "whole, and every page carries the one version of the record")
    status, version = states[0]

    screens: list[Screen] = []
    for n, (ht, st) in enumerate(zip(header_tables, screen_tables)):
        ident = re.search(r"`([^`]+)`", ht.rows[h["Identifier"]][ah])
        if not ident:
            raise Refusal(f"screen {n + 1}: its identifier is not written between backticks")
        sid = ident.group(1).strip()
        first = re.search(r"`([^`]+)`", st.rows[p["first"]][ap])
        if first and first.group(1).strip() != sid:
            raise Refusal(f"the table 'For each screen' at line {st.line} names `{first.group(1)}`, "
                          f"but the record header in the same position is `{sid}`")
        use_cases = ht.rows[h["Use cases"]][ah].strip()
        screen = Screen(n, sid, ht.rows[h["Name"]][ah].strip(), answers(ht), answers(st),
                        status, version, use_cases, serves_of(use_cases))
        for entry in entries(st.rows[p["variation"]][ap]):
            vid, said = leading_id(entry, "for a variation", sid)
            kind = ("own" if re.search(r"screen of its own", said, re.I)
                    else "of" if re.search(r"variation of", said, re.I) else None)
            if kind is None:
                raise Refusal(f"`{sid}`, variation `{vid}`: the record does not say whether it is a "
                              "variation of a screen already in the set or a screen of its own")
            if vid in screen.variations:
                raise Refusal(f"`{sid}` records variation `{vid}` twice")
            screen.variations[vid] = (kind, said)
        by_id: dict = {}
        for entry in entries(st.rows[p["origin"]][ap]):
            vid, rest = leading_id(entry, "where a value came from", sid)
            if " — " not in rest:
                raise Refusal(f"`{sid}`, value `{vid}`: the entry does not separate the value's "
                              "name from where it came from by ' — '")
            name, origin = rest.split(" — ", 1)
            if vid in by_id:
                raise Refusal(f"`{sid}` records value `{vid}` twice")
            by_id[vid] = Value(vid, name.strip(), origin.strip())
        for entry in entries(st.rows[p["demand"]][ap]):
            vid, rest = leading_id(entry, "what the screen demands", sid)
            if vid not in by_id:
                raise Refusal(f"`{sid}`: what the screen demands names `{vid}`, which is not a "
                              "value this screen records where it came from")
            if by_id[vid].demand:
                raise Refusal(f"`{sid}` states twice what it demands of `{vid}`")
            by_id[vid].demand = rest
        for v in by_id.values():
            if not v.demand:
                raise Refusal(f"`{sid}`, value `{v.id}`: the record does not state the least the "
                              "screen demands of it and the most it admits")
        for entry in entries(st.rows[p["rules"]][ap]):
            rid, rest = leading_id(entry, "a rule cited", sid)
            named = [t for t in re.findall(r"`([^`]+)`", rest) if t in by_id]
            for vid in dict.fromkeys(named):
                by_id[vid].rules.append((rid, rest))
            if not named:
                screen.rules.append((rid, rest))
        screen.values = list(by_id.values())
        screen.acts = [parse_act(e, sid) for e in entries(st.rows[p["acts"]][ap])]
        screens.append(screen)

    ids = [sc.id for sc in screens]
    if len(set(ids)) != len(ids):
        raise Refusal(f"two screens share an identifier: {sorted(i for i in ids if ids.count(i) > 1)}")
    set_lines = answers(set_table)
    return Record(path, path.stem, version, status, doc.head.get("edition", ""), screens,
                  set_lines, set_lines[s["notation"]][1], set_lines[s["commitment"]][1],
                  set_lines[s["produced"]][1], dict(p))


# ------------------------------------------------------------------ the states, and where they lead

def slug(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9._]+", "-", s).strip("-") or "x"


def page_of(state) -> str:
    kind, a, b = state
    if kind == "ending":
        return "ending-" + slug(re.sub(r"^ends\s*", "", a)) + ".html"
    return f"screen-{slug(a)}.html" if b is None else f"screen-{slug(a)}--{slug(b)}.html"


def states_of(record: Record) -> tuple[list, dict]:
    """Every state a person can be in — a screen, a screen with one of its variations, an
    ending — and the acts that leave each. Refuses an act that leads nowhere, a state no act
    reaches from the first screen, and a state from which no ending can be reached."""
    screens = {sc.id: sc for sc in record.screens}
    edges: dict = {}
    order: list = []
    for sc in record.screens:
        order.append(("screen", sc.id, None))
        order += [("screen", sc.id, v) for v, (k, _t) in sc.variations.items() if k == "of"]
    for sc in record.screens:
        if not [act for act in sc.acts if act.scope is None]:
            raise Refusal(f"`{sc.id}` leaves the person with no act: the record states no act that "
                          "takes them from it")
        for act in sc.acts:
            if act.scope is not None and sc.variations.get(act.scope, ("",))[0] != "of":
                raise Refusal(f"`{sc.id}`, the act '{act.words}' belongs to `{act.scope}`, which the "
                              "record does not carry as a variation of this screen")
            if act.ending:
                target = ("ending", act.ending, None)
            else:
                if act.screen not in screens:
                    raise Refusal(f"`{sc.id}`, the act '{act.words}' leads to `{act.screen}`, which is "
                                  "no screen of this record")
                if act.variation is not None and \
                        screens[act.screen].variations.get(act.variation, ("",))[0] != "of":
                    raise Refusal(f"`{sc.id}`, the act '{act.words}' raises `{act.variation}` on "
                                  f"`{act.screen}`, which that screen does not carry as a variation "
                                  "of itself")
                target = ("screen", act.screen, act.variation)
            edges.setdefault(("screen", sc.id, act.scope), []).append((act, target))
            if target[0] == "ending" and target not in order:
                order.append(target)
        for v, (k, _t) in sc.variations.items():
            if k == "of" and not edges.get(("screen", sc.id, v)):
                raise Refusal(f"`{sc.id}`, variation `{v}`: the record states no act the person may "
                              f"perform in it (write 'In `{v}`: <the act> → <target>' among the acts)")
    first = ("screen", record.screens[0].id, None)
    seen, todo = {first}, [first]
    while todo:
        for _act, target in edges.get(todo.pop(), []):
            if target not in seen:
                seen.add(target)
                todo.append(target)
    unreached = [st for st in order if st not in seen]
    if unreached:
        raise Refusal("no act reaches " + ", ".join(_said(st) for st in unreached) +
                      f" from the first screen, `{record.screens[0].id}`")
    ends = {st for st in order if st[0] == "ending"}
    reaches = set(ends)
    changed = True
    while changed:
        changed = False
        for st in order:
            if st not in reaches and any(t in reaches for _a, t in edges.get(st, [])):
                reaches.add(st)
                changed = True
    stuck = [st for st in order if st not in reaches]
    if stuck:
        raise Refusal("no ending can be reached from " + ", ".join(_said(st) for st in stuck))
    names = [page_of(st) for st in order] + ["index.html"]
    if len(set(names)) != len(names):
        raise Refusal(f"two states would be written to one page: {sorted(n for n in names if names.count(n) > 1)}")
    return order, edges


def _said(state) -> str:
    kind, a, b = state
    if kind == "ending":
        return f"the ending '{a}'"
    return f"`{a}`" if b is None else f"`{a}` with variation `{b}`"


# ------------------------------------------------------------------------------ the pages

# The drawing's choices, made once here for every set this program produces and recorded against
# no screen (SDD-07 section 8, "What the walk-through never carries"; rule 26). Every figure is a
# whole number, so that no figure of the drawing can be read as a record's version.
CSS = ("body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;"
       "margin:0;background:#f5f5f3;color:#1d1d1d;line-height:145%;font-size:16px}"
       "header,main,footer{max-width:920px;margin:0 auto;padding:10px 16px}"
       ".stamp{font-size:14px;background:#fff;border:1px solid #b9b9b9;padding:6px 10px}"
       "nav.pages a{margin-right:18px}"
       ".wireframe{background:#fff;border:2px dashed #8a8a8a;padding:16px;margin:16px 0}"
       ".screen-name{font-weight:600;margin:0 0 8px}"
       ".value{border-top:1px solid #dcdcdc;padding:8px 0}"
       ".value-name{display:block}"
       ".box{display:block;height:26px;border:1px solid #9a9a9a;background:#fafafa;margin:4px 0}"
       ".acts{margin-top:16px;display:flex;flex-wrap:wrap;gap:10px}"
       "a.act{display:inline-block;border:1px solid #333;padding:6px 12px;"
       "text-decoration:none;color:#1d1d1d;background:#ececec}"
       ".condition{display:block;font-size:13px;color:#3d3d3d}"
       ".variation{border-left:4px solid #555;background:#fff;padding:8px 12px;margin:16px 0}"
       "details{margin:8px 0}dt{font-weight:600}dd{margin:0 0 6px 16px}"
       "table{border-collapse:collapse;width:100%;background:#fff}"
       "td,th{border:1px solid #cfcfcf;padding:5px 6px;vertical-align:top;text-align:left}"
       "footer{font-size:14px;border-top:1px solid #b9b9b9;margin-top:24px}"
       "code{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:92%}")

PRODUCED = ("These pages are produced from the record by <code>kit screens walk</code> and are never "
            "edited by hand: a correction is made in the record, and the pages are produced again.")


def text_html(s: str) -> str:
    """Record text as HTML: escaped, identifiers between backticks as code, entries on lines."""
    out = []
    for part in _BR.split(s):
        e = html.escape(part.strip(), quote=False)
        out.append(re.sub(r"`([^`]+)`", r"<code>\1</code>", e))
    return "<br>".join(out)


def _page(record: Record, title: str, kind: str, tail: str, body: list, nav: list,
          serves: list = ()) -> str:
    attrs = (f'data-record="{html.escape(record.id)}" data-version="{html.escape(record.version)}" '
             f'data-status="{html.escape(record.status)}"')
    stamp = (f'<p class="stamp" {attrs}>The screen record <code>{html.escape(record.id)}</code>, '
             f"version {html.escape(record.version)}, {html.escape(record.status)} · {tail}</p>")
    return "\n".join([
        "<!doctype html>", '<html lang="en">', "<head>", '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">', GENERATOR_META,
        f'<meta name="walk-page" content="{kind}">',
        f'<meta name="walk-serves" content="{html.escape(" ".join(serves))}">',
        f"<title>{html.escape(title)}</title>", f"<style>{CSS}</style>", "</head>", "<body>",
        "<header>", stamp, '<nav class="pages">' + " ".join(nav) + "</nav>", "</header>",
        "<main>", *body, "</main>", "<footer>",
        '<p class="commitment"><strong>What agreeing to this walk-through commits the parties '
        f"to.</strong> {text_html(record.commitment)}</p>",
        f"<details><summary>What this notation cannot say</summary><p>{text_html(record.notation)}"
        "</p></details>",
        f'<p class="produced">{PRODUCED}</p>', "</footer>", "</body>", "</html>", ""])


def _nav(record: Record, extra: list = ()) -> list:
    first = page_of(("screen", record.screens[0].id, None))
    return ['<a class="nav" href="index.html">The index</a>',
            f'<a class="nav" href="{first}">The first screen</a>', *extra]


def _act_link(act: Act, target) -> str:
    if target[0] == "ending":
        note = f"the use case {html.escape(target[1])}"
    elif target[2] is not None:
        note = (f"raises variation <code>{html.escape(target[2])}</code> on "
                f"<code>{html.escape(target[1])}</code>")
    else:
        note = f"to <code>{html.escape(target[1])}</code>"
    return (f'<a class="act" href="{page_of(target)}">{text_html(act.words)}'
            f'<span class="condition">{note}</span></a>')


def _record_table(rows: list) -> str:
    cells = "".join(f"<tr><td>{html.escape(line)}</td><td>{text_html(ans) if ans else '—'}</td></tr>"
                    for line, ans in rows)
    return f"<table><tr><th>Line</th><th>Answer</th></tr>{cells}</table>"


def _screen_body(record: Record, sc: Screen, variation: str | None, acts: list) -> list:
    head = f"<h1><code>{html.escape(sc.id)}</code> · {text_html(sc.name)}"
    body = [head + (f" — with its variation <code>{html.escape(variation)}</code></h1>"
                    if variation else "</h1>")]
    if variation:
        body.append(f'<div class="variation"><p><strong>Variation <code>{html.escape(variation)}'
                    f"</code>.</strong> {text_html(sc.variations[variation][1])}</p></div>")
    body.append('<section class="wireframe" aria-label="The screen">')
    body.append(f'<p class="screen-name">{text_html(sc.name)}</p>')
    if not sc.values:
        said = sc.lines[record.keys["origin"]][1]
        body.append(f'<p class="no-values">{text_html(said)}</p>')
    for v in sc.values:
        rules = "<br>".join(f"<code>{html.escape(r)}</code> {text_html(said)}" for r, said in v.rules)
        body += ['<div class="value">', f'<span class="value-name">{text_html(v.name)}</span>',
                 '<span class="box"></span>',
                 f"<details><summary>What the record says about <code>{html.escape(v.id)}</code>"
                 "</summary><dl>",
                 f"<dt>Where it came from</dt><dd>{text_html(v.origin)}</dd>",
                 f"<dt>What the person may do with it</dt><dd>{text_html(v.demand)}</dd>",
                 "<dt>The rules in force here</dt><dd>"
                 f"{rules or 'The record cites no rule at this value.'}</dd>",
                 "</dl></details>", "</div>"]
    body.append('<div class="acts">' + " ".join(_act_link(a, t) for a, t in acts) + "</div>")
    body.append("</section>")
    if sc.rules:
        said = "<br>".join(f"<code>{html.escape(r)}</code> {text_html(t)}" for r, t in sc.rules)
        body.append("<details><summary>The rules cited on this screen and not at one value"
                    f"</summary><p>{said}</p></details>")
    shown = [r for r in sc.header if r[0] != "Status and version"] + \
            [r for n, r in enumerate(sc.lines) if n != record.keys["status"]]
    body.append("<details><summary>The record of this screen (its status and version are in the "
                f"line at the head of the page)</summary>{_record_table(shown)}</details>")
    return body


def render(record: Record, order: list, edges: dict) -> dict:
    pages: dict = {}
    screens = {sc.id: sc for sc in record.screens}
    for state in order:
        kind, sid, var = state
        if kind == "ending":
            continue
        sc = screens[sid]
        acts = edges.get(state, [])
        if var is None:
            tail = f"screen <code>{html.escape(sid)}</code>, serving {text_html(sc.use_cases)}"
            pages[page_of(state)] = _page(record, f"{sid} · {norm(sc.name)}", "screen", tail,
                                          _screen_body(record, sc, None, acts), _nav(record),
                                          sc.serves)
        else:
            uc = sc.serves[0].split("#")[0] if sc.serves else ""
            tail = (f"screen <code>{html.escape(sid)}</code> with its variation "
                    f"<code>{html.escape(var)}</code>" +
                    (f", of <code>{html.escape(uc)}</code>" if uc else ""))
            leave = (f'<a class="nav leave" href="{page_of(("screen", sid, None))}">Leave the '
                     f"variation: back to <code>{html.escape(sid)}</code></a>")
            pages[page_of(state)] = _page(record, f"{sid} with {var}", "variation", tail,
                                          _screen_body(record, sc, var, acts),
                                          _nav(record, [leave]), [f"{uc}#{var}"] if uc else [])
    for state in order:
        if state[0] != "ending":
            continue
        froms = [f"<li>{_said_html(src)}: {text_html(act.words)}</li>"
                 for src, outs in edges.items() for act, t in outs if t == state]
        body = [f"<h1>The use case {html.escape(state[1])}</h1>",
                "<p>The record says that these acts end the use case here:</p>",
                "<ul>" + "".join(froms) + "</ul>"]
        pages[page_of(state)] = _page(record, f"The use case {state[1]}", "ending",
                                      f"the ending: the use case {html.escape(state[1])}", body,
                                      _nav(record))
    pages["index.html"] = _page(record, f"The screens of {record.id}", "index",
                                "the index of its screens", _index_body(record, order),
                                _nav(record))
    return pages


def _said_html(state) -> str:
    kind, a, b = state
    return (f"<code>{html.escape(a)}</code>" if b is None else
            f"<code>{html.escape(a)}</code> with its variation <code>{html.escape(b)}</code>")


def _index_body(record: Record, order: list) -> list:
    first = record.screens[0]
    body = [f"<h1>The screens of a use case — <code>{html.escape(record.id)}</code></h1>",
            f'<p><a class="nav start" href="{page_of(("screen", first.id, None))}">Start at the '
            f"first screen: <code>{html.escape(first.id)}</code> · {text_html(first.name)}</a></p>",
            "<h2>The screens, from their own record headers</h2>", "<ul>"]
    for sc in record.screens:
        variations = [st for st in order if st[0] == "screen" and st[1] == sc.id and st[2]]
        inner = "".join(f'<li><a class="nav" href="{page_of(st)}">with its variation '
                        f"<code>{html.escape(st[2])}</code></a></li>" for st in variations)
        body.append(f'<li><a class="nav" href="{page_of(("screen", sc.id, None))}"><code>'
                    f"{html.escape(sc.id)}</code> · {text_html(sc.name)}</a> — serving "
                    f"{text_html(sc.use_cases)}" + (f"<ul>{inner}</ul>" if inner else "") + "</li>")
    body.append("</ul>")
    body.append("<h2>Where the walk-through ends</h2><ul>" +
                "".join(f'<li><a class="nav" href="{page_of(st)}">The use case '
                        f"{html.escape(st[1])}</a></li>" for st in order if st[0] == "ending") +
                "</ul>")
    body.append("<h2>The set as a whole</h2>")
    body.append(_record_table(record.set_lines))
    return body


# ------------------------------------------------------------------ the program's own check

def check_pages(pages: dict, record: Record) -> list[str]:
    """Before anything is written: every page stamped once with the record's version, nothing
    fetched from anywhere, every link to a page of the set, every value shown with its three parts."""
    problems = []
    for name, text in pages.items():
        stamps = [ln for ln in text.splitlines() if '<p class="stamp"' in ln]
        if len(stamps) != 1 or f'data-version="{html.escape(record.version)}"' not in stamps[0]:
            problems.append(f"{name}: not stamped exactly once with version {record.version}")
        if re.search(r"<(script|link|img|iframe|object|embed)\b|<[^>]+\bsrc\s*=|url\(", text, re.I):
            problems.append(f"{name}: refers to something outside the page")
        for href in re.findall(r'<a\b[^>]*\bhref="([^"]*)"', text):
            if href not in pages:
                problems.append(f"{name}: a link to '{href}', which is not a page of the set")
    for sc in record.screens:
        for state in [("screen", sc.id, None)] + [("screen", sc.id, v) for v, (k, _t)
                                                   in sc.variations.items() if k == "of"]:
            text = pages.get(page_of(state), "")
            if text.count("<dt>Where it came from</dt>") != len(sc.values):
                problems.append(f"{page_of(state)}: not every value shows where it came from")
    return problems


def prepare(out: pathlib.Path) -> list[pathlib.Path]:
    """The folder the pages go to: new, or holding only pages this program wrote before."""
    if out.exists() and not out.is_dir():
        raise CannotRun(f"{out} is not a folder")
    if not out.exists():
        return []
    old, foreign = [], []
    for p in sorted(out.iterdir()):
        if p.is_file() and p.suffix == ".html" and \
                GENERATOR_META in p.read_text(encoding="utf-8", errors="replace"):
            old.append(p)
        else:
            foreign.append(p)
    if foreign:
        raise CannotRun(f"{out} holds {len(foreign)} file(s) this program did not write, among "
                        f"them '{foreign[0].name}'; name another folder with --out")
    return old


def run(a) -> int:
    if not a.record.is_file():
        raise CannotRun(f"no such record: {a.record}")
    if not a.template.is_file():
        raise CannotRun(f"no such template: {a.template}")
    form = form_of(parse(a.template.read_text(encoding="utf-8")), a.template)
    record = read_record(a.record, form)
    order, edges = states_of(record)
    pages = render(record, order, edges)
    problems = check_pages(pages, record)
    if problems:
        print("screens walk: a defect of this program, found before any page was written:",
              *problems, sep="\n  ", file=sys.stderr)
        return 3
    out = a.out or a.record.parent / f"{a.record.stem}_walk-through"
    old = prepare(out)
    for p in old:
        p.unlink()
    out.mkdir(parents=True, exist_ok=True)
    for name in sorted(pages):
        (out / name).write_text(pages[name], encoding="utf-8", newline="\n")

    kinds = {k: sum(1 for t in pages.values() if f'<meta name="walk-page" content="{k}">' in t)
             for k in ("index", "screen", "variation", "ending")}
    acts = sum(len(v) for v in edges.values())
    values = sum(len(sc.values) for sc in record.screens)
    digest = hashlib.sha256(a.record.read_bytes()).hexdigest()
    print(f"screens walk: {len(pages)} pages written to {out}: {kinds['index']} index, "
          f"{kinds['screen']} screens, {kinds['variation']} variations carried on a screen, "
          f"{kinds['ending']} endings")
    print(f"the record {record.id}, version {record.version}, {record.status}; written to "
          f"{form.standard} edition {record.edition or '(none named)'}, read against the kit's "
          f"template of edition {form.edition or '(none named)'}")
    print("the walk-through rules of SDD-07, one line each:")
    print(f"  23 · produced from {a.record.name} (SHA-256 {digest[:16]}…) by this program; no page "
          "is written by hand, and a correction is made in the record and the pages produced again")
    print(f"  24 · {len(record.screens)} screens, {len(record.screens)} screen pages; {acts} acts, "
          "each a link to a page of the set; no script and nothing fetched from outside the folder")
    print(f"  25 · {values} values, each shown with where it came from, what the person may do with "
          "it and the rules in force at it, on the page of its screen and of every variation of that "
          "screen, without leaving it; nothing calculated, nothing stored")
    print("  26 · no property of the record is read by the walk-through alone: the drawing's sizes, "
          "weights and colours are this program's, the same for every set")
    print(f"  27 · every page carries the notation's limits, the statement of what agreeing commits "
          f"the parties to, and the record's identifier, version and status ({len(pages)} of "
          f"{len(pages)})")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="kit screens walk", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("record", type=pathlib.Path, help="the screen record, a filled copy of the template")
    ap.add_argument("--out", type=pathlib.Path,
                    help="the folder the pages go to (default: <record>_walk-through beside it)")
    ap.add_argument("--template", type=pathlib.Path, default=TEMPLATE,
                    help="the template the record is read against (default: the kit's)")
    a = ap.parse_args(argv)
    try:
        return run(a)
    except Refusal as exc:
        print(f"screens walk: refused — {exc}", file=sys.stderr)
        return 1
    except CannotRun as exc:
        print(f"screens walk: could not run — {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
