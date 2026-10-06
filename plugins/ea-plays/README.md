# ea-plays

This is the **"with the kit"** layer for the AI plays and the AI usage tips of four Knowledge
Product courses: **Government Enterprise Architecture** (the EA course), **Government
Interoperability Framework** (the interoperability course), the **education DPI roadmap**
course and the **service design** course. It has four skills. They check against PAERA as
published, draft the governance documents and the decree against public sources, and turn
open questions into decisions that a named post can answer.

**The plays work in any assistant without this kit.** The plays are the course material; the
kit is optional. It adds the step a bare prompt skips: it fetches the named sources before it
writes the draft, and it checks the draft against them afterwards.

Since v0.5.0 the kit carries only these four skills. The other skills of earlier versions
are in the repository's history before the v0.5.0 tag.

## Install

```
/plugin marketplace add alaponin/ea-plays-kit
/plugin install ea-plays@ea-plays-kit
```

Choose the **user** scope, so that the kit follows you into each folder. Later, run
`/plugin marketplace update ea-plays-kit` to get a new version.

Do you not use Claude Code? There are three other routes, from the same source tree:

- **Any agent, through the skills CLI** — the skills are published through the ITU Skills
  Marketplace, and `npx skills add alaponin/ea-plays-kit --skill paera-reference-check`
  installs one of them into Claude Code, Codex and other agents.
- **Cowork** — download `ea-plays-v<version>.plugin` from the release on GitHub. Then install
  it from Settings → Capabilities.
- **The Claude app, one skill at a time** — download this repository with **Code → Download
  ZIP**, or clone it. Then upload one folder from `plugins/ea-plays/skills/` at Settings →
  Capabilities → Skills. Each skill folder is self-contained.

## What you get

| Skill | What it does |
| --- | --- |
| `paera-reference-check` | Looks up PAERA and cites the section, its public address and the date; and checks against PAERA as published, and not against the simplification in the videos |
| `ea-governance-drafter` | The Board ToR, the RACI, the repository, the gate checklist, the scorecard and the risk register |
| `gif-decree-draft` | The Decree Drafting Kit: outline, Memorandum and Preamble, one article against a published model, Cover Note and Two-Track Memo — never invented law |
| `decision-cards` | Turns open questions into one page of cards that the person who rules answers by clicking, with the same cards as a numbered list in the chat |

Each output starts with a provenance header. The header gives the country, the date, the
count of sources in each tier, and the count of unverified lines. The next play can then use
the output, and you can see what the output depends on.

## Play → skill — the EA course

The plays below have a skill in this release. Every other play of the course runs bare.

| Play | Artefact | Primary skill | Also runs |
| --- | --- | --- | --- |
| 1.5 | A5 — PAERA foundation coverage map | `paera-reference-check` | — |
| 1.6 | A6 — Phase RACI and role-gap list | `ea-governance-drafter` | — |
| 1.7 | A7 — EA Governance Board ToR | `ea-governance-drafter` | `decision-cards` |
| 2.2 | A10 — Metamodel conformance report | `paera-reference-check` | — |
| 2.3 | A11 — Principle card set | `paera-reference-check` | — |
| 3.1 | A16 — EA repository structure | `ea-governance-drafter` | — |
| 3.3 | A18 — Repository update policy | `ea-governance-drafter` | — |
| 3.4 | A7 rev.2 — EA Board ToR, standing version | `ea-governance-drafter` | — |
| 3.5 | A19 — Review-gate checklist | `ea-governance-drafter` | — |
| 3.6 | A20 — EA health scorecard | `ea-governance-drafter` | — |
| 3.7 | A21 — Sustainment risk register | `ea-governance-drafter` | — |
| 5.2 | A21 rev.2 — Programme risk register | `ea-governance-drafter` | — |

Play ids follow version 0.2 of the EA course (3 September 2026). The whole course, play by
play, is in `tests/play-map.json`; its workbook chain is `shared/workbook-chain.md`.

## Play → skill — the interoperability course

The Government Interoperability Framework course makes **B-numbered** artefacts. The two
courses share play ids (both have a 2.4); the artefact letter says which course. The chain is
`shared/workbook-chain-gif.md`; the fixtures are under `tests/gif/`.

| Play | Artefact | Primary skill | Also runs |
| --- | --- | --- | --- |
| 2.2 | B9 — Decree outline (five components) | `gif-decree-draft` | — |
| 2.3 | B10 — Explanatory Memorandum and Preamble | `gif-decree-draft` | — |
| 2.4 | B11 — Operative article draft | `gif-decree-draft` | — |
| 2.5 | B12 — Cover Note and two-track memo | `gif-decree-draft` | — |
| 3.3 | B16 — Governance RACI | `ea-governance-drafter` | — |
| 3.4 | B17 — Member obligations and agreement | `ea-governance-drafter` | — |
| 3.5 | B18 — Four Working Group charters | `ea-governance-drafter` | — |
| 3.6 | B19 — Change control, standards register (with conformance fields) and semantic-registry charter | `ea-governance-drafter` | — |
| 5.2 | B29 — Member Requirements checklist | `ea-governance-drafter` | — |
| 5.3 | B30 — Service-Level Agreement template | `ea-governance-drafter` | — |

`paera-reference-check` also checks each PAERA anchor that plays 1.7 and 4.3 cite.

## The education DPI roadmap and service design courses

Their AI usage tips run bare. `decision-cards` serves the response matrix of the DPI roadmap
course (6.7), and the review record (3.6) and the model review (4.5) of the service design
course. `paera-reference-check` answers a PAERA question on any page of either course that
cites a PAERA section. The service design course's own method has its own plugin, `sdd-kit`,
in this repository.

## The rules every skill follows

- **Text in, text out.** No file, no chart, no image. The next play must read the output. The
  one exception is `decision-cards`: one HTML page of cards, with the same cards as a numbered
  list in the chat.
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
