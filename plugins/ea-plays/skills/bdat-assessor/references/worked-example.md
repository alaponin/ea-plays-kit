# Worked Example: Progressa Education Sector

Progressa is a demonstration country. All institutions are fictional.
Use this as a concrete model to follow or compare against when assessing a real sector.

---

## Bodies in Scope

| Body | Classification | Expected Profile |
|------|---------------|-----------------|
| Ministry of Education, Youth and Sport (MoEYS) | Policy Unit | Sets education policy and owns rules; funds schools; does not run services at scale |
| National Examination Authority (PNEA) | Service-Delivery Authority with regulatory edge | Runs examinations at scale; certifies results; holds authoritative record of results |
| Learner Registry (PLR) | State Registry | Authoritative single source for who is a learner; owned centrally, consumed by others |
| National Identity Authority (PNIA) | State Registry + Shared Platform | Owns the person identity every sector reuses; issues identity tokens |
| Digital Government Authority (PDGA) | Shared Platform Provider | Runs data-exchange backbone and payments infrastructure; no sector owns it |

Classification takes one minute. It tells you what to expect before the first interview.

---

## Business Layer

**Capabilities** (what each body can do):

| Capability | Owner |
|-----------|-------|
| Register a learner | PLR |
| Run an examination | PNEA |
| Certify an examination result | PNEA |
| Prove the identity of a person | PNIA |
| Set education policy and fund schools | MoEYS |
| Exchange data between bodies | PDGA |

**Services** (how capabilities reach citizens or other bodies):

| Service | Capability served | Delivered by |
|---------|------------------|-------------|
| Enrol a child in school | Register a learner | PLR via MoEYS schools |
| Sit a national examination | Run an examination | PNEA |
| Receive an examination certificate | Certify a result | PNEA |
| Transfer between schools | Register a learner | PLR |

**Quality test result**: ✅ Capabilities describe what each body does — not how it is organised internally.

**Gap to note**: If both MoEYS and PNEA each claim a "manage learner data" capability, that is a duplicate claim — the first gap, visible from the Business layer alone.

---

## Data Layer

| Domain | Owner | Authoritative Copy Location | Consuming Bodies |
|--------|-------|----------------------------|-----------------|
| Person | PNIA | National Identity Authority | All |
| Learner | PLR | Learner Registry | PNEA, MoEYS, schools |
| Examination result | PNEA | Examination Authority | MoEYS, PLR (reference) |
| School | MoEYS | Ministry | PLR, PNEA |

**Once-only rule applied**: When PNEA needs to know who a learner is, it consumes PLR and PNIA — it does not maintain its own private copy of the learner that drifts out of date.

**Quality test result**: ✅ One domain, one owner, one authoritative copy named for each.

**Gap to flag**: If the Examination Authority is found to maintain its own learner list, that is a duplicate registry. Write it down; it is not a detail.

---

## Application Layer

| Application | Capability served | Data domains used | Owner |
|------------|------------------|------------------|-------|
| Enrolment system | Register a learner | Learner, Person | PLR |
| Examination management system | Run an examination; Certify a result | Learner, Person, Examination result | PNEA |
| Identity verification service | Prove identity | Person | PNIA |
| School management system | Set policy; fund schools | School | MoEYS |
| Data exchange backbone | Exchange data | All (infrastructure) | PDGA |

**Quality test result**: ✅ Every application points to a capability and to the data domains it uses.

**Cross-layer check**: The examination management system uses Learner and Person domains owned by other bodies — those cross-body data flows must pass through the PDGA data-exchange backbone, not custom point-to-point connections.

**Gap to flag**: If the examination management system holds its own copy of the learner record rather than consuming PLR via the backbone, that is both a duplicate registry (Data layer) and a point-to-point integration risk (Technology layer).

---

## Technology Layer

| Component | Role | Standard |
|-----------|------|----------|
| Shared identity platform | Issues and verifies identity tokens | OpenID Connect |
| Data-exchange backbone | Routes data between bodies with audit trail | X-Road or equivalent |
| Government hosting | Hosts PLR, PNEA, MoEYS systems | To be standardised |

**Quality test result**: ⚠️ Standards named for identity and exchange; hosting standard not yet defined (a gap).

**Single points of failure**: The data-exchange backbone and the identity platform — if either is unavailable, cross-body services fail. Uptime and redundancy requirements must be specified.

---

## Full Traceability Trace

Service: **Sit an examination and receive a certificate**

```
Service: Sit an examination; receive a certificate
  ↓ delivered by
Capability: Run-an-examination + Certify-a-result (owner: PNEA)
  ↓ supported by
Application: Examination management system (owner: PNEA)
  ↓ uses
Data Domains: Learner (owner: PLR) + Person (owner: PNIA) + Examination result (owner: PNEA)
  ↓ reached via
Technology: Data-exchange backbone (PDGA) + Identity platform (PNIA)
  ↓ running on
Technology: Government hosting
```

This single thread — from citizen service to infrastructure — is a complete architectural reading. Every link is named, owned, and traceable. Any broken link in this chain is a gap.

---

## Universal Gap Findings for Progressa

| Gap | Status | Evidence |
|-----|--------|---------|
| Duplicate registries | **Risk** — PNEA may hold its own learner list | Check whether exam system queries PLR or maintains its own |
| Orphan systems | **Unknown** — school-level legacy systems not inventoried | MoEYS school management system scope unclear |
| Point-to-point spaghetti | **Risk** — no confirmation PDGA backbone is in use for all cross-body flows | Confirm all PNEA ↔ PLR ↔ PNIA connections route through PDGA |
| No clear owner | **Clear for named domains** — gaps possible for school-level sub-domains | District-level school data ownership not specified |

---

## Architecture Traps in Progressa

**Bespoke trap — present risk**: If a donor-funded education project decides to build its own learner registration rather than consume PLR, it adds a fifth version of the learner record. Flag at procurement stage; require project to demonstrate why PLR cannot be used.

**Vendor-driven trap — present risk**: If the examination management system is a proprietary product and examination result data is stored in a vendor-specific format, extracting results for a future system requires vendor cooperation. Require open data export format at procurement.
