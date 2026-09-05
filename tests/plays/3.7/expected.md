# Play 3.7 — expected output shape

This states the **shape**, not the wording. A run passes when every line below is
present; the words will differ every time.

## Provenance header — the first three lines, before anything else

```
> **Artefact** A21 — Sustainment risk register · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** ea-governance-drafter v<version> · **Consumed** A20, A6 · **Feeds** <play ids from workbook-chain.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields present. An empty field is `—`, never blank.

## The artefact

a four-row sustainment risk register plus early-warning signals

As the prompt states it: a risk register table plus the list of early-warning signals to watch

## The safeguard, handed back as the learner's next action

The early-warning signals are the point — a sustainment risk you only notice once it has happened is unmanageable. Confirm someone is actually watching each signal (months-since-last-Board-meeting is useless if no one checks it), or the register is just a tidy list of the ways the practice will quietly fail.

## Contract checks (all plays)

- Text in the chat only — no file, no chart, no image, no screenshot.
- Posts, not names. No real office-holder is named anywhere in the output.
- No model reasoning before the provenance header.
- Every claim about the outside world carries URL, tier and access date inline.
- The ⚠ count on header line 3 equals the number of ⚠ marks in the body.
