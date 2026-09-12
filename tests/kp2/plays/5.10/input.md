# KP2 play 5.10 — Map your framework's sector-portable vs sector-specific parts for a new sector · fixture input

**Consumes:** B28, B22, B23 — from [`tests/progressa.md`](../../../progressa.md) and [`tests/kp2/progressa-supplement.md`](../../progressa-supplement.md).
**Primary skill:** `ea-method-runner` · also runs: —
**Produces:** B37 — Sector-portability map

## What the learner types

I built a Government Interoperability Framework for [country X] in the education sector and want to extend it to [new sector — e.g. health]. Produce a sector-portability map. (1) REUSED UNCHANGED — list what carries over without change: the four-layer model, the decree pattern, the governance (tiers, RACI, Operating Authority), the standards portfolio, the bus and federation. For each, a one-line note on why it carries. (2) NEW FOR THIS SECTOR — list what must be built: the semantic layer (the sector's vocabularies and code lists — name the likely published standards for [new sector]), and the specific exchanges/services this sector needs. (3) THE BUSINESS CASE — a short statement a minister can read: here is the large platform we reuse, here is the small sector-specific part we build, and therefore this sector costs far less than the first. Then (4) place [new sector] in the usual sequencing — first wave (tax, civil registration, business register, health: foundational, high-volume) or second wave (education, justice, social protection, customs) — and say why. Output: the two lists, the wave placement, and the business-case statement.

## What the fixture supplies

Country: **Progressa** · Sector: **Education**. Put these two values in the place of each
placeholder in brackets above. The named input is B28, B22, B23. A0 §1–§7 come from
`tests/progressa.md`; A0 §8–§10, the once-only scenario and the federation identifiers come
from `tests/kp2/progressa-supplement.md`. Paste those sections without a change.

If this play consumes a B-artefact from an earlier play, run that play on Progressa first.
The chain is in
[`shared/workbook-chain-kp2.md`](../../../../plugins/ea-plays/shared/workbook-chain-kp2.md).
This is the KP2 play; KP1 has a play with the same id that makes an A-artefact.
