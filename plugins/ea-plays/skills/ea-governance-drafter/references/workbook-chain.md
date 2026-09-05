# The country workbook chain

Each play produces one artefact. The artefacts feed each other. A skill reads this
file to fill the **Consumed** and **Feeds** fields of its provenance header, and to
know what to ask the learner for when an input is missing.

**A0–A8 are frozen.** They are published on the GitBook workbook page and cited by
Module 1's play pages; renumbering them is a major version bump. A9–A31 are defined
here for Modules 2–5 and are stable from v0.1.0.

## Rule: no artefact, no guess

If a skill needs an artefact the learner does not have, it says which one and which
play produces it — *"this needs A0 §4, the roles register; run Play 0 first"* — and
stops. It never invents the missing input, and it never proceeds on a thinner one
without saying so in the output.

## A0 — the pack every play starts from

Play 0 produces seven sections. Each play's input is one or two of them.

| A0 § | Section | Feeds |
| --- | --- | --- |
| §1 | Digital-landscape brief | 1.1, 1.2 |
| §2 | Programme list with budget envelopes and building-block needs | 1.3, 1.5 |
| §3 | Ministry operating context and constraints | 1.4 |
| §4 | Institutional roles register, by post, status-tagged | 1.6, 1.7 |
| §5 | Country characteristics one-liner | 1.8, 5.1 |
| §6 | Public bodies, systems and registries | 2.1, 2.4, 2.5, 4.1 |
| §7 | Legal and policy list | 2.3, 1.7 |

## Module 1 — the cabinet-briefing pack

| Artefact | Play | Consumes | Feeds |
| --- | --- | --- | --- |
| **A0** Country context pack | Play 0 | — | everything below, and Modules 2 and 4 |
| **A1** Fragmentation diagnostic | 1.1 | A0 §1 | 1.3, 1.5 |
| **A2** Ministerial explainer slide | 1.2 | A0 §1 | 1.4 |
| **A3** Re-use business case | 1.3 | A0 §2, A1 | 1.7, 4.6, 5.4 |
| **A4** Joint business–IT agenda | 1.4 | A0 §3, A2 | 1.6 |
| **A5** PAERA foundation coverage map | 1.5 | A0 §2, A1 | 1.6, 2.5 |
| **A6** Phase RACI and role-gap list | 1.6 | A0 §4, A4, A5 | 1.7, 3.7, 5.5 |
| **A7** EA Governance Board ToR | 1.7 | A0 §4, A0 §7, A3, A6, A8 | 3.3, 3.4, 4.7 |
| **A8** Comparator-country cards | 1.8 | A0 §5 | 1.7, 5.1, 5.4, 5.7 |

## Module 2 — reading a government

| Artefact | Play | Consumes | Feeds |
| --- | --- | --- | --- |
| **A9** Four-layer reading template | 2.1 | A0 §6 | 2.5 |
| **A10** Metamodel conformance report | 2.2 | a draft model | 2.5 |
| **A11** Principle card set | 2.3 | A0 §7 | 2.6, 3.5, 4.5 |
| **A12** Body classification profile | 2.4 | A0 §6 | 2.5, 4.1 |
| **A13** Sector BDAT skeleton | 2.5 | A0 §6, A5, A9, A12 | 2.6, 3.1, 4.1 |
| **A14** Scored gap analysis | 2.6 | A13, A11 | 2.7, 4.3 (re-ranked) |
| **A15** Two-trap screen | 2.7 | A14, BB status register | 4.4, 4.7 |

## Module 3 — the practice

| Artefact | Play | Consumes | Feeds |
| --- | --- | --- | --- |
| **A16** EA repository structure | 3.1 | A13 | 3.2, 3.3, 3.6 |
| **A17** EA tool comparison + export test | 3.2 | A16, candidate list | 3.1 |
| **A18** Repository update policy | 3.3 | A16, A7 | 3.5, 3.6 |
| **A7 rev.2** EA Board ToR, standing version | 3.4 | A7, A0 §7 | 3.5, 4.7 |
| **A19** Review-gate checklist | 3.5 | A7 rev.2, A11, BB status register | 4.7 |
| **A20** EA health scorecard | 3.6 | A16, A18 | 3.7 |
| **A21** Sustainment risk register | 3.7 | A20, A6 | 5.2 (re-scoped) |

## Module 4 — the method on one sector

| Artefact | Play | Consumes | Feeds |
| --- | --- | --- | --- |
| **A22** Demonstration canvas | 4.1 | A0 §6, A12 | 4.2 |
| **A23** Discovery brief | 4.2 | A22, A0 §7 | 4.3 |
| **A14 rev.2** Ranked gap analysis | 4.3 | A23, A14 | 4.4 |
| **A24** Sourcing matrix | 4.4 | A14 rev.2, BB status register | 4.5 |
| **A25** Target architecture | 4.5 | A24, A11, BB status register | 4.6 |
| **A26** Wave roadmap | 4.6 | A25, A3 | 4.7, 4.8, 5.4, 5.6 |
| **A27** Gate decision paper | 4.7 | A26, A19, A7 rev.2, BB status register | 5.2 |
| **A28** Sector transfer plan | 4.8 | A26, A0 §6 (next sector) | 5.3 |

## Module 5 — the case and the rollout

| Artefact | Play | Consumes | Feeds |
| --- | --- | --- | --- |
| **A8 rev.2** Comparator evidence, sourced | 5.1 | A0 §5, A8 | 5.4, 5.7 |
| **A21 rev.2** Programme risk register | 5.2 | A21, A27 | 5.4 |
| **A28 rev.2** Second-sector map | 5.3 | A28, BB status register | 5.6 |
| **A29** Ministerial business case | 5.4 | A3, A8 rev.2, A21 rev.2, A26 | 5.7 |
| **A30** Capability-building plan | 5.5 | A6 | — |
| **A31** National rollout wave plan | 5.6 | A26, A28 rev.2, BB status register | 5.7 |
| **A29 rev.2** Closing one-page case | 5.7 | A29, A31, A8 rev.2 | — |

## Registers that are not A-numbered

Three registers are produced on demand rather than by a play, and are cited by
name in **Consumed**:

| Register | Skill | Cited as |
| --- | --- | --- |
| BB status register | `bb-landscape-check` | `BB status register (<date>)` |
| Legal register | `ea-legal-context` | `Legal register (<date>)` |
| Bodies register | `ea-institution-mapper` | `Bodies register (<date>)` |

They are dated because they go stale — a block that was *pilot* last quarter may
be *live* now. Re-run rather than reuse anything older than three months.
