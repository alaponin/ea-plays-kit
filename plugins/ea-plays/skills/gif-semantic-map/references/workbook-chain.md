# The country workbook chain

Each play makes one artefact. The artefacts are the inputs to each other. A skill
reads this file for two purposes: to fill the **Consumed** and **Feeds** fields of its
provenance header, and to know what to ask the learner for when an input is missing.

**A0 to A8 are frozen.** GitBook publishes them on the workbook page, and the play
pages of Module 1 cite them (A8 is now made by 5.1, but its number does not change). A change to these numbers is a major version bump. This
file defines A9 to A31 for Modules 2 to 5. They are stable from v0.1.0.

## Rule: no artefact, no guess

A skill can need an artefact that the learner does not have. The skill then tells
which artefact it needs and which play makes it, for example *"this needs A0 §4, the
roles register; run Play 0 first"*. Then the skill stops. The skill never invents the
missing input. If it continues with less input, it says so in the output.

## A0 — the pack that each play starts from

Play 0 makes seven sections. The input to each play is one section or two sections.

| A0 § | Section | Feeds |
| --- | --- | --- |
| §1 | Digital-landscape brief | 1.1, 1.2 |
| §2 | Programme list with budget envelopes and building-block needs | 1.3, 1.5 |
| §3 | Ministry operating context and constraints | 1.4 |
| §4 | Institutional roles register, by post, status-tagged | 1.6, 1.7 |
| §5 | Country characteristics one-liner | 5.1 |
| §6 | Public bodies, systems and registries | 2.1, 2.4, 2.5, 4.1 |
| §7 | Legal and policy list | 2.3, 1.7 |

## Module 1 — the cabinet-briefing pack

| Artefact | Play | Consumes | Feeds |
| --- | --- | --- | --- |
| **A0** Country context pack | Play 0 | the country name and sector | everything below, and Modules 2 and 4 |
| **A1** Fragmentation diagnostic | 1.1 | A0 §1 | 1.3, 1.5 |
| **A2** Ministerial explainer slide | 1.2 | A0 §1 | 1.4 |
| **A3** Re-use business case | 1.3 | A0 §2, A1 | 1.7, 4.6, 5.4 |
| **A4** Joint business–IT agenda | 1.4 | A0 §3, A2 | 1.6 |
| **A5** PAERA foundation coverage map | 1.5 | A0 §2, A1, the initiatives list | 1.6, 2.5 |
| **A6** Phase RACI and role-gap list | 1.6 | A0 §4, A4, A5 | 1.7, 3.7, 5.5 |
| **A7** EA Governance Board ToR | 1.7 | A0 §4, A0 §7, A3, A6 | 3.3, 3.4 |

## Module 2 — reading a government

| Artefact | Play | Consumes | Feeds |
| --- | --- | --- | --- |
| **A9** Four-layer reading template | 2.1 | A0 §6 | 2.5 |
| **A10** Metamodel conformance report | 2.2 | a draft model, or the initiatives list | 2.5 |
| **A11** Principle card set | 2.3 | A0 §7 | 2.6, 3.5, 4.5 |
| **A12** Body classification profile | 2.4 | A0 §6 | 2.5, 4.1 |
| **A13** Sector BDAT skeleton | 2.5 | A0 §6, A5, A9, A12, A10 | 2.6, 3.1, 4.1 |
| **A14** Scored gap analysis | 2.6 | A13, A11 | 2.7, 4.3 (re-ranked) |
| **A15** Two-trap screen | 2.7 | A14, BB status register | 4.4, 4.7 |

## Module 3 — the practice

| Artefact | Play | Consumes | Feeds |
| --- | --- | --- | --- |
| **A16** EA repository structure | 3.1 | A13, A17 | 3.2, 3.3, 3.6 |
| **A17** EA tool comparison + export test | 3.2 | A16, candidate list | 3.1 |
| **A18** Repository update policy | 3.3 | A16, A7 | 3.5, 3.6 |
| **A7 rev.2** EA Board ToR, standing version | 3.4 | A7, A0 §7 | 3.5, 4.7 |
| **A19** Review-gate checklist | 3.5 | A7 rev.2, A11, BB status register, A18 | 4.7 |
| **A20** EA health scorecard | 3.6 | A16, A18 | 3.7 |
| **A21** Sustainment risk register | 3.7 | A20, A6 | 5.2 (re-scoped) |

## Module 4 — the method on one sector

| Artefact | Play | Consumes | Feeds |
| --- | --- | --- | --- |
| **A22** Demonstration canvas | 4.1 | A0 §6, A12, A13, the sector problem paragraph | 4.2 |
| **A23** Discovery brief | 4.2 | A22, A0 §7 | 4.3 |
| **A14 rev.2** Ranked gap analysis | 4.3 | A23, A14 | 4.4 |
| **A24** Sourcing matrix | 4.4 | A14 rev.2, BB status register, A15 | 4.5 |
| **A25** Target architecture | 4.5 | A24, A11, BB status register | 4.6 |
| **A26** Wave roadmap | 4.6 | A25, A3 | 4.7, 4.8, 5.3, 5.4 |
| **A27** Gate decision paper | 4.7 | A26, A19, A7 rev.2, BB status register, A15 | 5.2 |
| **A28** Sector transfer plan | 4.8 | A26, A0 §6 (next sector) | 5.3, 5.3b |

## Module 5 — the case and the rollout

| Artefact | Play | Consumes | Feeds |
| --- | --- | --- | --- |
| **A8** Comparator-country cards, sourced | 5.1 | A0 §5 | 5.4, 5.6 |
| **A21 rev.2** Programme risk register | 5.2 | A21, A27 | 5.4 |
| **A31** National rollout wave plan | 5.3 | A26, A28, BB status register | 5.3b, 5.6 |
| **A28 rev.2** Second-sector map | 5.3b | A28, A31, BB status register | — |
| **A29** Ministerial business case | 5.4 | A3, A8, A21 rev.2, A26 | 5.6 |
| **A30** Capability-building plan | 5.5 | A6 | — |
| **A29 rev.2** Closing one-page case | 5.6 | A29, A31, A8 | — |

Play ids follow KP1 v0.2 (3 September 2026): 1.8 is retired and its comparator play is
5.1; 5.3 is the merged rollout video and carries the rollout-waves play; **5.3b** is the
sector-transfer play that lives on the 5.3 GitBook page only, with no video; the closing
case is 5.6. A8 keeps its number — the artefact did not move, only the play that makes it.

## Registers that are not A-numbered

Three registers are made on demand, not by a play. Cite them by name in
**Consumed**:

| Register | Skill | Cited as |
| --- | --- | --- |
| BB status register | `bb-landscape-check` | `BB status register (<date>)` |
| Legal register | `ea-legal-context` | `Legal register (<date>)` |
| Bodies register | `ea-institution-mapper` | `Bodies register (<date>)` |

Each register has a date because registers go stale. A block that was *pilot* last
quarter can be *live* now. Do not use a register that is more than three months old.
Run the skill again.
