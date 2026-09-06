# Play 5.3 — Sequence your national rollout into waves · fixture input

**Consumes:** A26, A28, BB status register — from [`tests/progressa.md`](../../progressa.md).
**Primary skill:** `ea-method-runner` · also runs: `bb-landscape-check`
**Produces:** A31 — National rollout wave plan

## What the learner types

I am planning a national EA rollout for [country X] across these sectors [list them, with the flagship outcome each has if known]. Sequence it into waves. (1) Wave 1: recommend the foundation sector — the one with the clearest flagship — and note that Wave 1 also stands up the permanent team, the governance board, and the first shared platforms (identity, data exchange). (2) Waves 2 onward: order the remaining sectors, and for each name what it REUSES from earlier waves (which shared platforms) versus what is new. (3) The national scorecard: the few metrics to report quarterly (sectors live, re-use rate, shared platforms in place). Output: a wave sequence with reuse noted per wave, plus the scorecard metrics.

## What the fixture supplies

Country: **Progressa** · Sector: **Education**. Put these two values in the place of each
placeholder in brackets above. The named input is A26, A28, BB status register of `tests/progressa.md`. Paste
those sections without a change.

If this play consumes an artefact from an earlier play, such as A1, A3 or A22, run that play
on Progressa first. The chain is in
[`shared/workbook-chain.md`](../../../plugins/ea-plays/shared/workbook-chain.md).
