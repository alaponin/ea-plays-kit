# KP2 play 3.3 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes when
each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** B16 — Governance RACI · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** ea-governance-drafter v<version> · **Consumed** B15, B6 · **Feeds** <play ids from workbook-chain-kp2.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The artefact

a RACI matrix plus a list of deadlock/drift risks and authority gaps

The prompt of the play says: the RACI table (one row per decision), then a list of deadlock/drift risks and authority gaps to resolve

## The safeguard, given back as the next action for the learner

A RACI only works if each Accountable body actually has the authority its row claims — verify that against the governance mandates and, where the decision compels an agency (suspension, mandatory connection), against the decree.

## Contract checks, for each play

- Text in the chat only: no file, no chart, no image, no screenshot.
- Posts, not names. The output names no real office-holder.
- The output has no analysis by the model before the provenance header.
- Each claim about the outside world carries its URL, its tier and its access date in the
  same line.
- Every identifier, code value and legal citation the country's own registries or statutes
  must confirm is marked `[confirm]`; the skill invents none.
- The ⚠ count on line 3 of the header is equal to the number of ⚠ marks in the body.
