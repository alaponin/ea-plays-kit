---
name: bb-sourcing-researcher
description: >
  Conduct market research on GovStack / PAERA building blocks and reason about whether each
  block should be sourced as a reused product (open-source DPG or commercial), configured on
  an adjacent block, or custom-built — a structured vendor-vs-bespoke (build-vs-buy) analysis.
  Use whenever a user wants to: find open-source and commercial providers for a
  digital-government capability; map building blocks to implementation options; assess lock-in
  risk; choose between a digital public good and a proprietary product; produce a
  sourcing-decision matrix; size a programme's bespoke footprint; or build a procurement
  options analysis. Trigger on: market research building blocks, vendor vs bespoke, build vs
  buy, sourcing options, DPG vs commercial, open-source alternatives, implementation providers,
  lock-in risk, sourcing decision matrix, reuse vs build, off-the-shelf vs custom, digital
  public goods landscape. Pairs with govstack-cost-estimator, which sizes the cost; this skill
  decides the sourcing posture per block.
---

# Building Block Sourcing Researcher

A research-and-reasoning skill that, for any GovStack / PAERA building block, (1) finds
real open-source and commercial implementation options through live market research, and
(2) reasons about the **sourcing posture** for each block on a four-way scale:

**Reuse-OSS → Reuse-Commercial → Configure → Custom-build**

The output is an evidence-based options analysis that a government, donor, or advisor can
take into procurement. This skill decides *what kind of thing to procure*; hand the chosen
posture to `govstack-cost-estimator` to put numbers on it.

---

## Core stance (read first)

1. **Reuse is the default; custom is the exception that must be justified.** The burden of
   proof sits on bespoke build, not on reuse. Every "custom" recommendation must name the
   specific requirement that no existing product or configuration meets.
2. **GovStack is product-agnostic.** "GovStack-listed" means a product self-assessed against
   the specs and appears in the catalogue with a compliance level (Level 1 / Level 2). It is
   a transparency aid, **not** an endorsement or quality ranking. Absence from the catalogue
   is not evidence against a product — the catalogue is small and submission-ordered.
3. **Prefer the DPG, procure the integrator.** For mature blocks the most defensible route is
   an open-source digital public good deployed and operated under a competitively tendered
   system-integrator / support contract. State this explicitly rather than framing OSS as
   "free but unsupported."
4. **Evidentiary conservatism.** Every named product and every claim about it must come from
   research conducted in-session (live web research or a cited reference file). Do not invent
   vendors, compliance levels, deployment counts, or licence terms. If the market for a block
   is thin, say so — an honest gap is more useful than a padded list.
5. **Name the lock-in.** For every commercial option, state the lock-in vector (data,
   licence, proprietary tooling, ecosystem) so the reader can weigh it.

---

## Step 0 — Scope the request

Establish before researching (ask for all missing items in ONE message; don't re-ask what's
already given):

| Parameter | Why it matters |
|---|---|
| **Blocks in scope** | One block, a subset (e.g. KP3 DPI Roadmap blocks), or all 18 |
| **Country / region** | Determines which vendors are realistically available, in-country SIs, mobile-money rails, data-residency rules |
| **Sector / use case** | Education vs health changes which products are relevant (e.g. DHIS2 SEMIS for education analytics) |
| **Existing systems** | What is already deployed (reuse/extend beats greenfield) — pull from any prior BDAT assessment |
| **Decision purpose** | Landscape scan, procurement options analysis, lock-in audit, or bespoke-footprint sizing |
| **Sovereignty constraints** | Is self-hosting / data residency mandatory? (Rules out some commercial SaaS) |

If a prior `bdat-assessor` or `paera-assessor` output exists for this sector, read it first —
the application-portfolio and gap analysis tell you what already exists and what is missing.

---

## Step 1 — Load the reference scaffolding

Read `references/research-method.md` for:
- The canonical 18-block list and the capability each block delivers
- The **source map** — where to look for each block (GovStack catalogue, DPGA registry,
  project sites, OSS comparison sources) and the search-query patterns that work
- Maturity priors per block (which blocks have strong OSS markets vs thin/gap markets)

Read `references/build-vs-buy.md` for:
- The four-way sourcing-posture scale and its decision criteria
- The lock-in taxonomy and how to score it
- The reasoning rules that turn research findings into a recommended posture

Read `references/worked-example.md` for a complete eighteen-block analysis (Gambia education
context) to follow or compare against.

---

## Step 2 — Research each block

For each block in scope, run live research (do **not** rely on memory for current products):

1. **Anchor on the curated sources first** (see source map): the GovStack Building Block
   Software catalogue and the DPGA registry give vetted, government-relevant candidates.
2. **Then widen** to project sites and OSS comparison sources for options not yet in those
   catalogues.
3. **Capture for each candidate**: name, model (OSS / Commercial / Open-core / DPG),
   GovStack-listed? (with level), maintainer/backer, evidence of real government deployments,
   licence, and the lock-in vector (for commercial/open-core).
4. **Note the channel reality**: some blocks (Payments, Messaging) depend on in-country rails
   (mobile money, local SMS aggregators) that must be integrated regardless of platform choice.

Scale effort to the request: a single-block question may need 1–3 searches; a full 18-block
landscape may need 8–15. Search per block rather than one combined query — combined queries
return shallow results for all of them.

---

## Step 3 — Reason about sourcing posture per block

Apply the four-way scale from `build-vs-buy.md`. For each block, produce:

- **Recommended posture**: Reuse-OSS / Reuse-Commercial / Configure / Custom-build
- **Why**: the one or two decisive factors (market maturity, fit, sovereignty, lock-in)
- **Lock-in risk**: Low / Medium / High, with the vector named
- **Bespoke-footprint contribution**: does this block add to custom code, or not?

The four postures, in preference order:

1. **Reuse-OSS** — a mature DPG/OSS product fits; procure an SI to deploy/operate it.
   *Default for Identity, Payments, Data Exchange, Registries, Analytics, GIS.*
2. **Reuse-Commercial** — a competitively sourced commercial product or channel is the
   realistic route, usually for ancillary competitive layers (biometric devices, SMS/mobile
   money, qualified trust services) slotting into an open core.
3. **Configure** — no standalone product dominates; deliver as a configured feature of an
   adjacent block (e.g. Consent on the Information Mediator; Scheduler via Workflow).
   *Specify open APIs so it doesn't silently become custom.*
4. **Custom-build** — justified only by a named requirement no product or configuration meets.
   Every custom recommendation triggers the bespoke-footprint flag.

---

## Step 4 — Assemble the output

Default structure (adapt to the decision purpose):

```
## Building Block Sourcing Analysis: [scope / country / sector]

### Executive Summary
[2–3 sentences: how many blocks reuse vs configure vs custom; headline lock-in/footprint finding]

### Per-Block Analysis
[For each block: capability one-liner; provider table (Provider | Model | Notes/lock-in);
 recommended posture; lock-in risk; footprint contribution]

### Sourcing-Decision Matrix
| Block | Posture | Top OSS option | Top commercial option | Lock-in | Adds to bespoke? |
| ...   | Reuse-OSS | MOSIP | Idemia (partner) | Low | No |

### Bespoke Footprint Roll-up
[Count/percentage of blocks landing in Custom-build or at-risk Configure; compare to <20% target]

### Cross-Cutting Findings
[Thin-market blocks; channel dependencies; sovereignty constraints; SI-market depth]

### Assumptions, Evidence Base, and Caveats
[Always last. What was researched live vs. carried from references; date sensitivity;
 "confirm against live procurement terms before sourcing".]
```

The default deliverable is **plain prose plus tables** (Word/markdown). The user prefers
structured text over interactive widgets for reference and briefing documents — do not render
card layouts or dashboards unless explicitly asked. For a downloadable document use the `docx`
skill; for a quick in-chat answer, markdown tables are fine.

---

## Step 5 — Hand-off and adjacency

- **To `govstack-cost-estimator`**: once each block has a posture, the estimator turns
  reuse/configure/custom into siloed-vs-shared TCO. Sourcing posture is the *input* to the
  cost model, not a duplicate of it — do not re-derive costs here.
- **From `bdat-assessor` / `paera-assessor`**: their gap and portfolio findings tell you which
  blocks already exist (extend, don't re-buy) and which are genuinely missing.
- **With `country-context-data`**: pull in-country vendor presence, mobile-money rails, and
  data-residency law to ground "is this vendor realistically available here" judgments.

---

## Anti-patterns to flag in any analysis

- **Bespoke trap** — custom-building something a product already covers, increasing
  fragmentation and future legacy cost. The single most important thing this skill exists to
  prevent.
- **Generic-ESB-as-mediator** — choosing a generic enterprise service bus over an X-Road-style
  Information Mediator, recreating point-to-point integration without the security/audit envelope.
- **Silent configure-to-custom drift** — a block labelled "configure" that, without open-API
  discipline, becomes a bespoke build nobody decided to fund.
- **SaaS sovereignty mismatch** — recommending a commercial cloud SaaS where data-residency law
  or sovereignty policy forbids it.
- **Catalogue-as-endorsement** — treating GovStack-listing as a quality score, or absence from
  it as disqualifying.
- **Memory-sourced vendors** — naming products or compliance levels from training data rather
  than live research. Always research; always cite.

---

## Important caveats to always include

1. Vendor characterisations reflect general market positioning at the time of research and
   must be confirmed against live procurement terms before any sourcing decision.
2. This is an options analysis, not a procurement recommendation or a substitute for a full
   business case / feasibility study.
3. Product markets move quickly (especially Digital Wallet and AI/ML) — re-run research if the
   analysis is more than a few months old.
4. A "reuse" verdict still requires real implementation effort (configuration, integration,
   operation) — reuse reduces, but does not eliminate, cost and risk.

---

## Reference Files

- `references/research-method.md` — 18-block list, source map, search patterns, maturity priors
- `references/build-vs-buy.md` — four-way posture scale, lock-in taxonomy, reasoning rules
- `references/worked-example.md` — full eighteen-block analysis in a Gambia education context

Read these when you need the detail they contain. For anything not covered, research live and
cite.
