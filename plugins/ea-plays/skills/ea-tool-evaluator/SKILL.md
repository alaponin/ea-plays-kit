---
name: ea-tool-evaluator
description: >-
  Score EA tool candidates on facts that you can check online, not on the claims of a
  vendor: the licence and whether OSI lists it, the ArchiMate tool certification register of
  the Open Group, the export formats that the documentation gives, whether the user can
  extend the metamodel as the vendor's own documentation says, the published pricing page,
  and the DPGA registry for open tools such as Archi. Serves play 3.2 only, but 3.2 is where
  vendor marketing does the most damage. Use when someone says "which EA tool should we
  use", "compare Archi and [vendor]", "score EA tools", "is this tool open", "will we be
  locked in", "can we get our models out", "do we need a dedicated EA tool or is a
  spreadsheet enough", "ArchiMate certified tools". Returns the comparison table that the
  play asks for, and an export-test script: load ten entities, export them, and open the
  file without the tool. The safeguard says to score the export that you performed, not the
  export that the brochure promises. It asks two questions first: how many entities you will
  hold, and your budget posture.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
---

## What this skill does

This skill scores two to four candidate EA tools on attributes that you can **verify**. It
also gives the learner a test to run before the learner signs a contract.

It serves play 3.2 only. This narrow scope has a purpose. In this play the difference
between what a vendor says and what a tool does is largest, and the learner pays for a wrong
choice for ten years.

## Inputs

The inputs are two to four candidates and the requirements of the learner.

**Ask two questions before you score. Ask both at the same time.** The August 2026 run of
this play asked these two questions:

1. **How many entities** will the repository hold in year one and in year three? The answer
   decides whether the learner needs a dedicated tool.
2. **What is the budget posture?** Is there a budget for a licence, or must the tool be
   free?

Record both answers in the output, in an *Inputs supplied by the learner* block. The answers
change the recommendation, and the next reader must see them.

If the learner has A16, the repository structure, read it. The number of sections and the
relationship types are the true requirement.

**Say when the answer is "no tool yet".** Below a few hundred entities, a spreadsheet with
the A16 schema and a decision log is better than a tool that nobody maintains. This is a
correct output of this skill, and frequently the correct one.

## Procedure

Score only the attributes that you can check. For each candidate, do these nine steps:

1. **Licence.** Is the licence **on the OSI list**? Check the licence list at
   opensource.org for the exact name of the licence. Do not check for the word "open".
   In marketing, "open" also covers open-core products, free tiers, and source-available
   licences that are not open source. Record the name of the licence.

2. **ArchiMate certification.** Check the **tool certification register of the Open Group**.
   The result is certified, not certified, or certified at an older version. The register is
   a record, so the answer is a fact and not an opinion.

3. **Export formats in the documentation.** Take them from the **documentation of the
   vendor**, not from the feature list. Look for the ArchiMate Exchange Format and its
   version, CSV, OpenAPI, plain files, and an open database. Record where the documentation
   describes each format. A format that is only on a marketing page is *claimed*. It is not
   documented.

4. **Metamodel extensibility.** Can the user add entity types and relationships, as the
   documentation of the vendor says? The answer decides whether the tool can hold the PAERA
   metamodel, or only the metamodel of the tool.

5. **Pricing.** Use the **published** page. Record whether the price is for each user or for
   each instance. Record which tier the learner needs to get the export formats above,
   because an export behind an enterprise tier is a mechanism for lock-in. Record whether
   there is a public price. "Contact us" is a finding. Record it as one.

6. **DPGA registry.** For an open tool, record whether the registry recognises it as a
   digital public good.

7. **Lock-in assessment.** Use the facts above. Do not use a general impression. Ask three
   questions: is there a documented export, is the export in an open format, and is that
   export available at the tier that the learner can pay for?

8. **Run `cite-or-discard` on each claim.** As evidence of quality, a vendor page is in the
   "reject" tier. As evidence of what the vendor documents, a vendor page is Tier 1. Cite a
   vendor page for the second purpose only, and say which purpose you use.

9. **Give the export test to the learner.** The procedure is in `scripts/export-test.md`.
   The scores stay provisional until the learner runs the test.

## Output contract

Write the provenance header first (`references/provenance-header.md`). Then write these
five sections.

**Inputs supplied by the learner** — the two answers.

**Comparison table**

```
| Tool | Licence (OSI?) | ArchiMate certified | Documented exports | Metamodel extensible | Published price | DPGA | Lock-in risk | Sources |
```

Each cell that contains a claim also contains its source. If you could not verify a cell,
write **not documented**. Never leave the cell blank. Never write the adjective of the
vendor.

**Recommendation** — with the two or three attributes that decided it, and this condition:
*provisional until the export test passes*.

**The export test** — the script from `scripts/export-test.md`, filled in for these
candidates.

**What could not be verified** — each attribute with no documentation. This list is the
agenda for the negotiation.

Write text in the chat. Do not make a file. Write no analysis before the header. See
`references/output-contract.md`.

## Safeguard handed back

**A vendor can claim that a tool is "open" and that it "exports everything". Test the claim
with a real export of real data before you sign. A demo is not a test.**

- **Run the export test yourself**, with your own ten entities. Open the file **without the
  tool**. Score the export that you performed, not the export that the brochure promises.
- **Find the price of the export.** An open format that is only on the enterprise tier is
  not an exit path at your budget.
- **Ask for the exit clause in writing.** Ask for the data format, the timeframe, and the
  cost to extract the data at the end of the contract. A supplier who refuses to write it
  down has answered the question.
- **Read the certification register again before you sign.** Certifications end, and
  versions move.
- The recommendation here is provisional until the test passes.

## References

- `references/verifiable-attributes.md` — each attribute, where its register or its
  documentation is, and how vendors hide it.
- `scripts/export-test.md` — the export test with ten entities, step by step, with the pass
  criteria.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` — the shared contract.
