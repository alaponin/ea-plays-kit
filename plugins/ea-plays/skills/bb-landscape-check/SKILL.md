---
name: bb-landscape-check
description: >-
  Find out which shared digital building blocks a country actually has LIVE — not planned —
  and return a status register with sources: national ID, instant payments, data exchange
  (X-Road, GovStack Information Mediator), civil registration, G-cloud and hosting, consent.
  Use whenever a play asks "which shared building blocks already exist", before the two-trap
  screen (2.7), the sourcing matrix (4.4), the target architecture (4.5), the review gate
  (3.5), the gate decision (4.7), the second-sector map (5.3) or the rollout waves (5.6), or
  whenever someone says "is the national ID live", "does the country have a data-exchange
  layer", "what DPI exists in [country]", "is the payment switch real", "can we reuse
  identity here", "verify the shared block is authoritative and available". Reads ID4D, the
  MOSIP deployment list, the NIIS X-Road map, GovStack country engagements, central-bank
  payment pages, UNICEF CRVS and national G-cloud pages; every status carries an operator, a
  coverage figure where one exists, a URL, a tier and a date. Answers what the country HAS —
  for which products could supply a block, use bb-sourcing-researcher.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
---

## What this skill does

Returns the **BB status register**: for each shared building block, whether the country has
it live, in pilot, planned, or not at all — with the operator, a coverage figure, and a
source that says so.

It answers the most repeated safeguard in Modules 2, 4 and 5 — *verify the shared block is
authoritative and available, not merely planned* — which the plays currently leave to the
learner as "note if unknown". It serves 2.7, 3.5, 4.4, 4.5, 4.7, 5.3 and 5.6.

`bb-sourcing-researcher` answers a different question: **which products could supply** a
block the country lacks. This skill answers **what the country has**. Run this one first;
its *none* and *planned* rows are that skill's input.

## Inputs

The country. Optionally a sector, which adds the sector's own registries to the register
(a learner registry, a facility registry, a farmer registry).

If the learner has A0 §1 or §6, read them — they already name the systems. Do not ask for
them; the whole point is that the learner does not have them.

## Procedure

For each block below, search the named sources in the order given, then fetch. **A slide, a
strategy document or a press release announcing an intention is not evidence a system is
live.** Only the operator's own statement, a regulator's report, a donor completion report,
or a deployment register counts for a *live* status.

| Block | Sources, in order | Tier |
| --- | --- | --- |
| **Identity** | World Bank ID4D country diagnostics and dataset; the ID authority's own site; ID4Africa country profile; the MOSIP deployment list; UNECA Africa Digital ID Landscape | T1, then T2 |
| **Civil registration** | The national CRVS agency; UNICEF birth-registration data; the World Bank ID4D CRVS material | T1/T2 |
| **Payments** | The central bank's instant-payment or national-switch page and annual report; the World Bank fast-payments material; GSMA mobile-money data | T1, then T2 |
| **Data exchange** | The NIIS X-Road world map; GovStack country engagements; the UNDP DPI map; the operator's own member list | T2, chase to T1 |
| **Cloud and hosting** | National data-centre and G-cloud announcements by the operating agency; the national ICT agency's service catalogue | T1 |
| **Consent / data sharing** | The data-protection regulator's register and guidance; any published consent service | T1 |
| **Sector registries** (if a sector is named) | The sector ministry's own systems list; the donor project documents that built them | T1/T2 |

Then:

1. **Assign a status per block**: **live** · **pilot** · **planned** · **none** · **unclear**.
   *Unclear* is a real status — use it when the sources conflict or the last statement is
   more than two years old, and say which source said what.

2. **Name the operator.** A block with no named operator is not live, whatever the strategy
   says. If you cannot find who runs it, the status is *unclear*, not *live*.

3. **Find the coverage figure** where one exists — adult ID coverage, birth-registration
   rate, number of connected members, transaction volume. With its year. A coverage figure
   without a year is useless to a gate decision.

4. **Date the claim.** Status goes stale faster than anything else in the workbook. Record
   the date of the *source statement*, not just the date you fetched it.

5. **Run `cite-or-discard`** on the register. Where a fetch fails, mark ⚠ and say so —
   central-bank and government portals block automated fetches routinely, and a refused
   fetch must never become a *planned* status. See `references/source-tiers.md`.

6. **Answer the availability question, not just the existence one.** A block can be live and
   still unavailable to a new sector: closed membership, no onboarding procedure, a fee no
   ministry can pay, a legal basis that covers only the founding members. Record that in
   the *Available to a new sector?* column — it is the column the gate decision actually
   turns on.

## Output contract

Provenance header first (`references/provenance-header.md`), then:

```
| Block | Status | Operator | Coverage (year) | Available to a new sector? | Source | Tier | Stated on |
```

Then, in order:

- **What this means for the plays that consume it** — one line per block: what the *none*
  and *planned* rows force into build-or-buy, and which *live* rows the gate can point to.
- **Contested or unclear** — where sources disagree, both cited.
- **Re-check by** — a date, three months out.

Text in the chat. No file, no chart, no map image. Posts, not names. No reasoning before
the header. See `references/output-contract.md`.

## Safeguard handed back

A register says a block exists. It does not say you can use it.

- **Confirm availability with the operator**, not with the strategy document. Ask for the
  onboarding procedure, the current member list, the fee, and the legal basis for a new
  member's traffic.
- **A pilot is not a platform.** Four members and no data catalogue is a pilot even where
  the announcement said *national*. Do not let a *pilot* row carry a wave in a roadmap.
- **Re-run this before any gate decision.** A status three months old has already been
  wrong once in this course's own test runs.
- Anything marked ⚠ or *unclear* is a call you make with a person, not with this table.

## References

- `references/block-sources.md` — the registries and pages per block, with what each one
  can and cannot prove, and where each moved to when it moved.
- `references/status-rubric.md` — what evidence is required for each of the five statuses.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` — the shared contract.
