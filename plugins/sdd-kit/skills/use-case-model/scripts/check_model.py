#!/usr/bin/env python3
"""check_model — the program's half of the use case model's review, line by line.

    python3 check_model.py <model file> [--legacy] [--checklist FILE] [--template FILE]
                           [--kit-root DIR] [--record FILE]

WHAT IT READS AT RUN TIME, AND HOLDS NOT. The lines of the review and their words are read from
the standard's checklist, `templates/spec/checklists/SDD-05.md` under the kit's root, which the
standard's build produces; the fields of the record header, and the closed sets of level, status
and format, from the kit's template of row 03 beside it. This program holds which part of each
line a program can decide, and how; nothing of what the lines say.

WHAT IT WRITES. One line for each line of the review, in the checklist's order:

    M16 · FINDING · <the checkpoint, as the checklist gives it>
          - UC-03 cites FR-X-9, which the named register of requirements does not carry

    PASS      the program's part found nothing, and the line has no part for a person
    FINDING   the program's part found something; every finding needs an owner
    OPEN      the program's part found nothing, or has none, and the person answers the line

then this skill's own heuristics under LOOK, each labelled as not a rule of the standard. A line
of the checklist this program has no part for is written OPEN and said to be so, so that a line
added to the standard is seen rather than skipped.

The verdicts of the claim are not written here: the person answers every rule in the verdicts
file, reading this output for the lines the program decided, and `kit conform 03` writes the
claim.

Exit: 0 no finding · 1 one finding or more · 2 could not run.
"""
from __future__ import annotations

import sys

sys.dont_write_bytecode = True                      # nothing compiled lands beside the skill

import argparse                                     # noqa: E402
import os                                           # noqa: E402
import pathlib                                      # noqa: E402
import re                                           # noqa: E402

import yaml                                         # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import extract as X                                 # noqa: E402

# sdd-kit: the kit stands three folders up from this file, at the plugin's root.
KIT_ROOT = pathlib.Path(os.environ.get("SDD_KIT_ROOT", str(pathlib.Path(__file__).resolve().parents[3] / "kit")))
CHECKLIST_REL = pathlib.Path("templates/spec/checklists/SDD-05.md")
TEMPLATE_REL = pathlib.Path("templates/spec/artefacts/03_use_case_model.md")

KINDS = ("primary", "supporting", "offstage")
BOUNDARY = ("organisation", "software")
TREATMENT = ("black-box", "white-box")
PICTURES = (".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tif", ".tiff", ".webp")
# The lines whose program part decides the whole line (no question is left for a person).
NO_PERSON_PART = {"M16", "M17", "M18"}


class CouldNotRun(Exception):
    pass


# --------------------------------------------------------------------------- the checklist

def norm_key(s: str) -> str:
    return re.sub(r"\s*[–—-]\s*", "–", X.plain(s))


def review_lines(checklist: pathlib.Path) -> tuple[dict, list[tuple[str, str]], list[str]]:
    text = checklist.read_text(encoding="utf-8")
    head = {}
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if m:
        head = yaml.safe_load(m.group(1)) or {}
    lines, rules = [], []
    for tab in X.tables(text.split("\n")):
        if tab and "checkpoint" in tab[0] and "rules" in tab[0]:
            for r in tab:
                if X.plain(r.get("rules", "")):
                    lines.append((norm_key(r["rules"]), X.plain(r.get("checkpoint", ""))))
        elif tab and "rule" in tab[0] and "program" in tab[0]:
            rules = [X.plain(r["rule"]) for r in tab if X.plain(r.get("rule", ""))]
    if not lines:
        raise CouldNotRun(f"the checklist {checklist} carries no review table (a table with the "
                          f"columns Rules and Checkpoint)")
    return head, lines, rules


def closed_set(what: str) -> list[str]:
    """'Summary, user goal or subfunction (section 2.3).' -> ['summary', 'user goal', 'subfunction']."""
    s = re.split(r"\s*[(;—]|\s+-\s+", what)[0]
    s = s.strip().rstrip(".")
    parts = re.split(r",\s*or\s+|,\s*|\s+or\s+", s)
    return [p.strip().lower() for p in parts if p.strip()]


def template_fields(template: pathlib.Path) -> dict:
    uc = X.read_use_case(template)
    out = {"names": uc["field_order"], "closed": {}}
    for name, f in uc["fields"].items():
        first = name.split()[0].lower()
        if first in ("level", "status") or f["rule"] == "M21":
            key = "format" if f["rule"] == "M21" else first
            out["closed"][key] = closed_set(f["what"])
    return out


# --------------------------------------------------------------------------- the heuristics (LOOK)

NOT_A_VERB = re.compile(
    r"^(the|a|an|management|administration|maintenance|handling|processing|creation|deletion|"
    r"configuration|generation|validation|calculation|reporting|monitoring|dashboard)\b", re.I)
NOUNISH = re.compile(r"^(screen|page|form|report|list|export|access|record|review|control|audit|"
                     r"register|schedule)\s+(of|for)\b", re.I)
CRUD = re.compile(r"^(create|read|update|delete|edit|add|remove|insert|get|set)\s+(a |an |the )?\w+$", re.I)
TRIVIAL = re.compile(r"^(log ?in|log ?out|sign ?in|sign ?out|authenticate|log on|enter \w+|select \w+|"
                     r"view \w+|search \w+)$", re.I)
UI = re.compile(r"\b(click|clicks|button|drop[- ]?down|checkbox|radio button|tick ?box|screen|dialog|"
                r"pop[- ]?up|menu|scroll|text box|widget|wizard|toolbar)\b", re.I)
TECH_CI = re.compile(r"\b(database|stored procedure|schema|primary key|foreign key|microservice|table row)\b", re.I)
TECH_CS = re.compile(r"\b(SQL|REST|JSON|XML|API|Kafka|Postgres|Oracle)\b")
VAGUE = re.compile(r"\b(normally|usually|typically|as needed|as appropriate|appropriately|if possible|"
                   r"where possible|quickly|in a timely manner|as required|where necessary|"
                   r"user[- ]friendly|efficiently|robust)\b", re.I)
VALUE = re.compile(r"(?<![\w-])\d+(?:\.\d+)?\s*(?:%|per cent|percentile|days?|months?|years?|hours?)?(?![\w-])")


# --------------------------------------------------------------------------- the gate

class Gate:
    def __init__(self, M: dict, tpl: dict):
        self.M, self.tpl = M, tpl
        self.found: dict[str, list[str]] = {}
        self.notes: dict[str, list[str]] = {}
        self.look: list[tuple[str, str]] = []
        self.ucs = M["use_cases"]
        self.by_id = {u["id"]: u for u in self.ucs if u["id"]}
        self.actor = {a["name"]: a for a in M["actors"]}
        self.legacy = M["shape"] == "legacy"

    def f(self, key, msg):
        self.found.setdefault(key, []).append(msg)

    def n(self, key, msg):
        self.notes.setdefault(key, []).append(msg)

    def lk(self, key, msg):
        self.look.append((key, msg))

    def named(self, key):
        return self.M["named"].get(key) or {"declared": None}

    def set_state(self, key, words, line):
        """Report a named set that is not there; return its entries when it is."""
        s = self.named(key)
        if "absent" in s:
            self.f(line, f"the model names {words} as absent ({s['absent']}); its owner: "
                         f"{s.get('owner') or 'NOT NAMED — the finding needs one'}")
            return None
        if "none" in s:
            return []
        if "inline" in s:
            return list(s.get("entries", []))
        if "path" in s:
            if not s.get("exists"):
                self.f(line, f"the model names {words} at {s['declared']}, which is not there")
                return None
            return list(s.get("entries", []))
        self.f(line, f"the model does not name {words}")
        return None

    # ---------------------------------------------------------------- the lines
    def l_M1_M3(self, k):
        M = self.M
        if not M["system"]:
            self.f(k, "the model names no system under discussion")
        if not M["inside"]:
            self.f(k, "the model says nothing of what is inside its boundary")
        if not M["outside"]:
            self.f(k, "the model says nothing of what is deliberately outside its boundary")
        if self.legacy:
            text = pathlib.Path(M["model_file"]).read_text(encoding="utf-8").lower()
            if not any(w in text for w in BOUNDARY):
                self.f(k, "the model does not say whether its boundary is the organisation or the software")
            if not any(w in text for w in TREATMENT):
                self.f(k, "the model does not say whether its treatment is black-box or white-box")
            return
        b = str(M["front"].get("boundary") or "").strip().lower()
        t = str(M["front"].get("treatment") or "").strip().lower()
        if b not in BOUNDARY:
            self.f(k, f"the model's head gives the boundary as {b or 'nothing'}, not one of {', '.join(BOUNDARY)}")
        if t not in TREATMENT:
            self.f(k, f"the model's head gives the treatment as {t or 'nothing'}, not one of {', '.join(TREATMENT)}")

    def l_M4_M6(self, k):
        if not self.M["actors"]:
            self.f(k, "the model's catalogue carries no actor")
        for a in self.M["actors"]:
            if a["kind"] not in KINDS:
                self.f(k, f"the actor {a['name']!r} has the kind {a['kind'] or 'nothing'}, not one of {', '.join(KINDS)}")
            if not self.legacy and a["person"] not in ("yes", "no"):
                self.f(k, f"the actor {a['name']!r} does not say whether it is a person")
        if self.M["actors"] and not any(a["person"] == "no" for a in self.M["actors"]):
            self.f(k, "no actor is a system, a device or a clock, and the model says nothing of it")

    def l_M7_M8(self, k):
        for u in self.ucs:
            nm = u["name"]
            if not nm:
                self.f(k, f"{u['id'] or u['file']} has no name")
                continue
            if NOT_A_VERB.match(nm):
                self.f(k, f"{u['id']} {nm!r} does not open on a verb")
            if NOUNISH.match(nm):
                self.lk(k, f"{u['id']} {nm!r} may be a noun phrase rather than a goal")
            a = u["actor"]
            if a:
                act = self.actor.get(a)
                if act is None:
                    self.f(k, f"{u['id']} names {a!r} as its primary actor, and the catalogue carries no such actor")
                elif act["kind"] and act["kind"] != "primary":
                    self.f(k, f"{u['id']} names {a!r} as its primary actor; the catalogue gives it as {act['kind']}")

    def l_M9(self, k):
        levels = self.tpl["closed"].get("level") or []
        single_sitting = levels[1] if len(levels) > 1 else "user goal"
        for u in self.ucs:
            if not u["level"]:
                self.f(k, f"{u['id']} states no level")
            elif levels and u["level"] not in levels:
                self.f(k, f"{u['id']} states the level {u['level']!r}, not one of {', '.join(levels)}")
            if TRIVIAL.match(u["name"] or "") and u["level"] == single_sitting:
                self.f(k, f"{u['id']} {u['name']!r} stands at the level of {u['level']}, and its name is "
                          f"one this skill reads as a step rather than a goal")

    def l_M10(self, k):
        for u in self.ucs:
            if CRUD.match(u["name"] or ""):
                self.lk(k, f"{u['id']} {u['name']!r} reads as an operation on one stored thing")
        self.n(k, "the program decides nothing on this line; its one heuristic is reported under LOOK")

    def l_M9_M11(self, k):
        levels = self.tpl["closed"].get("level") or ["summary", "user goal", "subfunction"]
        sub = levels[-1]
        included = {}
        for u in self.ucs:
            r = u["relationships"]
            for t in r.get("unread", []):
                self.f(k, f"{u['id']} states a relationship this program cannot read: {t!r}")
            for i in r["includes"]:
                included.setdefault(i, set()).add(u["id"])
                if i not in self.by_id:
                    self.f(k, f"{u['id']} includes {i}, which is not a use case of the model")
                elif not self.legacy and u["id"] not in self.by_id[i]["relationships"]["included_by"]:
                    self.f(k, f"{u['id']} includes {i}, and {i} does not say it is included by {u['id']}")
            for b in r["included_by"]:
                if b in self.by_id and not self.legacy and u["id"] not in self.by_id[b]["relationships"]["includes"]:
                    self.f(k, f"{u['id']} says it is included by {b}, and {b} does not include it")
                included.setdefault(u["id"], set()).add(b)
            for e in r["extends"]:
                if e["base"] not in self.by_id:
                    self.f(k, f"{u['id']} extends {e['base']}, which is not a use case of the model")
                elif not self.legacy and u["id"] not in self.by_id[e["base"]]["relationships"]["extended_by"]:
                    self.f(k, f"{u['id']} extends {e['base']}, and {e['base']} does not say it is extended by {u['id']}")
                if not self.legacy and not (e["point"] and e["when"]):
                    self.f(k, f"{u['id']} extends {e['base']} without naming the point and the condition")
            for x in r["extended_by"]:
                if x in self.by_id and not self.legacy and not any(
                        e["base"] == u["id"] for e in self.by_id[x]["relationships"]["extends"]):
                    self.f(k, f"{u['id']} says it is extended by {x}, and {x} does not extend it")
        for u in self.ucs:
            if u["level"] == sub and not included.get(u["id"]):
                self.f(k, f"{u['id']} is a {sub} that no use case includes")
        if not self.legacy:
            pairs_inc = {(i, u["id"]) for u in self.ucs for i in u["relationships"]["includes"]}
            pairs_ext = {(u["id"], e["base"]) for u in self.ucs for e in u["relationships"]["extends"]}
            for row in self.M["includes"]:
                for b in row["bases"]:
                    if (row["included"], b) not in pairs_inc:
                        self.f(k, f"the model file's table of included steps has {row['included']} included by {b}, which no header states")
            for row in self.M["extends"]:
                if (row["extension"], row["base"]) not in pairs_ext:
                    self.f(k, f"the model file's table of optional steps has {row['extension']} extending {row['base']}, which no header states")
            reg_inc = {(r["included"], b) for r in self.M["includes"] for b in r["bases"]}
            reg_ext = {(r["extension"], r["base"]) for r in self.M["extends"]}
            for p in sorted(pairs_inc - reg_inc):
                self.lk(k, f"{p[1]} includes {p[0]}, and the model file gives no reason it is written once")
            for p in sorted(pairs_ext - reg_ext):
                self.lk(k, f"{p[0]} extends {p[1]}, and the model file's table of optional steps does not carry it")
        n_rel = sum(len(u["relationships"]["includes"]) + len(u["relationships"]["extends"]) for u in self.ucs)
        if self.ucs and n_rel > 0.4 * len(self.ucs):
            self.lk(k, f"{n_rel} relationships against {len(self.ucs)} use cases (this skill's threshold, four in ten)")

    def l_M12_M13(self, k):
        codes = [p["code"] or p["name"] for p in self.M["packages"]]
        for c in {c for c in codes if codes.count(c) > 1}:
            self.f(k, f"two packages carry the code {c}")
        member = {}
        for p in self.M["packages"]:
            if not p["members"]:
                self.f(k, f"the package {p['name']!r} holds no use case")
            if self.legacy and p.get("stated_count"):
                stated = re.sub(r"\D", "", p["stated_count"])
                if stated and int(stated) != len(p["members"]):
                    self.f(k, f"the package {p['code']} states {stated} use cases; the survey lists {len(p['members'])}")
            for i in p["members"]:
                member.setdefault(i, []).append(p["code"] or p["name"])
                if i not in self.by_id:
                    self.f(k, f"the package {p['name']!r} lists {i}, which is not a use case of the model")
        for u in self.ucs:
            where = member.get(u["id"], [])
            if len(where) != 1:
                self.f(k, f"{u['id']} is in {len(where)} packages" + (f" ({', '.join(where)})" if where else ""))
        if not self.M["survey"]["exists"]:
            self.f(k, f"there is no survey at {self.M['survey']['path']}")
        statuses = self.tpl["closed"].get("status") or []
        for u in self.ucs:
            if not u["status"]:
                self.f(k, f"{u['id']} states no status")
            elif statuses and not self.legacy and u["status"] not in statuses:
                self.f(k, f"{u['id']} states the status {u['status']!r}, not one of {', '.join(statuses)}")
            if not u["priority"]:
                self.f(k, f"{u['id']} states no priority")

    def l_M14(self, k):
        for u in self.ucs:
            if not u["actor"]:
                self.f(k, f"{u['id']} names no primary actor")
            if not u["description"]:
                self.f(k, f"{u['id']} carries no one-line description, so it states no result")
        served = {u["actor"] for u in self.ucs}
        for a in self.M["actors"]:
            if a["kind"] == "primary" and a["name"] not in served:
                self.f(k, f"the primary actor {a['name']!r} is the primary actor of no use case")
        if self.legacy:
            self.n(k, "the one-file shape keeps no record of which supporting actor a goal calls on; "
                      "that part of the line is not decided")
            return
        called = {}
        for uid, acts in self.M["associations"].items():
            if uid not in self.by_id:
                self.f(k, f"the table of supporting actors names {uid}, which is not a use case of the model")
            for a in acts:
                called.setdefault(a, []).append(uid)
                act = self.actor.get(a)
                if act is None:
                    self.f(k, f"{uid} calls on {a!r}, which the catalogue does not carry")
                elif act["kind"] == "offstage":
                    self.f(k, f"{uid} calls on {a!r}, an offstage actor")
                elif act["kind"] != "supporting":
                    self.f(k, f"{uid} calls on {a!r}, which the catalogue gives as {act['kind']}")
        for a in self.M["actors"]:
            if a["kind"] == "supporting" and a["name"] not in called:
                self.f(k, f"the supporting actor {a['name']!r} is called by no use case")

    def l_M15(self, k):
        for u in self.ucs:
            if not u["requirements"]:
                self.f(k, f"{u['id']} carries no linked requirement, so no trace reaches it")
        self.n(k, "the links the model carries: the requirements each use case realises; it names no set of "
                  "screens, increment or test for any use case, which are recorded where they are written")

    def l_M16(self, k):
        entries = self.set_state("requirements", "the published register of requirements", k)
        for u in self.ucs:
            if not u["requirements"]:
                self.f(k, f"{u['id']} names no requirement by identifier")
        if entries is None:
            return
        have = set(entries)
        realised = set()
        for u in self.ucs:
            for r in u["requirements"]:
                realised.add(r)
                if r not in have:
                    self.f(k, f"{u['id']} cites {r}, which the named register of requirements does not carry")
        for e in entries:
            if e not in realised:
                self.f(k, f"the register's entry {e} is realised by no use case")

    def l_M17(self, k):
        entries = self.set_state("entity_model", "the entity model", k)
        named = [(u["id"], e) for u in self.ucs for e in u["entities"]["reads"] + u["entities"]["changes"]]
        if self.legacy:
            self.n(k, "no row names its entities: the one-file shape carries no field for them")
        if entries is None:
            return
        have = {e.lower() for e in entries}
        for uid, e in named:
            if e.lower() not in have:
                self.f(k, f"{uid} names the entity {e!r}, which the named entity model does not carry")
            if re.search(r"[:(){}\[\]]|\.\w", e):
                self.lk(k, f"{uid} names {e!r}, which looks like a field structure rather than a name")

    def l_M22(self, k):
        terms = self.set_state("glossary", "a glossary beside the entity model", k)
        if terms is None:
            return
        ents = {e.lower() for e in (self.named("entity_model").get("entries") or [])}
        for t in terms:
            if t.lower() in ents:
                self.f(k, f"the term {t!r} is both in the glossary and in the entity model")

    def l_M18(self, k):
        rules = self.set_state("business_rules", "the register of business rules", k)
        if rules is None:
            return
        have = set(rules)
        cited = set()
        for u in self.ucs:
            for r in u["rules"]:
                cited.add(r)
                if r not in have:
                    self.f(k, f"{u['id']} cites {r}, which the named register of business rules does not carry")
        for r in rules:
            if r not in cited:
                self.n(k, f"the register's rule {r} is cited by no use case (reported, not a finding)")
        st = (self.named("business_rules").get("statements") or {})
        for r, s in st.items():
            for m in VALUE.finditer(s or ""):
                if not re.fullmatch(r"\d", m.group(0).strip()):
                    self.lk(k, f"the rule {r} states a value ({m.group(0).strip()!r}); a value belongs to a "
                               f"setting with a marked default (SDD-01 §14, rule 6)")

    def l_M21(self, k):
        formats = self.tpl["closed"].get("format") or []
        full = formats[-1] if formats else "written out in full"
        outline = formats[1] if len(formats) > 1 else "outline"
        seen_full = False
        for u in self.ucs:
            fmt = u["format"]
            if fmt == "casual":
                self.n(k, f"{u['id']} gives its format as 'casual', read here as {outline!r}: SDD-06 U1 "
                          f"names the middle form 'a casual form', and the two standards disagree")
                fmt = outline
            if not fmt:
                self.f(k, f"{u['id']} states no format")
            elif formats and fmt not in formats:
                self.f(k, f"{u['id']} states the format {fmt!r}, not one of {', '.join(formats)}")
            if fmt == full:
                seen_full = True
        said_none = any("none" in p.lower() and "written out" in p.lower() for p in self.M["format_decision"])
        if self.ucs and not seen_full and not said_none:
            self.f(k, "no use case is written out in full, and the model does not say that none is yet")
        if not self.M["format_decision"]:
            self.f(k, "the model records no decision of which use cases are written out and in what order")

    def l_M19_M20(self, k):
        M = self.M
        if self.legacy:
            self.f(k, "the model is one file; there is no file for each use case")
            self.f(k, "the survey is written by hand inside the model, not generated from record headers")
            head = "\n".join(pathlib.Path(M["model_file"]).read_text(encoding="utf-8").split("\n")[:60]).lower()
            if "version" not in head:
                self.f(k, "the model names no version of itself")
            return
        ucdir = pathlib.Path(M["use_case_dir"])
        if not ucdir.is_dir():
            self.f(k, f"there is no folder of use case files at {ucdir}")
        names = self.tpl["names"]
        for u in self.ucs:
            got = u["field_order"]
            missing = [x for x in names if x not in got]
            extra = [x for x in got if x not in names]
            if missing:
                self.f(k, f"{u['file']} lacks the header fields {', '.join(missing)}")
            if extra:
                self.f(k, f"{u['file']} carries header fields the template does not: {', '.join(extra)}")
            if u["id"] and pathlib.Path(u["file"]).stem != u["id"]:
                self.f(k, f"{u['file']} carries the identifier {u['id']}")
            if not u["id"]:
                self.f(k, f"{u['file']} carries no identifier")
        ids = [u["id"] for u in self.ucs if u["id"]]
        for i in {i for i in ids if ids.count(i) > 1}:
            self.f(k, f"the identifier {i} is carried by {ids.count(i)} files")
        want = X.survey_text(M)
        if M["survey"]["exists"] and M["survey"]["text"] != want:
            diff = [ln for ln in want.split("\n") if ln not in M["survey"]["text"].split("\n")]
            self.f(k, "the survey is not the one the record headers generate (run extract.py --write-survey); "
                      f"{len(diff)} generated line(s) differ" + (f", the first: {diff[0][:90]!r}" if diff else ""))
        base = pathlib.Path(M["model_file"]).parent
        pics = [p for p in base.rglob("*") if p.suffix.lower() in PICTURES and "_conformance" not in p.parts]
        for p in pics:
            self.f(k, f"{p.relative_to(base)} is a picture kept with the model; its diagrams are drawn from the headers")
        if not M["diagrams"]:
            self.f(k, "the model does not say where its diagrams come from")
        if not M["version"]:
            self.f(k, "the model names no version of itself")

    def run(self, key: str) -> bool:
        fn = getattr(self, "l_" + key.replace("–", "_"), None)
        if fn is None:
            return False
        fn(key)
        return True

    # ---------------------------------------------------------------- the heuristics of the descriptions
    def descriptions(self):
        for u in self.ucs:
            d = u["description"] or ""
            for pat, what in ((UI, "the mechanics of a screen"), (TECH_CI, "technology or internal design"),
                              (TECH_CS, "technology or internal design"), (VAGUE, "a qualifier hiding a decision")):
                for m in pat.finditer(d):
                    self.lk("P4", f"{u['id']}'s description names {what}: {m.group(0)!r}")
            for m in VALUE.finditer(d):
                if not re.fullmatch(r"\d", m.group(0).strip()):
                    self.lk("P4", f"{u['id']}'s description states a value ({m.group(0).strip()!r}); a value "
                                  f"belongs to a setting (SDD-01 §14, rule 6)")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="check_model.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("model", type=pathlib.Path)
    ap.add_argument("--legacy", action="store_true", help="read the one-file shape of the retired plugin")
    ap.add_argument("--checklist", type=pathlib.Path)
    ap.add_argument("--template", type=pathlib.Path)
    ap.add_argument("--kit-root", type=pathlib.Path, default=KIT_ROOT)
    ap.add_argument("--record", type=pathlib.Path, help="also write the output to this file")
    a = ap.parse_args(argv)
    out: list[str] = []

    def say(s=""):
        out.append(s)
        print(s)

    try:
        cl = a.checklist or (a.kit_root / CHECKLIST_REL)
        tp = a.template or (a.kit_root / TEMPLATE_REL)
        for p, what in ((a.model, "the model"), (cl, "the checklist"), (tp, "the template")):
            if not p.is_file():
                raise CouldNotRun(f"{what} {p} is not there")
        head, lines, rules = review_lines(cl)
        tpl = template_fields(tp)
        M = X.read_legacy(a.model) if a.legacy else X.read_model(a.model)
    except (CouldNotRun, X.CouldNotRun, yaml.YAMLError) as exc:
        print(f"check_model: could not run: {exc}", file=sys.stderr)
        return 2

    g = Gate(M, tpl)
    say(f"check_model {a.model}{' --legacy' if a.legacy else ''}")
    say(f"  standard   {head.get('standard', '?')} {head.get('edition', '?')} — {head.get('document', '?')} "
        f"(sha256 {str(head.get('sha256', '?'))[:12]}…), as the checklist's head names it")
    say(f"  checklist  {cl}: {len(lines)} lines of the review, {len(rules)} rules")
    say(f"  template   {tp}: {len(tpl['names'])} header fields")
    wt = (M["front"].get("written_to") or {}) if isinstance(M["front"].get("written_to"), dict) else {}
    if wt and (str(wt.get("edition")) != str(head.get("edition")) or str(wt.get("sha256")) != str(head.get("sha256"))):
        say(f"  NOTE       the model was prepared against edition {wt.get('edition')}; the checklist is of "
            f"{head.get('edition')} — the model is read against the checklist")
    say(f"  the model  {len(M['use_cases'])} use cases · {len(M['packages'])} packages · {len(M['actors'])} actors "
        f"· shape {M['shape']}")
    say("  what a named set must itself contain is its own standard's — SDD-02 for the register of requirements,")
    say("  SDD-03 for the entity model, its glossary and its register of business rules, SDD-04 for the")
    say("  catalogue of settings; this gate resolves identifiers in each and judges nothing of a set's own shape")
    say()
    tally = {"PASS": 0, "FINDING": 0, "OPEN": 0}
    known = set()
    for key, words in lines:
        ran = g.run(key)
        known.add(key)
        fnd = g.found.get(key, [])
        if fnd:
            verdict = "FINDING"
        elif not ran or key not in NO_PERSON_PART:
            verdict = "OPEN"
        else:
            verdict = "PASS"
        tally[verdict] += 1
        say(f"{key} · {verdict} · {words}")
        for m in fnd:
            say(f"      - {m}")
        for m in g.notes.get(key, []):
            say(f"      · {m}")
        if not ran:
            say("      · this program has no part for this line; the person answers all of it")
        elif verdict == "OPEN" and not fnd:
            say("      · the program's part found nothing; the person answers the line as the checklist states it")
        elif fnd and key not in NO_PERSON_PART:
            say("      · the person also answers the line as the checklist states it")
    expected = {m[2:].replace("_", "–") for m in dir(g) if m.startswith("l_")}
    for k in sorted(expected - known):
        say(f"NOTE · the checklist carries no line {k}; this program's part for it was not run")
    g.descriptions()
    if g.look:
        say()
        say(f"LOOK — {len(g.look)}, this skill's heuristics and not rules of SDD-05; a false alarm is left, never silenced by widening a pattern")
        for key, m in g.look:
            say(f"  [{key}] {m}")
    say()
    say(f"{len(lines)} lines: {tally['PASS']} pass, {tally['FINDING']} with findings, {tally['OPEN']} open for the person")
    if tally["FINDING"]:
        say(f"REFUSED: {tally['FINDING']} line(s) of the review carry findings; each needs an owner before the claim is made")
    else:
        say("the program's half passes; the person answers the open lines, then the verdicts file is written and kit conform 03 run")
    if a.record:
        a.record.parent.mkdir(parents=True, exist_ok=True)
        a.record.write_text("\n".join(out) + "\n", encoding="utf-8")
    return 1 if tally["FINDING"] else 0


if __name__ == "__main__":
    sys.exit(main())
