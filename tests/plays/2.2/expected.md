# Play 2.2 — expected output shape

This states the **shape**, not the wording. A run passes when every line below is
present; the words will differ every time.

## Provenance header — the first three lines, before anything else

```
> **Artefact** A10 — Metamodel conformance report · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** paera-reference-check v<version> · **Consumed** a draft model, or the initiatives list · **Feeds** <play ids from workbook-chain.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields present. An empty field is `—`, never blank.

## The artefact

a mapping table plus lists of non-conforming elements, missing relationships, and suggested corrections

As the prompt states it: a mapping table (my element / PAERA entity / note), then a list of non-conforming elements, then a list of missing relationships, then 3 suggested corrections

## The safeguard, handed back as the learner's next action

The check only sees what you paste, and a clean mapping is necessary but not sufficient — a model can conform to the metamodel and still be wrong about the real world. Confirm the entity assignments with the body that owns the systems before relying on the result.

## Contract checks (all plays)

- Text in the chat only — no file, no chart, no image, no screenshot.
- Posts, not names. No real office-holder is named anywhere in the output.
- No model reasoning before the provenance header.
- Every claim about the outside world carries URL, tier and access date inline.
- The ⚠ count on header line 3 equals the number of ⚠ marks in the body.
