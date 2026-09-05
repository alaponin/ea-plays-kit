<!-- fixture: Progressa (fictional) · canonical: tests/progressa.md · keep consistent with it -->
# The change-impact template: how to trace the consequences in each layer

Use this template when the assessment covers a proposed change. The change can be a new
building block, the retirement of a system, a migration to a platform, or a change of policy.
Do not use this template for a description of the current state only.

The most valuable use of BDAT is not to describe what exists. It is to trace what changes
when a body introduces something new, or removes something old. Here the architecture gives
the reason for an investment decision.

---

## When to use this template

Use it in these six cases:

- a body proposes a new GovStack building block: identity, payments or data exchange;
- a body retires or replaces a system that exists;
- a body adopts a new platform or a new cloud provider;
- a change of policy creates a requirement for a new capability;
- a donor project proposes to build or to procure a system;
- a body extends a shared platform to a new sector.

---

## The Change-Impact Trace

For each proposed change, trace the consequences through the four layers. Trace downward,
for what the change needs from the layers below. Trace upward, for what the change makes
possible in the layers above.

### 1. Name the change

| Field | Content |
|-------|---------|
| Change | [What is being introduced or retired] |
| Initiating layer | [Which BDAT layer the change enters at] |
| Owner | [Which body is responsible for the change] |
| Trigger | [Policy decision, donor project, technology refresh, legal requirement] |

---

### 2. The downward trace — what the change needs

Start at the layer where the change enters. Then trace what the change needs from each layer
below it.

**If the change enters at the Business layer**, as a new policy or a new mandate for a
capability:
- Data: which new domains does this capability need? Who will own them?
- Application: which new applications does it need? Which applications that exist must a team
  extend?
- Technology: which infrastructure must exist before the applications can operate?

**If the change enters at the Application layer**, as a new system or a new building block:
- Data: which data domains does the new application use? Does a named body already own them,
  or must somebody assign the ownership?
- Technology: which infrastructure does the new application need? Does it exist, or must a
  body procure it or build it?

**If the change enters at the Technology layer**, as a new platform, new hosting or a new
backbone:
- Application: which applications depend on the component that changes? How much work does
  the integration need?
- Data: does the change affect how a system stores the data or exchanges it? Do the data
  standards stay the same?
- Business: does a constraint in the technology limit the capabilities that a team can
  deliver? This is the pressure upward. Name it honestly.

---

### 3. The upward trace — what the change makes possible

Trace what the change makes possible in the layers above.

| Layer | What is now possible that was not before |
|-------|------------------------------------------|
| Technology → Application | [Which applications can now be built or improved?] |
| Application → Data | [Which data flows are now possible or standardised?] |
| Data → Business | [Which capabilities are now supportable that were not?] |
| Business → Service | [Which citizen-facing services become deliverable?] |

---

### 4. The consequences for the other bodies

A change rarely affects one body only. Record these items for each body in the scope:

| Body | Impact | Action Required |
|------|--------|----------------|
| [Body A] | [How is it affected — consuming body, owning body, competing body?] | [What must it do — integrate, retire, hand over ownership?] |

---

### 5. The check for the architecture traps in this change

| Trap | Assessment |
|------|-----------|
| **Bespoke trap** | Does this change duplicate a shared building block that already exists? If so, what is the case for building rather than consuming? |
| **Vendor-driven trap** | Does this change introduce a product that stores data in a proprietary format? Can the government exit within two years at reasonable cost? |

---

### 6. The conditions that the change needs

Name what must be true before a team can implement the change. A benefit in theory does not
occur when the conditions are absent.

| Condition | Status |
|-----------|--------|
| Legal basis for the new capability or data flow | [In place / Needed / Unknown] |
| Named owner for each affected data domain | [Named / Vacant / Disputed] |
| Governance board with authority to enforce cross-body data agreements | [Exists / Absent] |
| Technology infrastructure already in place | [Ready / Gap / Procurement needed] |
| Consuming bodies technically able to integrate | [Confirmed / Uncertain] |
| Recurrent funding for operations and maintenance | [Committed / Donor-dependent / Unknown] |

---

## A worked example: the introduction of a National Learner Registry

**The change**: introduce the National Learner Registry (PLR) as a shared state registry.
The Education Sector Plan 2023–2028 asks for it, and it is **not started**. Today three
systems hold a learner: the district EMIS, the list of candidates of PNEA, and the register
of beneficiaries of the Social Protection Agency. Each one uses its own numbers, and the
three do not agree.

**The layer where the change enters**: Application, because a body introduces a new shared
system.
**The owner**: MoEYS. The Education Sector Plan 2023–2028 and §2 name it. Record two facts
about the owner before you continue: MoEYS is **not a member of Linkup**, and the sector has
**no function for data standards** (§6).
**The trigger**: the human-capital programme of the World Bank, USD 6.5m across three years
(§2, item 1).

### The downward trace

- **Data**: somebody must define a new Learner domain, and PLR must be its single owner. A
  body must assign that ownership formally. A team must reconcile the three partial lists
  that exist, and then retire them. PNIA owns the Person domain, but **PNIA issues an ID only
  at 16 years**. Therefore the National ID cannot be the anchor for a child in a primary
  school. The anchor for the legal identity is the Civil Registration Department, which works
  on paper first and registers 71% of the births (§1, §7). A design that uses the National ID
  fails for the main population of the registry. The 29% of births that nobody registered
  then stops a child from enrolling. It is not a footnote about the quality of the data.
- **Technology**: PLR must reach the bodies that use it, which are PNEA, the schools of
  MoEYS, and the Social Protection Agency. The layer for exchange exists. It is Linkup, on
  X-Road 7.x, live as a pilot with four members and a documented onboarding procedure. MoEYS
  is not one of the four. **The gap is the membership. It is not the infrastructure.** If
  nobody closes that gap, PLR becomes a silo that other systems reach with a direct
  integration. It can also get a point-to-point link, like the link that the tax authority
  built to the business register in 2022 and never migrated.

### Upward Trace

| Layer | Enabled |
|-------|---------|
| Application → Data | The three partial learner lists stop being maintained separately; the Learner domain gains a single authoritative source |
| Data → Business | The "register a learner once" capability becomes real rather than aspirational — today no body claims it |
| Business → Service | Once-only enrolment across schools, the examination authority and the scholarship programme becomes deliverable; the parent stops proving the child's identity on paper at every counter |

### The consequences for the other bodies

| Body | Impact | Action Required |
|------|--------|----------------|
| MoEYS | Owns the change, and holds one of the three lists in its district EMIS | Join Linkup; define which school-level sub-domains stay with the ministry and which migrate; retire the district learner numbering |
| PNEA | Must retire its candidate-list numbering as a learner identifier and consume PLR | Integration via Linkup; decommissioning plan for the internal list |
| Social Protection Agency | Holds the third learner list inside its beneficiary register | Consume PLR for learner identity; reconcile against the existing register before retiring anything |
| PNIA | PLR consumes the National ID for those aged 16+; no new identity function | API agreement; SLA for availability |
| Civil Registration Department | Becomes the identity anchor for learners below 16 | An electronic route into the civil register, which is paper-first today |
| PDGA | Onboards MoEYS to Linkup; coordinates, but cannot compel | Member onboarding; a data catalogue, which Linkup does not publish |

### The check for the architecture traps

- **The bespoke trap is present in the sector.** A vendor built the register of
  beneficiaries of the Social Protection Agency in 2016, under a World Bank programme. The
  team did not assemble it from the registries that the country shares. It is now one of the
  three lists of learners. The same donor funds PLR in the same way, and nothing yet obliges
  PLR to use PNIA and the civil register instead of building its own list. The
  counter-example already operates in the sector.
- **The vendor-driven trap is present, and it is specific.** One vendor maintains that
  register from 2016. The vendor that built it still holds the only maintenance contract. At
  the procurement, require an open format for the export of the data, and require a market of
  more than one maintainer. This failure is not hypothetical here. It is ten years old, and
  it is in the next room.

### The conditions that the change needs

| Condition | Status |
|-----------|--------|
| Legal basis for PLR as authoritative registry | **Needed** — no instrument designates an authoritative learner registry (§7) |
| Legal basis for sharing minors' data | **Needed** — the Data Protection Act 2023 requires one, and parental consent for non-statutory uses. The Data Protection Commission has 6 staff and no enforcement action yet (§7) |
| Named owner for the Learner domain | **Named** — MoEYS, in the Education Sector Plan 2023–2028 and §2 |
| Governance board able to enforce cross-body data agreements | **Absent** — no EA Governance Board; the ICT Steering Committee met twice in 2024 and not since, and PDGA's mandate is coordinating, not binding (§1, §4) |
| Data exchange available to the sector | **Ready, not joined** — Linkup is live in pilot with four members and MoEYS is not one. Onboarding, not build (§1) |
| Recurrent funding for operations and maintenance | **Absent** — annual budget cycle, no multi-year ICT envelopes (§4, §5) |

**The assessment**: the benefit of PLR in theory is real. It gives one record for each
learner, and each body uses that record. But of the six conditions, only one is in place.
Four are absent or not secure. The fifth, which is the layer for exchange, exists, and the
ministry that owns the change has not joined it. If a body introduces PLR before it resolves
these conditions, PLR can become **a fourth list, and it will not replace the three**. Use
this sequence. Resolve the two legal bases first. Then make MoEYS a member of Linkup, which
is a procedure and not a build. Then deploy PLR, against the civil register for a child below
16 years, and against the National ID above that age.
