# Where cost benchmarks come from, and how to cite one

Every figure in a cost case is one of three things. Say which, every time.

| Kind | Meaning | How to write it |
| --- | --- | --- |
| **Published** | A named source states this figure for a comparable context | `USD 4.2m — World Bank PAD, <project>, 2023, Table 3 (T2)` |
| **Derived** | Computed from published figures by a stated operation | `USD 2.9m — derived: published USD 4.2m × 0.7 (low-income build factor, cost-model.md)` |
| **Assumed** | No source; a working number to make the model run | `USD 1.5m — assumed; no published benchmark found for this block at this scale` |

An **assumed** figure is legitimate and must be visible. A model with no assumed figures in
a country with a thin public record has hidden them, not avoided them.

## The sources

| Source | Covers | Tier | Watch for |
| --- | --- | --- | --- |
| **GovStack cost-benefit material** | Building-block level cost and benefit framing | T1 | Framing more than figures; use for structure |
| **World Bank ID4D cost models** | Identity system build and per-capita enrolment costs | T1 | Enrolment cost per person varies by an order of magnitude with geography and biometrics |
| **Published X-Road / NIIS operating costs** | Data-exchange platform operations, per member | T1/T2 | Estonian figures reflect a mature, high-capability operator |
| **World Bank PADs** | Project cost tables, component by component | T2 | **Approved** cost, not spent cost. A PAD is intent. |
| **World Bank ICRs** | What the project actually cost and delivered | T2 | The better source of the two. Always prefer the ICR where one exists. |
| **AfDB, Global Fund, EU project documents** | Sector programme costs | T2 | Sector-specific overheads may not generalise |
| **National budget documents** | Actual appropriations for named programmes | T1 | Appropriation ≠ execution. Look for an execution rate. |
| **Auditor-general reports** | What overran, and by how much | T1 | The most honest cost source in most countries, and the least used |

## Adjustment factors

Apply the factors in `cost-model.md`, and **name each one where it is applied**, not only in
the assumption block. A reader tracing one row must see which factor moved it.

Three factors do most of the work:

- a **build factor** for local development cost against the benchmark's context;
- an **operations factor**, usually pointing the other way — operations in a
  capacity-constrained environment costs more, not less, and is where these models are most
  often wrong;
- a **local-cost factor** for hosting, connectivity and power, which in some countries
  dominates everything else.

## The replacement cliff

Over a five-year horizon, operations dominates. Over ten to fifteen, replacement and change
cycle dominate — and those are the costs a bespoke siloed architecture bears most heavily.
A five-year case understates the argument. Say so in *how to read this model*, and where
the audience will tolerate it, show the ten-year line as well.

## What never goes in a cost case

A single point estimate with no range. A figure with no attribution. A saving expressed as a
percentage with no base. A chart. A total that cannot be reconstructed from the rows above
it — every total in the output must be addable by hand from the table.
