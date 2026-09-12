# KP2 play 4.2 — Trace an exchange across the trust zones and name its security · fixture input

**Consumes:** B5, B20 — from [`tests/progressa.md`](../../../progressa.md) and [`tests/kp2/progressa-supplement.md`](../../progressa-supplement.md).
**Primary skill:** `bb-landscape-check` · also runs: —
**Produces:** B21 — Trust-zone trace

## What the learner types

Below is a cross-agency exchange on [country X]'s interoperability bus [describe it: which agency's system calls which other agency's service, and what data flows]. Trace the call across the three trust zones — Member-Internal (the caller's network), Public (between security servers), Member-Internal (the callee's network) — with the Trust-Anchor underwriting identities. For each boundary crossing, and for the audit record the call must leave (correlation id, sender, recipient, service, signature, timestamp),, state the security control required: mutual TLS between security servers, message signing and logging (X-Road message protocol), and valid Trust-Anchor certificates at both ends. Then list: which component holds each control (the security server at each edge), and what would have to be true for this exchange to be insecure (e.g. a revoked or expired certificate, a member system exposed directly to the public zone). Output: a zone-by-zone security specification plus a short 'how this could fail' list.

## What the fixture supplies

Country: **Progressa** · Sector: **Education**. Put these two values in the place of each
placeholder in brackets above. The named input is B5, B20. A0 §1–§7 come from
`tests/progressa.md`; A0 §8–§10, the once-only scenario and the federation identifiers come
from `tests/kp2/progressa-supplement.md`. Paste those sections without a change.

If this play consumes a B-artefact from an earlier play, run that play on Progressa first.
The chain is in
[`shared/workbook-chain-kp2.md`](../../../../plugins/ea-plays/shared/workbook-chain-kp2.md).
This is the KP2 play; KP1 has a play with the same id that makes an A-artefact.
