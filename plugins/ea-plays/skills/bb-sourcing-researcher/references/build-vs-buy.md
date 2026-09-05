# Build versus buy: how to reason about a sourcing posture

This file turns a research finding into a **sourcing posture** for each block that you can
defend. It is the core of the reasoning in this skill. `ea-cost-case` gives the magnitude of
the cost. This file decides *what kind of thing to source*, and that decision is the input to
the cost model.

---

## The scale of four postures

The postures are in the order of preference. Reuse is the presumption. You must argue for a
bespoke build.

### 1. Reuse-OSS. *This is the default for a mature block*

An open-source product of production quality fits the requirement. A digital public good is
best. Procure a system integrator in a competitive tender, to deploy the product, to
integrate it, and to operate it under a support contract. This route gives both benefits:
there is no lock-in to a licence, and a party is paid to support the system and is
accountable for it.

- **Choose it when** a mature open-source product covers the core capability, when real
  governments deployed it, and when a market of integrators exists, in the country or
  globally.
- **Lock-in**: Low. Watch only for lock-in to the integrator. Reduce that risk with
  documented configuration and with exit terms.

### 2. Reuse-Commercial

A commercial product or channel that you source competitively is the realistic route. You can
defend this posture best for a **layer at the edge, where real competition exists**, that
fits into an open core. Examples are biometric devices and ABIS, the channels for SMS and
mobile money, and qualified trust services. You can defend it much less for a full platform.

- **Choose it when** no open-source product is ready for production in this layer; or when
  the capability is a channel inside the country, such as mobile money or local SMS, that
  only a commercial provider gives; or when the law needs an accredited commercial provider,
  such as a QTSP.
- **Lock-in**: Medium to High for a proprietary agreement for a full platform. Low to Medium
  for a provider at the edge that you can exchange, behind an open core. **Always name the
  vector.**

### 3. Configure

No product dominates the category. Give the capability as a **configured feature of an
adjacent block**, and not as a separate procurement.

- **Choose it when** the market for the block is thin or empty, and an adjacent block already
  gives the substrate. The thin markets are Consent, Scheduler, QR Code, and in some contexts
  eMarketplace. Consent can go on the Information Mediator or on Identity. Scheduler can go
  on Workflow, or on the pre-registration function of MOSIP. QR can use the libraries for
  signing.
- **Lock-in**: Low, *if* you specify open APIs. Without the discipline of an API, this
  posture becomes a custom build in silence. See the anti-pattern about drift.

### 4. Custom-build. *This is the exception, and it needs a justification*

This is bespoke development. It is permitted **only** when a specific named requirement is
met by no product and by no configuration of an adjacent block.

- **Choose it when** you can write this sentence: "No product or configuration meets
  requirement X because Y." If you cannot complete the sentence with a concrete requirement,
  the posture is wrong. Return to Configure or to Reuse.
- **Lock-in**: you make it yourself. This is the bespoke trap. Each Custom verdict adds to
  the roll-up of the bespoke footprint, and a person must challenge it.

---

## The decision flow for each block

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

## The taxonomy of lock-in

Score each commercial option and each open-core option as Low, Medium or High. Name the
vector or the vectors.

| Vector | What it is | Typical signal of a high risk |
|---|---|---|
| **Data** | It is difficult to extract your data in a form that you can use | Proprietary formats, no export of all the data, and a product that only the vendor can host |
| **Licence** | The cost and the continuation depend on the terms of one vendor | A price for each seat, across all of government. The vendor has leverage at each renewal |
| **Proprietary tooling** | The logic is inside build tools that only the vendor has | Low-code applications that nobody can export or migrate |
| **Ecosystem** | To change one part, you must replace a suite that interlocks | A DXP or ERP from one vendor, where the blocks are entangled |
| **Skills** | Only the specialists of the vendor can operate the system | There is no open market of talent. The services of the vendor are mandatory |

Recommend these measures against lock-in: open standards and open APIs at each boundary;
clauses for data export and for exit in the contract; more than one source for the layers at
the edge; and a reserve for the exit, as the lessons in `ea-cost-case` describe, for a
commitment with a high lock-in.

---

## The roll-up of the bespoke footprint

This is the metric that the governance uses first. The target is custom code below about 20%
of the capability that the programme delivers.

- Count the blocks by their posture. A Custom-build block counts in the footprint.
- A Configure block that is at risk, because nobody specified the API discipline, counts as
  *latent* footprint. Flag it.
- Reuse-OSS and Reuse-Commercial do **not** add to the footprint. The programme still writes
  code to integrate them, and that code is small when the APIs are clean.
- Report it in this form: "X of N blocks are Custom-build, and Y more are Configure at risk.
  This is about Z% of the stack, against the target of less than 20%." If the number is above
  the target, name the blocks that cause it. Then ask whether reuse truly fails to meet each
  custom requirement.

---

## The rules for the reasoning

**Do these five things**

- Give the *decisive* factor for each posture in one or two sentences. Do not give a wall of
  advantages and disadvantages.
- Make reuse the default. Make a custom build earn its place with a named requirement.
- Keep the decision about the platform separate from the decision about the channel. Mojaloop
  is the switch and MTN MoMo is the rail. They have different postures.
- Treat sovereignty and availability in the country as hard constraints. They are not soft
  preferences.
- Connect a posture to the condition that it needs, where one applies: the authority to
  govern, financing from more than one donor, the capacity to integrate locally, and
  compliance with data protection.

**Do not do these five things**

- Do not recommend Custom-build before you complete the sentence "no product, because…".
- Do not use a GovStack listing as a ranking of quality. Do not use the absence of a listing
  to remove a product.
- Do not reduce build versus buy to the cost. Lock-in, sovereignty and the footprint are also
  primary factors, and the cost model does not capture them.
- Do not fill a thin market with weak options to make the list look complete. An honest gap
  is the finding.
- Do not name a product or a compliance level from memory. Research it live, and cite it.

---

## The conditions that a reuse posture needs

A reuse posture gives the savings that you promise only when these conditions are true.
Record each condition that the country does not have.

- The building block is available *before* the programmes need to build. This is a question
  of sequence.
- A governance authority with a legal mandate owns the shared block.
- Financing from the state or from several donors continues, and it covers the operations and
  not only the build.
- The capacity to integrate exists in the country, or there is a credible market of system
  integrators.
- The country treats compliance with data protection as a feature of the shared
  infrastructure.

If these conditions are absent, a Reuse-OSS posture that is correct in theory can give a
worse result in practice. Say so. Do not give the posture as a posture with no risk.
