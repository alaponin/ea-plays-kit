# Deliverable Templates

Ready-to-fill formats for the six EA lifecycle deliverables plus the
recurring gate-decision-log entry used in Execute & Govern. Swap in the
country's institutions and the sector's data domain; keep the structure.

---

## 1. Discovery Brief

Rule at the top of every Discovery brief: **describe what is; do not
recommend. Recommendations belong to Assess.**

### 1.1 Strategies in Force

| # | Question | Format | Source |
|---|---|---|---|
| Title, owning body, date range, stated goal | national digital strategy | Document |
| Title, owning body, date range, stated priorities | sector strategy/plan | Document |
| Successor/draft strategies and their status | title, status, owning body | Document / interview |
| Who funds implementation and for how long | funder, amount if known, instrument | Document / interview |

### 1.2 Systems That Exist

| # | Question | Format | Source |
|---|---|---|---|
| What system holds the core "who is registered" data | system name, owning body, coverage | Interview / system |
| What system(s) deliver the core service | system name, owning body, scope | Interview / system |
| What system(s) manage identity | system name, owning body, capture rules | Document / interview |
| Is there a live (not planned) data-exchange platform | system name, status, what connects | Document / interview |
| Technology/hosting/vendor per system | platform, hosting, contract owner | Interview / system |

### 1.3 Registries and Their Owners

| # | Question | Format | Source |
|---|---|---|---|
| How many lists claim to record "who is an X," who owns each | list name, owner, record count, identifier | Interview / system |
| Who owns the identity registry, what identifier does it assign | owner, identifier format, coverage | Document / interview |
| Do any two registries share a common key today | yes/no per pair, the key | Interview / system |
| Is there a designated authoritative source for any attribute | attribute, system if any | Interview |

### 1.4 Stakeholders

| # | Question | Format | Source |
|---|---|---|---|
| Which ministries hold formal mandate | ministry, mandate area, accounting officer | Document |
| Which agencies deliver services within that mandate | agency, service, reporting line | Document / interview |
| Active donors/development partners and what they fund | donor, programme, counterpart, period | Document / interview |
| Existing cross-body coordination structures | name, membership, mandate, frequency | Interview |

### 1.5 Legal Framework

| # | Question | Format | Source |
|---|---|---|---|
| What law establishes each body's mandate | act/instrument, year, body | Document |
| Data-protection/privacy law status and requirements | act name, year, obligations, enforcer | Document |
| Registration legal requirements and penalty regime | citation, timeframe, penalty | Document |
| Cross-body data-sharing legal basis | citation, what it permits/restricts | Document |
| Sector-specific consent/access rules | citation or policy, who's authorised | Document / interview |

**Sign-off:** *"Is this picture accurate enough to build on?"*

---

## 2. Gap Analysis

### 2.1 Maturity Scorecard

| Capability | Maturity (Low/Med/High) | Why |
|---|---|---|
| Register the person/object | | |
| Prove identity | | |
| Deliver the core service | | |
| Track transitions/lifecycle | | |
| Share data across bodies | | |

### 2.2 Ranked Gap Table

| Rank | Gap | Severity (cost / burden / flagship link) | Effort to close | Priority |
|---|---|---|---|---|
| | Duplicate registries | | | |
| | Available platform not consumed | | | |
| | No shared data exchange | | | |
| | No clear owner | | | |

### 2.3 Honesty Flags

State plainly, for any gap touching a powerful stakeholder: which body,
what they stand to lose, and why softening the finding would fail later.
Don't resolve the politics here — name it for the decision-maker to act on.

**Sign-off:** *"Does this gap analysis reflect ground truth — including the
parts that are politically uncomfortable?"*

---

## 3. Sourcing Matrix

### 3.1 Localised Principles

| Principle | Local law/rule it's anchored to | Written implication for the Board |
|---|---|---|
| Once-only | | |
| Reuse-before-build | | |
| One-owner-per-domain | | |
| Whole-of-government / no silos | | |
| [context-specific addition, if earned] | | |

### 3.2 Sourcing Matrix

| Building block | Call (BUILD/BUY/SHARE/SANDBOX) | Reason |
|---|---|---|

### 3.3 Flags

- Any BUILD that duplicates an existing shared block.
- Any BUY that risks vendor lock-in (no API layer, no data-export clause, single-vendor dependency).
- Any SHARE call where the platform being shared doesn't fully exist yet — note it as a flagged dependency, not a clean call.

**Sign-off:** *"Are the localised framework and sourcing approach
approved?"*

---

## 4. Target Architecture

### 4.1 Target Capability Map

| Capability | Target owning body | Duplicate resolved |
|---|---|---|

### 4.2 Target Data Domains

| Domain | Target authoritative owner | Collapses |
|---|---|---|

### 4.3 Target Shared Platforms

| Platform | Owner | What the sector consumes from it |
|---|---|---|

### 4.4 Target Technology Standards

- Open APIs / open standards for every exchange.
- Exchange model (federated / centralised — state which and why).
- No-legacy lifecycle limit for any bought component.
- Verification/certification standard for the sector's core output.
- Any context-specific standard (offline tolerance, low-bandwidth design, etc.).

### 4.5 First-Cut Integration Map

| Priority | Exchange (body ↔ body, over what domain) | Mechanism | Gap it closes |
|---|---|---|---|

### 4.6 Gap-and-Sourcing Trace

For every element above:

| Target element | Closes gap | Sourcing decision | Path to obtain it | Flag if unreachable |
|---|---|---|---|---|

**Sign-off:** designed and approved together with the sourcing matrix — the
agreed destination the roadmap sequences toward.

---

## 5. Wave Roadmap

| Wave | Delivers (visible outcome) | Prerequisites | Cost driver |
|---|---|---|---|
| 1 — Inception | | — | People |
| 2 — High-priority use case | *(the sector's promised flagship outcome)* | Wave 1 | Integration |
| 3 — Build-out | | Wave 2 | Platform |
| 4 — Mass scale | | Wave 3 | Platform + procurement |

Note explicitly, for the Board: which wave lands the decision-maker's
promised outcome (should be Wave 2, inside the first year — not Wave 4).

**Sign-off:** *"Does the Board approve this roadmap and commit the
budget?"* — state whether a multi-year envelope or an annual line is being
requested, and recommend the envelope.

---

## 6. Gate Decision Log

Use this template every time a project proposes to build something that
might duplicate a shared block already named in the sourcing matrix or
target architecture.

### Gate Questions (answer each)

1. Does a shared block already exist for what this builds?
2. Which data domain(s) does it touch, and does it consume the owner's copy?
3. Does it meet the localised principles?
4. Was the sourcing choice deliberate?

### Ruling

State, per element the project proposes: **consume the shared block**, or
**grant a written exception** (sunset date + reason + governance owner of
the exception).

### Decision-Log Entry

> **Date:**
> **Decision:**
> **Reasoning:**
> **Exception granted to (if any):**
> **Sunset condition:**
> **Owner of the exception:**
> **Standing conditions:**
