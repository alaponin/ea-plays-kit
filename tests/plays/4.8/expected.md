# Play 4.8 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes when
each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** A28 — Sector transfer plan · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** ea-method-runner v<version> · **Consumed** A26, A0 §6 for the next sector · **Feeds** <play ids from workbook-chain.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The artefact

a one-page transfer plan (classification, the high-priority use case, the six deliverables, the first two waves)

The prompt of the play says: a one-page transfer plan under those four headings

## The safeguard, given back as the next action for the learner

The transfer plan is a starting structure, not a substitute for running Discovery and Assess on the real sector. Confirm the gaps it assumes by actually looking — the duplicated domain it guesses may differ from what you find — before committing a roadmap or a budget to it.

## Contract checks, for each play

- Text in the chat only: no file, no chart, no image, no screenshot.
- Posts, not names. The output names no real office-holder.
- The output has no analysis by the model before the provenance header.
- Each claim about the outside world carries its URL, its tier and its access date in the
  same line.
- The ⚠ count on line 3 of the header is equal to the number of ⚠ marks in the body.
