<!-- fixture: Progressa (fictional) · canonical: tests/progressa.md · keep consistent with it -->
# Worked Example: Progressa Education Sector — 18-Block Sourcing Analysis

A complete pass over all eighteen blocks, sourced from live market research, with a posture and
lock-in verdict for each. Use it as a model to follow or compare against. Product positioning
reflects research at the time of writing — re-verify before reuse. This is an options analysis,
not a procurement recommendation.

Context assumed: lower-middle-income country, education sector, sovereignty-conscious
(self-hosting preferred). Existing systems: a district EMIS with its own learner numbering; the
PNIA National ID at 78% adult coverage with a live e-KYC platform; Linkup, an X-Road 7.x
deployment in pilot with four members, of which MoEYS is **not** one; and PayPro, the national
fast-payment system operated by the Central Bank of Progressa, which the scholarship programme
does not use — it still pays by cheque. Bespoke-footprint target < 20%.

---

## How postures were reached

Each block ran through the decision flow in `build-vs-buy.md`: existing system? → mature OSS? →
competitive/channel/legal commercial? → configure on adjacent block? → named custom requirement?
Step 1 short-circuits three blocks here — Identity, Payment and Information Mediator each have a
national system already running — so for those the question is onboarding, not procurement. The
anchor open-source DPGs (MOSIP, Mojaloop/Mifos, X-Road, OpenG2P/CRVS/SPP, Superset, QGIS) carry
the rest of the infrastructure blocks; the thin-market blocks (Consent, Scheduler) land on
Configure.

---

## Infrastructure blocks

| # | Block | Top OSS option | Top commercial option | Posture | Lock-in | Adds to bespoke? |
|---|---|---|---|---|---|---|
| 1 | Identity | (moot — PNIA National ID is live; MOSIP is the comparator, not the buy) | Idemia/Thales/NEC as ecosystem partners | **Reuse existing (PNIA)** | Low | No |
| 2 | Payment | Mojaloop + Mifos Payment Hub EE (GovStack-listed) | Mobile-money rails; aggregators | **Reuse existing (PayPro)** + commercial channel | Low (switch) / Med (rails) | No |
| 3 | Information Mediator | X-Road (NIIS, MIT) — already deployed as Linkup | UXP/Cybernetica (GovStack-listed) | **Reuse existing (Linkup) — onboard MoEYS** | Low | No |
| 4 | Registration | OpenG2P Registry; OpenCRVS; OpenSPP (DPGs) | Digital Registries System (GDB, GovStack-listed) | Reuse-OSS | Low | No |
| 5 | Workflow | Camunda (GovStack-listed); Flowable; jBPM | Appian/Pega/ProcessMaker | Reuse-OSS / Open-core | Low–Med | No |
| 6 | Messaging | Novu; RapidPro (DPG, SMS/USSD) | Twilio; local SMS aggregators | Reuse-OSS + commercial channel | Low (orchestration) / Med (channel) | No |
| 7 | GIS | QGIS; GeoServer; PostGIS | Esri ArcGIS | Reuse-OSS | Low | No |
| 8 | Consent | MOSIP Inji/Data Share; IM access-control patterns | OneTrust (web-consent oriented) | **Configure** (on IM/Identity) | Low if APIs specified | At-risk |
| 9 | E-signature | EU DSS; EJBCA/Dogtag PKI | QTSP (Entrust/Ascertia/Docaposte) | Reuse-OSS + commercial trust services | Low (lib) / Med (QTSP) | No |
| 10 | QR Code | ZXing; per-language QR libs; MOSIP Pixelpass | (rarely warranted) | **Configure** / Reuse-OSS | None | No |
| 11 | Adapters | Apache Camel; WSO2 Micro Integrator | MuleSoft/Boomi/Talend (iPaaS) | Reuse-OSS | Low (Camel) / High (iPaaS) | No |
| 12 | No-code/Low-code | Budibase; Appsmith; Baserow (GovStack-listed) | OutSystems/Mendix/Power Platform | Reuse-OSS | Low (OSS) / High (commercial low-code) | No |

**Worked reasoning, Block 3 (Information Mediator):** Decision-flow step 1 answers this one. An
X-Road 7.x deployment is already live in pilot as Linkup, with four members and a documented
onboarding procedure. → Reuse existing; the sourcing decision collapses into an onboarding
decision, and the finding to carry forward is that MoEYS is not yet a member. **Anti-pattern
avoided:** procuring a second exchange layer for the education sector, or — the cheaper-looking
and worse option — another direct database link of the kind the tax authority built to the
business register in 2022 and has not migrated since.

**Worked reasoning, Block 1 (Identity):** Also step 1. PNIA runs the National ID (78% adult
coverage) and an e-KYC platform. → Reuse existing, not Reuse-OSS: MOSIP is the comparator you
benchmark PNIA's APIs against, not a thing to deploy. **Carry forward the constraint, not just
the posture:** PNIA issues IDs only at 16, so for a primary-school learner the National ID cannot
be the key, and the civil register (71% birth registration, paper-first) is the legal anchor. A
learner-identity design that assumes the National ID will fail on its main population.

**Worked reasoning, Block 8 (Consent):** No dominant standalone DPG. The substrate already exists
in the Identity (MOSIP Inji/Data Share) and Information Mediator layers. → Configure consent as an
auditable, first-class feature of those blocks, specifying open APIs. **Drift flag:** without that
API discipline this silently becomes a bespoke consent ledger — latent footprint. Sharper here
than elsewhere: the Data Protection Act 2023 requires a legal basis for sharing minors' data and
parental consent for non-statutory uses, so this block carries a legal obligation, not just a
feature.

---

## Functional blocks

| # | Block | Top OSS option | Top commercial option | Posture | Lock-in | Adds to bespoke? |
|---|---|---|---|---|---|---|
| 13 | MyGov / Portal | Liferay (CE); Drupal; MOSIP Inji Web | Adobe AEM/Sitecore (DXP) | Reuse-OSS / SI build | Low (OSS) / High (DXP) | No |
| 14 | Digital Wallet | MOSIP Inji; EUDI reference; Hyperledger Aries/walt.id | IDEMIA/Thales/Spruce | Reuse-OSS (standards-led) | Low if W3C VC standards | No |
| 15 | Analytics | Superset; Metabase; DHIS2 (DPG) | Power BI/Tableau/Qlik | Reuse-OSS | Low | No |
| 16 | Scheduler | MOSIP pre-registration; Cal.com; Easy!Appointments | Calendly/MS Bookings | **Configure** (via Workflow / pre-reg) | Low–Med | At-risk |
| 17 | eMarketplace | OCDS tooling; Odoo; Medusa/Saleor | SAP Ariba/Coupa; GeM (reference) | **Configure** / Reuse-OSS | Low (OCDS) / High (suites) | At-risk |
| 18 | AI/ML | PyTorch/scikit-learn; open LLMs; MLflow/Kubeflow | Cloud AI (SageMaker/Vertex); hosted LLM APIs | **Configure** (governed capability) | Med (cloud/data residency) | Depends |

**Worked reasoning, Block 15 (Analytics):** Step 1 does *not* short-circuit here, and it is worth
saying why. The district EMIS is a records system on the ministry's own learner numbering, not an
analytics platform, and it holds one of three disagreeing copies of the learner. → Reuse-OSS
(Superset or Metabase over a governed warehouse). **Precondition, not a footnote:** analytics
built on top of three unreconciled learner lists reports three different enrolment figures with
equal confidence. Sequence this block after the registry work, not alongside it.

**Worked reasoning, Block 18 (AI/ML):** There is no procurable "AI building block." Treat it as a
governed capability applied to the other blocks' data (e.g. dropout-risk prediction on district
EMIS records). → Configure with open-source/self-hosted frameworks where citizen-data sovereignty
is required; flag data-protection, bias, and explainability governance as preconditions — and
note that minors' data brings the Data Protection Act 2023 consent requirement with it.

---

## Bespoke-footprint roll-up

- **Reuse:** 14 of 18 blocks — three of them (Identity, Payment, Information Mediator) reusing a
  national system that already exists rather than deploying anything, the other eleven reusing
  open-source products. No footprint contribution beyond clean integration glue.
- **Configure:** 4 blocks (Consent, Scheduler, eMarketplace, AI/ML), of which Consent, Scheduler
  and eMarketplace are **at-risk** (latent footprint if open APIs are not mandated). QR Code is
  Configure-but-safe at library level and is counted with Reuse above.
- **Custom-build:** 0 blocks. No block produced a named requirement unmet by product or
  configuration.

14 + 4 + 0 = 18.

**Verdict:** roughly 0% hard custom, with up to ~3 blocks of latent footprint if API discipline
slips. Comfortably inside the <20% target **provided** the Configure blocks are delivered as
API-first features of adjacent blocks rather than drifting into bespoke builds — and provided the
three Reuse-existing postures survive contact with the onboarding problem below.

---

## Cross-cutting findings for this context

- **Existing-system reuse is the cheapest posture and three foundational blocks already have
  one.** Identity, payment and data exchange are running nationally. The education sector's task
  is onboarding, not procurement — check the BDAT portfolio before sourcing anything new.
- **The onboarding, not the product, is the risk.** MoEYS is not a Linkup member and the
  scholarship programme does not use PayPro. A correct Reuse-existing posture delivers nothing
  until the ministry is a member of the rail it is told to reuse.
- **PDGA's mandate is coordinating, not binding.** Every Reuse-existing posture above depends on a
  body that cannot compel a ministry to onboard. This is the single largest threat to the 0%
  custom verdict: a ministry that cannot be made to join builds its own.
- **Thin-market blocks** (Consent, Scheduler) have no dominant product; deliver as configured
  features and specify open APIs. This is the main footprint risk on the product side.
- **Channel dependencies** are commercial and in-country: messaging (local SMS aggregators) needs
  commercial integration regardless of platform choice. Payment is the exception — the rail is
  domestic and public, so the gap is a disbursement flow, not a switch.
- **Sovereignty** favours self-hosted OSS across the board; the main tension is AI/ML, where the
  strongest models are hosted commercial APIs that may breach data-residency rules.
- **Enabling conditions:** the Reuse savings depend on a governance authority with a legal mandate
  owning the shared blocks, sustained financing for operations, and a credible in-country or
  regional SI market. The fixture supplies none of the three cleanly — a single donor-funded
  contract architect at PDGA, an annual budget cycle with no multi-year ICT envelopes, and a 2016
  register still under single-vendor maintenance. Absence of any of these turns a correct posture
  into a delivery risk.

---

## Hand-off

Feed the posture column into `ea-cost-case`: Reuse blocks model as shared infrastructure;
Configure blocks add modest integration cost; any Custom block (none here) carries full build +
ops. The sourcing posture is the *input* to the cost comparison, not a second cost model.
