<!-- fixture: Progressa (fictional) · canonical: tests/progressa.md · keep consistent with it -->
# The Progressa federation — Linkup and the once-only proof

The worked example of plays 5.4, 5.5 and 5.6 on Progressa, as the KP2 build pack stands it
up. Country facts from `tests/progressa.md` §1, §6 and `tests/kp2/progressa-supplement.md`.
Progressa is fictional. The exchange is the target state that the National Learner
Registry programme delivers; in the baseline the Progressa Learner Registry (PLR) is
planned and not started, and Linkup — X-Road 7.x, operated by the Progressa Digital
Government Authority (PDGA), a 2025 pilot with four members — has no education member.

## Topology (5.5)

| Component | Progressa value | Demonstration-only? |
| --- | --- | --- |
| Central Server | owned by `PROGRESSA/GOV/PDGA`, management subsystem `MANAGEMENT`, management Security Server `ss-pdga` | single host: yes |
| Trust anchor | a Test CA with OCSP and timestamping | **yes** — production uses a real certification service |
| Security Servers | `ss-pdga`, `ss-pnea`, `ss-plr`, `ss-pnia` — one per member, host name `ss-<member key>` | container names: yes; host naming that encodes only the owner: yes |
| X-Road release | 7.7.0 in the pack; the portfolio pins it | — |
| Management requests | approved explicitly over the Central Server admin API — no auto-approval flag | no: the same sequence works against a production Central Server |

## Registrations (5.4)

| Member | Subsystem | Role | Services | ACL grants |
| --- | --- | --- | --- | --- |
| `PROGRESSA/GOV/PNEA` — Progressa National Examination Authority | `EXAMS` | consumer | — | — |
| `PROGRESSA/GOV/PLR` — Progressa Learner Registry | `ENROLMENT` | provider | `enrolment-api` (`GET /enrolments/{nin}`) | `PNEA:EXAMS` only |
| `PROGRESSA/GOV/PNIA` — Progressa National ID Authority | `IDENTITY` | provider | `identity-api` (`GET /persons/{nin}`) | `PNEA:EXAMS` only |

The Ministry of Education, Youth and Skills (MoEYS) is not a member of the demonstration
federation; the pack retired its subsystem, and the fixture's problem statement — MoEYS is
not on Linkup — stays true. These identifiers are frozen: KP3 and KP4 build against them.

## The acceptance (5.6)

**Scenario.** A learner applies for a senior-secondary certificate at PNEA. PNEA pre-fills
identity from PNIA and enrolment from PLR over Linkup. The learner provides the NIN;
nothing else is asked.

**WHEN** — through `ss-pnea`, with `X-Road-Client: PROGRESSA/GOV/PNEA/EXAMS`:

```
GET /r1/PROGRESSA/GOV/PNIA/IDENTITY/identity-api/persons/{nin}
GET /r1/PROGRESSA/GOV/PLR/ENROLMENT/enrolment-api/enrolments/{nin}
```

**THEN**

| # | Assertion | Layer |
| --- | --- | --- |
| 1 | both calls return 200 cross-server (ss-pnea → ss-pnia / ss-plr) | technical |
| 2 | every returned field equals the seeded record for that NIN — name, date of birth, region; school, level, year, status | semantic |
| 3 | the assembled application holds `nin` from the citizen and only the nine pre-filled fields from the bus; disjoint; covering the form | organisational + legal |
| 4 | the identity call repeated with `X-Road-Client: PROGRESSA/GOV/PLR/ENROLMENT`, routed through PLR's own Security Server, is denied with the X-Road access-denied fault — from the provider-side ACL | organisational |
| 5 | both responses carry exactly the fields their contracts declare | legal |

Observability: a NIN seeded in PNIA and absent from PLR returns identity plus a clean 404
from enrolment. The artefact: the assembled application for the test NIN with per-field
provenance.

## What differs in production — the seams 5.7 picks up

A real certification service; a member's own Security Server rather than a hosted one;
a pairwise pseudonymous identifier instead of the raw NIN over the bus; message-log
retention and its legal basis; the consent-bearing exchanges the education slice does not
have, because its exchanges are statutory.
