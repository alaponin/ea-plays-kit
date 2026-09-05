# Play 2.6 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes when
each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** A14 — Scored gap analysis · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** bdat-assessor v<version> · **Consumed** A13, A11 · **Feeds** <play ids from workbook-chain.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The artefact

a scored gap table, per-layer maturity scores, and the top-three priority gaps with rationale

The prompt of the play says: a gap table, a per-layer maturity line, and the top-three rationale

## The safeguard, given back as the next action for the learner

The model ranks only what you give it — a gap you did not capture cannot be scored. And any severity judgment that touches a politically powerful body must be validated with the decision-maker, not softened by the model; the honesty of the assessment is yours to defend, not the tool's.

## Contract checks, for each play

- Text in the chat only: no file, no chart, no image, no screenshot.
- Posts, not names. The output names no real office-holder.
- The output has no analysis by the model before the provenance header.
- Each claim about the outside world carries its URL, its tier and its access date in the
  same line.
- The ⚠ count on line 3 of the header is equal to the number of ⚠ marks in the body.
