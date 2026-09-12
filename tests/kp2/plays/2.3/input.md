# KP2 play 2.3 — Generate the Explanatory Memorandum and Preamble (gif-decree-draft) · fixture input

**Consumes:** B4, B9 — from [`tests/progressa.md`](../../../progressa.md) and [`tests/kp2/progressa-supplement.md`](../../progressa-supplement.md).
**Primary skill:** `gif-decree-draft` · also runs: `ea-legal-context`, `cite-or-discard`
**Produces:** B10 — Explanatory Memorandum and Preamble

## What the learner types

Below is the Strategic Foundation Document for [country X]'s Government Interoperability Framework [paste it]. Draft two components of an interoperability decree. (1) EXPLANATORY MEMORANDUM — in plain language for a minister: the problem, what the decree does, why now, and the expected benefit; 1-2 pages. (2) PREAMBLE — a scaffold of formal recitals leading to the enacting clause, AND a list of the legal authorities the decree would need to cite (constitutional articles, enabling statutes). CRITICAL: for every legal authority, output a placeholder in the form [confirm: <the kind of authority needed>] rather than naming a specific article or act — you do not have [country X]'s statute book and must not invent citations. Flag any factual claim in the Memorandum that would need evidence. Output: the Memorandum draft, then the Preamble scaffold, then a list of every [confirm] a lawyer must resolve.

## What the fixture supplies

Country: **Progressa** · Sector: **Education**. Put these two values in the place of each
placeholder in brackets above. The named input is B4, B9. A0 §1–§7 come from
`tests/progressa.md`; A0 §8–§10, the once-only scenario and the federation identifiers come
from `tests/kp2/progressa-supplement.md`. Paste those sections without a change.

If this play consumes a B-artefact from an earlier play, run that play on Progressa first.
The chain is in
[`shared/workbook-chain-kp2.md`](../../../../plugins/ea-plays/shared/workbook-chain-kp2.md).
This is the KP2 play; KP1 has a play with the same id that makes an A-artefact.
