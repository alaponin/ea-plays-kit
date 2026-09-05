<!-- fixture: Progressa (fictional) · canonical: tests/progressa.md · keep consistent with it -->
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

**Change**: Introduce the National Learner Registry (PLR) as a shared state registry. The
Education Sector Plan 2023–2028 calls for it and it has **not started**. Today a learner is
held three times — in the district EMIS, in the PNEA candidate list, and in the Social
Protection Agency's beneficiary register — each on its own numbering, and the three do not
agree.

**Initiating layer**: Application (a new shared system is being introduced)
**Owner**: MoEYS — named in the Education Sector Plan 2023–2028 and in §2. Note two things
about that owner before going further: MoEYS is **not a Linkup member**, and the sector has
**no data-standards function** (§6).
**Trigger**: World Bank human-capital programme — USD 6.5m over three years (§2, item 1)

### Downward Trace

- **Data**: A new Learner domain must be defined, with PLR as the single owner. Ownership
  must be formally assigned; the three existing partial lists must be reconciled and
  retired. The Person domain is owned by PNIA — but **PNIA issues IDs only at 16**, so for a
  primary-school child the National ID cannot be the anchor. The legal identity anchor is
  the Civil Registration Department: paper-first, 71% birth registration (§1, §7). A design
  that assumes the National ID will fail on the registry's main population, and the missing
  29% of birth registrations becomes an enrolment barrier rather than a data-quality
  footnote.
- **Technology**: PLR must reach its consuming bodies (PNEA, MoEYS schools, the Social
  Protection Agency). The exchange layer already exists — Linkup, X-Road 7.x, live in pilot
  with four members and a documented onboarding procedure — but MoEYS is not one of the
  four. **The gap is membership, not infrastructure.** If that is not fixed, PLR either
  becomes a silo reached by direct integration, or gets a point-to-point link of the kind
  the tax authority built to the business register in 2022 and has not migrated since.

### Upward Trace

| Layer | Enabled |
|-------|---------|
| Application → Data | The three partial learner lists stop being maintained separately; the Learner domain gains a single authoritative source |
| Data → Business | The "register a learner once" capability becomes real rather than aspirational — today no body claims it |
| Business → Service | Once-only enrolment across schools, the examination authority and the scholarship programme becomes deliverable; the parent stops proving the child's identity on paper at every counter |

### Cross-Body Consequences

| Body | Impact | Action Required |
|------|--------|----------------|
| MoEYS | Owns the change, and holds one of the three lists in its district EMIS | Join Linkup; define which school-level sub-domains stay with the ministry and which migrate; retire the district learner numbering |
| PNEA | Must retire its candidate-list numbering as a learner identifier and consume PLR | Integration via Linkup; decommissioning plan for the internal list |
| Social Protection Agency | Holds the third learner list inside its beneficiary register | Consume PLR for learner identity; reconcile against the existing register before retiring anything |
| PNIA | PLR consumes the National ID for those aged 16+; no new identity function | API agreement; SLA for availability |
| Civil Registration Department | Becomes the identity anchor for learners below 16 | An electronic route into the civil register, which is paper-first today |
| PDGA | Onboards MoEYS to Linkup; coordinates, but cannot compel | Member onboarding; a data catalogue, which Linkup does not publish |

### Architecture Trap Check

- **Bespoke trap**: **Present in the sector.** The Social Protection Agency's beneficiary
  register was built in 2016 by a vendor under a World Bank programme rather than assembled
  from shared registries, and it is now one of the three learner lists. PLR is funded the
  same way, by the same donor, and nothing yet requires it to consume PNIA and the civil
  register rather than build its own. The counter-example is already running in the sector.
- **Vendor-driven trap**: **Present, and specific.** That 2016 register is under
  single-vendor maintenance — the vendor that built it still holds the only maintenance
  contract. Require open data export and a maintenance market at procurement, because the
  failure mode is not hypothetical here; it is ten years old and in the next room.

### Enabling Conditions

| Condition | Status |
|-----------|--------|
| Legal basis for PLR as authoritative registry | **Needed** — no instrument designates an authoritative learner registry (§7) |
| Legal basis for sharing minors' data | **Needed** — the Data Protection Act 2023 requires one, and parental consent for non-statutory uses. The Data Protection Commission has 6 staff and no enforcement action yet (§7) |
| Named owner for the Learner domain | **Named** — MoEYS, in the Education Sector Plan 2023–2028 and §2 |
| Governance board able to enforce cross-body data agreements | **Absent** — no EA Governance Board; the ICT Steering Committee met twice in 2024 and not since, and PDGA's mandate is coordinating, not binding (§1, §4) |
| Data exchange available to the sector | **Ready, not joined** — Linkup is live in pilot with four members and MoEYS is not one. Onboarding, not build (§1) |
| Recurrent funding for operations and maintenance | **Absent** — annual budget cycle, no multi-year ICT envelopes (§4, §5) |

**Assessment**: The theoretical benefit of PLR — one learner record, consumed by all — is
real. But of six enabling conditions only one is in place; four are absent or unsecured, and
the fifth, the exchange layer, exists while the owning ministry has not joined it.
Introducing PLR before these are resolved risks creating **a fourth list rather than
replacing the three**. Sequence: resolve the two legal bases first, onboard MoEYS to Linkup
second — it is procedural, not a build — then deploy PLR against the civil register for
under-16s and the National ID above.
