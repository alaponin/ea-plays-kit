# The framework workbook chain — KP2

KP2 is the Government Interoperability Framework course. Its plays make **B-numbered**
artefacts, which are the *configuration* of a framework: the decree is the legal
configuration, the Governance Pack the organisational, the semantic map and the service
contracts the technical, and Module 5 stands them up as one running slice. This file is
the KP2 counterpart of `workbook-chain.md`. A skill reads it for the same two purposes: to
fill the **Consumed** and **Feeds** fields of its provenance header, and to know what to
ask the learner for when an input is missing.

The rule **no artefact, no guess** applies without change. A skill that needs B5 and does
not have it says *"this needs B5, the Use-Case Catalogue; run KP2 play 1.5 first"* and
stops. It never invents the missing input.

**KP1 and KP2 share play ids.** Play 2.4 exists in both courses. When a learner names a play
id and the artefact letter is not clear, ask which course. A KP2 play always makes a
B-artefact; a KP1 play always makes an A-artefact. Write the course in the **Artefact**
field only through the letter: `B11 — Operative article draft` is enough.

## A0 — the pack KP2 starts from, and its three extra sections

KP2 reads the seven sections of A0 that Play 0 makes, and three more that the KP2 Play 0
supplement makes. `country-context-pack` makes all ten.

| A0 § | Section | Feeds (KP2) |
| --- | --- | --- |
| §1 | Digital-landscape brief | 1.1, 1.2, 1.7 |
| §2 | Programme list with budget envelopes and building-block needs | 1.3 |
| §4 | Institutional roles register, by post, status-tagged | 1.6, 3.2 |
| §6 | Public bodies, systems and registries | 1.6, 3.1, 4.1 |
| §7 | Legal and policy list | 1.4, 2.1 |
| §8 | Current exchange approach — the platform if one exists, how interoperability is required today, the known point-to-point links, any duplication assessment | 1.1 |
| §9 | Integration map — the 6–10 exchanges the sector's services depend on, today's mechanism for each, and the citizen's re-supply burden | 1.2, 1.3, 1.5 |
| §10 | Data-protection law and DPA — the act, the section on public-sector sharing, the authority and whether it operates, the instruments that already mandate or restrict exchange | 2.1, 4.8 |

## Hand-offs from KP1

Three KP1 artefacts enter the chain. Cite them in **Consumed** by their A-number. If the
learner does not have them, the KP2 play named builds the equivalent.

| KP1 artefact | Enters KP2 at | If the learner does not have it |
| --- | --- | --- |
| **A0** country context pack | 1.1, 1.5, 1.6 | run Play 0 and the KP2 supplement |
| **A7** EA Governance Board ToR | 3.1 — the Operating Authority | 3.1 drafts the mandate from A0 §6 |
| **A24** sourcing matrix | 4.3 — the standards portfolio | 4.3 assembles it from the published menu and B7 |

## Module 1 — the foundation

| Artefact | Play | Consumes | Feeds |
| --- | --- | --- | --- |
| **B1** Procured-vs-planned diagnostic | 1.1 | A0 §1, A0 §8 | 1.4 |
| **B2** Four-layer exchange map | 1.2 | A0 §1, A0 §9 | — |
| **B3** Highest-value once-only exchange | 1.3 | A0 §2, A0 §9 | 1.4, 1.5 |
| **B4** Strategic Foundation Document | 1.4 | B1, B3, A0 §7 | 2.2, 2.3, 3.1 |
| **B5** Use-Case Catalogue | 1.5 | A0 §9, B3 | 2.4, 2.6, 4.2, 4.4, 4.8, 5.1, home |
| **B6** Stakeholder tier map | 1.6 | A0 §4, A0 §6 | 3.3, 3.4, 4.7, 5.1 |
| **B7** Standards-to-reuse shortlist | 1.7 | A0 §1 | 4.3 |

## Module 2 — the legal configuration: the decree

| Artefact | Play | Consumes | Feeds |
| --- | --- | --- | --- |
| **B8** Legal-readiness assessment | 2.1 | A0 §7, A0 §10 | 2.2 |
| **B9** Decree outline (five components) | 2.2 | B4, B8 | 2.3, 2.4 |
| **B10** Explanatory Memorandum and Preamble | 2.3 | B4, B9 | 2.5 |
| **B11** Operative article draft | 2.4 | B9, B5 | 2.5, 2.6, 4.8, 5.9 |
| **B12** Cover Note and two-track memo | 2.5 | B10, B11 | — |
| **B13** Legal acceptance check | 2.6 | B5, B11 | 5.2 |

## Module 3 — the organisational configuration: the Governance Pack

| Artefact | Play | Consumes | Feeds |
| --- | --- | --- | --- |
| **B14** Owner's mandate, regulator and operator split | 3.1 | A0 §6, B4 | 3.2 |
| **B15** Three-tier governance structure | 3.2 | A0 §4, B14 | 3.3, 3.5 |
| **B16** Governance RACI | 3.3 | B15, B6 | 3.4, 3.6 |
| **B17** Member obligations and agreement | 3.4 | B16, B6 | 5.3 |
| **B18** Four Working Group charters | 3.5 | B15 | 3.6 |
| **B19** Change control, standards register (with conformance fields) and semantic-registry charter | 3.6 | B16, B18 | 5.9 |

## Module 4 — the technical configuration

| Artefact | Play | Consumes | Feeds |
| --- | --- | --- | --- |
| **B20** Component-to-layer map | 4.1 | A0 §6 | 4.2, 4.3 |
| **B21** Trust-zone trace | 4.2 | B5, B20 | — |
| **B22** Standards portfolio | 4.3 | B7, B20 | 4.4, 4.5, 5.2, 5.9, 5.10 |
| **B23** Semantic map | 4.4 | B5, B22 | 4.5, 4.6, 5.10 |
| **B24** OpenAPI service contract | 4.5 | B23, B22 | 4.7 |
| **B25** Bronze/silver/gold source map | 4.6 | B23 | — |
| **B26** X-Road service description and wiring checklist | 4.7 | B24, B6 | 5.4 |
| **B27** Data-protection envelope | 4.8 | B5, B11 | 5.6 |

## Module 5 — the runnable slice, then the framework in operation

| Artefact | Play | Consumes | Feeds |
| --- | --- | --- | --- |
| **B28** Implementation plan: phased schedule, investment, procurement, workforce, risk register and metrics | 5.1 | B5, B6 | 5.7, 5.10, home |
| **B29** Member Requirements checklist | 5.2 | B22, B13 | 5.4 |
| **B30** Service-Level Agreement template | 5.3 | B17 | — |
| **B31** X-Road member registration | 5.4 | B26, B29 | 5.5 |
| **B32** Federation stand-up run book | 5.5 | B31 | 5.6, 5.7 |
| **B33** Once-only acceptance script | 5.6 | B32, B27 | 5.8 |
| **B34** Demonstration-to-production gap checklist | 5.7 | B32, B28 | — |
| **B35** Bus-health summary and anomaly list | 5.8 | B33 | — |
| **B36** Document-consistency report | 5.9 | B11, B19, B22 | — |
| **B37** Sector-portability map | 5.10 | B28, B22, B23 | — |

## The storyboard — a play on the KP2 home page, with no video

| Artefact | Play | Consumes | Feeds |
| --- | --- | --- | --- |
| **B38** Country storyboard | home | B5, B28 | — |

Play ids follow the KP2 GitBook of 12 September 2026. Module 6 is retired: its bus
monitoring, document cross-check and sector portability are 5.8, 5.9 and 5.10; its
storyboard is the `home` play. B-numbers follow curriculum order and are stable from
v0.3.0.

## Registers that are not B-numbered

The three on-demand registers of `workbook-chain.md` serve KP2 in the same way, and
under the same three-month rule:

| Register | Skill | KP2 plays that read it |
| --- | --- | --- |
| BB status register | `bb-landscape-check` | 1.2 (technical layer), 4.1, 4.2 |
| Legal register | `ea-legal-context` | 1.2 (legal layer), 2.1, 2.2–2.5 (the [confirm] placeholders), 4.8 |
| Bodies register | `ea-institution-mapper` | 1.2 (organisational layer), 1.6, 3.1, 3.2 |

## The build pack is Progressa's finished configuration

The KP2 build pack is the worked example of Modules 4 and 5 for Progressa: a real
once-only exchange on an X-Road federation, PNEA ← PNIA + PLR. Its frozen identifiers
(instance `PROGRESSA`, member class `GOV`, owner `PDGA`, members `PNEA:EXAMS`,
`PLR:ENROLMENT`, `PNIA:IDENTITY`) are the join keys that KP3 and KP4 build against. A
skill that runs on Progressa uses those identifiers and no others. A skill that runs on a
real country never copies them: every identifier of a real country is `[confirm: against
the live registry]` until the learner confirms it.
