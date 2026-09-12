# The provenance header

Each artefact from this kit starts with the provenance header. The header has three
blockquote lines. Put the header before all prose, all tables, and all analysis.

```
> **Artefact** A6 — Phase RACI and role-gap list · **Country** Progressa · **Sector** Education · **Built** 2026-09-05
> **Skill** ea-governance-drafter v0.3.0 · **Consumed** A0 §4, A4, A5 · **Feeds** 1.7, 3.7, 5.5
> **Sources** 4 × Tier 1, 2 × Tier 2, 0 × Tier 3 · **Unverified lines** 1 (marked ⚠)
```

## The fields

| Field | Line | Rule |
| --- | --- | --- |
| **Artefact** | 1 | The number and the name of the workbook artefact, for example `A6 — Roles register`. Use the em dash `—`. A KP1 artefact is A-numbered; a KP2 artefact is B-numbered, for example `B11 — Operative article draft`. If the output is not a numbered workbook artefact, write only the name. |
| **Country** | 1 | The country as the learner named it. Write `Progressa` for a fixture run. |
| **Sector** | 1 | The sector. Write `—` if the artefact applies to all of government. |
| **Built** | 1 | The date in ISO format. Use the day that the skill ran. |
| **Skill** | 2 | `<skill-name> v<version>`. Take the version from `plugin.json`. |
| **Consumed** | 2 | The A-numbered inputs that you read, with their sections, for example `A0 §1, A0 §6`. Write `—` if the learner gave free text. |
| **Feeds** | 2 | The play ids that use this artefact as an input. Take them from `workbook-chain.md` for an A-artefact and from `workbook-chain-kp2.md` for a B-artefact. |
| **Sources** | 3 | The count for each tier: `n × Tier 1, n × Tier 2, n × Tier 3`. Write the zeros. Do not omit them. |
| **Unverified lines** | 3 | The number of lines that have a ⚠ mark. Add `(marked ⚠)` if the number is more than zero. Write `0` if you verified all lines. |

## Rules

- **Write all nine fields each time.** If a field has no value, write `—`. Do not
  write a blank. Do not remove the field. The fixture check in `tests/` fails if a
  field is missing.
- **Put the header first.** A skill can tell what it did after the header and after
  the artefact. It must not do this before them.
- **A skill that writes documents also counts its sources.** A document that comes
  from templates and two published exemplars is `2 × Tier 1, 0 × Tier 2, 0 × Tier 3`.
  It is not an absent Sources line.
- **Keep the ⚠ marks together.** The count on line 3 must be equal to the number of ⚠
  marks in the body.
