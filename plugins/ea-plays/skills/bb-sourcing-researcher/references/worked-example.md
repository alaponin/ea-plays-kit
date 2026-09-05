# Worked Example: Gambia Education Sector — 18-Block Sourcing Analysis

A complete pass over all eighteen blocks, sourced from live market research, with a posture and
lock-in verdict for each. Use it as a model to follow or compare against. Product positioning
reflects research at the time of writing — re-verify before reuse. This is an options analysis,
not a procurement recommendation.

Context assumed: low-income country, education sector, sovereignty-conscious (self-hosting
preferred), existing systems include DHIS2 SEMIS, iLearn Gambia, an SMS attendance system, and
a national digital ID effort. Bespoke-footprint target < 20%.

---

## How postures were reached

Each block ran through the decision flow in `build-vs-buy.md`: existing system? → mature OSS? →
competitive/channel/legal commercial? → configure on adjacent block? → named custom requirement?
The anchor open-source DPGs (MOSIP, Mojaloop/Mifos, X-Road, OpenG2P/CRVS/SPP, DHIS2, QGIS) carry
most infrastructure blocks; the thin-market blocks (Consent, Scheduler) land on Configure.

---

## Infrastructure blocks

| # | Block | Top OSS option | Top commercial option | Posture | Lock-in | Adds to bespoke? |
|---|---|---|---|---|---|---|
| 1 | Identity | MOSIP (DPG, MPL 2.0) | Idemia/Thales/NEC as ecosystem partners | Reuse-OSS + commercial partners | Low (platform) / Med (biometric layer) | No |
| 2 | Payment | Mojaloop + Mifos Payment Hub EE (GovStack-listed) | Mobile-money rails (MTN MoMo, Orange Money); aggregators | Reuse-OSS + commercial channel | Low (switch) / Med (rails) | No |
| 3 | Information Mediator | X-Road (NIIS, MIT) | UXP/Cybernetica (GovStack-listed) | Reuse-OSS | Low | No |
| 4 | Registration | OpenG2P Registry; OpenCRVS; OpenSPP (DPGs) | Digital Registries System (GDB, GovStack-listed) | Reuse-OSS | Low | No |
| 5 | Workflow | Camunda (GovStack-listed); Flowable; jBPM | Appian/Pega/ProcessMaker | Reuse-OSS / Open-core | Low–Med | No |
| 6 | Messaging | Novu; RapidPro (DPG, SMS/USSD) | Twilio; Africa's Talking (local SMS) | Reuse-OSS + commercial channel | Low (orchestration) / Med (channel) | No |
| 7 | GIS | QGIS; GeoServer; PostGIS | Esri ArcGIS | Reuse-OSS | Low | No |
| 8 | Consent | MOSIP Inji/Data Share; IM access-control patterns | OneTrust (web-consent oriented) | **Configure** (on IM/Identity) | Low if APIs specified | At-risk |
| 9 | E-signature | EU DSS; EJBCA/Dogtag PKI | QTSP (Entrust/Ascertia/Docaposte) | Reuse-OSS + commercial trust services | Low (lib) / Med (QTSP) | No |
| 10 | QR Code | ZXing; per-language QR libs; MOSIP Pixelpass | (rarely warranted) | **Configure** / Reuse-OSS | None | No |
| 11 | Adapters | Apache Camel; WSO2 Micro Integrator | MuleSoft/Boomi/Talend (iPaaS) | Reuse-OSS | Low (Camel) / High (iPaaS) | No |
| 12 | No-code/Low-code | Budibase; Appsmith; Baserow (GovStack-listed) | OutSystems/Mendix/Power Platform | Reuse-OSS | Low (OSS) / High (commercial low-code) | No |

**Worked reasoning, Block 3 (Information Mediator):** A mature DPG (X-Road) with 20+ national
deployments and an integrator market exists; no sovereignty blocker (self-hostable). → Reuse-OSS.
Commercial X-Road distributions (UXP) exist if enterprise support is preferred, but the open core
plus an SI contract is the lower-lock-in route. **Anti-pattern avoided:** a generic ESB would
recreate point-to-point integration without X-Road's PKI/non-repudiation/audit envelope.

**Worked reasoning, Block 8 (Consent):** No dominant standalone DPG. The substrate already exists
in the Identity (MOSIP Inji/Data Share) and Information Mediator layers. → Configure consent as an
auditable, first-class feature of those blocks, specifying open APIs. **Drift flag:** without that
API discipline this silently becomes a bespoke consent ledger — latent footprint.

---

## Functional blocks

| # | Block | Top OSS option | Top commercial option | Posture | Lock-in | Adds to bespoke? |
|---|---|---|---|---|---|---|
| 13 | MyGov / Portal | Liferay (CE); Drupal; MOSIP Inji Web | Adobe AEM/Sitecore (DXP) | Reuse-OSS / SI build | Low (OSS) / High (DXP) | No |
| 14 | Digital Wallet | MOSIP Inji; EUDI reference; Hyperledger Aries/walt.id | IDEMIA/Thales/Spruce | Reuse-OSS (standards-led) | Low if W3C VC standards | No |
| 15 | Analytics | DHIS2 (DPG — already deployed: SEMIS); Superset; Metabase | Power BI/Tableau/Qlik | Reuse-OSS (extend existing) | Low | No |
| 16 | Scheduler | MOSIP pre-registration; Cal.com; Easy!Appointments | Calendly/MS Bookings | **Configure** (via Workflow / pre-reg) | Low–Med | At-risk |
| 17 | eMarketplace | OCDS tooling; Odoo; Medusa/Saleor | SAP Ariba/Coupa; GeM (reference) | **Configure** / Reuse-OSS | Low (OCDS) / High (suites) | At-risk |
| 18 | AI/ML | PyTorch/scikit-learn; open LLMs; MLflow/Kubeflow | Cloud AI (SageMaker/Vertex); hosted LLM APIs | **Configure** (governed capability) | Med (cloud/data residency) | Depends |

**Worked reasoning, Block 15 (Analytics):** An existing system already covers this — DHIS2 SEMIS
is deployed. → Extend/reuse, do not re-buy. Decision-flow step 1 short-circuits the rest. This is
the cheapest and lowest-risk posture available and should always be checked first.

**Worked reasoning, Block 18 (AI/ML):** There is no procurable "AI building block." Treat it as a
governed capability applied to the other blocks' data (e.g. dropout-risk prediction on SEMIS).
→ Configure with open-source/self-hosted frameworks where citizen-data sovereignty is required;
flag data-protection, bias, and explainability governance as preconditions.

---

## Bespoke-footprint roll-up

- **Reuse-OSS / Reuse-Commercial:** 14 of 18 blocks. No footprint contribution beyond clean
  integration glue.
- **Configure:** 4 blocks (Consent, Scheduler, eMarketplace, AI/ML), of which Consent, Scheduler
  and eMarketplace are **at-risk** (latent footprint if open APIs are not mandated). QR Code is
  Configure-but-safe (library-level).
- **Custom-build:** 0 blocks. No block produced a named requirement unmet by product or
  configuration.

**Verdict:** roughly 0% hard custom, with up to ~3 blocks of latent footprint if API discipline
slips. Comfortably inside the <20% target **provided** the Configure blocks are delivered as
API-first features of adjacent blocks rather than drifting into bespoke builds.

---

## Cross-cutting findings for this context

- **Thin-market blocks** (Consent, Scheduler) have no dominant product; deliver as configured
  features and specify open APIs. This is the main footprint risk.
- **Channel dependencies** are commercial and in-country: payments (mobile money) and messaging
  (local SMS aggregators) require commercial integration regardless of platform choice.
- **Existing-system reuse** is the cheapest posture and already applies to Analytics (DHIS2 SEMIS)
  and partially to Messaging (SMS attendance) and Identity (national ID effort) — check the BDAT
  portfolio before sourcing anything new.
- **Sovereignty** favours self-hosted OSS across the board; the main tension is AI/ML, where the
  strongest models are hosted commercial APIs that may breach data-residency rules.
- **Enabling conditions:** the Reuse-OSS savings depend on a governance authority with a legal
  mandate owning the shared blocks, sustained financing for operations, and a credible in-country
  or regional SI market. Absence of any of these turns a correct posture into a delivery risk.

---

## Hand-off

Feed the posture column into `govstack-cost-estimator`: Reuse blocks model as shared
infrastructure; Configure blocks add modest integration cost; any Custom block (none here) carries
full build + ops. The sourcing posture is the *input* to the cost comparison, not a second cost model.
