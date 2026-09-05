# GovStack Building Blocks — Reference Catalogue & Cost Benchmarks

Source: GovStack Specifications (specs.govstack.global), GovStack Initiative publications, ITU/DIAL/GIZ research

---

## The Three Core Building Blocks for Cost Comparison

The GovStack cost-comparison skill focuses on these three BBs because they are the most universally duplicated across government programmes:

### 1. Identity Building Block

**What it does:**  
Provides foundational identity verification, authentication, and credential management for all digital government services. Uses OpenID Connect flows. Enables relying parties (programmes) to verify citizen identity and retrieve foundational attributes without each programme maintaining its own identity database.

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

**Why programmes duplicate it without shared infra:**  
Health programmes build patient ID, social protection builds beneficiary ID, tax builds taxpayer ID — all solving the same problem of "who is this person?" with separate databases and no interoperability.

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

**What it does:**  
Provides government payment infrastructure for G2P (government-to-person), G2B (government-to-business), P2G (person-to-government) and B2G flows. Handles bulk payment processing, bank/wallet mapping, reconciliation, and multicurrency support (v3.0, Dec 2025).

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

**Why programmes duplicate it:**  
Social protection, health insurance, agricultural subsidies, emergency cash transfers — each programme builds its own payment pipeline, its own FSP (financial service provider) integrations, its own reconciliation logic.

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

**What it does:**  
Provides secure, auditable, consent-aware data exchange between government systems. Based on X-Road-style architecture (Estonia's model, widely adopted). Acts as the data highway of the GovStack — without it, identity and payment BBs cannot share data across programmes.

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

**Why programmes duplicate it:**  
Without shared mediation, each programme builds point-to-point integrations. N programmes = N×(N-1)/2 integration pairs. With a shared Information Mediator: N integrations (each programme connects once to the hub).

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

## Other GovStack Building Blocks (for context, not primary cost comparison)

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

## Commodity vs. Differentiating Capabilities (Sourcing Guide)

A common costing error is applying one sourcing stance (e.g. "build everything bespoke" or "buy everything COTS") across the whole stack. Different capabilities warrant different sourcing — drive build/buy/configure decisions by strategic character:

| Capability Type | Sourcing Default | Rationale | Expected Bespoke Footprint |
|---|---|---|---|
| **Commodity / non-differentiating** (case management, generic workflow, document management, intake forms, dashboards, notifications) | Configure on COTS or low-code platform | These solve the same problems across organisations and sectors. Vendor maintains the platform; configuration is cheap to change. Bespoke build of these is waste | 5–15% |
| **Standard shared infrastructure** (identity, payments, data exchange, registries) | Configure on Digital Public Goods (MOSIP, X-Road, Mifos) or open-source platforms | Mature DPGs exist with active communities. Custom builds of these are now considered an anti-pattern in donor-funded contexts | 10–25% |
| **Domain logic with moderate uniqueness** (sector-specific business rules, eligibility calculations) | Configure rules engine / policy-as-code | Rules change frequently with policy; embedding in code creates maintenance drag | 15–30% |
| **Differentiating / competitive-asset capabilities** (capabilities where deep domain knowledge creates strategic value — e.g. tax risk-scoring models, fraud detection algorithms, sector-specific analytics) | Bespoke build justified | These are where organisational competence is expressed; outsourcing them removes the strategic edge | 60–90% |

**Costing implication**: For BBs in the "commodity" or "shared infrastructure" rows, apply the configuration dividend (~80% bespoke code reduction) when modelling Scenario B. For "differentiating" capabilities, model bespoke build cost honestly — the dividend doesn't apply, and that's correct.

---

## Country Tier Classification

Use GDP per capita (current USD) as proxy:
- **LIC**: <$1,135/year (World Bank threshold)
- **LMIC**: $1,136–$4,465/year
- **UMIC**: $4,466–$13,845/year
- **HIC**: >$13,845/year (usually have existing infrastructure; different model applies)

**Adjustment factors for specific contexts:**
- Conflict/fragile states: ×1.5–2.0 on all costs (security, logistics, turnover)
- Island nations / small population (<2M): ×0.6–0.8 on build, ×1.2 on ops (small market, imported expertise)
- Federated systems (states/provinces each need own instance): multiply by federation units
- Strong diaspora tech community: ×0.7–0.9 on labour costs

---

## Non-Financial Benefits Catalogue

Always include relevant items from this list in the output:

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
