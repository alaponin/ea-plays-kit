#!/usr/bin/env python3
"""standard_text — the words of a standard, taken out of its document at the moment of use.

    python3 standard_text.py <the standard's .docx or .md> [--section N]

Prints the document's text in body order: a heading with as many `#` as its level, every other
paragraph as it stands, and every table row as `| cell | cell |`. With `--section N`, only the
section whose heading begins with that number (`9`, `9.1`, `11`), down to the next heading at
the same level or above. The assist moment reads the standard this way, part by part, so that no
line of it is ever copied into the skill.

Exit: 0 printed · 1 the section is not in the document · 2 could not run.
"""
from __future__ import annotations

import argparse
import pathlib
import sys

import re


def md_body(path: pathlib.Path) -> list[tuple[int, str]]:
    """(heading level or 0, text) for every line of a standard bundled as Markdown (sdd-kit):
    a heading `## 9  Title` is level 1, `### 9.1 Title` level 2 and so on, as in the Word
    edition, where the document's title is not a numbered heading."""
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m and len(m.group(1)) >= 2:
            out.append((len(m.group(1)) - 1, m.group(2).strip()))
        else:
            out.append((0, line))
    return out


def body(path: pathlib.Path) -> list[tuple[int, str]]:
    """(heading level or 0, text) for every block of the document, in order."""
    if path.suffix.lower() == ".md":
        return md_body(path)
    try:
        from docx import Document
        from docx.oxml.ns import qn
    except ImportError:
        print("standard_text: could not run: python-docx is not installed", file=sys.stderr)
        sys.exit(2)
    d = Document(str(path))
    out = []
    for el in d.element.body.iterchildren():
        if el.tag == qn("w:p"):
            t = "".join(x.text or "" for x in el.iter(qn("w:t")))
            if not t.strip():
                continue
            ppr = el.find(qn("w:pPr"))
            style = ""
            if ppr is not None and ppr.find(qn("w:pStyle")) is not None:
                style = ppr.find(qn("w:pStyle")).get(qn("w:val")) or ""
            lvl = int(style[-1]) if style.startswith("Heading") and style[-1:].isdigit() else 0
            out.append((lvl, t))
        elif el.tag == qn("w:tbl"):
            for tr in el.iter(qn("w:tr")):
                cells = [" ".join("".join(x.text or "" for x in p.iter(qn("w:t"))) for p in tc.iter(qn("w:p"))).strip()
                         for tc in tr.iter(qn("w:tc"))]
                out.append((0, "| " + " | ".join(cells) + " |"))
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="standard_text.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("docx", type=pathlib.Path)
    ap.add_argument("--section")
    a = ap.parse_args(argv)
    if not a.docx.is_file():
        print(f"standard_text: could not run: {a.docx} is not there", file=sys.stderr)
        return 2
    blocks = body(a.docx)
    if a.section:
        start = next((i for i, (lv, t) in enumerate(blocks)
                      if lv and (t.split()[0].rstrip('.') == a.section if t.split() else False)), None)
        if start is None:
            print(f"standard_text: {a.docx.name} has no heading beginning {a.section}", file=sys.stderr)
            return 1
        level = blocks[start][0]
        end = next((i for i in range(start + 1, len(blocks)) if blocks[i][0] and blocks[i][0] <= level), len(blocks))
        blocks = blocks[start:end]
    for lv, t in blocks:
        print(("#" * lv + " " if lv else "") + t)
    return 0


if __name__ == "__main__":
    sys.exit(main())
