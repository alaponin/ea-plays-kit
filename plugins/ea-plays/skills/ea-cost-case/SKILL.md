---
name: ea-cost-case
description: >-
  Build the whole-of-government re-use business case, which compares siloed building blocks
  with shared building blocks. State the assumption block before the numbers. Name the
  benchmark sources with their URLs. Take the programme list and the budget envelopes from
  the country context instead of asking the learner for them. Serves the re-use business
  case (1.3) and the ministerial business case (5.4), and feeds the closing case (5.7).
  Use when someone says "build the business case for shared building blocks", "what does
  duplication cost us", "cost the re-use argument", "siloed vs shared", "how much would a
  shared identity layer save", "I need numbers for the minister", "TCO for these
  programmes", "is this worth it". Returns a per-programme table, a five-year country total,
  the point-to-point integration count, and a how-to-read-this-model note — as TEXT TABLES,
  never charts, because the next play has to consume them. Reads GovStack cost-benefit
  material, ID4D cost models, published X-Road operating costs and World Bank project cost
  tables, and names every benchmark it applies.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
---

## What this skill does

This skill makes the directional cost case to build a block one time and not many times. It
gives the assumptions first, then the numbers for each programme, then the five-year total.
Each benchmark has a published source.

Its predecessor changed play 1.3 from *"the percentages are invented"* into *"the
assumptions are these, confirm the tier"*. This skill adds two things. The programme list
and the budget envelopes come from A0 §2 and not from the learner. The benchmarks have a
**name and a citation**, so that the label "directional, not a quotation" has support.

## Inputs

**A0 §2** — the programme list with the budget envelopes and the building-block needs.

**A1**, the fragmentation diagnostic, if one exists. Its rows for duplicate registries and
point-to-point integration give the count that this model prices.

If the learner has no A0 §2, do not ask the learner to paste one. Use
`country-context-pack`. You can also build the programme list yourself from the national
budget document and the donor project documents. Then say that you did this.

If you do not know the budget envelopes, give the benchmark tier and the adjustment factors
that you apply. Give them **before** the table. Then continue. The August 2026 run did
this, and it was correct. Do not stop for numbers that the public record does not have.

## Procedure

1. **Write the assumption block first.** Write it before any figure. Give the income tier
   of the benchmarks. Give the adjustment factors and the reason for each one: a build
   factor, an operations factor and a local-cost factor. Give the time horizon, the
   currency and its year, and what you exclude. A reader who does not agree with the case
   must find the assumption that they dispute in the first paragraph.

2. **Price the two scenarios**, as `references/cost-model.md` defines them. In scenario A,
   each programme builds its own identity, payments and data exchange. In scenario B, all
   programmes use shared blocks. Use the TCO components in that file: build, deploy,
   operations, security, integration, training, governance, change cycle, replacement, and
   exit from lock-in.

3. **Count the point-to-point integrations.** For *n* systems that must exchange data, the
   siloed count increases as n(n−1)/2, and the shared count increases as *n*. Show the
   arithmetic with the true *n* of the country from A0 §2. This calculation is the most
   persuasive line in the case, and a reader must be able to check it.

4. **Name each benchmark with its source** (T1/T2). Use the GovStack cost-benefit material,
   the World Bank ID4D cost models, the published operating costs of X-Road and other data-
   exchange platforms, and the project cost tables in World Bank PADs and ICRs. If you
   derive a benchmark instead of taking it from a publication, write "derived from" and show
   the derivation.

5. **Find the sequencing window.** Say which programmes are live or in procurement, because
   a shared block cannot enter those. Say which programmes are still planned. The window is
   usually short. The minister acts on that line.

6. **Run `cite-or-discard` on each benchmark URL.** People quote a cost case more than any
   other artefact. An invented benchmark in a cabinet paper cannot be corrected.

7. **For plays 5.4 and 5.7, assemble the case. Do not build it again.** Use this case, the
   proof section from `ea-comparator-evidence`, and the risk register. Write one page, with
   the ask at the top.

## Output contract

Write the provenance header first (`references/provenance-header.md`). Then write these six
sections in this order.

**Assumptions** — a block, before any number: the tier, the factors, the horizon, the
currency and its year, and the exclusions.

**Per-programme table**

```
| Programme | Blocks needed | Siloed 5-yr TCO | Shared 5-yr TCO | Difference | Benchmark applied | Source |
```

**Integration arithmetic** — the n(n−1)/2 calculation with the *n* of the country, for both
scenarios.

**Five-year country total** — the two scenarios and the difference. Give a range. Do not
give one number.

**Sequencing window** — the programmes that a shared block can still enter, and the date
after which it cannot.

**How to read this model** — what the model is, which is directional; what the model is
not, which is a quotation or a costing exercise; and the three assumptions that are most
probably wrong.

**USE TEXT TABLES ONLY.** Do not make a chart, an image or a generated figure. The August
2026 run made charts, and the chain could not use them. Play 5.4 needs these numbers as
text. Posts, not names. Write no analysis before the header. See
`references/output-contract.md`.

## Safeguard handed back

**This is a directional model. It is not a quotation. Nobody asked a supplier for a
price.**

- **Commission a costing exercise** before a figure goes into a budget submission. This
  case gives the direction and the order of magnitude. It does not give a price.
- **Confirm the budget envelopes** with the budget department. Donor documents give the
  amounts that were approved, not the amounts that were paid. Approved amounts change
  frequently.
- **Confirm that the benchmark tier is correct.** A lower-middle-income benchmark applied
  to a low-income country makes the build cost too high and the operations problem too
  small.
- **The three assumptions that are most probably wrong** are in the output. Dispute them
  before another person does.
- Each item marked ⚠ is unverified.

## References

- `references/cost-model.md` — the TCO framework, the component splits, and the arguments
  about the lifecycle and the replacement cliff. Inherited.
- `references/building-blocks.md` — the blocks and their cost characteristics. Inherited.
- `references/benchmark-sources.md` — where the published cost benchmarks are, what each
  one covers, and how to cite a figure that you derived.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` — the shared contract.
