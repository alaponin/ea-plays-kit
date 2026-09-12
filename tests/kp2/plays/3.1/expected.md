# KP2 play 3.1 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes when
each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** B14 — Owner's mandate, regulator and operator split · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** ea-institution-mapper v<version> · **Consumed** A0 §6, B4 · **Feeds** <play ids from workbook-chain-kp2.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The artefact

a mandate statement with the regulator and operator hats separated, plus a list of mandate gaps

The prompt of the play says: a one-page mandate plus a list of mandate gaps to close

## The safeguard, given back as the next action for the learner

Hosting the Operating Authority in an existing agency often requires a legal change to its mandate — treat every power the body does not already hold as a gap for legal counsel to close, not an assumption, and confirm the budget is a standing line, not a one-off project grant that disappears in year two.

## Contract checks, for each play

- Text in the chat only: no file, no chart, no image, no screenshot.
- Posts, not names. The output names no real office-holder.
- The output has no analysis by the model before the provenance header.
- Each claim about the outside world carries its URL, its tier and its access date in the
  same line.
- Every identifier, code value and legal citation the country's own registries or statutes
  must confirm is marked `[confirm]`; the skill invents none.
- The ⚠ count on line 3 of the header is equal to the number of ⚠ marks in the body.
