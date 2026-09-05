# API Query Guide — Country Context Data

## Table of Contents
1. [World Bank API](#1-world-bank-api)
2. [UNESCO UIS API](#2-unesco-uis-api)
3. [UN SDG API](#3-un-sdg-api)
4. [ITU DataHub](#4-itu-datahub)
5. [Eurostat API](#5-eurostat-api)
6. [OECD API](#6-oecd-api)
7. [UNICEF Data](#7-unicef-data)
8. [UNDP Human Development Reports](#8-undp-human-development-reports)
9. [ILO ILOSTAT](#9-ilo-ilostat)
10. [IMF World Economic Outlook](#10-imf-world-economic-outlook)
11. [UN e-Government Survey (UNDESA)](#11-un-e-government-survey-undesa)
12. [World Bank GovTech Maturity Index (GTMI)](#12-world-bank-govtech-maturity-index-gtmi)
13. [World Bank ID4D Dataset](#13-world-bank-id4d-dataset)
14. [EU DESI](#14-eu-desi)
15. [Transparency International CPI](#15-transparency-international-cpi)
16. [Open Government Partnership](#16-open-government-partnership)
17. [Ookla Speedtest Global Index](#17-ookla-speedtest-global-index)
18. [A4AI Internet Affordability](#18-a4ai-internet-affordability)
19. [IEA (TIMSS / PIRLS)](#19-iea-timss--pirls)
20. [Giga / Project Connect (UNICEF–ITU)](#20-giga--project-connect-unicef-itu)
21. [African Digital Government & Identity Sources](#21-african-digital-government--identity-sources)
22. [Key Indicator Codes Reference](#22-key-indicator-codes-reference)
23. [Quick Start: Recommended Query Sequence](#23-quick-start-recommended-query-sequence)

---

## 1. World Bank API

**Base URL**: `https://api.worldbank.org/v2/`
**Auth**: None | **Format**: JSON | **Coverage**: 200+ countries, 16,000+ indicators

### Basic Query Pattern
```
GET https://api.worldbank.org/v2/country/{COUNTRY_CODE}/indicator/{INDICATOR_CODE}?format=json&mrv={N}
```

### Useful Parameters
| Parameter | Description | Example |
|---|---|---|
| `format` | Response format | `json` |
| `date` | Year or range | `2020`, `2015:2023` |
| `mrv` | Most recent N values | `mrv=5` |
| `per_page` | Results per page | `per_page=100` |

### Example Queries
```
# GDP per capita (most recent)
https://api.worldbank.org/v2/country/GH/indicator/NY.GDP.PCAP.CD?format=json&mrv=1

# School enrollment, primary (last 5 years)
https://api.worldbank.org/v2/country/GH/indicator/SE.PRM.ENRR?format=json&mrv=5

# Internet users % of population
https://api.worldbank.org/v2/country/GH/indicator/IT.NET.USER.ZS?format=json&mrv=3

# Government effectiveness (WGI)
https://api.worldbank.org/v2/country/GH/indicator/GE.EST?format=json&mrv=3

# Multiple countries at once
https://api.worldbank.org/v2/country/GH;KE;RW/indicator/IT.NET.USER.ZS?format=json&mrv=1
```

### Python Snippet
```python
import requests

def get_wb_indicator(country_code, indicator, years=3):
    url = f"https://api.worldbank.org/v2/country/{country_code}/indicator/{indicator}"
    params = {"format": "json", "mrv": years}
    data = requests.get(url, params=params).json()
    # data[0] = metadata, data[1] = results
    return [{"year": r["date"], "value": r["value"]} for r in data[1] if r["value"]]

def get_wb_batch(country_code, indicators: list, years=3):
    return {ind: get_wb_indicator(country_code, ind, years) for ind in indicators}
```

---

## 2. UNESCO UIS API

**Base URL**: `http://api.uis.unesco.org/api/public/`
**Auth**: Free API key — register at https://apiportal.uis.unesco.org
**Format**: JSON | **Coverage**: Education, literacy, science — 200+ countries

### Basic Query Pattern
```
GET http://api.uis.unesco.org/api/public/data/indicators?indicator={CODE}&country={ISO3}&start={YEAR}&end={YEAR}
Authorization: Bearer {YOUR_API_KEY}
```

### Key Endpoints
| Endpoint | Description |
|---|---|
| `/data/indicators` | Fetch indicator data |
| `/structure/indicators` | List all available indicators |
| `/structure/countries` | List supported countries |

### Example Query (Literacy Rate, Ghana)
```
GET http://api.uis.unesco.org/api/public/data/indicators?indicator=LR.AG15T99&country=GHA&start=2018&end=2023
```

### Python Snippet
```python
def get_uis_indicator(country_iso3, indicator_code, api_key):
    url = "http://api.uis.unesco.org/api/public/data/indicators"
    headers = {"Authorization": f"Bearer {api_key}"}
    params = {"indicator": indicator_code, "country": country_iso3}
    return requests.get(url, headers=headers, params=params).json()
```

---

## 3. UN SDG API

**Base URL**: `https://unstats.un.org/SDGAPI/v1/`
**Auth**: None | **Format**: JSON | **Coverage**: All UN member states

### Key Endpoints
| Endpoint | Description |
|---|---|
| `/sdg/Goal/List` | List all SDG goals |
| `/sdg/Target/List?goal=4` | SDG 4 targets |
| `/sdg/Indicator/List?target=4.1` | Indicators for target 4.1 |
| `/sdg/DataV2/PivotData` | Fetch data |
| `/sdg/GeoArea/List` | Country codes (M49) |

### Example Queries
```
# SDG 4.1.1 — minimum proficiency reading/math, Ghana
https://unstats.un.org/SDGAPI/v1/sdg/DataV2/PivotData?indicator=4.1.1&areaCode=GHA&timePeriodStart=2015

# SDG 16.9.1 — birth registration rate (links to ID coverage)
https://unstats.un.org/SDGAPI/v1/sdg/DataV2/PivotData?indicator=16.9.1&areaCode=GHA

# SDG 9.c.1 — mobile-broadband subscriptions
https://unstats.un.org/SDGAPI/v1/sdg/DataV2/PivotData?indicator=9.c.1&areaCode=GHA
```

> **Note**: SDG 16.9.1 (birth registration rate) is a key proxy for ID system reach in African countries.

---

## 4. ITU DataHub

**Base URL**: `https://datahub.itu.int/`
**Auth**: None for downloads; registration for API
**Format**: CSV/Excel (bulk), JSON (API)

### Key Indicators
| Code | Description |
|---|---|
| `ICT_IU` | Individuals using the Internet (%) |
| `ICT_MOBB` | Mobile-broadband subscriptions per 100 |
| `ICT_FIBB` | Fixed-broadband subscriptions per 100 |
| `ICT_IDI` | ICT Development Index (composite) |
| `ICT_HHIB` | Households with broadband internet |

### Example Queries
```
# Bulk download (no auth)
https://datahub.itu.int/data/?e=ICT_IU&c=GHA&s=&default=true

# API (registration required)
GET https://datahub.itu.int/api/data/?indicator=ICT_IU&country=GHA&format=json
Authorization: Token {YOUR_TOKEN}
```

> **Tip**: World Bank mirrors ITU data — `IT.NET.USER.ZS` requires no auth and is usually sufficient.

---

## 5. Eurostat API

**Base URL**: `https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/`
**Auth**: None | **Format**: JSON-stat | **Coverage**: EU-27 + candidates

### Query Pattern
```
GET https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/{DATASET}?geo={COUNTRY}&time={YEAR}&format=JSON
```

### Key Datasets
| Code | Description |
|---|---|
| `educ_uoe_enrt01` | Enrollment by education level |
| `isoc_ci_in_h` | Internet access in households |
| `isoc_r_broad_h` | Broadband access in households |
| `edat_lfse_14` | Early school leavers |
| `isoc_sk_dskl_i21` | Digital skills indicators |
| `gov_10a_exp` | Government expenditure by function |

---

## 6. OECD API

**Base URL**: `https://stats.oecd.org/SDMX-JSON/data/`
**Auth**: None | **Format**: SDMX-JSON | **Coverage**: OECD members + partner countries

### Query Pattern
```
GET https://stats.oecd.org/SDMX-JSON/data/{DATASET}/{FILTER}/all?startTime={YEAR}&endTime={YEAR}
```

### Key Datasets
| Code | Description |
|---|---|
| `EAG_EXP` | Education at a Glance — expenditure |
| `EAG_TEACH_RATIO` | Pupil-teacher ratios |
| `PISA` | PISA learning outcomes |
| `DGI` | Digital Government Index |

> **Note**: PISA data released every 3 years (2018, 2022, 2025). OECD sources are limited to members + partners — for most African countries use UNESCO UIS instead.

---

## 7. UNICEF Data

**Base URL**: `https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/data/`
**Auth**: None | **Format**: JSON/CSV | **Coverage**: Global, children-focused

### Example Queries
```
# Out-of-school rate, primary, Ghana
GET https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/data/UNICEF,EDUCATION,1.0/GHA..OOSC_RATE_PRIMARY....?format=jsondata

# MICS surveys by country
GET https://mics.unicef.org/api/surveys?country=GH
```

---

## 8. UNDP Human Development Reports

**Base URL**: `https://hdrdata.org/api/`
**Auth**: None | **Format**: JSON

### Key Indicators
| Code | Description |
|---|---|
| `hdi` | Human Development Index |
| `gii` | Gender Inequality Index |
| `mpi_n` | Multidimensional Poverty Index |
| `eys` | Expected years of schooling |
| `mys` | Mean years of schooling |
| `ineq_edu` | Inequality in education |

### Example Query
```
https://hdrdata.org/api/composite/indicators/hdi?country=GHA&year=2022
```

---

## 9. ILO ILOSTAT

**Base URL**: `https://sdmx.ilo.org/rest/data/`
**Auth**: None | **Format**: SDMX-JSON | **Coverage**: 200+ countries

### Example Queries
```
# Youth unemployment rate, Ghana
GET https://sdmx.ilo.org/rest/data/ILO,DF_YI_ALL_EAP_DWAP_SEX_AGE_RT/GHA...YA?format=jsondata&startPeriod=2018&endPeriod=2023
```

### Alternative: World Bank mirrors ILO data
```
# Youth unemployment (World Bank, no auth needed)
https://api.worldbank.org/v2/country/GH/indicator/SL.UEM.1524.ZS?format=json&mrv=5
```

---

## 10. IMF World Economic Outlook

**Base URL**: `https://www.imf.org/external/datamapper/api/v1/`
**Auth**: None | **Format**: JSON | **Coverage**: 190+ countries

### Query Pattern
```
GET https://www.imf.org/external/datamapper/api/v1/{INDICATOR}/{COUNTRY_ISO3}
```

### Key Indicators
| Code | Description |
|---|---|
| `NGDPDPC` | GDP per capita (current USD) |
| `NGDP_RPCH` | Real GDP growth rate (%) |
| `GGX_NGDP` | General gov. expenditure (% GDP) |
| `GGXWDG_NGDP` | Gross gov. debt (% GDP) |
| `PCPIPCH` | Inflation rate (%) |

### Example Query
```
https://www.imf.org/external/datamapper/api/v1/NGDP_RPCH/GHA
```

---

## 11. UN e-Government Survey (UNDESA)

**Access**: Dataset download (no streaming API)
**URL**: `https://publicadministration.un.org/egovkb/en-us/Data-Center`
**Auth**: None | **Format**: Excel/CSV | **Frequency**: Biennial (even years, most recent: 2024)

### Key Indices
| Index | Description |
|---|---|
| EGDI | e-Government Development Index (composite) |
| OSI | Online Services Index |
| TII | Telecommunication Infrastructure Index |
| HCI | Human Capital Index (within EGDI) |
| EPI | e-Participation Index |

### Access Steps
1. Go to `https://publicadministration.un.org/egovkb/en-us/Data-Center`
2. Select "Data by Country" or "Time Series"
3. Download as Excel/CSV — no API key required

### Python Snippet (after download)
```python
import pandas as pd

df = pd.read_excel("UN_eGov_2024.xlsx", sheet_name="EGDI")
country_data = df[df["Country ISO3"] == "GHA"]
egdi_score = country_data["EGDI Score"].values[0]
osi_score = country_data["OSI Score"].values[0]
```

---

## 12. World Bank GovTech Maturity Index (GTMI)

**Access**: World Bank DataBank and Open Data Portal
**URL**: `https://www.worldbank.org/en/programs/govtech`
**DataBank**: `https://databank.worldbank.org/source/govtech-maturity-index`
**Auth**: None | **Format**: JSON (via WB API) / Excel download | **Coverage**: 198 countries | **Frequency**: Biennial

### What It Measures
The GTMI assesses digital government maturity across four pillars:

| Pillar | What It Covers |
|---|---|
| CGSS — Core Government Systems | Shared platforms, civil service systems, financial management, interoperability |
| PSDS — Public Service Delivery Systems | Digital services for citizens and businesses, online portals |
| CTES — Citizen and Technology Engagement | Open data, citizen feedback, digital literacy programs |
| GTES — GovTech Enabling Systems | Legal/regulatory frameworks, digital identity, cybersecurity |

> **Key for cross-agency systems**: The CGSS pillar directly measures whether a country has shared back-office platforms, interoperability layers, and integrated government data systems.

### Why Use for African Countries
- Covers 198 countries including all African nations
- Directly answers questions about cross-agency integration that EGDI's composite score obscures
- Updated every 2 years; 2022 edition available; 2024 forthcoming

### Querying via World Bank API
```
# GovTech Maturity Index — overall score
https://api.worldbank.org/v2/country/GH/indicator/GT.GOV.MTRC.XQ?format=json&mrv=1

# Core Government Systems score (cross-agency pillar)
https://api.worldbank.org/v2/country/GH/indicator/GT.GOV.CGSS.XQ?format=json&mrv=1

# Public Service Delivery score
https://api.worldbank.org/v2/country/GH/indicator/GT.GOV.PSDS.XQ?format=json&mrv=1

# GovTech Enabling Systems (includes digital ID, legal frameworks)
https://api.worldbank.org/v2/country/GH/indicator/GT.GOV.GTES.XQ?format=json&mrv=1
```

### GTMI Score Bands
| Band | Score Range | Description |
|---|---|---|
| A | 0.75–1.00 | Transforming |
| B | 0.50–0.74 | Scaling |
| C | 0.25–0.49 | Emerging |
| D | 0.00–0.24 | Incipient |

### Python Snippet
```python
GTMI_INDICATORS = {
    "overall": "GT.GOV.MTRC.XQ",
    "core_systems": "GT.GOV.CGSS.XQ",
    "service_delivery": "GT.GOV.PSDS.XQ",
    "citizen_engagement": "GT.GOV.CTES.XQ",
    "enabling_systems": "GT.GOV.GTES.XQ",
}

def get_gtmi_profile(country_code):
    results = {}
    for pillar, indicator in GTMI_INDICATORS.items():
        data = get_wb_indicator(country_code, indicator, years=1)
        results[pillar] = data[0]["value"] if data else None
    return results
```

---

## 13. World Bank ID4D Dataset

**Access**: World Bank DataBank and Data360
**DataBank URL**: `https://databank.worldbank.org/source/identification-for-development-(id4d)-data`
**Data360 URL**: `https://data360.worldbank.org/en/dataset/WB_ID4D`
**Auth**: None | **Coverage**: 190+ countries | **Frequency**: Every 3 years (aligns with Global Findex)

### What It Measures
ID coverage gaps and digital ID system capabilities:

| Indicator Type | Examples |
|---|---|
| Demand-side (coverage) | % adults with official ID, % children with birth registration |
| Digital ID availability | Whether government-recognized digital ID exists for online transactions |
| System characteristics | Biometric use, remote authentication capability, interoperability |

### Key Data Points for African Context
- **~800 million people globally lack official ID** — majority in sub-Saharan Africa and South Asia
- **Sub-Saharan Africa accounts for 50%+ of the global unidentified population**
- **~95 million African children under 5 have never had births recorded**

### Querying via World Bank API
```
# Adult ID ownership rate (% with official ID)
https://api.worldbank.org/v2/country/GH/indicator/ID.01.1?format=json&mrv=1

# Birth registration rate (% under 5 registered)
https://api.worldbank.org/v2/country/GH/indicator/SP.REG.BRTH.ZS?format=json&mrv=3

# Also available on DataBank — search "ID4D" for full indicator list
```

> **Note**: For detailed country-level ID system characteristics (technology type, legal framework, interoperability architecture), use the qualitative country diagnostic reports — see section 21 (African Sources) below.

### Country Diagnostic Reports
Published for 30+ countries including: Botswana, Burkina Faso, Côte d'Ivoire, Ethiopia, Guinea, Kenya, Liberia, Madagascar, Morocco, Namibia, Nigeria, Rwanda, Sierra Leone, Somalia, Uganda, Zambia.
```
https://id4d.worldbank.org/country-action/id4d-diagnostics
```

---

## 14. EU DESI

**URL**: `https://digital-agenda-data.eu/`
**Auth**: None | **Coverage**: EU-27 member states | **Format**: Excel/CSV + Eurostat API components

### DESI Dimensions
| Dimension | Sub-indices |
|---|---|
| 1. Connectivity | Fixed broadband, mobile broadband, fast broadband |
| 2. Human Capital | Internet use, basic/advanced digital skills |
| 3. Use of Internet Services | Content, transactions, e-government |
| 4. Integration of Digital Tech | Business digitisation, e-commerce, AI |
| 5. Digital Public Services | e-Government, open data, health services |

### Eurostat DESI components via API
```
# Digital skills
https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/isoc_sk_dskl_i21?geo=EE&format=JSON

# e-Government usage
https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/isoc_ci_ac_i?geo=EE&format=JSON
```

---

## 15. Transparency International CPI

**URL**: `https://www.transparency.org/en/cpi`
**Auth**: None | **Format**: Excel/CSV download | **Frequency**: Annual (January)

### Key Fields
| Field | Description |
|---|---|
| `CPI Score` | 0 (highly corrupt) to 100 (very clean) |
| `Rank` | Global rank out of ~180 countries |
| `Standard Error` | Confidence interval |

### Python Snippet (after download)
```python
import pandas as pd

df = pd.read_excel("CPI2023.xlsx", sheet_name="CPI Timeseries 2012-2023", header=2)
country_row = df[df["ISO3"] == "GHA"]
cpi_score = country_row["CPI score 2023"].values[0]
```

---

## 16. Open Government Partnership

**URL**: `https://www.opengovpartnership.org/data/`
**Auth**: None | **Format**: JSON

### Access
```
# Members list
https://www.opengovpartnership.org/wp-json/ogp/v1/members

# Country commitments
https://www.opengovpartnership.org/wp-json/ogp/v1/countries/{country-slug}/action-plans
```

---

## 17. Ookla Speedtest Global Index

**URL**: `https://www.speedtest.net/global-index`
**Auth**: None for country-level | **Format**: CSV download | **Frequency**: Monthly

### Download
```
# Ookla Open Datasets (GitHub, quarterly tiles)
https://github.com/teamookla/ookla-open-data
```

---

## 18. A4AI Internet Affordability

**URL**: `https://a4ai.org/extra/mobile-broadband-pricing-gni/`
**Auth**: None | **Format**: CSV/Excel download | **Frequency**: Annual

### Key Metric
Cost of cheapest 1GB prepaid mobile broadband plan as % of monthly GNI per capita.
- Target: ≤2% (ITU/A4AI affordability threshold)
- Especially important for lower-income African countries

---

## 19. IEA (TIMSS / PIRLS)

**URL**: `https://www.iea.nl/data-tools/repository`
**Auth**: None | **Format**: SPSS/SAS/R datasets | **Frequency**: Every 4–5 years

### Assessments
| Assessment | Subject | Grade | Coverage |
|---|---|---|---|
| TIMSS | Math & Science | Grades 4 & 8 | Broader than PISA — many African countries participate |
| PIRLS | Reading literacy | Grade 4 | Includes South Africa, Morocco, Egypt, others |

### Access
```
https://timssandpirls.bc.edu/databases-landing.html
```

---

## 20. Giga / Project Connect (UNICEF–ITU)

**Overview**: Joint UNICEF/ITU initiative mapping school connectivity globally.
**Coverage**: 2.1M+ schools in 140+ countries | All tools open-source: `https://github.com/unicef/`

---

### 20a. Giga Maps API

**Base URL**: `https://api.gigamaps.org/`
**Auth**: Free API key — register at `https://uni.cf/gigamaps-api`
**Format**: JSON

#### Key Endpoints
| Endpoint | Description |
|---|---|
| `/api/schools/` | List schools with connectivity status, coordinates, country |
| `/api/countries/{iso3}/schools/` | All schools in a country |
| `/api/countries/{iso3}/statistics/` | Country-level connectivity statistics |

#### Key Data Fields
| Field | Description |
|---|---|
| `connectivity` | Boolean — connected or not |
| `connectivity_type` | `fiber`, `cellular`, `p2p`, `satellite`, `none` |
| `connectivity_speed` | Measured download speed (Mbps) |
| `coverage_type` | `2G`, `3G`, `4G`, `5G`, `no signal` |

#### Example Queries
```
# Country statistics
GET https://api.gigamaps.org/api/countries/GHA/statistics/
Authorization: Token {YOUR_API_KEY}

# Unconnected schools
GET https://api.gigamaps.org/api/schools/?country_iso3=GHA&connectivity=false&format=json
Authorization: Token {YOUR_API_KEY}
```

#### Python Snippet
```python
GIGA_HEADERS = {"Authorization": f"Token {GIGA_API_KEY}"}
BASE = "https://api.gigamaps.org/api"

def get_country_school_stats(iso3):
    return requests.get(f"{BASE}/countries/{iso3}/statistics/", headers=GIGA_HEADERS).json()

def get_unconnected_schools(iso3, page_size=100):
    params = {"country_iso3": iso3, "connectivity": "false", "page_size": page_size}
    return requests.get(f"{BASE}/schools/", headers=GIGA_HEADERS, params=params).json()
```

---

### 20b. Giga Daily Check App

**Dashboard**: `https://dailycheckapp.gigamaps.org/`
**Purpose**: Real-time school bandwidth and latency monitoring

#### Giga Meaningful Connectivity Benchmarks
| Threshold | Value |
|---|---|
| Minimum acceptable | 10 Mbps dedicated download |
| Target | 20 Mbps dedicated download |
| Wi-Fi coverage | 100m omni-directional, 200+ concurrent users |
| Frequency | Dual-band: 2.4GHz and 5GHz |

---

### 20c. Giga AI School Mapping

**GitHub**: `https://github.com/unicef/giga-global-school-mapping`
**Performance**: AUPRC > 0.96 across 10 pilot African countries
Use to identify unregistered schools not in official government registries.

---

### 20d. Giga Financing & Infrastructure Models

| Model | Description |
|---|---|
| Connectivity Credits | Schools earn credits by connection difficulty; backed by government subsidies |
| Infrastructure Exchange | ISPs connect schools free in exchange for backhaul access |
| Anchor Customer / Pooling | Aggregates budgets across government departments |
| Technology Cost Models | Fiber vs. cellular vs. P2P vs. VSAT cost comparisons |

**Reference**: `https://giga.global/connecting-schools/`

---

## 21. African Digital Government & Identity Sources

These sources are qualitative and document-based rather than API-queryable, but are essential for assessing cross-agency systems, identity programmes, and digital government strategies in African countries. Always check these after running quantitative API queries for African contexts.

---

### 21a. World Bank ID4D Country Diagnostics

**URL**: `https://id4d.worldbank.org/country-action/id4d-diagnostics`
**Auth**: None | **Format**: PDF reports | **Coverage**: 30+ African countries

#### What It Provides (per country)
- Assessment of ID system architecture (foundational vs. functional)
- Biometric technology used and enrollment status
- Legal and regulatory framework for ID
- Cross-agency use of the ID system (health, education, social protection, finance)
- Interoperability gaps and recommendations

#### Available African Country Reports
Botswana, Burkina Faso, Côte d'Ivoire, Ethiopia, Guinea, Kenya, Liberia, Madagascar, Morocco, Namibia, Nigeria, Rwanda, Sierra Leone, Somalia, Uganda, Zambia (and others).

#### Synthesis Report
"The State of Identification Systems in Africa" (2017) — summarizes 17 country assessments:
```
http://documents.worldbank.org/curated/en/156111493234231522/
```

---

### 21b. UNECA Africa Digital Identity Landscape (2023)

**URL**: `https://www.uneca.org/sites/default/files/DITE-AFRICA/Africa%20Digtial%20ID%20Landscape%20Report%20(2023).pdf`
**Auth**: None | **Format**: PDF | **Coverage**: 54 African countries

#### What It Covers
- Country-by-country survey of national ID system status
- Local, national, and regional identity system architectures
- Cross-border ID interoperability initiatives (ECOWAS ENBIC, AU framework)
- Legal and data protection framework maturity
- Key finding: ~85% of African countries have national ID systems backed by electronic databases; 70%+ collect biometrics

#### Key Stats for Context
- ~542 million Africans lack identity cards
- ~95 million children under 5 have never had births recorded
- Countries implementing digital ID could unlock 3–13% of GDP by 2030 (UNECA estimate)

---

### 21c. ID4Africa Movement

**URL**: `https://id4africa.com/`
**Auth**: None | **Coverage**: 48 African member countries

#### What It Provides
- Annual General Meeting proceedings with country case studies
- National ID authority contacts and programme updates
- Policy briefs on specific identity topics (displaced persons, women, rural populations)
- Real-world implementation assessments beyond what quantitative data shows

#### Search for Country Information
```
# Country-specific sessions and case studies from AGM proceedings
https://id4africa.com/events/

# Knowledge library
https://id4africa.com/knowledge/
```

---

### 21d. Smart Africa Alliance

**URL**: `https://smartafrica.org/knowledge/`
**Auth**: None | **Coverage**: 37+ African member states

#### What It Provides
- **National Digital Economy Blueprints** — country-specific digital transformation roadmaps
- **Digital Identity Blueprint** — governance and technical framework for interoperable ID across member states
- **Data Governance Blueprint** — national data strategy design guidance
- **Smart Africa Data Exchange (SADX)** — cross-border data sharing platform (pilot: Ghana, Benin, Rwanda as of 2025)

#### Key Documents to Check
```
# Digital Identity Blueprint
https://smartafrica.org/knowledge/digital-id/

# Data Governance Blueprint
https://smartafrica.org/knowledge/data-governance/

# Country blueprints index
https://smartafrica.org/knowledge/
```

#### SADX Status
The Smart Africa Data Exchange enables secure cross-border government data sharing. Check readiness by country:
- Ghana: readiness validated (April 2025)
- Benin: readiness validated
- Rwanda: next in queue
- Wider rollout: post-pilot 2025–2026

---

### 21e. UNECA Digital Strategy Repository

**URL**: `https://www.uneca.org/` (search by country + "digital transformation strategy")
**Auth**: None | **Coverage**: African countries where UNECA co-developed the strategy

#### What It Provides
Published national digital transformation strategies co-developed with UNECA, including:
- The Gambia Digital Transformation Strategy + Digital ID Strategy (2023)
- Tanzania Digital Economy Strategic Framework 2024–2034
- Country-specific strategies for Rwanda, Kenya, Ethiopia, and others

#### How to Find Country Strategies
1. Search `site:uneca.org "[country name] digital transformation strategy"`
2. Or browse: `https://www.uneca.org/publications` filtered by country
3. Also check national ICT ministry websites — UNECA strategies are often published there

---

### 21f. DIAL / Africa Data Leadership Initiative (ADLI)

**URL**: `https://dial.global/work/adli/`
**Auth**: None | **Format**: Web articles, reports | **Frequency**: Annual cohorts

#### What It Provides
Country snapshots on **Digital Public Infrastructure (DPI)** readiness — the "stack" of:
- Foundational digital ID system
- Digital payments infrastructure
- Cross-government data exchange systems

#### Countries Covered (as of 2025)
Uganda, Sierra Leone, The Gambia, Zambia, Tanzania, Nigeria, Eswatini (2024–2025 cohorts)

#### Key Insight Format
Each country snapshot covers: what interoperable systems exist, what's missing, policy blockers, and what peer countries can learn. Example — Tanzania's Jamii suite:
- Jamii Namba (digital ID)
- Jamii Malipo (digital payments)
- Jamii X-Change (cross-agency data exchange)

---

### 21g. AU Digital Transformation Strategy 2020–2030 (Reference Document)

**URL**: `https://au.int/sites/default/files/documents/38507-doc-dts-english.pdf`
**Auth**: None | **Format**: PDF

#### How to Use
Use as a checklist when assessing a country's national strategy:
- Does the country's strategy align with AU DTS pillars (infrastructure, policy, digital skills, innovation, digital finance, e-government)?
- Is the country implementing the AU Interoperability Framework for Digital ID?
- Is the country participating in the African Continental Free Trade Area (AfCFTA) digital single market initiative?

#### AU Interoperability Framework for Digital ID
```
https://au.int/en/documents/20231211/au-interoperability-framework-digital-id
```
Endorsed by AU Executive Council in 2022 — defines minimum technical standards and governance mechanisms for cross-border and cross-agency ID interoperability. Check whether target country's systems are aligned.

---

## 22. Key Indicator Codes Reference

### World Bank — Education
| Code | Description |
|---|---|
| `SE.PRM.ENRR` | School enrollment, primary (% gross) |
| `SE.SEC.ENRR` | School enrollment, secondary (% gross) |
| `SE.TER.ENRR` | School enrollment, tertiary (% gross) |
| `SE.PRM.CMPT.ZS` | Primary completion rate |
| `SE.PRM.PRSL.ZS` | Pupil-teacher ratio, primary |
| `SE.XPD.TOTL.GD.ZS` | Gov. expenditure on education (% GDP) |
| `SE.ADT.LITR.ZS` | Literacy rate, adult total |
| `SE.ADT.1524.LT.ZS` | Literacy rate, youth (15–24) |

### World Bank — ICT
| Code | Description |
|---|---|
| `IT.NET.USER.ZS` | Individuals using the Internet (%) |
| `IT.CEL.SETS.P2` | Mobile cellular subscriptions per 100 |
| `IT.NET.BBND.P2` | Fixed broadband subscriptions per 100 |

### World Bank — Governance (WGI)
| Code | Description |
|---|---|
| `GE.EST` | Government effectiveness |
| `RL.EST` | Rule of law |
| `CC.EST` | Control of corruption |
| `RQ.EST` | Regulatory quality |
| `PV.EST` | Political stability |
| `VA.EST` | Voice and accountability |

### World Bank — GovTech Maturity Index (GTMI)
| Code | Description |
|---|---|
| `GT.GOV.MTRC.XQ` | GTMI overall score |
| `GT.GOV.CGSS.XQ` | Core Government Systems (cross-agency) |
| `GT.GOV.PSDS.XQ` | Public Service Delivery Systems |
| `GT.GOV.CTES.XQ` | Citizen & Technology Engagement |
| `GT.GOV.GTES.XQ` | GovTech Enabling Systems (ID, cybersecurity) |

### World Bank — Digital Identity (ID4D)
| Code | Description |
|---|---|
| `ID.01.1` | Adults with official ID (%) |
| `SP.REG.BRTH.ZS` | Birth registration rate (% under 5) |

### World Bank — Socioeconomic
| Code | Description |
|---|---|
| `NY.GDP.PCAP.CD` | GDP per capita (current USD) |
| `SI.POV.GINI` | Gini index |
| `SP.POP.TOTL` | Population, total |
| `SP.URB.TOTL.IN.ZS` | Urban population (%) |
| `SI.POV.DDAY` | Poverty headcount at $2.15/day |
| `HD.HCI.OVRL` | Human Capital Index |
| `SL.UEM.1524.ZS` | Youth unemployment rate |

### World Bank — Business Environment
| Code | Description |
|---|---|
| `IC.BUS.EASE.XQ` | Ease of doing business score |
| `GB.XPD.RSDV.GD.ZS` | R&D expenditure (% of GDP) |

### UNESCO UIS
| Code | Description |
|---|---|
| `LR.AG15T99` | Literacy rate, adult (15+) |
| `LR.AG15T24` | Literacy rate, youth (15–24) |
| `XGDP.FST.FSGOV` | Gov. expenditure on education (% GDP) |
| `ROFST.H.PRIMAR` | Out-of-school rate, primary |
| `SCHBSP.1.G2T3.PART` | Schools with internet access |

### SDG Indicators (UN SDG API)
| SDG | Description |
|---|---|
| 4.1.1 | Minimum proficiency in reading/math |
| 4.4.1 | ICT skills (youth and adults) |
| 4.6.1 | Literacy and numeracy proficiency |
| 4.c.1 | Proportion of trained teachers |
| 9.c.1 | Mobile-broadband subscriptions |
| 16.6.1 | Gov. expenditure as % of approved budget |
| 16.9.1 | Birth registration rate (proxy for ID reach) |
| 16.10.2 | Countries with open data policies |

### IMF World Economic Outlook
| Code | Description |
|---|---|
| `NGDPDPC` | GDP per capita (current USD) |
| `NGDP_RPCH` | Real GDP growth (%) |
| `GGX_NGDP` | Gov. expenditure (% GDP) |
| `GGXWDG_NGDP` | Gross gov. debt (% GDP) |

### Giga / Project Connect
| Field | Description |
|---|---|
| `connectivity` | Boolean — school connected (true/false) |
| `connectivity_type` | fiber / cellular / p2p / satellite / none |
| `connectivity_speed` | Measured download speed (Mbps) |
| Country stat: `connectivity_rate` | % of mapped schools connected |

---

## 23. Quick Start: Recommended Query Sequence

### All Countries — Phase 1: Core Profile (no auth, <10 min)
1. **World Bank** — GDP, population, internet access, enrollment, literacy, WGI governance scores, GTMI
2. **IMF WEO** — GDP growth, public debt, government expenditure
3. **UN SDG API** — SDG 4, 9, 16 progress (including SDG 16.9.1 for birth registration)
4. **UNDP HDR API** — HDI, Gender Inequality Index, expected years of schooling

### All Countries — Phase 2: Digital & Education Depth (free keys)
5. **UNESCO UIS** — education-specific indicators, out-of-school rates, schools with internet
6. **World Bank ID4D DataBank** — adult ID ownership, birth registration, digital ID availability
7. **World Bank GTMI DataBank** — GovTech maturity score, core systems pillar, enabling systems pillar
8. **Giga Maps API** — school connectivity status, % connected, speed data
9. **UN e-Government Survey** — EGDI, OSI, EPI scores (download)
10. **ITU DataHub** — ICT Development Index

### All Countries — Phase 3: Governance & Strategy Context (downloads)
11. **Transparency International** — CPI score and rank
12. **OGP** — open government commitments
13. **ITU Digital Development Dashboard** — national ICT strategy existence and age

### African Countries — Additional Block (always run for sub-Saharan Africa)
14. **UNECA Africa Digital ID Landscape (2023)** — country ID system profile, legal framework, interoperability status
15. **Smart Africa membership check** — if member, retrieve national blueprint from `smartafrica.org/knowledge/`
16. **UNECA strategy search** — `site:uneca.org "[country] digital transformation strategy"` for co-developed strategies
17. **DIAL/ADLI** — check `dial.global/work/adli/` for DPI stack assessment if country is in cohort
18. **ID4Africa** — country case studies from AGM proceedings
19. **World Bank ID4D Diagnostics** — full country diagnostic report if published

### Phase 4: Connectivity & Education Quality Detail
20. **Ookla** — real-world internet speeds
21. **A4AI** — internet affordability (1GB cost as % GNI)
22. **ILO ILOSTAT** — youth unemployment, employment by sector
23. **IEA TIMSS/PIRLS** — learning outcome benchmarks (if country participates)

### Regional Enrichment (if applicable)
24. **Eurostat** (EU countries) — DESI, digital skills, detailed education data
25. **OECD** (OECD members) — Digital Government Index, PISA, Education at a Glance
