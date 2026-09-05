# The export test with ten entities

The scores in the comparison table are provisional until a tool passes this test. Run the
test yourself on each tool on the shortlist, before you sign a contract. It takes less than
one hour for each tool.

## Why a demo is not this test

A person who knows the tool runs a demo. The data in a demo has the shape that suits the
tool. The demo ends before the export. You run this test, on your data, and it ends only
when the file opens **without the tool**.

## The procedure

**1. Build the ten entities.** Use real entities from your own repository schema (A16). Do
not use the sample model of the tool. Ten entities show you everything:

- 3 capabilities;
- 2 data domains, and give **each one an attribute for its named owner**. The owner is the
  field that an export loses most frequently;
- 3 applications. **Map each one** to a minimum of one capability and one data domain;
- 2 technology elements;
- and a minimum of one **custom attribute** on one entity, such as a status, a source or a
  review date. An export that loses data loses the custom attributes first.

**2. Export the model** in each format that the vendor documents. Record which licence tier
each format needed.

**3. Open each file with a program that is not the tool.** Use a text editor for XML and
CSV. Use a different EA tool for the ArchiMate Exchange Format, because Archi is free and
reads it. Use a spreadsheet for CSV.

**4. Check these six items in the exported file:**

| Check | Pass |
| --- | --- |
| All ten entities are present | 10 of 10 |
| Each relationship is present | all of them, and you can identify both ends |
| The **owner** attribute of the data domain is present | yes |
| The **custom attribute** is present | yes |
| The **types** of the entities are preserved, and not flattened to a generic node | yes |
| You can read the file without the documentation of the tool | yes |

**5. Import the export into a *different* tool**, or into a new instance of the same tool.
Count what survived.

**6. Measure the time.** How long did the export take, and how many steps did it need? An
export that needs one day of work by an expert is not an exit path.

## Scoring

| Result | Meaning |
| --- | --- |
| The six checks pass, and the import is clean | **Low lock-in.** The models can leave. |
| The entities and the relationships survive, and the attributes are lost | **Medium.** You can exit with more work. Measure the work: how many attributes are in your real estate? |
| The relationships or the types are lost, or the export needs a higher tier | **High.** Treat the tool as proprietary, whatever its licence says. |
| There is no export that you could run | **This is the answer.** |

## After the test

Send the result to the supplier in writing. Ask for the **exit clause**: the format, the
timeframe, and the cost to extract all of the data at the end of the contract. A supplier
who refuses to write this down has told you the value of the export.

Record the result of the test in the decision log of the repository (A16), with the date and
the versions of the tools. In two years, a person evaluates the tool again, and that person
must know what was true this time.
