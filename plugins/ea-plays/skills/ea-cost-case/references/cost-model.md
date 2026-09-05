# GovStack Cost Model — TCO Formulas and Methodology

---

## Total Cost of Ownership (TCO) Framework

### Cost Components

Every building block deployment has these cost components:

```
TCO(bb, scenario, years) =
    C_build          # One-time: design, develop/procure, configure, test
  + C_deploy         # One-time: cloud/server setup, data migration, go-live
  + C_ops × years    # Annual: hosting, maintenance, support team, monitoring
  + C_security       # Annual: security audits, pen testing, compliance
  + C_integrate      # One-time per programme: API integration effort
  + C_train          # One-time per programme: staff training
  + C_govern         # Annual (Scenario B only): platform governance overhead
  + C_change × n     # Annual: marginal cost of policy/rule changes (n per year)
  + C_replace × p    # Probability-weighted replacement cost (horizons >10yr)
  + C_lockin_exit    # Contingent: budgeted exit/portability reserve
```

### Typical Component Splits (% of 5-year TCO)

| Component | Siloed (A) | Shared (B) |
|---|---|---|
| Build / Procure | 25–35% | 15–20% |
| Deployment | 5–10% | 3–6% |
| Operations (5yr) | 40–50% | 35–45% |
| Security (5yr) | 5–10% | 8–12% (higher % but lower absolute) |
| Integration | 5–10% | 3–7% |
| Change cycle (5yr) | 5–12% | 1–4% (with policy-as-code) |
| Governance | — | 5–10% |

**Key insight**: Operations dominates short-term cost. Over a 10–15 year horizon, the replacement cliff and change-cycle costs often dominate — and these are exactly the costs that bespoke siloed architectures bear most heavily.

### The Lifecycle Principle

The cost of a system is its total cost of ownership over its lifetime, not its implementation cost. A system that is quickly implemented but creates long-term maintenance burden is more expensive than one that takes longer to implement but is sustainable. Cost models that stop at go-live or at a 3-year horizon systematically undervalue sustainable architectures.

For any government system intended to operate for 10+ years, model:
- The full O&M curve (which typically grows as the system accumulates complexity)
- The probability and cost of mid-life replacement
- The marginal cost of every policy change accumulated over the horizon
- The contingent cost of vendor switching

---

## Scenario A: Siloed Cost Model

### Formula

```
A_total = Σ_programmes Σ_BBs [
    (C_build_bb + C_deploy_bb) × silo_factor
  + C_ops_bb × years
  + C_security_bb × years
  + C_integrate_bb_per_prog
  + C_train_bb_per_prog
]
```

**silo_factor = 1.0** (each programme bears full build cost)

### Point-to-Point Integration Explosion (Information Mediator only)

If programmes are NOT using a shared Information Mediator, each needs to integrate directly with the others for data exchange. Use the network formula:

```
N_integrations = N_programmes × (N_programmes - 1) / 2
A_integration_pairs = N_integrations × C_integration_pair
```

| Programmes | Integration pairs |
|---|---|
| 3 | 3 |
| 5 | 10 |
| 8 | 28 |
| 10 | 45 |

This is often the most dramatic illustration of siloed cost escalation.

### Hidden Costs in Scenario A (often missed in initial estimates)

1. **Duplicate beneficiary management**: Each programme maintains its own beneficiary database. Cross-referencing requires manual processes or bespoke integrations. Estimated cost: $50K–$300K per cross-reference project
2. **Ghost beneficiary / fraud losses**: Without shared identity, duplicate beneficiaries are common. World Bank estimates 10–30% of social transfer leakage in countries without shared ID. This is a programme cost, not IT cost, but should be noted
3. **Procurement overhead**: Each programme runs its own vendor selection. Rough cost: 3–8% of contract value in staff time and consultants
4. **Knowledge fragmentation**: Each programme's IT team reinvents the wheel. Estimated cost: 6–12 additional months per programme for identity/payment implementation
5. **Security fragmentation**: N separate systems = N separate attack surfaces, N separate audit exercises
6. **Replacement cycle (year 10–15)**: Bespoke siloed systems typically enter crisis state at year 10–15. Replacement programmes overrun original estimates by 2–3× and require multi-year dual-running. This is the largest hidden cost in long-horizon analysis — see Lifecycle Replacement Modelling below
7. **Bespoke maintenance premium**: Each percentage point of Bespoke Footprint above the 20% target carries higher per-year maintenance load, slower change cycles, and key-person dependency. As staff turn over, knowledge of custom code is lost
8. **Peak provisioning waste**: Siloed on-premise systems must be sized for peak demand. For spiky workloads (filing seasons, monthly disbursement, emergency surge), utilisation outside peak windows is often <30%
9. **Change-cycle drag**: Where rules are embedded in operational code rather than expressed as configurable policy, every legal/regulatory change becomes a full SDLC cycle — code change, test, deploy. Across N programmes, every change is multiplied N times

---

## Lifecycle Replacement Modelling

For horizons ≥10 years, replacement-cycle costs become a material part of Scenario A.

### Observed pattern in monolithic bespoke systems

- **Years 0–5**: Initial build delivers value; user satisfaction high
- **Years 5–10**: Feature creep accumulates; complexity grows; change cycles slow
- **Years 10–15**: Crisis state — replacement is discussed but blocked by complexity
- **Replacement programme**: Expected 3 years, actually takes 7–10 years and costs 2–3× original estimate
- **Dual-running period**: Old and new systems both operational, effectively doubling annual ops cost during transition

### Probability-weighted replacement cost

```
C_replace_expected = C_original_build × overrun_factor × p_replacement(horizon)
                   + C_ops_annual × dual_running_years × p_replacement(horizon)
```

**Default parameters**:
- `overrun_factor`: 2.0–3.0 (use 2.5 as base)
- `dual_running_years`: 3–5 years
- `p_replacement(horizon)`:
  - Horizon 5 years: ~0.1
  - Horizon 10 years: ~0.35
  - Horizon 15 years: ~0.75
  - Horizon 20 years: ~0.95

Shared GovStack-aligned architectures with low Bespoke Footprint and modular domain separation can defer or substantially reduce replacement-cliff exposure, because individual components can be replaced incrementally without disrupting the whole system. Reflect this by reducing `p_replacement` by 40–60% in Scenario B.

---

## Bespoke Footprint as a Cost KPI

Track Bespoke Footprint as a measurable proxy for long-term cost exposure:

```
Bespoke_Footprint = lines_of_custom_code / total_lines_in_production
```

**Targets and triggers**:
- Target: <20% across the platform
- Review trigger: >25% (investigate why code is being written instead of configured/purchased)
- Crisis indicator: >50% (high replacement-cliff risk)

**Cost coupling**: Each percentage point of Bespoke Footprint above 20% can be modelled as a ~1–2% uplift on annual maintenance cost for that component, plus accelerated replacement-cycle risk.

**Typical footprints by sourcing approach**:
- Pure bespoke ITAS / monolithic build: 80–95% bespoke
- COTS heavily customised: 50–70% bespoke (worst of both worlds — vendor upgrade pain + custom maintenance)
- COTS configured + minimal custom integration: 5–15% bespoke
- Low-code platform + custom integrations only: 5–10% bespoke
- Open-source DPG (MOSIP, X-Road, Mifos) + local configuration: 10–25% bespoke

---

## The Configuration Dividend

Where commodity capabilities are delivered on COTS or low-code platforms (rather than bespoke), expect substantial reductions in custom code volume and corresponding TCO benefits:

- **~80% reduction in custom development**: Bespoke implementation of a commodity capability typically requires 50,000+ lines of custom code; equivalent delivery on a low-code platform requires <5,000 lines (primarily for custom integrations to legacy systems)
- **Faster change cycles**: Workflow changes that take weeks of SDLC effort on bespoke become hours of configuration on low-code
- **Reduced upgrade pain**: Platform vendor maintains the underlying framework; configurations remain compatible across versions
- **Lower key-person risk**: Configuration is more accessible to a wider talent pool than bespoke code maintenance

**When to apply the configuration dividend**:
- Commodity capabilities (case management, generic workflow, document management, intake forms, dashboards): apply full dividend
- Differentiating capabilities (capabilities where deep domain knowledge creates a competitive asset): do NOT apply — bespoke build may be the right choice

This distinction is critical: applying one sourcing assumption across the whole stack systematically overestimates cost in commodity domains and may underestimate cost (or misallocate strategic effort) in differentiating domains.

---

## Lock-In Exit Reserve

Vendor lock-in is a contingent financial cost. Procurement is not a one-shot decision; over a 10–15 year horizon, vendors may raise prices, discontinue products, be acquired, or pursue directions incompatible with the organisation's needs.

**Recommended approach**: Include a budgeted reserve for vendor switching at year 5–7 of the horizon.

```
C_lockin_exit = C_build_original × portability_difficulty × switch_probability
```

**portability_difficulty**:
- 0.15–0.25 for systems with strong open standards, documented APIs, exportable data formats
- 0.30–0.50 for COTS systems with partial standards compliance
- 0.60–1.00 for proprietary systems with custom data formats or restrictive contracts

**switch_probability over 10 years**:
- DPG / open-source with active community: 0.10–0.20
- Commercial COTS with multi-vendor market: 0.20–0.35
- Single-vendor proprietary: 0.40–0.60

Shared GovStack-aligned scenarios reduce both factors because of API contracts as vendor boundaries, multi-vendor strategies (e.g. Case Management can run on multiple low-code platforms), and contractual data portability clauses.

---

## Elastic vs. Peak-Provisioned Infrastructure

Government workloads are often spiky:
- Tax filing seasons (high concentration around deadlines)
- Monthly social transfer disbursement cycles
- Emergency cash transfer surges (disaster response, pandemic relief)
- Year-end and audit cycle peaks

**Peak provisioning penalty**: Siloed on-premise systems must be provisioned for peak demand. Off-peak utilisation is often 20–40%, meaning 60–80% of capacity sits idle most of the year.

**Elastic factor in cost modelling**:
```
C_ops_effective = C_ops_baseline × elastic_factor
```

| Workload profile | On-prem siloed (A) | Cloud-native shared (B) |
|---|---|---|
| Steady (flat utilisation) | 1.0× | 0.95× |
| Moderately spiky | 1.0× | 0.70–0.85× |
| Highly spiky (deadline-driven) | 1.0× | 0.50–0.70× |
| Surge-prone (emergency) | 1.0–1.3× | 0.40–0.60× |

Apply on top of the scalability_factor in Scenario B for spiky workloads. The savings stack: shared infra means fewer concurrent peak provisioning needs across programmes, AND elastic scaling means each peak is served only when it happens.

---

## Change-Cycle Cost Modelling

Policy, eligibility, regulatory, and procedural changes are continuous facts of life in government systems. Their marginal cost varies dramatically by architecture:

```
C_change_per_event = engineering_hours × hourly_rate + testing_overhead + deployment_overhead
```

**Typical cost per change**, by architecture:

| Architecture | Per-change cost (LMIC) | Per-change cost (UMIC) |
|---|---|---|
| Bespoke monolithic (rules embedded in code) | $30K–$80K | $60K–$200K |
| Bespoke with separated business logic | $10K–$30K | $25K–$80K |
| COTS configured | $5K–$15K | $10K–$40K |
| Policy-as-code / rules engine | $1K–$5K | $3K–$15K |

**Across siloed programmes**: every cross-cutting policy change is multiplied by N programmes if each implements it separately.

**Over a 15-year horizon at 10 policy changes/year**: change-cycle cost can exceed the original build cost for bespoke architectures, and be a small fraction of it for rules-engine architectures.

---

## Scenario B: Shared GovStack Cost Model

### Formula

```
B_total =
    Σ_BBs [
        (C_build_bb × setup_premium + C_deploy_bb_shared)    # shared build, one-time
      + C_ops_bb × scalability_factor × years                # shared ops
      + C_security_bb × years                                # centralized security
    ]
  + Σ_programmes Σ_BBs [
        C_integrate_bb_api × reduction_factor                # API integration (lighter)
      + C_train_bb_per_prog                                  # training still per-programme
    ]
  + C_governance × years                                     # platform coordination
```

### Key Parameters

**setup_premium** (enterprise-grade shared service setup):
- 1.2× if existing DPG software used (MOSIP, X-Road, Mifos)
- 1.35× if custom development needed
- 1.5× if regulatory/legal framework also needs to be built

**scalability_factor** (shared ops vs. siloed ops per programme):
- 0.25–0.35 at 5+ programmes (strong economies of scale)
- 0.35–0.50 at 3–4 programmes
- 0.50–0.65 at 2 programmes (minimal sharing benefit)

**reduction_factor** (API integration vs. full build):
- 0.10–0.20 for Identity BB (API call replaces entire identity module)
- 0.15–0.25 for Payments BB (API call replaces payment pipeline build)
- 0.05–0.15 for Information Mediator (once connected, marginal cost per data flow)

**Platform_Governance_Cost**:
- Small country (<5M pop, <5 programmes): $100K–$200K/year
- Medium (5–20M pop, 5–10 programmes): $200K–$400K/year
- Large (>20M pop, 10+ programmes): $400K–$800K/year
Includes: steering committee, API management team, SLA monitoring, dispute resolution

---

## Break-Even Analysis

Scenario B has higher upfront cost (setup_premium) but lower ongoing costs. Break-even is when cumulative B cost < cumulative A cost.

```
Year_0:  A = Σ build costs (all programmes)  |  B = shared build × setup_premium
Year_1:  A += Σ ops (all programmes)          |  B += shared ops + governance
...
Break-even year = min(t) where B_cumulative(t) < A_cumulative(t)
```

**Typical break-even ranges from literature and GovStack case studies:**
- 2 programmes: Year 2–3
- 3–5 programmes: Year 1–2
- 6–10 programmes: Within Year 1 (shared build often < combined siloed build)
- 10+ programmes: B may be cheaper even in Year 0

---

## Sensitivity Analysis Parameters

Always run at least two sensitivity scenarios:

| Variable | Low case | Base case | High case |
|---|---|---|---|
| N programmes | N-2 | N | N+3 |
| Ops cost factor | 12% of build/yr | 18% | 25% |
| Setup premium | 1.2× | 1.35× | 1.5× |
| Integration reduction | 0.20 | 0.15 | 0.10 |
| Scalability factor | 0.50 | 0.35 | 0.25 |
| Elastic factor (spiky workloads) | 0.85× | 0.70× | 0.55× |
| Time horizon | 3 years | 5 years | 7+ years (model replacement) |
| Policy changes per year | 5 | 10 | 25 |
| Replacement probability at year 10 | 0.20 | 0.35 | 0.55 |
| Bespoke Footprint (Scenario A) | 60% | 80% | 95% |
| Bespoke Footprint (Scenario B) | 8% | 15% | 25% |

---

## Risk-Adjusted Scenario Comparison

For decisions involving large-scale modernisation (big-bang replacement vs. phased delivery, single-vendor vs. multi-vendor), point estimates are misleading. Compute Expected Value:

```
EV(scenario) = Σ [ probability(outcome) × Cost(outcome) ]
```

### Big-bang vs. phased delivery

**Big-bang ITAS-style replacement** (siloed, monolithic):
- Base-case cost: $X
- Failure mode 1: severe overrun (2–3× cost, 2–3 year delay) — probability 0.30–0.50
- Failure mode 2: project abandonment / restart — probability 0.10–0.25
- Service disruption cost (if failure during cutover): 0.5–2× annual ops cost

**Phased delivery** (3–6 month increments, e.g. GovStack-aligned modular rollout):
- Base-case cost: ~1.1–1.2× big-bang base case (higher coordination overhead)
- Failure mode: phase abandonment with isolated impact — probability 0.10–0.20
- Service disruption: typically minimal (each phase deploys non-disruptively alongside legacy)

**EV comparison typically favours phased delivery once failure probability is priced in**, even though its base case is higher. Real-world cases show big-bang replacement programmes overrunning by 100–200% and sometimes being abandoned after 5+ years and billions in spend.

### Decision rule

When the EV of phased delivery is within 20% of the big-bang point estimate, phased delivery is the rational choice — the variance reduction alone is worth more than the coordination premium.

### Worked logic

```
Big-bang:  EV = 0.5 × $100M + 0.3 × $250M + 0.2 × $400M = $205M
Phased:    EV = 0.85 × $115M + 0.15 × $160M = $122M
```

The phased point estimate ($115M) is 15% higher than the big-bang point estimate ($100M), but the risk-adjusted EV is 40% lower.

---

## Literature-Based Savings Benchmarks

These are from GovStack documentation, World Bank, and development partner assessments:

| Context | Reported Savings | Source |
|---|---|---|
| India Aadhaar identity (shared vs. siloed) | 30–40% reduction in identity verification costs across programmes | World Bank / UIDAI |
| Estonia X-Road (whole-of-govt data exchange) | ~1,400 services using shared infrastructure; estimated 2% of GDP saved in efficiency | e-Estonia / Deloitte |
| Philippines PhilSys (MOSIP deployment) | Avoided duplication across 18+ agencies | GovStack / DPGA case study |
| Kenya Integrated Financial Management (payments) | 25–35% savings in G2P disbursement costs vs. siloed | World Bank Kenya |
| Generic GovStack estimate (3 BBs, 5 programmes, 5yr) | 40–65% TCO reduction in Scenario B vs. A | GovStack Initiative modelling |

**Important caveat**: These are reference ranges. Actual savings depend heavily on country context, procurement efficiency, and political economy of shared-service adoption.

---

## Worked Example (Reference)

**Context**: LMIC, 5 programmes, 3 BBs (Identity, Payments, Info Mediator), 5-year horizon

### Scenario A (Siloed)
| BB | Build (×5) | Ops (×5 prog, 5yr) | Integration | Total |
|---|---|---|---|---|
| Identity | $15M | $13.5M | $0.75M | $29.25M |
| Payments | $12.5M | $9.4M | $0.63M | $22.53M |
| Info Mediator | $9M | $5.4M + pair integrations | $7.5M (10 pairs × $750K) | $21.9M |
| **Total A** | | | | **$73.7M** |

### Scenario B (Shared)
| BB | Build ×1.35 | Shared Ops (5yr, 0.35×) | Integration (5 prog) | Total |
|---|---|---|---|---|
| Identity | $4.05M | $2.36M | $0.75M | $7.16M |
| Payments | $3.38M | $1.65M | $0.63M | $5.66M |
| Info Mediator | $2.43M | $0.95M | $0.38M | $3.76M |
| Governance (5yr) | — | $1.5M | — | $1.5M |
| **Total B** | | | | **$18.08M** |

**Savings**: $55.6M (75% reduction)  
**ROI**: 307%  
**Break-even**: Year 1

*Note: This example uses mid-range LMIC figures. Real analysis requires country-specific data.*

---

## Presenting the Non-Obvious: The Information Mediator Effect

The most counter-intuitive saving comes from the Information Mediator. Without it:
- Each programme that needs to share data with others must build a custom integration
- With N=5 programmes: 10 integration pairs, each costing $60K–$150K in LMIC
- Total: $600K–$1.5M just for point-to-point plumbing, with no audit trail

With a shared Information Mediator:
- Each programme integrates once to the hub: 5 integrations × $40K–$120K = $200K–$600K
- Plus: every future programme adds only 1 integration, not N-1

This is the "compound interest" of shared infrastructure — the more programmes, the more dramatic the saving.

---

## Transition Cost Awareness

Scenario B is not free of risk. Always flag:

1. **Migration costs**: Existing programmes with legacy identity/payment systems face migration effort ($200K–$1M per programme, depending on complexity)
2. **Coordination costs**: Governance structures, MOUs between ministries, legal frameworks for data sharing — often underestimated
3. **Political economy**: Ministries may resist surrendering "their" systems; change management is real
4. **Phased adoption is strongly recommended**: Big-bang transitions to shared infrastructure carry the same failure-mode risks as big-bang ITAS replacements. Most successful country implementations roll out shared BBs incrementally over 18–30 months, with each phase delivering standalone value. Model phased scenario explicitly when relevant — see Risk-Adjusted Scenario Comparison above

**Recommended framing**: Present Scenario B as an investment with a clear payback period, not just a cost reduction. The language of "shared digital infrastructure as DPI" helps move the conversation from IT cost to national strategic asset. For ministerial audiences, lead with: (1) the avoided replacement cliff over a 15-year horizon, (2) the freed budget for service delivery, and (3) the risk-adjusted EV advantage of phased shared rollout over siloed big-bang procurement.
