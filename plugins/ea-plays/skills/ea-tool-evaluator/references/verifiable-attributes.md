# The attributes, where to check them, and how vendors hide them

Score only what a register or the documentation of the vendor states. Everything else is
"not documented", and that is a finding.

| Attribute | Where the fact is | How it is hidden |
| --- | --- | --- |
| **Licence** | The list of approved licences at **opensource.org**. Check it against the exact name of the licence in the repository or the licence file of the tool | The word "open" covers open-core products, where the useful half is proprietary. It also covers a free tier, and a source-available licence that forbids the use that you need. Record the **name of the licence**. Then check the name against the OSI list. |
| **ArchiMate certification** | The **tool certification register of the Open Group** | A vendor gives a certification against an older version of ArchiMate as if it were current. Record the version that the register certifies. |
| **Export formats** | The **documentation** of the vendor. Use the manual, not the grid of features | A format on a marketing page that is not in the manual. Also a format that exists and loses data: it drops the relationships, the layout or the custom attributes. The manual usually says so in a note. |
| **Metamodel extensibility** | The documentation of the vendor about custom entity types and custom relationship types | "Customisable" that means colours and views, and not the metamodel. Look for whether a user can define a *new entity type*, not a new attribute. |
| **Pricing** | The **published pricing page** | There is no public price, and the page says "contact us". Record this as a finding, not as a blank cell. The vendor can also put the export or the API behind an enterprise tier, which turns an open format into a mechanism for lock-in. A price for each user can also become impossible when the CIOs of the sectors need read access. |
| **DPGA status** | The registry of the **Digital Public Goods Alliance** | Almost nothing. This is a simple register. |
| **Repository and activity** | For an open tool, the public repository: the last release, the open issues, and the number of contributors | A tool with one contributor is a dependency on one person. |

## Three questions that decide the lock-in

Answer these three questions from the facts above. Do not answer from an impression.

1. **Is there a documented export** of the full model, in the manual?
2. **Is the export in an open format** — the ArchiMate Exchange Format, CSV, or plain files
   that another tool reads?
3. **Is that export available at the tier that you can pay for?**

Three answers of yes mean low lock-in. One answer of no is the result, whatever the rest of
the table says.

## When the answer is "no tool"

Below a few hundred entities, a spreadsheet or a wiki with the A16 schema is better than a
tool that the practice cannot maintain. The A16 schema holds the capabilities, the data
domains with one named owner each, the applications mapped to both, the technology, and a
decision log. A dedicated EA tool in a small practice does not fail because of its cost. It
fails because one person learns it and then leaves.

Recommend the spreadsheet when it is the correct answer. The play asks for a scored
comparison. A comparison that ends with "not yet" is a valid result, and it is the honest
result more frequently than the market suggests.

## How to cite a page of a vendor

As evidence that a tool is *good*, the page of a vendor is in the "reject" tier. As evidence
of *what the vendor documents*, it is Tier 1. This skill scores what the vendor documents,
because you can hold a vendor to a documented claim. Cite the page for the second purpose,
and say which purpose you use.
