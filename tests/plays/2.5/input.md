# Play 2.5 — Draft a first-pass BDAT skeleton for a sector · fixture input

**Consumes:** A0 §6, A5, A9, A12 — from [`tests/progressa.md`](../../progressa.md).
**Primary skill:** `bdat-assessor` · also runs: `ea-institution-mapper`
**Produces:** A13 — Sector BDAT skeleton

## What the learner types

Below are the main public bodies in [country X]'s [sector] sector and what each does [paste a short list: body name, mandate, known systems, known registries]. Produce a first-pass BDAT skeleton. (1) Classification: assign each body a PAERA taxonomy type (policy unit / regulatory agency / service-delivery authority / state registry / shared platform). (2) Business layer: list the main capabilities and, for each, the single body that should own it; list the main citizen-facing services on top. (3) Data layer: list the main data domains and, for each, the single owning body; flag any domain that appears to have more than one owner as a possible duplicate registry. (4) Application layer: map each known system to a capability and the data domains it uses; flag any system that maps to no capability. (5) Technology layer: list the shared platforms and standards. Output: five sections, with all duplicate-owner and orphan-system conflicts flagged at the end.

## What the fixture supplies

Country: **Progressa** · Sector: **Education**. Put these two values in the place of each
placeholder in brackets above. The named input is A0 §6, A5, A9, A12 of `tests/progressa.md`. Paste
those sections without a change.

If this play consumes an artefact from an earlier play, such as A1, A3 or A22, run that play
on Progressa first. The chain is in
[`shared/workbook-chain.md`](../../../plugins/ea-plays/shared/workbook-chain.md).
