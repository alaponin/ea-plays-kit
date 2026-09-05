# A quick reference: how to select a source

## Select by the type of country

### A member state of the EU
**Priority order**: Eurostat → World Bank → DESI → OECD → UNESCO UIS → ILO → UNDP
- Eurostat gives the most detail for an EU country.
- DESI gives a full score for the digital economy.
- The OECD sources are available for an EU member that is also an OECD member. Most of them are.

### A member of the OECD that is not in the EU
**Priority order**: World Bank → OECD API → UNESCO UIS → ILO → UNDP → IMF
- OECD API unlocks PISA, Digital Government Index, Education at a Glance
- World Bank still best starting point (speed, breadth)

### A country in sub-Saharan Africa
**Priority order**: World Bank → UNESCO UIS → UN SDG → ID4D → GTMI → UNDP → ILO → UNICEF → IMF → ITU
- Always run the **African Additional Block** (see api-guide.md section 23)
- Expect data gaps — flag them; use UNICEF for equity/child indicators
- UNECA Africa Digital ID Landscape is the definitive source for ID system status
- Smart Africa and UNECA repositories are primary sources for strategy documents
- TIMSS/PIRLS more relevant than PISA for learning outcome benchmarks

### An upper-middle-income country that is not in the OECD and not in Africa
**Priority order**: World Bank → UNESCO UIS → UN SDG → ILO → UNDP → IMF → ITU
- World Bank has good coverage; TIMSS/PIRLS likely available

---

## Select by the data that you need

### The assessment of the digital readiness
| Priority | Source | Key Data |
|---|---|---|
| 1 | World Bank | IT.NET.USER.ZS, IT.NET.BBND.P2, IT.CEL.SETS.P2 |
| 2 | ITU DataHub | ICT Development Index (IDI), detailed breakdowns |
| 3 | World Bank GTMI | GovTech maturity, digital enabling environment |
| 4 | Giga Maps API | School connectivity status, % connected, speeds |
| 5 | UN e-Gov Survey | EGDI, Online Services Index, TII |
| 6 | Ookla | Real-world speeds vs. subscription numbers |
| 7 | A4AI | Affordability — 1GB cost as % GNI |
| 8 | DESI (EU only) | Connectivity, digital skills, internet use sub-indices |
| 9 | UNESCO UIS | Schools with internet access (aggregate %) |

### The baseline of the education system
| Priority | Source | Key Data |
|---|---|---|
| 1 | World Bank | SE.* enrollment, completion, pupil-teacher, expenditure |
| 2 | UNESCO UIS | Out-of-school rates, literacy, schools with internet |
| 3 | Giga Maps API | School-level connectivity, unconnected count, speed data |
| 4 | UN SDG API | SDG 4 indicators (4.1.1, 4.4.1, 4.6.1, 4.c.1) |
| 5 | UNICEF | Child equity, gender parity, out-of-school |
| 6 | IEA TIMSS/PIRLS | Learning outcome benchmarks (broader African coverage than PISA) |
| 7 | UNDP HDR | Expected/mean years of schooling, education inequality |

### The connectivity of the schools, for the digital transformation of education
| Priority | Source | Key Data |
|---|---|---|
| 1 | Giga Maps API | % schools connected, connectivity type breakdown, locations |
| 2 | Giga Daily Check App | Real-time speeds vs. contracted SLA |
| 3 | UNESCO UIS `SCHBSP` | Aggregate % schools with internet (cross-check) |
| 4 | Giga Cost Models | Technology options (fiber/cellular/satellite), cost per school |
| 5 | ITU DataHub | National ICT infrastructure context |
| 6 | A4AI | Connectivity affordability for sustainability |

**The Giga benchmarks**: a minimum of 10 Mbps of dedicated download, and a target of 20 Mbps. The Wi-Fi covers 100 m and more than 200 users.

### The digital identity and the civil registration
| Priority | Source | Key Data |
|---|---|---|
| 1 | World Bank ID4D DataBank | Adult ID ownership %, birth registration rate, digital ID availability |
| 2 | UN SDG 16.9.1 | Birth registration rate (SDG proxy for ID reach) |
| 3 | UNICEF | Birth registration rate, child identity coverage |
| 4 | UNECA Africa Digital ID Landscape (Africa) | Country ID system type, legal framework, interoperability |
| 5 | ID4Africa (Africa) | Country case studies, implementation maturity |
| 6 | World Bank ID4D Diagnostics | Full country diagnostic (30+ African countries) |
| 7 | AU Interoperability Framework | Whether country's system meets continental standards |

### The maturity of the digital government, and the systems that cross the agencies
| Priority | Source | Key Data |
|---|---|---|
| 1 | World Bank GTMI | Core systems score (cross-agency), service delivery, enabling systems |
| 2 | UN e-Gov Survey | EGDI, OSI, EPI scores |
| 3 | OECD DGI (OECD only) | Digital Government Index |
| 4 | DESI Dim 5 (EU only) | Digital public services sub-index |
| 5 | OGP | Open data commitments, action plan status |
| 6 | UN SDG 16.10.2 | Countries with open data policies |

### The strategy documents of the national digital government
| Priority | Source | What to Find |
|---|---|---|
| 1 | UNECA Repository (Africa) | Co-developed national digital transformation strategies |
| 2 | Smart Africa Alliance (Africa) | Country digital economy blueprints |
| 3 | ITU Digital Development Dashboard | Strategy existence, year, alignment status |
| 4 | DIAL/ADLI Snapshots (Africa) | DPI implementation narrative, current status |
| 5 | AU DTS 2020–2030 | Continental reference to assess country alignment |
| 6 | National ICT ministry websites | Most recent and authoritative version |

### The governance and the institutional capacity
| Priority | Source | Key Data |
|---|---|---|
| 1 | World Bank WGI | GE.EST, RL.EST, CC.EST, RQ.EST, PV.EST, VA.EST |
| 2 | TI CPI | Corruption Perceptions Index score and rank |
| 3 | OGP | Open government commitments |
| 4 | UN SDG 16 | Rule of law, transparency, public service indicators |
| 5 | OECD (members) | Public at a Glance, Digital Government Index |

### The socioeconomic context
| Priority | Source | Key Data |
|---|---|---|
| 1 | World Bank | NY.GDP.PCAP.CD, SI.POV.GINI, SP.POP.TOTL, SP.URB.TOTL.IN.ZS |
| 2 | UNDP HDR | HDI, Gender Inequality Index, MPI |
| 3 | IMF WEO | GDP growth, public debt, inflation |
| 4 | World Bank | SI.POV.DDAY (poverty headcount) |

### The labour market and the skills of the workforce
| Priority | Source | Key Data |
|---|---|---|
| 1 | ILO ILOSTAT | Youth unemployment, employment by sector, participation |
| 2 | World Bank | SL.UEM.1524.ZS (mirrors ILO, no auth needed) |
| 3 | Eurostat | Detailed labor data (EU countries only) |

### The economic and fiscal context
| Priority | Source | Key Data |
|---|---|---|
| 1 | IMF WEO | NGDPDPC, NGDP_RPCH, GGX_NGDP, GGXWDG_NGDP |
| 2 | World Bank | GDP, business environment (IC.* codes) |

---

## Select by the phase of the project

### Phase 1: the first scoping, and the feasibility
Focus on high-level composite indices:
- World Bank GDP, HDI, WGI governance scores, GTMI overall score
- World Bank ID4D — ID ownership rate, birth registration
- UN e-Government Survey EGDI
- TI CPI
- UN SDG progress overview
- DESI (EU) / OECD overview (if applicable)

### Phase 2: the assessment of the needs, and the baseline
Go deep on sector-specific indicators:
- All education sources (UNESCO UIS, UNICEF, IEA TIMSS/PIRLS)
- Giga Maps API (school connectivity)
- Detailed ICT (ITU, Ookla, A4AI)
- Labor market (ILO)
- Governance detail (WGI sub-scores, OGP action plans)
- **Africa**: UNECA Digital ID Landscape, Smart Africa blueprint, DIAL/ADLI snapshot

### Phase 3: the design of the solution, and the development of the policy
Add policy environment and strategy alignment:
- World Bank GTMI sub-scores (which pillar is weakest?)
- World Bank ID4D Country Diagnostic (detailed ID system architecture)
- UNECA/Smart Africa national strategy documents
- AU DTS 2020–2030 alignment check
- ID4Africa country case studies (implementation lessons)
- Cross-country comparisons using same GTMI/EGDI/ID4D indicators

### Phase 4: the monitoring and the evaluation
Focus on SDG-aligned trackable indicators:
- UN SDG API (SDG 4, 9, 16 — including 16.9.1 birth registration)
- World Bank indicators with annual updates
- UNESCO UIS education indicators
- Giga Maps (school connectivity progress)
- GTMI biennial update
- ID4D triennial update (aligns with Global Findex)

---

## A summary of the authentication and the access

| Auth Needed | Sources |
|---|---|
| None (instant API) | World Bank (incl. ID4D, GTMI), UN SDG, IMF, UNDP, WHO, OECD, Eurostat, OGP, ILO |
| Free registration | UNESCO UIS (API key), ITU DataHub (API), Giga Maps API |
| Download only | UN e-Gov Survey, TI CPI, DESI, TIMSS/PIRLS, Ookla, A4AI |
| Web/PDF search | UNECA strategies, Smart Africa blueprints, DIAL/ADLI snapshots, ID4Africa case studies, AU DTS, ID4D Diagnostics |

---

## A guide to how current the data is

| Freshness | Sources |
|---|---|
| Real-time / daily | Giga Daily Check App (school bandwidth monitoring) |
| Monthly | Ookla Speedtest |
| Continuous | Giga Maps / Project Connect (school connectivity, updated as mapped) |
| Annual | World Bank (1–2yr lag), IMF WEO, TI CPI, DESI, ILO, UNDP HDR, A4AI |
| Biennial | UN e-Government Survey (even years), GTMI (even years), Eurostat |
| Every 3 years | ID4D Dataset (aligns with Global Findex), PISA |
| Every 4–5 years | TIMSS/PIRLS |
| Ad hoc (check date) | UNECA/Smart Africa strategies, DIAL/ADLI snapshots, ID4Africa reports |

**The rule**: flag each indicator that is more than 3 years old. Another document can supersede a strategy document that is more than 5 years old. Search for a later version.
