<!-- fixture: Progressa (fictional) · canonical: tests/progressa.md · keep consistent with it -->
# A worked example: the sourcing analysis of 18 blocks for the education sector of Progressa

This is a full pass over the eighteen blocks. It comes from live market research. Each block has
a posture and a verdict on its lock-in. Use it as a model. Follow it, or compare your analysis
against it. The position of each product in the market comes from the research at the time of
writing. Verify it again before you use it. This is an options analysis. It is not a
recommendation for a procurement.

The context of this example: a lower-middle-income country, the education sector, and a
government that cares about sovereignty and prefers to host its own systems. These systems exist:
a district EMIS with its own numbers for the learners; the PNIA National ID, which covers 78% of
the adults, with a live e-KYC platform; Linkup, which is a deployment of X-Road 7.x, in pilot with
four members, and MoEYS is **not** one of them; and PayPro, the national system for fast payments
that the Central Bank of Progressa operates. The scholarship programme does not use PayPro. It
still pays by cheque. The target for the bespoke footprint is less than 20%.

---

## How this example reached each posture

Each block went through the decision flow in `build-vs-buy.md`: does a system exist? → is there a
mature open-source product? → is this a competitive layer, a channel, or a commercial provider
that the law needs? → can an adjacent block give it as a configured feature? → is there a named
custom requirement?
Step 1 answers three blocks here. Identity, Payment and Information Mediator each have a national
system that operates now. For those three, the question is the onboarding and not the
procurement. The anchor open-source digital public goods carry the other infrastructure blocks.
They are MOSIP, Mojaloop and Mifos, X-Road, OpenG2P, OpenCRVS, OpenSPP, Superset and QGIS. The
blocks with a thin market, which are Consent and Scheduler, get the posture Configure.

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

**The reasoning for Block 3, the Information Mediator.** Step 1 of the decision flow answers this
block. A deployment of X-Road 7.x is live as a pilot, with the name Linkup, four members and a
documented onboarding procedure. → Reuse the system that exists. The sourcing decision becomes an
onboarding decision. Carry this finding forward: MoEYS is not a member yet. **The anti-pattern
that this avoids:** to procure a second layer for exchange for the education sector. It also
avoids the option that looks cheaper and is worse, which is one more direct link between two
databases, like the link that the tax authority built to the business register in 2022 and never
migrated.

**The reasoning for Block 1, Identity.** Step 1 answers this block also. PNIA operates the
National ID, which covers 78% of the adults, and an e-KYC platform. → Reuse the system that
exists. The posture is not Reuse-OSS. MOSIP is the comparator that you use to benchmark the APIs
of PNIA. It is not a product to deploy. **Carry the constraint forward, not only the posture.**
PNIA issues an ID only at 16 years. Therefore the National ID cannot be the key for a learner in
a primary school. The civil register is the legal anchor, and it registers 71% of the births and
works on paper first. A design for the identity of a learner that uses the National ID fails for
the main population of that design.

**The reasoning for Block 8, Consent.** No digital public good dominates this category. The
substrate exists in the Identity layer, with MOSIP Inji and Data Share, and in the Information
Mediator layer. → Configure consent as a primary feature of those blocks, and make it auditable.
Specify open APIs. **The flag for drift:** without the discipline of an API, this block becomes a
bespoke ledger for consent, in silence, and that is latent footprint. This block matters more
than the others here. The Data Protection Act 2023 needs a legal basis to share the data of a
minor, and it needs the consent of a parent for a use that is not statutory. Therefore this block
carries a legal obligation. It is not only a feature.

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

**The reasoning for Block 15, Analytics.** Step 1 does *not* answer this block, and the reason
matters. The district EMIS is a system of records on the numbers that the ministry gives to the
learners. It is not a platform for analytics, and it holds one of three copies of the learner that
do not agree. → Reuse-OSS, with Superset or Metabase over a warehouse that a body governs. **This
is a precondition, not a footnote:** analytics on three lists of learners that nobody reconciled
reports three different figures for the enrolment, with the same confidence in each one. Put this
block after the work on the registry. Do not put it next to that work.

**The reasoning for Block 18, AI and ML.** There is no "AI building block" that a body can
procure. Treat it as a capability that a body governs and applies to the data of the other blocks.
An example is the prediction of the risk that a learner leaves school, on the records of the
district EMIS. → Configure it with open-source frameworks that you host yourself, where the
sovereignty of the data of the citizens needs that. Flag three preconditions: the governance for
data protection, for bias, and for the explanation of a decision. Also record that the data of a
minor brings the requirement for consent in the Data Protection Act 2023.

---

## Bespoke-footprint roll-up

- **Reuse: 14 of the 18 blocks.** Three of them, which are Identity, Payment and Information
  Mediator, reuse a national system that exists. They deploy nothing. The other eleven reuse an
  open-source product. They add nothing to the footprint, except the small amount of code that
  integrates them.
- **Configure: 4 blocks**, which are Consent, Scheduler, eMarketplace, and AI and ML. Three of
  them, Consent, Scheduler and eMarketplace, are **at risk**. They become latent footprint if
  nobody makes open APIs mandatory. QR Code is Configure and is safe, because it is at the level
  of a library. The count above puts it with Reuse.
- **Custom-build: 0 blocks.** No block gave a named requirement that a product or a configuration
  cannot meet.

14 + 4 + 0 = 18.

**The verdict:** about 0% is truly custom. Up to 3 blocks become latent footprint if the
discipline of the API fails. This is well inside the target of less than 20%, **on two
conditions**. First, a team must deliver the Configure blocks as features of an adjacent block,
with the API first, and must not let them become bespoke builds. Second, the
three Reuse-existing postures survive contact with the onboarding problem below.

---

## Cross-cutting findings for this context

- **Existing-system reuse is the cheapest posture and three foundational blocks already have
  one.** Identity, payment and data exchange are running nationally. The education sector's task
  is onboarding, not procurement — check the BDAT portfolio before sourcing anything new.
- **The risk is the onboarding. It is not the product.** MoEYS is not a member of Linkup, and the
  scholarship programme does not use PayPro. A correct posture of Reuse-existing gives nothing
  until the ministry becomes a member of the rail that it must reuse.
- **The mandate of PDGA coordinates. It does not bind.** Each posture of Reuse-existing above
  depends on a body that cannot oblige a ministry to join. This is the largest threat to the
  verdict of 0% custom code. A ministry that nobody can oblige to join builds its own system.
- **The blocks with a thin market**, which are Consent and Scheduler, have no dominant product.
  Deliver them as configured features, and specify open APIs. On the side of the products, this is
  the main risk to the footprint.
- **The channels are commercial, and they are inside the country.** Messaging needs an
  integration with a local SMS aggregator, whichever platform you choose. Payment is the
  exception. The rail is domestic and public, so the gap is a flow for disbursement and not a
  switch.
- **Sovereignty prefers open-source software that you host yourself**, for each block. The
  tension is in AI and ML. There the strongest models are commercial APIs that a company hosts,
  and they can break the rules on data residency.
- **The conditions that the postures need.** The savings from reuse need three conditions: a
  governance authority with a legal mandate that owns the shared blocks; financing for the
  operations that continues; and a credible market of system integrators, in the country or in the
  region. The fixture gives none of the three clearly. It has one architect at PDGA, on a contract
  that a donor funds; a budget cycle of one year, with no ICT envelope for several years; and a
  register from 2016 that one vendor still maintains. If one condition is absent, a correct posture
  becomes a risk to the delivery.

---

## The hand-off

Give the posture column to `ea-cost-case`. Model a Reuse block as shared infrastructure. A
Configure block adds a small cost to integrate it. A Custom block, and there is none here, carries
the full cost of the build and of the operations. The sourcing posture is the *input* to the cost
comparison. It is not a second cost model.
