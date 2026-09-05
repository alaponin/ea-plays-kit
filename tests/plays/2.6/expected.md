# Play 2.6 — expected output shape

This states the **shape**, not the wording. A run passes when every line below is
present; the words will differ every time.

## Provenance header — the first three lines, before anything else

```
> **Artefact** A14 — Scored gap analysis · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** bdat-assessor v<version> · **Consumed** A13, A11 · **Feeds** <play ids from workbook-chain.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields present. An empty field is `—`, never blank.

## The artefact

a scored gap table, per-layer maturity scores, and the top-three priority gaps with rationale

As the prompt states it: a gap table, a per-layer maturity line, and the top-three rationale

## The safeguard, handed back as the learner's next action

The model ranks only what you give it — a gap you did not capture cannot be scored. And any severity judgment that touches a politically powerful body must be validated with the decision-maker, not softened by the model; the honesty of the assessment is yours to defend, not the tool's.

## Contract checks (all plays)

- Text in the chat only — no file, no chart, no image, no screenshot.
- Posts, not names. No real office-holder is named anywhere in the output.
- No model reasoning before the provenance header.
- Every claim about the outside world carries URL, tier and access date inline.
- The ⚠ count on header line 3 equals the number of ⚠ marks in the body.
