# KP2 play 5.1 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes when
each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** B28 — Implementation plan: phased schedule, investment, procurement, workforce, risk register and metrics · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** ea-method-runner v<version> · **Consumed** B5, B6 · **Feeds** <play ids from workbook-chain-kp2.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The artefact

the phased schedule plus the investment plan, procurement plan, workforce plan, and risk register with success metrics

The prompt of the play says: the five parts plus a one-line funding ask per phase

## The safeguard, given back as the next action for the learner

Cost and duration figures are the most scrutinised and the easiest to get wrong — treat every number as [confirm] and benchmark it against documented comparable builds before putting it in front of a funder.

## Contract checks, for each play

- Text in the chat only: no file, no chart, no image, no screenshot.
- Posts, not names. The output names no real office-holder.
- The output has no analysis by the model before the provenance header.
- Each claim about the outside world carries its URL, its tier and its access date in the
  same line.
- Every identifier, code value and legal citation the country's own registries or statutes
  must confirm is marked `[confirm]`; the skill invents none.
- The ⚠ count on line 3 of the header is equal to the number of ⚠ marks in the body.
