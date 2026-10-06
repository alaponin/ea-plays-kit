#!/usr/bin/env python3
"""extract — read a use case model and write model.json. Nothing here judges; it parses.

    python3 extract.py <model file> [--out model.json]
    python3 extract.py <model file> --survey          print the survey generated from the headers
    python3 extract.py <model file> --write-survey    write it to the file the model names
    python3 extract.py <one-file model> --legacy [--out model.json]

THE SHAPE READ (references/model-shape.md). A model file with a YAML head naming the system,
the folder of use case files, the survey file and the five named sets; one file for each use
case, each a filled copy of the kit's template of row 03 (its record header table, whose
`Field` and `Answer` columns are read) with a one-line description beneath it; and a survey
generated from those headers by this program, never written by hand.

The meaning of each header field is taken from the rule its row cites, read from the file
itself (the template's `Rule` column), so no field list is held here: the row citing M16
carries the linked requirements, M17 the entities, M18 the business rules, M21 the format,
M11 the relationships, M5 the primary actor, M8 the name. The three rows no single rule
identifies are known by the first word of their name: the identifier, the level, the status.

THE LEGACY SHAPE (--legacy). The one-file shape of the retired plugin for use case models, read by its
section numbers, for checking only: every field that shape cannot carry is marked absent, so
that the gate reports what is missing instead of failing to parse.

Exit: 0 written · 2 could not run.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

import yaml

ID_RX = re.compile(r"\b[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*-\d+\b")
ROLE_BY_RULE = {"M16": "requirements", "M17": "entities", "M18": "rules", "M21": "format",
                "M11": "relationships", "M5": "actor", "M8": "name"}
ROLE_BY_FIRST_WORD = {"identifier": "id", "level": "level", "status": "status"}
DASHES = {"", "—", "–", "-", "none", "n/a", "not applicable"}


class CouldNotRun(Exception):
    pass


# --------------------------------------------------------------------------- markdown

def front_matter(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text
    data = yaml.safe_load(m.group(1)) or {}
    if not isinstance(data, dict):
        raise CouldNotRun("the model file's head is not a mapping")
    return data, text[m.end():]


def plain(s: str) -> str:
    s = re.sub(r"\*\*|`", "", s or "")
    return re.sub(r"\s+", " ", s).strip()


def cells(line: str) -> list[str]:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", s)]


def is_rule_line(line: str) -> bool:
    return bool(re.match(r"^\|[\s:|-]+\|\s*$", line.strip()))


def tables(lines: list[str]) -> list[list[dict]]:
    """Every pipe table in the lines, as a list of rows keyed by the lower-cased header."""
    out, i = [], 0
    while i < len(lines):
        if lines[i].lstrip().startswith("|") and i + 1 < len(lines) and is_rule_line(lines[i + 1]):
            head = [plain(c).lower() for c in cells(lines[i])]
            rows, j = [], i + 2
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                c = cells(lines[j])
                rows.append({head[k]: (c[k] if k < len(c) else "") for k in range(len(head))})
                j += 1
            out.append(rows)
            i = j
        else:
            i += 1
    return out


def sections(body: str) -> list[tuple[int, str, list[str]]]:
    """(level, heading, lines under it up to the next heading of any level)."""
    out, cur = [], (0, "", [])
    for line in body.split("\n"):
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            out.append(cur)
            cur = (len(m.group(1)), plain(m.group(2)), [])
        else:
            cur[2].append(line)
    out.append(cur)
    return out


def find(secs, *words, level=None):
    """The first section whose heading carries every word given (lower case)."""
    for lv, h, ls in secs:
        hl = h.lower()
        if all(w in hl for w in words) and (level is None or lv == level):
            return lv, h, ls
    return None


def under(secs, start_words, level=2):
    """The lines of a section and of all its sub-sections, down to the next heading at its level."""
    out, on = [], False
    for lv, h, ls in secs:
        if on and lv and lv <= level:
            break
        if not on and lv == level and all(w in h.lower() for w in start_words):
            on = True
            out.extend(ls)
            continue
        if on:
            out.append("#" * lv + " " + h)
            out.extend(ls)
    return out


def prose(lines: list[str]) -> list[str]:
    """Paragraphs of prose; tables, headings, quotes and comments left out."""
    paras, cur = [], []
    for ln in lines:
        if not ln.strip() or ln.lstrip().startswith(("|", "#", ">", "<!--", "-->")):
            if cur:
                paras.append(plain(" ".join(cur)))
                cur = []
            continue
        cur.append(ln.strip())
    if cur:
        paras.append(plain(" ".join(cur)))
    return [p for p in paras if p]


def ids_in(s: str) -> list[str]:
    return list(dict.fromkeys(ID_RX.findall(s or "")))


def split_list(s: str) -> list[str]:
    s = plain(s)
    if s.lower() in DASHES:
        return []
    return [x.strip() for x in re.split(r"\s*[,;]\s*", s) if x.strip() and x.strip().lower() not in DASHES]


# --------------------------------------------------------------------------- one use case file

def parse_relationships(s: str) -> dict:
    rel = {"includes": [], "included_by": [], "extends": [], "extended_by": [],
           "generalises": [], "specialises": []}
    for part in re.split(r"\s*;\s*", plain(s)):
        p = part.strip()
        pl = p.lower()
        if pl in DASHES:
            continue
        if pl.startswith("included by"):
            rel["included_by"] += ids_in(p)
        elif pl.startswith("includes"):
            rel["includes"] += ids_in(p)
        elif pl.startswith("extended by"):
            rel["extended_by"] += ids_in(p)
        elif pl.startswith("extends"):
            m = re.match(r"extends\s+(\S+)(?:\s+at\s+(.*?))?(?:\s+when\s+(.*))?$", p, re.I)
            if m:
                rel["extends"].append({"base": m.group(1).strip(",."),
                                       "point": (m.group(2) or "").strip(),
                                       "when": (m.group(3) or "").strip().rstrip(".")})
        elif pl.startswith(("generalises", "is the parent of")):
            rel["generalises"] += ids_in(p)
        elif pl.startswith(("specialises", "is a kind of")):
            rel["specialises"] += ids_in(p)
        else:
            rel.setdefault("unread", []).append(p)
    return rel


def parse_entities(s: str) -> dict:
    s = plain(s)
    out = {"reads": [], "changes": []}
    if s.lower() in DASHES:
        return out
    labelled = False
    for part in re.split(r"\s*;\s*", s):
        m = re.match(r"^(reads?|changes?)\s*:\s*(.*)$", part.strip(), re.I)
        if m:
            labelled = True
            key = "reads" if m.group(1).lower().startswith("read") else "changes"
            out[key] += split_list(m.group(2))
    if not labelled:
        out["reads"] = split_list(s)
        out["unlabelled"] = True
    return out


def read_use_case(path: pathlib.Path) -> dict:
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    fields, order = {}, []
    for tab in tables(lines):
        if tab and "field" in tab[0] and "answer" in tab[0]:
            for r in tab:
                name = plain(r.get("field", ""))
                if name:
                    fields[name] = {"rule": plain(r.get("rule", "")), "answer": plain(r.get("answer", "")),
                                    "what": plain(r.get("what to record", ""))}
                    order.append(name)
            break
    uc = {"file": path.name, "fields": fields, "field_order": order}
    for name, f in fields.items():
        role = ROLE_BY_RULE.get(f["rule"]) or ROLE_BY_FIRST_WORD.get(name.split()[0].lower())
        if role:
            uc[f"_{role}"] = f["answer"]
    uc["id"] = plain(uc.get("_id", ""))
    uc["name"] = plain(uc.get("_name", ""))
    uc["level"] = plain(uc.get("_level", "")).lower()
    uc["actor"] = plain(uc.get("_actor", ""))
    st = [x.strip() for x in re.split(r"\s*[·;,]\s*", plain(uc.get("_status", ""))) if x.strip()]
    uc["status"] = st[0].lower() if st else ""
    uc["priority"] = st[1] if len(st) > 1 else ""
    uc["format"] = plain(uc.get("_format", "")).lower()
    uc["requirements"] = ids_in(uc.get("_requirements", ""))
    uc["requirements_text"] = plain(uc.get("_requirements", ""))
    uc["entities"] = parse_entities(uc.get("_entities", ""))
    uc["rules"] = ids_in(uc.get("_rules", ""))
    uc["relationships"] = parse_relationships(uc.get("_relationships", ""))
    secs = sections(text)
    d = find(secs, "one-line description")
    uc["description"] = (prose(d[2]) or [""])[0] if d else ""
    for k in [k for k in uc if k.startswith("_")]:
        del uc[k]
    return uc


# --------------------------------------------------------------------------- the named sets

def entries_of(path: pathlib.Path) -> list[str]:
    """The identifiers or names a named set carries: the first cell of every table row of a
    markdown file, the keys or `id`/`name` values of a YAML or JSON file, the first column of a
    delimited file."""
    suf = path.suffix.lower()
    text = path.read_text(encoding="utf-8")
    out: list[str] = []
    if suf in (".yaml", ".yml", ".json"):
        data = json.loads(text) if suf == ".json" else yaml.safe_load(text)
        if isinstance(data, dict):
            data = data.get("entries", data)
        if isinstance(data, dict):
            out = [str(k) for k in data]
        elif isinstance(data, list):
            for x in data:
                if isinstance(x, dict):
                    out.append(str(x.get("id") or x.get("name") or ""))
                else:
                    out.append(str(x))
    elif suf in (".csv", ".tsv"):
        sep = "\t" if suf == ".tsv" else ","
        rows = [ln.split(sep)[0].strip().strip('"') for ln in text.splitlines() if ln.strip()]
        out = rows[1:]
    else:
        for tab in tables(text.split("\n")):
            for r in tab:
                first = plain(next(iter(r.values()), ""))
                if first:
                    out.append(first)
    return [x for x in out if x]


def statements_of(path: pathlib.Path) -> dict:
    """For a markdown named set: the first cell of each row mapped to its second cell, which is
    what the reader's edition quotes for a rule or an entity. Other formats map to nothing."""
    out = {}
    if path.suffix.lower() in (".md", ".markdown", ""):
        for tab in tables(path.read_text(encoding="utf-8").split("\n")):
            for r in tab:
                vals = list(r.values())
                if vals and plain(vals[0]):
                    out[plain(vals[0])] = plain(vals[1]) if len(vals) > 1 else ""
    return out


def named_sets(front: dict, base: pathlib.Path) -> dict:
    out = {}
    for key, val in (front.get("named") or {}).items():
        rec = {"declared": val}
        if isinstance(val, str) and val.strip():
            p = (base / val).resolve()
            rec["path"] = str(p)
            rec["exists"] = p.is_file()
            rec["entries"] = entries_of(p) if p.is_file() else []
            rec["statements"] = statements_of(p) if p.is_file() else {}
        elif isinstance(val, dict):
            if "absent" in val:
                rec["absent"] = str(val.get("absent", ""))
                rec["owner"] = str(val.get("owner", ""))
            if "none" in val:
                rec["none"] = str(val.get("none", ""))
        out[key] = rec
    return out


# --------------------------------------------------------------------------- the model file

def natural(i: str):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", i)]


def read_model(model: pathlib.Path) -> dict:
    text = model.read_text(encoding="utf-8")
    front, body = front_matter(text)
    if not front:
        raise CouldNotRun(f"{model} opens with no YAML head; a model in the one-file shape is "
                          f"read with --legacy")
    secs = sections(body)
    base = model.parent
    M: dict = {"shape": "files", "model_file": str(model), "front": front,
               "system": plain(str(front.get("system", "")))}
    M["purpose"] = prose(under(secs, ["purpose"]))
    ins = find(secs, "inside")
    outs = find(secs, "outside")
    M["inside"] = prose(ins[2]) if ins else []
    M["outside"] = prose(outs[2]) if outs else []

    M["actors"] = []
    for tab in tables(under(secs, ["actors"])):
        for r in tab:
            name = plain(r.get("actor", ""))
            if not name:
                continue
            person = plain(next((v for k, v in r.items() if "person" in k), "")).lower()
            M["actors"].append({"name": name, "kind": plain(r.get("kind", "")).lower(),
                                "person": person,
                                "goal": plain(next((v for k, v in r.items() if "goal" in k or "service" in k), ""))})
    M["packages"] = []
    for tab in tables(under(secs, ["packages"])):
        for r in tab:
            name = plain(r.get("package", ""))
            if not name:
                continue
            members = ids_in(next((v for k, v in r.items() if "use cases" in k), ""))
            M["packages"].append({"name": name, "code": plain(r.get("code", "")),
                                  "about": plain(next((v for k, v in r.items() if "about" in k), "")),
                                  "members": members})
        break
    dep = find(secs, "depend")
    M["packages_prose"] = prose(dep[2]) if dep else []

    M["associations"] = {}
    for tab in tables(under(secs, ["supporting actor"])):
        for r in tab:
            uc = ids_in(r.get("use case", ""))
            if uc:
                M["associations"][uc[0]] = split_list(next((v for k, v in r.items() if "supporting" in k), ""))
    rsecs = sections("\n".join(under(secs, ["relationships"])))
    M["includes"], M["extends"] = [], []
    inc = find(rsecs, "included")
    if inc:
        for tab in tables(inc[2]):
            for r in tab:
                i = ids_in(r.get("included", ""))
                if i:
                    M["includes"].append({"included": i[0],
                                          "bases": ids_in(next((v for k, v in r.items() if "base" in k), "")),
                                          "why": plain(next((v for k, v in r.items() if "why" in k), ""))})
    ext = find(rsecs, "optional")
    if ext:
        for tab in tables(ext[2]):
            for r in tab:
                e = ids_in(r.get("extension", ""))
                if e:
                    M["extends"].append({"extension": e[0], "base": (ids_in(r.get("base", "")) or [""])[0],
                                         "point": plain(next((v for k, v in r.items() if "point" in k), "")),
                                         "when": plain(r.get("when", ""))})
    gen = find(rsecs, "generalisation")
    M["generalisations"] = prose(gen[2]) if gen else []
    nd = find(rsecs, "not draw")
    M["not_drawn"] = prose(nd[2]) if nd else []
    dg = find(secs, "diagrams")
    M["diagrams"] = prose(dg[2]) if dg else []
    fd = find(secs, "written out")
    M["format_decision"] = prose(fd[2]) if fd else []

    ucdir = base / str(front.get("use_cases", "use_cases"))
    M["use_case_dir"] = str(ucdir)
    M["use_cases"] = [read_use_case(p) for p in sorted(ucdir.glob("*.md"), key=lambda p: natural(p.stem))] \
        if ucdir.is_dir() else []
    member_of = {i: p["code"] or p["name"] for p in M["packages"] for i in p["members"]}
    for uc in M["use_cases"]:
        uc["package"] = member_of.get(uc["id"], "")
    M["named"] = named_sets(front, base)
    sv = base / str(front.get("survey", "survey.md"))
    M["survey"] = {"path": str(sv), "exists": sv.is_file(),
                   "text": sv.read_text(encoding="utf-8") if sv.is_file() else ""}
    M["version"] = str(front.get("version", "") or "")
    return M


# --------------------------------------------------------------------------- the survey

def survey_text(M: dict) -> str:
    """The survey, generated from the record headers: one row for each use case, every field of
    its header in the order the header carries them, then its package and its one-line
    description. Rows in the order of the packages, then of the identifiers."""
    ucs = M["use_cases"]
    if not ucs:
        return ""
    order = ucs[0]["field_order"]
    pk_order = {p["code"] or p["name"]: i for i, p in enumerate(M["packages"])}
    rows = sorted(ucs, key=lambda u: (pk_order.get(u["package"], len(pk_order)), natural(u["id"])))
    head = order + ["Package", "One-line description"]
    out = ["<!-- Generated from the record headers by extract.py --write-survey. Never written by hand: "
           "a change goes into a use case file, and the survey is generated again. -->",
           "", "# The survey", "",
           "| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    for u in rows:
        vals = [u["fields"].get(f, {}).get("answer", "") for f in order]
        vals += [u["package"], u["description"]]
        out.append("| " + " | ".join(v.replace("|", "\\|") for v in vals) + " |")
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------- the legacy shape

LEGACY_SEC = {
    'packages': (r'^## 5\.', r'^## 6\.'), 'survey': (r'^## 6\.', r'^## 7\.'),
    'actors': (r'^## 4\.', r'^## 5\.'), 'entities': (r'^## 15\.', r'^## 16\.'),
    'rules': (r'^## 16\.', r'^## 17\.'), 'includes': (r'^### 7\.1', r'^### 7\.2'),
    'extends': (r'^### 7\.2', r'^### 7\.3|^## 8\.'), 'in_scope': (r'^### 3\.1', r'^### 3\.2'),
    'out_scope': (r'^### 3\.3', r'^### 3\.4'), 'purpose': (r'^## 1\.', r'^### 1\.|^## 2\.'),
}
LEVEL_LETTER = {"S": "summary", "U": "user goal", "F": "subfunction", "X": "subfunction"}


def read_legacy(model: pathlib.Path) -> dict:
    L = model.read_text(encoding="utf-8").split("\n")

    def rng(key):
        a, b = LEGACY_SEC[key]
        i = next((k for k, l in enumerate(L) if re.match(a, l)), None)
        if i is None:
            return 0, 0
        j = next((k for k, l in enumerate(L) if k > i and re.match(b, l)), len(L))
        return i, j

    def rows(key, first=r"."):
        i, j = rng(key)
        out = []
        for l in L[i:j]:
            if not l.startswith("|") or is_rule_line(l):
                continue
            c = [x.strip() for x in l.strip().strip("|").split("|")]
            if not c or not c[0] or re.match(r"^(ID|Package|Entity|Actor|Rule|Parameter|#|Included|Extension)$", c[0]):
                continue
            if re.match(first, c[0]):
                out.append(c)
        return out

    M: dict = {"shape": "legacy", "model_file": str(model), "front": {}}
    h1 = next((l for l in L if l.startswith("# ")), "")
    M["system"] = plain(h1[2:])
    i, j = rng("purpose")
    M["purpose"] = prose(L[i + 1:j]) if j else []
    i, j = rng("in_scope")
    M["inside"] = prose(L[i + 1:j]) if j else []
    i, j = rng("out_scope")
    M["outside"] = prose(L[i + 1:j]) if j else []
    M["actors"] = []
    i, j = rng("actors")
    bucket = None
    for l in L[i:j]:
        h = re.match(r"^#{2,4} \d+\.\d+\s+(.*)$", l)
        if h:
            t = h.group(1).lower()
            bucket = ("human" if "human" in t else "bodies" if "bod" in t or "decision" in t else
                      "time" if "time" in t or "clock" in t else "systems" if "support" in t or "system" in t
                      else "offstage" if "offstage" in t else None)
            continue
        if bucket is None or not l.startswith("|") or is_rule_line(l):
            continue
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) < 2 or c[0] in ("ID", "Actor"):
            continue
        if bucket == "offstage":
            M["actors"].append({"name": plain(c[0]), "kind": "offstage", "person": "", "goal": plain(c[1])})
        elif re.match(r"^AC-\d+", c[0].strip("`* ")):
            kind = "supporting" if bucket == "systems" else "primary"
            person = "yes" if bucket in ("human", "bodies") else "no"
            M["actors"].append({"name": re.split(r"\s+[—–(]", plain(c[1]))[0].strip(), "kind": kind,
                                "person": person, "goal": plain(c[2]) if len(c) > 2 else ""})
    M["packages"] = []
    for c in rows("packages", r"^\*\*"):
        if len(c) >= 4 and "Total" not in c[0]:
            M["packages"].append({"name": plain(c[0]), "code": plain(c[1]), "about": plain(c[2]),
                                  "members": [], "stated_count": plain(c[3])})
    M["packages_prose"] = []
    M["use_cases"] = []
    i, j = rng("survey")
    cur, cols = None, None
    default_cols = ["id", "use case", "primary actor", "lv · pri · st", "brief", "provenance"]
    for k in range(i, j):
        h = re.match(r"^#{2,4} \d+\.\d+\s+(.*)$", L[k])
        if h:
            code = re.search(r"\b([A-Z]{2})\b", h.group(1))
            cur, cols = (code.group(1) if code else ""), None
            continue
        c = [x.strip() for x in L[k].strip().strip("|").split("|")] if L[k].startswith("|") else []
        if c and c[0] == "ID":                 # a table re-declares its columns; the groups differ
            cols = [plain(x).lower() for x in c]
            continue
        if len(c) < 4 or not re.match(r"^[A-Z]{2,3}-\d+$", c[0].strip("`* ")):
            continue
        cc = cols or default_cols

        def col(*names):
            for nm in names:
                for ci, hd in enumerate(cc):
                    if nm in hd and ci < len(c):
                        return plain(c[ci])
            return ""
        lv = [x.strip() for x in col("lv").split("·")]
        actor = col("primary actor", "actor")
        # the role alone: a gloss after a dash, a bracket or a comma is not part of the name
        actor = re.split(r"\s+[—–(]|,", actor)[0].strip()
        uc = {"file": model.name, "fields": {}, "field_order": [], "id": c[0].strip("`* "),
              "name": col("use case"), "actor": actor,
              "level": LEVEL_LETTER.get(lv[0][:1].upper(), lv[0].lower()) if lv and lv[0] else "",
              "priority": lv[1] if len(lv) > 1 else "", "status": lv[2].lower() if len(lv) > 2 else "",
              "format": lv[3].lower() if len(lv) > 3 else "", "requirements": [], "requirements_text": "",
              "entities": {"reads": [], "changes": []}, "rules": [],
              "relationships": {"includes": [], "included_by": ids_in(col("included by")), "extends": [],
                                "extended_by": [], "generalises": [], "specialises": []},
              "description": col("brief"), "package": cur or "",
              "absent": ["format", "linked requirements", "entities", "business rules", "relationships"]}
        if "subfunction" in uc["actor"].lower() or uc["actor"] in ("—", "-"):
            uc["actor"] = ""
        M["use_cases"].append(uc)
    for p in M["packages"]:
        p["members"] = [u["id"] for u in M["use_cases"] if u["package"] == p["code"]]
    by_id = {u["id"]: u for u in M["use_cases"]}
    M["includes"], M["extends"] = [], []
    for c in rows("includes", r"^\*\*[A-Z]{2,3}-\d+"):
        inc = ids_in(c[0])
        bases = ids_in(c[2]) if len(c) > 2 else []
        if inc:
            M["includes"].append({"included": inc[0], "bases": bases, "why": plain(c[3]) if len(c) > 3 else ""})
            if inc[0] in by_id:
                by_id[inc[0]]["relationships"]["included_by"] += bases or ["(bases named in words)"]
            for b in bases:
                if b in by_id:
                    by_id[b]["relationships"]["includes"].append(inc[0])
    for c in rows("extends", r"^\*\*"):
        e, b = ids_in(c[0]), (ids_in(c[1]) if len(c) > 1 else [])
        if e:
            M["extends"].append({"extension": e[0], "base": b[0] if b else "", "point": "",
                                 "when": plain(c[3]) if len(c) > 3 else plain(c[2]) if len(c) > 2 else ""})
    M["generalisations"], M["not_drawn"], M["diagrams"], M["format_decision"] = [], [], [], []
    M["associations"] = {}
    ents = [plain(c[0]) for c in rows("entities", r"^\*\*") if len(c) >= 2]
    rules = [c[0].strip("`* ") for c in rows("rules", r"^`?BR-\d+")]
    M["named"] = {
        "requirements": {"declared": None},
        "entity_model": {"declared": "inline", "inline": "the model file's section 15", "entries": ents},
        "glossary": {"declared": None},
        "business_rules": {"declared": "inline", "inline": "the model file's section 16", "entries": rules},
        "settings": {"declared": None},
    }
    M["survey"] = {"path": str(model), "exists": True, "text": "", "written_by_hand": True}
    M["version"] = ""
    M["use_case_dir"] = ""
    return M


# --------------------------------------------------------------------------- main

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="extract.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("model", type=pathlib.Path)
    ap.add_argument("--out", type=pathlib.Path)
    ap.add_argument("--legacy", action="store_true")
    ap.add_argument("--survey", action="store_true", help="print the survey generated from the headers")
    ap.add_argument("--write-survey", action="store_true", help="write it to the file the model names")
    a = ap.parse_args(argv)
    try:
        if not a.model.is_file():
            raise CouldNotRun(f"{a.model} is not there")
        M = read_legacy(a.model) if a.legacy else read_model(a.model)
    except CouldNotRun as exc:
        print(f"extract: could not run: {exc}", file=sys.stderr)
        return 2
    if a.survey or a.write_survey:
        if a.legacy:
            print("extract: the one-file shape has no record headers to generate a survey from", file=sys.stderr)
            return 2
        s = survey_text(M)
        if a.write_survey:
            pathlib.Path(M["survey"]["path"]).write_text(s, encoding="utf-8")
            print(f"written {M['survey']['path']}: {len(M['use_cases'])} rows")
        else:
            sys.stdout.write(s)
        return 0
    out = a.out or pathlib.Path("model.json")
    out.write_text(json.dumps(M, indent=1, ensure_ascii=False), encoding="utf-8")
    kinds: dict = {}
    for x in M["actors"]:
        kinds[x["kind"] or "?"] = kinds.get(x["kind"] or "?", 0) + 1

    def said(v):
        if "absent" in v:
            return "absent"
        if "none" in v:
            return "none"
        if "inline" in v:
            return "inside the model file"
        if "path" in v:
            return "found" if v.get("exists") else "NOT FOUND"
        return "not named"
    print(f"shape {M['shape']} · use cases {len(M['use_cases'])} · packages {len(M['packages'])} · "
          f"actors {len(M['actors'])} ({', '.join(f'{k} {v}' for k, v in sorted(kinds.items()))}) · "
          f"includes {len(M['includes'])} · extends {len(M['extends'])}")
    print("named sets: " + ", ".join(f"{k} {said(v)}" for k, v in M["named"].items()))
    print(f"written {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
