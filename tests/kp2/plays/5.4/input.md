# KP2 play 5.4 — Generate the X-Road member registration (subsystem + ACL) · fixture input

**Consumes:** B26, B29 — from [`tests/progressa.md`](../../../progressa.md) and [`tests/kp2/progressa-supplement.md`](../../progressa-supplement.md).
**Primary skill:** `gif-federation-standup` · also runs: `gif-openapi-gen`
**Produces:** B31 — X-Road member registration

## What the learner types

Generate the X-Road member-registration configuration for an agency joining [country X]'s bus. Inputs: the member's details [paste: organisation name, the member class and any known member/subsystem codes], the services it will provide [from its service contracts], and the access policy [which other members may call which of its services]. Produce: (1) the SUBSYSTEM registration — member class, member code, subsystem code, and the service codes it exposes; (2) the ACCESS-CONTROL LIST — for each service, the consumer subsystems permitted to call it. CRITICAL: output every member code, subsystem code and service code as [confirm: verify against the live X-Road registry] — do not invent identifiers, because a wrong code silently routes nowhere or to the wrong agency. Also list, for an onboarding checklist: the certificate steps and the approval (per the governance RACI) that must happen alongside this config. Close with the onboarding checklist in the source method's order — application and signed obligations; certificate issuance; security server deployment; CONFORMANCE TEST against the standards portfolio (state the approach: self-assessment / third-party / test suite); first service registration; production go-live. Output: the subsystem registration, the access-control list, and the [confirm] / approval checklist.

## What the fixture supplies

Country: **Progressa** · Sector: **Education**. Put these two values in the place of each
placeholder in brackets above. The named input is B26, B29. A0 §1–§7 come from
`tests/progressa.md`; A0 §8–§10, the once-only scenario and the federation identifiers come
from `tests/kp2/progressa-supplement.md`. Paste those sections without a change.

If this play consumes a B-artefact from an earlier play, run that play on Progressa first.
The chain is in
[`shared/workbook-chain-kp2.md`](../../../../plugins/ea-plays/shared/workbook-chain-kp2.md).
This is the KP2 play; KP1 has a play with the same id that makes an A-artefact.
