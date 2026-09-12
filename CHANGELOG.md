# Changelog

Semver in both manifests, bumped together. **Patch:** a source-tier or reference fix.
**Minor:** a new skill, a changed output contract, or a PAERA version change (named here).
**Major:** reserved for a workbook-chain change that breaks artefact numbering.

Video descriptions and the GitBook link the install command, never a release number.

## [Unreleased]

## [0.3.0] — 2026-09-12

The KP2 layer. The KP2 GitBook of 12 September names three skills in its AI tips —
`gif-decree-draft`, `gif-semantic-map`, `gif-openapi-gen` — that did not exist, and sixteen
of its thirty-eight plays said *no skill yet, so the prompt runs bare*. Every KP2 play now
has a primary skill, and the three named skills ship under exactly those names.

Minor: eight new skills, a second workbook chain, no change to any KP1 artefact number, skill
name or output contract.

### Added

- **Eight `gif-*` skills**, one per KP2 artefact family: `gif-four-layer-map` (1.2),
  `gif-foundation-drafter` (1.4, the home-page storyboard), `gif-decree-draft` (2.2–2.5),
  `gif-consistency-check` (2.6, 5.9), `gif-semantic-map` (4.4, 4.6), `gif-openapi-gen`
  (4.5, 4.7), `gif-federation-standup` (5.4–5.6), `gif-bus-monitor` (5.8). Each follows the
  output contract, runs `cite-or-discard` where it cites, and keeps every identifier, code
  value and legal citation the country's own registries or statutes must confirm as
  `[confirm]`. Three carry Progressa fixture material from the KP2 build pack — the
  semantic map, the identity-service contract and wiring, the federation and its acceptance
  — each under the fixture marker.
- **`shared/workbook-chain-kp2.md`** — the B1–B38 chain, the A0 §8–§10 sections, the KP1
  hand-offs (A0, A7, A24), and the frozen Progressa federation identifiers. Synced into every
  skill's `references/` like the other shared files.
- **`tests/kp2/`** — `progressa-supplement.md` (A0 §8–§10 for Progressa, the once-only
  scenario and the federation), `play-map.json` for the 38 KP2 plays, and one fixture folder
  per play. KP1 and KP2 share play ids, so the KP2 fixtures live in their own tree.
- **`tests/check_fixtures.py`** — a KP2 block with the same criteria: fixtures complete,
  skills shipped, nine provenance fields, README rows, the B-chain consistent in both
  directions, the map equal to the chain, and the three tip-named skills present.
- **`country-context-pack/references/a0-kp2-supplement.md`** — how to build A0 §8–§10.

### Changed

- **Eight existing skills gained a `## KP2 plays` section and KP2 trigger phrases** in
  their descriptions: `country-context-pack`, `ea-institution-mapper`,
  `ea-comparator-evidence`, `ea-legal-context`, `ea-governance-drafter`,
  `bb-landscape-check`, `ea-method-runner`, `paera-reference-check`. Their KP1 behaviour is
  unchanged.
- **`shared/provenance-header.md`** — the Artefact field says A- for KP1 and B- for KP2;
  the Feeds field names which chain to read.
- The plugin README carries a second play → skill table for KP2; both manifests say 0.3.0.
- **Every skill description is a trigger blurb again.** They had grown to 1,850 characters
  by restating the procedure the body already carries, and all 22 load before any skill
  runs. Each is now one sentence of identity plus its trigger list, with the sibling
  disambiguators kept: 29,282 → 20,321 characters, roughly 2,200 tokens off the standing
  cost. No trigger phrase was dropped, and everything below `allowed-tools:` is
  byte-identical in all 22 files.
- **The six KP1-only skills name `workbook-chain-kp2.md`** in their shared contract, as the
  `gif-*` skills already did. `sync-shared.sh` copies all five shared files into all 22
  skills and still does; making it course-aware was considered and rejected, because which
  course a skill serves is the most volatile fact about it — this release alone moved eight
  skills from one course to two — and a skill that loses a chain it turns out to need fails
  inside a folder a learner has already uploaded. A file shipped and never opened costs
  disk; a file needed and not shipped costs the learner.
- `.claude-plugin/marketplace.json` — the marketplace description names KP2 beside KP1, as
  the plugin entry inside it already did.

### Fixed

- **Progressa's coverage figures no longer leak into generic guidance.** `gif-semantic-map`
  told the model that a national ID "covers 78% of adults", and its `identifier-rules.md`
  named "the 22% of adults without a national ID" — the fixture's numbers, in two files
  that carry no fixture marker, read by a learner working on a real country. Check 9 only
  fires on named tokens (`Progressa`, `PNIA`, …), so a bare percentage walked past it.
- **`gif-bus-monitor` and `gif-consistency-check` run `cite-or-discard`**, as the other six
  `gif-*` skills do. Both fetch published sources — the operational monitoring protocol,
  the current version of a standard — and both were reaching the output with those
  citations unverified.
- **`gif-federation-standup` no longer claims a dependency the chain does not carry.** Play
  5.5's inputs named "the X-Road release from B22", but the chain has 5.5 consuming B31
  alone, so B22's Feeds never reached it. The release is now asked for directly, with B22
  as "also useful". `check_fixtures.py` compares `play-map.json` with the chain in both
  directions but nothing compared the SKILL tables, which is why this passed every run.

### Tests

- **A ceiling on skill descriptions** (2b), 1,500 characters. A ratchet: lower it as the
  longest come down, never raise it.
- **A bidirectional reference check** (2c). A `references/x.md` a SKILL.md names must exist,
  or the skill breaks in the folder a learner uploaded; and a skill-specific file that
  nothing names is flagged as a dead file or a dropped mention. The five shared files are
  exempt from the second direction — they ship everywhere by contract, not by reference.

### Not in this release

- The KP2 GitBook still says *no skill yet* on sixteen play pages and lists fourteen skills
  on the kit page. `KP2-GIF/gitbook/play-map.json` (`skill`, `also`) and `KIT_SKILLS` in
  `kp-gitbook-render` are the two edits, then a re-render; the KP2 skill mapping is
  `tests/kp2/play-map.json` here.

## [0.2.3] — 2026-09-07

The workbook chain agreed with itself in one direction only. Ten artefacts named a play in
their **Feeds** cell that did not name them back in its **Consumes** cell — A10 → 2.5,
A15 → 4.4 and 4.7, A17 → 3.1, A18 → 3.5, A13 → 4.1 among them. `check_fixtures.py` walked
Consumes → Feeds and never the reverse, so the one-way edges passed every run, and the KP1
GitBook rendered 2.2 and 2.7 as dead ends because it reads the map rather than the chain.

Patch: no artefact number, skill name or output contract changed.

### Fixed

- **`shared/workbook-chain.md`** — the nine Consumes cells missing an input now carry it.
  One correction went the other way: **A7** listed 4.7 in its Feeds, but 4.7 consumes
  **A7 rev.2** (the standing ToR from 3.4), so 4.7 was left alone and A7's Feeds corrected.
- **`tests/play-map.json`** — `consumes` synced from the chain for ten plays. The chain is
  the source; the map had drifted both wider (1.2 carried A0 §6, which the chain routes to
  2.1, 2.4, 2.5 and 4.1) and narrower.

### Added

- **`tests/check_fixtures.py` 10b** — walks Feeds → Consumes, so a one-way edge now fails.
- **`tests/check_fixtures.py` 10c** — compares `play-map.json` `consumes` against the chain
  cell by cell: the drift the KP1 structure draft §10.1 predicted when the two are
  maintained apart.

## [0.2.2] — 2026-09-06

Play ids aligned with KP1 v0.2 (the 3 September 2026 tightening). Patch: no artefact number
changes, no skill name changes, no output contract changes — only which play makes what.

### Changed

- **1.8 is retired.** KP1 v0.2 folded its comparator play into 5.1. The `1.8` fixture and
  play-map entry are gone; 5.1 now makes **A8 — Comparator-country cards, sourced** from
  A0 §5 in one pass, and the "A8 rev.2" label is dropped. A8 keeps its number because the
  artefact did not move. 1.7 no longer consumes A8 (it comes later in the course now).
- **5.3 is the rollout-waves play** (A31), formerly 5.6, because the portability video and
  the rollout video were merged into one 5.3.
- **5.3b is the sector-transfer play** (A28 rev.2), formerly 5.3. It lives on the 5.3
  GitBook page only, with no video; the `b` suffix keeps one fixture folder per play id.
- **5.6 is the closing case** (A29 rev.2), formerly 5.7. Module 5 has six videos.
- `shared/workbook-chain.md`, `tests/play-map.json`, the plugin README play table, the
  fixture folders and every SKILL.md that named the old ids now say the same thing;
  `check_fixtures.py` expects 37 chain rows.

### Removed

- **The old tags.** `v0.1.0`, `v0.1.2`, `v0.1.3` and `v0.0.1-baseline` are deleted, with
  the GitHub releases for 0.1.2 and 0.1.3. The remote now carries `v0.2.0` and `v0.2.1`,
  and each of the two has its `.plugin` attached to a release. The entries for the old
  versions stay in this file, because they are the record of what each release said. Two
  of those entries pointed at the baseline tag, and they now say that it is gone.

## [0.2.1] — 2026-09-05

Marketplace metadata. No skill contract changes.

### Added

- **The frontmatter of each skill declares `license` and `metadata.provider`.** The Giga
  Skills Marketplace scans a public repository, and each directory that holds a `SKILL.md`
  becomes one skill. Its automated checks fail a skill that does not declare a name, a
  description, a licence and a provider. The fourteen skills declared the first two only.
  They now also declare `license: CC-BY-4.0` and `metadata.provider: FiscalAdmin OÜ`.
- **`LICENSE` at the root of the repository.** The marketplace needs a licence file at the
  root. It shows the licence as provenance in the catalogue, and a moderator reads it. The
  two licence files were under `plugins/ea-plays/`, with names that GitHub does not detect,
  so GitHub reported no licence for this repository. The new file carries the full text of
  CC BY 4.0, from creativecommons.org, under one line of copyright.
  `LICENSE-CONTENT` and `LICENSE-CODE` stay where they are, because `package.sh` puts them
  inside the plugin that a learner installs.

## [0.2.0] — 2026-09-05

Two passes: the dangling references, and Simplified Technical English. Minor: two skills gain
the output contract they ship inside, and every skill file changes its wording.

### Changed

- **Every markdown file in the kit is written in ASD-STE100 Simplified Technical English.**
  This covers `shared/`, the fourteen `SKILL.md` files, each file in `references/` and
  `scripts/`, both READMEs, `tests/README.md`, `tests/progressa.md`, and the 76 play
  fixtures. Sentences are short, the voice is active, one sentence gives one instruction, and
  one word has one meaning. The technical names stay: artefact, play, learner, PAERA,
  building block, and the A-numbers.
  Three kinds of text keep their wording. The `Trigger on:` lists in each frontmatter
  `description` are the surface that the harness matches against the words of a user, so the
  quoted phrases are unchanged. The `What the learner types` block in each `input.md`, the
  `The prompt of the play says:` line and the safeguard in each `expected.md` quote the
  published play, and this repo is not their source. The released entries in this CHANGELOG
  are a record of what the releases said, so they stay as they were written.
- **`docs/plans/` is no longer tracked.** Both plans shipped, and both still said *Status:
  proposed*. They stay on disk. `.gitignore` keeps them out of the repository.
- **The citations to a build plan that is not in this repo are gone**: `plan §3.1` in
  `.gitignore`, `§3.5` in `sync-shared.sh`, and `§3.7` in `package.sh`. `tests/README.md`
  already said that the plan which numbered the criteria is not here.
- `tests/progressa.md` cited `gitbook-demo/fixture.py` as its source. A learner cannot open
  that path. The file now says that the source is outside this repo, and that this page is
  the authority for each fact about Progressa.

### Fixed

- **`bdat-assessor` and `bb-sourcing-researcher` now obey the contract that they carry.** The
  0.1.0 release carried both skills over without a change, and neither joined the contract.
  They had no provenance header, no output contract, no `allowed-tools`, and no reference to
  the four shared files that `sync-shared.sh` copies into them. Each folder therefore held
  four files that the skill never read. `bdat-assessor` is the primary skill for plays 2.1,
  2.5 and 2.6, and their `expected.md` needs the nine fields, so the fixture asked for output
  that the skill never asked the model to write. Both skills now start with the header, name
  `output-contract.md`, and are read-only, like the other twelve. `bb-sourcing-researcher` no
  longer offers a `.docx` deliverable, because play 4.4 must paste the output.
- **No skill names a skill that does not ship.** The four extended originals —
  `country-context-data`, `paera-assessor`, `ea-lifecycle-method` and
  `govstack-cost-estimator` — were still cited as live hand-offs: *"hand the posture to"*,
  *"pull these in"*, and *"load it when §1 needs a figure"*. A learner who installs this kit
  does not have them. Each citation now names its successor in the kit, and the *Inherited*
  notes drop the name.
- The owner URL in both manifests was `github.com/aarelaponin`. The install command in both
  READMEs, and the git remote, are `alaponin/ea-plays-kit`.
- The plugin README told a learner to download `ea-plays-<version>.plugin`. `package.sh`
  builds `ea-plays-v<version>.plugin`.
- Release 0.1.2 said that 0.1.1 "was tagged but never released". There is no `v0.1.1` tag,
  here or on the remote.
- The root README said that CI runs all four commands in the *Working on it* block. The
  fourth command loads the plugin for a session. CI runs the validation of the marketplace
  instead.

### Added

- **Criterion 3 also checks the version in the shared header example.** The example named
  `v0.1.3` in fifteen copies, and nothing kept it current. Release 0.1.3 changed it by hand.
  The checker now fails a release that changes `plugin.json` and forgets the example.

## [0.1.3] — 2026-09-05

Reference and documentation fixes. No skill contract changes.

### Fixed

- **`bdat-assessor/references/change-impact-template.md` carried the fixture marker but not
  the fixture's content.** Its filled example was the pre-review fork: "DGA" for PDGA, the
  learner registry "contested between MoEYS and DGA" where §2 assigns it to MoEYS, a backbone
  "not yet operational" where Linkup is live and the real gap is MoEYS membership, a sixth
  learner list where the fixture has three, and no Data Protection Act row under legal basis.
  Criterion 9 passed it because the deny-list encoded the first review's divergences, not
  these.
- **The workbook chain disagreed with itself in ten rows.** A6 said *Feeds 1.7* while A21
  (3.7) and A30 (5.5) both listed A6 under *Consumed*; A3, A7, A8, A11, A13, A16 and A26 had
  the same fault, A7's cell saying "Module 3" where 3.3 and 3.4 consume it. A skill filling
  its **Feeds** field from this file was under-reporting where its artefact goes. The header
  example, which copies the A6 row, inherited the error.
- Five programmes across **four** ministries, not five — §2 puts the National Learner
  Registry and the Scholarship Management Platform both under MoEYS.
- **Shared Platform**, PAERA's term, not "Shared Platform Provider".
- `change-impact-template.md` was listed twice in `bdat-assessor/SKILL.md`.
- The plugin README credited `bdat-assessor` with the metamodel conformance check. That is
  play 2.2 and `paera-reference-check`'s, whose own row already says so.

### Changed

- **`tests/README.md` owns the fixture rules and the acceptance criteria.** Both lived only
  in a CHANGELOG entry and checker comments; the criteria were cited by number in prose and
  never listed. They are now a table with a *Checked by* column, criterion 7 included as the
  manual row it has always been. Criteria 1, 4, 5 and 6 are written from what the tooling
  actually tests — the build plan that numbered them is not in this repo, and the README says
  so.
- **Every checker exemption earns its line.** `workbook-chain.md` and `source-tiers.md` leave
  `EXEMPT` (neither carries a fixture token); the three that stay carry a comment saying why.
  `GAMBIA_OK` becomes `REAL_COUNTRY_AS_COMPARATOR_OK`, and its failure message claims what it
  checks rather than "no real country leaks in".
- The two plan documents are committed under `docs/plans/`.

### Added

- **Criterion 10 — the workbook chain agrees with itself.** Parses the table and checks that
  every artefact a play consumes lists that play in its producer's *Feeds* cell. This is the
  class of error that had just happened; it found nine more instances of it. A0 is exempt —
  its Feeds cell is prose, and the section table above it does the routing.
- Three deny-list entries for the divergences above. `DENY` is a ledger of every divergence a
  review has found, not a snapshot of the last one.

## [0.1.2] — 2026-09-05

Packaging only. 0.1.1 was never released, so this is the first release carrying the
0.1.1 reference fixes below.

### Changed

- **`skills-standalone-<version>.zip` is no longer built.** The Claude app uploads one skill
  folder, so a zip of all fourteen under a `skills/` root made the learner unzip and re-zip
  anyway — which GitHub's own source download already gives them. `package.sh` now builds the
  Cowork `.plugin` alone, and the README points that route at the source tree.

## [0.1.1] — 2026-09-05

Reference fixes only. No skill contract changes.

### Fixed

- **The shared provenance-header example is a Progressa run.** It named a real country two
  lines above the rule that says fixture runs are `Progressa`, and attributed A6 to the wrong
  skill. It is now `A6 — Phase RACI and role-gap list`, `ea-governance-drafter`, consistent
  with `tests/plays/1.6/expected.md`.
- **`bdat-assessor/references/worked-example.md` rewritten against `tests/progressa.md`.** It
  had forked from the canonical fixture: MoEYS as "Youth and Sport", PDGA running payments,
  and a Learner Registry modelled as an operating body with an enrolment system. The fixture
  says Skills, says the Central Bank of Progressa operates PayPro, and says the PLR is planned
  and not started — its absence *is* the sector problem. Duplicate registries and
  point-to-point integration are now **Confirmed** findings with the fixture's evidence, not
  hypothetical risks, and the Civil Registration Department and Central Bank rows are present.
- **`ea-institution-mapper/references/paera-a1-2.md`** cited an "Establishment Decree 2019 §3"
  that the fixture does not contain. Replaced with PDGA's stated basis — a coordinating but not
  binding mandate, a unit under the Ministry of ICT — and a hybrid note pointing at the 2021
  Interoperability Framework, published but not applied.

### Changed

- **`bb-sourcing-researcher/references/worked-example.md` is a Progressa run.** It was a
  real-country analysis while `bdat-assessor`'s was Progressa — two example-country
  conventions in one kit. The eighteen product columns are unchanged; the country frame is the
  fixture's, and Identity, Payment and Information Mediator become *Reuse existing* (PNIA,
  PayPro, Linkup) rather than deploy-OSS postures. Analytics loses its extend-an-existing-
  platform argument.
- **The eight `tests/plays/1.*/gambia.md` baselines are removed.** The fixture tree is
  one-country, and real-country material does not belong in a public CC BY kit. They were
  excerpts of a synthesis document that is in no repo, covering 8 of 38 plays, and
  `check_fixtures.py` never read them. `tests/README.md` now says plainly that acceptance
  criterion 7 is a manual read against a private record and is not machine-checked.

### Added

- **Fixture marker and `Fixture material` convention**, enforced by `check_fixtures.py`
  criterion 9 — see `tests/README.md`.

## [0.1.0] — 2026-09-05

First release of the learner kit.

### Added

- **Fourteen skills** in one plugin, `ea-plays`. Eight new, four extensions of existing
  account skills, two carried over unchanged.
  - `cite-or-discard` — verifies claims against their sources; audit mode populates the
    4.2 source column. A refused fetch is *unverified*, never *unsupported*.
  - `country-context-pack` — Play 0 as the seven-section A0 pack. Extends
    `country-context-data`.
  - `bb-landscape-check` — which shared building blocks are actually live, with an
    *available to a new sector?* column.
  - `ea-institution-mapper` — bodies, legal mandates, systems, posts, and the full
    seven-type PAERA A1.2 classification with the teaching type in brackets.
  - `ea-legal-context` — the national legal register, with *enacted but not commenced* as
    its own status.
  - `ea-comparator-evidence` — comparator cards with primary sources and a mandatory
    contested case.
  - `ea-cost-case` — extends `govstack-cost-estimator`: assumptions first, benchmarks
    named, text tables not charts.
  - `paera-reference-check` — extends `paera-assessor`: checks against PAERA as published
    and says where the video's simplification was applied.
  - `ea-method-runner` — extends `ea-lifecycle-method`: reads the workbook, writes back
    with provenance, calls `bb-landscape-check` at sourcing, target and gate.
  - `ea-governance-drafter` — the seven institutional documents from the kit's own
    templates.
  - `ea-tool-evaluator` — verifiable attributes only, plus the ten-entity export test.
  - `ea-open-learning-catalogue` — every link fetched on the day it runs.
  - `bdat-assessor`, `bb-sourcing-researcher` — carried over unchanged.
- **`shared/`** — the four source tiers and the cite-or-discard loop, the nine-field
  provenance header, the six output-contract rules, and the A0–A31 workbook chain.
  `sync-shared.sh` copies them into every skill so each folder is self-contained.
- **`tests/`** — the canonical Progressa fixture, a folder for all 37 plays plus Play 0,
  eight real-country baselines (removed in 0.1.1), and `check_fixtures.py`.
- **`scripts/package.sh`** — the Cowork `.plugin` and the standalone skills zip.
- CI: `sync-shared.sh --check`, `check_fixtures.py`, and `claude plugin validate --strict`
  on both manifests.

### Notes

- **Skill names are frozen from this release.** Rename before the first GitBook page cites
  them, never after.
- **Artefact numbering:** A0–A8 are the published Module 1 numbering and are frozen.
  A9–A31 are defined in `shared/workbook-chain.md` for Modules 2–5 and are stable from
  this release.
- **PAERA v1.0.** The annex text is referenced by section and re-read from
  paera.govstack.global at run time rather than embedded — its licence terms for verbatim
  excerpts are unconfirmed. Embedding it is a future minor bump.
- The four extended originals (`country-context-data`, `paera-assessor`,
  `ea-lifecycle-method`, `govstack-cost-estimator`) are **not shipped**, so two skills
  never compete for one trigger. Their `references/` are inherited by the extensions.
  (The `v0.0.1-baseline` tag that held them was never pushed, and was deleted after
  0.2.1. See the note under 0.0.1-baseline below.)

## [0.0.1-baseline] — 2026-09-05

The six account skills exactly as exported from the Claude app, in no way modified, so that
every extension is a diff against a versioned baseline. Not a release.

**The tag is gone.** It stayed on one machine and nobody pushed it, so no person who
cloned this repository could reach it. It was deleted after 0.2.1, with the 0.1 tags. The
four extended originals are therefore in no tag of this repository. Their content survives
in the `references/` folder of the skill that extends each one, which is where a reader
needs it.
