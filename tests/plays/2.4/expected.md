# Play 2.4 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes when
each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** A12 — Body classification profile · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** ea-institution-mapper v<version> · **Consumed** A0 §6 · **Feeds** <play ids from workbook-chain.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The artefact

a classification, an expected-profile table, and confirmation questions

The prompt of the play says: classification, expected-profile table, confirmation questions

## The safeguard, given back as the next action for the learner

The classification is a hypothesis, and many real bodies straddle types or have drifted from their mandate. Confirm against the body's actual legal mandate and current practice before you record the classification — a wrong type sends the whole interview looking for the wrong things.

## Contract checks, for each play

- Text in the chat only: no file, no chart, no image, no screenshot.
- Posts, not names. The output names no real office-holder.
- The output has no analysis by the model before the provenance header.
- Each claim about the outside world carries its URL, its tier and its access date in the
  same line.
- The ⚠ count on line 3 of the header is equal to the number of ⚠ marks in the body.
