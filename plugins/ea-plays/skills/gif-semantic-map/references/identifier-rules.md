# The linking identifier

The identifier is the field that says *this record in agency A is the same person as
that record in agency B*. It is the one decision in the semantic map that can cause harm
on its own. Describe it in five parts. Never leave one of the five out.

| Part | What to write | Where it comes from |
| --- | --- | --- |
| What it is | the field, its format, the issuing body | A0 §1, §6; the agencies' field lists |
| Who issues it, and when | the body; the age or event at which a person receives it | A0 §1 (a national ID issued at 16 does not identify a child of 9); the register's own rules |
| Coverage | the share of the population that holds one, by the group the exchange serves | A0 §1, §5; the BB status register |
| Fallback | what links a record that has no identifier — and what does *not* (a name-and-birthdate composite merges twins and namesakes; a school-issued number is not unique across schools) | your analysis, stated as `[confirm]` |
| Risk | what happens if it is not unique (records of two people merge) and if it is missing (a person is dropped, or asked again — the once-only promise fails for exactly the people with the least documentation) | your analysis |

## Rules

1. **Every identifier value is `[confirm: check against the live registry]`.** A format
   in a document is not the format in the database. A "unique" number is unique when the
   registry proves it, not when the specification says it.
2. **Never derive a linking key from personal attributes** — name, date of birth, place —
   as the primary key. Offer it only as a matching aid with a human review step, and say
   so.
3. **Coverage is a fact from A0, not an assumption.** If A0 gives no coverage figure for
   the group the exchange serves, write ⚠ *coverage for this group not established*.
4. **A pairwise pseudonymous identifier is the production answer.** The GovStack Identity
   BB's `sub` is pairwise so that one identifier cannot be aggregated across services. A
   demonstration may route the raw national number; a production design should not.
   Say which the map assumes.
5. **The de-duplication key of the silver stage (4.6) is this identifier.** If the
   source dataset does not carry it, the silver stage must say how records are matched,
   how a match is scored, and who reviews the uncertain ones. A pipeline that
   de-duplicates on a non-unique key merges records for different people silently.

## The failure modes to name in every map

- two people, one identifier (a re-issued number; a family number used for each child)
- one person, two identifiers (issued twice; a district number and a national number)
- no identifier (the share of adults A0 §1 records as uncovered; every child under the
  issuing age)
- a format that changed (a number lengthened in a re-issue; leading zeros lost in a
  spreadsheet)
