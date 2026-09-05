# The ten-entity export test

The scoring in the comparison table is provisional until this passes. Run it yourself, on
each shortlisted tool, before signing anything. It takes under an hour per tool.

## Why a demo is not this test

A demo is run by someone who knows the tool, on data shaped to suit it, and ends before the
export. This test is run by you, on your data, and only ends when the file opens **without
the tool**.

## The procedure

**1. Build the ten entities.** Use real ones from your own repository schema (A16), not the
tool's sample model. Ten is enough to expose everything:

- 3 capabilities;
- 2 data domains, **each with a named owner attribute** — the owner is the field most often
  lost in export;
- 3 applications, each **mapped to** at least one capability and one data domain;
- 2 technology elements;
- and at least one **custom attribute** on one entity (a status, a source, a review date),
  because custom attributes are where lossy exports lose things.

**2. Export**, in every format the vendor documents. Note which formats needed which
licence tier.

**3. Open each file with something that is not the tool.** A text editor for XML and CSV.
A different EA tool for ArchiMate Exchange Format — Archi is free and reads it. A
spreadsheet for CSV.

**4. Check, in the exported file:**

| Check | Pass |
| --- | --- |
| All ten entities present | 10 of 10 |
| Every relationship present | all of them, with both ends identifiable |
| The data-domain **owner** attribute present | yes |
| The **custom attribute** present | yes |
| Entity **types** preserved, not flattened to a generic node | yes |
| The file is readable without the tool's documentation | yes |

**5. Re-import** the export into a *different* tool, or back into a fresh instance of the
same one. Count what survived.

**6. Time it.** How long did the export take, and how many steps? An export that takes a
day of expert effort is not an exit path.

## Scoring

| Result | Meaning |
| --- | --- |
| All six checks pass, re-import clean | **Low lock-in.** The models can leave. |
| Entities and relationships survive, attributes lost | **Medium.** Exit is possible with re-work. Quantify it: how many attributes across your real estate? |
| Relationships or types lost, or export needs a higher tier | **High.** Treat as proprietary regardless of the licence. |
| No export you could run | **The answer.** |

## After the test

Put the result in writing to the supplier and ask for the **exit clause**: the format, the
timeframe and the cost of full data extraction at contract end. A supplier who will not put
that in writing has told you what the export is worth.

Record the test result in the repository's decision log (A16), with the date and the tool
versions. A tool re-evaluated in two years needs to know what was true this time.
