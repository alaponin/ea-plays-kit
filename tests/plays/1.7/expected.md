# Play 1.7 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes when
each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** A7 — EA Governance Board ToR · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** ea-governance-drafter v<version> · **Consumed** A0 §4, A0 §7, A3, A6 · **Feeds** <play ids from workbook-chain.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The artefact

a structured ToR document

The prompt of the play says: structured Terms of Reference ready to circulate for cabinet approval

## The safeguard, given back as the next action for the learner

Have the country's legal counsel review the document before it is formally adopted — particularly the 'binding decision scope' section, which interacts with existing sectoral legislation.

## Contract checks, for each play

- Text in the chat only: no file, no chart, no image, no screenshot.
- Posts, not names. The output names no real office-holder.
- The output has no analysis by the model before the provenance header.
- Each claim about the outside world carries its URL, its tier and its access date in the
  same line.
- The ⚠ count on line 3 of the header is equal to the number of ⚠ marks in the body.
