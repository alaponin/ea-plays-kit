---
name: bb-sourcing-researcher
description: >-
  Do market research on the GovStack and PAERA building blocks, then reason about how to
  source each one: reuse a product, which can be an open-source digital public good or a
  commercial product; configure the block on an adjacent block; or build it. This is a
  structured vendor-versus-bespoke analysis, also called build-versus-buy. Trigger on:
  market research building blocks, vendor vs bespoke, build vs buy, sourcing options, DPG vs
  commercial, open-source alternatives, implementation providers, lock-in risk, sourcing
  decision matrix, reuse vs build, off-the-shelf vs custom, digital public goods landscape,
  "find providers for a digital-government capability", "map building blocks to
  implementation options", "size a programme's bespoke footprint", "procurement options
  analysis". Pairs with ea-cost-case, which sizes the cost; this skill decides the sourcing
  posture per block.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
---

# Building Block Sourcing Researcher

This skill does research and reasoning. For any GovStack or PAERA building block it does two
things. It finds real open-source and commercial options with live market research. Then it
reasons about the **sourcing posture** of each block on a scale of four:

**Reuse-OSS → Reuse-Commercial → Configure → Custom-build**

The output is an options analysis with evidence. A government, a donor or an advisor can
take it into a procurement. This skill decides *what kind of thing to procure*. Give the
posture that you choose to `ea-cost-case`, which puts numbers on it.

---

## The core stance (read this first)

1. **Reuse is the default. Custom is the exception, and it needs a justification.** The
   burden of proof is on the bespoke build, not on the reuse. Each recommendation to build
   must name the specific requirement that no product and no configuration meets.
2. **GovStack does not endorse products.** "GovStack-listed" means that a product assessed
   itself against the specifications, and that the catalogue shows it with a compliance
   level, which is Level 1 or Level 2. The catalogue helps transparency. It is **not** an
   endorsement and it is not a ranking of quality. A product that is not in the catalogue is
   not a worse product. The catalogue is small, and it is in the order of submission.
3. **Prefer the digital public good. Procure the integrator.** For a mature block, the route
   that you can defend best is an open-source digital public good. A system integrator
   deploys and operates it under a support contract that you tender competitively. State this
   route. Do not describe open-source software as "free but unsupported".
4. **Be conservative with evidence.** Each product that you name, and each claim about it,
   must come from research in this session. This is live web research, or a reference file
   that you cite. Do not invent a vendor, a compliance level, a count of deployments, or a
   licence term. If the market for a block is thin, say so. An honest gap is more useful than
   a list that you filled.
5. **Name the lock-in.** For each commercial option, give the lock-in vector: the data, the
   licence, the proprietary tooling, or the ecosystem. The reader then can judge it.

---

## Step 0 — Scope the request

Establish these six items before you research. Ask for all the items that you do not have in
ONE message. Do not ask again for an item that the learner gave you.

| Parameter | Why it matters |
|---|---|
| **Blocks in scope** | One block, a subset such as the KP3 DPI Roadmap blocks, or all 18 |
| **Country / region** | It decides which vendors are available, which system integrators are in the country, which mobile-money rails exist, and which data-residency rules apply |
| **Sector / use case** | Education and health need different products, for example DHIS2 SEMIS for education analytics |
| **Existing systems** | What the country already operates. To reuse or extend is better than to start again. Take this from a BDAT assessment, if one exists |
| **Decision purpose** | A landscape scan, a procurement options analysis, a lock-in audit, or a measurement of the bespoke footprint |
| **Sovereignty constraints** | Is self-hosting or data residency mandatory? This removes some commercial SaaS products |

If a prior `bdat-assessor` or `paera-reference-check` output exists for this sector, read it
first. Its application portfolio and its gap analysis tell you what exists and what is
missing.

---

## Step 1 — Load the reference material

Read `references/research-method.md` for these three items:

- the canonical list of 18 blocks, and the capability that each block gives;
- the **source map**, which gives where to look for each block, which is the GovStack
  catalogue, the DPGA registry, the project sites and the sources that compare open-source
  products, and the patterns of search query that work;
- the maturity prior for each block, which tells which blocks have a strong open-source
  market and which have a thin market or no market.

Read `references/build-vs-buy.md` for these three items:

- the scale of four sourcing postures and the criteria to decide between them;
- the taxonomy of lock-in and how to score it;
- the rules that turn a research finding into a recommended posture.

Read `references/worked-example.md` for a complete analysis of eighteen blocks in the
Progressa education context. Follow it or compare against it.

---

## Step 2 — Research each block

For each block in the scope, do live research. Do **not** use your memory for the products
that exist now.

1. **Start with the curated sources**, in the source map. The GovStack Building Block
   Software catalogue and the DPGA registry give candidates that somebody checked and that
   are relevant to a government.
2. **Then look wider.** Use the project sites and the sources that compare open-source
   products, to find options that the catalogues do not have yet.
3. **Record these seven items for each candidate**: the name; the model, which is OSS,
   Commercial, Open-core or DPG; whether GovStack lists it, and at which level; the
   maintainer or the backer; the evidence of real deployments in a government; the licence;
   and the lock-in vector, for a commercial or open-core product.
4. **Record the reality of the channel.** Some blocks, such as Payments and Messaging, depend
   on rails inside the country. These are mobile money and local SMS aggregators. You must
   integrate them, whichever platform you choose.

Make the effort fit the request. A question about one block can need one to three searches. A
landscape of 18 blocks can need eight to fifteen. Search for each block separately. One
combined query gives shallow results for each block.

---

## Step 3 — Reason about the sourcing posture of each block

Apply the scale of four from `build-vs-buy.md`. Give these four items for each block:

- the **recommended posture**: Reuse-OSS, Reuse-Commercial, Configure or Custom-build;
- **why**: the one or two factors that decided it, which are market maturity, fit,
  sovereignty or lock-in;
- the **lock-in risk**: Low, Medium or High, with the vector named;
- the **contribution to the bespoke footprint**: does this block add custom code?

These are the four postures, in the order of preference:

1. **Reuse-OSS** — a mature DPG or open-source product fits. Procure a system integrator to
   deploy it and operate it. *This is the default for Identity, Payments, Data Exchange,
   Registries, Analytics and GIS.*
2. **Reuse-Commercial** — a commercial product or channel that you source competitively is
   the realistic route. This is usually for a competitive layer at the edge, such as
   biometric devices, SMS, mobile money, or qualified trust services. These fit into an open
   core.
3. **Configure** — no product dominates the category. Give the capability as a configured
   feature of an adjacent block, for example Consent on the Information Mediator, or a
   Scheduler through Workflow. *Specify open APIs, or the feature becomes a custom build with
   no decision.*
4. **Custom-build** — this posture needs a named requirement that no product and no
   configuration meets. Each recommendation to build raises the flag for the bespoke
   footprint.

---

## Step 4 — Assemble the output

Write the provenance header first (`references/provenance-header.md`), then the analysis.

This is the default structure. Adapt it to the purpose of the decision.

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

**Text in, text out.** Write markdown tables and sections with headings, in the chat. Never
make a file, a `.docx`, a chart or an image. Play 4.4 must paste this output into the
sourcing matrix. Posts, not names. Write no analysis before the header. See
`references/output-contract.md`.

---

## Step 5 — Hand-off and adjacency

- **To `ea-cost-case`**: when each block has a posture, the cost case turns reuse, configure
  and custom into a siloed-versus-shared TCO. The sourcing posture is the *input* to the cost
  model. It is not a copy of it. Do not calculate costs here.
- **From `bdat-assessor` and `paera-reference-check`**: their gap findings and portfolio
  findings tell you which blocks exist, and which blocks are truly missing. Extend a block
  that exists. Do not buy it again.
- **With `country-context-pack`**: take the vendors that are present in the country, the
  mobile-money rails, and the data-residency law. They support your judgement on whether a
  vendor is available in this country.

---

## Anti-patterns to flag in any analysis

- **The bespoke trap** — to build something that a product already covers. It increases
  fragmentation and the future cost of legacy systems. To prevent this is the most important
  purpose of this skill.
- **A generic ESB as the mediator** — to choose a generic enterprise service bus instead of
  an Information Mediator in the style of X-Road. This makes point-to-point integration again,
  and it has no envelope for security and audit.
- **Silent drift from configure to custom** — a block with the label "configure" that becomes
  a bespoke build that nobody decided to fund, because nobody applied the discipline of open
  APIs.
- **A SaaS product against the sovereignty rules** — to recommend a commercial cloud SaaS
  product where the data-residency law or the sovereignty policy forbids it.
- **The catalogue as an endorsement** — to use a GovStack listing as a score for quality, or
  to use absence from the catalogue to remove a product.
- **Vendors from memory** — to name a product or a compliance level from training data and
  not from live research. Always research. Always cite.

---

## Caveats to include each time

1. The description of a vendor gives its general position in the market at the time of the
   research. Confirm it against the live procurement terms before any sourcing decision.
2. This is an options analysis. It is not a procurement recommendation. It does not replace a
   full business case or a feasibility study.
3. Product markets move quickly, and the markets for Digital Wallet and for AI/ML move
   fastest. Do the research again if the analysis is more than a few months old.
4. A verdict of "reuse" still needs real work to implement: configuration, integration and
   operation. Reuse makes the cost and the risk smaller. It does not remove them.

---

## Reference files

- `references/research-method.md` — the list of 18 blocks, the source map, the search
  patterns, and the maturity priors.
- `references/build-vs-buy.md` — the scale of four postures, the taxonomy of lock-in, and the
  rules for reasoning.

### Fixture material

- `references/worked-example.md` — a full analysis of eighteen blocks in an education
  context. Three blocks reuse a national system that already exists.

  Progressa is the fictional demonstration country that each play shares. The canonical
  description is `tests/progressa.md` in the kit repo.

### The shared contract

- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` ·
  `references/workbook-chain-kp2.md` — read them before you write the output. They are the
  same five files that each skill in this kit obeys.

Read these files when you need the detail in them. For a subject that they do not cover, do
live research and cite it.
