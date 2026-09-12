# KP2 play 4.5 — Generate an OpenAPI service contract (gif-openapi-gen) · fixture input

**Consumes:** B23, B22 — from [`tests/progressa.md`](../../../progressa.md) and [`tests/kp2/progressa-supplement.md`](../../progressa-supplement.md).
**Primary skill:** `gif-openapi-gen` · also runs: —
**Produces:** B24 — OpenAPI service contract

## What the learner types

Generate an OpenAPI 3.x contract for a service on [country X]'s interoperability bus. Inputs: the service brief [paste: what the service does, e.g. 'return a learner's identity and enrolment given a national ID'] and the semantic map for the data it returns [paste the relevant fields, types and identifier from your semantic map]. Produce: (1) the path(s) and operation(s); (2) the request parameters, including the identifier; (3) the response schema, with field names and types taken from the semantic map; (4) the error responses; (5) the security scheme (OAuth 2.x / OIDC). CRITICAL: mark every path, field name and type as [confirm: verify against what the provider system actually exposes] — do not invent fields the provider may not return. Then note which parts become the X-Road service description. Output: the OpenAPI document (YAML), a list of [confirm] items, and the X-Road service-description notes.

## What the fixture supplies

Country: **Progressa** · Sector: **Education**. Put these two values in the place of each
placeholder in brackets above. The named input is B23, B22. A0 §1–§7 come from
`tests/progressa.md`; A0 §8–§10, the once-only scenario and the federation identifiers come
from `tests/kp2/progressa-supplement.md`. Paste those sections without a change.

If this play consumes a B-artefact from an earlier play, run that play on Progressa first.
The chain is in
[`shared/workbook-chain-kp2.md`](../../../../plugins/ea-plays/shared/workbook-chain-kp2.md).
This is the KP2 play; KP1 has a play with the same id that makes an A-artefact.
