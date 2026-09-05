# Play 1.4 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes when
each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** A4 — Joint business–IT agenda · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** ea-legal-context v<version> · **Consumed** A0 §3, A2 · **Feeds** <play ids from workbook-chain.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The artefact

a 3-column decomposition plus a meeting agenda

The prompt of the play says: a 3-column table (business / IT / joint), plus a 5-bullet 'agenda for the first joint meeting' with named decisions

## The safeguard, given back as the next action for the learner

The decomposition is a starting structure for the conversation, not a verdict. The actual lines between 'business decision' and 'IT decision' are politically negotiated in every country — use the output to surface the conversation, not to settle it.

## Contract checks, for each play

- Text in the chat only: no file, no chart, no image, no screenshot.
- Posts, not names. The output names no real office-holder.
- The output has no analysis by the model before the provenance header.
- Each claim about the outside world carries its URL, its tier and its access date in the
  same line.
- The ⚠ count on line 3 of the header is equal to the number of ⚠ marks in the body.
