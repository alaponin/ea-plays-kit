# ea-plays

The **"with the kit"** layer for the Knowledge Product AI plays on government enterprise
architecture. Fourteen skills that build sourced country context, verify every claim against
tiered public sources, and produce artefacts that chain into a country workbook.

**The plays run bare in any assistant.** They are the product; this kit is optional. What it
adds is the step learners skip: bringing the named source in before the draft is written,
and checking it afterwards.

## Install

```
/plugin marketplace add aarelaponin/ea-plays-kit
/plugin install ea-plays@ea-plays-kit
```

Choose **user** scope so the kit follows you across folders. Later, `/plugin marketplace
update ea-plays-kit` pulls a new version.

Not using Claude Code? Two other routes, same source tree:

- **Cowork** — download `ea-plays-<version>.plugin` from the GitHub release and install it
  from Settings → Capabilities.
- **The Claude app, one skill at a time** — download `skills-standalone-<version>.zip` from
  the release and upload any single folder under Settings → Capabilities → Skills. Every
  skill folder is self-contained.

## What you get

| Skill | What it does |
| --- | --- |
| `country-context-pack` | Play 0 — the seven-section A0 pack every other play consumes |
| `cite-or-discard` | Verifies every claim against its source; drops what does not survive |
| `bb-landscape-check` | Which shared building blocks a country actually has **live** |
| `ea-institution-mapper` | Public bodies, legal mandates, systems, posts, PAERA classification |
| `ea-legal-context` | The national legal register an EA programme touches |
| `ea-comparator-evidence` | Comparator countries with primary sources and a contested case |
| `ea-cost-case` | The re-use business case, assumptions first, benchmarks cited |
| `paera-reference-check` | Checks against PAERA as published, not the teaching simplification |
| `ea-method-runner` | The five-phase lifecycle, reading and writing the workbook |
| `ea-governance-drafter` | Board ToR, RACI, repository, gate checklist, scorecard, risk register |
| `ea-tool-evaluator` | EA tool scoring on verifiable facts, plus a real export test |
| `ea-open-learning-catalogue` | A capability plan whose links were checked today |
| `bdat-assessor` | The four-layer read and the metamodel conformance check |
| `bb-sourcing-researcher` | Which products could supply a block the country lacks |

Every output opens with a provenance header — country, date, sources by tier, unverified
count — so the next play can consume it and you can see what it rests on.

## Play → skill

Exactly one primary skill per play. `cite-or-discard` runs inside most of the others rather
than being invoked directly.

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
| 1.8 | A8 — Comparator-country cards | `ea-comparator-evidence` | `cite-or-discard` |

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
| 5.1 | A8 rev.2 — Comparator evidence, sourced | `ea-comparator-evidence` | `cite-or-discard` |
| 5.2 | A21 rev.2 — Programme risk register | `ea-governance-drafter` | — |
| 5.3 | A28 rev.2 — Second-sector map | `ea-method-runner` | `bb-landscape-check`, `ea-institution-mapper` |
| 5.4 | A29 — Ministerial business case | `ea-cost-case` | `ea-comparator-evidence`, `cite-or-discard` |
| 5.5 | A30 — Capability-building plan | `ea-open-learning-catalogue` | — |
| 5.6 | A31 — National rollout wave plan | `ea-method-runner` | `bb-landscape-check` |
| 5.7 | A29 rev.2 — Closing one-page case | `ea-comparator-evidence` | `cite-or-discard`, `ea-cost-case` |

## The rules every skill follows

- **Text in, text out.** No files, no charts, no images — the next play has to read it.
- **Posts, not names.** Never a real office-holder's name, however public.
- **Cite or discard.** Every claim carries a URL, a tier and a date, or it is marked ⚠ or
  dropped. A refused fetch is *unverified*, never *unsupported*.
- **The safeguard comes back to you.** Every output ends with what remains your judgement.

## Licence

Content (skills, references, this README) — CC BY 4.0, see `LICENSE-CONTENT`.
Scripts — MIT, see `LICENSE-CODE`.
