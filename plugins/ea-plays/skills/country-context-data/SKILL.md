---
name: country-context-data
description: >
  Use this skill whenever the user needs to gather public data about a country for policy, research, or digital transformation projects — especially in education, governance, public services, or economic development. Triggers include: "gather country data", "find public statistics for [country]", "get education indicators", "assess digital readiness", "ICT infrastructure data", "socioeconomic context", "SDG progress", "governance indicators", "labor market data", "corruption index", "e-government maturity", "human development index", "internet affordability", "workforce skills", "school connectivity", "schools with internet", "Giga maps", "Project Connect", "national ID system", "digital identity programme", "cross-agency systems", "digital government strategy", "GovTech maturity", "African digital transformation". Also trigger when preparing a needs assessment, country brief, policy brief, baseline report, or feasibility study for any public sector digital project.
---

# Country Context Data Skill

A skill for gathering authoritative, publicly available data about a country to support digital transformation projects, policy development, and public sector research — especially in education, governance, and public services. Includes specific guidance for African countries on identity programmes, cross-agency systems, and digital government strategies.

---

## When to Use This Skill

Use this skill when the user needs:
- Background statistics for a country (education, ICT, economy, demographics, governance)
- Digital readiness and e-government maturity assessments
- SDG progress tracking (especially SDG 4: Education; SDG 16: Governance; SDG 9: Infrastructure)
- Labor market and workforce skills analysis
- Governance quality and institutional capacity assessment
- Baseline data for project proposals, needs assessments, or policy briefs
- Cross-country comparisons on any development indicator
- Internet affordability and equity analysis
- School connectivity mapping, monitoring, and infrastructure planning (Giga / Project Connect)
- National digital identity programme status and cross-agency interoperability (especially Africa)
- National digital government strategy documents and GovTech maturity

---

## Data Sources Overview

### Core Sources (always query)
| Source | Best For | API / Access | Auth |
|---|---|---|---|
| World Bank Open Data | Socioeconomic, education, ICT, governance, ID coverage | `https://api.worldbank.org/v2/` | No |
| UNESCO UIS | Education-specific statistics | `http://api.uis.unesco.org/` | Free key |
| UN SDG API | SDG monitoring across all goals | `https://unstats.un.org/SDGAPI/v1/` | No |
| ITU DataHub | ICT infrastructure, internet access | `https://datahub.itu.int/` | No |
| UNICEF Data | Child equity, out-of-school rates | `https://sdmx.data.unicef.org/` | No |

### Governance & Institutional Quality
| Source | Best For | Access | Auth |
|---|---|---|---|
| World Governance Indicators (WB) | Rule of law, corruption, gov. effectiveness | WB API (`GV.*` codes) | No |
| Transparency International CPI | Corruption Perceptions Index | CSV/JSON download | No |
| Open Government Partnership | OGP commitments and action plans | `https://www.opengovpartnership.org/data/` | No |

### Digital Government, GovTech & e-Services
| Source | Best For | Access | Auth |
|---|---|---|---|
| World Bank GovTech Maturity Index (GTMI) | Cross-agency systems, back-office digitalization, 198 countries | WB DataBank | No |
| UN e-Government Survey (UNDESA) | EGDI, online services maturity, e-participation | Dataset download | No |
| OECD Digital Government Index | Gov. digital maturity (OECD members) | `https://stats.oecd.org/` | No |
| EU DESI | Digital economy & society (EU only) | `https://digital-agenda-data.eu/` | No |

### Digital Identity & Civil Registration
| Source | Best For | Access | Auth |
|---|---|---|---|
| World Bank ID4D Dataset | ID ownership rates, birth registration, digital ID capabilities | WB DataBank + Data360 | No |
| UNECA Africa Digital ID Landscape (2023) | Country-level ID system profiles, legal frameworks, interoperability | PDF download | No |
| ID4Africa Movement | Country case studies, implementation maturity (48 African members) | `https://id4africa.com/` | No |
| AU Interoperability Framework for Digital ID | Continental standards for cross-agency/cross-border ID | PDF reference | No |

### African Digital Government Strategies & Frameworks
| Source | Best For | Access | Auth |
|---|---|---|---|
| Smart Africa Alliance | National digital strategies, Data Governance Blueprint, SADX pilot | `https://smartafrica.org/knowledge/` | No |
| UNECA Digital Strategy Repository | Co-developed national digital transformation strategies | `https://www.uneca.org/` | No |
| DIAL / ADLI Country Snapshots | DPI stack readiness — ID, payments, data exchange (Uganda, Tanzania, Nigeria, etc.) | `https://dial.global/work/adli/` | No |
| AU Digital Transformation Strategy 2020–2030 | Continental reference framework for strategy alignment | PDF reference | No |

### Human Development & Equity
| Source | Best For | Access | Auth |
|---|---|---|---|
| UNDP Human Development Reports | HDI, Gender Inequality, Multidim. Poverty | `https://hdr.undp.org/data-center/` | No |

### Labor Market & Skills
| Source | Best For | Access | Auth |
|---|---|---|---|
| ILO ILOSTAT | Employment, youth unemployment, skills by sector | SDMX API | No |

### Economic Competitiveness
| Source | Best For | Access | Auth |
|---|---|---|---|
| IMF World Economic Outlook | Macro projections, fiscal data | `https://www.imf.org/en/Data` | No |
| World Bank Business Ready | Regulatory environment | WB API (`IC.*` codes) | No |

### Connectivity & Infrastructure
| Source | Best For | Access | Auth |
|---|---|---|---|
| Ookla Speedtest Global Index | Real-world broadband/mobile speeds | Public download | No |
| A4AI Internet Affordability | Cost of 1GB as % of GNI | `https://a4ai.org/data/` | No |

### School Connectivity (Giga — UNICEF/ITU)
| Source | Best For | Access | Auth |
|---|---|---|---|
| Giga Maps / Project Connect | Geolocated school connectivity status (2.1M+ schools, 140 countries) | `https://api.gigamaps.org/` | Free key |
| Giga Daily Check App | Real-time school bandwidth/speed monitoring | Dashboard + API | Free key |
| Giga AI School Mapping | School location predictions from satellite imagery | GitHub + download | No |
| Giga Connectivity Cost Models | Technology options and cost scenarios per country | Engagement + reports | No |

### Education Quality & Assessments
| Source | Best For | Access | Auth |
|---|---|---|---|
| IEA (TIMSS / PIRLS) | Math, science, reading benchmarks (broader than PISA) | `https://www.iea.nl/data-tools/` | No |
| OECD PISA | Learning outcomes (OECD + partners) | `https://stats.oecd.org/` | No |

### Regional Sources
| Source | Best For | Access | Auth |
|---|---|---|---|
| Eurostat | EU-27 + candidates (rich granularity) | `https://ec.europa.eu/eurostat/api/` | No |
| OECD API | OECD member detailed datasets | `https://stats.oecd.org/SDMX-JSON/` | No |

See `references/api-guide.md` for detailed query patterns, indicator codes, and code snippets.

---

## Workflow

### Step 1: Clarify the Project Scope

Before querying, establish:
- **Country** (or countries) — get the ISO 3166-1 alpha-2 or alpha-3 code
- **Project domain** — education, governance, health, infrastructure, economic development, etc.
- **Key questions** — what does the user need to understand?
- **Time frame** — most recent snapshot, or trend over years?
- **Regional context** — African country? EU member? OECD member? This determines which source tiers apply.

### Step 2: Select Relevant Indicator Categories

#### 📚 Education System
- Net enrollment rate (primary, secondary, tertiary)
- Pupil-to-teacher ratio; government expenditure on education (% of GDP)
- Completion and dropout rates
- Learning outcomes (PISA/TIMSS scores if available)
- Out-of-school children rate

#### 🏫 School Connectivity (Giga / Project Connect)
- School geolocation and connectivity status by country (Giga Maps)
- % of mapped schools with internet access; connectivity type (fiber, cellular, satellite, none)
- Real-time bandwidth speeds measured at school level (Daily Check App)
- Infrastructure gap — schools without any connectivity
- Technology cost scenarios for connecting unconnected schools
- Meaningful connectivity threshold: ≥10 Mbps per school (Giga standard; target 20 Mbps)

#### 💻 Digital Infrastructure & Access
- Internet penetration (% of population); mobile and fixed broadband subscriptions
- Real-world internet speeds (Ookla); affordability — cost of 1GB mobile data (A4AI)
- Schools with internet access (UNESCO UIS); ICT Development Index (ITU)

#### 🪪 Digital Identity & Civil Registration (especially Africa)
- ID ownership rate — % of adults with official ID (ID4D Dataset)
- Birth registration rate — % of children under 5 registered (ID4D / UNICEF)
- Digital ID availability for online transactions (ID4D)
- National ID system type: foundational, functional, or none (UNECA Africa Digital ID Landscape)
- Cross-agency interoperability status (AU Interoperability Framework alignment)
- Legal and data protection framework maturity (UNECA / ID4Africa case studies)

#### 🖥️ Digital Government Maturity & Cross-Agency Systems
- GovTech Maturity Index — core systems, service delivery, citizen engagement, enablers (WB GTMI)
- e-Government Development Index / EGDI (UNDESA)
- Online Services Index and e-Participation Index (UNDESA)
- National digital government strategy: existence, age, alignment with AU DTS 2020–2030
- Cross-agency data sharing and interoperability systems (Smart Africa SADX, DIAL/ADLI)
- Digital Government Index (OECD members only)
- DESI score and sub-indices (EU members only)

#### 🏛️ Governance & Institutional Quality
- Government effectiveness, rule of law, control of corruption (WGI)
- Regulatory quality, political stability (WGI)
- Corruption Perceptions Index rank (TI)
- OGP membership and open data commitments

#### 🌍 Socioeconomic Context
- GDP per capita; Human Development Index (UNDP)
- Gender Inequality Index; Gini coefficient; Multidimensional Poverty Index
- Population total, urban/rural split; poverty headcount ratio

#### 💼 Labor Market & Workforce
- Youth unemployment rate (ILO); employment by sector
- Share of workforce in ICT sector; labor force participation rate

#### 💰 Economic Competitiveness & Fiscal
- GDP growth rate; public debt as % of GDP (IMF WEO)
- Ease of doing business / Business Ready rank (WB)
- R&D expenditure (% of GDP)

#### 🎯 SDG Indicators
- SDG 4 (Education): literacy, enrollment, learning outcomes, teacher training
- SDG 9 (Infrastructure): internet access, R&D, mobile networks
- SDG 16 (Governance): rule of law, transparency, legal identity (16.9)
- SDG 10 (Inequality): income inequality, social protection

### Step 3: Source Selection Strategy

```
Is the country an EU member or candidate?
  YES → Eurostat first (richest granularity), supplement with WB/UNESCO/DESI
  NO  → World Bank first (broadest coverage)

Is the country an OECD member?
  YES → Add OECD API for Digital Gov Index, PISA, Education at a Glance
  NO  → Use UNESCO UIS for education, ILO for labor, UNDP for human development

Is the country in sub-Saharan Africa?
  YES → Add Africa-specific tier (see African Country Block below)

Governance data needed?
  Always → World Bank WGI indicators (GV.* codes)
  Also   → Transparency International CPI download
  If EU  → DESI digital public services sub-index

Digital government maturity?
  Always → World Bank GTMI (cross-agency systems, 198 countries)
  Always → UN e-Government Survey (EGDI download, biennial)
  OECD   → OECD Digital Government Index
  EU     → DESI Digital Public Services index

Digital identity / cross-agency systems?
  Always → World Bank ID4D Dataset (DataBank, no auth)
  Africa → UNECA Africa Digital ID Landscape (2023 PDF)
  Africa → ID4Africa country case studies
  Africa → Smart Africa Alliance blueprints and SADX status
  Africa → DIAL/ADLI country snapshots (DPI stack)

National digital strategy documents?
  Africa → UNECA Digital Strategy Repository (co-developed strategies)
  Africa → Smart Africa Alliance country blueprint index
  All    → ITU Digital Development Dashboard (strategy existence/age)
  Check  → au.int for AU DTS 2020-2030 alignment

School connectivity data needed?
  Always → Giga Maps API (geolocated school connectivity status, 140 countries)
  Speeds → Giga Daily Check App (real-time bandwidth at school level)
  Planning → Giga Connectivity Cost Models (technology options + cost scenarios)
  Aggregate → UNESCO UIS SCHBSP indicator (% schools with internet, country-level)

Connectivity depth?
  Basic         → World Bank IT.* indicators (mirrors ITU, no auth)
  Real speeds   → Ookla Speedtest Global Index (download)
  Affordability → A4AI data
```

### African Country Block — Additional Sources to Always Check

For any sub-Saharan African country, run this additional query sequence after the core sources:

1. **World Bank ID4D DataBank** — adult ID ownership %, birth registration rate, digital ID availability
2. **World Bank GTMI** — GovTech maturity score and sub-index breakdown
3. **UNECA Africa Digital ID Landscape 2023** — check country entry for ID system type, legal framework, interoperability status
4. **Smart Africa membership** — check if country is a Smart Africa member (37+ countries); if yes, look for national blueprint at `smartafrica.org/knowledge/`
5. **UNECA strategy repository** — search `uneca.org` for country name + "digital transformation strategy" for any co-developed national strategy
6. **DIAL/ADLI snapshots** — check `dial.global/work/adli/` for country-specific DPI stack assessment (currently covers Uganda, Tanzania, Nigeria, Sierra Leone, Zambia, Eswatini, The Gambia)
7. **ID4Africa** — check `id4africa.com` for country case studies and AGM proceedings

### Step 4: Query APIs

Start with **World Bank** (no auth, broadest coverage, fastest), then layer in specialized sources.
See `references/api-guide.md` for ready-to-use query templates for every source.

### Step 5: Synthesize into a Country Brief

1. **Executive summary** — 3–5 key takeaways for the project
2. **Education system snapshot** — enrollment, quality, equity, spending
3. **School connectivity** — % connected, connectivity types, speed benchmarks, unconnected gap (Giga Maps)
4. **Digital readiness** — national connectivity, affordability, device access, infrastructure
5. **Digital identity & civil registration** — ID ownership, birth registration, system type, interoperability (especially Africa)
6. **Digital government maturity & cross-agency systems** — GTMI scores, EGDI, national strategy status, interoperability
7. **Governance & institutional capacity** — WGI scores, TI CPI, OGP status
8. **Socioeconomic context** — HDI, income, inequality, demographics
9. **Labor market & workforce** — employment, youth unemployment, skills levels
10. **Economic environment** — GDP, fiscal space, competitiveness
11. **Key gaps and opportunities** — intervention priorities the data reveals
12. **Data sources and caveats** — recency, missing data, coverage limitations

Always note the **year of each data point** and flag indicators older than 3 years.

---

## Important Notes

- **Country codes**: ISO alpha-2 (`EE`, `GH`) for World Bank/Eurostat; alpha-3 (`EST`, `GHA`) for UNESCO UIS/OECD; M49 numeric for UN SDG API
- **Data gaps**: Low-income countries often have delayed or missing data — note explicitly and suggest proxies
- **Recency**: WB data lags 1–2 years; ITU up to 3 years; UN e-Gov survey every 2 years (even years); ID4D every 3 years (aligns with Global Findex)
- **OECD sources**: PISA, Digital Gov Index available for OECD members + selected partners only
- **UNESCO UIS**: Free API key required — register at `http://api.uis.unesco.org/`
- **TI / Ookla / A4AI**: No streaming API — use annual dataset downloads
- **Giga Maps API**: Free API key at `https://uni.cf/gigamaps-api`; covers 2.1M+ schools in 140 countries
- **Giga meaningful connectivity standard**: ≥10 Mbps dedicated download per school (target 20 Mbps)
- **African ID systems**: ~85% of African countries have national ID systems backed by electronic databases; coverage and interoperability vary sharply — always check ID4D + UNECA landscape for country-specific status rather than assuming
- **Smart Africa SADX**: Cross-border data exchange platform in active pilot (Ghana, Benin, Rwanda as of 2025); check current status before citing

---

## Reference Files

- `references/api-guide.md` — Detailed API query patterns, indicator codes, and Python snippets for all sources
- `references/source-selection.md` — Quick reference for source selection by country type, data need, and project phase
