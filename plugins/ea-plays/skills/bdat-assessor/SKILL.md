---
name: bdat-assessor
description: >
  Use this skill to assess government bodies, sectors, or digital initiatives using the
  BDAT (Business, Data, Application, Technology) enterprise architecture model, grounded
  in the PAERA metamodel and GovStack building block principles. Trigger on: "BDAT
  assessment", "assess using BDAT", "read this ministry in four layers", "enterprise
  architecture review", "capability mapping", "data domain ownership", "application
  portfolio review", "architecture gap analysis", "current-state architecture",
  "target-state architecture", "orphan systems", "duplicate registry", "point-to-point
  integration", "bespoke trap", "vendor lock-in", "government architecture audit",
  "classify this body", "PAERA metamodel", "GovStack architecture",
  "whole-of-government architecture". Also trigger when a user shares a strategy
  document or sector description and asks for an architectural reading or gap analysis.
---

# BDAT Assessor Skill

Conduct structured enterprise architecture assessments of government bodies, sectors,
and digital initiatives using the BDAT (Business, Data, Application, Technology) model,
grounded in the PAERA metamodel and aligned to GovStack building block principles.

Produce assessments that are honest about trade-offs, anchored in verifiable evidence,
and useful for investment decisions — not just documentation exercises.

---

## BDAT Reference: The Four Layers

Each layer has a governing question, an expected deliverable, and a quality test.
Hold every layer to its own test before accepting the picture as complete.

| Layer | Governing Question | Expected Deliverable | Quality Test |
|-------|-------------------|---------------------|--------------|
| **Business** | What does this body do, for whom, and how well? | Capability map + service catalogue | Describes capabilities, not org boxes — could swap ministers and the map would not change |
| **Data** | What information does the body hold, who owns it, where is the authoritative copy? | Data-domain catalogue with one owner per domain | Every domain has exactly one named owner and one authoritative copy |
| **Application** | What software supports the work, and which capability does each one serve? | Application portfolio mapped to capabilities and data domains | Every system maps to a capability and a data domain — no orphan systems |
| **Technology** | What does everything run on? | Short list of technology standards + simple infrastructure picture | Names standards in use and single points of failure — not a server-by-server audit |

### The Traceability Chain
Every assessment must be able to trace:
**Service → Capability (Business) → Application → Data Domain(s) → Technology**

A layer that floats free — with no connection up or down — is the first gap.

---

## PAERA Metamodel: Shared Entity Types

Use these entity types consistently. Do not invent per-body or per-sector variants.

| Entity | Definition |
|--------|-----------|
| **Capability** | Something a public body can do (e.g., register a learner, certify a result) |
| **Service** | How a capability reaches a citizen or another body |
| **Application** | Software that supports a capability |
| **Data Domain** | A kind of information, with exactly one owner |
| **Technology Component** | The infrastructure underneath |
| **Organisation** | Owns capabilities, data domains, applications |

Fixed relationships (do not vary these):
- Capability → *delivered by* → Service
- Capability → *supported by* → Application
- Application → *uses* → Data Domain
- Everything → *runs on* → Technology Component
- Organisation → *owns* → each of the above

**Source**: PAERA v1.0 Annex 2

---

## Organisational Taxonomy: Classify First

Classify every body before modelling it. Classification gives you an expected profile —
confirm or correct it rather than starting from blank.

| Type | Primary Role | Expected Data Domains | Typical Risk |
|------|--------------|-----------------------|--------------|
| **Policy Unit** | Sets policy, owns rules; does not run services at scale | Policy instruments, standards, funding allocations | Capability drift into regulation or delivery without mandate |
| **Regulatory Agency** | Licenses, supervises, enforces; holds registers and decisions | Register of the regulated, licences, decisions, appeals | Building its own delivery infrastructure rather than consuming shared platforms |
| **Service-Delivery Authority** | Runs services to citizens at scale | Case files, transactions, outcomes, queues | Duplicate registries, vendor lock-in, bespoke build |
| **State Registry** | Authoritative single source for one domain | One canonical domain (person, learner, business, land) | Treated as a private asset of the hosting ministry rather than a shared resource |
| **Shared Platform** | Identity, payments, data exchange — consumed across many bodies | Minimal; provides infrastructure, not content | Fragmentation if each sector builds its own instead of consuming |

**Source**: PAERA v1.0 §4.6; Annex A1.2

---

## Assessment Process

### Step 1 — Clarify Scope
Before assessing, establish:
- **What** is being assessed: a single ministry, a sector, a specific programme, a procurement, a strategy document?
- **What information** is available: documents provided, general description, interview notes?
- **Purpose**: gap analysis, investment decision, roadmap input, donor report, self-assessment?
- **Which layers** are in scope: all four, or a specific one?

### Step 2 — Classify the Bodies
For each organisation in scope:
1. Apply the taxonomy (Policy Unit, Regulatory Agency, Service-Delivery Authority, State Registry, Shared Platform)
2. State the expected profile for that type
3. Note any misclassification — a body acting outside its type is itself a finding

### Step 3 — Read the Four Layers
Work through each layer in order, using the governing question and quality test.
For each layer, record:
- What exists (evidence-based)
- What is missing against the quality test
- Any entity with no named owner

Apply the cross-layer traceability check at the end: can you trace at least one service all the way from citizen-facing to infrastructure?

### Step 4 — Apply the Four Universal Gap Tests
These gaps appear in almost every first assessment. Look for them deliberately:

1. **Duplicate registries** — multiple bodies each holding their own version of the same data domain, none agreeing. Test: how many bodies claim to own the [learner / person / business / land] record?
2. **Orphan systems** — applications that map to no current capability. Test: for every application named, can you point to the capability it supports?
3. **Point-to-point spaghetti** — every system connected to every other by its own custom link, with no shared data-exchange backbone. Test: is there a shared integration layer, or does every pair of systems have its own custom connection?
4. **No clear owner** — a capability or data domain everyone uses and no one owns. Test: for each domain, is there exactly one body prepared to be held accountable for its accuracy and currency?

### Step 5 — Check the Two Architecture Traps
Flag these at Assess, before they are built:

**Bespoke Trap**: A project proposes to build a function that already exists as a shared building block. Locally rational; nationally ruinous. Flag whenever a project intends to build its own identity, payments, or data-exchange function.
Diagnostic questions:
- Does a shared building block already exist for what this project wants to build?
- Is the build-vs-reuse decision deliberate, or is it the path of least resistance?

**Vendor-Driven Trap**: A product quietly becomes the architecture. Processes bend to fit it; data is stored the product's way; other systems integrate to the product, not to a standard.
Diagnostic questions:
- Is the data stored to an open standard, or to one vendor's format?
- If this supplier doubled their price, could the government replace them within two years?
- Who understands how this system works — government staff, or only the vendor?

**Source**: PAERA v1.0 §5.6 (Sourcing — build / buy / share / sandbox)

### Step 6 — Score Each Layer
Rate each layer against its quality test:

- ✅ **Sound** — passes the quality test; complete enough to decide from
- ⚠️ **Partial** — some elements present but gaps material to decisions
- ❌ **Gap** — quality test fails; layer cannot be used for decisions as-is
- ❓ **Unknown** — insufficient information to assess

### Step 7 — Produce the Assessment
See Output Format below.

---

## Common First-Time Architect Mistakes to Check Against

These are active checks, not background knowledge. For each, note whether the mistake
is present in the material being assessed.

| Mistake | Active Check |
|---------|-------------|
| Org chart used as Business layer | Does the Business layer describe capabilities or reporting lines? |
| Data layer lists databases, not domains | Does the Data layer name entity types with owners, or storage systems? |
| Application and Technology layers conflated | Are software components and infrastructure clearly separated? |
| No traceability between layers | Can you follow one service from citizen to infrastructure? |
| BDAT used descriptively only, not analytically | Is a current-state vs. target-state comparison present? |
| Upward pressure from lower layers ignored | Does the assessment note how technology constraints bound what is feasible above? |
| Change-impact not modelled | If a new component is introduced, are cross-layer consequences traced? |
| Governance gaps at Data and Application layers | Is there named ownership and change-control for each layer, or only at Technology? |

---

## Architectural Principles to Apply

The following PAERA principles have direct BDAT implications. Note which are met,
at risk, or violated.

| Principle | BDAT Layer It Tests | What to Check |
|-----------|--------------------|-|
| **Once-only** | Data | Every domain has one authoritative copy; consuming bodies do not hold their own |
| **Reuse before buy, buy before build** | Application | Any bespoke build where a shared BB exists is a violation |
| **Data as a managed asset — one source of truth** | Data | One owner per domain; named in the assessment |
| **Technology neutrality / avoid lock-in** | Technology + Application | Data stored to open standards; supplier replaceability tested |
| **Interoperability by default** | Application + Technology | Shared data-exchange backbone vs. point-to-point integrations |

**Source**: PAERA v1.0 §5.2

---

## Output Format

```
## BDAT Assessment: [Organisation / Sector / Initiative Name]

### Scope and Evidence Base
[What was assessed; what information was available; confidence level]

### Organisational Classification
[Body type per taxonomy; expected profile; any misclassification finding]

### Layer-by-Layer Findings

#### Business Layer [✅ / ⚠️ / ❌ / ❓]
Capabilities identified: [list]
Services identified: [list]
Quality test result: [capabilities or org boxes?]
Gaps: [missing capabilities, unowned services, duplicate claims]

#### Data Layer [✅ / ⚠️ / ❌ / ❓]
Domains identified: [domain — owner — authoritative copy location]
Quality test result: [one owner per domain?]
Gaps: [duplicate domains, missing ownership, databases listed instead of domains]

#### Application Layer [✅ / ⚠️ / ❌ / ❓]
Systems identified: [system — capability served — data domains used]
Quality test result: [every system maps to a capability and domain?]
Gaps: [orphan systems, systems with no data domain link, duplicate functions]

#### Technology Layer [✅ / ⚠️ / ❌ / ❓]
Standards in use: [list]
Single points of failure: [list]
Quality test result: [standards and failure points named, not a server audit?]
Gaps: [missing backbone, no standards named, server-level detail without architecture-level view]

### Traceability Check
[Can one service be traced from citizen to infrastructure? Show the chain, or name where it breaks.]

### Four Universal Gaps
1. Duplicate registries: [present / absent / unknown — evidence]
2. Orphan systems: [present / absent / unknown — evidence]
3. Point-to-point spaghetti: [present / absent / unknown — evidence]
4. No clear owner: [present / absent / unknown — evidence]

### Architecture Trap Flags
- Bespoke trap: [flagged / clear — evidence]
- Vendor-driven trap: [flagged / clear — evidence]

### Principle Alignment
[Table or list: which PAERA principles are met / at risk / violated, with evidence]

### First-Time Architect Mistakes Present
[List any of the eight common mistakes identified in the assessed material]

### Priority Gaps (ranked by impact × feasibility)
1. [Highest priority gap — why it hurts — what closing it requires]
2. ...

### Recommended Next Steps
[3–5 concrete, sequenced actions]
```

---

## Honesty Standard

An assessment that flatters the current state — that softens a duplicate-registry
problem because a powerful ministry owns one of the copies, or marks a principle
as met when only an intention exists — fails quietly and expensively, a year later.

- **Severe ratings require direct evidence.** Do not rate a layer ❌ on suspicion;
  cite what is missing or contradictory.
- **Gaps and false negatives must be flagged explicitly**, not papered over.
- **Upward pressure must be acknowledged**: if technology constraints bound what
  is achievable above, say so rather than presenting an aspirational target as reachable.
- **Enabling conditions are as important as findings**: note what must be true for
  a recommendation to be actionable — governance, political will, legal basis, funding.

---

## Reference Files

- `references/change-impact-template.md` — Template for tracing the cross-layer
  consequences of a proposed change (new BB, system retirement, platform migration).
  Read this when the assessment involves a proposed investment or intervention, not
  just a current-state description (its filled example is fixture material and carries
  the marker).

### Fixture material

- `references/worked-example.md` — the education-sector walkthrough: how to classify, read
  four layers, trace a service, and name gaps. Read this when the user needs a concrete
  model to follow or compare against.
  Progressa is the fictional demonstration country shared by every play; the canonical
  description is `tests/progressa.md` in the kit repo.
