# Where a cost benchmark comes from, and how to cite it

Each figure in a cost case is one of three kinds. Say which kind, each time.

| Kind | Meaning | How to write it |
| --- | --- | --- |
| **Published** | A named source gives this figure for a context that is comparable | `USD 4.2m — World Bank PAD, <project>, 2023, Table 3 (T2)` |
| **Derived** | You calculated it from published figures with an operation that you state | `USD 2.9m — derived: published USD 4.2m × 0.7 (low-income build factor, cost-model.md)` |
| **Assumed** | There is no source. It is a working number that makes the model run | `USD 1.5m — assumed; no published benchmark found for this block at this scale` |

An **assumed** figure is legitimate, and a reader must see it. A model with no assumed figure,
for a country with a thin public record, hides its assumed figures. It does not avoid them.

## The sources

| Source | Covers | Tier | Watch for |
| --- | --- | --- | --- |
| **GovStack cost-benefit material** | How to frame the cost and the benefit of a building block | T1 | It gives the frame more than the figures. Use it for the structure |
| **World Bank ID4D cost models** | The build cost of an identity system, and the enrolment cost for each person | T1 | The enrolment cost for each person changes by a factor of ten with the geography and the biometrics |
| **Published operating costs of X-Road and NIIS** | The operations of a data-exchange platform, for each member | T1/T2 | The Estonian figures come from an operator that is mature and has a high capability |
| **World Bank PADs** | The cost tables of a project, for each component | T2 | These are the costs that a body **approved**. They are not the costs that the project spent. A PAD gives the intent |
| **World Bank ICRs** | What the project cost, and what it delivered | T2 | This is the better of the two sources. Always use the ICR when one exists |
| **Project documents of AfDB, the Global Fund and the EU** | The costs of a sector programme | T2 | The overheads of a sector do not always apply to another sector |
| **National budget documents** | The appropriations for a named programme | T1 | An appropriation is not the money that a body spent. Look for the rate of execution |
| **Reports of the auditor-general** | What went above the budget, and by how much | T1 | In most countries this is the most honest source of cost, and the source that people use least |

## The adjustment factors

Apply the factors in `cost-model.md`. **Name each factor where you apply it**, and not only
in the assumption block. A reader who follows one row must see which factor moved that row.

Three factors do most of the work:

- a **build factor**, for the local cost of development against the context of the
  benchmark;
- an **operations factor**, which usually moves the number in the other direction. Operations
  cost more, not less, in an environment with a constraint on capacity. This is where these
  models are most frequently wrong;
- a **local-cost factor**, for hosting, connectivity and power. In some countries this factor
  is larger than each other factor.

## The replacement cliff

Across five years, the operations cost is the largest cost. Across ten to fifteen years, the
replacement and the change cycle are the largest costs, and a siloed bespoke architecture
carries most of them. A case for five years makes the argument weaker than it is. Say so in
*how to read this model*. Where the audience accepts it, also show the line for ten years.

## What never goes into a cost case

One point estimate with no range. A figure with no attribution. A saving as a percentage
with no base. A chart. A total that a reader cannot rebuild from the rows above it. A reader
must be able to add each total in the output by hand, from the table.
