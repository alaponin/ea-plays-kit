# KP2 play 5.7 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes when
each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** B34 — Demonstration-to-production gap checklist · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** ea-method-runner v<version> · **Consumed** B32, B28 · **Feeds** <play ids from workbook-chain-kp2.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The artefact

a demonstration-to-production gap checklist mapped to the phased plan and cost frame

The prompt of the play says: a gap checklist (area / demo / production / phase / cost-bearing?) plus a one-line 'do not ship the demo as production' caution

## The safeguard, given back as the next action for the learner

The gap checklist is a planning aid, not a security sign-off — production hardening and audit must be done and independently reviewed, not merely listed.

## Contract checks, for each play

- Text in the chat only: no file, no chart, no image, no screenshot.
- Posts, not names. The output names no real office-holder.
- The output has no analysis by the model before the provenance header.
- Each claim about the outside world carries its URL, its tier and its access date in the
  same line.
- Every identifier, code value and legal citation the country's own registries or statutes
  must confirm is marked `[confirm]`; the skill invents none.
- The ⚠ count on line 3 of the header is equal to the number of ⚠ marks in the body.
