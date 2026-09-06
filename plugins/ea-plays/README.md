# ea-plays

This is the **"with the kit"** layer for the Knowledge Product AI plays on government
enterprise architecture. It has fourteen skills. They build a country context that has its
sources, they verify each claim against public sources in four tiers, and they make artefacts
that go into a country workbook.

**The plays run bare in any assistant.** They are the product. This kit is optional. It adds
the step that a learner does not do: it brings in the named source before it writes the
draft, and it checks the draft after.

## Install

```
/plugin marketplace add alaponin/ea-plays-kit
/plugin install ea-plays@ea-plays-kit
```

Choose the **user** scope, so that the kit follows you into each folder. Later, run
`/plugin marketplace update ea-plays-kit` to get a new version.

Do you not use Claude Code? There are two other routes, from the same source tree:

- **Cowork** — download `ea-plays-v<version>.plugin` from the release on GitHub. Then install
  it from Settings → Capabilities.
- **The Claude app, one skill at a time** — download this repository with **Code → Download
  ZIP**, or clone it. Then upload one folder from `plugins/ea-plays/skills/` at Settings →
  Capabilities → Skills. Each skill folder is self-contained.

## What you get

| Skill | What it does |
| --- | --- |
| `country-context-pack` | Play 0 — the A0 pack of seven sections that each other play uses |
| `cite-or-discard` | Verifies each claim against its source, and drops the claims that fail |
| `bb-landscape-check` | Which shared building blocks a country has **live** |
| `ea-institution-mapper` | The public bodies, their legal mandates, their systems, the posts, and the PAERA classification |
| `ea-legal-context` | The national legal register that an EA programme touches |
| `ea-comparator-evidence` | Comparator countries, with primary sources and one contested case |
| `ea-cost-case` | The business case for re-use: the assumptions first, and each benchmark cited |
| `paera-reference-check` | Checks against PAERA as published, and not against the simplification in the videos |
| `ea-method-runner` | The lifecycle of five phases. It reads the workbook and writes to it |
| `ea-governance-drafter` | The Board ToR, the RACI, the repository, the gate checklist, the scorecard and the risk register |
| `ea-tool-evaluator` | Scores an EA tool on facts that you can verify, and gives a real export test |
| `ea-open-learning-catalogue` | A capability plan. Each of its links was checked today |
| `bdat-assessor` | Reads a body or a sector in four layers, and traces the impact of a change |
| `bb-sourcing-researcher` | Which products can supply a block that the country does not have |

Each output starts with a provenance header. The header gives the country, the date, the
count of sources in each tier, and the count of unverified lines. The next play can then use
the output, and you can see what the output depends on.

## Play → skill

Each play has exactly one primary skill. `cite-or-discard` runs inside most of the other
skills. You do not call it directly.

**Play 0**

| Play | Artefact | Primary skill | Also runs |
| --- | --- | --- | --- |
| 0 | A0 — Country context pack | `country-context-pack` | — |

**Module 1 — Why EA**

| Play | Artefact | Primary skill | Also runs |
| --- | --- | --- | --- |
| 1.1 | A1 — Fragmentation diagnostic | `country-context-pack` | `cite-or-discard` |
| 1.2 | A2 — Ministerial explainer slide | `ea-institution-mapper` | — |
| 1.3 | A3 — Re-use business case | `ea-cost-case` | `cite-or-discard` |
| 1.4 | A4 — Joint business–IT agenda | `ea-legal-context` | — |
| 1.5 | A5 — PAERA foundation coverage map | `paera-reference-check` | `cite-or-discard` |
| 1.6 | A6 — Phase RACI and role-gap list | `ea-governance-drafter` | `ea-institution-mapper` |
| 1.7 | A7 — EA Governance Board ToR | `ea-governance-drafter` | `ea-legal-context` |

**Module 2 — Reading a government**

| Play | Artefact | Primary skill | Also runs |
| --- | --- | --- | --- |
| 2.1 | A9 — Four-layer reading template | `bdat-assessor` | — |
| 2.2 | A10 — Metamodel conformance report | `paera-reference-check` | — |
| 2.3 | A11 — Principle card set | `paera-reference-check` | `ea-legal-context` |
| 2.4 | A12 — Body classification profile | `ea-institution-mapper` | — |
| 2.5 | A13 — Sector BDAT skeleton | `bdat-assessor` | `ea-institution-mapper` |
| 2.6 | A14 — Scored gap analysis | `bdat-assessor` | — |
| 2.7 | A15 — Two-trap screen | `bb-landscape-check` | `bb-sourcing-researcher` |

**Module 3 — The practice**

| Play | Artefact | Primary skill | Also runs |
| --- | --- | --- | --- |
| 3.1 | A16 — EA repository structure | `ea-governance-drafter` | — |
| 3.2 | A17 — EA tool comparison + export test | `ea-tool-evaluator` | `cite-or-discard` |
| 3.3 | A18 — Repository update policy | `ea-governance-drafter` | — |
| 3.4 | A7 rev.2 — EA Board ToR, standing version | `ea-governance-drafter` | `ea-legal-context` |
| 3.5 | A19 — Review-gate checklist | `ea-governance-drafter` | `bb-landscape-check` |
| 3.6 | A20 — EA health scorecard | `ea-governance-drafter` | — |
| 3.7 | A21 — Sustainment risk register | `ea-governance-drafter` | — |

**Module 4 — The method on one sector**

| Play | Artefact | Primary skill | Also runs |
| --- | --- | --- | --- |
| 4.1 | A22 — Demonstration canvas | `ea-institution-mapper` | — |
| 4.2 | A23 — Discovery brief | `ea-method-runner` | `cite-or-discard` |
| 4.3 | A14 rev.2 — Ranked gap analysis | `ea-method-runner` | — |
| 4.4 | A24 — Sourcing matrix | `ea-method-runner` | `bb-landscape-check`, `bb-sourcing-researcher` |
| 4.5 | A25 — Target architecture | `ea-method-runner` | `bb-landscape-check` |
| 4.6 | A26 — Wave roadmap | `ea-method-runner` | — |
| 4.7 | A27 — Gate decision paper | `ea-method-runner` | `bb-landscape-check` |
| 4.8 | A28 — Sector transfer plan | `ea-method-runner` | `ea-institution-mapper` |

**Module 5 — The case and the rollout**

| Play | Artefact | Primary skill | Also runs |
| --- | --- | --- | --- |
| 5.1 | A8 — Comparator-country cards, sourced | `ea-comparator-evidence` | `cite-or-discard` |
| 5.2 | A21 rev.2 — Programme risk register | `ea-governance-drafter` | — |
| 5.3 | A31 — National rollout wave plan | `ea-method-runner` | `bb-landscape-check` |
| 5.3b | A28 rev.2 — Second-sector map (GitBook-only companion play, no video) | `ea-method-runner` | `bb-landscape-check`, `ea-institution-mapper` |
| 5.4 | A29 — Ministerial business case | `ea-cost-case` | `ea-comparator-evidence`, `cite-or-discard` |
| 5.5 | A30 — Capability-building plan | `ea-open-learning-catalogue` | — |
| 5.6 | A29 rev.2 — Closing one-page case | `ea-comparator-evidence` | `cite-or-discard`, `ea-cost-case` |

Play ids follow KP1 v0.2 (3 September 2026). 1.8 is retired: its comparator play is 5.1.

## The rules every skill follows

- **Text in, text out.** No file, no chart, no image. The next play must read the output.
- **Posts, not names.** Never write the name of a real office-holder, also when the name is
  public.
- **Cite or discard.** Each claim has a URL, a tier and a date. If it does not, a skill marks
  it ⚠ or drops it. A fetch that a server refuses gives *unverified*. It never gives
  *unsupported*.
- **The safeguard comes back to you.** Each output ends with what stays your judgement.

## Licence

The content uses CC BY 4.0. The content is the skills, the references and this README. See
`LICENSE-CONTENT` here, and `LICENSE` at the root of the repository for the full text.
The scripts use MIT. See `LICENSE-CODE`.
