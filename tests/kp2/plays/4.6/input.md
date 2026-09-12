# KP2 play 4.6 — Map a real sector data source through bronze/silver/gold onto the bus · fixture input

**Consumes:** B23 — from [`tests/progressa.md`](../../../progressa.md) and [`tests/kp2/progressa-supplement.md`](../../progressa-supplement.md).
**Primary skill:** `gif-semantic-map` · also runs: `gif-openapi-gen`
**Produces:** B25 — Bronze/silver/gold source map

## What the learner types

I want to put a real data source onto [country X]'s interoperability bus: [describe the source — e.g. Giga school data, or the national school registry; name its schema/fields if known]. Plan its bronze/silver/gold pipeline and its path onto the bus. (1) BRONZE — what raw data is ingested as-is, and what is retained for audit. (2) SILVER — the cleaning and validation rules, the conformance to a schema and semantic map, and how bad/duplicate records are flagged (note the identifier used for de-duplication as [confirm: verify uniqueness]). (3) GOLD — the published authoritative dataset and the service it backs. (4) ONTO THE BUS — the OpenAPI contract, the X-Road service description, the trust-zone security, and the data-protection basis required. Output: the pipeline plan stage by stage, plus a checklist of what must be confirmed against the real source before go-live.

## What the fixture supplies

Country: **Progressa** · Sector: **Education**. Put these two values in the place of each
placeholder in brackets above. The named input is B23. A0 §1–§7 come from
`tests/progressa.md`; A0 §8–§10, the once-only scenario and the federation identifiers come
from `tests/kp2/progressa-supplement.md`. Paste those sections without a change.

If this play consumes a B-artefact from an earlier play, run that play on Progressa first.
The chain is in
[`shared/workbook-chain-kp2.md`](../../../../plugins/ea-plays/shared/workbook-chain-kp2.md).
This is the KP2 play; KP1 has a play with the same id that makes an A-artefact.
