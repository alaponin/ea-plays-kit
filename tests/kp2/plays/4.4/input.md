# KP2 play 4.4 — Generate a semantic map for an exchange (gif-semantic-map) · fixture input

**Consumes:** B5, B22 — from [`tests/progressa.md`](../../../progressa.md) and [`tests/kp2/progressa-supplement.md`](../../progressa-supplement.md).
**Primary skill:** `gif-semantic-map` · also runs: `cite-or-discard`
**Produces:** B23 — Semantic map

## What the learner types

Below are two agencies that need to exchange data on [country X]'s bus, with each one's field list for the shared entity [paste: the entity, e.g. a learner; agency A's fields and code lists; agency B's fields and code lists; and the published vocabulary to align to, e.g. OneRoster / CEDS]. Produce a semantic map for this exchange: (1) the shared entity and its fields, aligned to the published vocabulary; (2) for each field, the mapping from agency A's term and agency B's term to the shared definition; (3) code-list reconciliation — where A's allowed values differ from B's, the translation; (4) the identifier to use to link the same record across both agencies, and the risk if it is not unique. CRITICAL: output every identifier choice and every code-list value as [confirm: check against the live registry], because you do not have the real registries and an invented mapping can merge two people's records. Output: the semantic map plus a list of every [confirm] to resolve.

## What the fixture supplies

Country: **Progressa** · Sector: **Education**. Put these two values in the place of each
placeholder in brackets above. The named input is B5, B22. A0 §1–§7 come from
`tests/progressa.md`; A0 §8–§10, the once-only scenario and the federation identifiers come
from `tests/kp2/progressa-supplement.md`. Paste those sections without a change.

If this play consumes a B-artefact from an earlier play, run that play on Progressa first.
The chain is in
[`shared/workbook-chain-kp2.md`](../../../../plugins/ea-plays/shared/workbook-chain-kp2.md).
This is the KP2 play; KP1 has a play with the same id that makes an A-artefact.
