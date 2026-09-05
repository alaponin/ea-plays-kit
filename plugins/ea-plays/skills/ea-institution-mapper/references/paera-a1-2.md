# The body taxonomy — seven types, and the five the videos teach

## Read this first

This file is a **mapping aid, not a substitute for the specification**. PAERA v1.0
Annex A1.2 is the authority for the type names and their definitions. Before using a
classification in anything that will be shown to the bodies concerned, re-read Annex A1.2
at **paera.govstack.global** and use its wording. Cite the annex, not this file.

The kit does not embed the annex text: its licence terms for verbatim excerpts have not
been confirmed, so this kit references the annex by section and re-reads the published
version at run time. If that changes, this file becomes a verbatim copy and the change is
a minor version bump naming the PAERA version.

## The five teaching types

These are the five used on video in 2.4, 2.5, 4.1 and 4.8, and carried in
`bdat-assessor`. They are correct as far as they go — a deliberate simplification for a
four-minute explanation.

| Type | Primary role | Expected data domains | Typical risk |
| --- | --- | --- | --- |
| **Policy Unit** | Sets policy, owns rules; does not run services at scale | Policy instruments, standards, funding allocations | Capability drift into regulation or delivery without mandate |
| **Regulatory Agency** | Licenses, supervises, enforces; holds registers and decisions | Register of the regulated, licences, decisions, appeals | Building its own delivery infrastructure rather than consuming shared platforms |
| **Service-Delivery Authority** | Runs services to citizens at scale | Case files, transactions, outcomes, queues | Duplicate registries, vendor lock-in, bespoke build |
| **State Registry** | Authoritative single source for one domain | One canonical domain (person, learner, business, land) | Treated as a private asset of the hosting ministry rather than a shared resource |
| **Shared Platform** | Identity, payments, data exchange — consumed across many bodies | Minimal; provides infrastructure, not content | Fragmentation if each sector builds its own instead of consuming |

*Source: PAERA v1.0 §4.6 and Annex A1.2, as carried in `bdat-assessor`.*

## What the teaching subset leaves out

Annex A1.2 carries **seven** types. Three concepts the five-type subset does not surface
are **Horizontal System**, **Natural Digital Environment** and **Public Ecosystem**. Read
the annex for their definitions and for how the seven partition the space — do not assume
the five map one-to-one onto five of the seven, because they do not.

In outline, and to be confirmed against the annex:

- **Horizontal System** — a system serving many bodies across sectors as a common function
  (document management, workflow, messaging, HR, finance). Distinct from a Shared Platform
  in that it is a system many bodies *run instances of* or *consume as a service*, not a
  foundational rail like identity or payments. Countries build these several times over
  and rarely notice.
- **Natural Digital Environment** — services delivered inside the digital contexts citizens
  already use, rather than in a government-owned channel. PAERA carries the same idea as
  principle #7 (§5.2).
- **Public Ecosystem** — the arrangement in which non-government actors (banks, mobile
  operators, schools, clinics, civil society) participate in delivering a public service.
  It classifies an *arrangement*, not a single body, which is why it has no counterpart in
  the five.

## How to write a classification

```
Progressa Digital Government Authority — Shared Platform [teaching type: Shared Platform]
  · confidence: confirmed (Establishment Decree 2019 §3)
  · hybrid: also Policy Unit — the same decree gives it standards-setting authority
```

Three rules:

1. **The full type first, the teaching type in brackets.** A learner who watched the video
   must be able to reconcile the output with what they were taught. A learner who did not
   should still get the specification's answer.
2. **Confidence is about the evidence, not your certainty.** *Confirmed* means you read the
   clause. *Inferred* means you read the behaviour. There is no third state.
3. **Flag hybrids; never resolve them silently.** A ministry that sets policy and runs a
   national system is both, and the tension between the two is usually the reason the
   sector is fragmented. Collapsing it to one type deletes the finding.

## The classification is a claim about a mandate

Every type assignment must be traceable to a clause in an instrument, or marked *inferred*.
A body classified from its website is classified from its aspirations.
