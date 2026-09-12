# KP2 play 4.7 — Generate the X-Road service description and wiring checklist · fixture input

**Consumes:** B24, B6 — from [`tests/progressa.md`](../../../progressa.md) and [`tests/kp2/progressa-supplement.md`](../../progressa-supplement.md).
**Primary skill:** `gif-openapi-gen` · also runs: —
**Produces:** B26 — X-Road service description and wiring checklist

## What the learner types

I am wiring a service onto [country X]'s X-Road bus. Inputs: the OpenAPI contract for the service [paste it or its key paths/fields], the provider agency and the consumer agency [name them], and the access policy [who may call this service]. Produce: (1) the X-Road service-description notes derived from the OpenAPI contract (service code, version, the operations exposed); (2) the wiring configuration — the provider's subsystem identity, and the access-control list entries naming which consumer subsystems may call the service; (3) a test-call plan — the exact call a consumer would make and the expected response, to prove the service resolves over the bus. CRITICAL: mark every member/subsystem identifier and service code as [confirm: verify against the live registry], since an invented identifier breaks routing. Note where this aligns to the GovStack Information Mediation building block. Output: the service-description notes, the access-control entries, and the test-call plan.

## What the fixture supplies

Country: **Progressa** · Sector: **Education**. Put these two values in the place of each
placeholder in brackets above. The named input is B24, B6. A0 §1–§7 come from
`tests/progressa.md`; A0 §8–§10, the once-only scenario and the federation identifiers come
from `tests/kp2/progressa-supplement.md`. Paste those sections without a change.

If this play consumes a B-artefact from an earlier play, run that play on Progressa first.
The chain is in
[`shared/workbook-chain-kp2.md`](../../../../plugins/ea-plays/shared/workbook-chain-kp2.md).
This is the KP2 play; KP1 has a play with the same id that makes an A-artefact.
