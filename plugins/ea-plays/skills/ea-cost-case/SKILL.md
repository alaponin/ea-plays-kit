---
name: ea-cost-case
description: >-
  Build the whole-of-government re-use business case — siloed versus shared building blocks
  — with the assumption block stated before the numbers, benchmark sources named with URLs,
  and the programme list and budget envelopes pulled from the country context instead of
  asked for. Serves the re-use business case (1.3) and the ministerial business case (5.4),
  and feeds the closing case (5.7). Use when someone says "build the business case for
  shared building blocks", "what does duplication cost us", "cost the re-use argument",
  "siloed vs shared", "how much would a shared identity layer save", "I need numbers for
  the minister", "TCO for these programmes", "is this worth it". Returns a per-programme
  table, a five-year country total, the point-to-point integration count, and a
  how-to-read-this-model note — as TEXT TABLES, never charts, because the next play has to
  consume them. Reads GovStack cost-benefit material, ID4D cost models, published X-Road
  operating costs and World Bank project cost tables, and names every benchmark it applies.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
---

## What this skill does

Produces the directional cost case for building blocks once rather than many times: the
assumptions first, then the per-programme numbers, then the five-year total, with every
benchmark traceable to a published source.

It extends `govstack-cost-estimator`, which already turned 1.3 from *"the percentages are
invented"* into *"the assumptions are these, confirm the tier"*. Two things are added:
the programme list and budget envelopes come from A0 §2 rather than from the learner, and
the benchmarks are **named and cited** so the "directional, not a quotation" label is backed
by something.

## Inputs

**A0 §2** — the programme list with budget envelopes and building-block needs. **A1**, the
fragmentation diagnostic, where one exists: its duplicate-registry and point-to-point rows
are the count this model prices.

If the learner has no A0 §2, do not ask them to paste one — hand off to
`country-context-pack`, or build the programme list from the national budget document and
the donor project documents yourself, and say that is what you did.

**Where budget envelopes are unknown**, state the benchmark tier and the adjustment factors
you are applying **before** the table, and proceed. The August 2026 run did exactly this and
it was the right call; do not stall for numbers the public record does not carry.

## Procedure

1. **Write the assumption block first.** Before any figure: the income tier the benchmarks
   come from, the adjustment factors applied and why (a build factor, an operations factor,
   a local-cost factor), the time horizon, the currency and year, and what is excluded.
   A reader who disagrees with the case must be able to find the assumption they disagree
   with in the first paragraph.

2. **Price the two scenarios** per `references/cost-model.md`: (A) each programme builds its
   own identity, payments and data exchange; (B) all programmes consume shared blocks.
   Use the TCO components in that file — build, deploy, operations, security, integration,
   training, governance, change cycle, replacement, lock-in exit.

3. **Count the point-to-point integrations.** For *n* systems needing to exchange, the
   siloed count grows as n(n−1)/2 and the shared count as *n*. Show the arithmetic with the
   country's actual *n* from A0 §2 — this calculation is the most persuasive single line in
   the whole case and it must be checkable.

4. **Name every benchmark with its source** (T1/T2): GovStack cost-benefit material, World
   Bank ID4D cost models, published X-Road and data-exchange operating costs, World Bank
   project cost tables from PADs and ICRs. Where a benchmark is derived rather than
   published, say "derived from" and show the derivation.

5. **Find the sequencing window.** Which programmes are already live or in procurement, and
   therefore past the point where a shared block can be intercepted; which are still
   planned. The window is usually narrow and naming it is the line the minister acts on.

6. **Run `cite-or-discard`** on every benchmark URL. A cost case is the artefact most likely
   to be quoted back, and an invented benchmark quoted in a cabinet paper is unrecoverable.

7. **For 5.4 and 5.7**, assemble rather than rebuild: this case plus `ea-comparator-evidence`
   for the proof section plus the risk register. One page, the ask at the top.

## Output contract

Provenance header first (`references/provenance-header.md`), then, in this order:

**Assumptions** — a block, before any number. Tier, factors, horizon, currency and year,
exclusions.

**Per-programme table**

```
| Programme | Blocks needed | Siloed 5-yr TCO | Shared 5-yr TCO | Difference | Benchmark applied | Source |
```

**Integration arithmetic** — the n(n−1)/2 calculation with the country's *n*, both scenarios.

**Five-year country total** — the two scenarios and the difference, with the range, not a
point estimate.

**Sequencing window** — which programmes can still be intercepted, and by when.

**How to read this model** — what it is (directional), what it is not (a quotation or a
costing exercise), and the three assumptions most likely to be wrong.

**TEXT TABLES ONLY.** No charts, no images, no generated figures. The August 2026 run
produced charts and the chain could not consume them; 5.4 needs these numbers as text.
Posts, not names. No reasoning before the header. See `references/output-contract.md`.

## Safeguard handed back

**This is a directional model, not a quotation, and no supplier has been asked.**

- **Commission a costing exercise** before any figure enters a budget submission. This case
  establishes the direction and the order of magnitude; it does not establish a price.
- **Confirm the budget envelopes** with the budget department. Donor documents state
  approved amounts, not disbursed ones, and approved amounts are frequently revised.
- **Confirm the benchmark tier fits.** A lower-middle-income benchmark applied to a
  low-income country overstates build cost and understates the operations problem.
- **The three assumptions most likely to be wrong** are named in the output. Argue with
  them before anyone else does.
- Anything marked ⚠ is unverified.

## References

- `references/cost-model.md` — the TCO framework, component splits, and the lifecycle and
  replacement-cliff arguments. Inherited from `govstack-cost-estimator`.
- `references/building-blocks.md` — the blocks and their cost characteristics. Inherited.
- `references/benchmark-sources.md` — where published cost benchmarks live, what each one
  covers, and how to cite a derived figure.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` — the shared contract.
