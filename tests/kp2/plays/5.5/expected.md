# KP2 play 5.5 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes when
each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** B32 — Federation stand-up run book · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** gif-federation-standup v<version> · **Consumed** B31 · **Feeds** <play ids from workbook-chain-kp2.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The artefact

an ordered, reproducible stand-up run book with production-difference notes

The prompt of the play says: the ordered run book plus a 'differs in production' note per step

## The safeguard, given back as the next action for the learner

A run book is only reproducible if it has been run — execute it end to end in the sandbox and confirm all four members register, before treating it as the build-pack run book.

## Contract checks, for each play

- Text in the chat only: no file, no chart, no image, no screenshot.
- Posts, not names. The output names no real office-holder.
- The output has no analysis by the model before the provenance header.
- Each claim about the outside world carries its URL, its tier and its access date in the
  same line.
- Every identifier, code value and legal citation the country's own registries or statutes
  must confirm is marked `[confirm]`; the skill invents none.
- The ⚠ count on line 3 of the header is equal to the number of ⚠ marks in the body.
