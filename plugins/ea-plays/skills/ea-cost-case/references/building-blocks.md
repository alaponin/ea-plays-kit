# The GovStack building blocks — the catalogue and the cost benchmarks

Source: GovStack Specifications (specs.govstack.global), GovStack Initiative publications, ITU/DIAL/GIZ research

---

## The three core building blocks for a cost comparison

This skill compares the cost of these three building blocks. Government programmes duplicate
these three more than any others.

### 1. Identity Building Block

**What it does**

It gives foundational identity verification, authentication and credential management to each
digital government service. It uses OpenID Connect flows. A relying party, which is a
programme, can verify the identity of a citizen and read the foundational attributes. The
programme does not need its own database of identities.

**Key functions:**  
- Identity verification API (OpenID Connect)
- Foundational identity attribute retrieval
- Verifiable credential issuance (links to Wallet BB)
- Consent-aware data sharing
- Multi-factor authentication

**Real-world implementations (Digital Public Goods aligned with this BB):**  
- MOSIP (Modular Open Source Identity Platform) — Philippines PhilSys, Ethiopia, Morocco
- OpenCRVS (civil registration)
- National Digital ID systems in Togo, Sierra Leone, Uganda

**Why programmes duplicate it when there is no shared infrastructure**

A health programme builds a patient ID. A social protection programme builds a beneficiary
ID. A tax programme builds a taxpayer ID. Each one answers the same question, "who is this
person?", with its own database, and the databases are not interoperable.

**Cost Benchmarks (build cost, one-time, includes integration and customization):**

| Country Income Tier | Low-end | Mid | High-end | Notes |
|---|---|---|---|---|
| Low income (LIC) | $800K | $1.5M | $3M | Donor-funded, DPG software, local team |
| Lower-middle income (LMIC) | $1.5M | $3M | $6M | Mixed funding, partial COTS |
| Upper-middle income (UMIC) | $3M | $6M | $12M | More COTS, stronger SLA requirements |

**Annual Operations Cost (% of build, per year):**  
- LIC: 15–20% of build cost  
- LMIC: 18–22%  
- UMIC: 20–25%  

**Per-programme integration cost (consuming the shared Identity BB via API):**  
- LIC: $50K–$150K per programme  
- LMIC: $80K–$200K per programme  
- UMIC: $150K–$400K per programme  

**Shared-infrastructure premium (to make it enterprise-grade for multi-programme use):**  
1.3–1.5× build cost

---

### 2. Payments Building Block

**What it does**

It gives the payment infrastructure of the government for four flows: government to person
(G2P), government to business (G2B), person to government (P2G), and business to government
(B2G). It processes bulk payments, maps a beneficiary to a bank or a wallet, reconciles the
payments, and supports more than one currency (v3.0, Dec 2025).

**Key functions:**  
- Bulk disbursement processing (social transfers, salaries, subsidies)
- G2P Connect interoperability layer
- Payment gateway integration (mobile money, bank transfers)
- Reconciliation and audit trails
- Beneficiary bank/wallet mapping
- Multicurrency support

**Real-world implementations:**  
- Mifos X / Apache Fineract
- G2P Connect (open blueprint, World Bank)
- GSMA Mobile Money API-aligned systems
- MoMo-based G2P systems (West Africa)

**Why programmes duplicate it**

Social protection, health insurance, agricultural subsidies and emergency cash transfers each
build their own payment pipeline. Each one builds its own integrations to the financial
service providers, and its own logic to reconcile the payments.

**Cost Benchmarks:**

| Country Income Tier | Low-end | Mid | High-end | Notes |
|---|---|---|---|---|
| LIC | $600K | $1.2M | $2.5M | Often mobile money-centric, simpler stack |
| LMIC | $1.2M | $2.5M | $5M | Mixed bank + MoMo, regulatory compliance |
| UMIC | $2.5M | $5M | $10M | Full banking integration, compliance overhead |

**Annual Operations Cost:**  
- LIC: 12–18%  
- LMIC: 15–20%  
- UMIC: 18–25%  

**Per-programme integration cost:**  
- LIC: $40K–$120K  
- LMIC: $70K–$180K  
- UMIC: $120K–$350K  

**Shared-infrastructure premium:** 1.2–1.4×

---

### 3. Information Mediator (Data Exchange) Building Block

**What it does**

It exchanges data between the systems of a government. The exchange is secure, a person can
audit it, and it applies the consent of the citizen. Its architecture follows X-Road, which
is the model of Estonia that many countries adopted. It is the road for the data in GovStack.
Without it, the Identity block and the Payment block cannot share data between programmes.

**Key functions:**  
- Secure API gateway between government systems
- Data exchange logging and audit
- Consent management integration (links to Consent BB)
- Service directory (what data is available from whom)
- Access control and trust federation

**Real-world implementations:**  
- X-Road (Estonia, Finland, Iceland, and adopted by several LMIC)
- DIGIT (Egovernments Foundation, India)
- OpenHIE (health information exchange)

**Why programmes duplicate it**

Without a shared mediator, each programme builds point-to-point integrations. For N
programmes there are N×(N−1)/2 pairs to integrate. With a shared Information Mediator there
are N integrations, because each programme connects one time to the hub.

**Integration complexity multiplier (siloed):**  
- 3 programmes: 3 pairs → 3 bespoke integrations  
- 5 programmes: 10 pairs → 10 bespoke integrations  
- 10 programmes: 45 pairs → 45 bespoke integrations  
- Formula: N×(N-1)/2

**Cost Benchmarks:**

| Country Income Tier | Low-end | Mid | High-end | Notes |
|---|---|---|---|---|
| LIC | $400K | $900K | $2M | X-Road deployment + local config |
| LMIC | $800K | $1.8M | $4M | Enterprise config, legal framework needed |
| UMIC | $1.5M | $3.5M | $7M | Regulatory, data protection compliance |

**Annual Operations Cost:**  
- LIC: 10–15%  
- LMIC: 12–18%  
- UMIC: 15–22%  

**Per-programme integration cost (connecting to the shared mediator):**  
- LIC: $20K–$80K  
- LMIC: $40K–$120K  
- UMIC: $80K–$200K  

**Point-to-point integration cost (siloed, per pair):**  
- LIC: $30K–$100K per integration pair  
- LMIC: $60K–$150K per pair  
- UMIC: $100K–$300K per pair  

**Shared-infrastructure premium:** 1.2–1.35×

---

## The other GovStack building blocks. They give context. They are not in the main cost comparison

| Building Block | Function | When to include in cost model |
|---|---|---|
| **Consent** | Citizen consent management for data processing | When data protection law (GDPR-like) requires explicit consent per transaction |
| **Digital Registries** | Structured data stores (beneficiary lists, business registries) | When programmes each build their own registries |
| **Messaging** | SMS/email/push notifications to citizens | When each programme has its own comms stack |
| **Registration** | Citizen-facing service registration workflows | When programmes have separate intake forms |
| **Scheduler** | Appointment/task scheduling | Health, social services with appointments |
| **Workflow** | Process orchestration across BBs | Complex multi-step government services |
| **E-Signature** | Digital document signing | For legally binding digital transactions |
| **Wallet** | Verifiable credential wallet for citizens | For digital ID credential portability |

---

## Commodity capabilities and differentiating capabilities: a guide to sourcing

People make one common error when they cost a programme. They apply one sourcing stance to
the full stack, such as "build everything bespoke" or "buy everything as a commercial
product". A different capability needs a different sourcing decision. Decide to build, to buy
or to configure by the strategic character of the capability.

| Capability Type | Sourcing Default | Rationale | Expected Bespoke Footprint |
|---|---|---|---|
| **Commodity / non-differentiating** (case management, generic workflow, document management, intake forms, dashboards, notifications) | Configure on COTS or low-code platform | These solve the same problems across organisations and sectors. Vendor maintains the platform; configuration is cheap to change. Bespoke build of these is waste | 5–15% |
| **Standard shared infrastructure** (identity, payments, data exchange, registries) | Configure on Digital Public Goods (MOSIP, X-Road, Mifos) or open-source platforms | Mature DPGs exist with active communities. Custom builds of these are now considered an anti-pattern in donor-funded contexts | 10–25% |
| **Domain logic with moderate uniqueness** (sector-specific business rules, eligibility calculations) | Configure rules engine / policy-as-code | Rules change frequently with policy; embedding in code creates maintenance drag | 15–30% |
| **Differentiating / competitive-asset capabilities** (capabilities where deep domain knowledge creates strategic value — e.g. tax risk-scoring models, fraud detection algorithms, sector-specific analytics) | Bespoke build justified | These are where organisational competence is expressed; outsourcing them removes the strategic edge | 60–90% |

**What this means for the cost.** For a block in the "commodity" row or in the "shared
infrastructure" row, apply the configuration dividend when you model Scenario B. The dividend
removes about 80% of the bespoke code. For a "differentiating" capability, model the full
cost of a bespoke build. The dividend does not apply there, and that is correct.

---

## How to classify the tier of a country

Use the GDP for each person, in current USD:
- **LIC**: <$1,135/year (World Bank threshold)
- **LMIC**: $1,136–$4,465/year
- **UMIC**: $4,466–$13,845/year
- **HIC**: >$13,845/year (usually have existing infrastructure; different model applies)

**The adjustment factors for a specific context**

- A state in conflict, or a fragile state: multiply each cost by 1.5 to 2.0, for the
  security, the logistics and the turnover of staff.
- An island nation, or a population below 2 million: multiply the build by 0.6 to 0.8, and
  multiply the operations by 1.2. The market is small, and the country imports the expertise.
- A federated system, where each state or province needs its own instance: multiply by the
  number of units in the federation.
- A large technology community in the diaspora: multiply the labour costs by 0.7 to 0.9.

---

## The catalogue of benefits that are not financial

Put each item from this list that applies into the output.

**Efficiency gains:**
- Faster programme launch: consuming a shared BB is 6–18 months faster than building from scratch
- Reduced procurement overhead: one shared procurement vs. N separate ones
- Interoperability unlocked: programmes can share beneficiary data without custom integrations

**Governance and accountability:**
- Single audit trail across all programmes using shared BBs
- Reduced duplicate beneficiaries / ghost beneficiaries in payment programmes
- Centralized fraud detection across programmes

**Citizen experience:**
- One digital identity works across all services (no re-registration per programme)
- Consistent UX patterns across government services
- Faster service delivery (no manual ID re-verification)

**Sustainability:**
- Maintenance cost shared across programmes and donors
- Reduced vendor lock-in (open standards, shared negotiating power)
- Talent concentration: one team maintains shared BB vs. scattered expertise

**SDG alignment:**
- SDG 16.6: Effective, accountable institutions
- SDG 17.18: Data availability and quality for monitoring
- Direct alignment with SDG Digital Investment Framework (ITU/DIAL)
