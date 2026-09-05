# The research method: the source map and the search patterns

This file tells you *where to look* for each building block, *how to search* for it, and
what to expect, which is the maturity prior. It gives the name of a vendor only for a stable
anchor product, because the market moves. Always confirm the products that exist now with
live research.

---

## The 18 blocks and the capability each delivers

### The infrastructure blocks. A country needs these from Phase 1
1. **Identity** — digital identity, authentication, e-signature
2. **Payment** — payment processing and (at scale) interoperable real-time switching
3. **Information Mediator** — secure, decentralised inter-agency data exchange (X-Road model)
4. **Registration** — functional registries of people, entities, objects
5. **Workflow** — business-process automation, case management (BPMN/CMMN/DMN)
6. **Messaging** — multi-channel notifications (SMS, email, push, in-app)
7. **GIS** — geographic data, mapping, spatial services
8. **Consent** — citizen consent management for data sharing
9. **E-signature** — electronic signing and verification (often eIDAS-aligned)
10. **QR Code** — generation/verification of QR codes for verification and access
11. **Adapters** — legacy-system integration into the BB ecosystem
12. **No-code/Low-code** — rapid application development

### The functional blocks. A country adds these from Phase 2
13. **MyGov / Citizen Portal** — one-stop citizen/business front-end
14. **Digital Wallet** — citizen-held verifiable credentials and documents
15. **Analytics** — analytics, dashboards, reporting
16. **Scheduler** — appointment and scheduling services
17. **eMarketplace** — government procurement, catalogues
18. **AI/ML** — machine-learning services for automation/decision support

---

## The source map — where to look, in the order of priority

### Tier 1 — curated sources that a government body checked. Look here first
- The **GovStack Building Block Software catalogue** — `govstack.global/software/`. Filter it
  by building block. It records the product, the model, which is open-source or proprietary,
  and the **compliance level**, which is Level 1 ⭐ or Level 2 ⭐⭐. Each product assessed
  itself. The list is in the order of submission. It does not prefer a product.
- **GovMarket** — `govstack.global/our-offerings/govmarket/`, for the wider directory of
  software and services.
- The registry of the **Digital Public Goods Alliance (DPGA)** — the digital public goods
  that the alliance checked. It is the authoritative list of open-source candidates that have
  an endorsement for their development and their standards.

### Tier 2 — the primary sources of a project or a product
- The sites and the documentation of the anchor digital public goods: MOSIP, Mojaloop and
  Mifos, X-Road (NIIS), OpenG2P, OpenSPP, OpenCRVS, DHIS2, RapidPro, QGIS and GeoServer, and
  the reference implementations of EU DSS and the EUDI wallet.
- The GitHub organisations, for the licence, the activity and the structure of the modules.
  Examples are `github.com/mosip`, `github.com/openMF` and
  `github.com/nordic-institute/X-Road`.

### Tier 3 — sources that compare products or describe the landscape
- Articles that compare open-source products, such as a comparison of BPM engines or a guide
  to open-source GIS. They show you options that the curated catalogues do not have yet.
  Treat them as leads to verify. They are not an authority.
- The sites of the vendors, for a commercial option. Confirm the position of the product in
  the market. Do not confirm a marketing claim.

### Tier 4 — the reality inside the country
- Use the `country-context-pack` skill for the system integrators that are present in the
  country, the mobile-money rails, the local SMS aggregators, and the rules for the cloud and
  for data residency. A product that is strong globally is not available in this country when
  it has no integrator there, or when it breaks the law on data residency.

---

## The patterns of search query that work

- Search for one block at a time. Do not combine the blocks. Search
  `"<block capability> open source government DPI"`, then
  `"<block capability> vendor / commercial provider government"`.
- Search for the alternatives to an anchor product: `"<anchor product> alternatives <block>"`.
  Examples are "X-Road alternatives data exchange" and "Camunda alternatives BPM open
  source".
- Scan the catalogue: read `govstack.global/software/` and read the entries for each block.
- Find the evidence of a deployment: `"<product> deployed <country/region>"`.
- For the licence and the lock-in, open the GitHub repository or the licence page. Do not
  trust a summary.
- Do not put an old year in a query. Use the current year, or use no year.

---

## Maturity priors (what to expect before you search)

A prior tells you what to expect, and the sourcing posture that is probable. **Verify each
prior. Do not assume it.**

| Block | OSS market | Likely default posture | Notes |
|---|---|---|---|
| Identity | Strong (MOSIP) | Reuse-OSS + commercial partners | Biometrics/printing = competitive commercial layer |
| Payment | Strong (Mojaloop/Mifos) | Reuse-OSS + commercial channels | Mobile-money rails are commercial and in-country |
| Information Mediator | Strong (X-Road) | Reuse-OSS | Commercial X-Road distros exist (e.g. UXP) |
| Registration | Strong (OpenG2P/CRVS/SPP) | Reuse-OSS | Distinguish registry from app database |
| Workflow | Strong (Camunda/Flowable/jBPM) | Reuse-OSS / Open-core | Horizontal BPM, not gov-specific |
| Messaging | Moderate (Novu/RapidPro) | Reuse-OSS + commercial channel | SMS/USSD channel is commercial, local |
| GIS | Strong (QGIS/GeoServer/PostGIS) | Reuse-OSS | Esri is the heavy commercial incumbent |
| Consent | **Thin / gap** | Configure (on IM or Identity) | No dominant standalone DPG |
| E-signature | Moderate (EU DSS, PKI OSS) | Reuse-OSS + commercial trust services | QTSP may be legally required |
| QR Code | Library-level (ZXing etc.) | Configure / Reuse-OSS | Almost never a purchase |
| Adapters | Strong (Camel/WSO2) | Reuse-OSS | iPaaS is the commercial alternative |
| No-code/Low-code | Strong (Budibase/Appsmith) | Reuse-OSS | Commercial low-code = high lock-in |
| MyGov / Portal | Strong (Liferay/Drupal/CMS) | Reuse-OSS / SI build | Often a thin portal over IM services |
| Digital Wallet | Emerging (MOSIP Inji, EUDI) | Reuse-OSS (standards-led) | Fast-moving; favour W3C VC standards |
| Analytics | Strong (DHIS2/Superset/Metabase) | Reuse-OSS | DHIS2 directly relevant in education/health |
| Scheduler | **Thin / gap** | Configure (via Workflow or pre-reg) | No gov-specific DPG |
| eMarketplace | Emerging (OCDS, Odoo, GeM model) | Configure / Reuse-OSS | Standards (OCDS) more mature than products |
| AI/ML | General-purpose only | Configure (governed capability) | Not a procurable "block"; apply with governance |

---

## What to record for each candidate

Record these nine items for each product that you find:

```
Product:            <name>
Model:              OSS (DPG) | OSS | Open-core | Commercial
GovStack-listed:    No | Level 1 | Level 2
Maintainer/backer:  <org / foundation / company>
Licence:            <e.g. MPL 2.0, MIT, Apache 2.0, proprietary>
Deployment evidence:<countries/programmes, with source>
Lock-in vector:     <none | data | licence | proprietary tooling | ecosystem>
Fit note:           <one line: where it fits, caveats>
```

If your research gives no evidence for a field, write "unconfirmed" in it. Do not guess.
