# Domain Transfer Guide

Use this to move fast when the method is being run on a sector or country
for the first time in this engagement.

---

## Institution Classification Taxonomy

Every public body encountered in Discovery should be classified as one (or
occasionally two) of these five types. The classification isn't cosmetic —
it predicts what capabilities the body needs and what its role should be in
the target architecture.

| Type | Definition | Needs (per PAERA org typology) | Typical target-architecture role |
|---|---|---|---|
| **Policy unit** | Sets policy, funds delivery, does not run frontline services itself | Document/content management, analytics | Sets standards; consumes sector-wide reporting from the shared platforms |
| **Regulatory agency** | Licenses, certifies, or enforces standards within a domain | Policy-unit capabilities + a digital service-delivery platform (forms, licensing, payments) | Certifies against the authoritative registry rather than maintaining its own list |
| **Service-delivery authority** | Delivers a service at scale to citizens/businesses | Regulatory-agency capabilities + registration, compliance, customer management at industrial scale | Consumes identity + the core registry; owns only its own service-execution data |
| **State registry** | The legally designated owner of a "who/what is registered" list (identity, land, business, learner, patient) | Registration BB, strong data-quality and audit requirements | Becomes (or should become) the authoritative source other bodies read from |
| **Shared platform** | Provides infrastructure or a capability every sector reuses (identity, payments, data exchange, hosting) | Interoperability, uptime, governance of consuming bodies | The thing everything else in the target architecture consumes |

Some bodies span two types (e.g. an exam council can be both a
service-delivery authority and, informally, a shadow registry if it keeps
its own candidate list — that's usually itself one of the four common gaps).

---

## Cross-Sector Domain Analogy Table

The same fragmentation shapes — duplicate registries, paper re-entry,
point-to-point integration, no clear owner, a stalled flagship — recur
across sectors. Use this table to translate quickly.

| Sector | The duplicated "person/object" | Typical stalled flagship | Typical registries in tension | Typical shared platforms to check for reuse |
|---|---|---|---|---|
| **Education** | The learner | A single learner record from primary school to university | School census, exam-board candidate list, tertiary records | National identity authority, national data-exchange backbone, national payment switch |
| **Health** | The patient | A single patient record across primary care, hospitals, and insurance | Facility-level patient registers, insurance-scheme membership lists, disease-programme registers | National identity/civil registration, health information exchange, payment/claims switch |
| **Agriculture** | The farmer / the farm plot | A single farmer registry linking land, subsidy eligibility, and extension services | Land registry, subsidy/input-scheme beneficiary lists, cooperative membership records | National identity authority, land registry, payment switch, GIS/land-parcel platform |
| **Social protection** | The beneficiary / the household | A single social registry determining eligibility across programmes | Programme-specific beneficiary lists (cash transfer, school feeding, health insurance) | National identity authority, payment switch, data-exchange backbone |
| **Tax / revenue** | The taxpayer | A single taxpayer identifier across income, VAT, customs, and property | Tax-type-specific taxpayer databases, customs declarant lists, property registers | National identity authority, national payment switch, business registry |
| **Land** | The parcel / the rights-holder | A single land record resolving overlapping claims | Deeds registry, cadastral survey records, customary/traditional tenure records | National identity authority, GIS platform, data-exchange backbone |

When starting a new sector, name the row above (or draft an equivalent one
if the sector isn't listed) before Discovery begins — it gives the
engagement a fast, testable hypothesis for what Assess will likely confirm.

---

## Companion Skills by Phase

| Phase | Companion skill | What it adds |
|---|---|---|
| Discover | `country-context-data` | Public indicators, institutional structures, existing digital-ID/registry programmes for the country |
| Assess | `paera-assessor` | GovStack/PAERA-anchored maturity scoring and formal gap-to-building-block mapping |
| Assess / Adapt | `bdat-assessor` | Four-layer (Business/Data/Application/Technology) current-state reading of a specific body, if deeper organisational detail is needed than the sector-wide gap analysis covers |
| Adapt | `bb-sourcing-researcher` | Real market/DPG options for BUY calls; lock-in risk assessment |
| Adapt / Plan | `govstack-cost-estimator` | Explicit cost comparison between siloed (per-programme) and shared (whole-of-government) sourcing, to justify SHARE calls to a budget-holder |

Pull these in for their specialised sub-task; this skill (`ea-lifecycle-method`)
owns the overall five-phase sequence, the discipline at each gate, and the
six deliverables that tie the whole engagement together.
