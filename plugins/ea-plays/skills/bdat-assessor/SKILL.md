---
name: bdat-assessor
description: >-
  Use this skill to assess a government body, a sector, or a digital initiative with the
  BDAT model, which has the four layers Business, Data, Application and Technology. The
  assessment is grounded in the PAERA metamodel and in the GovStack building block
  principles. Trigger on: "BDAT
  assessment", "assess using BDAT", "read this ministry in four layers", "enterprise
  architecture review", "capability mapping", "data domain ownership", "application
  portfolio review", "architecture gap analysis", "current-state architecture",
  "target-state architecture", "orphan systems", "duplicate registry", "point-to-point
  integration", "bespoke trap", "vendor lock-in", "government architecture audit",
  "classify this body", "PAERA metamodel", "GovStack architecture",
  "whole-of-government architecture". Also trigger when a user shares a strategy
  document or sector description and asks for an architectural reading or gap analysis.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
---

# BDAT Assessor Skill

This skill assesses government bodies, sectors and digital initiatives with the BDAT model.
The four layers of the model are Business, Data, Application and Technology. The assessment
uses the PAERA metamodel and the principles of the GovStack building blocks.

Write an assessment that is honest about the trade-offs, that has evidence a reader can
verify, and that helps a person to make an investment decision. Do not write documentation.

---

## BDAT reference: the four layers

Each layer has a question that governs it, a deliverable, and a quality test. Apply the
test of each layer before you accept that the picture is complete.

| Layer | Governing question | Expected deliverable | Quality test |
|-------|-------------------|---------------------|--------------|
| **Business** | What does this body do, for whom, and how well? | Capability map and service catalogue | It describes capabilities, not boxes on an organisation chart. If the ministers changed, the map would not change |
| **Data** | What information does the body hold, who owns it, and where is the authoritative copy? | Data-domain catalogue with one owner for each domain | Each domain has exactly one named owner and one authoritative copy |
| **Application** | What software supports the work, and which capability does each application serve? | Application portfolio, mapped to the capabilities and the data domains | Each system maps to a capability and to a data domain. There are no orphan systems |
| **Technology** | What does the software run on? | A short list of technology standards and a simple picture of the infrastructure | It names the standards in use and the single points of failure. It is not an audit of each server |

### The traceability chain

Each assessment must be able to trace this chain:
**Service → Capability (Business) → Application → Data Domain(s) → Technology**

A layer with no connection above it or below it is the first gap.

---

## PAERA metamodel: the shared entity types

Use these entity types in the same way each time. Do not invent a variant for a body or for
a sector.

| Entity | Definition |
|--------|-----------|
| **Capability** | Something that a public body can do, for example register a learner or certify a result |
| **Service** | How a capability reaches a citizen or another body |
| **Application** | Software that supports a capability |
| **Data Domain** | A kind of information, with exactly one owner |
| **Technology Component** | The infrastructure below the applications |
| **Organisation** | The owner of capabilities, data domains and applications |

These relationships are fixed. Do not change them:

- Capability → *delivered by* → Service
- Capability → *supported by* → Application
- Application → *uses* → Data Domain
- Everything → *runs on* → Technology Component
- Organisation → *owns* → each of the above

**Source**: PAERA v1.0 Annex 2

---

## Organisational taxonomy: classify first

Classify each body before you model it. The classification gives you an expected profile.
Confirm the profile or correct it. Do not start with nothing.

| Type | Primary role | Expected data domains | Typical risk |
|------|--------------|-----------------------|--------------|
| **Policy Unit** | Sets policy and owns the rules. Does not operate services at scale | Policy instruments, standards, funding allocations | The capability moves into regulation or delivery with no mandate |
| **Regulatory Agency** | Licenses, supervises and enforces. Holds registers and decisions | Register of the regulated bodies, licences, decisions, appeals | It builds its own infrastructure for delivery instead of using the shared platforms |
| **Service-Delivery Authority** | Operates services to citizens at scale | Case files, transactions, outcomes, queues | Duplicate registries, lock-in to a vendor, bespoke build |
| **State Registry** | The authoritative single source for one domain | One canonical domain: person, learner, business or land | The ministry that hosts it treats it as its own asset, not as a shared resource |
| **Shared Platform** | Identity, payments and data exchange, used by many bodies | Few. It gives infrastructure, not content | Fragmentation, if each sector builds its own instead of using the platform |

**Source**: PAERA v1.0 §4.6; Annex A1.2

---

## Assessment process

### Step 1 — Clarify the scope

Establish these four items before you assess:

- **What** you assess: one ministry, a sector, one programme, a procurement, or a strategy
  document.
- **What information** you have: the documents that the learner gave you, a general
  description, or interview notes.
- **The purpose**: a gap analysis, an investment decision, an input to a roadmap, a report
  to a donor, or a self-assessment.
- **Which layers** are in scope: all four, or one of them.

### Step 2 — Classify the bodies

For each organisation in the scope, do these three steps:

1. Apply the taxonomy: Policy Unit, Regulatory Agency, Service-Delivery Authority, State
   Registry, or Shared Platform.
2. Give the expected profile for that type.
3. Record a classification that is wrong. A body that operates outside its type is a
   finding.

### Step 3 — Read the four layers

Read the layers in order. Use the governing question and the quality test of each layer.
Record these three items for each layer:

- what exists, with the evidence for it;
- what is missing, against the quality test;
- each entity with no named owner.

At the end, apply the traceability check between the layers. Trace a minimum of one service
from the citizen to the infrastructure.

### Step 4 — Apply the four universal gap tests

These gaps are in almost every first assessment. Look for each of them.

1. **Duplicate registries** — two bodies or more hold their own version of the same data
   domain, and the versions do not agree. Test: how many bodies say that they own the
   record of the learner, the person, the business, or the land?
2. **Orphan systems** — applications that map to no current capability. Test: for each
   application, can you name the capability that it supports?
3. **Point-to-point integration** — each system connects to each other system by its own
   custom link, and there is no shared backbone for data exchange. Test: is there a shared
   integration layer, or does each pair of systems have its own custom connection?
4. **No clear owner** — many bodies use a capability or a data domain, and no body owns it.
   Test: for each domain, is there exactly one body that accepts accountability for its
   accuracy and its currency?

### Step 5 — Check the two architecture traps

Flag these traps at Assess, before somebody builds them.

**The bespoke trap.** A project proposes to build a function that already exists as a shared
building block. The decision is rational for the project and ruinous for the country. Flag
it whenever a project intends to build its own function for identity, payments or data
exchange.

Ask these two questions:

- Does a shared building block already exist for the function that this project wants to
  build?
- Is the decision to build instead of to reuse a deliberate decision, or is it the easiest
  path?

**The vendor-driven trap.** A product becomes the architecture. The processes change to fit
the product. The data goes into storage in the format of the product. The other systems
integrate to the product and not to a standard.

Ask these three questions:

- Is the data stored to an open standard, or to the format of one vendor?
- If this supplier made the price two times higher, could the government replace the
  supplier in two years?
- Who understands how this system works: the staff of the government, or only the vendor?

**Source**: PAERA v1.0 §5.6 (Sourcing — build / buy / share / sandbox)

### Step 6 — Score each layer

Score each layer against its quality test:

- ✅ **Sound** — it passes the quality test, and it is complete enough for a decision.
- ⚠️ **Partial** — some elements are present, but the gaps change a decision.
- ❌ **Gap** — it fails the quality test. A person cannot make a decision from this layer.
- ❓ **Unknown** — there is not enough information to assess the layer.

### Step 7 — Write the assessment

See the output format below.

---

## Common mistakes of a first-time architect

These are active checks. They are not background knowledge. For each mistake, record whether
the material that you assess contains the mistake.

| Mistake | Active check |
|---------|-------------|
| The organisation chart is the Business layer | Does the Business layer describe capabilities, or lines of reporting? |
| The Data layer lists databases, not domains | Does the Data layer name entity types with their owners, or systems that store data? |
| The Application layer and the Technology layer are mixed | Are the software components separate from the infrastructure? |
| No traceability between the layers | Can you follow one service from the citizen to the infrastructure? |
| BDAT is used only to describe, not to analyse | Is there a comparison between the current state and the target state? |
| The pressure upward from the lower layers is ignored | Does the assessment record how the constraints in technology limit what is possible above? |
| The impact of a change is not modelled | If somebody adds a new component, does the assessment trace the consequences in each layer? |
| Governance gaps at the Data layer and the Application layer | Is there a named owner and change control for each layer, or only for Technology? |

---

## Architectural principles to apply

These PAERA principles apply directly to BDAT. Record which principles the material meets,
which are at risk, and which it violates.

| Principle | The BDAT layer that it tests | What to check |
|-----------|--------------------|-|
| **Once-only** | Data | Each domain has one authoritative copy. The bodies that use the domain do not hold their own copy |
| **Reuse before buy, buy before build** | Application | A bespoke build where a shared building block exists is a violation |
| **Data as a managed asset — one source of truth** | Data | One owner for each domain, named in the assessment |
| **Technology neutrality and no lock-in** | Technology and Application | The data is stored to open standards. You tested whether the government can replace the supplier |
| **Interoperability by default** | Application and Technology | A shared backbone for data exchange, and not point-to-point integrations |

**Source**: PAERA v1.0 §5.2

---

## Output format

Write the provenance header first (`references/provenance-header.md`), then the assessment.
Posts, not names; text in, text out — no file, no chart, no image, so that plays 2.5 and 2.6
can consume it. See `references/output-contract.md`.

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

## Honesty standard

An assessment can flatter the current state. It can make a duplicate-registry problem look
small because a powerful ministry owns one of the copies. It can record a principle as met
when only an intention exists. Such an assessment fails one year later, quietly and at high
cost.

- **A severe score needs direct evidence.** Do not give a layer ❌ because you suspect a
  problem. Cite what is missing or what does not agree.
- **Flag each gap and each false negative.** Do not hide them.
- **Record the pressure from the layers below.** If the constraints in technology limit what
  is possible above, say so. Do not give a target that the country cannot reach.
- **The enabling conditions are as important as the findings.** Record what must be true
  before a person can act on a recommendation: governance, political will, a legal basis, and
  funding.

---

## Reference files

- `references/change-impact-template.md` — a template to trace the consequences of a
  proposed change in each layer. The change can be a new building block, the retirement of a
  system, or a migration to a platform. Read this file when the assessment covers a proposed
  investment or intervention, and not only a description of the current state. Its filled
  example is fixture material and carries the marker.

### Fixture material

- `references/worked-example.md` — the walkthrough in the education sector: how to classify
  a body, how to read four layers, how to trace a service, and how to name the gaps. Read
  this file when the user needs a concrete model to follow or to compare against.

  Progressa is the fictional demonstration country that each play shares. The canonical
  description is `tests/progressa.md` in the kit repo.

### The shared contract

- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` — read them before you
  write the output. They are the same four files that each skill in this kit obeys.
