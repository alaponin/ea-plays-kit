# Play 3.7 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes when
each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** A21 — Sustainment risk register · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** ea-governance-drafter v<version> · **Consumed** A20, A6 · **Feeds** <play ids from workbook-chain.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The artefact

a four-row sustainment risk register plus early-warning signals

The prompt of the play says: a risk register table plus the list of early-warning signals to watch

## The safeguard, given back as the next action for the learner

The early-warning signals are the point — a sustainment risk you only notice once it has happened is unmanageable. Confirm someone is actually watching each signal (months-since-last-Board-meeting is useless if no one checks it), or the register is just a tidy list of the ways the practice will quietly fail.

## Contract checks, for each play

- Text in the chat only: no file, no chart, no image, no screenshot.
- Posts, not names. The output names no real office-holder.
- The output has no analysis by the model before the provenance header.
- Each claim about the outside world carries its URL, its tier and its access date in the
  same line.
- The ⚠ count on line 3 of the header is equal to the number of ⚠ marks in the body.
