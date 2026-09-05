# Play 1.3 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes when
each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** A3 — Re-use business case · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** ea-cost-case v<version> · **Consumed** A0 §2, A1 · **Feeds** <play ids from workbook-chain.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The artefact

a per-programme cost table plus a country-level 5-year saving estimate, plus the realisation-conditions note

The prompt of the play says: per-programme table showing the local cost of 'do it yourself' (cheaper for this project) vs the local cost of 'consume the BB' (more expensive for this project), plus a country-level total over 5 years. End with a 'what makes this calculation work' note — the conditions (BB availability, governance authority, sustained funding, training capacity) that turn the country-level math from theoretical to realised

## The safeguard, given back as the next action for the learner

This is a directional calculation, not a costed business case. Use it to motivate a detailed costing exercise — do not present the per-programme numbers as quotations.

## Contract checks, for each play

- Text in the chat only: no file, no chart, no image, no screenshot.
- Posts, not names. The output names no real office-holder.
- The output has no analysis by the model before the provenance header.
- Each claim about the outside world carries its URL, its tier and its access date in the
  same line.
- The ⚠ count on line 3 of the header is equal to the number of ⚠ marks in the body.
