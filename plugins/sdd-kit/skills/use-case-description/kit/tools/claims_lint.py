#!/usr/bin/env python3
"""claims_lint.py — gate verdicts are computed, never authored (ADR-065 / Job B #3).

The 8077 counterfeit wore the method's vocabulary in a YAML comment: "re-authored through the
gated upstream method … 0 open decisions … realism-anchored to the TADAT Field Guide 2019" —
while no gate had run. This lint makes that move fail validation: **gate-verdict vocabulary in
an authored L1 model file is an error.** The only valid carriers of such claims are computed
artefacts — the realism trace (`kit diff-reference`), the gate report, lint outputs.

Scope (v0.1): L1 model files (*.app.yaml) — where the counterfeit header lived. The standalone
CLI accepts any text file for manual sweeps. Pack-doc scanning (SOURCING.md etc.) is designed
into the Phase-2 pack authoring, not bolted on here.

Exemption (loud, auditable, never silent): a file whose first 30 lines carry `NEGATIVE CONTROL`
or `RETRACTED` is a frozen exhibit — it may describe retracted claims — and is reported as
exempt rather than scanned. The marker itself is the audit trail.

Usage:
    claims_lint.py <file> [file ...]

Exit codes: 0 clean/exempt · 1 violations · 3 input error.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

TOOL_VERSION = "0.1.0"

# The gate-verdict vocabulary. Tight by design (zero collisions in the honest corpus,
# checked 2026-07-11); extend deliberately, never casually.
CLAIM_PATTERNS = [
    (re.compile(r"\b(0|zero)\s+open\s+decisions\b", re.I), "0 open decisions"),
    (re.compile(r"\brealism[- ]anchored\b", re.I), "realism-anchored"),
    (re.compile(r"\bverified\s+against\s+the\s+source\b", re.I), "verified against the source"),
    # KR-11 (12 Aug 2026): `\b` keeps UNGATED (the stamp) unmatched, but a hyphen IS a word
    # boundary, so the bare pattern also matched `approval-gated` — a value in the
    # `change_class` vocabulary GOV §3.2 mandates. A model naming its own change classes was
    # failing a lint about counterfeit gate claims. `(?<!-)` absorbs the hyphenated compound
    # (approval-gated, non-gated) while the bare claim word — "the gated upstream method" —
    # is still caught, which is the only thing this pattern was ever about.
    (re.compile(r"(?<!-)\bgated\b", re.I), "gated"),
]

EXEMPT_MARKERS = ("NEGATIVE CONTROL", "RETRACTED")
EXEMPT_HEAD_LINES = 30


def lint_text(text: str) -> tuple[list[tuple[int, str, str]], str | None]:
    """Return (violations, exempt_reason). Pure — no I/O — so tests call it directly.

    violations: [(1-based line, matched vocabulary, the line text)]
    exempt_reason: the marker found in the head, or None.
    """
    lines = text.splitlines()
    head = "\n".join(lines[:EXEMPT_HEAD_LINES])
    for marker in EXEMPT_MARKERS:
        if marker in head:
            return [], marker
    violations = []
    for i, line in enumerate(lines, 1):
        for pat, label in CLAIM_PATTERNS:
            if pat.search(line):
                violations.append((i, label, line.strip()))
    return violations, None


def lint_file(path: pathlib.Path) -> int:
    """0 clean/exempt · 1 violations. Prints findings."""
    text = path.read_text(encoding="utf-8", errors="replace")
    violations, exempt = lint_text(text)
    if exempt:
        print(f"claims-lint: {path} — EXEMPT ({exempt} exhibit; frozen, not scanned)")
        return 0
    if not violations:
        print(f"claims-lint: {path} — OK (no authored gate-verdict claims)")
        return 0
    print(f"claims-lint: {path} — FAIL: gate verdicts are computed artefacts "
          f"(realism trace, gate report), never author prose (ADR-065):")
    for ln, label, snippet in violations:
        print(f"  ERR  line {ln}: authored claim {label!r}: {snippet[:100]}")
    return 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+", type=pathlib.Path)
    a = ap.parse_args()
    rc = 0
    for f in a.files:
        if not f.exists():
            print(f"claims-lint: not found: {f}")
            return 3
        rc = lint_file(f) or rc
    return rc


if __name__ == "__main__":
    sys.exit(main())
