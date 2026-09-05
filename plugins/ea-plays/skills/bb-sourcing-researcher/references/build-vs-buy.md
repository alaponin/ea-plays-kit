# Build-vs-Buy: Sourcing Posture Reasoning

This file turns research findings into a defensible **sourcing posture** for each block. It is
the reasoning core of the skill. The cost magnitude is `govstack-cost-estimator`'s job; this
file decides *what kind of thing to source*, which is the estimator's input.

---

## The four-way posture scale

Postures in preference order. The presumption is reuse; bespoke must be argued for.

### 1. Reuse-OSS *(default for mature blocks)*
A production-grade open-source product (ideally a DPG) fits the requirement. Procure a
competitively tendered system integrator to deploy, integrate, and operate it under a support
contract. Best of both: no licence lock-in, with paid support and accountability.
- **Choose when**: a mature OSS product covers the core capability with real government
  deployments, and an integrator market exists (globally or in-country).
- **Lock-in**: Low. Watch only for SI lock-in — mitigate with documented config and exit terms.

### 2. Reuse-Commercial
A competitively sourced commercial product or channel is the realistic route. Most defensible
for **ancillary, genuinely competitive layers** that slot into an open core — biometric
devices/ABIS, SMS/mobile-money channels, qualified trust services — rather than for the whole
platform.
- **Choose when**: no OSS product is production-ready for this layer, OR the capability is an
  in-country channel (mobile money, local SMS) only commercial providers supply, OR a legal
  requirement (e.g. QTSP) mandates an accredited commercial provider.
- **Lock-in**: Medium–High for whole-platform proprietary deals; Low–Medium for swappable
  ancillary providers behind an open core. **Always name the vector.**

### 3. Configure
No standalone product dominates the category; deliver the capability as a **configured feature
of an adjacent block** rather than a separate procurement.
- **Choose when**: the block is a thin or gap market (Consent, Scheduler, QR Code,
  eMarketplace in some contexts) and an adjacent block already provides the substrate
  (Consent on the Information Mediator/Identity; Scheduler via Workflow or MOSIP pre-reg; QR via
  signing libraries).
- **Lock-in**: Low — *if* open APIs are specified. Without API discipline this silently
  becomes Custom-build (see drift anti-pattern).

### 4. Custom-build *(exception — must be justified)*
Bespoke development. Permitted **only** when a specific, named requirement is met by no product
and no configuration of an adjacent block.
- **Choose when**: you can write the sentence "No product or configuration meets requirement X
  because Y." If you cannot complete that sentence with a concrete requirement, the posture is
  wrong — go back to Configure or Reuse.
- **Lock-in**: Self-inflicted; this is the bespoke trap. Every Custom verdict adds to the
  bespoke-footprint roll-up and should be challenged.

---

## Decision flow per block

```
1. Does an existing system already cover this? (from BDAT/PAERA portfolio)
   → YES: extend/reuse it; do not re-buy. Stop.
   → NO: continue.

2. Is there a production-grade OSS/DPG product with real gov deployments + an integrator market?
   → YES: posture = Reuse-OSS, UNLESS a sovereignty/fit blocker applies. Stop.
   → NO or blocked: continue.

3. Is this a competitive ancillary layer, an in-country channel, or legally-mandated accredited provider?
   → YES: posture = Reuse-Commercial. Name the lock-in vector. Stop.
   → NO: continue.

4. Can an adjacent block provide this as a configured feature with open APIs?
   → YES: posture = Configure. Flag the configure-to-custom drift risk. Stop.
   → NO: continue.

5. Name the specific requirement no product/configuration meets.
   → CAN name it: posture = Custom-build. Add to bespoke footprint.
   → CANNOT name it: you missed an option — return to step 2.
```

---

## Lock-in taxonomy

Score every commercial / open-core option as Low / Medium / High and name the vector(s):

| Vector | What it is | Typical High-risk signal |
|---|---|---|
| **Data** | Your data is hard to extract in usable form | Proprietary formats, no bulk export, hosted-only |
| **Licence** | Cost/continuation depends on a single vendor's terms | Per-seat scaling across whole-of-government; renewal leverage |
| **Proprietary tooling** | Logic trapped in vendor-specific build tools | Low-code apps that can't be exported/migrated |
| **Ecosystem** | Switching means replacing an interlocking suite | Single-vendor DXP/ERP where blocks are entangled |
| **Skills** | Only the vendor's specialists can operate it | No open talent market; mandatory vendor services |

Mitigations to recommend: open standards and APIs at every boundary; data-export and exit
clauses in contract; multi-sourcing of ancillary layers; an exit reserve (see
`govstack-cost-estimator` lessons) for high-lock-in commitments.

---

## Bespoke-footprint roll-up

The headline governance metric. Target: custom code < ~20% of the delivered capability.

- Count blocks by posture. Custom-build clearly counts toward the footprint.
- At-risk Configure (no API discipline specified) counts as *latent* footprint — flag it.
- Reuse-OSS and Reuse-Commercial do **not** add to footprint (integration glue is expected and
  small if APIs are clean).
- Report as: "X of N blocks land in Custom-build, plus Y at-risk Configure → roughly Z% of the
  stack, against the <20% target." If over target, name the blocks driving it and ask whether
  each custom requirement is truly unmet by reuse.

---

## Reasoning rules (do / don't)

**Do**
- State the *decisive* factor for each posture in one or two sentences, not a wall of pros/cons.
- Default to reuse and make custom earn its place with a named requirement.
- Separate the platform decision from the channel decision (e.g. Mojaloop the switch vs. MTN
  MoMo the rail) — they have different postures.
- Carry sovereignty and in-country availability as hard constraints, not soft preferences.
- Tie each posture back to an enabling condition where relevant (governance authority, multi-
  donor financing, local integration capacity, data-protection compliance).

**Don't**
- Don't recommend Custom-build without completing the "no product because…" sentence.
- Don't treat GovStack-listing as a quality ranking or its absence as disqualifying.
- Don't collapse build-vs-buy into cost alone — lock-in, sovereignty, and footprint are
  first-class factors the money model doesn't capture.
- Don't pad thin-market blocks with weak options to look complete; an honest gap is the finding.
- Don't name products or compliance levels from memory — research live and cite.

---

## Enabling-condition reminders (theory-to-practice)

A "reuse" posture only delivers its promised savings if the conditions hold. Note any that are
absent for the country in question:
- The building block is available *before* programmes need to build (sequencing).
- A governance authority with a legal mandate owns the shared block.
- Sustained multi-donor / state financing covers operations, not just build.
- Local integration capacity (or a credible SI market) exists in-country.
- Data-protection / PDPA compliance is treated as a feature of the shared infrastructure.

If these are absent, a theoretically-correct Reuse-OSS posture may underperform in practice —
say so rather than presenting the posture as risk-free.
