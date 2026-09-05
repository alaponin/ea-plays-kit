---
name: ea-lifecycle-method
description: >
  Guides an architect through a five-phase EA lifecycle -- Discover, Assess,
  Adapt, Plan (target + roadmap), Execute & Govern -- for digitalising any
  public-sector domain in any country: education, health, agriculture,
  social protection, tax, land, etc. Produces six deliverables: Discovery
  brief, ranked gap analysis, build/buy/share/sandbox sourcing matrix,
  target architecture, costed wave roadmap, governed EA -- the first four
  each ending in a sign-off question. Use for EA assessments; a Discovery
  brief, gap analysis, sourcing matrix, target architecture, or roadmap for
  a ministry/agency/registry; classifying bodies (policy unit / regulatory
  agency / service authority / state registry / shared platform); naming a
  sector's "stalled flagship" (a single patient/learner/farmer record a
  minister promised); or a build/buy/share governance gate. Triggers without
  phase names too, e.g. "map our health ministry's fragmentation."
  Complements paera-assessor, bdat-assessor, govstack-cost-estimator, bb-
  sourcing-researcher.

---

# EA Lifecycle Method

A five-phase method for taking any public-sector domain, in any country, from
a fragmented starting point to a living, governed architecture. It was proven
on a worked education-sector example (institutions renamed for
demonstration purposes) and is written here stripped to what transfers to any
sector: health, agriculture, social protection, tax, land, or anything else
you are handed.

## The method at a glance

| Phase | Question it answers | Deliverable(s) | Discipline | Typical duration |
|---|---|---|---|---|
| 1 — Discover | What exists today? | Discovery brief | Describe, do not recommend | 3–4 weeks |
| 2 — Assess | What is the gap, ranked? | Maturity scorecard + gap analysis | Judge honestly, including the political gaps | 6–8 weeks |
| 3 — Adapt | How will we source each piece? | Localised principles + build/buy/share/sandbox matrix | Reuse before build, buy before build | 4–6 weeks |
| 4 — Plan (design) | What does the future state look like? | Target architecture + integration map | Every element traces to a gap and a sourcing decision | — |
| 4 — Plan (sequence) | In what order, at what cost? | Wave-sequenced, costed roadmap | The minister's promised outcome lands early, not last | 6–8 weeks |
| 5 — Execute & Govern | How does reuse keep happening? | Living repository + binding Board + review gate | Runs forever | Ongoing |

**One rule holds the whole thing together: the order is not optional.**
Discover before you judge. Judge before you adapt. Adapt before you design
the target. Design the target before you sequence the roadmap. Govern,
always, once the roadmap starts landing. Skipping ahead — designing a target
before the gaps are ranked, or sequencing a roadmap before the target is
signed off — produces a plan built on assumptions nobody checked.

Four of the five phases end in a formal sign-off: a specific yes/no question
put to a named senior decision-maker (a minister, a digitalisation officer,
an EA Board). The sign-off is not a status update — it is the gate that
keeps a wrong picture, a softened gap, an undebated sourcing call, or an
unfunded roadmap from quietly becoming the foundation the rest of the work
stands on.

---

## Before you start: scope the engagement

Ask (or infer from what the user has already told you):

1. **Which country and which sector?** The institutions and the duplicated
   data domain are the two things that change every time — get both named
   early. See `references/domain-transfer-guide.md` for the domain-analogy
   table (learner → patient → farmer → beneficiary → taxpayer) and the
   institution classification taxonomy.
2. **Where is the user in the lifecycle?** They may be starting fresh at
   Discovery, or they may already have a Discovery brief or gap analysis and
   want the next phase run against it. Don't restart a phase that's already
   been signed off — build on it.
3. **What decision-maker will sign off each phase?** Name them if possible
   (a minister, a permanent secretary, an EA Board chair) — the sign-off
   question in each phase should be addressed to a real role, not left
   generic.

If the user hands you findings from an earlier phase (a gap list, a
principle set, a sourcing matrix), treat those as given inputs and carry them
forward — do not silently re-derive them from scratch.

---

## Phase 1 — Discover

**Question:** What exists today? Not what's wrong — that's Phase 2.

**Collect five things**, each with a **source** (document, interview, or
system) recorded against every entry so the brief can be checked, not just
believed:

1. **Strategies in force** — the national digital strategy, the sector plan, and anything in draft/validation.
2. **Systems that exist** — one entry per system: what it does, who owns it, what platform it runs on.
3. **Registries and their owners** — every list that claims to record "who is an X" (a learner, a patient, a farmer), who owns each, and whether any two share a common key. Record duplication as a fact, not a verdict.
4. **Stakeholders** — the ministries with mandate, the agencies that deliver, the donors funding each piece, any existing coordination structure.
5. **Legal framework** — the mandate for each body, data-protection law status, any sector-specific consent or registration requirements.

**The discipline:** describe without recommending. If you catch yourself
writing "this should be fixed," that sentence belongs in Phase 2, not here.
Discovery records that three lists exist and who owns each — it does not yet
say that's a problem. Judgement mixed into Discovery biases the assessment
before the picture is complete.

**Use `country-context-data`** to gather public indicators, institutional
structures, and existing digital-identity/registry programmes for the
country if the user hasn't supplied primary documents.

**Output shape:** a Discovery brief organised under the five headings above,
one row per fact, with a Source column. See
`references/deliverable-templates.md#1-discovery-brief` for the exact table
format.

**Sign-off question:** *"Is this picture accurate enough to build on?"* —
not complete, not perfect, accurate. Addressed to the chair of the EA Board
or equivalent senior decision-maker.

---

## Phase 2 — Assess

**Question:** What is the gap between where the sector is and where it needs
to be — ranked?

**Step 1 — Score capability maturity** against a single-source-of-truth,
once-only standard (Low / Medium / High, or a finer scale if useful). Score
the core capabilities: register the person/object, prove identity, deliver
the core service, share data across bodies. Use `paera-assessor` for the
GovStack/PAERA-anchored scoring dimensions if the user wants that framework
explicitly.

**Step 2 — Name the gaps.** Look on purpose for the four that appear in
almost every first assessment of a fragmented sector:

- **Duplicate registries** — more than one list claims the same object, none authoritative.
- **An available platform not consumed** — a shared capability (identity, payment) exists elsewhere in government but this sector re-collects instead of reusing it.
- **No shared data exchange** — every link between bodies is point-to-point or paper, not a reusable backbone.
- **No clear owner** — everyone references "the record," nobody is accountable for the authoritative copy.

**Step 3 — Rank, don't just list.** For each gap, score severity (cost,
citizen burden, and whether it's the direct cause of the sector's stalled
flagship promise) against effort to close. The ranking — not the list — is
what later phases act on. A gap that's high-impact but hard to close (like
building a data-exchange backbone) sequences later, not lower in priority;
a gap that's high-impact *and* closable without waiting on anything else
(like designating one existing list authoritative) goes first.

**Step 4 — Flag the political gaps honestly.** If a gap involves a
powerful body that won't want to give up its own list, or split ownership
between two ministries with their own funded programmes, name it plainly at
this stage. Softening it here is the version that fails quietly, a year
later, when the flagship promise still hasn't landed.

**Output shape:** a maturity scorecard, a ranked gap table (gap / severity /
effort / priority), and an explicit honesty-flags section. See
`references/deliverable-templates.md#2-gap-analysis`.

**Sign-off question:** *"Does this gap analysis reflect ground truth —
including the parts that are politically uncomfortable?"*

---

## Phase 3 — Adapt

**Question:** How will each capability be sourced?

**Step 1 — Localise the principles.** Don't draft from scratch. Take a
reference principle set (PAERA's ten, or whatever framework the country has
adopted) and, for each principle, write one line pointing it at the
country's own law or rule (once-only → the data-protection act;
reuse-before-build → the procurement rules) plus a written implication the
Board can use to settle an argument later. Add any principle the context
specifically needs (e.g. offline access for low-connectivity areas) — but
only if it earns its place; don't pad the set.

**Step 2 — Make a deliberate sourcing call per building block.** Four kinds
of decision, each written down with a one-line reason:

- **BUILD** — reserved for the authoritative core nobody else can own (a new registry that doesn't exist as a shared block anywhere else).
- **SHARE** — consume an existing national platform (an identity authority, a payment switch, a data-exchange backbone) instead of building a parallel one, even if that platform isn't fully built yet — sharing the *intent* to consume it, sequenced correctly, still beats building a substitute nobody plans to retire.
- **BUY** — a solved market problem (exam management, workflow, messaging) where building would be reinventing a commodity.
- **SANDBOX** — a capability nobody is sure about yet (a new analytics use case, a consent model ahead of the law that will govern it) — pilot narrow before committing sector-wide.

**The default is reuse and share; build is the exception that must justify
itself.** Use `bb-sourcing-researcher` to find real market/DPG options for
BUY calls and assess lock-in risk. Use `govstack-cost-estimator` if the user
wants the cost comparison between siloed and shared sourcing made explicit.

**Output shape:** a localised principle table and a sourcing matrix (block /
call / reason), with any BUILD that risks duplicating an existing shared
block and any BUY that risks vendor lock-in flagged explicitly. See
`references/deliverable-templates.md#3-sourcing-matrix`.

**Sign-off question:** *"Are the localised framework and the sourcing
approach approved?"* This is a consequential gate — it commits the shape of
everything downstream. Skipping this deliberation means every future project
re-litigates build-versus-reuse on its own, which is the fragmentation the
whole exercise exists to prevent.

---

## Phase 4a — Plan: design the target architecture

**Question:** What does the future state look like, once the gaps are
closed?

Don't invent the target from imagination — design it by applying the
principles from Adapt to the gaps from Assess. Once-only says duplicate
lists collapse to one. Reuse-before-build says the sector consumes rather
than re-implements a shared platform. One-owner-per-domain resolves who owns
what. Draw the future state in the same four layers used for the current
state, but designed rather than observed:

1. **Target capability map** — each capability owned by exactly one body, duplicates resolved.
2. **Target data domains** — one authoritative owner per domain (the person, the object being registered, the certified outcome).
3. **Target shared platforms** — the identity platform, payment rail, and data-exchange backbone every body will consume.
4. **Target technology standards** — open APIs, no-legacy lifecycle limits, verification standards, and anything context-specific (offline tolerance, etc.).

**Add the integration map** — the artefact the current state never had:
which bodies exchange which data domains, over what mechanism, in what
priority order. This is a first cut; full interoperability design is later
work.

**One discipline keeps it useful: every element must be reachable.** Trace
each target element back to the gap it closes and forward to the sourcing
decision (build/buy/share) that obtains it. If an element has no path to
acquire it — a platform that's planned but unfunded, a legal basis that
doesn't exist yet — **flag it explicitly as a dependency**, don't silently
assume it into the design. A target with unflagged wishful elements is not
an architecture the roadmap can be built on.

**Output shape:** the four target layers plus the integration map, each
element carrying its gap-and-sourcing trace, with unreachable elements
flagged. See `references/deliverable-templates.md#4-target-architecture`.

**Sign-off:** designed together with the sourcing matrix from Adapt —
together they are the agreed destination the roadmap sequences toward.

---

## Phase 4b — Plan: sequence the roadmap

**Question:** In what order, at what cost, does the sector get from today to
the target?

**Sequence into waves.** The pattern that transfers:

- **Wave 1 — Inception:** stand up the repository and the Board; make the
  core registry authoritative (even if just seeded from an existing
  operational list); resolve any governance prerequisite the target flagged
  (an ownership mandate, a sanctioned interim mechanism).
- **Wave 2 — High-priority use case:** the one cross-cutting outcome the
  senior decision-maker has already promised — the sector's equivalent of
  "the single learner record" — landing inside the first year, not the
  fifth. This is usually achievable by having one or two consuming bodies
  read from the new authoritative registry and the shared identity source,
  even before the full backbone exists.
- **Wave 3 — Build-out:** the shared data-exchange backbone or other
  flagged-dependency platform gets funded and built; any interim mechanism
  from Wave 2 is retired into it.
- **Wave 4 — Mass scale:** every remaining service in the sector runs on
  the shared platforms.

Each wave must deliver something the decision-maker can **see**, not just
groundwork. Cost each wave honestly and directionally — enough for a
multi-year budget commitment, not a false-precision quote. Typical cost
drivers by wave: people (Wave 1), integration (Wave 2), platform (Wave 3),
platform + procurement at scale (Wave 4).

**The roadmap does double duty.** The decision-maker reads outcomes and
dates. The architects read a dependency sequence (you cannot do Wave 2
before the registry is authoritative in Wave 1). Same document, two
readings — write it so both land without translation.

**Output shape:** a four-wave table (deliverable / prerequisites / cost
driver) — see `references/deliverable-templates.md#5-wave-roadmap`.

**Sign-off question:** *"Does the Board approve this roadmap and commit the
budget?"* — ideally a multi-year envelope, not an annual line that has to be
re-fought every year. This is the most consequential of the four sign-offs;
approving it moves the sector from planning to building.

---

## Phase 5 — Execute & Govern

**Question:** How does reuse keep happening after this roadmap is
delivered? This phase never ends.

Three things make it real:

1. **The repository** — a single, current store of the architecture: the
   layers, the sourcing decisions, the principle set, the decision log. One
   named owner keeps it updated as each wave lands.
2. **The permanent team** — two to four architects who exist whether or not
   any single project is running. This is the sector's standing capacity
   for cross-cutting decisions, and it is the single most common point of
   failure: the practice dies when architects get pulled onto the urgent
   project of the week. Protect this team explicitly in the governance
   design, not as an afterthought.
3. **The review gate** — every new project that touches a domain already
   covered by a shared block gets asked the same few questions before it's
   allowed to build.

### Running a gate decision

When a new project proposes to build something, run this pattern (see
`references/deliverable-templates.md#6-gate-decision-log` for the full
template):

1. **Does a shared block already exist for what this builds?** Check the
   sourcing matrix and target architecture from Adapt/Plan.
2. **Which data domain(s) does it touch, and does it consume the owner's
   copy** rather than duplicating it?
3. **Does it meet the localised principles** from Adapt?
4. **Was the sourcing choice deliberate** — build/buy/share/sandbox, with a
   reason — or is it happening by default because reuse looked slower?

**Rule:** consume the shared block, or grant a **written exception** with an
explicit sunset date and reason. An exception is not a loophole — it is how
the method handles a real gap (a shared platform that's planned but not yet
built) without either stalling the project or letting an unreviewed
workaround become permanent. Every ruling — consume or exception — goes in
the decision log with its reason, so the next architect (or the next
project) knows why.

The Board should also meet on a standing cadence (quarterly is typical) with
the business side and the architects reviewing the same repository together
— this is the forum no single project can provide on its own, and it's what
keeps the architecture from freezing after the first delivery.

---

## Adapting the method to a new country or sector

**What changes every time:** the institutions, the duplicated data domain,
the specific gaps found, the political sensitivities. **What never
changes:** the five phases, the four sign-offs, the six deliverables, the
reuse-before-build default, and a Board with the authority to say no.

Use `references/domain-transfer-guide.md` for:
- The institution classification taxonomy (policy unit / regulatory agency / service-delivery authority / state registry / shared platform) with one-line definitions.
- A domain-analogy table across sectors (learner, patient, farmer, beneficiary, taxpayer) to help name the duplicated-registry problem quickly in a new sector.
- Guidance on which companion skill to reach for at each phase.

**Three things to carry into any new engagement, named explicitly at the
start of the work rather than discovered the hard way:**

1. **Start small.** Pick the one high-priority use case — the sector's
   equivalent of the single learner record — and land it in Wave 2, not
   Wave 4.
2. **Sign off honestly.** Including the politically uncomfortable gap. An
   assessment that flatters a powerful stakeholder fails quietly, later.
3. **Protect the team.** The architects need to survive contact with the
   urgent project of the week, or the practice dies before Phase 5 ever
   starts.

Once a country has run this lifecycle on one sector, the second sector is
cheaper than the first — the team, the localised principle set, and the
Board are already there. Only the institutions and the domain change.

---

## Reference files

- `references/deliverable-templates.md` — exact output formats for all six deliverables plus the gate-decision-log entry, ready to fill in for any sector.
- `references/domain-transfer-guide.md` — institution classification taxonomy, cross-sector domain-analogy table, and companion-skill guidance.

Read these when producing an actual deliverable — the templates keep every
sector's output in the same shape, which is what makes the method
comparable and reusable across a country's second and third sector.
