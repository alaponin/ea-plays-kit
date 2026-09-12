# KP2 play 2.6 — Check your decree authorises exactly your catalogue (the legal acceptance check) · fixture input

**Consumes:** B5, B11 — from [`tests/progressa.md`](../../../progressa.md) and [`tests/kp2/progressa-supplement.md`](../../progressa-supplement.md).
**Primary skill:** `gif-consistency-check` · also runs: —
**Produces:** B13 — Legal acceptance check

## What the learner types

Below are two things for [country X]'s interoperability framework: (A) the Use-Case Catalogue — the list of cross-agency exchanges the framework intends to carry [paste it]; and (B) the draft Articles of the interoperability decree [paste them]. Run two checks. COVERAGE: for each exchange in the catalogue, identify which article(s) of the decree provide its lawful basis, or flag it as NOT COVERED if none does. SCOPE: for each article that authorises or compels data exchange, check whether the exchanges it permits are all within the catalogue and the framework's principles, or whether it OVER-REACHES by authorising broader sharing than the framework needs. Output: a coverage table (catalogue exchange / authorising article / status), a list of NOT COVERED exchanges, and a list of OVER-REACHING articles — each with a one-line note on the fix.

## What the fixture supplies

Country: **Progressa** · Sector: **Education**. Put these two values in the place of each
placeholder in brackets above. The named input is B5, B11. A0 §1–§7 come from
`tests/progressa.md`; A0 §8–§10, the once-only scenario and the federation identifiers come
from `tests/kp2/progressa-supplement.md`. Paste those sections without a change.

If this play consumes a B-artefact from an earlier play, run that play on Progressa first.
The chain is in
[`shared/workbook-chain-kp2.md`](../../../../plugins/ea-plays/shared/workbook-chain-kp2.md).
This is the KP2 play; KP1 has a play with the same id that makes an A-artefact.
