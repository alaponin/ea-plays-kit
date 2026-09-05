# Progressa — the demonstration country

Progressa is fictional. It is the single worked example used across every Knowledge
Product, so a learner with no country to hand can still run every play and compare
against the published worked output.

This page is the **A0 country context pack for Progressa**, in the seven sections
Play 0 produces. Every fixture under `tests/plays/` names the sections it consumes.

Source: `gitbook-demo/fixture.py` (GEATDM-Sector-Education-v1.0 §7.1) and the KP1
Module 4 script bundle, subtopic 4.1.

> **Artefact** A0 — Country context pack · **Country** Progressa · **Sector** Education · **Built** 2026-09-05
> **Skill** — (fixture, not a skill run) · **Consumed** — · **Feeds** every play
> **Sources** 0 × Tier 1, 0 × Tier 2, 0 × Tier 3 · **Unverified lines** 0

*Progressa is fictional, so the fixture carries no sources. A real Play 0 run has a
source per claim; the fixture exercises the shape, not the sourcing.*

## §1 Digital-landscape brief — feeds 1.1, 1.2

Progressa is a lower-middle-income country of 16.8 million people (median age 18.7). It joined GovStack in 2024 and is a 50-in-5 DPI pilot country. The Digital Transformation Roadmap 2024–2030 is awaiting cabinet approval; it was drafted by the Progressa Digital Government Authority (PDGA), a unit under the Ministry of ICT with a coordinating but not binding mandate.

Identity: the Progressa National ID Authority (PNIA) has rolled out the National ID since 2018 (78% adult coverage) and runs an e-KYC platform since 2024. The Ministry of Education, Youth and Skills (MoEYS) keeps district-level EMIS records with its own learner numbering; the Social Protection Agency runs a separate beneficiary register built in 2016 by a vendor under a World Bank programme, with the vendor still holding the only maintenance contract; the Ministry of Health's patient index uses yet another identifier.

Data exchange: Linkup, an X-Road 7.x deployment, went live in 2025 in pilot with four members (PNIA, the business register, the tax authority, PDGA). The tax-to-business-register link was built as a direct database link in 2022 before Linkup existed and has not been migrated. MoEYS and Health exchange data by spreadsheet on request.

Payments: PayPro, the national fast-payment system, is operated by the central bank and is used by the tax authority; the scholarship programme still pays by cheque.

Strategies in force: the Digital Transformation Roadmap 2024–2030 (draft), the Education Sector Plan 2023–2028 (which calls for a National Learner Registry, not yet started), and a 2021 e-Government Interoperability Framework that was published by the previous PDGA leadership and is not referenced by current projects.

## §2 Programme list with budget envelopes and building-block needs — feeds 1.3, 1.5

1. National Learner Registry (MoEYS) — planned, USD 6.5m over 3 years (World Bank human-capital programme). Needs: learner identity (link to National ID), school facility data, data exchange with PNIA and examinations authority, parental consent.
2. Scholarship Management Platform (MoEYS with Ministry of Finance) — planned, USD 2.1m. Needs: applicant identity, eligibility data from the social register, payments to students/families (currently cheques), workflow.
3. Social Register modernisation (Social Protection Agency) — procurement stage, USD 4.8m. Needs: beneficiary identity, household data exchange with civil registration, payment disbursement.
4. Digital Health Records pilot (Ministry of Health, 3 provinces) — running, USD 3.2m (Global Fund). Needs: patient identity, facility registry, consent, data exchange with civil registration.
5. Farmer Registry and Input Subsidy (Ministry of Agriculture) — planned, USD 2.9m (AfDB). Needs: farmer identity, land parcel link, subsidy payments, data exchange with the cooperative bank.

## §3 Ministry operating context and constraints — feeds 1.4

Question: should MoEYS move to a Once-Only model for learner data, so that a parent enrolling a child in school never re-supplies information already held by civil registration, PNIA or a previous school?

Context: today enrolment is on paper at the school; the head teacher keys it into district EMIS; the same child may appear in a district file, a provincial secondary file and the examinations authority's candidate list with different spellings. The Education Sector Plan calls for a National Learner Registry (NLR). Linkup exists but MoEYS is not a member. The Data Protection Act 2023 requires a legal basis for sharing minors' data and parental consent for non-statutory uses. PNIA covers 78% of adults but issues child IDs only at 16; birth registration is at 71%. Head teachers are unionised and resisted the last EMIS change. The Minister wants a 'one learner, one record' announcement within 12 months.

## §4 Institutional roles register, by post — feeds 1.6, 1.7

- Minister of ICT (political sponsor of the Digital Transformation Roadmap)
- PDGA Director-General (coordinating mandate; reports to Minister of ICT)
- PDGA architecture unit: 1 senior architect (contract, donor-funded), 2 junior analysts
- Sector CIOs: MoEYS ICT Director; Ministry of Health ICT Director; Social Protection Agency IT manager; Ministry of Agriculture has no ICT director (handled by the Planning unit)
- PNIA Director (National ID; owner of the identity register)
- Civil Registration Department (under Ministry of Interior)
- Progressa Public Procurement Authority
- Data Protection Commission (established 2023, 6 staff, no enforcement action yet)
- Ministry of Finance budget department (annual budget cycle; no multi-year envelopes for ICT)
- No EA Governance Board exists; an ICT Steering Committee met twice in 2024 and not since

## §5 Country characteristics one-liner — feeds 1.8, 5.1

Population 16.8 million; lower-middle-income; unitary state with 10 provinces that have delegated (not devolved) administration; East/Southern Africa region; GovStack member and 50-in-5 pilot; National ID 78% adult coverage; X-Road-based exchange layer in pilot; a coordinating digital agency (PDGA) without binding authority; annual budget cycle with no multi-year ICT envelopes; three donors (World Bank, AfDB, Global Fund) funding separate sectoral systems; no EA function or governance board yet.

## §6 Public bodies, systems and registries — feeds 2.1, 2.4, 2.5, 4.1

| Body | Mandate | Systems it runs | Registries it holds | Confidence |
| --- | --- | --- | --- | --- |
| Ministry of Education, Youth and Skills (MoEYS) | Sets education policy, funds schools | District EMIS (own learner numbering) | School census; district learner files | confirmed |
| Progressa National Examination Authority (PNEA) | Runs examinations, certifies results | Candidate management system | Candidate list (own numbering) | confirmed |
| Progressa Learner Registry (PLR) | Intended single list of learners | none — called for in the Education Sector Plan 2023–2028, not started | none yet | planned |
| Progressa National ID Authority (PNIA) | Owns person identity; issues National ID | National ID (2018, 78% adult coverage); e-KYC platform (2024) | National ID register | confirmed |
| Progressa Digital Government Authority (PDGA) | Coordinates digital government; runs shared data exchange | Linkup (X-Road 7.x, 2025 pilot, 4 members) | member/service catalogue (none published) | confirmed |
| Social Protection Agency | Social grants | Beneficiary register (2016, single-vendor maintenance) | Beneficiary register | confirmed |
| Civil Registration Department (Ministry of Interior) | Birth and death registration | paper-first; 71% birth registration | Civil register | confirmed |
| Central Bank of Progressa | Operates the national fast-payment system | PayPro | — | confirmed |

Not found where one would be expected: no education-sector data-standards function; no sector CIO in the Ministry of Agriculture (handled by the Planning unit).

## §7 Legal and policy list — feeds 2.3, 1.7

| Instrument | Year | Status | Owning body | The one constraint it places on an EA design |
| --- | --- | --- | --- | --- |
| Data Protection Act | 2023 | enacted | Data Protection Commission (6 staff, no enforcement action yet) | A legal basis is required for sharing minors' data; parental consent for non-statutory uses |
| Public Procurement Act | (in force) | enacted | Progressa Public Procurement Authority | No framework for multi-year ICT procurement; annual award cycle |
| e-Government Interoperability Framework | 2021 | published, not applied | PDGA (previous leadership) | Names message formats and an approved-standards list; its governance committee no longer meets |
| Digital Transformation Roadmap 2024–2030 | 2024 | draft, awaiting cabinet | PDGA | Not yet binding; PDGA's mandate is coordinating, not binding |
| Education Sector Plan 2023–2028 | 2023 | in force | MoEYS | Calls for a National Learner Registry; contains no architecture content |
| Civil Registration Act | (in force) | enacted | Civil Registration Department | Birth registration is the legal identity anchor for a child; PNIA issues IDs only at 16 |

No e-transactions act and no access-to-information act found in the fixture.

## The sector problem, in one paragraph — feeds 4.1

A learner is registered three times — once in the school census, once by the
Examination Authority for exams, once by a social grant programme. None of the three
lists agree. A parent proves the child's identity on paper at every counter, because
no system trusts another's. The minister has promised a single learner record that
follows the child from primary school to university, and it cannot be delivered
because the systems do not fit together.

## The initiatives to assess — feeds 1.5, 2.2

1. Digital Transformation Roadmap 2024–2030 (draft, PDGA) — a strategy with 5 pillars (connectivity, DPI, services, skills, governance); lists priority projects; contains a short 'guiding principles' section (8 principles including user-centricity, once-only, open standards).
2. e-Government Interoperability Framework 2021 (PDGA, previous leadership) — defines message formats, an approved-standards list and a governance committee that no longer meets; not used by current projects.
3. Linkup (X-Road 7.x, 2025 pilot) — technical data-exchange layer with 4 members; member onboarding procedure documented; no data-catalogue.
4. PNIA National ID and e-KYC (2018/2024) — operational identity foundation, 78% adult coverage; API documented; no sector adoption framework.
5. Education Sector Plan 2023–2028 (MoEYS) — sector strategy naming a National Learner Registry and EMIS modernisation; no architecture content.
6. GovStack membership (2024) and 50-in-5 pilot — access to GovStack BB specifications and the sandbox; no local adaptation yet.
