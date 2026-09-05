# Play 4.3 — expected output shape

This states the **shape**, not the wording. A run passes when every line below is
present; the words will differ every time.

## Provenance header — the first three lines, before anything else

```
> **Artefact** A14 rev.2 — Ranked gap analysis · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** ea-method-runner v<version> · **Consumed** A23, A14 · **Feeds** <play ids from workbook-chain.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields present. An empty field is `—`, never blank.

## The artefact

capability maturity scores, a ranked gap table, and the honesty flags

As the prompt states it: a maturity table, a ranked gap table, and the honesty flags

## The safeguard, handed back as the learner's next action

The ranking is only as honest as the inputs. A gap that involves a powerful body must be validated with the decision-maker, not softened by the model — the honesty of the assessment is yours to defend, and softening it is exactly the failure that surfaces a year later.

## Contract checks (all plays)

- Text in the chat only — no file, no chart, no image, no screenshot.
- Posts, not names. No real office-holder is named anywhere in the output.
- No model reasoning before the provenance header.
- Every claim about the outside world carries URL, tier and access date inline.
- The ⚠ count on header line 3 equals the number of ⚠ marks in the body.
