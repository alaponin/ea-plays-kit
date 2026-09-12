# KP2 play 5.6 — Script and verify the once-only exchange (the acceptance check) · fixture input

**Consumes:** B32, B27 — from [`tests/progressa.md`](../../../progressa.md) and [`tests/kp2/progressa-supplement.md`](../../progressa-supplement.md).
**Primary skill:** `gif-federation-standup` · also runs: —
**Produces:** B33 — Once-only acceptance script

## What the learner types

Script the once-only acceptance check for [country X] / Progressa's interoperability demonstration. The scenario: a learner applies for a credential at the examination authority (PNEA), which pre-fills identity from the identity authority (PNIA) and enrolment from the learner registry (PLR) over the X-Road bus. Produce: (1) the GIVEN — the federation deployed, the four members registered, the service published, the demonstration data seeded; (2) the WHEN — the exact cross-server call(s) PNEA makes to PNIA and PLR; (3) the THEN — the expected result: identity and enrolment returned over the bus, the learner asked once, no paper re-entry; (4) the negative check — that a member NOT authorised by the access-control list cannot make the call. Map each step to the layer it exercises (technical/legal/organisational/semantic). Mark every identifier and endpoint as [confirm: against the live registry]. Output: the given/when/then acceptance script plus the negative check.

## What the fixture supplies

Country: **Progressa** · Sector: **Education**. Put these two values in the place of each
placeholder in brackets above. The named input is B32, B27. A0 §1–§7 come from
`tests/progressa.md`; A0 §8–§10, the once-only scenario and the federation identifiers come
from `tests/kp2/progressa-supplement.md`. Paste those sections without a change.

If this play consumes a B-artefact from an earlier play, run that play on Progressa first.
The chain is in
[`shared/workbook-chain-kp2.md`](../../../../plugins/ea-plays/shared/workbook-chain-kp2.md).
This is the KP2 play; KP1 has a play with the same id that makes an A-artefact.
