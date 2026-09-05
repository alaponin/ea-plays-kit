# Play 1.3 — expected output shape

This states the **shape**, not the wording. A run passes when every line below is
present; the words will differ every time.

## Provenance header — the first three lines, before anything else

```
> **Artefact** A3 — Re-use business case · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** ea-cost-case v<version> · **Consumed** A0 §2, A1 · **Feeds** <play ids from workbook-chain.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields present. An empty field is `—`, never blank.

## The artefact

a per-programme cost table plus a country-level 5-year saving estimate, plus the realisation-conditions note

As the prompt states it: per-programme table showing the local cost of 'do it yourself' (cheaper for this project) vs the local cost of 'consume the BB' (more expensive for this project), plus a country-level total over 5 years. End with a 'what makes this calculation work' note — the conditions (BB availability, governance authority, sustained funding, training capacity) that turn the country-level math from theoretical to realised

## The safeguard, handed back as the learner's next action

This is a directional calculation, not a costed business case. Use it to motivate a detailed costing exercise — do not present the per-programme numbers as quotations.

## Contract checks (all plays)

- Text in the chat only — no file, no chart, no image, no screenshot.
- Posts, not names. No real office-holder is named anywhere in the output.
- No model reasoning before the provenance header.
- Every claim about the outside world carries URL, tier and access date inline.
- The ⚠ count on header line 3 equals the number of ⚠ marks in the body.
