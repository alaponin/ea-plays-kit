# The published vocabularies

Align to a vocabulary that a standards body publishes. Never define a shared element fresh
when a published one exists. Fetch the specification each time; quote the element's
definition; record the version. The organisations are named here; the exact URL of a
version moves, so find it from the body's own site and cite what you read.

## By entity

| Entity | Vocabulary (body) | What it defines | What it does not | Pin |
| --- | --- | --- | --- | --- |
| person (identity) | GovStack Identity Building Block, the OIDC standard claims chapter; OpenID Connect Core 1.0 §5.1 standard claims | given_name, family_name, birthdate, gender, address (with region), the pairwise `sub` | a national ID number — that is the country's own identifier | Identity BB 2.0; OIDC Core 1.0 |
| person (education view) | CEDS — Common Education Data Standards (US Department of Education) | person and demographic elements with definitions and option sets | non-US identifiers; sector-specific coverage outside education | the CEDS version on the day; cite the element URL |
| learner, enrolment, school, class | OneRoster (1EdTech) | user, org, enrollment, class, academicSession, with enumerations for role and status | grading of national examinations; a national learner number | OneRoster 1.2 |
| school (facility) | Giga open schema — school master data (school id, name, location as GeoJSON, connectivity fields); ISO 3166-1 alpha-3 for the country | the facility register's shape and the connectivity measures | learner-level data | the Giga schema version published on the day |
| award, credential | W3C Verifiable Credentials Data Model 2.0; the GovStack Wallet BB | credentialSubject, issuer, validity | the education-specific fields of a certificate — those are local | VC 2.0 |
| any element | ISO/IEC 11179 (metadata registries) — the data-element structure: name, definition, representation, permitted values | how to describe an element in the semantic registry | any element content | ISO/IEC 11179-3 |
| serialisation | JSON-LD 1.1 (W3C) | how a shared vocabulary is carried in JSON with `@context` | the vocabulary itself | JSON-LD 1.1 |

## The GovStack renames that carry across

The GovStack Identity BB's OIDC claims and a CEDS-anchored person entity name the same
things differently. When both appear in a portfolio, record the correspondence once in the
map, so that the two anchors do not read as two entities:

| Education anchor | Identity BB / OIDC claim |
| --- | --- |
| date_of_birth | birthdate |
| sex | gender |
| region | address.region |

## What a vocabulary cannot give you

- **The identifier.** A vocabulary defines *person*; it does not tell you which number the
  country uses to say *this* person. `identifier-rules.md`.
- **The code-list values in the live registry.** OneRoster's enrolment status enumeration
  is not the status list in the district EMIS. Map both; confirm the live one.
- **Purpose limitation.** Which fields an exchange may carry is the decree's and the
  data-protection envelope's (B27) — the map lists the fields the entity has; the
  service contract (B24) releases only the ones the purpose needs.

## Rejected as an anchor

A vendor's data model; an EMIS product's export schema; a donor project's template; a
draft-grade GovStack specification (a data chapter that is still a template placeholder).
Use them as a *source* of an agency's terms, never as the shared definition.
