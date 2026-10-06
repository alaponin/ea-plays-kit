#!/usr/bin/env python3
"""four_lists — the screens of one use case set beside the four lists of that use case (SDD-07 §7).

    python3 four_lists.py <screen record> <use case> [--kit-root D]

WHAT IT COMPARES. The four lists are read from the use case, and never from the screens: its
numbered steps, its variations, the entities it reads and the entities it changes, and the
requirements it realises. Each item of each list is set beside the record headers of the screens
that serve this use case, and is found in one of three states:

    reached     a screen names it — the screens that do are printed beside it
    no screen   no screen names it, and the set writes a reason for it — the reason is printed
    UNMATCHED   no screen names it, and the set writes no reason for it

It then reads the other direction: every step, variation, entity and requirement a screen names
that the use case's lists do not hold, every entity a screen changes that the use case declares
it only reads, every reason the set writes for an item the use case does not have, and every
screen that serves no step and no variation of any use case. Each of these is UNMATCHED.

WHAT IT DOES NOT DO. It prints no figure: no count of items and no proportion. It does not make
the reading against the stakeholders' interests, which a person makes and the set records. It
does not judge whether a reason is true, whether two steps may share a screen, or whether a
variation is placed on the right screen; those are the review's.

WHERE IT READS THE USE CASE — a filled copy of the kit's template of row 06:
  - its identifier: the record header's line 'Unique identifier';
  - the entities: the record header's line 'Entities read or changed', written
    'Reads: Member, Copy. Changes: Loan.' — names separated by commas, 'none' for none;
  - the requirements: the record header's line 'Requirements realised', every identifier in it;
  - the steps: the numbered lines ('1. …') under a heading that names the main success
    scenario, where the use case sets them out below its table; otherwise the numbered entries of
    the field 'Main success scenario' itself, separated by <br>;
  - the variations: the first column of the table under a heading that names the extensions;
    otherwise the entries of the field 'Extensions' itself, each beginning with its reference
    (2a, 4b, *a); an answer beginning 'None' has none.

WHERE IT READS THE SCREENS — a filled copy of the kit's template of row 07, read by the kit's own
reader of that record, tools/screens_walk.py, so that the record has one grammar:
  - each screen's identifier, and its record header's lines 'Use cases' (the steps and variations
    it serves of each use case, in the grammar `kit screens walk --help` documents), 'Entities'
    (written 'Shown: A, B. Changed: C.') and 'Requirements realised';
  - the written reasons, in the lines of 'For the set as a whole' that the template gives each
    list: steps and variations in the line beginning 'How many steps and variations', entities in
    the line beginning 'The two lists of entities', requirements in the line beginning 'The
    requirements, and what reaches each'. A reason is one entry of its line, entries separated by
    <br>, written in one of four forms:

        No screen for step 3: <the reason>
        No screen for variation 2b: <the reason>
        No screen for entity Copy: <the reason>
        No screen for requirement `F-2`: <the reason>

    A reason written in another line is not read.

EXIT. 0 nothing is unmatched; 1 something is unmatched, and every such item is printed; 2 the
program could not run — a file missing, the kit's reader not found, a record outside the
template's form, a use case from which a list cannot be read, or a record in which no screen
serves the use case. It writes nothing.
"""
from __future__ import annotations

import sys

sys.dont_write_bytecode = True                   # no byte-code beside the kit's reader, ever

import argparse                                  # noqa: E402
import datetime                                  # noqa: E402
import hashlib                                   # noqa: E402
import pathlib                                   # noqa: E402
import re                                        # noqa: E402

# sdd-kit: the kit stands three folders up from this file, at the plugin's root.
KIT_ROOT = pathlib.Path(__file__).resolve().parents[3] / "kit"
BR = re.compile(r"<br\s*/?>", re.I)
STEP_LINE = re.compile(r"^\s*(\d+)[.)]\s+\S")
VAR_ID = re.compile(r"^\s*`?\\?(\*|\d+)([a-z]+)`?(?=[\s.:,;)]|$)")
REQ_ID = re.compile(r"\b[A-Z][A-Za-z0-9]*(?:[-_.][A-Za-z0-9]+)+\b")
REASON = re.compile(r"^\s*no screen for (step|variation|entity|requirement)\s+`?([^`:]+?)`?\s*:\s*(\S.*)$",
                    re.I | re.S)
SET_LINES = {"steps and variations": "how many steps and variations",
             "entities": "the two lists of entities",
             "requirements": "the requirements, and what reaches each"}
KIND_LINE = {"step": "steps and variations", "variation": "steps and variations",
             "entity": "entities", "requirement": "requirements"}


class CannotRun(Exception):
    pass


def now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def plain(s: str) -> str:
    return " ".join(s.replace("`", "").replace("\\", "").split())


def key(name: str) -> str:
    return plain(name).lower().rstrip(".")


def req_ids(text: str) -> list[str]:
    return list(dict.fromkeys(m for m in REQ_ID.findall(plain(text)) if re.search(r"\d", m)))


def names(fragment: str) -> list[str]:
    out = []
    for part in re.split(r"[,;]", plain(fragment)):
        n = part.strip().rstrip(".").strip()
        if n and n.lower() not in ("none", "nothing", "no entity", "none of them"):
            out.append(n)
    return out


def entity_lists(text: str, read_words: str, change_words: str, where: str) -> tuple[list, list]:
    """'Reads: A, B. Changes: C.' -> (['A', 'B'], ['C'])."""
    t = plain(BR.sub(" ", text))
    rd = re.search(rf"\b(?:{read_words})\s*:\s*(.*?)(?=\b(?:{change_words})\s*:|$)", t, re.I | re.S)
    ch = re.search(rf"\b(?:{change_words})\s*:\s*(.*?)(?=\b(?:{read_words})\s*:|$)", t, re.I | re.S)
    if not rd and not ch:
        if not t or t.lower().startswith("none"):
            return [], []
        raise CannotRun(f"{where}: '{t}' names no list the program can read "
                        f"(write '{read_words.split('|')[0].capitalize()}: …' and "
                        f"'{change_words.split('|')[0].capitalize()}: …')")
    return (names(rd.group(1)) if rd else []), (names(ch.group(1)) if ch else [])


def load_reader(kit_root: pathlib.Path):
    tools = kit_root / "tools"
    if not (tools / "screens_walk.py").is_file():
        raise CannotRun(f"the kit's reader of the screen record, {tools / 'screens_walk.py'}, is not there")
    sys.path.insert(0, str(tools))
    import screens_walk                           # noqa: E402  the kit's one reader of the record
    return screens_walk


# ------------------------------------------------------------------------------ the use case

def answer_table(sw, doc, first_line: str):
    """The table of the use case whose first column carries `first_line`, and its Answer column."""
    for t in doc.tables:
        header = [sw.norm(c) for c in t.header]
        if "Answer" in header and any(sw.norm(r[0]).lower() == first_line.lower() for r in t.rows if r):
            return t, header.index("Answer")
    return None, None


def field(sw, table, col, words: str) -> str:
    for r in table.rows:
        if r and sw.norm(r[0]).lower() == words.lower():
            return r[col].strip() if col < len(r) else ""
    raise CannotRun(f"the use case carries no line '{words}'")


def lines_under(text_lines: list[str], doc, test) -> list[str] | None:
    """The lines under the first heading `test` accepts, up to the next heading; None if none."""
    hs = doc.headings
    for n, (_lvl, htext, line) in enumerate(hs):
        if test(htext.lower()):
            end = hs[n + 1][2] - 1 if n + 1 < len(hs) else len(text_lines)
            return text_lines[line:end]
    return None


def read_use_case(sw, path: pathlib.Path) -> dict:
    text = path.read_text(encoding="utf-8")
    doc = sw.parse(text)
    head, hc = answer_table(sw, doc, "Unique identifier")
    if head is None:
        raise CannotRun(f"{path.name}: no record header with the line 'Unique identifier' and a column "
                        "headed Answer — is it a filled copy of the kit's template of row 06?")
    ident = REQ_ID.search(plain(field(sw, head, hc, "Unique identifier")))
    if not ident:
        raise CannotRun(f"{path.name}: the line 'Unique identifier' carries no identifier")
    reads, changes = entity_lists(field(sw, head, hc, "Entities read or changed"), "reads|read",
                                  "changes|changed", f"{path.name}, 'Entities read or changed'")
    reqs = req_ids(field(sw, head, hc, "Requirements realised"))

    narr, nc = answer_table(sw, doc, "Main success scenario")
    if narr is None:
        raise CannotRun(f"{path.name}: no table with the field 'Main success scenario'")
    lines = text.splitlines()

    below = lines_under(lines, doc, lambda h: "main success scenario" in h)
    steps = [m.group(1) for m in (STEP_LINE.match(l) for l in (below or [])) if m]
    if not steps:
        cell = field(sw, narr, nc, "Main success scenario")
        steps = [m.group(1) for m in (STEP_LINE.match(e) for e in BR.split(cell)) if m]
    if not steps:
        raise CannotRun(f"{path.name}: no numbered step can be read, neither under a heading naming the "
                        "main success scenario nor in the field itself")

    variations: list[str] = []
    ext_heading = [n for n, (_l, h, _ln) in enumerate(doc.headings) if "extension" in h.lower()]
    tables = [t for t in doc.tables if ext_heading and t.under == ext_heading[0]]
    if tables:
        t = tables[0]
        header = [sw.norm(c).lower() for c in t.header]
        col = header.index("ref") if "ref" in header else 0
        for r in t.rows:
            m = VAR_ID.match(r[col]) if col < len(r) else None
            if m:
                variations.append(m.group(1) + m.group(2))
    else:
        cell = field(sw, narr, nc, "Extensions")
        if cell and not plain(cell).lower().startswith("none"):
            for e in BR.split(cell):
                m = VAR_ID.match(plain(e))
                if m:
                    variations.append(m.group(1) + m.group(2))
            if not variations:
                raise CannotRun(f"{path.name}: the field 'Extensions' says '{plain(cell)[:80]}', and no "
                                "variation can be read from it or from a table under a heading naming "
                                "the extensions")
    return {"id": ident.group(0), "steps": list(dict.fromkeys(steps)),
            "variations": list(dict.fromkeys(variations)), "reads": reads, "changes": changes,
            "requirements": reqs}


# ------------------------------------------------------------------------------ the screens

def read_screens(sw, path: pathlib.Path, kit_root: pathlib.Path) -> dict:
    template = kit_root / "templates" / "spec" / "artefacts" / "07_screen_record.md"
    if not template.is_file():
        raise CannotRun(f"the kit's template of row 07, {template}, is not there")
    try:
        form = sw.form_of(sw.parse(template.read_text(encoding="utf-8")), template)
        headers, _screens, set_table = sw.check_form(sw.parse(path.read_text(encoding="utf-8")), form)
    except (sw.Refusal, sw.CannotRun) as exc:
        raise CannotRun(f"{path.name}: {exc}")
    tpl_h = form.tables[form.header_at][0]
    tpl_s = form.tables[form.set_at][0]
    ah, as_ = sw.answer_of(tpl_h), sw.answer_of(tpl_s)
    at = {w: sw.line_index(tpl_h, w, exact=True)
          for w in ("Identifier", "Use cases", "Entities", "Requirements realised")}
    screens = []
    for n, t in enumerate(headers, start=1):
        m = re.search(r"`([^`]+)`", t.rows[at["Identifier"]][ah])
        sid = m.group(1).strip() if m else f"screen {n}"
        shown, changed = entity_lists(t.rows[at["Entities"]][ah], "shown", "changed",
                                      f"{path.name}, `{sid}`, 'Entities'")
        screens.append({"id": sid, "serves": sw.serves_of(t.rows[at["Use cases"]][ah]),
                        "shown": shown, "changed": changed,
                        "requirements": req_ids(t.rows[at["Requirements realised"]][ah])})
    reasons: dict = {"step": {}, "variation": {}, "entity": {}, "requirement": {}}
    for line, words in SET_LINES.items():
        cell = set_table.rows[sw.line_index(tpl_s, words)][as_]
        for entry in BR.split(cell):
            m = REASON.match(entry.strip())
            if not m:
                continue
            kind = m.group(1).lower()
            if KIND_LINE[kind] != line:
                continue
            item = plain(m.group(2))
            item = key(item) if kind == "entity" else item.rstrip(".")
            reasons[kind][item] = plain(m.group(3))
    return {"screens": screens, "reasons": reasons}


# ------------------------------------------------------------------------------ the comparison

def compare(uc: dict, rec: dict) -> tuple[list, list]:
    """(the report's lines, the unmatched items)."""
    out, unmatched = [], []
    ucid = uc["id"]
    serving = []
    for s in rec["screens"]:
        mine = [x.split("#", 1)[1] for x in s["serves"] if x.split("#", 1)[0] == ucid]
        others = sorted({x.split("#", 1)[0] for x in s["serves"] if x.split("#", 1)[0] != ucid})
        s["steps"] = [x for x in mine if x.isdigit()]
        s["variations"] = [x for x in mine if not x.isdigit()]
        s["others"] = others
        if mine:
            serving.append(s)
    if not serving:
        raise CannotRun(f"no screen of the record names the use case {ucid} in its line 'Use cases'")
    rs = rec["reasons"]

    def verdict(label: str, item: str, reached: list, reason_key: str, kind: str, note: str = ""):
        reason = rs[kind].get(reason_key)
        if reached:
            extra = "; a reason is also written for it" if reason else ""
            out.append(f"  {label:<12} reached     {', '.join(reached)}{extra}")
        elif reason:
            out.append(f"  {label:<12} no screen   {reason}{note}")
        else:
            out.append(f"  {label:<12} UNMATCHED   reached by no screen, and the set writes no reason{note}")
            unmatched.append(f"{kind} {item}")

    out.append("THE STEPS OF THE MAIN PATH")
    for n in uc["steps"]:
        verdict(f"step {n}", n, [s["id"] for s in serving if n in s["steps"]], n, "step")
    out.append("THE VARIATIONS")
    if not uc["variations"]:
        out.append("  none in the use case")
    for v in uc["variations"]:
        verdict(f"variation {v}", v, [s["id"] for s in serving if v in s["variations"]], v, "variation")
    out.append("THE ENTITIES THE USE CASE READS")
    if not uc["reads"]:
        out.append("  none in the use case")
    for e in uc["reads"]:
        verdict(e, e, [s["id"] for s in serving
                       if key(e) in {key(x) for x in s["shown"] + s["changed"]}], key(e), "entity")
    out.append("THE ENTITIES THE USE CASE CHANGES")
    if not uc["changes"]:
        out.append("  none in the use case")
    for e in uc["changes"]:
        shown_on = [s["id"] for s in serving if key(e) in {key(x) for x in s["shown"]}]
        changed_on = [s["id"] for s in serving if key(e) in {key(x) for x in s["changed"]}]
        note = ""
        if not changed_on and rs["entity"].get(key(e)):
            note = " (a reason written for an entity the use case changes: SDD-07 §7 and rule 7 read " \
                   "differently here, and the person at the review decides)"
        elif not changed_on and shown_on:
            note = f" (shown on {', '.join(shown_on)}, changed on none)"
        verdict(e, e, changed_on, key(e), "entity", note)
    out.append("THE REQUIREMENTS THE USE CASE REALISES")
    if not uc["requirements"]:
        out.append("  none in the use case")
    for r in uc["requirements"]:
        verdict(r, r, [s["id"] for s in serving if r in s["requirements"]], r, "requirement")

    out.append("NAMED BY THE SCREENS, AND NOT IN THE USE CASE'S LISTS")
    other = []
    declared = {key(x) for x in uc["reads"] + uc["changes"]}
    for s in rec["screens"]:
        for n in s["steps"]:
            if n not in uc["steps"]:
                other.append(f"`{s['id']}` serves step {n}, which the use case does not number")
        for v in s["variations"]:
            if v not in uc["variations"]:
                other.append(f"`{s['id']}` serves variation {v}, which the use case does not have")
        for e in s["shown"] + s["changed"]:
            if key(e) not in declared:
                other.append(f"`{s['id']}` names the entity {e}, which the use case does not declare")
        for e in s["changed"]:
            if key(e) in declared and key(e) not in {key(x) for x in uc["changes"]}:
                other.append(f"`{s['id']}` changes the entity {e}, which the use case declares it "
                             "reads and not that it changes")
        for r in s["requirements"]:
            if r not in uc["requirements"]:
                other.append(f"`{s['id']}` names the requirement {r}, which the use case does not "
                             "declare it realises")
        if not s["serves"]:
            other.append(f"`{s['id']}` serves no step and no variation of any use case")
        elif s["others"] and not (s["steps"] or s["variations"]):
            out.append(f"  `{s['id']}` serves only {', '.join(s['others'])}; not compared here")
    for kind, items in rs.items():
        have = {"step": uc["steps"], "variation": uc["variations"],
                "entity": [key(x) for x in uc["reads"] + uc["changes"]],
                "requirement": uc["requirements"]}[kind]
        for item in items:
            if item not in have:
                other.append(f"a reason is written for {kind} {item}, which the use case does not have")
    for o in other:
        out.append(f"  UNMATCHED   {o}")
        unmatched.append(o)
    if not other:
        out.append("  none")
    out.append("THE READING AGAINST THE STAKEHOLDERS' INTERESTS")
    out.append("  a person's reading, recorded in the set's own line; this program does not make it")
    return out, unmatched


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="four_lists.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("record", type=pathlib.Path, help="the screen record: a filled copy of the kit's template of row 07")
    ap.add_argument("use_case", type=pathlib.Path, help="the use case: a filled copy of the kit's template of row 06")
    ap.add_argument("--kit-root", type=pathlib.Path, default=KIT_ROOT,
                    help=f"the delivery kit's root (default: {KIT_ROOT})")
    a = ap.parse_args(argv)
    try:
        for p in (a.record, a.use_case):
            if not p.is_file():
                raise CannotRun(f"no such file: {p}")
        sw = load_reader(a.kit_root)
    except CannotRun as exc:
        print(f"four lists: could not run — {exc}", file=sys.stderr)
        return 2
    try:
        uc = read_use_case(sw, a.use_case)
        rec = read_screens(sw, a.record, a.kit_root)
        lines, unmatched = compare(uc, rec)
    except (CannotRun, sw.Refusal, sw.CannotRun) as exc:
        print(f"four lists: could not run — {exc}", file=sys.stderr)
        return 2
    print(f"four lists at {now()}")
    print(f"  the screens   {a.record} (sha256 {sha(a.record)[:12]})")
    print(f"  the use case  {a.use_case} (sha256 {sha(a.use_case)[:12]}), {uc['id']}")
    print(f"  read by       {a.kit_root / 'tools' / 'screens_walk.py'}, the kit's reader of the record")
    for ln in lines:
        print(ln)
    if unmatched:
        print("unmatched:")
        for u in unmatched:
            print(f"  {u}")
        return 1
    print("unmatched: none")
    return 0


if __name__ == "__main__":
    sys.exit(main())
