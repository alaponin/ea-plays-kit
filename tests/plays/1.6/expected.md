# Play 1.6 — expected output shape

This states the **shape**, not the wording. A run passes when every line below is
present; the words will differ every time.

## Provenance header — the first three lines, before anything else

```
> **Artefact** A6 — Phase RACI and role-gap list · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** ea-governance-drafter v<version> · **Consumed** A0 §4, A4, A5 · **Feeds** <play ids from workbook-chain.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields present. An empty field is `—`, never blank.

## The artefact

a per-phase RACI matrix plus a list of role gaps to resolve

As the prompt states it: a 5-row RACI table (one row per phase, columns R/A/C/I) plus a 'role gaps' list at the end

## The safeguard, handed back as the learner's next action

A RACI is only as useful as the people named in it have actual authority — if the 'Accountable' role for a phase is unclear in the country, the gap matters more than the matrix.

## Contract checks (all plays)

- Text in the chat only — no file, no chart, no image, no screenshot.
- Posts, not names. No real office-holder is named anywhere in the output.
- No model reasoning before the provenance header.
- Every claim about the outside world carries URL, tier and access date inline.
- The ⚠ count on header line 3 equals the number of ⚠ marks in the body.
