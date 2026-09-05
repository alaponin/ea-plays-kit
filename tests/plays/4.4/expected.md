# Play 4.4 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes when
each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** A24 — Sourcing matrix · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** ea-method-runner v<version> · **Consumed** A14 rev.2, BB status register · **Feeds** <play ids from workbook-chain.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The artefact

a build/buy/share/sandbox matrix with flags

The prompt of the play says: a sourcing matrix (block / call / reason) plus the flags

## The safeguard, given back as the next action for the learner

A BUY or BUILD that looks cheapest for one project may be costliest for the country. Check each call against the whole-sector view and the existing shared platforms before approving — the model sees only what you paste, and a duplication it misses becomes the next fragmentation.

## Contract checks, for each play

- Text in the chat only: no file, no chart, no image, no screenshot.
- Posts, not names. The output names no real office-holder.
- The output has no analysis by the model before the provenance header.
- Each claim about the outside world carries its URL, its tier and its access date in the
  same line.
- The ⚠ count on line 3 of the header is equal to the number of ⚠ marks in the body.
