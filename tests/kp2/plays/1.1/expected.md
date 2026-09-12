# KP2 play 1.1 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes when
each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** B1 — Procured-vs-planned diagnostic · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** country-context-pack v<version> · **Consumed** A0 §1, A0 §8 · **Feeds** <play ids from workbook-chain-kp2.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The artefact

a diagnostic table plus a 3-bullet summary

The prompt of the play says: a table (data need / how it is met now / planned-vs-procured / risk if the supplier changes), plus a 3-bullet summary of where a whole-of-government framework would most change the outcome. Be conservative — mark 'delivered by a shared mechanism' only if the input names one

## The safeguard, given back as the next action for the learner

Treat the output as a hypothesis to test with the agencies named, not a finding.

## Contract checks, for each play

- Text in the chat only: no file, no chart, no image, no screenshot.
- Posts, not names. The output names no real office-holder.
- The output has no analysis by the model before the provenance header.
- Each claim about the outside world carries its URL, its tier and its access date in the
  same line.
- Every identifier, code value and legal citation the country's own registries or statutes
  must confirm is marked `[confirm]`; the skill invents none.
- The ⚠ count on line 3 of the header is equal to the number of ⚠ marks in the body.
