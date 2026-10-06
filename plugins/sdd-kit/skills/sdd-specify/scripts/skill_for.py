#!/usr/bin/env python3
"""skill_for.py — which skill the register names for a row, read from the row's `skill` cell.

    python3 skill_for.py <row> [<row> ...] [--all] [--slots F] [--kit K] [--marketplace M]

WHAT IT READS. The register of the delivery kit, `templates/spec/slots.yaml` under the kit's root
`K` (or the file `--slots` names), and in it, for each row asked, two cells: `standard` and
`skill`. It reads no other cell and holds nothing of any row.

WHAT IT PRINTS, one line for each row asked, in one of three forms:

    <row> · the skill <plugin:skill> · <its SKILL.md>          the cell names a skill
    <row> · none · <why>                                       the method gives the thing no skill
    <row> · absent · owner <owner> · <the cell's reason>       the cell is not filled yet

A cell reading `plugin:skill` names the skill; the program looks for it in the marketplace `M`, at
`plugins/<plugin>/skills/<skill>/SKILL.md`, or, where `M` is the root of the plugin itself (the
default in sdd-kit), at `skills/<skill>/SKILL.md`, and prints that path relative to `M`, and says so where it is not there, or where it is there
and its description says it is not yet written. A cell reading absent, on a row whose standard also
reads absent, is `none`: the target state of the method gives a skill to each standard that governs
a thing a person writes, and to nothing else (the design of 25 September 2026,
`_working/2026-09-25_the_target_state/04_TARGET_STATE.md`, section 2, in the estate's root), so a
thing no standard governs has no skill of the method, whatever the cell's owner may later write. A
cell reading absent on a row that has a standard is `absent`, with the owner and the reason the cell
gives.

Exit: 0 every row asked names a skill that is there and written, or has none · 1 some row reads
absent, or names a skill that is not there or not yet written · 2 could not run.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

import yaml

# sdd-kit: this file is at skills/sdd-specify/scripts/; the skill's own folder, one up, carries its copy of the
# kit and the standards (scripts/sync-skills.sh), so the skill works when installed on its own.
PLUGIN_ROOT = pathlib.Path(__file__).resolve().parents[1]
KIT = PLUGIN_ROOT / "kit"
MARKETPLACE = PLUGIN_ROOT
SKILL = re.compile(r"^([a-z0-9][a-z0-9-]*):([a-z0-9][a-z0-9-]*)$")
NOT_YET = "not yet written"


def one_line(s) -> str:
    return " ".join(str(s or "").split())


def description_of(path: pathlib.Path) -> str:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return ""
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return ""
    return one_line(fm.get("description"))


def read(row: dict, marketplace: pathlib.Path) -> tuple[str, bool]:
    """(the line after the row's number, whether the row resolved)."""
    cell = row.get("skill")
    std = row.get("standard")
    has_standard = isinstance(std, dict) and bool(std.get("code"))
    if isinstance(cell, str):
        m = SKILL.match(cell.strip())
        if not m:
            return f"absent · the cell reads {cell!r}, which is not of the form plugin:skill", False
        plugin, skill = m.groups()
        path = marketplace / "plugins" / plugin / "skills" / skill / "SKILL.md"
        manifest = marketplace / ".claude-plugin" / "plugin.json"
        if not (marketplace / "plugins").is_dir() and manifest.is_file():
            import json
            if json.loads(manifest.read_text(encoding="utf-8")).get("name") == plugin:
                path = marketplace / "skills" / skill / "SKILL.md"
        elif not (marketplace / "plugins").is_dir() and (marketplace / "SKILL.md").is_file():
            path = marketplace.parent / skill / "SKILL.md"   # one skill's own folder: siblings beside it
        try:
            shown = path.resolve().relative_to(marketplace.resolve()).as_posix()
        except ValueError:
            shown = str(path)
        if not path.is_file():
            return f"the skill {cell} · not there: no {shown}", False
        if description_of(path).lower().startswith(NOT_YET):
            return f"the skill {cell} · {shown} · its description says it is {NOT_YET}", False
        return f"the skill {cell} · {shown}", True
    if isinstance(cell, dict) and "absent" in cell:
        reason = one_line(cell.get("absent"))
        owner = one_line(cell.get("owner")) or "none named"
        if not has_standard:
            return (f"none · no standard of the method governs this thing, so the method gives it "
                    f"no skill; the register's cell reads absent, owner {owner}"), True
        return f"absent · owner {owner} · {reason}", False
    return "absent · the row carries no skill cell", False


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("rows", nargs="*", help="the rows as the register writes them, e.g. 01, 08a, 09")
    ap.add_argument("--all", action="store_true", help="every row of the register, in its order")
    ap.add_argument("--kit", type=pathlib.Path, default=KIT)
    ap.add_argument("--slots", type=pathlib.Path, default=None)
    ap.add_argument("--marketplace", type=pathlib.Path, default=MARKETPLACE)
    a = ap.parse_args(argv)
    slots = a.slots or a.kit / "templates" / "spec" / "slots.yaml"
    try:
        reg = yaml.safe_load(slots.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError) as exc:
        print(f"skill_for.py: could not run: {exc}", file=sys.stderr)
        return 2
    rows = {str(r.get("n")): r for r in reg.get("slots") or [] if isinstance(r, dict)}
    asked = list(rows) if a.all else a.rows
    if not asked:
        print("skill_for.py: could not run: name a row, or --all", file=sys.stderr)
        return 2
    rc = 0
    print(f"the register {slots}")
    for n in asked:
        if n not in rows:
            print(f"{n} · no such row in the register")
            rc = 1
            continue
        line, ok = read(rows[n], a.marketplace)
        print(f"{n} · {line}")
        rc = rc or (0 if ok else 1)
    return rc


if __name__ == "__main__":
    sys.exit(main())
