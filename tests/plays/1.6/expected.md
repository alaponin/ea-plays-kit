# Play 1.6 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes when
each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** A6 — Phase RACI and role-gap list · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** ea-governance-drafter v<version> · **Consumed** A0 §4, A4, A5 · **Feeds** <play ids from workbook-chain.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The artefact

a per-phase RACI matrix plus a list of role gaps to resolve

The prompt of the play says: a 5-row RACI table (one row per phase, columns R/A/C/I) plus a 'role gaps' list at the end

## The safeguard, given back as the next action for the learner

A RACI is only as useful as the people named in it have actual authority — if the 'Accountable' role for a phase is unclear in the country, the gap matters more than the matrix.

## Contract checks, for each play

- Text in the chat only: no file, no chart, no image, no screenshot.
- Posts, not names. The output names no real office-holder.
- The output has no analysis by the model before the provenance header.
- Each claim about the outside world carries its URL, its tier and its access date in the
  same line.
- The ⚠ count on line 3 of the header is equal to the number of ⚠ marks in the body.
