---
name: paera-assessor
description: >
  Assess digital government initiatives, strategies, policies, and organisations against
  the GovStack Public Administration Ecosystem Reference Architecture (PAERA) framework.
  Use this skill whenever a user wants to evaluate a country's digital transformation
  readiness, assess a government agency's digital maturity, review a digital government
  initiative against PAERA principles, score a programme against PAERA dimensions,
  generate a PAERA-aligned assessment report, identify gaps in digital government
  infrastructure, recommend a GovStack implementation roadmap, or check whether a
  digital government plan is aligned with GovStack building blocks. Trigger on keywords:
  PAERA, GovStack, digital government assessment, digital transformation maturity,
  public administration architecture, digital infrastructure assessment, e-government
  readiness, GovStack building blocks, digital public infrastructure, DPI assessment.
---

# PAERA Assessor Skill

Assess digital government initiatives against the GovStack Public Administration
Ecosystem Reference Architecture (PAERA). Produce structured, evidence-based assessments
with actionable recommendations.

**Live documentation**: https://paera.govstack.global  
**Query API**: `GET https://paera.govstack.global/<page>.md?ask=<question>`  
Use this API to fetch up-to-date PAERA content when you need detail beyond what's in this skill file.

---

## Quick Reference: PAERA Structure

PAERA has two primary assessment levels and one implementation layer:

### Level 1 — National Level (Chapter 3)
Assesses the national ecosystem enabling digital government:

| Pillar | Key Questions |
|--------|--------------|
| **3.1 Governance & Policy** | Political leadership? Dedicated agency/CIO? Digital culture? Digital strategy? |
| **3.2 Legal Framework** | E-signature law? Data protection? Cybersecurity law? Digital identity legal basis? Once-only in law? |
| **3.3 Digital Infrastructure** | Connectivity? Cloud? Shared platform approach? Whole-of-government coordination? |
| **3.4.1 Access** | Broadband coverage? Digital literacy programs? Affordability? Inclusion? |
| **3.4.2 Digital Data** | Data privacy law? Open data policy? State registries? Data governance? Interoperability standards? |
| **3.4.3 Interoperability** | Decentralised X-Road-style platform? Governance of interoperability? PKI/audit trail? |
| **3.4.4 Digital Identity** | Legal framework (eIDAS-equivalent)? Identity provider? Token/certificate layer? Digital signature? |

### Level 2 — Organisational Level (Chapter 4)
Assesses individual public administration organisations (ministries, agencies):

| Dimension | What to Evaluate |
|-----------|-----------------|
| **4.2 Management & Architecture** | CDO present? Architecture documented? IT-business alignment? |
| **4.3 Digital Services** | Digital-first? User-centric design? Digital literacy of staff? Omnichannel? |
| **4.4 Data-driven Decisions** | EDW/data warehouse? Dashboards? Data quality process? Metadata? Analytics culture? |
| **4.5 Digital Co-creation** | Multi-year budgeting? Modern procurement? Private sector engagement? Startup ecosystem? |

### Organisational Types (4.6)
- **Policy Development Unit (PDU)**: needs document + content management, analytics
- **Regulatory Agency (RA)**: needs PDU capabilities + digital service delivery platform (forms, licensing, inspections, payments)
- **Service Delivery Authority (SDA)**: needs RA capabilities at industrialised scale + registration, compliance, customer management

### Implementation Framework (Chapter 5)

#### Maturity Levels (5.1)
| Level | Label | Key Indicator |
|-------|-------|---------------|
| Ground Floor | No automation | No IT systems for service delivery |
| 1st Floor | Trust of Data | EDW in place, digital services delivered, architecture managed |
| 2nd Floor | Process Management | SLAs/KPIs, fully digital, data-driven decisions |
| 3rd Floor | Change Management | Can absorb frequent policy changes; business continuity in place |
| 4th Floor | Compliance Management | Proactively recommends policy change; two-sided digital platform |

#### 10 PAERA Principles (5.2)
1. Rule of Law — legal compliance, human rights in digital era, SDG alignment
2. Whole of Government — interoperability, shared services, no silos
3. Digital by Default — digital as primary channel
4. No Legacy Software — 5–7 year lifecycle limit; planned decommissioning
5. Once-Only — data provided once; reused across agencies
6. Customer-centricity — outside-in user design
7. Natural Digital Environment — embed services in citizens' existing digital contexts
8. Public-Private Co-creation — engage private sector, startups, GovTech/CivTech
9. Cross-border by Default — services work across borders; international standards
10. Intrinsic Security & Privacy — security/privacy by design; not afterthought

#### Recommended Roadmap Phases (5.7)
| Phase | Focus | Key BBs |
|-------|-------|---------|
| 1 — Inception | Assessment, governance, cloud, Identity + Payment BBs | Identity, Payment, No-code/Low-code |
| 2 — HPUC | High-priority use cases, MyGov portal | MyGov, IM, Registration, GIS, Workflow, Messaging |
| 3 — Initial Transformation | Digitalise state registries + priority MDAs | All infrastructure BBs |
| 4 — Mass Scale | Full public sector digitalisation | All GovStack BBs |

---

## Assessment Process

### Step 1: Clarify scope
Before assessing, establish:
- **What** is being assessed: a country strategy, a specific agency/programme, a policy, a procurement, or a concept note?
- **Which PAERA level(s)** apply: national, organisational, or both?
- **What information** is available: documents provided, general description, or online-accessible initiative?
- **Purpose**: gap analysis, readiness scorecard, donor reporting, advisory, self-assessment?

### Step 2: Gather evidence
- Ask the user to share relevant documents (strategy, TOR, project documents, legislation).
- If a URL is provided, fetch it.
- Use the PAERA query API for clarification: `https://paera.govstack.global/<page>.md?ask=<question>`
- Note explicitly what evidence is available vs. assumed.

### Step 3: Score each applicable dimension
For each relevant pillar/dimension, assign a rating and cite evidence:

**Rating scale:**
- ✅ **Meets** — clear evidence of requirement being addressed
- ⚠️ **Partial** — some progress but gaps remain
- ❌ **Gap** — not addressed or contradicts PAERA
- ❓ **Unknown** — insufficient information to assess

### Step 4: Identify maturity level (for organisational assessments)
Map findings to the 5-level maturity model (Ground Floor → 4th Floor). An organisation cannot skip levels — identify the *current* level honestly.

### Step 5: Check against the 10 principles
Note which principles are supported, which are at risk, and which are violated.

### Step 6: Identify applicable GovStack Building Blocks
Map gaps to specific BBs that could address them. See reference file for BB list.

### Step 7: Recommend roadmap phase
Based on maturity level and national infrastructure status, recommend which PAERA implementation phase the initiative should target next.

---

## Output Format

Produce structured assessments with these sections:

```
## PAERA Assessment: [Initiative/Country/Organisation Name]

### Executive Summary
[2–3 sentences: what was assessed, overall finding, priority action]

### Scope and Evidence Base
[What documents/information was assessed; confidence level]

### National Level Assessment (if applicable)
[Table or section per pillar with rating + evidence + gap]

### Organisational Assessment (if applicable)
[Maturity level determination + per-dimension findings]

### Principle Alignment
[Which of the 10 principles are met/at risk/violated]

### Building Block Gaps & Recommendations
[Specific BBs to adopt; phase of roadmap]

### Priority Recommendations
[3–5 numbered, specific, actionable items in priority order]

### Suggested Next Steps
[Concrete actions: assessments to run, documents to develop, BBs to pilot]
```

---

## Common Assessment Scenarios

**Country readiness assessment**: Focus on Chapter 3 national pillars. Start with governance and legal framework, then infrastructure pillars. Use GovStack's readiness indicators from 3.1.3.

**Agency/ministry assessment**: Focus on Chapter 4 dimensions + maturity level. Classify org type (PDU/RA/SDA) to calibrate expectations.

**Project/programme review**: Check alignment with 10 principles; identify which BBs are being used vs. custom-built; flag legacy risk; check if national infrastructure is assumed but not confirmed.

**Digital strategy review**: Check against the recommended roadmap phases; assess sequencing logic (is the country trying to skip phases?); check governance and legal preconditions.

**Procurement/TOR review**: Check for BB reuse vs. silo development; flag no-legacy compliance; check for outcome-based requirements; check for open standards.

---

## Important Caveats to Include in Assessments

1. PAERA is a reference architecture, not a rigid compliance standard — adapt language accordingly.
2. Context matters: low-income countries at Ground Floor level need different recommendations than middle-income countries at 2nd Floor.
3. "Chicken-egg" problems are normal — acknowledge sequencing dependencies (e.g., can't build personalized services without Digital ID).
4. Political will is the most important readiness factor — note if it's absent.
5. Donor-funded projects need explicit state budget commitment for sustainability.

---

## Reference Files

- `references/building-blocks.md` — Full list of GovStack building blocks with descriptions
- `references/state-registries.md` — Key state registries for Annex 3 reference

Read these when you need the specific details they contain. For anything not covered, query the live PAERA API.
