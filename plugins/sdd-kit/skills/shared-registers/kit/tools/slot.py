#!/usr/bin/env python3
"""slot — resolve the register of the method's things against the documents themselves.

    kit slot <n>                  print one resolved row
    kit slot --check              check every row and every handover the register holds

How many things and how many handovers there are is read from the register itself, from its
`counts:` entry, and from nowhere else: the register is the single place each of its facts
lives, and a new thing is a change to it and not to this program (METHOD-2026-09-25-12; the
design round's report, "Found, not fixed", item 7). The rows and the handovers are checked
against those counts, and the handovers against their numbering, one to the count.

Every cell of `templates/spec/slots.yaml` that names a document, an edition, a section, a
rule range, a path or a program is checked here against the standards root and the kit, so
that the register cannot quietly fall behind the documents it describes. Four cells are
derived rather than believed — the edition, the standing, the rule range and the one-line
`governs` rendering the scaffold prints — and a row whose typed value differs from the
document's is refused.

The two roots are arguments and no path of one machine is written into the register. The
project's constants file names them; `--standards-root` and `--kit-root` carry them here,
and `--outside-root` carries the folder that holds both, against which a citation to a
document outside either is resolved.

Three cells of each row point at what helps a person with the thing (METHOD-2026-09-28-10, the
target state's section 3). `preparation.template`, and each of `preparation.beside`, must name a
file of the kit that is a template of the thing itself and not the scaffold's readme for the
slot. `check.checklist` must name a checklist of the kit whose head names the row's standard, its
document, the edition that document states, and the SHA-256 checksum of the document standing in
the standards root — so that a standard rebuilt or replaced without its checklist being emitted
again is reported. `skill` must stand on every row, as `plugin:skill`, or reading absent with an
owner; and a named skill must exist, at `plugins/<plugin>/skills/<skill>/SKILL.md` under the
marketplace (or at `skills/<skill>/SKILL.md` under a plugin's own root), carry in its frontmatter the standard the row names and pin, in `written_against`, the
edition the row names (METHOD-2026-09-30-01, the third of the three new checks). The marketplace is
`--marketplace`, and by default the root of the plugin this kit stands in (sdd-kit). A
knowledge cell that reads absent carries its reason and its owner, as every other does, and is
counted with them.

Exit: 0 clean · 1 something to report · 2 could not run.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import pathlib
import re
import sys
import zipfile
from xml.etree import ElementTree as ET

import yaml

HERE = pathlib.Path(__file__).resolve().parent
KIT_ROOT = HERE.parent
PLUGIN_ROOT = KIT_ROOT.parent              # sdd-kit: the kit, the standards and the skills
SLOTS = KIT_ROOT / "templates" / "spec" / "slots.yaml"
# The scaffold's readme for a slot, which a template cell may not name (the target state, §3).
SLOT_README = "templates/spec/slot_README.md.tmpl"
# The six lines of a checklist's head, in the order the plan of the finish fixes (its §3.1).
CHECKLIST_HEAD = ("standard", "title", "edition", "document", "sha256", "produced_by")
SKILL_NAME = re.compile(r"^[a-z0-9][a-z0-9-]*:[a-z0-9][a-z0-9-]*$")

W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

# A citation names sections of a standard by code: "SDD-03 §1; EM-46 to EM-51". SDD-10 and
# SDD-11 were added with the interaction design's slot (METHOD-2026-09-25-12), and IXD with it.
CODE = re.compile(r"\b(SDD-0[1-9]|SDD-1[01]|UX-01|S2C-01)\b")
SECTION = re.compile(r"§\s*(\d+(?:\.\d+)*)")
RULE = re.compile(r"\b(RQR|EM|IOS|ARC|IXD)-(\d+)\b|\b([MU])(\d{1,2})\b")
RULE_TEXT = re.compile(r"\b(?:RQR|EM|IOS|ARC|IXD)-\d+\b")
FORMAT_VERSION = "2.1"                     # the register's own format: 2.1 carries `counts:`
# A heading of one of these documents: a number, then a short title that is not a sentence.
HEADING = re.compile(r"^[ \t]*(\d+(?:\.\d+)*)[.):]?[ \t]+(\S.*)$")
MD_HEADING = re.compile(r"^#{1,6}\s+(?:Annex\s+)?([A-Z0-9]+(?:\.\d+)*)[.\s]")


def now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def plugin_skill_md(market, plugin: str, name: str):
    """Where a skill named plugin:skill stands. Under a marketplace, at
    plugins/<plugin>/skills/<name>/SKILL.md; under a plugin's own root — sdd-kit, whose kit
    reads the skills beside it — at skills/<name>/SKILL.md when the plugin's manifest carries
    that name; in one skill's own folder, installed on its own with its copy of the kit, at
    ../<name>/SKILL.md, beside it. None when none of these applies."""
    import json
    if market is None:
        return None
    market = pathlib.Path(market)
    if (market / "plugins").is_dir():
        return market / "plugins" / plugin / "skills" / name / "SKILL.md"
    manifest = market / ".claude-plugin" / "plugin.json"
    if manifest.is_file():
        try:
            if json.loads(manifest.read_text(encoding="utf-8")).get("name") == plugin:
                return market / "skills" / name / "SKILL.md"
        except ValueError:
            return None
    if (market / "SKILL.md").is_file():
        return market.parent / name / "SKILL.md"
    return None


# --------------------------------------------------------------------------- the documents

def docx_text(path: pathlib.Path) -> str:
    """The readable text of a .docx, paragraphs and table rows in document order."""
    with zipfile.ZipFile(path) as z:
        root = ET.fromstring(z.read("word/document.xml"))
    body = root.find(W_NS + "body")
    out = []
    for child in body:
        tag = child.tag[len(W_NS):]
        if tag == "p":
            out.append(_runs(child))
        elif tag == "tbl":
            for tr in child.findall(W_NS + "tr"):
                out.append(" | ".join(" ".join(_runs(tc).split())
                                      for tc in tr.findall(W_NS + "tc")))
    return "\n".join(out)


def _runs(el) -> str:
    buf = []
    for node in el.iter():
        t = node.tag[len(W_NS):] if node.tag.startswith(W_NS) else node.tag
        if t == "t":
            buf.append(node.text or "")
        elif t == "tab":
            buf.append("\t")
        elif t in ("br", "cr"):
            buf.append("\n")
    return "".join(buf)


class Document:
    """One edition of record, read once and answered from."""

    def __init__(self, path: pathlib.Path):
        self.path = path
        self.text = (docx_text(path) if path.suffix.lower() == ".docx"
                     else path.read_text(encoding="utf-8"))
        self.sections = self._sections()
        self.rules = {m.group(0) for m in RULE_TEXT.finditer(self.text)}
        self.rules |= {m.group(0) for m in re.finditer(r"\b[MU]\d{1,2}\b", self.text)}

    def _sections(self) -> set[str]:
        out: set[str] = set()
        for line in self.text.splitlines():
            line = line.rstrip()
            if re.search(r"\t\d+$", line):      # a contents line, with its page number
                continue
            md = MD_HEADING.match(line)
            if md:
                out.add(md.group(1))
                continue
            m = HEADING.match(line)
            if not m:
                continue
            title = m.group(2).strip()
            if len(line) >= 90 or title.endswith(".") or not title[:1].isupper():
                continue                         # a numbered list item, not a heading
            out.add(m.group(1))
        # a subsection implies its parent
        for s in list(out):
            while "." in s:
                s = s.rsplit(".", 1)[0]
                out.add(s)
        return out

    # the three cells every standard states about itself
    def edition(self) -> str | None:
        m = re.search(r"Version and standing \|\s*Version\s+([0-9][0-9.]*)", self.text)
        return m.group(1) if m else None

    def standing(self) -> str | None:
        m = re.search(r"Version and standing \|([^\n]*)", self.text)
        if not m:
            return None
        # The standing is the document's own, stated in the line's first sentence ("Version 1.2
        # · 25 September 2026 · in force."). A later sentence may speak of another document's
        # standing — SDD-07 v1.2 and SDD-01 v3.3 say that SDD-11 "is a draft" — which is not
        # this document's (METHOD-2026-09-25-12).
        line = re.split(r"\.(?:\s|$)", m.group(1), maxsplit=1)[0].lower()
        if "draft for customer review" in line:
            return "draft for customer review"
        if "draft" in line:
            return "draft"
        if "in force" in line:
            return "in force"
        return None

    def rule_range(self) -> str | None:
        for line in self.text.splitlines():
            if not line.startswith("Rules |"):
                continue
            body = line[len("Rules |"):].strip()
            if body.lower().startswith("checkpoint"):
                continue                          # a review-table row, not the declaration
            return re.split(r"[,.](?:\s|$)", body)[0].strip().rstrip(".")
        return None


# --------------------------------------------------------------------------- the register

class Resolver:
    def __init__(self, spec, standards_root, kit_root, outside_root, marketplace=None):
        self.spec = spec
        self.marketplace = marketplace
        self.skills_read: list[str] = []
        self.standards_root = standards_root
        self.kit_root = kit_root
        self.outside_root = outside_root
        self.docs: dict[str, Document] = {}
        self.problems: list[str] = []
        self.absent: list[str] = []
        self.citations: list[tuple] = []
        self.by_code: dict[str, pathlib.Path] = {}
        for s in spec["slots"]:
            st = s.get("standard") or {}
            if "code" in st and "file" in st:
                self.by_code[st["code"]] = standards_root / st["file"]
        # every other code the register may cite, found by listing the standards root
        for code in ("SDD-01", "SDD-02", "SDD-03", "SDD-04", "SDD-05", "SDD-06",
                     "SDD-07", "SDD-08", "SDD-09", "SDD-10", "SDD-11", "UX-01", "S2C-01"):
            if code in self.by_code:
                continue
            found = self._find(code, ("UX-01_Enterprise_UX_Standard.md"
                                      if code == "UX-01" else None))
            if found:
                self.by_code[code] = found

    def _find(self, code, name):
        if name and (self.standards_root / name).exists():
            return self.standards_root / name
        hits = sorted(self.standards_root.glob(f"{code}_*"))
        hits = [h for h in hits if h.suffix.lower() in (".docx", ".md")]
        return hits[-1] if hits else None

    def doc(self, code: str) -> Document | None:
        if code in self.docs:
            return self.docs[code]
        path = self.by_code.get(code)
        if not path or not path.exists():
            return None
        self.docs[code] = Document(path)
        return self.docs[code]

    def bad(self, where: str, msg: str):
        self.problems.append(f"{where}: {msg}")

    # ---- citations

    def check_citation(self, where: str, citation: str, default_code: str | None):
        """Every section and rule a citation names must stand in the edition of record."""
        if not citation:
            return
        self._cite(where, citation, default_code)

    def _cite(self, where: str, citation: str, default_code: str | None):
        parts = re.split(r";", citation)
        for part in parts:
            codes = CODE.findall(part)
            code = codes[0] if codes else default_code
            if not code:
                continue
            d = self.doc(code)
            if d is None:
                self.bad(where, f"{code} names no document in the standards root")
                continue
            for sec in SECTION.findall(part):
                ok = sec in d.sections
                self.citations.append((where, code, f"§{sec}", d.path.name, ok))
                if not ok:
                    self.bad(where, f"{code} §{sec} is not a section of {d.path.name}")
            for m in RULE.finditer(part):
                rule = m.group(0)
                ok = rule in d.rules
                self.citations.append((where, code, rule, d.path.name, ok))
                if not ok:
                    self.bad(where, f"{code} {rule} is not a rule of {d.path.name}")

    def check_stated(self, where: str, value):
        """A `how` in the `stated` form names where the act of crossing is stated.

        It names it as one or more citations separated by `;`, each carrying a section or a
        rule of a standard. A value that carries neither resolves to nothing, and a program
        that only resolves what it happens to find has nothing to fail on: prose with no
        citation, a correct citation with the act written out after it, and the empty string
        would all pass. So every part must name a place, and the cell as a whole must resolve
        at least one section or rule against the edition of record.
        """
        text = "" if value is None else str(value)
        parts = [p.strip() for p in text.split(";") if p.strip()]
        before = len(self.citations)
        self.check_citation(where, text, None)
        if not parts:
            self.bad(where, "reads stated and is empty, so it names no place where the act "
                            "of crossing is stated")
            return
        nameless = [p for p in parts if not (SECTION.search(p) or RULE.search(p))]
        for p in nameless:
            self.bad(where, "carries a part naming no section and no rule, which is prose "
                            "and not a place where the act is stated: "
                            + " ".join(p.split())[:120])
        if not nameless and len(self.citations) == before:
            self.bad(where, "reads stated and resolves to no section and no rule of any "
                            "edition of record")

    def check_path(self, where: str, rel: str, root: pathlib.Path, root_name: str):
        if not rel or rel in ("none", "absent"):
            return
        for candidate_root, nm in ((root, root_name), (self.outside_root, "the folder holding both")):
            if (candidate_root / rel).exists():
                return
        # In one skill's own folder, a path to skills/<name>/ stands beside it, at ../<name>/.
        if rel.startswith("skills/") and (self.outside_root / "SKILL.md").is_file() \
                and (self.outside_root.parent / rel[len("skills/"):]).exists():
            return
        self.bad(where, f"{rel} exists under neither {root_name} nor the folder holding both")

    # ---- one cell

    def check_how(self, where: str, how: dict):
        if not isinstance(how, dict) or len(set(how) - {"note", "owner"}) != 1:
            self.bad(where, "how carries none of the four forms, or more than one")
            return
        form = next(k for k in how if k not in ("note", "owner"))
        value = how[form]
        if form == "stated":
            self.check_stated(where + " how.stated", value)
        elif form == "kit":
            for token in re.split(r"[;,]", value):
                token = token.strip()
                m = re.match(r"^([A-Za-z0-9_./-]+\.(?:md|py|yaml|yml|tmpl))", token)
                if m:
                    self.check_path(where + " how.kit", m.group(1), self.kit_root, "the kit root")
        elif form == "elsewhere":
            m = re.match(r"^([A-Za-z0-9_./-]+\.(?:md|py|yaml|yml))", value.strip())
            if m:
                self.check_path(where + " how.elsewhere", m.group(1),
                                self.outside_root, "the folder holding both")
            if not how.get("note"):
                self.bad(where, "how.elsewhere carries no note saying no standard cites it")
        elif form == "absent":
            if not how.get("owner"):
                self.bad(where, "how.absent carries no owner")
            self.absent.append(where + " how")
        else:
            self.bad(where, f"how carries the unknown form {form}")

    # ---- the whole file

    def counts(self) -> tuple[int | None, int | None]:
        """How many things and how many handovers the register states it holds, from its own
        `counts:` entry; None where it states none it can be held to."""
        c = self.spec.get("counts") or {}
        things, handovers = c.get("things"), c.get("handovers")
        ok = lambda v: isinstance(v, int) and not isinstance(v, bool) and v > 0   # noqa: E731
        return (things if ok(things) else None), (handovers if ok(handovers) else None)

    def run(self):
        spec = self.spec
        if spec.get("version") != FORMAT_VERSION:
            self.bad("the file", f"version reads {spec.get('version')!r} and not {FORMAT_VERSION}")
        sdd01 = self.doc("SDD-01")
        if sdd01 is None:
            self.bad("the file", "SDD-01 names no document in the standards root")
        else:
            ed = sdd01.edition()
            src = str(spec.get("sourced_from", ""))
            if ed and f"v{ed}" not in src:
                self.bad("the file",
                         f"sourced_from reads {src!r}; the method standard in the root is at "
                         f"version {ed}")
        outside = set(spec.get("outside") or {})
        numbers = [s["n"] for s in spec["slots"]]
        things, _ = self.counts()
        if things is None:
            self.bad("the file", "states no count of its things (counts.things, a whole number), "
                                 "so its rows cannot be held to one")
        elif len(numbers) != things:
            self.bad("the file", f"{len(numbers)} slot rows, and the register's counts.things "
                                 f"states {things}")
        if len(set(numbers)) != len(numbers):
            self.bad("the file", "a slot number stands on more than one row")

        carried: dict[int, list[str]] = {}
        for s in spec["slots"]:
            n = s["n"]
            where = f"slot {n}"
            st = s.get("standard") or {}
            code = st.get("code")
            ungoverned = "absent" in st
            if ungoverned:
                self.absent.append(where + " standard")
                if not st.get("owner"):
                    self.bad(where + " standard", "reads absent and carries no owner")
            elif st:
                self.check_standard(where, s, st)
            else:
                self.check_prose_only(where, s)
                ungoverned = not CODE.findall(str(s.get("governs", "")))
            self.check_ungoverned_claims(where, s, ungoverned)
            if "cadence" not in s:
                self.bad(where, "carries no cadence field")
            if "seams" not in s:
                self.bad(where, "carries no seams field")
            if "preparation" not in s:
                self.bad(where, "carries no preparation field")
            else:
                self.check_preparation(where, s)
            if "check" not in s:
                self.bad(where, "carries no check field")
            else:
                self.check_check(where, s, code)
            self.check_skill(where, s)
            self.check_seams(where, s, code, outside, numbers, carried)

        self.check_handovers(outside, numbers, carried)

    RANGE = re.compile(r"\b((?:RQR|EM|IOS|ARC)-\d+|[MU]\d{1,2}|\d{1,2})\s+to\s+"
                       r"((?:RQR|EM|IOS|ARC)-\d+|[MU]\d{1,2}|\d{1,2})\b")

    def check_prose_only(self, where, s):
        """A row carrying no `standard` cell still states a code and a range in prose."""
        self.bad(where + " standard",
                 "the row carries no standard cell; version 2.0 requires the four "
                 "structured fields")
        prose = str(s.get("governs", ""))
        codes = CODE.findall(prose)
        if not codes:
            return
        d = self.doc(codes[0])
        if d is None:
            self.bad(where + " governs", f"{codes[0]} names no document in the standards root")
            return
        m = self.RANGE.search(prose)
        if not m:
            return
        typed = f"{m.group(1)} to {m.group(2)}"
        got = d.rule_range()
        if got and got.strip().lower() != typed.strip().lower():
            self.bad(where + " governs",
                     f"the register gives the rule range as {typed!r}; {d.path.name} states "
                     f"{got!r}")

    def check_ungoverned_claims(self, where, s, ungoverned: bool):
        """A claim that something is governed by nothing, where a standard governs it."""
        for field in ("governs", "notes"):
            text = str(s.get(field) or "")
            for sentence in re.split(r"(?<=[.!?])\s+", text):
                if ("governed by nothing" in sentence
                        or "claimed by neither" in sentence):
                    if not ungoverned:
                        self.bad(f"{where} {field}",
                                 "states that a thing is governed by nothing, while the row "
                                 "names a standard that governs it: "
                                 + " ".join(sentence.split())[:160])

    def check_standard(self, where, s, st):
        if "file" not in st or "code" not in st:
            self.bad(where + " standard", "carries no code or no file")
            return
        path = self.standards_root / st["file"]
        if not path.exists():
            self.bad(where + " standard", f"{st['file']} is not in the standards root")
            return
        d = self.doc(st["code"])
        for key, got in (("edition", d.edition()), ("standing", d.standing()),
                         ("rules", d.rule_range())):
            typed = str(st.get(key, ""))
            if got is None:
                self.bad(where + f" standard.{key}",
                         f"{path.name} states none and the register types {typed!r}")
            elif got.strip().lower() != typed.strip().lower():
                self.bad(where + f" standard.{key}",
                         f"the register types {typed!r}; {path.name} states {got!r}")
        rendered = f"`{st['code']}` · {st.get('rules')} · **{st.get('standing')}**"
        if str(s.get("governs", "")).strip() != rendered:
            self.bad(where + " governs",
                     f"reads {str(s.get('governs')).strip()!r}; the standard cell renders "
                     f"{rendered!r}")

    def check_preparation(self, where, s):
        p = s.get("preparation") or {}
        code = (s.get("standard") or {}).get("code")
        if "absent" in p:
            self.absent.append(where + " preparation")
            if not p.get("owner"):
                self.bad(where + " preparation", "reads absent and carries no owner")
            return
        self.check_citation(where + " preparation.form", p.get("form", ""), code)
        self.check_path(where + " preparation.template", p.get("template", ""),
                        self.kit_root, "the kit root")
        templates = [("preparation.template", p.get("template"))]
        beside = p.get("beside") or []
        if not isinstance(beside, list):
            self.bad(where + " preparation.beside", "is not a list of templates")
            beside = []
        for i, b in enumerate(beside):
            self.check_path(where + f" preparation.beside[{i}]", str(b), self.kit_root,
                            "the kit root")
            templates.append((f"preparation.beside[{i}]", b))
        for cell, t in templates:
            if str(t or "").strip() == SLOT_README:
                self.bad(where + f" {cell}",
                         f"names {SLOT_README}, the scaffold's readme for the slot, and not a "
                         f"template of the thing itself")
        if p.get("driver"):
            self.check_path(where + " preparation.driver", p["driver"],
                            self.outside_root, "the folder holding both")

    def check_check(self, where, s, code):
        c = s.get("check") or {}
        if "absent" in c:
            self.absent.append(where + " check")
            if not c.get("owner"):
                self.bad(where + " check", "reads absent and carries no owner")
            return
        self.check_citation(where + " check.gate", c.get("gate", ""), code)
        conf = c.get("conformance")
        if isinstance(conf, dict) and "absent" in conf:
            if not conf.get("owner"):
                self.bad(where + " check.conformance", "reads absent and carries no owner")
        else:
            self.check_citation(where + " check.conformance", str(conf or ""), code)
        prog = c.get("program")
        if prog and prog != "none":
            self.check_path(where + " check.program", prog, self.kit_root, "the kit root")
        cl = c.get("checklist")
        if isinstance(cl, dict):
            if "absent" not in cl or not cl.get("owner"):
                self.bad(where + " check.checklist",
                         "reads neither a path nor absent with a reason and an owner")
            else:
                self.absent.append(where + " check.checklist")
        elif str(cl or "").strip() == "absent":
            self.bad(where + " check.checklist",
                     "reads absent with no reason and no owner; a cell whose knowledge does not "
                     "exist says why, and who fills it")
        elif cl:
            self.check_path(where + " check.checklist", str(cl), self.kit_root, "the kit root")
            self.check_checklist_head(where + " check.checklist", str(cl), s)

    def check_checklist_head(self, where, rel, s):
        """The checklist's head names the row's standard and the document standing in the root:
        its file, the edition it states, and its SHA-256 checksum. A checklist emitted from
        another edition, or left behind by a build that did not run to its end, disagrees."""
        path = self.kit_root / rel
        if not path.is_file():
            return                                   # check_path has reported it
        text = path.read_text(encoding="utf-8")
        m = re.match(r"---\n(.*?)\n---\n", text, re.S)
        head = {}
        if m:
            for line in m.group(1).splitlines():
                k, sep, v = line.partition(": ")
                if sep:
                    head[k.strip()] = v.strip().strip('"')
        missing = [k for k in CHECKLIST_HEAD if not head.get(k)]
        if missing:
            self.bad(where, f"{rel} carries no head line for {', '.join(missing)}")
            return
        st = s.get("standard") or {}
        doc_path = self.standards_root / str(st.get("file", ""))
        if head["standard"] != st.get("code"):
            self.bad(where, f"{rel} is the checklist of {head['standard']}, and the row's "
                            f"standard is {st.get('code')}")
        if head["document"] != st.get("file"):
            self.bad(where, f"{rel} was produced from {head['document']}, and the row's "
                            f"document is {st.get('file')}")
        if not doc_path.is_file():
            return                                   # check_standard has reported it
        d = self.doc(st.get("code"))
        stated = d.edition() if d else None
        if stated and head["edition"] != stated:
            self.bad(where, f"{rel} names edition {head['edition']}; {doc_path.name} states "
                            f"edition {stated}")
        digest = hashlib.sha256(doc_path.read_bytes()).hexdigest()
        if head["sha256"] != digest:
            self.bad(where, f"{rel} names the checksum {head['sha256'][:12]}…; {doc_path.name} "
                            f"in the standards root is {digest[:12]}…, so the checklist was not "
                            f"emitted from the document standing there")

    def check_skill(self, where, s):
        """The cell that names the skill helping a person with the thing: plugin:skill, or
        absent with a reason and an owner. Resolving a named skill is the filling round's."""
        if "skill" not in s:
            self.bad(where, "carries no skill field")
            return
        sk = s["skill"]
        if isinstance(sk, dict):
            if "absent" not in sk or not str(sk.get("absent") or "").strip():
                self.bad(where + " skill", "reads neither plugin:skill nor absent with a reason")
            elif not sk.get("owner"):
                self.bad(where + " skill", "reads absent and carries no owner")
            else:
                self.absent.append(where + " skill")
        elif not SKILL_NAME.match(str(sk or "").strip()):
            self.bad(where + " skill", f"reads {sk!r}, which is not of the form plugin:skill")
        else:
            self.check_skill_resolves(where + " skill", s, str(sk).strip())

    def check_skill_resolves(self, where, s, sk):
        """A named skill stands under the marketplace's plugins, carries the standard of its row
        in its frontmatter and pins the edition the row names."""
        plugin, name = sk.split(":")
        path = plugin_skill_md(self.marketplace, plugin, name)
        if path is None:
            self.bad(where, f"{sk} cannot be looked for: {self.marketplace} is neither a "
                            f"marketplace with a plugins folder nor the root of the plugin {plugin}")
            return
        if not path.is_file():
            self.bad(where, f"{sk} names no skill: {path} is not there")
            return
        self.skills_read.append(sk)
        st = s.get("standard") or {}
        code, edition = st.get("code"), str(st.get("edition", "")).strip()
        if not code:
            self.bad(where, f"{sk} is named on a row that names no standard, so the skill's pin "
                            f"cannot be held to one")
            return
        lines = path.read_text(encoding="utf-8").splitlines()
        end = next((j for j in range(1, len(lines)) if lines[j].strip() == "---"), None)
        if not lines or lines[0].strip() != "---" or end is None:
            self.bad(where, f"{sk} carries no frontmatter, so it names no standard and pins no edition")
            return
        try:
            fm = yaml.load("\n".join(lines[1:end]), Loader=yaml.BaseLoader) or {}
        except yaml.YAMLError as exc:
            self.bad(where, f"{sk} has a frontmatter that does not parse: {str(exc).splitlines()[0]}")
            return
        if str(fm.get("standard", "")).strip() != code:
            self.bad(where, f"{sk} names the standard {str(fm.get('standard', '')).strip() or 'none'!r} "
                            f"and its row names {code}")
        wa = fm.get("written_against")
        ed = str(wa.get("edition", "")).strip() if isinstance(wa, dict) else ""
        if not ed:
            self.bad(where, f"{sk} pins no edition (no written_against with an edition)")
        elif ed != edition:
            self.bad(where, f"{sk} is written against edition {ed} of {code}; its row names "
                            f"edition {edition}")

    def check_seams(self, where, s, code, outside, numbers, carried):
        seams = s.get("seams") or {}
        for side in ("takes", "gives"):
            for i, e in enumerate(seams.get(side) or []):
                w = f"{where} seams.{side}[{i}]"
                end = e.get("from") if side == "takes" else e.get("to")
                if end not in numbers and end not in outside:
                    self.bad(w, f"{end!r} is neither a slot of this file nor a declared endpoint")
                self.check_citation(w + " declared_at", e.get("declared_at", ""), code)
                if side == "takes":
                    if "how" not in e:
                        self.bad(w, "a takes entry carrying no how")
                    else:
                        self.check_how(w, e["how"])
                elif "how" in e:
                    self.check_how(w, e["how"])
                if "handover" in e:
                    carried.setdefault(int(e["handover"]), []).append(
                        (side, s["n"], end, "how" in e))

    def check_handovers(self, outside, numbers, carried):
        hs = self.spec.get("handovers") or []
        _, want = self.counts()
        if want is None:
            self.bad("handovers", "the register states no count of its handovers "
                                  "(counts.handovers, a whole number), so they cannot be held to one")
        elif len(hs) != want:
            self.bad("handovers", f"{len(hs)} entries, and the register's counts.handovers "
                                  f"states {want}")
        if not hs:
            for num in sorted(carried):
                self.bad(f"handover {num}",
                         "carried by a seam entry and in no handover entry")
            return
        seen = set()
        additions = (self.standards_root / "_working" / "2026-09-14_improving_the_method"
                     / "03_ADDITIONS.md")
        add_text = additions.read_text(encoding="utf-8") if additions.exists() else None
        for h in hs:
            num = int(h["h"])
            w = f"handover {num}"
            if num in seen:
                self.bad(w, "appears more than once")
            seen.add(num)
            for side in ("from", "to"):
                if h[side] not in numbers and h[side] not in outside:
                    self.bad(w, f"{side} {h[side]!r} is neither a slot nor a declared endpoint")
            for side in ("giving", "receiving"):
                self.check_citation(w + f" declared_by.{side}",
                                    (h.get("declared_by") or {}).get(side, ""), None)
            state = h.get("state")
            if state not in ("holds", "broken", "holds-on-paper"):
                self.bad(w, f"state reads {state!r}")
            clause = (h.get("closes_with") or "").strip()
            if state == "broken" and not clause:
                self.bad(w, "reads broken and names no clause that closes it")
            if state != "broken" and clause:
                self.bad(w, "names a clause and does not read broken")
            if clause:
                if add_text is None:
                    self.bad(w, "names a clause and the additions document is not in the estate")
                else:
                    for c in re.findall(r"clauses? ([0-9a-z, and]+)", clause):
                        for one in re.findall(r"\d+[a-z]?", c):
                            if not re.search(r"\b" + re.escape(one) + r"\b", add_text):
                                self.bad(w, f"clause {one} is not in the additions document")
            # the entries that carry this number, and the one that carries its how
            holders = carried.get(num, [])
            if not holders:
                self.bad(w, "no seam entry of any slot carries this number")
                continue
            for side, slot_n, end, _has_how in holders:
                if side == "takes":
                    if h["to"] != slot_n or h["from"] != end:
                        self.bad(w, f"carried by a takes entry of slot {slot_n} from {end}, "
                                    f"which does not agree with {h['from']} -> {h['to']}")
                elif h["to"] != end or (h["from"] != slot_n and h["from"] not in outside):
                    self.bad(w, f"carried by a gives entry of slot {slot_n} to {end}, which "
                                f"does not agree with {h['from']} -> {h['to']}")
            with_how = [x for x in holders if x[3]]
            if not with_how:
                self.bad(w, "no seam entry carrying this number carries a how")
            elif len(with_how) > 1:
                self.bad(w, f"{len(with_how)} seam entries carrying this number carry a how")
        if want is not None:
            missing = sorted(set(range(1, want + 1)) - seen)
            if missing:
                self.bad("handovers", f"no entry for {missing}")
            beyond = sorted(n for n in seen if n > want or n < 1)
            if beyond:
                self.bad("handovers", f"entries numbered {beyond}, outside 1 to {want}, the "
                                      f"register's count")
        for num in sorted(set(carried) - seen):
            self.bad(f"handover {num}", "carried by a seam entry and in no handover entry")


# --------------------------------------------------------------------------- printing

def print_row(spec, n, res):
    s = next((x for x in spec["slots"] if x["n"] == n), None)
    if s is None:
        print(f"slot {n}: this file carries no such slot", file=sys.stderr)
        return 1
    stamp = now()
    print(f"{s['n']} · {s['title']}")
    print(f"     written by   {s['who']}")
    print(f"     cadence      {', '.join(s['cadence'])}")
    print(f"     when         {' '.join(str(s['when']).split())}")
    print()
    st = s.get("standard") or {}
    print("  THE STANDARD IT READS")
    if "absent" in st:
        print(f"     absent · owner {st.get('owner')}")
        print(f"     {' '.join(str(st['absent']).split())}")
    else:
        path = res.standards_root / st["file"]
        d = res.doc(st["code"])
        print(f"     {st['code']}  {st['file']}")
        print(f"     edition {st['edition']} · {st['standing']} · rules {st['rules']}")
        if d:
            print(f"     read out of {path} at {stamp}")
            print(f"     by           {' '.join(sys.argv)}")
            print(f"     which states edition {d.edition()} · {d.standing()} · "
                  f"rules {d.rule_range()}")
    print()
    p = s.get("preparation") or {}
    print("  THE PREPARATION IT OPENS")
    if "absent" in p:
        print(f"     absent · owner {p.get('owner')}")
        print(f"     {' '.join(str(p['absent']).split())}")
    else:
        print(f"     {p.get('form')}")
        print(f"     template  {p.get('template')}")
        for b in p.get("beside") or []:
            print(f"     beside    {b}")
        if p.get("driver"):
            print(f"     driver    {p['driver']}")
    print()
    print("  THE SEAMS IT VERIFIES")
    for side in ("takes", "gives"):
        for e in (s.get("seams") or {}).get(side) or []:
            end = e.get("from") if side == "takes" else e.get("to")
            arrow = "<-" if side == "takes" else "->"
            num = f"  handover {e['handover']}" if "handover" in e else ""
            print(f"     {arrow} {end}{num}")
            print(f"        what        {' '.join(str(e['what']).split())}")
            print(f"        declared at {e.get('declared_at')}")
            if "how" in e:
                form = next(k for k in e["how"] if k not in ("note", "owner"))
                print(f"        how         {form}: {' '.join(str(e['how'][form]).split())}")
                if e["how"].get("note"):
                    print(f"                    note: {' '.join(str(e['how']['note']).split())}")
                if e["how"].get("owner"):
                    print(f"                    owner: {e['how']['owner']}")
    print()
    c = s.get("check") or {}
    print("  THE CHECK IT RUNS OR NAMES")
    if "absent" in c:
        print(f"     absent · owner {c.get('owner')}")
        print(f"     {' '.join(str(c['absent']).split())}")
    else:
        print(f"     gate         {c.get('gate')}")
        print(f"     checklist    {c.get('checklist')}")
        print(f"     program      {c.get('program')}")
        conf = c.get("conformance")
        if isinstance(conf, dict):
            print(f"     conformance  absent · owner {conf.get('owner')}")
        else:
            print(f"     conformance  {conf}")
    print()
    sk = s.get("skill")
    print("  THE SKILL THAT HELPS BUILD IT")
    if isinstance(sk, dict):
        print(f"     absent · owner {sk.get('owner')}")
        print(f"     {' '.join(str(sk.get('absent')).split())}")
    else:
        print(f"     {sk}")
    print()
    print("  NOTES")
    for line in str(s.get("notes", "")).rstrip().splitlines():
        print(f"     {line}" if line else "")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="kit slot", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("n", nargs="?", help="the slot number as the register writes it, e.g. 07 or 08a")
    ap.add_argument("--check", action="store_true",
                    help="check every row and every handover, against the counts the register "
                         "states")
    ap.add_argument("--slots", type=pathlib.Path, default=SLOTS)
    ap.add_argument("--standards-root", type=pathlib.Path,
                    default=PLUGIN_ROOT / "standards")
    ap.add_argument("--kit-root", type=pathlib.Path, default=KIT_ROOT)
    ap.add_argument("--outside-root", type=pathlib.Path, default=None)
    ap.add_argument("--marketplace", type=pathlib.Path, default=None,
                    help="the marketplace whose plugins hold the skills the register names "
                         "(default: the root of the plugin this kit stands in)")
    ap.add_argument("--citations", action="store_true",
                    help="with --check, print every section and rule the register names, "
                         "the document it was looked for in, and whether it is there")
    a = ap.parse_args(argv)

    outside_root = a.outside_root or a.kit_root.resolve().parent
    if not a.slots.exists():
        print(f"could not run: {a.slots} is not there", file=sys.stderr)
        return 2
    if not a.standards_root.exists():
        print(f"could not run: the standards root {a.standards_root} is not there",
              file=sys.stderr)
        return 2
    try:
        spec = yaml.safe_load(a.slots.read_text(encoding="utf-8"))
    except Exception as exc:                                   # noqa: BLE001
        print(f"could not run: {a.slots} does not parse — {exc}", file=sys.stderr)
        return 2
    if not isinstance(spec, dict) or "slots" not in spec:
        print(f"could not run: {a.slots} carries no slots", file=sys.stderr)
        return 2

    marketplace = a.marketplace or outside_root
    res = Resolver(spec, a.standards_root.resolve(), a.kit_root.resolve(), outside_root,
                   marketplace.resolve())

    if not a.check:
        if not a.n:
            ap.print_usage(sys.stderr)
            return 2
        return print_row(spec, a.n, res)

    try:
        res.run()
    except Exception as exc:                                   # noqa: BLE001
        print(f"could not run: {exc}", file=sys.stderr)
        return 2

    stamp = now()
    if a.citations:
        print(f"every section and rule the register names, looked for at {stamp}")
        print(f"  {'where':<34} {'document':<44} {'names':<14} present")
        for where, code, what, doc, ok in res.citations:
            print(f"  {where:<34} {doc:<44} {code + ' ' + what:<14} "
                  f"{'yes' if ok else 'NO'}")
        good = sum(1 for c in res.citations if c[4])
        print(f"  {len(res.citations)} citations, {good} present, "
              f"{len(res.citations) - good} not")
        print()
    print(f"kit slot --check at {stamp}")
    print(f"  register        {a.slots}")
    print(f"  standards root  {a.standards_root}")
    print(f"  kit root        {a.kit_root}")
    print(f"  marketplace     {marketplace}")
    cells = [x for x in res.absent if not x.endswith(" how")]
    hows = [x for x in res.absent if x.endswith(" how")]
    print(f"  read {len(res.docs)} editions of record; "
          f"{len(spec['slots'])} rows, {len(spec.get('handovers') or [])} handovers")
    print(f"  {len(res.skills_read)} skills named by the register, each found and read for its "
          f"standard and its pin")
    print(f"  {len(cells)} knowledge cells and {len(hows)} how cells read absent, "
          f"each with a reason and an owner; `kit slot <n>` names them")
    if res.problems:
        print(f"  {len(res.problems)} to report:")
        for p in res.problems:
            print(f"    - {p}")
        return 1
    print("  nothing to report")
    return 0


if __name__ == "__main__":
    sys.exit(main())
