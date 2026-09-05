# The GovStack cost model — the TCO formulas and the method

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

**The key insight**: across a short period, the operations cost is the largest cost. Across 10 to 15 years, the replacement cliff and the change-cycle costs are frequently the largest, and a siloed bespoke architecture carries most of them.

### The Lifecycle Principle

The cost of a system is its total cost of ownership across its life. It is not the cost to implement the system. A team can implement a system quickly, and the system then needs much maintenance. That system costs more than a system that takes longer to implement and that a team can sustain. A cost model that stops at the go-live date, or at three years, always gives an architecture that a team can sustain a value that is too low.

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

When the programmes do NOT use a shared Information Mediator, each programme must integrate directly with each other programme to exchange data. Use the formula for a network:

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

1. **Duplicate management of the beneficiaries**: each programme maintains its own database of beneficiaries. To compare two databases needs a manual process or a bespoke integration. The estimated cost is $50K to $300K for each project that compares them
2. **Losses to ghost beneficiaries and to fraud**: without a shared identity, one beneficiary is in more than one database frequently. The World Bank estimates that a country with no shared ID loses 10% to 30% of its social transfers. This is a cost of the programme and not a cost of the IT, but you must record it
3. **The overhead of the procurement**: each programme selects its own vendor. The approximate cost is 3% to 8% of the value of the contract, in the time of the staff and in consultants
4. **Fragmentation of the knowledge**: the IT team of each programme solves a problem that another team already solved. The estimated cost is 6 to 12 more months for each programme, to implement identity and payments
5. **Fragmentation of the security**: N separate systems give N separate surfaces to attack, and N separate audits
6. **The replacement cycle, in year 10 to year 15**: a siloed bespoke system usually reaches a crisis in year 10 to year 15. A replacement programme costs 2 to 3 times its first estimate, and the country must operate both systems for some years. In an analysis across a long period, this is the largest cost that people do not see. See the section on the model for the replacement of the lifecycle, below
7. **The premium to maintain bespoke code**: each percentage point of the bespoke footprint above the target of 20% adds maintenance work each year, makes each change slower, and creates a dependency on one person. When the staff change, the knowledge of the custom code is lost
8. **The waste from provisioning for the peak**: a siloed system on the premises must have the size of the peak demand. Some workloads have short peaks, such as a filing season, a monthly disbursement, or an emergency. Outside the peak, these systems frequently use less than 30% of their capacity
9. **The drag of the change cycle**: a team can put the rules in the operational code, or express them as a policy that a person configures. When the rules are in the code, each change in the law or the regulation needs a full development cycle: change the code, test it, deploy it. Across N programmes, each change happens N times

---

## Lifecycle Replacement Modelling

For horizons ≥10 years, replacement-cycle costs become a material part of Scenario A.

### Observed pattern in monolithic bespoke systems

- **Years 0–5**: Initial build delivers value; user satisfaction high
- **Years 5–10**: Feature creep accumulates; complexity grows; change cycles slow
- **Years 10–15**: Crisis state — replacement is discussed but blocked by complexity
- **The replacement programme**: a government expects 3 years. The programme takes 7 to 10 years, and it costs 2 to 3 times the first estimate
- **The period when both systems operate**: the old system and the new system both operate. This makes the annual operations cost two times larger during the transition

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

A shared architecture can move the replacement cliff later, or make it much smaller. Such an architecture follows GovStack, has a low bespoke footprint, and separates its domains into modules. A team can replace one component at a time, and the other components continue to operate. To show this, make `p_replacement` 40% to 60% smaller in Scenario B.

---

## Bespoke Footprint as a Cost KPI

Track Bespoke Footprint as a measurable proxy for long-term cost exposure:

```
Bespoke_Footprint = lines_of_custom_code / total_lines_in_production
```

**Targets and triggers**:
- Target: <20% across the platform
- The trigger for a review is above 25%. Then find why a team writes code instead of configuring a product or buying one
- Crisis indicator: >50% (high replacement-cliff risk)

**How the footprint couples to the cost**: model each percentage point of the bespoke footprint above 20% as about 1% to 2% more maintenance cost each year for that component. It also makes the risk in the replacement cycle come sooner.

**Typical footprints by sourcing approach**:
- Pure bespoke ITAS / monolithic build: 80–95% bespoke
- A commercial product with many customisations: 50% to 70% bespoke. This gives both problems: the upgrades of the vendor are difficult, and the team must maintain the custom code
- COTS configured + minimal custom integration: 5–15% bespoke
- Low-code platform + custom integrations only: 5–10% bespoke
- Open-source DPG (MOSIP, X-Road, Mifos) + local configuration: 10–25% bespoke

---

## The Configuration Dividend

A team can deliver a commodity capability on a commercial product or a low-code platform, and not as a bespoke build. Then expect much less custom code, and expect the benefits below in the TCO:

- **About 80% less custom development**: a bespoke implementation of a commodity capability usually needs more than 50,000 lines of custom code. The same capability on a low-code platform needs fewer than 5,000 lines, and most of those lines integrate the legacy systems
- **A faster change cycle**: a change to a workflow needs weeks of development on a bespoke system. On a low-code platform it needs hours of configuration
- **An upgrade is easier**: the vendor of the platform maintains the framework below, and the configurations continue to work in the new version
- **Less risk from one key person**: more people can configure a platform than can maintain bespoke code

**When to apply the configuration dividend**:
- For a commodity capability, apply the full dividend. The commodity capabilities are case management, generic workflow, document management, intake forms and dashboards
- For a differentiating capability, do NOT apply the dividend. These are the capabilities where deep knowledge of the domain creates an asset, and a bespoke build can be the correct decision

This difference is important. One sourcing assumption across the full stack always makes the cost of a commodity domain too high. It can also make the cost of a differentiating domain too low, or put the strategic effort in the wrong place.

---

## Lock-In Exit Reserve

Lock-in to a vendor is a financial cost that can occur. A procurement is not one decision at one time. Across 10 to 15 years a vendor can increase its prices or stop a product. Another company can buy the vendor. The vendor can also move in a direction that the organisation cannot use.

**The recommended approach**: put a reserve in the budget, to change the vendor in year 5 to year 7.

```
C_lockin_exit = C_build_original × portability_difficulty × switch_probability
```

**portability_difficulty**:
- Use 0.15 to 0.25 for a system with strong open standards, documented APIs and data formats that a team can export
- 0.30–0.50 for COTS systems with partial standards compliance
- 0.60–1.00 for proprietary systems with custom data formats or restrictive contracts

**switch_probability over 10 years**:
- DPG / open-source with active community: 0.10–0.20
- Commercial COTS with multi-vendor market: 0.20–0.35
- Single-vendor proprietary: 0.40–0.60

A shared scenario that follows GovStack makes both factors smaller. The API contract is the boundary of the vendor. The strategy uses more than one vendor, because, for example, Case Management runs on several low-code platforms. The contract also has clauses for the portability of the data.

---

## Elastic vs. Peak-Provisioned Infrastructure

Government workloads are often spiky:
- Tax filing seasons (high concentration around deadlines)
- Monthly social transfer disbursement cycles
- Emergency cash transfer surges (disaster response, pandemic relief)
- Year-end and audit cycle peaks

**The penalty for provisioning for the peak**: a siloed system on the premises must have the capacity of the peak demand. Outside the peak it frequently uses 20% to 40% of that capacity. Therefore 60% to 80% of the capacity does nothing for most of the year.

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

For a workload with short peaks, apply this factor and the scalability_factor together in Scenario B. The two savings add together. A shared infrastructure has fewer peaks at the same time across the programmes. Elastic scaling gives the capacity for a peak only when the peak happens.

---

## Change-Cycle Cost Modelling

A government system changes continuously: the policy, the eligibility rules, the regulation and the procedure. The cost of one more change is very different in each architecture:

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

**Across siloed programmes**: when each programme implements a change separately, one policy change that crosses the programmes costs N times more.

**Across 15 years, with 10 policy changes each year**: in a bespoke architecture, the cost of the change cycle can be more than the cost of the first build. In an architecture with a rules engine, it is a small part of that cost.

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

Scenario B costs more at the start, because of the setup_premium. It then costs less each year. The break-even point is the year when the total cost of B becomes less than the total cost of A.

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

Some decisions are about modernisation at a large scale: to replace everything at one time or to deliver in phases, and to use one vendor or several vendors. For these decisions, one number gives the wrong answer. Calculate the expected value:

```
EV(scenario) = Σ [ probability(outcome) × Cost(outcome) ]
```

### Big-bang vs. phased delivery

**Big-bang ITAS-style replacement** (siloed, monolithic):
- Base-case cost: $X
- Failure mode 1: the programme costs 2 to 3 times more and is 2 to 3 years late. The probability is 0.30 to 0.50
- Failure mode 2: project abandonment / restart — probability 0.10–0.25
- Service disruption cost (if failure during cutover): 0.5–2× annual ops cost

**Phased delivery** (3–6 month increments, e.g. GovStack-aligned modular rollout):
- Base-case cost: ~1.1–1.2× big-bang base case (higher coordination overhead)
- Failure mode: phase abandonment with isolated impact — probability 0.10–0.20
- The disruption to the service is usually small, because each phase deploys next to the legacy system and does not stop it

**When you price the probability of failure, the expected value usually prefers delivery in phases**, although its base case costs more. In real cases, a programme that replaced everything at one time cost 100% to 200% more than its estimate. Some governments stopped such a programme after more than 5 years and billions of dollars.

### Decision rule

When the expected value of delivery in phases is inside 20% of the single estimate for the big-bang approach, choose delivery in phases. The smaller variance alone is worth more than the premium that you pay to coordinate the phases.

### Worked logic

```
Big-bang:  EV = 0.5 × $100M + 0.3 × $250M + 0.2 × $400M = $205M
Phased:    EV = 0.85 × $115M + 0.15 × $160M = $122M
```

The estimate for the phased approach is $115M. It is 15% more than the estimate for the big-bang approach, which is $100M. But the expected value, adjusted for the risk, is 40% less.

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

**An important caveat**: these are reference ranges. The true saving depends on the context of the country, the efficiency of its procurement, and the political economy of the move to a shared service.

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

*Note: this example uses figures in the middle of the LMIC range. A true analysis needs the data of the country.*

---

## Presenting the Non-Obvious: The Information Mediator Effect

The most counter-intuitive saving comes from the Information Mediator. Without it:
- Each programme that needs to share data with others must build a custom integration
- With N=5 programmes: 10 integration pairs, each costing $60K–$150K in LMIC
- Total: $600K–$1.5M just for point-to-point plumbing, with no audit trail

With a shared Information Mediator:
- Each programme integrates one time to the hub: 5 integrations × $40K–$120K = $200K–$600K
- Plus: every future programme adds only 1 integration, not N-1

This is the compound interest of a shared infrastructure. With each new programme, the saving becomes larger.

---

## Transition Cost Awareness

Scenario B is not free of risk. Always flag:

1. **The cost to migrate**: a programme that has a legacy system for identity or payments must migrate it. This costs $200K to $1M for each programme, and the figure depends on how complex the system is
2. **The cost to coordinate**: the governance structures, the memoranda of understanding between the ministries, and the legal frameworks to share data. People make this figure too small frequently
3. **The political economy**: a ministry can refuse to give up the system that it calls its own. The work to manage that change is real work
4. **Adopt the blocks in phases. This is the strong recommendation**: a move to a shared infrastructure at one time has the same risks of failure as a replacement of an ITAS at one time. Most countries that succeeded deployed the shared blocks one after another, across 18 to 30 months, and each phase gave value on its own. Model the phased scenario when it applies. See the section above on the comparison of the scenarios, adjusted for risk

**The recommended frame**: give Scenario B as an investment with a payback period that you state. Do not give it only as a reduction of the cost. The words "shared digital infrastructure as DPI" move the conversation from the cost of the IT to a strategic asset of the country. For a minister, start with these three points: (1) the replacement cliff that the country avoids across 15 years; (2) the budget that this frees for the delivery of services; and (3) the advantage in the expected value, adjusted for risk, of a shared rollout in phases against a siloed procurement that happens at one time.
