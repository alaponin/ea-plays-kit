# Progressa — the demonstration country

Progressa is fictional. It is the one worked example in each Knowledge Product. A learner
who has no country to work on can run each play on Progressa, and can compare the result
against the published output.

This page is the **A0 country context pack for Progressa**. It has the seven sections that
Play 0 makes. Each fixture under `tests/plays/` names the sections that it uses.

Source: the GEATDM demonstration fixture (GEATDM-Sector-Education-v1.0 §7.1) and the
KP1 Module 4 script bundle, subtopic 4.1. Neither is in this repo; this page is the
copy the kit tests against, and the authority for every Progressa fact here.

> **Artefact** A0 — Country context pack · **Country** Progressa · **Sector** Education · **Built** 2026-09-05
> **Skill** — (fixture, not a skill run) · **Consumed** — · **Feeds** every play
> **Sources** 0 × Tier 1, 0 × Tier 2, 0 × Tier 3 · **Unverified lines** 0

*Progressa is fictional, so the fixture has no sources. A true run of Play 0 gives one
source for each claim. This fixture tests the shape of the output. It does not test the
sourcing.*

## §1 Digital-landscape brief — feeds 1.1, 1.2

Progressa is a lower-middle-income country. It has 16.8 million people, and the median age is 18.7 years. It joined GovStack in 2024, and it is a pilot country for the 50-in-5 DPI campaign. The cabinet has not yet approved the Digital Transformation Roadmap 2024–2030. The Progressa Digital Government Authority (PDGA) wrote the roadmap. PDGA is a unit under the Ministry of ICT, and its mandate coordinates but does not bind.

Identity: the Progressa National ID Authority (PNIA) has deployed the National ID since 2018, and it covers 78% of the adults. PNIA also operates an e-KYC platform since 2024. The Ministry of Education, Youth and Skills (MoEYS) keeps EMIS records at the district level, with its own numbers for the learners. The Social Protection Agency operates a separate register of beneficiaries. A vendor built that register in 2016, under a World Bank programme, and that vendor still holds the only maintenance contract. The patient index of the Ministry of Health uses a third identifier.

Data exchange: Linkup is a deployment of X-Road 7.x. It went live in 2025 as a pilot with four members: PNIA, the business register, the tax authority, and PDGA. A team built the link from the tax authority to the business register as a direct link between two databases, in 2022, before Linkup existed. Nobody has migrated it. MoEYS and the Ministry of Health exchange data in a spreadsheet, on request.

Payments: PayPro is the national system for fast payments. The central bank operates it, and the tax authority uses it. The scholarship programme still pays by cheque.

The strategies in force: the Digital Transformation Roadmap 2024–2030, which is a draft; the Education Sector Plan 2023–2028, which asks for a National Learner Registry that is not started; and the e-Government Interoperability Framework of 2021. The previous leadership of PDGA published that framework, and no current project cites it.

## §2 Programme list with budget envelopes and building-block needs — feeds 1.3, 1.5

1. National Learner Registry (MoEYS) — planned, USD 6.5m over 3 years (World Bank human-capital programme). Needs: learner identity (link to National ID), school facility data, data exchange with PNIA and examinations authority, parental consent.
2. Scholarship Management Platform (MoEYS with Ministry of Finance) — planned, USD 2.1m. Needs: applicant identity, eligibility data from the social register, payments to students/families (currently cheques), workflow.
3. Social Register modernisation (Social Protection Agency) — procurement stage, USD 4.8m. Needs: beneficiary identity, household data exchange with civil registration, payment disbursement.
4. Digital Health Records pilot (Ministry of Health, 3 provinces) — running, USD 3.2m (Global Fund). Needs: patient identity, facility registry, consent, data exchange with civil registration.
5. Farmer Registry and Input Subsidy (Ministry of Agriculture) — planned, USD 2.9m (AfDB). Needs: farmer identity, land parcel link, subsidy payments, data exchange with the cooperative bank.

## §3 Ministry operating context and constraints — feeds 1.4

The question: must MoEYS move the learner data to a once-only model? In that model, a parent who enrols a child in a school never gives information again that civil registration, PNIA or an earlier school already holds.

The context: today a parent enrols a child on paper at the school. The head teacher then types the record into the district EMIS. The same child can be in three places: a district file, a provincial file for secondary school, and the candidate list of the examination authority. The three can spell the name differently. The Education Sector Plan asks for a National Learner Registry (NLR). Linkup exists, and MoEYS is not a member. The Data Protection Act 2023 needs a legal basis to share the data of a minor. It also needs the consent of a parent for a use that is not statutory. PNIA covers 78% of the adults, and it issues an ID to a child only at 16 years. Birth registration is at 71%. The head teachers have a union, and they opposed the last change to the EMIS. The Minister wants to announce 'one learner, one record' inside 12 months.

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

## §5 Country characteristics one-liner — feeds 5.1

The population is 16.8 million. The income group is lower-middle. It is a unitary state with 10 provinces, and their administration is delegated, not devolved. The region is East and Southern Africa. It is a member of GovStack and a pilot country for 50-in-5. The National ID covers 78% of the adults. The layer for exchange uses X-Road and is in pilot. The digital agency, PDGA, coordinates and has no authority that binds. The budget cycle is one year, and there is no ICT envelope for several years. Three donors fund separate systems for separate sectors: the World Bank, the AfDB and the Global Fund. There is no EA function and no governance board.

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

Not found where a person expects it: there is no function for data standards in the education sector. The Ministry of Agriculture has no CIO for the sector, and the Planning unit does that work.

## §7 Legal and policy list — feeds 2.3, 1.7

| Instrument | Year | Status | Owning body | The one constraint it places on an EA design |
| --- | --- | --- | --- | --- |
| Data Protection Act | 2023 | enacted | Data Protection Commission (6 staff, no enforcement action yet) | A legal basis is required for sharing minors' data; parental consent for non-statutory uses |
| Public Procurement Act | (in force) | enacted | Progressa Public Procurement Authority | No framework for multi-year ICT procurement; annual award cycle |
| e-Government Interoperability Framework | 2021 | published, not applied | PDGA (previous leadership) | Names message formats and an approved-standards list; its governance committee no longer meets |
| Digital Transformation Roadmap 2024–2030 | 2024 | draft, awaiting cabinet | PDGA | Not yet binding; PDGA's mandate is coordinating, not binding |
| Education Sector Plan 2023–2028 | 2023 | in force | MoEYS | Calls for a National Learner Registry; contains no architecture content |
| Civil Registration Act | (in force) | enacted | Civil Registration Department | Birth registration is the legal identity anchor for a child; PNIA issues IDs only at 16 |

The fixture has no e-transactions act and no access-to-information act.

## The sector problem, in one paragraph — feeds 4.1

Three bodies register a learner: the school census, the Examination Authority for the
examinations, and a programme for social grants. The three lists do not agree. A parent
proves the identity of the child on paper at each counter, because no system trusts the
record of another system. The minister promised one record for each learner, that follows
the child from primary school to university. Nobody can deliver that record, because the
systems do not fit together.

## The initiatives to assess — feeds 1.5, 2.2

1. The Digital Transformation Roadmap 2024–2030. It is a draft by PDGA. It is a strategy with 5 pillars: connectivity, DPI, services, skills and governance. It lists the priority projects. It has a short section of guiding principles, with 8 principles. They include user-centricity, once-only and open standards.
2. The e-Government Interoperability Framework 2021, by the previous leadership of PDGA. It defines the message formats and a list of approved standards. It also creates a governance committee that does not meet. No current project uses it.
3. Linkup, on X-Road 7.x, a pilot from 2025. It is the technical layer for data exchange, and it has 4 members. Its onboarding procedure for a member is documented. It has no catalogue of the data.
4. The National ID and the e-KYC platform of PNIA, from 2018 and 2024. This is the foundation for identity, and it operates. It covers 78% of the adults. Its API is documented. There is no framework for a sector to adopt it.
5. The Education Sector Plan 2023–2028, by MoEYS. It is the strategy of the sector, and it names a National Learner Registry and the modernisation of the EMIS. It has no content about the architecture.
6. GovStack membership (2024) and 50-in-5 pilot — access to GovStack BB specifications and the sandbox; no local adaptation yet.
