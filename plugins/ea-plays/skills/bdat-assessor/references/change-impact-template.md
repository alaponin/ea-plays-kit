# Change-Impact Template: Tracing Cross-Layer Consequences

Use this template whenever the assessment involves a proposed change — a new building
block, a system retirement, a platform migration, a policy change — not just a
current-state description.

BDAT's most valuable use is not describing what exists. It is tracing what changes
when something new is introduced or something old is removed. This is where
architecture justifies investment decisions.

---

## When to Use This Template

- A new GovStack building block is being proposed (identity, payments, data exchange)
- An existing system is being retired or replaced
- A new platform or cloud provider is being adopted
- A policy change creates a new capability requirement
- A donor project proposes to build or procure a system
- A shared platform is being extended to a new sector

---

## The Change-Impact Trace

For any proposed change, trace consequences through all four layers — both downward
(what the change requires below) and upward (what the change enables above).

### 1. Name the Change

| Field | Content |
|-------|---------|
| Change | [What is being introduced or retired] |
| Initiating layer | [Which BDAT layer the change enters at] |
| Owner | [Which body is responsible for the change] |
| Trigger | [Policy decision, donor project, technology refresh, legal requirement] |

---

### 2. Downward Trace — What the Change Requires

Start at the layer the change enters and trace what it demands from each layer below.

**If the change is at the Business layer** (new policy, new capability mandate):
- Data: What new domains does this capability require? Who will own them?
- Application: What new applications are needed, or which existing ones must be extended?
- Technology: What infrastructure must be in place for the applications to function?

**If the change is at the Application layer** (new system, new building block):
- Data: What data domains does the new application use? Are they already owned by a named body, or does ownership need to be assigned?
- Technology: What infrastructure does the new application require? Is it already in place, or does it need to be procured or built?

**If the change is at the Technology layer** (new platform, new hosting, new backbone):
- Application: Which applications depend on the component being changed? What integration work is required?
- Data: Does the change affect how data is stored or exchanged? Are data standards preserved?
- Business: Does a technology constraint limit what capabilities can realistically be delivered? (Upward pressure — name it honestly.)

---

### 3. Upward Trace — What the Change Enables

Trace what the change makes possible in layers above.

| Layer | What is now possible that was not before |
|-------|------------------------------------------|
| Technology → Application | [Which applications can now be built or improved?] |
| Application → Data | [Which data flows are now possible or standardised?] |
| Data → Business | [Which capabilities are now supportable that were not?] |
| Business → Service | [Which citizen-facing services become deliverable?] |

---

### 4. Cross-Body Consequences

Changes rarely affect only one body. For each body in scope, note:

| Body | Impact | Action Required |
|------|--------|----------------|
| [Body A] | [How is it affected — consuming body, owning body, competing body?] | [What must it do — integrate, retire, hand over ownership?] |

---

### 5. Architecture Trap Check for This Change

| Trap | Assessment |
|------|-----------|
| **Bespoke trap** | Does this change duplicate a shared building block that already exists? If so, what is the case for building rather than consuming? |
| **Vendor-driven trap** | Does this change introduce a product that stores data in a proprietary format? Can the government exit within two years at reasonable cost? |

---

### 6. Enabling Conditions

Name what must be true for the change to be successfully implemented.
Theoretical benefits do not materialise if enabling conditions are absent.

| Condition | Status |
|-----------|--------|
| Legal basis for the new capability or data flow | [In place / Needed / Unknown] |
| Named owner for each affected data domain | [Named / Vacant / Disputed] |
| Governance board with authority to enforce cross-body data agreements | [Exists / Absent] |
| Technology infrastructure already in place | [Ready / Gap / Procurement needed] |
| Consuming bodies technically able to integrate | [Confirmed / Uncertain] |
| Recurrent funding for operations and maintenance | [Committed / Donor-dependent / Unknown] |

---

## Worked Example: Introducing a National Learner Registry

**Change**: Introduce a National Learner Registry (PLR) as a shared state registry,
where none currently exists. Each ministry and examination authority currently holds
its own partial learner list.

**Initiating layer**: Application (a new shared system is being introduced)
**Owner**: To be assigned — currently contested between MoEYS and Digital Government Authority
**Trigger**: Donor-funded digital education programme

### Downward Trace

- **Data**: A new Learner domain must be defined, with PLR as the single owner.
  Ownership must be formally assigned; all existing partial lists must be retired.
  Person domain (already owned by PNIA) must be linked — PLR uses PNIA as its
  identity anchor.
- **Technology**: PLR requires access to the data-exchange backbone to serve
  consuming bodies (PNEA, MoEYS, schools). If no backbone exists, PLR becomes
  a silo accessible only by direct integration — defeating its purpose.

### Upward Trace

| Layer | Enabled |
|-------|---------|
| Application → Data | Other systems stop maintaining their own learner copies; the Learner domain gains a single authoritative source |
| Data → Business | The "register a learner once" capability becomes real rather than aspirational |
| Business → Service | Once-only enrolment across schools, examination bodies, and scholarship programmes becomes deliverable |

### Cross-Body Consequences

| Body | Impact | Action Required |
|------|--------|----------------|
| PNEA | Must retire its private learner list and consume PLR | Integration with backbone; decommissioning plan for internal list |
| MoEYS | Must define which school-level sub-domains remain under ministry and which migrate to PLR | Data governance decision |
| PNIA | PLR must consume PNIA for person identity; no new identity function | API agreement; SLA for availability |
| PDGA | Backbone must be in place and serving PLR before PLR can serve others | Infrastructure readiness confirmation |

### Architecture Trap Check

- **Bespoke trap**: Clear — PLR is the shared building block; the trap to watch for is
  any consuming body that refuses to retire its own list and continues maintaining a
  private copy.
- **Vendor-driven trap**: Risk — if PLR is procured from a vendor and learner data is
  stored in a proprietary schema, migration to a future system is expensive. Require
  open data export and national data standard compliance at procurement.

### Enabling Conditions

| Condition | Status |
|-----------|--------|
| Legal basis for PLR as authoritative registry | Needed — no existing law designates a single learner registry |
| Named owner (ministry or agency) | Contested — MoEYS and DGA both claim it |
| Data-exchange backbone available | Gap — backbone not yet operational |
| PNEA agreement to retire private learner list | Not yet secured |
| Recurrent funding post-donor project | Unknown |

**Assessment**: The theoretical benefit of PLR — one learner record, consumed by all —
is real. But four of five enabling conditions are absent or contested. Introducing PLR
before these are resolved risks creating a sixth version of the learner record rather
than replacing the five that exist. Sequence: resolve ownership and legal basis first,
confirm backbone readiness second, then deploy PLR.
