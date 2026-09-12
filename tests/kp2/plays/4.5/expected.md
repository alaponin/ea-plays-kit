# KP2 play 4.5 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes when
each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** B24 — OpenAPI service contract · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** gif-openapi-gen v<version> · **Consumed** B23, B22 · **Feeds** <play ids from workbook-chain-kp2.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The artefact

an OpenAPI 3.x contract with [confirm] placeholders, plus X-Road service-description notes

The prompt of the play says: the OpenAPI document (YAML), a list of [confirm] items, and the X-Road service-description notes

## The safeguard, given back as the next action for the learner

An OpenAPI contract that names fields the provider does not actually expose fails at the first real call — confirm every path and field against the provider system's real interface (not its documentation alone, which drifts) before publishing the contract or deriving the X-Road service description.

## Contract checks, for each play

- Text in the chat only: no file, no chart, no image, no screenshot.
- Posts, not names. The output names no real office-holder.
- The output has no analysis by the model before the provenance header.
- Each claim about the outside world carries its URL, its tier and its access date in the
  same line.
- Every identifier, code value and legal citation the country's own registries or statutes
  must confirm is marked `[confirm]`; the skill invents none.
- The ⚠ count on line 3 of the header is equal to the number of ⚠ marks in the body.
