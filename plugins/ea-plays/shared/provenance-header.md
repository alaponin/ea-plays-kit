# The provenance header

Every artefact this kit produces opens with it. Three blockquote lines, before
any prose, any table and any reasoning.

```
> **Artefact** A6 — Phase RACI and role-gap list · **Country** Progressa · **Sector** Education · **Built** 2026-09-05
> **Skill** ea-governance-drafter v0.1.2 · **Consumed** A0 §4, A4, A5 · **Feeds** 1.7
> **Sources** 4 × Tier 1, 2 × Tier 2, 0 × Tier 3 · **Unverified lines** 1 (marked ⚠)
```

## The fields

| Field | Line | Rule |
| --- | --- | --- |
| **Artefact** | 1 | The workbook number and name, e.g. `A6 — Roles register`. Use `—` (em dash). If the output is not a numbered workbook artefact, write the artefact name alone. |
| **Country** | 1 | As the learner named it. `Progressa` for fixture runs. |
| **Sector** | 1 | The sector, or `—` where the artefact is whole-of-government. |
| **Built** | 1 | ISO date, the day the skill ran. |
| **Skill** | 2 | `<skill-name> v<version>`, the version from `plugin.json`. |
| **Consumed** | 2 | The A-numbered inputs actually read, with sections, e.g. `A0 §1, A0 §6`. `—` if the learner pasted free text. |
| **Feeds** | 2 | The play ids this artefact is an input to, from `workbook-chain.md`. |
| **Sources** | 3 | Counts by tier: `n × Tier 1, n × Tier 2, n × Tier 3`. Zeros are written, not omitted. |
| **Unverified lines** | 3 | How many lines carry ⚠, and `(marked ⚠)` when the count is above zero. `0` when everything verified. |

## Rules

- **All nine fields, always.** A field with no value gets `—`, never a blank or a
  dropped field. The fixture check in `tests/` fails on a missing field.
- **Before everything.** If the skill wants to say what it did, it says it after
  the header and after the artefact, never before.
- **A drafting skill still counts sources.** A document drafted from templates with
  two published exemplars is `2 × Tier 1, 0 × Tier 2, 0 × Tier 3` — not an absent
  Sources line.
- **⚠ travels.** The count on line 3 must equal the number of ⚠ marks in the body.
