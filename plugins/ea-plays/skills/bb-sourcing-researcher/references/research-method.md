# Research Method: Source Map and Search Patterns

This file tells you *where to look* and *how to search* for each building block, and what to
expect (maturity priors). It does not hard-code vendor names beyond stable anchors, because
the market moves — always confirm current products with live research.

---

## The 18 blocks and the capability each delivers

### Infrastructure blocks (Phase 1+ — always needed)
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

### Functional blocks (Phase 2+)
13. **MyGov / Citizen Portal** — one-stop citizen/business front-end
14. **Digital Wallet** — citizen-held verifiable credentials and documents
15. **Analytics** — analytics, dashboards, reporting
16. **Scheduler** — appointment and scheduling services
17. **eMarketplace** — government procurement, catalogues
18. **AI/ML** — machine-learning services for automation/decision support

---

## Source map — where to look, in priority order

### Tier 1 — Curated, government-vetted (always check first)
- **GovStack Building Block Software catalogue** — `govstack.global/software/`. Filter by
  building block. Records the product, model (open-source/proprietary), and **compliance
  level** (Level 1 ⭐ / Level 2 ⭐⭐). Self-assessed, submission-ordered, product-agnostic.
- **GovMarket** — `govstack.global/our-offerings/govmarket/` for the broader software/service
  directory.
- **Digital Public Goods Alliance (DPGA) registry** — vetted DPGs. The authoritative list of
  open-source candidates with a development/standards endorsement.

### Tier 2 — Project / product primary sources
- Project sites and docs for the anchor DPGs: MOSIP, Mojaloop / Mifos, X-Road (NIIS), OpenG2P,
  OpenSPP, OpenCRVS, DHIS2, RapidPro, QGIS/GeoServer, EU DSS / EUDI wallet reference.
- GitHub orgs for licence, activity, and module structure (e.g. `github.com/mosip`,
  `github.com/openMF`, `github.com/nordic-institute/X-Road`).

### Tier 3 — Comparison / landscape sources
- OSS comparison write-ups (e.g. BPM-engine comparisons, OSS-GIS guides) to surface options
  not yet in the curated catalogues. Treat as leads to verify, not as authority.
- Vendor sites for commercial options — confirm positioning, not marketing claims.

### Tier 4 — In-country grounding
- Use `country-context-data` skill for in-country SI presence, mobile-money rails, local SMS
  aggregators, cloud/data-residency rules. A globally-strong product that has no in-country
  integrator or violates data-residency law is not realistically available.

---

## Search-query patterns that work

- Per block, not combined: `"<block capability> open source government DPI"` then
  `"<block capability> vendor / commercial provider government"`.
- Anchor + alternatives: `"<anchor product> alternatives <block>"` (e.g. "X-Road alternatives
  data exchange", "Camunda alternatives BPM open source").
- Catalogue scan: fetch `govstack.global/software/` and read the listing for each block.
- Deployment evidence: `"<product> deployed <country/region>"` to verify real-world use.
- Licence/lock-in: open the GitHub repo or licence page rather than trusting a summary.
- Avoid stale years — use the current year or no year, never a past year, in queries.

---

## Maturity priors (what to expect before you search)

These priors set expectations and the likely sourcing posture; **verify, don't assume**.

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

## Capture template per candidate

For every product surfaced, record:

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

If a field cannot be evidenced from research, mark it "unconfirmed" rather than guessing.
