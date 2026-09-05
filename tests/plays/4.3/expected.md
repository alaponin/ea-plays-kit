# Play 4.3 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes when
each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** A14 rev.2 — Ranked gap analysis · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** ea-method-runner v<version> · **Consumed** A23, A14 · **Feeds** <play ids from workbook-chain.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The artefact

capability maturity scores, a ranked gap table, and the honesty flags

The prompt of the play says: a maturity table, a ranked gap table, and the honesty flags

## The safeguard, given back as the next action for the learner

The ranking is only as honest as the inputs. A gap that involves a powerful body must be validated with the decision-maker, not softened by the model — the honesty of the assessment is yours to defend, and softening it is exactly the failure that surfaces a year later.

## Contract checks, for each play

- Text in the chat only: no file, no chart, no image, no screenshot.
- Posts, not names. The output names no real office-holder.
- The output has no analysis by the model before the provenance header.
- Each claim about the outside world carries its URL, its tier and its access date in the
  same line.
- The ⚠ count on line 3 of the header is equal to the number of ⚠ marks in the body.
