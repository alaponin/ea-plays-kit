# Progressa — the KP2 supplement to the A0 pack

This page adds the three sections that the KP2 Play 0 supplement makes, **§8 to §10**, to
the A0 country context pack for Progressa in `tests/progressa.md`. It also gives the
once-only scenario and the federation identifiers that the Module 4 and 5 fixtures use.
Each fact here agrees with `tests/progressa.md`, which stays the authority for every
Progressa fact. Where the two say the same thing, `tests/progressa.md` wins.

Progressa is fictional, so this supplement has no sources. A true run of the supplement
gives one source for each claim. The fixture tests the shape of the output, not the sourcing.

> **Artefact** A0 §8–§10 — KP2 supplement · **Country** Progressa · **Sector** Education · **Built** 2026-09-12
> **Skill** — (fixture, not a skill run) · **Consumed** A0 §1, A0 §6, A0 §7 · **Feeds** 1.1, 1.2, 1.3, 1.5, 2.1, 4.8
> **Sources** 0 × Tier 1, 0 × Tier 2, 0 × Tier 3 · **Unverified lines** 0

## §8 Current exchange approach — feeds 1.1

An interoperability platform exists in pilot. Linkup is a deployment of X-Road 7.x, operated by the Progressa Digital Government Authority (PDGA), live since 2025 with four members: PNIA, the business register, the tax authority and PDGA itself. It has a documented onboarding procedure for a member and no published catalogue of members or services. MoEYS is not a member.

Interoperability is not required by any instrument that binds. The e-Government Interoperability Framework of 2021, published by the previous leadership of PDGA, names message formats and an approved-standards list, but no current project cites it and its governance committee no longer meets. The Public Procurement Act has no interoperability clause and no framework for multi-year ICT procurement; each ministry tenders on an annual cycle and writes its own integration requirements, or none. The Digital Transformation Roadmap 2024–2030 is a draft awaiting cabinet, and PDGA's mandate coordinates but does not bind.

The best-known point-to-point integrations are three. The tax authority reads the business register over a direct database link built in 2022, before Linkup existed; the tax authority's IT unit maintains it and nobody has migrated it to the bus. MoEYS and the Ministry of Health exchange data in a spreadsheet, on request, with no owner on either side. The Social Protection Agency's beneficiary register, built in 2016 under a World Bank programme, exchanges nothing; its single vendor holds the only maintenance contract.

No published assessment of duplication exists. The Education Sector Plan 2023–2028 says that a learner is registered three times — in the school census, by the Examination Authority and by a social grant programme — and that the lists do not agree; it gives no count of re-submitted documents.

## §9 Integration map — feeds 1.2, 1.3, 1.5

| # | Providing body · registry | Consuming body · service | Entity exchanged | How it happens today | Citizen re-supplies? | Documented / inferred |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | PNIA · National ID register | PNEA · examination candidate registration | person identity | not at all — the candidate list uses its own numbering | yes, on paper at registration | documented (Education Sector Plan) |
| 2 | PLR · single learner list (planned, not started) | PNEA · certificate application | enrolment (school, level, year, status) | not at all — the PLR does not exist; the school sends a paper list | yes | inferred from the services involved |
| 3 | Civil Registration Department · civil register | MoEYS · school enrolment (district EMIS) | birth record of a child | citizen carries a certificate; 71% of births are registered | yes | documented (Civil Registration Act; EMIS census) |
| 4 | PNIA · National ID register | MoEYS · district EMIS | parent identity | not at all — the head teacher types the record from paper | yes | inferred |
| 5 | Social Protection Agency · beneficiary register | MoEYS with Ministry of Finance · Scholarship Management Platform (planned) | household eligibility | not at all — the platform is planned; today a paper attestation | yes | documented (programme list) |
| 6 | Central Bank of Progressa · PayPro | MoEYS · scholarship payment | payment instruction | not at all — the scholarship programme pays by cheque | not applicable | documented |
| 7 | MoEYS · school census | Ministry of Health · school health programme | school facility list | file transfer — a spreadsheet on request | no | documented (§1) |
| 8 | PNIA · e-KYC platform | any sector service | identity verification | live integration exists for the four Linkup members; no education body uses it | — | documented |

Observations. A parent proves the identity of a child on paper at three counters — the school, the Examination Authority and the grant programme — because no education system reads the National ID register. The enrolment record is asked for again at every level change, because the PLR that would hold it is planned and not started. The birth certificate is the one document every counter asks for, and 29% of children do not have one.

## §10 Data-protection law and DPA — feeds 2.1, 4.8

The Data Protection Act 2023 is in force. Its section on processing by public bodies requires a legal basis for the sharing of personal data between bodies, and it requires a legal basis — not consent alone — for the data of a minor when the use is statutory; parental consent is required for a use that is not statutory. The Act has no provision that names once-only sharing, and no provision that makes a register of one body an authoritative source for another.

The Data Protection Commission was established in 2023 under the Act. It has six staff and has taken no enforcement action. It has published no guidance on public-sector data sharing.

Instruments that already mandate or restrict exchange between named bodies: the Civil Registration Act makes birth registration the legal identity anchor for a child and does not provide for electronic access by other bodies; PNIA issues a National ID only at 16 years, so no identity instrument covers a learner below that age; the Education Sector Plan 2023–2028 calls for a National Learner Registry and gives it no legal basis; the e-Government Interoperability Framework of 2021 is a policy document with no legal force. Progressa has no e-transactions act and no access-to-information act.

The gaps a lawyer would name before an interoperability decree could be enacted: no lawful basis for a body to fetch what another body holds; no instrument that designates an authoritative source; no provision for the identity of a child below 16 in a cross-body exchange; no mandate for PDGA that binds a ministry to connect; and no statutory footing for the Data Protection Commission's role in a cross-body exchange.

## The once-only scenario and the federation — feeds 4.4 to 4.7, 5.4 to 5.8

This is the target-state slice that the National Learner Registry programme delivers. In the
Progressa baseline the PLR is planned, not started; the scenario builds the exchange the
country is working towards, not one it has.

**The scenario.** A learner applies for a senior-secondary certificate at PNEA. PNEA pre-fills
identity from PNIA and enrolment from PLR over Linkup. The learner provides one field, the
NIN. Nothing else is asked. A member that holds no grant on PNIA's identity service — PLR's
own subsystem in the negative check — is denied by the provider-side access-control list.

**The federation.** One Central Server, owned by PDGA; a Test CA as the trust anchor; four
Security Servers — `ss-pdga` (the management server), `ss-pnea`, `ss-plr`, `ss-pnia`.

| Item | Progressa value |
| --- | --- |
| X-Road instance | `PROGRESSA` |
| Member class | `GOV` |
| Owner | `PROGRESSA/GOV/PDGA`, management subsystem `MANAGEMENT` |
| Members | `PROGRESSA/GOV/PNEA:EXAMS` (consumer) · `PROGRESSA/GOV/PLR:ENROLMENT` (provider) · `PROGRESSA/GOV/PNIA:IDENTITY` (provider) |
| Services | `PROGRESSA/GOV/PNIA/IDENTITY/identity-api` — `GET /persons/{nin}` · `PROGRESSA/GOV/PLR/ENROLMENT/enrolment-api` — `GET /enrolments/{nin}` |
| Access | `identity-api` and `enrolment-api` grant `PNEA:EXAMS` only |
| Semantic entities | `person` (anchor CEDS): nin, given_name, family_name, date_of_birth, sex, region · `enrolment` (anchor OneRoster): nin, school, level, enrolment_year, status |
| Asked once | the citizen provides `nin`; the bus pre-fills the nine other fields |

These identifiers are frozen: KP3 and KP4 build against them. A fixture run uses them and no
others.
