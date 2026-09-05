---
name: govstack-cost-estimator
description: Use this skill whenever a user wants to estimate, compare, or analyze costs related to GovStack building blocks — especially the comparison between siloed (each programme builds its own) vs. shared (whole-of-government) digital infrastructure. Trigger on any mention of GovStack, digital public infrastructure (DPI), building blocks, shared services cost analysis, identity/payments/data-exchange cost comparison, programme duplication analysis, whole-of-government approach, or digital transformation ROI. Also trigger for: total cost of ownership (TCO) modelling of government systems, lifecycle cost of digital government platforms, replacement-cycle risk for legacy government systems, bespoke vs. COTS vs. low-code sourcing decisions in government, risk-adjusted comparisons of big-bang vs. phased digital modernisation, vendor lock-in cost exposure, policy-as-code / change-cycle costing, and bespoke code footprint as a cost KPI. Essential for GovTech advisors, donors, government CIOs/CTOs, development partners, and ministerial briefings on digital transformation business cases.
---

# GovStack Building Block Cost Estimator

A reasoning skill for estimating the cost difference between:
- **(A) Siloed approach** — each government programme builds its own identity, payments, and data-exchange components
- **(B) Shared GovStack-aligned approach** — all programmes consume a common set of building blocks

---

## Step 0 — Gather Context First

Before any cost modelling, elicit the following from the user. Ask for all missing items in ONE message:

| Parameter | Why it matters |
|---|---|
| **Number of programmes** | Determines duplication multiplier in Scenario A |
| **Country/region context** | Affects labour costs, vendor market, existing DPI maturity |
| **Building blocks in scope** | Identity, Payments, Information Mediator, or all three (+others) |
| **Time horizon** | 5-year TCO is the minimum credible window; 10–15 years captures the replacement cliff and is strongly recommended for legacy modernisation cases |
| **Scale** | Number of citizens/transactions served; affects shared-infra unit cost and the elastic-vs-peak provisioning gap |
| **Existing legacy systems?** | If programmes already run legacy monolithic systems, Scenario A must include replacement-cycle costs, not just steady-state ops |
| **Sourcing assumptions per BB** | Build / buy / configure stance for each BB — defaulting to one stance across the stack is a common costing error |
| **Workload profile** | Steady vs. spiky (e.g. seasonal filing, monthly disbursement, emergency surge) — drives infrastructure provisioning model |
| **Expected policy change frequency** | How often do rules/eligibility/regulations change? Drives the marginal-cost-per-change line item |
| **Budget data available?** | If user has actual figures, use them; otherwise use reference benchmarks below |

If the user has already provided most context, proceed directly — don't re-ask what's already answered.

---

## Step 1 — Load Building Block Reference Data

Read `/mnt/skills/user/govstack-cost-estimator/references/building-blocks.md` for:
- Canonical GovStack BB descriptions and scope
- Typical build-vs-buy cost ranges (low/mid/high income country tiers)
- Key cost drivers per BB

Read `/mnt/skills/user/govstack-cost-estimator/references/cost-model.md` for:
- Full TCO formula and cost components
- Shared-infrastructure amortization logic
- Typical savings ranges from literature

---

## Step 2 — Model Scenario A (Siloed)

For each programme × each building block in scope, estimate:

```
Siloed_Cost(prog, bb) = 
    Build_Cost(bb, country_tier) × (1 + bespoke_premium)
  + Annual_Ops_Cost(bb, country_tier) × peak_provisioning_factor × years
  + Integration_Cost(bb)                                    # per programme, per BB
  + Change_Cycle_Cost(bb) × n_policy_changes_per_year × years
  + Replacement_Cost(bb) × replacement_probability(horizon)  # see lifecycle modelling
```

**Total Scenario A** = Σ over all programmes and BBs

**Key multipliers to call out:**
- Duplicated build: each programme pays full build cost
- Duplicated ops: each programme runs own infra/team
- No interoperability: integration costs are additive, not shared
- Security/compliance overhead per silo
- **Replacement cliff**: monolithic systems built bespoke typically enter a crisis state at year 10–15, with replacement projects running 2–3× original estimates and a multi-year dual-running period that effectively doubles operational cost during transition. For horizons >10 years, this must be modelled — see cost-model.md
- **Bespoke premium**: each percentage point above the 20% Bespoke Footprint target carries higher per-year maintenance cost and key-person risk
- **Peak provisioning**: on-premise systems sized for peak demand sit underutilised most of the time; elastic cloud-native deployment lets capacity scale to actual demand

---

## Step 3 — Model Scenario B (Shared GovStack)

```
Shared_Cost(bb) = 
    Build_Cost(bb, country_tier) × (1 + setup_premium)         # one-time, shared
  + Annual_Ops_Cost(bb, country_tier) × scalability_factor × elastic_factor × years
  + Platform_Governance_Cost × years                            # coordination overhead
  + Integration_Cost(bb) × N_programmes × reduction_factor      # APIs vs full builds
  + Change_Cycle_Cost(bb) × n_policy_changes_per_year × config_dividend × years
  + Lock_in_Exit_Reserve(bb)                                    # contingent cost, see below
```

**setup_premium**: 1.2–1.5× for enterprise-grade shared service setup  
**scalability_factor**: 0.3–0.6× (shared infra doesn't scale linearly)  
**elastic_factor**: 0.5–0.8× for cloud-native shared deployment vs. peak-provisioned siloed (spiky workloads gain most)  
**reduction_factor**: 0.15–0.25× (API integration vs full build per programme)  
**config_dividend**: 0.1–0.3× for BBs where policy is expressed as configurable rules rather than embedded in code  
**Platform_Governance_Cost**: ~10–15% of shared BB annual ops  
**Lock_in_Exit_Reserve**: budgeted contingency for vendor switching at year 5–7 — see cost-model.md

**Total Scenario B** = Σ over all BBs (not per programme)

---

## Step 4 — Calculate Savings and Present Results

```
Gross_Savings = Total_A - Total_B
ROI = Gross_Savings / Total_B × 100%
Break_even_year = year where cumulative B costs < cumulative A costs
```

**For credible decision-making, compute risk-adjusted Expected Value** alongside point estimates:

```
EV(scenario) = Σ [ probability(outcome) × Cost(outcome) ]
```

This is especially important when comparing big-bang implementation against phased delivery. Big-bang ITAS-style replacements have a documented failure rate; a phased 3–6 month delivery approach typically beats big-bang on EV once failure probability is priced in, even when its base-case coordination cost is higher. See cost-model.md → Risk-Adjusted Scenario Comparison.

Present results as:
1. **Executive summary table** (A vs B total, savings, ROI, break-even)
2. **Per-building-block breakdown** showing where most savings come from
3. **Sensitivity analysis** — what if programmes = N±2? what if ops costs differ? what if policy change frequency doubles?
4. **Risk-adjusted view** — point estimate vs. EV for both scenarios, with explicit failure-probability assumptions
5. **Bespoke Footprint projection** for each scenario (target: <20%)
6. **Non-financial co-benefits** (see reference file)
7. **Assumptions and caveats** — always explicit, always last

---

## Step 5 — Reasoning Principles

When making the case for shared BBs, always ground arguments in GovStack's documented rationale and broader enterprise architecture evidence:

**On lifecycle cost**
- **Price the full lifecycle, not the build**: The cost of a government system is not its implementation cost but its total cost of ownership over its lifetime. Cost models that stop at go-live systematically undervalue sustainable architectures
- **Model the replacement cliff**: Monolithic bespoke systems typically work well for 5–10 years, enter a crisis state by year 10–15, and then require replacement programmes that run 2–3× original estimates with a multi-year dual-running period. Any horizon beyond 10 years must include a probability-weighted replacement cost
- **Maintenance is the long tail**: Build costs are visible; ops costs over 5–7 years typically dwarf them. Shared ops is the primary savings driver

**On sourcing and code discipline**
- **Treat bespoke code as a measurable liability**: Track Bespoke Footprint (lines of custom code / total lines in production) as a KPI with a <20% target. Each percentage point above target carries higher maintenance cost, slower change cycles, and higher key-person risk
- **Distinguish commodity from differentiating capabilities**: Apply build/buy/configure decisions per BB based on strategic character — not a single sourcing stance across the stack. Commodity capabilities (case management, generic workflow, document management) should be configured on COTS/low-code platforms; differentiating capabilities may warrant bespoke build
- **Quantify the configuration dividend**: Where commodity capabilities are delivered on low-code or COTS platforms (rather than bespoke), expect ~80% reduction in custom code volume vs. equivalent bespoke ITAS-style builds — with corresponding reductions in maintenance burden, change cycle time, and TCO

**On hidden cost categories**
- **Price vendor lock-in as a contingent cost**: Include an exit/portability scenario — what does it cost to switch in year 7? — rather than treating procurement as a one-shot decision. Lock-in is a financial risk when vendors raise prices, discontinue support, or pursue incompatible directions
- **Use elastic, demand-shaped infrastructure assumptions**: Government workloads are often spiky (filing seasons, monthly disbursement, emergency surge). On-premise systems must be provisioned for peak; cloud-native systems scale to actual demand. Flat-utilisation cost-per-transaction models systematically understate cloud
- **Cost in the change cycle, not just steady-state ops**: Track marginal cost per policy change as a distinct line item. Where rules and policy are expressed as configurable code (rules engine, policy-as-code), change cost is configuration cost rather than full SDLC cost — and this compounds over 10–15 years
- **Integration is a first-class line item**: Cross-system integration is routinely under-budgeted. Track integration points as a discrete cost driver; siloed point-to-point integration scales as N(N-1)/2, while shared mediation scales as N

**On delivery and risk**
- **Phased vs. big-bang must be compared on risk-adjusted terms**: Big-bang replacement of legacy systems has a documented failure pattern — multi-billion overruns, revenue or service disruption. Phased delivery (3–6 month increments) typically beats big-bang on expected value once failure probability is priced in, even when base-case coordination cost is higher

**On the shared-infrastructure case**
- **Avoid duplication**: Traditional siloed approaches result in each programme building the same capability from scratch — identity verification, payment rails, data-exchange adapters are near-identical needs
- **Interoperability compounds value**: When all programmes share the Information Mediator BB, cross-programme data flows are enabled at marginal cost — invisible in siloed models
- **Security and trust**: Siloed identity and payment systems create fragmented attack surfaces; shared infrastructure concentrates security investment
- **Whole-of-government narrative**: Frame savings not just as line-item reductions but as freed budget for programme-level service delivery

---

## Step 6 — Output Format

Default output structure (adapt to user's needs):

```
## GovStack Building Block Cost Comparison
### Scenario A: Siloed — [N] Programmes, [X] Years
### Scenario B: Shared GovStack — [N] Programmes, [X] Years
### Summary: [Savings] | [ROI]% | Break-even: Year [Y]

### Per-Building-Block Analysis
| Building Block | Scenario A | Scenario B | Savings |
|---|---|---|---|
| Identity        | $X         | $Y         | $Z      |
| Payments        | $X         | $Y         | $Z      |
| Info. Mediator  | $X         | $Y         | $Z      |
| **Total**       | **$X**     | **$Y**     | **$Z**  |

### Lifecycle View ([X]-year horizon)
- Build / one-time: $X (A) vs $Y (B)
- Ops + governance, cumulative: $X (A) vs $Y (B)
- Change-cycle cost ([n] policy changes/yr): $X (A) vs $Y (B)
- Replacement-cliff exposure: $X (A) vs $Y (B) [if horizon ≥10yr]
- Integration: $X (A) vs $Y (B)

### Risk-Adjusted View
| Scenario | Point estimate | EV (risk-adjusted) | Failure probability assumed |
|---|---|---|---|
| A (siloed, big-bang) | $X | $X' | p% |
| B (shared, phased)   | $Y | $Y' | p% |

### Bespoke Footprint Projection
- Scenario A: ~[X]% bespoke (above 20% target → review trigger)
- Scenario B: ~[Y]% bespoke

### Non-Financial Benefits
[bullet list]

### Key Assumptions
[explicit list, including: sourcing stance per BB, workload profile, policy change frequency, failure-probability estimates, lock-in exit scenario]
```

If the user needs a visual, create an artifact (bar chart or table) using the React chart libraries.

---

## Important Caveats to Always Include

1. Cost estimates are illustrative — actual figures require country-specific procurement data
2. Scenario B requires political will and cross-ministry coordination — transition costs are real
3. Shared infrastructure has single-point-of-failure risk; mitigated by proper SLAs and redundancy
4. If a programme has unique/specialized needs, a building block may not cover 100% of requirements
5. Benchmark figures for the configuration dividend (~80% bespoke code reduction on COTS/low-code), replacement overruns (2–3× original estimate), and Bespoke Footprint targets (<20%) are reference values drawn from enterprise architecture literature and GovStack case studies — use as defensible defaults but disclose as estimates, not country-specific data
6. Failure probabilities used in risk-adjusted EV calculations are judgement-based; sensitivity-test them explicitly
7. These estimates do not replace a full feasibility study or business case

---

## Reference Files

- `references/building-blocks.md` — GovStack BB catalogue with cost benchmarks
- `references/cost-model.md` — Full TCO model, formulas, and literature-based ranges
