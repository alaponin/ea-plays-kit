# KP2 play 2.6 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes when
each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** B13 — Legal acceptance check · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** gif-consistency-check v<version> · **Consumed** B5, B11 · **Feeds** <play ids from workbook-chain-kp2.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The artefact

a coverage table plus lists of uncovered exchanges and over-reaching articles

The prompt of the play says: a coverage table (catalogue exchange / authorising article / status), a list of NOT COVERED exchanges, and a list of OVER-REACHING articles — each with a one-line note on the fix

## The safeguard, given back as the next action for the learner

This check tests alignment between two of your own documents — it is not a ruling on whether an article is lawful or well-drafted.

## Contract checks, for each play

- Text in the chat only: no file, no chart, no image, no screenshot.
- Posts, not names. The output names no real office-holder.
- The output has no analysis by the model before the provenance header.
- Each claim about the outside world carries its URL, its tier and its access date in the
  same line.
- Every identifier, code value and legal citation the country's own registries or statutes
  must confirm is marked `[confirm]`; the skill invents none.
- The ⚠ count on line 3 of the header is equal to the number of ⚠ marks in the body.
