# Play 2.6 — Turn AS-IS notes into a scored gap analysis · fixture input

**Consumes:** A13, A11 — from [`tests/progressa.md`](../../progressa.md).
**Primary skill:** `bdat-assessor`
**Produces:** A14 — Scored gap analysis

## What the learner types

Below are my current-state (AS-IS) notes for [name the sector or body] in [country X], organised by layer [paste your Business, Data, Application, Technology notes]. Produce a scored gap analysis. (1) Identify gaps, looking on purpose for the four common ones: duplicate registries (more than one owner of a data domain), orphan systems (applications mapped to no capability), point-to-point integration with no shared data exchange, and capabilities or domains with no clear owner. (2) For each gap, give: the layer, a one-line description, severity (Low / Medium / High — based on cost, citizen burden and risk), effort to close (Low / Medium / High), and a priority that favours high impact where movement is possible. (3) Give a per-layer maturity score (1–5). (4) List the three highest-priority gaps with a one-paragraph rationale each. Output: a gap table, a per-layer maturity line, and the top-three rationale.

## What the fixture supplies

Country: **Progressa** · Sector: **Education**. Put these two values in the place of each
placeholder in brackets above. The named input is A13, A11 of `tests/progressa.md`. Paste
those sections without a change.

If this play consumes an artefact from an earlier play, such as A1, A3 or A22, run that play
on Progressa first. The chain is in
[`shared/workbook-chain.md`](../../../plugins/ea-plays/shared/workbook-chain.md).
