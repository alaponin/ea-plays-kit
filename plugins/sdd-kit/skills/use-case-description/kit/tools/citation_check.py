#!/usr/bin/env python3
"""citation_check — the citation column: every build parameter cites its decision, or logs an assumption.

Closes the §2.4 SECOND failure class (the DM Class-B leak): the build re-derived values the spec
had already decided, without citation — matching values became unauditable luck, and two silently
diverged. This enforces the one column that fixes it: every parameter, state set and rule in a
build realization (FIS) names its decision id, or carries an explicit ASSUMPTION. 100% or exit 1.

Referential integrity against the decision inventory: a cited decision must exist and be VERIFIED —
a build may not rest on a DRAFT, an open TO_CONFIRM, or a WAIVED decision.

    kit citation-check <realization.yaml> --decisions <design/decisions.yaml>

realization.yaml shape:
    realization: { slice: <id> }
    items:
      - { ref: escalation.offset_1, kind: parameter, value: "7d", decision: DR-DM-005 }
      - { ref: ws.timeout,          kind: parameter, value: "30s", assumption: "engineering default, no SoT" }
"""
from __future__ import annotations

import argparse
import pathlib
import sys

import yaml


def _load(p): return yaml.safe_load(pathlib.Path(p).read_text(encoding="utf-8"))


def citation_check(realization: dict, decisions: dict) -> list[str]:
    """Return a list of error strings. Empty == every item is cited or an explicit assumption."""
    errors: list[str] = []
    by_id = {d.get("id"): d for d in (decisions or {}).get("decisions", []) or []}
    for i, it in enumerate(realization.get("items", []) or []):
        ref = it.get("ref", f"items[{i}]")
        has_dec = "decision" in it and it["decision"]
        has_asm = "assumption" in it and str(it.get("assumption") or "").strip()
        if has_dec and has_asm:
            errors.append(f"{ref}: carries BOTH a decision and an assumption — pick one")
        elif not has_dec and not has_asm:
            errors.append(f"{ref}: UNCITED — names no decision id and logs no assumption (Class-B leak)")
        elif has_dec:
            did = it["decision"]
            d = by_id.get(did)
            if d is None:
                errors.append(f"{ref}: cites {did} which is not in the decision inventory")
            elif d.get("status") != "VERIFIED":
                errors.append(f"{ref}: cites {did} but its status is {d.get('status')} (a build needs a VERIFIED decision)")
    return errors


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("realization", type=pathlib.Path)
    ap.add_argument("--decisions", type=pathlib.Path, required=True)
    a = ap.parse_args()
    for p in (a.realization, a.decisions):
        if not p.exists():
            print(f"citation-check: not found: {p}"); return 3
    real = _load(a.realization) or {}
    errors = citation_check(real, _load(a.decisions) or {})
    n = len(real.get("items", []) or [])
    cited = n - len(errors)
    for e in errors:
        print(f"  ERR {e}")
    pct = 100.0 * cited / n if n else 100.0
    print(f"citation-check: {cited}/{n} items clean ({pct:.0f}%)")
    if errors:
        print(f"citation-check: FAIL — {len(errors)} uncited/invalid"); return 1
    print("citation-check: OK — 100% cited-or-assumption"); return 0


if __name__ == "__main__":
    sys.exit(main())
