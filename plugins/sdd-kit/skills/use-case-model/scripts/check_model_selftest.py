#!/usr/bin/env python3
"""check_model_selftest — the check proved on both sides before it is trusted.

    python3 check_model_selftest.py [--kit-root DIR]

The fixture of this skill, `examples/fixture/`, is copied into a temporary folder and checked
as it stands: the program's half must find nothing. Then each mutation below is made on a fresh
copy, one fault at a time; the survey is generated again after every change to a use case file,
except in the mutation that edits the survey itself. Each mutation must produce a finding on the
line named beside it and on no other line. Last, the one-file fixture, `examples/refused/`, must
be refused on the four lines the report of 24 September 2026 named for a model of that shape
(M16, M19–M20, M21, M22).

Nothing is written inside the skill: every copy is made in a temporary folder and removed.

Exit: 0 every case as expected · 1 a case not as expected · 2 could not run.
"""
from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import argparse                                     # noqa: E402
import os                                           # noqa: E402
import pathlib                                      # noqa: E402
import re                                           # noqa: E402
import shutil                                       # noqa: E402
import subprocess                                   # noqa: E402
import tempfile                                     # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
SKILL = HERE.parent
FIXTURE = SKILL / "examples" / "fixture"
REFUSED = SKILL / "examples" / "refused" / "use_case_model_one_file.md"
LINE = re.compile(r"^(M\d+(?:–M\d+)?) · (PASS|FINDING|OPEN) · ")


def run(args: list[str], env: dict) -> tuple[int, str]:
    p = subprocess.run([sys.executable, "-B", *args], capture_output=True, text=True, env=env)
    return p.returncode, p.stdout + p.stderr


def verdicts(out: str) -> dict:
    return {m.group(1): m.group(2) for m in (LINE.match(l) for l in out.splitlines()) if m}


def sub(path: pathlib.Path, old: str, new: str):
    t = path.read_text(encoding="utf-8")
    if old not in t:
        raise SystemExit(f"selftest: the mutation's text {old!r} is not in {path.name}")
    path.write_text(t.replace(old, new, 1), encoding="utf-8")


def answer(uc: pathlib.Path, field: str, new: str):
    """Replace the Answer cell of one header row."""
    lines = uc.read_text(encoding="utf-8").split("\n")
    for i, ln in enumerate(lines):
        c = ln.split("|")
        if ln.startswith("| ") and len(c) >= 6 and c[1].strip() == field:
            c[-2] = f" {new} "
            lines[i] = "|".join(c)
            uc.write_text("\n".join(lines), encoding="utf-8")
            return
    raise SystemExit(f"selftest: {uc.name} has no header row {field!r}")


# Each: (the line expected to carry the finding, what the fault is, the change, whether the
# survey is generated again after it).
def mutations(d: pathlib.Path):
    uc = d / "use_cases"
    ns = d / "named_sets"
    model = d / "use_case_model.md"
    return [
        ("M14", "a use case with no primary actor", lambda: answer(uc / "UC-09.md", "Primary actor", ""), True),
        ("M4–M6", "an actor with no kind", lambda: sub(model, "| Council auditor | offstage |", "| Council auditor |  |"), True),
        ("M7–M8", "a name opening on a noun", lambda: answer(uc / "UC-09.md", "Name", "Management of plots"), True),
        ("M9", "a use case with no level", lambda: answer(uc / "UC-09.md", "Level", ""), True),
        ("M9–M11", "a subfunction nothing includes", lambda: (
            answer(uc / "UC-02.md", "Relationships", "includes UC-06; extended by UC-04"),
            answer(uc / "UC-07.md", "Relationships", "—"),
            sub(model, "| UC-07 | UC-02 | The residence check is the same step for every application |\n", "")), True),
        ("M12–M13", "a use case in no package", lambda: sub(model, "UC-08, UC-09 |", "UC-08 |"), True),
        ("M16", "a linked requirement not in the register", lambda: answer(uc / "UC-09.md", "Linked requirements", "FR-REL-001, FR-XXX-999"), True),
        ("M16", "a register entry no use case realises", lambda: sub(ns / "requirements.md", "| FR-REL-001 |", "| FR-NEW-001 | A requirement nothing realises |\n| FR-REL-001 |"), True),
        ("M17", "an entity the entity model does not carry", lambda: answer(uc / "UC-09.md", "Entities", "reads: Allocation; changes: Allocation, Plot, Tool shed"), True),
        ("M18", "a rule the register does not carry", lambda: answer(uc / "UC-09.md", "Business rules", "BR-XXX-99"), True),
        ("M21", "a use case with no format", lambda: answer(uc / "UC-09.md", "Format", ""), True),
        ("M22", "no glossary named", lambda: sub(model, "  glossary: named_sets/glossary.md\n", ""), True),
        ("M14", "a supporting actor no use case calls on", lambda: sub(model, "| UC-06 | Identity service |\n", ""), True),
        ("M19–M20", "the survey edited by hand", lambda: sub(d / "survey.md", "| Give up a plot |", "| Give a plot up |"), False),
        ("M16", "the register of requirements absent, with its owner named", lambda: sub(
            model, "  requirements: named_sets/requirements.md\n",
            '  requirements: {absent: "the published register of requirements", owner: "the requirements analyst"}\n'), True),
    ]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="check_model_selftest.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--kit-root", type=pathlib.Path)
    a = ap.parse_args(argv)
    env = dict(os.environ)
    if a.kit_root:
        env["SDD_KIT_ROOT"] = str(a.kit_root)
    if not FIXTURE.is_dir() or not REFUSED.is_file():
        print("selftest: could not run: the fixtures are not beside the skill", file=sys.stderr)
        return 2
    bad = 0
    with tempfile.TemporaryDirectory(prefix="ucm-selftest-") as tmp:
        base = pathlib.Path(tmp) / "fixture"
        shutil.copytree(FIXTURE, base)
        code, out = run([str(HERE / "check_model.py"), str(base / "use_case_model.md")], env)
        if code == 2:
            print(out)
            print("selftest: could not run the check on the fixture", file=sys.stderr)
            return 2
        v = verdicts(out)
        found = sorted(k for k, x in v.items() if x == "FINDING")
        ok = code == 0 and not found and len(v) > 0
        bad += not ok
        print(f"{'ok  ' if ok else 'BAD '} the fixture as it stands: exit {code}, {len(v)} lines, findings on {found or 'none'}")
        for i, (line, what, change, regen) in enumerate(mutations(base)):
            d = pathlib.Path(tmp) / f"m{i:02d}"
            shutil.copytree(FIXTURE, d)
            for m in mutations(d)[i:i + 1]:
                m[2]()
            if regen:
                run([str(HERE / "extract.py"), str(d / "use_case_model.md"), "--write-survey"], env)
            code, out = run([str(HERE / "check_model.py"), str(d / "use_case_model.md")], env)
            v = verdicts(out)
            found = sorted(k for k, x in v.items() if x == "FINDING")
            ok = code == 1 and found == [line]
            bad += not ok
            print(f"{'ok  ' if ok else 'BAD '} {what}: exit {code}, findings on {', '.join(found) or 'none'} (expected {line} alone)")
            if not ok:
                print("\n".join("      " + l for l in out.splitlines() if l.startswith("      - ")))
        code, out = run([str(HERE / "check_model.py"), str(REFUSED), "--legacy"], env)
        v = verdicts(out)
        found = sorted(k for k, x in v.items() if x == "FINDING")
        four = {"M16", "M19–M20", "M21", "M22"}
        ok = code == 1 and four <= set(found)
        bad += not ok
        print(f"{'ok  ' if ok else 'BAD '} the one-file fixture: exit {code}, findings on {', '.join(found)}; "
              f"the four lines M16, M19–M20, M21, M22 {'all refused' if four <= set(found) else 'NOT all refused'}")
    print(f"{'every case as expected' if not bad else f'{bad} case(s) not as expected'}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
