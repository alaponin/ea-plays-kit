#!/usr/bin/env python3
"""Shared custody-stamp helpers (CH-01 WP-A, ADR-069).

Projectors accept `--custody GATED:<sha>|UNGATED` — a CLI INPUT, never an env/clock read,
so projector purity and byte-reproducibility are preserved (invariant 3 / DP-6). `kit gen`
supplies the value from `kit gate resolve`; a direct projector call defaults to UNGATED
(absence of information is never silently credible).
"""
from __future__ import annotations


def add_arg(ap) -> None:
    """Register `--custody` on a projector's argparse (default UNGATED = backwards compatible)."""
    ap.add_argument("--custody", default="UNGATED",
                    help="CH-01 custody stamp: GATED:<report-sha> | UNGATED")


def line(custody: str) -> str:
    """The one provenance-header line every Layer-2 file carries."""
    return f"# custody:        {custody or 'UNGATED'}\n"


def is_ungated(custody: str) -> bool:
    return not (custody or "").startswith("GATED:")


def description_prefix(custody: str) -> str:
    """L3-visible marker for form/userview `description` (rides through to the deployed
    artefact — the floor for G1 'the instance shows its own custody state'). Empty when gated."""
    return "[UNGATED build] " if is_ungated(custody) else ""
