# KP2 play 5.9 — Cross-check the decree, Governance Pack and standards portfolio for drift · fixture input

**Consumes:** B11, B19, B22 — from [`tests/progressa.md`](../../../progressa.md) and [`tests/kp2/progressa-supplement.md`](../../progressa-supplement.md).
**Primary skill:** `gif-consistency-check` · also runs: —
**Produces:** B36 — Document-consistency report

## What the learner types

Below are three foundational documents of [country X]'s Government Interoperability Framework: (A) the decree (legal); (B) the Governance Pack (organisational); (C) the standards portfolio (technical) [paste the three, or their key sections]. Cross-check them for contradictions and report: (1) standards in the catalogue not authorised or referenced by the decree, or referenced at a different version; (2) roles/bodies in the RACI or decree that the Governance Pack does not describe (or the reverse); (3) exchanges the decree authorises that no catalogued service implements, or services with no decree authorisation; (4) key terms ('member', 'service', 'authority', etc.) used inconsistently across the three. For each finding: the contradiction, where it appears in each document, and a QUESTION for a human ('which is correct?') — do NOT decide which document is right. Output: a contradiction table (finding / document A / document B / question) ordered by how damaging it would be if a reviewer found it.

## What the fixture supplies

Country: **Progressa** · Sector: **Education**. Put these two values in the place of each
placeholder in brackets above. The named input is B11, B19, B22. A0 §1–§7 come from
`tests/progressa.md`; A0 §8–§10, the once-only scenario and the federation identifiers come
from `tests/kp2/progressa-supplement.md`. Paste those sections without a change.

If this play consumes a B-artefact from an earlier play, run that play on Progressa first.
The chain is in
[`shared/workbook-chain-kp2.md`](../../../../plugins/ea-plays/shared/workbook-chain-kp2.md).
This is the KP2 play; KP1 has a play with the same id that makes an A-artefact.
