# Play 3.2 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes when
each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** A17 — EA tool comparison + export test · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** ea-tool-evaluator v<version> · **Consumed** A16 and a candidate list · **Feeds** <play ids from workbook-chain.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The artefact

a scored comparison table plus a recommendation

The prompt of the play says: a comparison table plus a recommendation

## The safeguard, given back as the next action for the learner

Vendor claims of 'open' and 'exports everything' must be tested with a real export of real data before you sign — a demo is not a test. Score the export you actually performed, not the one the brochure promises.

## Contract checks, for each play

- Text in the chat only: no file, no chart, no image, no screenshot.
- Posts, not names. The output names no real office-holder.
- The output has no analysis by the model before the provenance header.
- Each claim about the outside world carries its URL, its tier and its access date in the
  same line.
- The ⚠ count on line 3 of the header is equal to the number of ⚠ marks in the body.
