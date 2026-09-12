# ea-plays

This is the **"with the kit"** layer for the Knowledge Product AI plays on government
enterprise architecture and, since v0.3.0, on the government interoperability framework (KP2). It has twenty-two skills. They build a country context that has its
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

## Play → skill — KP1

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

The KP2 plays follow, after the KP1 table.

## Play → skill — KP2

KP2 is the Government Interoperability Framework course. Its plays make **B-numbered**
artefacts — the configuration of a framework: the decree, the Governance Pack, the semantic
map and contracts, the running slice. KP1 and KP2 share play ids (both have a 2.4); the
artefact letter says which course. The chain is `shared/workbook-chain-kp2.md`; the
fixtures are under `tests/kp2/`.

Eight skills are KP2's own, all prefixed `gif-`. The three the KP2 play pages name —
`gif-decree-draft`, `gif-semantic-map`, `gif-openapi-gen` — ship under those names. The
other fourteen skills serve KP2 plays as the table says.

| Skill | What it does |
| --- | --- |
| `gif-four-layer-map` | One exchange graded at the four EIF layers from the three registers, and the binding constraint |
| `gif-foundation-drafter` | The Strategic Foundation Document and the country storyboard, mandate cited, calendar honest |
| `gif-decree-draft` | The Decree Drafting Kit: outline, Memorandum and Preamble, one article against a published model, Cover Note and Two-Track Memo — never invented law |
| `gif-consistency-check` | The legal acceptance check and the three-document drift report — a question per finding, never a ruling |
| `gif-semantic-map` | The semantic map aligned to a fetched vocabulary, and the bronze/silver/gold source map; identifiers stay [confirm] |
| `gif-openapi-gen` | The OpenAPI contract from the map, and the X-Road service description, ACL and test call |
| `gif-federation-standup` | The member registration, the stand-up run book and the once-only acceptance script, cited to the NIIS guides |
| `gif-bus-monitor` | Bus health from metadata logs, with the personal-data gate first and every anomaly a question |

**Play 0 supplement**

| Play | Artefact | Primary skill | Also runs |
| --- | --- | --- | --- |
| §8–§10 | A0 §8–§10 — Current exchange approach, integration map, data-protection law and DPA | `country-context-pack` | `ea-legal-context` (§10) |

**Module 1 — Why interoperability, the four layers, the foundation**

| Play | Artefact | Primary skill | Also runs |
| --- | --- | --- | --- |
| 1.1 | B1 — Procured-vs-planned diagnostic | `country-context-pack` | `cite-or-discard` |
| 1.2 | B2 — Four-layer exchange map | `gif-four-layer-map` | `bb-landscape-check`, `ea-legal-context` |
| 1.3 | B3 — Highest-value once-only exchange | `country-context-pack` | `cite-or-discard` |
| 1.4 | B4 — Strategic Foundation Document | `gif-foundation-drafter` | `ea-legal-context` |
| 1.5 | B5 — Use-Case Catalogue | `country-context-pack` | `cite-or-discard` |
| 1.6 | B6 — Stakeholder tier map | `ea-institution-mapper` | — |
| 1.7 | B7 — Standards-to-reuse shortlist | `ea-comparator-evidence` | `paera-reference-check` |

**Module 2 — Legal framework: the Decree Drafting Kit**

| Play | Artefact | Primary skill | Also runs |
| --- | --- | --- | --- |
| 2.1 | B8 — Legal-readiness assessment | `ea-legal-context` | — |
| 2.2 | B9 — Decree outline (five components) | `gif-decree-draft` | `ea-legal-context` |
| 2.3 | B10 — Explanatory Memorandum and Preamble | `gif-decree-draft` | `ea-legal-context`, `cite-or-discard` |
| 2.4 | B11 — Operative article draft | `gif-decree-draft` | `ea-legal-context`, `cite-or-discard` |
| 2.5 | B12 — Cover Note and two-track memo | `gif-decree-draft` | `ea-legal-context` |
| 2.6 | B13 — Legal acceptance check | `gif-consistency-check` | — |

**Module 3 — Governance model: three tiers with RACI**

| Play | Artefact | Primary skill | Also runs |
| --- | --- | --- | --- |
| 3.1 | B14 — Owner's mandate, regulator and operator split | `ea-institution-mapper` | — |
| 3.2 | B15 — Three-tier governance structure | `ea-institution-mapper` | — |
| 3.3 | B16 — Governance RACI | `ea-governance-drafter` | — |
| 3.4 | B17 — Member obligations and agreement | `ea-governance-drafter` | — |
| 3.5 | B18 — Four Working Group charters | `ea-governance-drafter` | — |
| 3.6 | B19 — Change control, standards register and semantic-registry charter | `ea-governance-drafter` | — |

**Module 4 — Architecture, technical standards and the Giga end-to-end case**

| Play | Artefact | Primary skill | Also runs |
| --- | --- | --- | --- |
| 4.1 | B20 — Component-to-layer map | `bb-landscape-check` | — |
| 4.2 | B21 — Trust-zone trace | `bb-landscape-check` | — |
| 4.3 | B22 — Standards portfolio | `ea-comparator-evidence` | `paera-reference-check` |
| 4.4 | B23 — Semantic map | `gif-semantic-map` | `cite-or-discard` |
| 4.5 | B24 — OpenAPI service contract | `gif-openapi-gen` | — |
| 4.6 | B25 — Bronze/silver/gold source map | `gif-semantic-map` | `gif-openapi-gen` |
| 4.7 | B26 — X-Road service description and wiring checklist | `gif-openapi-gen` | — |
| 4.8 | B27 — Data-protection envelope | `ea-legal-context` | — |

**Module 5 — Implementation, onboarding, the demonstration federation, and running the framework**

| Play | Artefact | Primary skill | Also runs |
| --- | --- | --- | --- |
| 5.1 | B28 — Implementation plan: phased schedule, investment, procurement, workforce, risk register and metrics | `ea-method-runner` | — |
| 5.2 | B29 — Member Requirements checklist | `ea-governance-drafter` | — |
| 5.3 | B30 — Service-Level Agreement template | `ea-governance-drafter` | — |
| 5.4 | B31 — X-Road member registration | `gif-federation-standup` | `gif-openapi-gen` |
| 5.5 | B32 — Federation stand-up run book | `gif-federation-standup` | — |
| 5.6 | B33 — Once-only acceptance script | `gif-federation-standup` | — |
| 5.7 | B34 — Demonstration-to-production gap checklist | `ea-method-runner` | — |
| 5.8 | B35 — Bus-health summary and anomaly list | `gif-bus-monitor` | — |
| 5.9 | B36 — Document-consistency report | `gif-consistency-check` | — |
| 5.10 | B37 — Sector-portability map | `ea-method-runner` | — |

**The storyboard — on the KP2 home page, no video**

| Play | Artefact | Primary skill | Also runs |
| --- | --- | --- | --- |
| home | B38 — Country storyboard | `gif-foundation-drafter` | — |

Play ids follow the KP2 GitBook of 12 September 2026. Module 6 is retired; its three real
plays are 5.8, 5.9 and 5.10, and its storyboard is the home-page play.

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
