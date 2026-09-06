# Play 5.1 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes when
each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** A8 — Comparator-country cards, sourced · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** ea-comparator-evidence v<version> · **Consumed** A0 §5 · **Feeds** <play ids from workbook-chain.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The artefact

comparator cards with cited sources, a recurring-elements synthesis, and a lessons summary

The prompt of the play says: per-country cards, the recurring-elements synthesis, and a 'most transferable lessons' summary

## The safeguard, given back as the next action for the learner

Cite or discard — AI invents plausible citations. Open the source for every example and discard any whose source does not document the claim. Include the contested cases honestly; a proof case built only on flattering, unverified examples collapses the first time a sharp official checks one.

## Contract checks, for each play

- Text in the chat only: no file, no chart, no image, no screenshot.
- Posts, not names. The output names no real office-holder.
- The output has no analysis by the model before the provenance header.
- Each claim about the outside world carries its URL, its tier and its access date in the
  same line.
- The ⚠ count on line 3 of the header is equal to the number of ⚠ marks in the body.
