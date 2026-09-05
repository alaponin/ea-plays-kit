# Play 1.5 — expected output shape

This states the **shape**, not the wording. A run passes when every line below is
present; the words will differ every time.

## Provenance header — the first three lines, before anything else

```
> **Artefact** A5 — PAERA foundation coverage map · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** paera-reference-check v<version> · **Consumed** A0 §2, the initiatives list, A1 · **Feeds** <play ids from workbook-chain.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields present. An empty field is `—`, never blank.

## The artefact

a per-initiative coverage table plus a coverage summary

As the prompt states it: per-initiative table plus 3-bullet summary

## The safeguard, handed back as the learner's next action

An initiative that says 'we have principles' may not have PAERA-aligned principles — confirm coverage by reading the actual document, not the marketing summary.

## Contract checks (all plays)

- Text in the chat only — no file, no chart, no image, no screenshot.
- Posts, not names. No real office-holder is named anywhere in the output.
- No model reasoning before the provenance header.
- Every claim about the outside world carries URL, tier and access date inline.
- The ⚠ count on header line 3 equals the number of ⚠ marks in the body.
