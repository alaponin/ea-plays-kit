"""observation.py — nothing-to-observe is an outcome, not a pass.

The single most common way this toolkit has lied is by reporting a green pass over an empty
population. Ten of the seventy-four recorded failures are this one shape:

  * `diff-reference` with zero in-scope anchors hardcoded BOTH percentages to 100.0 and
    printed CLEAN — the clearest empty-input pass in the kit.
  * `drift` on a missing build directory returned `in_sync 0` and exit 0, because `all()`
    over an empty collection is True. A missing build passed.
  * `adoption` with zero measures initialised its worst ratio to 1.0 and printed `lowest 100%`.
  * `zone-check` found no rows for its entity, returned immediately, and printed
    `0 blocking, 0 reported` — so an app naming its entity anything else was never checked.
  * `spec-lint` over a subjects file with no subjects printed `0 gap(s), 0 weak`.

None of these is a bug in the arithmetic. Each is arithmetic applied to nothing, and the
result of dividing by nothing was reported as success. For a country implementer this is the
most dangerous class in the whole catalogue, because a NEW application is mostly empty: their
first run is the run where every one of these fires at once.

Two verbs already got this right and are the model. `ui-probe` reports UNPROVEN for a list with
no rows rather than passing it. `totality` refuses outright when there is no `generated/` —
"an app that generated nothing has no transmission to check". This module makes that idea
shared vocabulary rather than two good instincts.

THE RULE. A check has FIVE outcomes, never two:

    proved            it was looked at and it holds
    refused           it was looked at and it does not hold
    nothing to observe  it ran, and the thing it grades was empty      <- exit code NOTHING
    not run           it never executed
    does not apply    the app legitimately has no such thing

`nothing to observe` is NOT `does not apply`. "This app declares no scenarios" is the latter and
is carried by the existing `applicable` flag. "This app declares scenarios and the suite is
empty" is the former, and it must never read as evidence.

A missing INPUT is already handled upstream — the gate's input-conditional plan records no check
at all when a file is absent. What this module addresses is the narrower and more dangerous case:
the input is present, the check runs, and there is nothing inside it.
"""
from __future__ import annotations

# Distinct from 0 (proved) and from 1/2 (refused). Chosen to match `totality`, which has
# refused on exit 3 since it was written.
NOTHING = 3


def nothing_to_observe(verb: str, what: str, why: str = "") -> int:
    """Print the standard line and return the standard exit code.

    `what` names the empty population — "no in-scope anchors", "no rows for entity X".
    `why` says what a reader should do about it. Both are read by someone who does not know
    this toolkit, so neither may use its vocabulary.
    """
    tail = f" {why}" if why else ""
    print(f"{verb}: NOTHING TO OBSERVE — {what}.{tail}")
    print(f"{verb}: this is not a pass. Nothing was measured, so nothing is proven.")
    return NOTHING
