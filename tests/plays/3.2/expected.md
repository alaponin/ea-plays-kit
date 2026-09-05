# Play 3.2 — expected output shape

This states the **shape**, not the wording. A run passes when every line below is
present; the words will differ every time.

## Provenance header — the first three lines, before anything else

```
> **Artefact** A17 — EA tool comparison + export test · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** ea-tool-evaluator v<version> · **Consumed** A16 and a candidate list · **Feeds** <play ids from workbook-chain.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields present. An empty field is `—`, never blank.

## The artefact

a scored comparison table plus a recommendation

As the prompt states it: a comparison table plus a recommendation

## The safeguard, handed back as the learner's next action

Vendor claims of 'open' and 'exports everything' must be tested with a real export of real data before you sign — a demo is not a test. Score the export you actually performed, not the one the brochure promises.

## Contract checks (all plays)

- Text in the chat only — no file, no chart, no image, no screenshot.
- Posts, not names. No real office-holder is named anywhere in the output.
- No model reasoning before the provenance header.
- Every claim about the outside world carries URL, tier and access date inline.
- The ⚠ count on header line 3 equals the number of ⚠ marks in the body.
