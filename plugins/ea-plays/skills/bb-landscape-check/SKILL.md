---
name: bb-landscape-check
description: >-
  Find which shared digital building blocks a country has LIVE, not planned — national ID,
  instant payments, data exchange (X-Road, GovStack Information Mediator), civil
  registration, G-cloud and hosting, consent — and give a status register with sources.
  Serves the two-trap screen (2.7), the review gate (3.5), the sourcing matrix (4.4), the
  target architecture (4.5), the gate decision (4.7), the rollout waves (5.3) and the
  second-sector map (5.3b), and the KP2 component-to-layer map (4.1, B20), trust-zone trace
  (4.2, B21) and technical layer of the four-layer exchange map (1.2). Use whenever a play
  asks "which shared building blocks already exist", or someone says "is the national ID
  live", "does the country have a data-exchange layer", "what DPI exists in [country]", "is
  the payment switch real", "can we reuse identity here", "verify the shared block is
  authoritative and available", "component-to-layer map", "functional layers of the bus",
  "trust zones", "trust-zone trace", "is the exchange layer live". Answers what the country
  HAS — for which products could supply a block, use bb-sourcing-researcher.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
---

## What this skill does

This skill gives the **BB status register**. For each shared building block, the register
tells whether the country has the block live, in pilot, planned, or not at all. It gives
the operator, a coverage figure, and a source that says so.

Modules 2, 4 and 5 repeat one safeguard more than any other: *verify the shared block is
authoritative and available, not merely planned*. The plays leave this work to the learner
with the words "note if unknown". This skill does the work. It serves 2.7, 3.5, 4.4, 4.5,
4.7, 5.3 and 5.3b.

`bb-sourcing-researcher` answers a different question: **which products can supply** a
block that the country does not have. This skill answers **what the country has**. Run
this skill first. Its *none* rows and *planned* rows are the input to that skill.

## Inputs

The skill needs the country. It can also use a sector. A sector adds the registries of
that sector to the register: a learner registry, a facility registry, or a farmer registry.

If the learner has A0 §1 or A0 §6, read them. They already give the names of the systems.
Do not ask the learner for them. The learner does not have them. This is why the skill
exists.

## Procedure

For each block in the table below, search the sources in the order given. Then read the
pages. **An intention in a slide, a strategy document or a press release is not evidence
that a system is live.** For a *live* status you need one of these: a statement by the
operator, a report by a regulator, a completion report by a donor, or a deployment
register.

| Block | Sources, in order | Tier |
| --- | --- | --- |
| **Identity** | World Bank ID4D country diagnostics and dataset; the site of the ID authority; the ID4Africa country profile; the MOSIP deployment list; the UNECA Africa Digital ID Landscape | T1, then T2 |
| **Civil registration** | The national CRVS agency; UNICEF birth-registration data; the CRVS material of World Bank ID4D | T1/T2 |
| **Payments** | The instant-payment page or national-switch page of the central bank, and its annual report; the fast-payments material of the World Bank; GSMA mobile-money data | T1, then T2 |
| **Data exchange** | The NIIS X-Road world map; GovStack country engagements; the UNDP DPI map; the member list of the operator | T2, then find the T1 source |
| **Cloud and hosting** | The national data-centre and G-cloud announcements by the agency that operates them; the service catalogue of the national ICT agency | T1 |
| **Consent / data sharing** | The register and guidance of the data-protection regulator; any consent service that is published | T1 |
| **Sector registries** (if the learner gives a sector) | The systems list of the sector ministry; the donor project documents that built the systems | T1/T2 |

Then do these six steps:

1. **Give each block a status**: **live** · **pilot** · **planned** · **none** ·
   **unclear**. *Unclear* is a true status. Use it when the sources do not agree, or when
   the last statement is more than two years old. Then tell which source says what.

2. **Give the name of the operator.** A block with no named operator is not live, whatever
   the strategy says. If you cannot find who operates it, the status is *unclear*. It is
   not *live*.

3. **Find the coverage figure**, if one exists: adult ID coverage, the birth-registration
   rate, the number of members that are connected, or the transaction volume. Give the
   year with the figure. A coverage figure with no year has no value at a gate decision.

4. **Put the date on the claim.** Status goes stale faster than any other item in the
   workbook. Record the date of the *statement in the source*, not only the date that you
   read the page.

5. **Run `cite-or-discard`** on the register. If a fetch fails, mark the row ⚠ and say so.
   Central-bank portals and government portals block automatic fetches frequently. A
   refused fetch must never become a *planned* status. See `references/source-tiers.md`.

6. **Answer the availability question. Do not answer only the existence question.** A
   block can be live and still not available to a new sector. The membership can be
   closed. There can be no onboarding procedure. The fee can be more than a ministry can
   pay. The legal basis can cover only the members that started it. Record this in the
   *Available to a new sector?* column. The gate decision depends on that column.

## Output contract

Write the provenance header first (`references/provenance-header.md`). Then write this
table:

```
| Block | Status | Operator | Coverage (year) | Available to a new sector? | Source | Tier | Stated on |
```

Then write these three sections in this order:

- **What this means for the plays that consume it** — one line for each block. Say what
  the *none* rows and the *planned* rows force into a build-or-buy decision. Say which
  *live* rows the gate can use.
- **Contested or unclear** — the blocks where the sources do not agree, with both sources
  cited.
- **Re-check by** — a date three months from now.

Write text in the chat. Do not make a file, a chart or an image of a map. Posts, not
names. Write no analysis before the header. See `references/output-contract.md`.

## Safeguard handed back

A register says that a block exists. It does not say that you can use the block.

- **Confirm availability with the operator.** Do not confirm it with the strategy
  document. Ask for the onboarding procedure, the current member list, the fee, and the
  legal basis for the traffic of a new member.
- **A pilot is not a platform.** Four members and no data catalogue is a pilot, also when
  the announcement used the word *national*. Do not let a *pilot* row carry a wave in a
  roadmap.
- **Run this skill again before each gate decision.** In the test runs of this course, a
  status three months old was already wrong one time.
- Each item marked ⚠ or *unclear* is a decision that you make with a person. You do not
  make it with this table.

## KP2 plays

| KP2 play | Artefact | This skill supplies |
| --- | --- | --- |
| 4.1 | B20 — Component-to-layer map | which components are already provided by the live exchange layer (the X-Road software adopted), so a 'missing' component is not procured twice |
| 4.2 | B21 — Trust-zone trace | the live trust services — the certification authority, OCSP, timestamping — and whether each is a production service or a test one |
| 1.2 | the technical layer of B2 | the data-exchange row of the BB status register: live, pilot, planned or none |

The chain is in `references/workbook-chain-kp2.md`.

## References

- `references/block-sources.md` — the registries and pages for each block, what each one
  can prove, what each one cannot prove, and where each one moved to.
- `references/status-rubric.md` — the evidence that each of the five statuses needs.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` ·
  `references/workbook-chain-kp2.md` — the shared contract.
