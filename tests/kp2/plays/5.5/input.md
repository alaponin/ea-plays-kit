# KP2 play 5.5 — Draft the federation stand-up run book · fixture input

**Consumes:** B31 — from [`tests/progressa.md`](../../../progressa.md) and [`tests/kp2/progressa-supplement.md`](../../progressa-supplement.md).
**Primary skill:** `gif-federation-standup` · also runs: —
**Produces:** B32 — Federation stand-up run book

## What the learner types

Draft a stand-up run book for an X-Road demonstration federation for [country X] / Progressa. The components are: a Central Server (operated by the digital-government authority), four Security Servers (one each at the four member agencies), and a Test CA. Produce the run book as ordered, reproducible steps: (1) bring up the Central Server and its configuration; (2) bring up the Test CA and register it as the trust anchor; (3) for each Security Server: install, register with the Central Server, obtain its certificate from the Test CA, and verify it is registered; (4) a verification step confirming all four members appear in the Central Server registry. Note which steps are demonstration-only (single VM, sandboxed containers, Test CA) and would differ in production. Mark every server identifier and address as [confirm: set per the actual environment]. Output: the ordered run book plus a 'differs in production' note per step.

## What the fixture supplies

Country: **Progressa** · Sector: **Education**. Put these two values in the place of each
placeholder in brackets above. The named input is B31. A0 §1–§7 come from
`tests/progressa.md`; A0 §8–§10, the once-only scenario and the federation identifiers come
from `tests/kp2/progressa-supplement.md`. Paste those sections without a change.

If this play consumes a B-artefact from an earlier play, run that play on Progressa first.
The chain is in
[`shared/workbook-chain-kp2.md`](../../../../plugins/ea-plays/shared/workbook-chain-kp2.md).
This is the KP2 play; KP1 has a play with the same id that makes an A-artefact.
