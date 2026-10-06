#!/usr/bin/env python3
"""skills_check — every skill's pin, against the standard in the root and the checklist's head.

    kit skills --check [--standards-root D] [--marketplace D] [--kit-root D]

THE PIN. A skill of the method records, in its frontmatter, the standard it serves and the
edition and checksum of the document it was written against (04_TARGET_STATE.md section 5;
the plan of the finish, PLAN.md section 3.1):

    standard: SDD-05
    written_against: {edition: "2.1", sha256: "…"}

The pin is the record of what the skill's author read, not what the skill reads at run time.

THE CHECK. For every SKILL.md at `plugins/<plugin>/skills/<skill>/SKILL.md` under the
marketplace (or at `skills/<skill>/SKILL.md` under a plugin's own root, as in sdd-kit) whose frontmatter carries a `standard:` line, the program finds the document
standing in the standards root for that standard — by its code (`SDD-05` is the file whose name
begins `SDD-05_`) or, for a pin that names a document rather than a code, by that name — reads
its edition and computes its checksum, and reads the head of the standard's checklist,
`templates/spec/checklists/<code>.md` under the kit. It prints one line for each skill:

    current                                  the pin is the document standing in the root
    behind                                   the root holds another edition or another text;
                                             both editions and both checksums are named
    pinned to a document not in the root     nothing standing in the root answers to the pin

and says on the same line whether the checklist's head names the edition and checksum the skill
pins: `checklist agrees`, `checklist disagrees` with what it names, or `no checklist in the kit`
when the standard has none. A skill that carries a `standard:` line and no `written_against`
with an edition and a checksum is reported as `unpinned`; one whose frontmatter does not parse,
as `could not be read`; and a pin to a standard for which the root holds two documents, as
`not judged`, since a superseded standard leaves the root.

It exits 0 when every skill is current and every checklist it read agrees, 1 when anything is
to report, and 2 when it could not run. It reports and never blocks (CONSTANTS.md section 5,
item 11). The edition of a document of record is read by the kit's own reader, `slot.py`.
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
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import conform                                                    # noqa: E402  read_head
import slot                                                       # noqa: E402  Document, docx_text

CODE = re.compile(r"^[A-Z][A-Z0-9]*-\d+$")
NOT_IN_ROOT = "pinned to a document not in the root"


def now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_of(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def short(h: str | None) -> str:
    return (h or "?")[:12]


def documents_in_root(root: pathlib.Path, standard: str) -> list[pathlib.Path]:
    """The documents standing in the root (not below it) that answer to a pin's `standard:`."""
    files = [f for f in root.iterdir()
             if f.is_file() and f.suffix.lower() in (".docx", ".md")
             and not f.name.startswith(("~$", "."))]
    if CODE.match(standard):
        return sorted(f for f in files if f.name.startswith(standard + "_"))
    return sorted(f for f in files if f.stem == standard or f.stem.startswith(standard + "_"))


def edition_of(path: pathlib.Path) -> str | None:
    """The edition a document of record states: its `Version and standing` line, read by the
    kit's reader; failing that, a `Version N.N` in its first lines; failing that, its name."""
    doc = slot.Document(path)
    ed = doc.edition()
    if ed:
        return ed.rstrip(".")
    m = re.search(r"\bVersion\s+([0-9]+(?:\.[0-9]+)+)", "\n".join(doc.text.splitlines()[:60]))
    if m:
        return m.group(1)
    m = re.search(r"_v([0-9]+(?:[._][0-9]+)*)$", path.stem)
    return m.group(1).replace("_", ".") if m else None


def frontmatter(text: str):
    """(the frontmatter's text or None, whether it carries a `standard:` line)."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, False
    for j in range(1, len(lines)):
        if lines[j].strip() == "---":
            body = "\n".join(lines[1:j])
            return body, bool(re.search(r"(?m)^standard\s*:", body))
    return None, False


def checklist_line(kit_root: pathlib.Path, standard: str, edition: str, sha: str):
    """(the words for the checklist's side, whether it is something to report)."""
    if not CODE.match(standard):
        return "no checklist in the kit", False
    path = kit_root / "templates" / "spec" / "checklists" / f"{standard}.md"
    if not path.is_file():
        return "no checklist in the kit", False
    head, _, err = conform.read_head(path.read_text(encoding="utf-8"))
    if head is None:
        return f"checklist {path.name} has no head in the form of PLAN.md section 3.1 ({err})", True
    ced, csha = str(head.get("edition", "")), str(head.get("sha256", ""))
    if ced == edition and csha == sha:
        return "checklist agrees", False
    return (f"checklist disagrees: its head names {ced or '?'} (sha256 {short(csha)}), "
            f"the pin {edition} (sha256 {short(sha)})"), True


def judge_skill(skill_md: pathlib.Path, root: pathlib.Path, kit_root: pathlib.Path):
    """(verdict, the rest of the line, whether it is something to report) — or None when the
    skill carries no `standard:` line and so pins nothing."""
    body, has_standard = frontmatter(skill_md.read_text(encoding="utf-8"))
    if not has_standard:
        return None
    try:
        fm = yaml.load(body, Loader=yaml.BaseLoader) or {}
    except yaml.YAMLError as exc:
        return ("could not be read", f"its frontmatter does not parse: "
                f"{str(exc).splitlines()[0]}", True)
    standard = str(fm.get("standard", "")).strip()
    wa = fm.get("written_against")
    edition = str(wa.get("edition", "")).strip() if isinstance(wa, dict) else ""
    sha = str(wa.get("sha256", "")).strip().lower() if isinstance(wa, dict) else ""
    if not standard or not edition or not sha:
        return ("unpinned", f"carries `standard: {standard}` and no `written_against` with an "
                "edition and a sha256", True)
    pin = f"{standard} {edition} (sha256 {short(sha)})"
    docs = documents_in_root(root, standard)
    if not docs:
        return (NOT_IN_ROOT, f"pins {pin}; nothing standing in {root} answers to {standard}", True)
    if len(docs) > 1:
        return ("not judged", f"pins {pin}; the root holds {len(docs)} documents for "
                f"{standard}, {', '.join(d.name for d in docs)}, and a superseded standard "
                "leaves the root (README, the rules this folder is under)", True)
    doc = docs[0]
    red, rsha = edition_of(doc), sha256_of(doc)
    cl, cl_bad = checklist_line(kit_root, standard, edition, sha)
    if red == edition and rsha == sha:
        return "current", f"{pin} is {doc.name}; {cl}", cl_bad
    same = "the same edition, another text" if red == edition else "another edition"
    return ("behind", f"pins {pin}; the root holds {red or 'an edition it does not state'} "
            f"(sha256 {short(rsha)}) in {doc.name} — {same}; {cl}", True)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="kit skills", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true",
                    help="compare every skill's pin with the root and the checklist's head")
    ap.add_argument("--standards-root", type=pathlib.Path,
                    default=KIT_ROOT.parent / "standards")
    ap.add_argument("--marketplace", type=pathlib.Path,
                    default=KIT_ROOT.parent)
    ap.add_argument("--kit-root", type=pathlib.Path, default=KIT_ROOT)
    a = ap.parse_args(argv)
    if not a.check:
        ap.print_usage(sys.stderr)
        print("kit skills: --check is the one act of this command", file=sys.stderr)
        return 2
    root, market, kit_root = a.standards_root, a.marketplace, a.kit_root
    if not root.is_dir():
        print(f"kit skills --check: could not run: the standards root {root} is not there",
              file=sys.stderr)
        return 2
    plugins = market / "plugins"
    manifest = market / ".claude-plugin" / "plugin.json"
    if plugins.is_dir():
        found = [(p.parent.parent.parent.name, p) for p in sorted(plugins.glob("*/skills/*/SKILL.md"))]
    elif manifest.is_file():                      # a plugin's own root: sdd-kit
        import json
        name = json.loads(manifest.read_text(encoding="utf-8")).get("name") or market.name
        plugins = market / "skills"
        found = [(name, p) for p in sorted(plugins.glob("*/SKILL.md"))]
    elif (market / "SKILL.md").is_file():         # one skill's own folder, with its copy of the kit
        plugins = market
        found = [("sdd-kit", market / "SKILL.md")]
    else:
        print(f"kit skills --check: could not run: {plugins} is not there, and {market} is not "
              f"the root of a plugin", file=sys.stderr)
        return 2

    rows = []
    try:
        for plugin_name, skill_md in found:
            r = judge_skill(skill_md, root, kit_root)
            if r is not None:
                rows.append((plugin_name + "/" + skill_md.parent.name,) + r)
    except Exception as exc:                                         # noqa: BLE001
        print(f"kit skills --check: could not run: {exc}", file=sys.stderr)
        return 2

    print(f"kit skills --check at {now()}")
    print(f"  standards root  {root}")
    print(f"  marketplace     {market}")
    print(f"  kit root        {kit_root}")
    if not rows:
        print(f"  no SKILL.md under {plugins} carries a `standard:` line; "
              "nothing is pinned, so nothing is compared")
        return 0
    width = max(len(r[0]) for r in rows)
    for name, verdict, rest, _ in rows:
        print(f"  {verdict:<11} {name:<{width}}  {rest}")
    tally = {}
    for _, verdict, _, _ in rows:
        tally[verdict] = tally.get(verdict, 0) + 1
    bad = sum(1 for r in rows if r[1] != "current" or r[3])
    print(f"  {len(rows)} skills carry a `standard:` line: "
          + ", ".join(f"{n} {v}" for v, n in sorted(tally.items()))
          + f"; {bad} to report")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
