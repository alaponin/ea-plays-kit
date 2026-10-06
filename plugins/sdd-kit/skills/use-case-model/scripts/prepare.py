#!/usr/bin/env python3
"""prepare — the machine half of the prepare moment: the model file and one use case file each.

    python3 prepare.py <model folder> --system NAME [--use-case ID ...] [--answers FILE]
                       [--template FILE] [--kit-root DIR]

THE MODEL FILE. Where the folder holds no `use_case_model.md`, one is written from the skeleton
in references/model-shape.md (between its two skeleton markers), with the system's name and,
in `written_to`, the edition and checksum the template's head gives. An existing model file is
never touched.

THE USE CASE FILES. For every identifier given, `use_cases/<ID>.md` is written as a copy of the
kit's template of row 03, `templates/spec/artefacts/03_use_case_model.md` under the kit's root,
with the `Answer` cell of the identifier's row filled and a heading for the one-line
description added beneath the header. An existing use case file is never overwritten.

THE ANSWERS (--answers). A YAML file mapping each identifier to the answers of its header, by
the field names the template carries, and to its one-line description:

    UC-02:
      Name: Apply for a plot
      Level: user goal
      description: The resident applies for a plot for the season and learns whether it is accepted.

A field name the template does not carry is refused, so that no field list is held here: the
names are the template's. Answers already filled are replaced only with --force.

Nothing upstream is written: the requirements, the entity model, the glossary, the register of
business rules and the catalogue of settings are named in the model file's head by path, or as
absent with a finding and an owner, and are written by their own rows.

Exit: 0 written · 1 refused, nothing written · 2 could not run.
"""
from __future__ import annotations

import argparse
import os
import pathlib
import re
import sys

import yaml

HERE = pathlib.Path(__file__).resolve().parent
SKILL = HERE.parent
# sdd-kit: the kit stands three folders up from this file, at the plugin's root.
KIT_ROOT = pathlib.Path(os.environ.get("SDD_KIT_ROOT", str(pathlib.Path(__file__).resolve().parents[3] / "kit")))
TEMPLATE_REL = pathlib.Path("templates/spec/artefacts/03_use_case_model.md")
DESCRIPTION = "## One-line description"


def template_head(text: str) -> dict:
    m = re.match(r"^\s*<!--\n(.*?)\n-->", text, re.S)
    return (yaml.safe_load(m.group(1)) or {}) if m else {}


def skeleton() -> str:
    t = (SKILL / "references" / "model-shape.md").read_text(encoding="utf-8")
    m = re.search(r"<!-- skeleton:begin -->\s*```markdown\n(.*?)```\s*<!-- skeleton:end -->", t, re.S)
    if not m:
        raise SystemExit("prepare: references/model-shape.md carries no skeleton between its markers")
    return m.group(1)


def fill(text: str, field: str, answer: str, force: bool) -> tuple[str, bool]:
    """Set the Answer cell of the header row for `field`. Returns the text and whether the row was found."""
    out, found = [], False
    for line in text.split("\n"):
        cells = line.split("|")
        if line.startswith("| ") and len(cells) >= 6 and cells[1].strip() == field:
            found = True
            if cells[-2].strip() and not force:
                out.append(line)
                continue
            cells[-2] = f" {answer} "
            line = "|".join(cells)
        out.append(line)
    return "\n".join(out), found


def field_names(text: str) -> list[str]:
    names, on = [], False
    for line in text.split("\n"):
        c = [x.strip() for x in line.split("|")]
        if len(c) >= 6 and c[1] == "Field":
            on = True
            continue
        if on:
            if not line.startswith("|"):
                break
            if not re.match(r"^[-: ]*$", c[1]):
                names.append(c[1])
    return names


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="prepare.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folder", type=pathlib.Path)
    ap.add_argument("--system", required=True)
    ap.add_argument("--use-case", action="append", default=[])
    ap.add_argument("--answers", type=pathlib.Path)
    ap.add_argument("--template", type=pathlib.Path)
    ap.add_argument("--kit-root", type=pathlib.Path, default=KIT_ROOT)
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args(argv)

    tpl = a.template or (a.kit_root / TEMPLATE_REL)
    if not tpl.is_file():
        print(f"prepare: could not run: the template {tpl} is not there", file=sys.stderr)
        return 2
    ttext = tpl.read_text(encoding="utf-8")
    head = template_head(ttext)
    names = field_names(ttext)
    if not names:
        print(f"prepare: could not run: the template {tpl} carries no record header table", file=sys.stderr)
        return 2
    answers = yaml.safe_load(a.answers.read_text(encoding="utf-8")) if a.answers else {}
    ids = list(dict.fromkeys(a.use_case + list(answers or {})))
    identifier = next((n for n in names if n.lower().startswith("identifier")), names[0])

    refusals = []
    for uc, vals in (answers or {}).items():
        for k in (vals or {}):
            if k != "description" and k not in names:
                refusals.append(f"{uc}: the template carries no field named {k!r}; its fields are "
                                f"{', '.join(names)}")
    if refusals:
        print("prepare: REFUSED, nothing written:")
        for r in refusals:
            print(f"  - {r}")
        return 1

    a.folder.mkdir(parents=True, exist_ok=True)
    model = a.folder / "use_case_model.md"
    if not model.exists():
        sk = skeleton().replace("{system}", a.system)
        sk = sk.replace("{edition}", str(head.get("edition", ""))).replace("{sha256}", str(head.get("sha256", "")))
        model.write_text(sk, encoding="utf-8")
        print(f"written {model} from the skeleton")
    else:
        print(f"kept    {model}")
    ucdir = a.folder / "use_cases"
    ucdir.mkdir(exist_ok=True)
    for uc in ids:
        p = ucdir / f"{uc}.md"
        new = not p.exists()
        text = ttext if new else p.read_text(encoding="utf-8")
        text, _ = fill(text, identifier, uc, a.force)
        vals = (answers or {}).get(uc) or {}
        for k, v in vals.items():
            if k == "description":
                continue
            text, _ = fill(text, k, str(v), a.force or new)
        if DESCRIPTION not in text:
            text = text.rstrip("\n") + f"\n\n{DESCRIPTION}\n\n"
        if vals.get("description"):
            body, _, rest = text.partition(DESCRIPTION)
            if not rest.strip() or a.force or new:
                text = body + DESCRIPTION + "\n\n" + str(vals["description"]).strip() + "\n"
        if new or text != p.read_text(encoding="utf-8"):
            p.write_text(text, encoding="utf-8")
            print(f"{'written' if new else 'filled '} {p}")
        else:
            print(f"kept    {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
