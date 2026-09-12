# KP2 play 4.6 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes when
each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** B25 — Bronze/silver/gold source map · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** gif-semantic-map v<version> · **Consumed** B23 · **Feeds** <play ids from workbook-chain-kp2.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The artefact

a bronze/silver/gold pipeline plan plus a path-onto-the-bus checklist

The prompt of the play says: the pipeline plan stage by stage, plus a checklist of what must be confirmed against the real source before go-live

## The safeguard, given back as the next action for the learner

The de-duplication identifier in the silver stage is the highest-risk decision — a non-unique key merges records for different people.

## Contract checks, for each play

- Text in the chat only: no file, no chart, no image, no screenshot.
- Posts, not names. The output names no real office-holder.
- The output has no analysis by the model before the provenance header.
- Each claim about the outside world carries its URL, its tier and its access date in the
  same line.
- Every identifier, code value and legal citation the country's own registries or statutes
  must confirm is marked `[confirm]`; the skill invents none.
- The ⚠ count on line 3 of the header is equal to the number of ⚠ marks in the body.
