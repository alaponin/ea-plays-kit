---
name: gif-consistency-check
description: >-
  Cross-check the documents of a Government Interoperability Framework against each other
  and report every contradiction as a question for a human — never as a ruling. Two KP2
  plays: the legal acceptance check, which tests whether the decree's articles authorise
  exactly the exchanges in the Use-Case Catalogue (2.6, B13); and the document-consistency
  report, which reads the decree, the Governance Pack and the standards portfolio side by
  side (5.9, B36). Use when someone says "does the decree cover the catalogue", "legal
  acceptance check", "which exchanges are not authorised", "does this article over-reach",
  "cross-check the decree and the governance pack", "document drift", "are these three
  documents consistent", "consistency report", "which is correct". It decides nothing.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
---

## What this skill does

This skill compares documents that the learner wrote against each other. It finds where
they disagree. It does not decide which one is right. Whether the decree or the catalogue
is correct is a legal and governance judgement that a person owns.

Two plays use it. **2.6, the legal acceptance check**, compares two documents: the
Use-Case Catalogue (B5) and the draft Articles (B11). It tests one thing — that the decree
authorises exactly the exchanges the framework intends to carry. **5.9, the
document-consistency report**, compares three: the decree (B11, or the whole Articles
package), the Governance Pack (B14–B19; at minimum B19) and the standards portfolio (B22).
Both plays produce a table of contradictions, each with a question.

The skill adds three things to the bare play. It quotes the **passage on each side** of a
finding, with its location, so that a reviewer can see the contradiction without opening
both documents. It **orders** the findings by the damage a reviewer would do with them. And
where a finding turns on an external fact — the current version of a standard, the text of
a statute the decree cites — it **checks that fact** and cites it, instead of leaving the
question open when a source can close it.

## Inputs

| Play | Makes | Needs |
| --- | --- | --- |
| 2.6 | B13 Legal acceptance check | B5 the Use-Case Catalogue; B11 the draft Articles (all articles drafted so far) |
| 5.9 | B36 Document-consistency report | B11 the decree; B19 (and any of B14–B18 the learner has); B22 the standards portfolio |

The learner pastes the documents. If one is missing, name it and stop; a consistency check
with one document is not a check. If the learner pastes a summary rather than the text,
say that the findings are about the summary, and mark the header's Unverified count
accordingly.

Ask at most three questions, together, before you start — for 5.9 the usual one is which
version of each document is current, because drift between versions is itself a finding.

## Procedure

1. **Index each document before you compare.** For B5: each exchange, with its provider,
   consumer, entity and stated legal-readiness flag. For B11: each article and clause that
   authorises, mandates, permits or restricts an exchange, and the bodies it names. For
   B19 and the Governance Pack: each body, role and decision. For B22: each standard, its
   version, profile and binding date. Write the index as tables in the output, after the
   findings; it is what the reviewer checks your findings against.

2. **Run the checks the play names — and only those.** For 2.6: COVERAGE, each catalogue
   exchange → the clause that gives it a lawful basis, or NOT COVERED; SCOPE, each
   authorising article → whether every exchange it permits is in the catalogue and within
   the principles, or OVER-REACHES. For 5.9: the four checks — standards not authorised,
   referenced or at a different version; roles and bodies present in one document and not
   another; exchanges authorised but not implemented, or implemented but not authorised;
   key terms (*member*, *service*, *authority*, *authoritative source*, *subsystem*) used
   inconsistently.

3. **Quote both sides.** For each finding, the passage in document A and the passage in
   document B, each with its location (article, clause, row, section). A finding with no
   passage is an impression, not a finding; drop it.

4. **Check the external fact where one exists.** A version mismatch between B22 and the
   decree is a finding; which version is current is a fact — fetch the standard's own
   publication and cite it (`references/source-tiers.md`). A citation in the decree to a
   statute is a fact — if the legal register is available, check it. Report the fact beside
   the finding. The question for the human remains: *which document should change?*

5. **Order by damage.** First, a finding that would make an exchange unlawful if a
   reviewer found it (an exchange in production with no authorising article). Then one that
   would make a member non-conformant (a version mismatch). Then a governance gap (a role
   with no body). Then a terminology drift. `references/finding-rubric.md` gives the
   order and the question shape for each.

6. **Write a question, not a verdict.** Each row ends with the question a human must
   answer: *"Does the decree's Article 4 cover exchange #7, or should #7 leave the
   first wave?"* Never *"the catalogue is wrong"*.

7. **Run `cite-or-discard`** on every external fact from step 4 before you give the
   output. A version or a statute the fetched source does not confirm is *not supported*:
   remove the fact, keep the finding, and say the fact is unchecked. The passages quoted
   from the learner's own documents are not citations and are not checked this way.

## Output contract

Write the provenance header first (`references/provenance-header.md`). Then:

For **2.6**: the coverage table `| Catalogue exchange | Authorising article and clause | Status (COVERED / NOT COVERED / PARTIAL) | Passage | Question |`; the list of NOT COVERED exchanges with a one-line note on the fix; the list of OVER-REACHING articles with the exchanges they permit that the catalogue does not carry, and a one-line note on the fix.

For **5.9**: the contradiction table `| # | Finding | Document A (passage, location) | Document B (passage, location) | External fact checked (source, tier, date) | Damage rank | Question for a human |`, ordered by damage rank.

Then, for both: the indexes from step 1; the **Inputs supplied by the learner** block;
and the safeguard below. Text in the chat, never a file. Posts, not names. Write no analysis
before the header. See `references/output-contract.md`.

## Safeguard handed back

**This check tests alignment between documents you wrote. It is not a ruling on whether an
article is lawful or well drafted, and it must not resolve the drift it finds.**

- Take each question to the body that owns the document: the legal drafter for the
  decree, the Steering Committee for the Governance Pack, the standards owner named in
  B19 for the portfolio.
- A COVERED status means that a clause exists whose words reach the exchange. Whether
  the clause is lawful, in force and enforceable is counsel's finding, not this check's.
- An OVER-REACH is a drafting observation. Some over-reach is deliberate — a decree may
  authorise more than the first wave carries. Ask the drafter whether it is.
- Run 5.9 again whenever one of the three documents changes. A report is dated; the
  documents move.

## References

- `references/finding-rubric.md` — the damage order, the question shape for each finding
  type, and the terms that drift most often.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` ·
  `references/workbook-chain-kp2.md` — the shared contract.
