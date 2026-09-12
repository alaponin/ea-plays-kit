# KP2 play 5.8 — Summarise bus health and flag anomalies from the logs · fixture input

**Consumes:** B33 — from [`tests/progressa.md`](../../../progressa.md) and [`tests/kp2/progressa-supplement.md`](../../progressa-supplement.md).
**Primary skill:** `gif-bus-monitor` · also runs: —
**Produces:** B35 — Bus-health summary and anomaly list

## What the learner types

Below are operational logs from [country X]'s interoperability bus, containing ONLY exchange metadata — timestamp, calling subsystem, called service, success/failure, latency — and NO citizen personal data [paste the metadata logs]. Produce a health summary: (1) volume and success/failure rates by service; (2) any service with a rising failure rate or latency; (3) anomalies — unusual spikes, a caller that has not called this service before, off-hours surges — each flagged as a QUESTION for a human to investigate, not a conclusion; (4) the top 3 things the Operating Authority should look at this week; (5) a one-paragraph compliance note for the quarterly Steering Committee report — which members show sustained failure or unusual behaviour that warrants a conformance re-check. Do not infer anything about individual citizens; if the logs appear to contain personal data, stop and flag that as a data-protection issue. Output: the health summary plus the prioritised investigate list.

## What the fixture supplies

Country: **Progressa** · Sector: **Education**. Put these two values in the place of each
placeholder in brackets above. The named input is B33. A0 §1–§7 come from
`tests/progressa.md`; A0 §8–§10, the once-only scenario and the federation identifiers come
from `tests/kp2/progressa-supplement.md`. Paste those sections without a change.

If this play consumes a B-artefact from an earlier play, run that play on Progressa first.
The chain is in
[`shared/workbook-chain-kp2.md`](../../../../plugins/ea-plays/shared/workbook-chain-kp2.md).
This is the KP2 play; KP1 has a play with the same id that makes an A-artefact.
