# Changelog

Semver in both manifests, bumped together. **Patch:** a source-tier or reference fix.
**Minor:** a new skill, a changed output contract, or a PAERA version change (named here).
**Major:** reserved for a workbook-chain change that breaks artefact numbering.

Video descriptions and the GitBook link the install command, never a release number.

## [Unreleased]

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
  eight Gambia baselines, and `check_fixtures.py`.
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
