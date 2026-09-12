# KP2 play 1.3 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes when
each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** B3 — Highest-value once-only exchange · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** country-context-pack v<version> · **Consumed** A0 §2, A0 §9 · **Feeds** <play ids from workbook-chain-kp2.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The artefact

a ranked once-only opportunity table plus a first-exchange recommendation

The prompt of the play says: a ranked table (repeated fact / authoritative source / services that re-ask it / rough annual interactions affected / build difficulty Low-Med-High), and recommend the single best first once-only exchange to build

## The safeguard, given back as the next action for the learner

The interaction estimates are directional, for prioritisation only — confirm the authoritative source agency actually holds the fact reliably (a registry that is incomplete is not yet a trusted source) before committing it as the first build.

## Contract checks, for each play

- Text in the chat only: no file, no chart, no image, no screenshot.
- Posts, not names. The output names no real office-holder.
- The output has no analysis by the model before the provenance header.
- Each claim about the outside world carries its URL, its tier and its access date in the
  same line.
- Every identifier, code value and legal citation the country's own registries or statutes
  must confirm is marked `[confirm]`; the skill invents none.
- The ⚠ count on line 3 of the header is equal to the number of ⚠ marks in the body.
