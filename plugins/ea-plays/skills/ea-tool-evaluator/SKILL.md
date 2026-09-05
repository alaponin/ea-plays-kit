---
name: ea-tool-evaluator
description: >-
  Score EA tool candidates on facts that can be checked online rather than on vendor claims —
  licence (OSI-listed or not), the Open Group's ArchiMate tool certification register,
  documented export formats, whether the metamodel is user-extensible per the vendor's own
  documentation, the published pricing page, and the DPGA registry for open tools such as
  Archi. Serves play 3.2 only, but 3.2 is where vendor marketing does the most damage. Use
  when someone says "which EA tool should we use", "compare Archi and [vendor]", "score EA
  tools", "is this tool open", "will we be locked in", "can we get our models out", "do we
  need a dedicated EA tool or is a spreadsheet enough", "ArchiMate certified tools". Returns
  the comparison table the play asks for plus an export-test script — load ten entities,
  export, open the file without the tool — because the safeguard says to score the export
  you performed, not the one the brochure promises. Expect it to ask two questions first:
  how many entities you will hold, and your budget posture.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
---

## What this skill does

Scores two to four candidate EA tools on **verifiable** attributes, and hands back a test
the learner runs themselves before signing anything.

It serves 3.2 alone. The narrowness is the point: this is the play where the gap between
what a vendor says and what a tool does is widest, and where a wrong choice is paid for
over a decade.

## Inputs

Two to four candidates and the learner's requirements. **Ask two questions before scoring**,
both at once — the August 2026 run showed this play asking exactly these:

1. **How many entities** will the repository hold in year one and year three? (This decides
   whether a dedicated tool is warranted at all.)
2. **Budget posture** — is there a licence budget, or must this be free?

Record both answers in the output as *Inputs supplied by the learner*. They change the
recommendation and the next reader needs to see them.

If the learner has A16, the repository structure, read it — the section count and the
relationship types are the real requirement.

**Say when the answer is "no tool yet".** Under a few hundred entities, a spreadsheet with
the A16 schema and a decision log beats a tool nobody maintains. Recommending that is a
legitimate output of this skill and often the right one.

## Procedure

Score only what can be checked. For each candidate:

1. **Licence** — is it **OSI-listed**? Check opensource.org's licence list for the exact
   licence named, not for the word "open". "Open" in marketing covers open-core, free tiers,
   and source-available licences that are not open source. Record the licence name.

2. **ArchiMate certification** — check **the Open Group's tool certification register**.
   Certified / not certified / certified at an older version. This is a register, so the
   answer is a fact and not an opinion.

3. **Export formats, documented** — from the **vendor's own documentation**, not the feature
   list: ArchiMate Exchange Format (and which version), CSV, OpenAPI, plain files, an
   open database. Record where in the documentation each format is described. A format
   mentioned only on a marketing page is *claimed*, not documented.

4. **Metamodel extensibility** — can the user add entity types and relationships, per the
   vendor's own documentation? This decides whether the tool can hold the PAERA metamodel or
   only its own.

5. **Pricing** — the **published** page. Per user or per instance; what tier is needed for
   the export formats above (export behind an enterprise tier is a lock-in mechanism);
   whether there is a public price at all. "Contact us" is a finding — record it as such.

6. **DPGA registry** — for open tools, whether it is a recognised digital public good.

7. **Lock-in assessment** — from the facts above, not from a general impression: can the
   models leave? Three questions — is there a documented export, is it in an open format,
   and is that export available at the tier you can afford?

8. **Run `cite-or-discard`** on every claim. Vendor pages are Tier "reject" as *evidence of
   quality* but Tier 1 as *evidence of what the vendor documents* — cite them for the second
   only, and say which you are doing.

9. **Hand over the export test.** `scripts/export-test.md` is the procedure. The scoring is
   provisional until the learner has run it.

## Output contract

Provenance header first (`references/provenance-header.md`), then:

**Inputs supplied by the learner** — the two answers.

**Comparison table**

```
| Tool | Licence (OSI?) | ArchiMate certified | Documented exports | Metamodel extensible | Published price | DPGA | Lock-in risk | Sources |
```

Every cell that is a claim carries its source. A cell you could not verify says **not
documented** — never blank, and never the vendor's adjective.

**Recommendation** — with the reason stated as the two or three attributes that decided it,
and the condition: *provisional until the export test passes*.

**The export test** — the script from `scripts/export-test.md`, filled in for these
candidates.

**What could not be verified** — every attribute where documentation was absent. This list
is the negotiation agenda.

Text in the chat. No file. No reasoning before the header. See
`references/output-contract.md`.

## Safeguard handed back

**Vendor claims of "open" and "exports everything" must be tested with a real export of real
data before you sign. A demo is not a test.**

- **Run the export test yourself**, on your own ten entities, and open the file **without
  the tool**. Score the export you performed, not the one the brochure promises.
- **Check what the export costs.** An open format available only on the enterprise tier is
  not an exit path at your budget.
- **Ask for the exit clause in writing** — data format, timeframe, and cost of extraction at
  contract end. A supplier who will not put it in writing has answered the question.
- **Re-check the certification register** before signing; certifications lapse and versions
  move.
- The recommendation here is provisional until the test passes.

## References

- `references/verifiable-attributes.md` — each attribute, where the register or
  documentation is, and how vendors obscure it.
- `scripts/export-test.md` — the ten-entity export test, step by step, with the pass
  criteria.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` — the shared contract.
