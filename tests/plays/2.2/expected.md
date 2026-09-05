# Play 2.2 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes when
each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** A10 — Metamodel conformance report · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** paera-reference-check v<version> · **Consumed** a draft model, or the initiatives list · **Feeds** <play ids from workbook-chain.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The artefact

a mapping table plus lists of non-conforming elements, missing relationships, and suggested corrections

The prompt of the play says: a mapping table (my element / PAERA entity / note), then a list of non-conforming elements, then a list of missing relationships, then 3 suggested corrections

## The safeguard, given back as the next action for the learner

The check only sees what you paste, and a clean mapping is necessary but not sufficient — a model can conform to the metamodel and still be wrong about the real world. Confirm the entity assignments with the body that owns the systems before relying on the result.

## Contract checks, for each play

- Text in the chat only: no file, no chart, no image, no screenshot.
- Posts, not names. The output names no real office-holder.
- The output has no analysis by the model before the provenance header.
- Each claim about the outside world carries its URL, its tier and its access date in the
  same line.
- The ⚠ count on line 3 of the header is equal to the number of ⚠ marks in the body.
