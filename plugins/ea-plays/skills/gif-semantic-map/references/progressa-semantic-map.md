<!-- fixture: Progressa (fictional) · canonical: tests/progressa.md · keep consistent with it -->
# The Progressa semantic map — the once-only exchange

This is the semantic map of the KP2 build pack, the worked example of play 4.4 on
Progressa. The facts come from `tests/progressa.md` §1 and §6 and from
`tests/kp2/progressa-supplement.md`. Progressa is fictional, so the map carries no sources
for the country; the vocabulary anchors are real.

**The target-state note.** In the Progressa baseline the Progressa Learner Registry (PLR)
is planned and not started. The map below is the target state that the National Learner
Registry programme delivers — the exchange the country is working towards. The exchange:
a learner applies for a senior-secondary certificate at the Progressa National
Examination Authority (PNEA); PNEA pre-fills identity from the Progressa National ID
Authority (PNIA) and enrolment from the PLR over Linkup; the learner provides the NIN and
nothing else.

## The entities

| Entity | Anchor | Fields | Linking key |
| --- | --- | --- | --- |
| person | CEDS (a second anchor: the GovStack Identity BB OIDC claims — date_of_birth → birthdate, sex → gender, region → address.region) | nin, given_name, family_name, date_of_birth, sex, region | nin |
| enrolment | OneRoster | nin, school, level, enrolment_year, status | nin |
| award | CEDS | nin, award_id, program, year | nin |

The map lists the fields an entity *has*. Each service releases only the fields its purpose
needs — PNIA's identity service returns the six person fields and no more, because the
decree's purpose limitation says so.

## The term-to-term map, person

| Shared field | Vocabulary element | PNIA term (National ID register) | PNEA term (candidate list) | Type | Transformation |
| --- | --- | --- | --- | --- | --- |
| nin | — (national identifier, local) | NIN | candidate_id ≠ NIN — the candidate list uses its own numbering | string, 11 digits `[confirm]` | none; the candidate list gains a NIN column |
| given_name | CEDS First Name | first_name | forenames | string | none |
| family_name | CEDS Last or Surname | surname | surname | string | none |
| date_of_birth | CEDS Birthdate (OIDC birthdate) | dob | date_of_birth | date (ISO 8601) | format from DD/MM/YYYY `[confirm]` |
| sex | CEDS Sex (OIDC gender) | sex {F, M} | gender {Female, Male} | enum | code list: Female → F, Male → M `[confirm]` |
| region | CEDS address region (OIDC address.region) | region (10 provinces) | exam_centre_region | string | `[confirm: the two region lists agree]` |

## The identifier

The linking key is the NIN of the National ID, issued by PNIA. Coverage: 78% of adults;
PNIA issues an ID to a child only at 16. **This is the map's known weakness**: a learner
below 16 has no NIN, so the target-state exchange serves the senior-secondary certificate
first, where candidates are at or past the issuing age. For younger learners the PLR must
carry its own learner number, linked to a birth registration (71% of births are
registered) — a `[confirm]` for the National Learner Registry programme, not something the
map resolves. The demonstration routes the raw NIN over the bus; a production design uses
a pairwise pseudonymous identifier.

## The code lists

| Field | PNIA values | PNEA values | Shared |
| --- | --- | --- | --- |
| sex | F, M | Female, Male | F, M `[confirm]` |
| status (enrolment) | — | enrolled, withdrawn, completed | OneRoster enrollment status, mapped `[confirm]` |
| level | — | JS1–SS3 | local — no OneRoster element; registered as a local code list for the Semantics Working Group |

## What a real country's run adds that this fixture cannot

Sources. A real run cites the vocabulary version it read, the registry's published data
dictionary for each agency term, and the coverage figure with its year. Every `[confirm]`
above stays a `[confirm]` until the data owners confirm it against the live registry.
