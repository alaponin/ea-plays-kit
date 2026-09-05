<!-- fixture: Progressa (fictional) · canonical: tests/progressa.md · keep consistent with it -->
# Worked Example: Progressa Education Sector

All facts from `tests/progressa.md` §1, §6, §7 and the sector-problem paragraph. Progressa
is fictional; the example carries no sources.

Use it as a concrete model to follow or compare against when assessing a real sector.

---

## Bodies in Scope

| Body | Classification | Expected Profile |
|------|---------------|-----------------|
| Ministry of Education, Youth and Skills (MoEYS) | Policy Unit | Sets education policy, funds schools; runs district EMIS with its own learner numbering |
| Progressa National Examination Authority (PNEA) | Service-Delivery Authority with regulatory edge | Runs examinations, certifies results; holds a candidate list on its own numbering |
| Progressa Learner Registry (PLR) | State Registry | Intended single list of learners. Status: **planned** — called for in the Education Sector Plan 2023–2028, not started. Runs nothing and holds nothing yet |
| Progressa National ID Authority (PNIA) | State Registry + Shared Platform | Owns person identity; National ID since 2018 at 78% adult coverage, e-KYC since 2024. Issues IDs only at 16 |
| Progressa Digital Government Authority (PDGA) | Shared Platform Provider | Coordinates digital government and runs the shared data exchange, Linkup. Coordinating mandate, not binding; a unit under the Ministry of ICT |
| Social Protection Agency | Service-Delivery Authority | Social grants; beneficiary register built 2016 by a vendor under a World Bank programme |
| Civil Registration Department (Ministry of Interior) | State Registry | Birth and death registration, paper-first, 71% birth registration |
| Central Bank of Progressa | Shared Platform Provider | Operates PayPro, the national fast-payment system |

Classification takes one minute. It tells you what to expect before the first interview.

**Read the PLR row twice.** The registry that would resolve the sector's problem does not
exist. Every finding below follows from its absence, not from its design.

**Read the Civil Registration row too.** It is the legal identity anchor for a child under
the Civil Registration Act, and because PNIA issues no ID before 16, the National ID cannot
be the learner key for a primary-school child.

---

## Business Layer

**Capabilities** (what each body can do):

| Capability | Owner |
|-----------|-------|
| Set education policy and fund schools | MoEYS |
| Run an examination | PNEA |
| Certify an examination result | PNEA |
| Prove the identity of a person aged 16 or over | PNIA |
| Establish the legal identity of a child | Civil Registration Department |
| Determine social-grant eligibility | Social Protection Agency |
| Exchange data between bodies | PDGA |
| Settle a payment between accounts | Central Bank of Progressa |
| Register a learner | **unowned** — the PLR that would own it is not started |

**Services** (how capabilities reach citizens or other bodies):

| Service | Capability served | Delivered by |
|---------|------------------|-------------|
| Enrol a child in school | Register a learner | the school, on paper; the head teacher keys it into district EMIS |
| Sit a national examination | Run an examination | PNEA, from its own candidate list |
| Receive an examination certificate | Certify a result | PNEA |
| Receive a scholarship | Determine eligibility; settle a payment | MoEYS, by cheque |

**Quality test result**: ⚠️ Capabilities describe what each body does — but one capability
has no owner, which is the finding, not a formatting fault.

**Gap confirmed**: MoEYS and PNEA both maintain learner data as a side-effect of their own
capabilities, and the Social Protection Agency holds a third list. No body claims "register
a learner" as its capability. A capability nobody owns is held three times by nobody's
design.

---

## Data Layer

| Domain | Owner | Authoritative Copy Location | Consuming Bodies |
|--------|-------|----------------------------|-----------------|
| Person (16+) | PNIA | National ID register | tax authority, business register, PDGA members |
| Legal identity of a child | Civil Registration Department | Civil register, paper-first | none electronically |
| Learner | **none** | three partial copies, none authoritative | — |
| Examination result | PNEA | Examination Authority | MoEYS |
| School | MoEYS | School census | — |
| Grant beneficiary | Social Protection Agency | Beneficiary register (2016) | — |

**Once-only rule applied**: it is not. A parent proves the child's identity on paper at
every counter, because no system trusts another's.

**Quality test result**: ❌ One domain — Learner — has no owner and no authoritative copy.

**Gap confirmed, not suspected**: learner data is held three times, in the district EMIS,
in the PNEA candidate list and in the Social Protection beneficiary register, each on its
own numbering. None of the three lists agree.

---

## Application Layer

| Application | Capability served | Data domains used | Owner |
|------------|------------------|------------------|-------|
| District EMIS | Fund schools; school census | Learner (partial), School | MoEYS |
| Candidate management system | Run an examination; certify a result | Learner (partial), Examination result | PNEA |
| National ID and e-KYC platform | Prove identity (16+) | Person | PNIA |
| Linkup (X-Road 7.x) | Exchange data | all, for its four members | PDGA |
| Beneficiary register | Determine eligibility | Learner (partial), Grant beneficiary | Social Protection Agency |
| PayPro | Settle a payment | — | Central Bank of Progressa |
| — | Register a learner | Learner | no application exists |

**Quality test result**: ⚠️ Every application points to a capability, and the three that
hold the Learner domain each hold a different partial copy.

**Cross-layer check**: three applications carry learner data and none of them consumes
another. There is no application to consume: the PLR is not started.

**Gap confirmed**: this is both a duplicate registry (Data layer) and, because the copies
are reconciled by hand or by spreadsheet, a point-to-point problem at the Technology layer.

---

## Technology Layer

| Component | Role | Standard |
|-----------|------|----------|
| National ID and e-KYC (PNIA) | Issues and verifies identity, 16+ | documented API; no sector adoption framework |
| Linkup (PDGA) | Routes data between members with an audit trail | X-Road 7.x — live pilot, four members: PNIA, the business register, the tax authority, PDGA |
| PayPro (Central Bank of Progressa) | Settles a payment between accounts | used by the tax authority; the scholarship programme still pays by cheque |
| e-Government Interoperability Framework 2021 | Names message formats and an approved-standards list | published, not applied; its governance committee no longer meets |
| Government hosting | Hosts the sector's systems | not standardised |

**Quality test result**: ❌ A standards instrument exists and is not applied; the exchange
layer exists and the education sector is not on it. **MoEYS is not a Linkup member.**

**Point-to-point finding — Confirmed, not a risk.** The tax-to-business-register link was
built as a direct database link in 2022, before Linkup existed, and has not been migrated.
MoEYS and the Ministry of Health exchange data by spreadsheet on request. Both are
point-to-point integrations running alongside an exchange layer that could carry them.

**Single points of failure**: Linkup and the National ID platform. Neither yet carries an
education-sector flow, so the sector's exposure is not to their downtime but to its own
absence from them.

---

## Full Traceability Trace

Service: **Sit an examination and receive a certificate**

```
Service: Sit an examination; receive a certificate
  ↓ delivered by
Capability: Run-an-examination + Certify-a-result (owner: PNEA)
  ↓ supported by
Application: Candidate management system (owner: PNEA)
  ↓ uses
Data Domains: Examination result (owner: PNEA)
            + Learner — no owner; PNEA keeps its own candidate numbering
            + legal identity of the child (owner: Civil Registration Department, on paper)
  ↓ reached via
Technology: none — MoEYS is not a Linkup member; the school file reaches PNEA on paper
  ↓ running on
Technology: government hosting, not standardised
```

The trace is a complete architectural reading precisely because it breaks. Two links —
the Learner owner and the exchange route — are empty, and every symptom the minister
describes hangs off those two gaps.

---

## Universal Gap Findings for Progressa

| Gap | Status | Evidence |
|-----|--------|---------|
| Duplicate registries | **Confirmed** | A learner is held three times: district EMIS, PNEA candidate list, Social Protection beneficiary register — each on its own numbering, and the lists do not agree |
| Orphan systems | **Risk** | Provincial secondary files and school-level records are named in §3 but not inventoried |
| Point-to-point spaghetti | **Confirmed** | Tax ↔ business register by direct database link since 2022, unmigrated; MoEYS ↔ Health by spreadsheet; Linkup has four members and MoEYS is not one |
| No clear owner | **Confirmed** | The Learner domain has no owner. The PLR that would own it is not started |
| No standards function | **Confirmed** | §6 records no education-sector data-standards function; the 2021 Interoperability Framework is published, not applied |

---

## Architecture Traps in Progressa

**Bespoke trap — present.** The Social Protection Agency's beneficiary register was built in
2016 by a vendor under a World Bank programme rather than assembled from shared registries,
and it is now the third place a learner appears. Four more donor-funded systems are in the
same shape: five programmes across five ministries, each with its own identity and exchange
needs, funded by three donors on separate timetables. The National Learner Registry at
USD 6.5m is the next one to be procured, and nothing yet requires it to consume PNIA and
the civil register rather than build a sixth list.

**Vendor-driven trap — present.** The same 2016 register is under single-vendor maintenance:
the vendor that built it still holds the only maintenance contract. That is the fixture's
vendor-lock-in case, already realised, not a procurement risk to guard against later.
Require an open export format and a maintenance market before the PLR contract is signed,
because the counter-example is already running in the same sector.
