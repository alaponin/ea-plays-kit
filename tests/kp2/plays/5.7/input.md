# KP2 play 5.7 — Build the demonstration-to-production gap checklist · fixture input

**Consumes:** B32, B28 — from [`tests/progressa.md`](../../../progressa.md) and [`tests/kp2/progressa-supplement.md`](../../progressa-supplement.md).
**Primary skill:** `ea-method-runner` · also runs: —
**Produces:** B34 — Demonstration-to-production gap checklist

## What the learner types

Build a demonstration-to-production gap checklist for [country X]'s X-Road federation. The demonstration runs on a single VM with sandboxed containers and a Test CA; production must carry real citizen data at scale. For each area, state what the demonstration has, what production requires, and roughly when in the four-phase plan it should be delivered: (1) hosting — single VM vs separate sized hosts; (2) certification authority — Test CA vs real CA; (3) availability — single instance vs high availability and redundancy; (4) monitoring and alerting; (5) capacity for expected transaction volumes; (6) operational support hours; (7) security hardening and audit. For each, note that the configuration shape (subsystem registrations, service descriptions) does NOT change — only scale, resilience and operations do. Mark cost-bearing items for the cost frame. Output: a gap checklist (area / demo / production / phase / cost-bearing?) plus a one-line 'do not ship the demo as production' caution.

## What the fixture supplies

Country: **Progressa** · Sector: **Education**. Put these two values in the place of each
placeholder in brackets above. The named input is B32, B28. A0 §1–§7 come from
`tests/progressa.md`; A0 §8–§10, the once-only scenario and the federation identifiers come
from `tests/kp2/progressa-supplement.md`. Paste those sections without a change.

If this play consumes a B-artefact from an earlier play, run that play on Progressa first.
The chain is in
[`shared/workbook-chain-kp2.md`](../../../../plugins/ea-plays/shared/workbook-chain-kp2.md).
This is the KP2 play; KP1 has a play with the same id that makes an A-artefact.
