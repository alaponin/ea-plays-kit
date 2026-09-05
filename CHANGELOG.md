# Changelog

Semver in both manifests, bumped together. **Patch:** a source-tier or reference fix.
**Minor:** a new skill, a changed output contract, or a PAERA version change (named here).
**Major:** reserved for a workbook-chain change that breaks artefact numbering.

Video descriptions and the GitBook link the install command, never a release number.

## [Unreleased]

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
- **`skills-standalone-<version>.zip` is no longer built.** The Claude app uploads one skill
  folder, so a zip of all fourteen under a `skills/` root made the learner unzip and re-zip
  anyway — which GitHub's own source download already gives them. `package.sh` now builds the
  Cowork `.plugin` alone, and the README points that route at the source tree.
- **The eight `tests/plays/1.*/gambia.md` baselines are removed.** The fixture tree is
  one-country, and real-country material does not belong in a public CC BY kit. They were
  excerpts of a synthesis document that is in no repo, covering 8 of 38 plays, and
  `check_fixtures.py` never read them. `tests/README.md` now says plainly that acceptance
  criterion 7 is a manual read against a private record and is not machine-checked.

### Added

- **A fixture marker.** Every file under `plugins/` that carries Progressa material opens with
  `<!-- fixture: Progressa (fictional) · canonical: tests/progressa.md · keep consistent with
  it -->`, and its `SKILL.md` declares it under a `Fixture material` sub-heading. A skill is
  not "a Progressa skill"; a file contains fixture material, and it says so — the
  standalone-upload route has no `tests/` to point at.
- **`check_fixtures.py` acceptance criterion 9.** Enforces the above rather than requesting
  it: fixture tokens require the marker, a deny-list catches each divergence the 2026-09-05
  review found, no file outside `known-frameworks.md` and `api-guide.md` may name a real
  comparator country as its own context, and `tests/plays/*/` may hold only `input.md` and
  `expected.md`.

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
  `ea-lifecycle-method`, `govstack-cost-estimator`) are in the `v0.0.1-baseline` tag but
  are **not shipped**, so two skills never compete for one trigger. Their `references/`
  are inherited by the extensions.

## [0.0.1-baseline] — 2026-09-05

The six account skills exactly as exported from the Claude app, in no way modified, so that
every extension is a diff against a versioned baseline. Not a release.
