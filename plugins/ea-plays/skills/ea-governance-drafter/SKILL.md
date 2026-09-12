---
name: ea-governance-drafter
description: >-
  Draft the standing institutional documents that an EA practice needs: the Governance Board
  terms of reference (1.7, 3.4), the phase RACI and role-gap list (1.6), the repository
  structure (3.1) and its update policy (3.3), the architecture review-gate checklist (3.5),
  the EA health scorecard (3.6) and the sustainment risk register (3.7, 5.2). It also drafts
  the KP2 Government Interoperability Framework Governance Pack and member documents: the
  governance RACI (3.3, B16), the member obligations and membership agreement (3.4, B17),
  the four Technical Working Group charters (3.5, B18), the change-control process with the
  standards register and semantic-registry charter (3.6, B19), the Member Requirements
  checklist (5.2, B29) and the Service-Level Agreement template (5.3, B30). Use when someone
  says "draft the Board ToR", "terms of reference for an architecture board", "build a RACI
  for the EA phases", "how should the repository be structured", "write the update policy",
  "review gate checklist", "EA metrics", "what will kill this programme in year two",
  "sustainment risks", "what do I ask my minister for", "member agreement", "membership
  obligations", "working group charter", "change control process", "standards register",
  "member requirements checklist", "SLA template". For a gate decision inside a running
  workbook chain (4.7), use ea-method-runner instead — this skill drafts the standing
  instrument, that one takes the decision.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
---

## What this skill does

This skill drafts the family of documents that occur again in Modules 1, 3 and 5. One skill
drafts all of them, because they are one family of artefacts. They are not seven separate
artefacts.

This skill uses references more than the web. The other skills in the kit do the opposite.
The templates in `references/` are the authority for the draft. Use the web only to find
**exemplars**: two or three published documents for each type, so that the learner can see
how a government wrote one.

## Inputs

| Document | Needs |
| --- | --- |
| Board ToR (1.7, 3.4) | The **legal register** from `ea-legal-context`, because the binding-decision scope must cite statutes that exist. The **roles register**, for the membership. A3, A6 and A8, if they exist. |
| Phase RACI (1.6) | The **roles register** from `ea-institution-mapper`, or A0 §4, with its confirmed, partial and gap tags. A4 and A5. |
| Repository structure (3.1) | A13, the BDAT skeleton, because the repository holds what the architecture describes. |
| Update policy (3.3) | A16 and the Board ToR, because the policy must name who enforces it. |
| Review-gate checklist (3.5) | The ToR, the principles (A11), and the **BB status register**, because a gate can point only at blocks that exist. |
| Health scorecard (3.6) | A16 and A18, because you can measure only what the repository records. |
| Sustainment risk register (3.7, 5.2) | A20 and A6, because in most countries the role gaps are the largest sustainment risk. |

**Do not draft a ToR without the legal register.** A binding-decision scope can cite a
statute that does not exist. The mandate of an agency can be coordinating where the ToR
assumes that it binds. This is the most damaging document that this kit can make. If the
register is missing, say so, and use `ea-legal-context`.

The same rule applies to the RACI. Without a roles register, the RACI names posts that can
be absent.

## Procedure

1. **Load the template** for the document type from `references/document-templates.md`.
   Draft from the template. Do not draft from your knowledge of governance documents.

2. **Fill the roles from the register, by post.** Keep the status tag on each role. Write a
   RACI row for a *gap* role as a gap. Give the phase that it blocks, and two or three
   options to resolve it. The August 2026 run used this pattern. It is more useful than a
   matrix that looks complete.

3. **Fill the binding scope from the legal register.** Quote the instrument and the section.
   Read the verb in the functions clause. The mandate of the coordinating body can be
   *coordinating* and not *binding*. Then the ToR cannot claim an authority that the
   instrument does not give. Say so, and draft the alternative: authority that comes from a
   spending gate, a cabinet directive, or a condition in a procurement. That paragraph is
   usually the most valuable paragraph in the document.

4. **Find two or three published exemplars** for each document type (T1): a national EA
   governance charter, a policy for digital spend control, a mandate for an architecture
   review board, or a published repository policy. Cite each one with its URL and one line
   on what to take from it. Use exemplars **for illustration only**. Never put the text of
   an exemplar into the draft. Run `cite-or-discard` on the URLs of the exemplars.

5. **Write what the document must not contain.** Each of these documents has one
   characteristic failure: a ToR with no quorum and no escalation path; a RACI with two
   Accountable roles; an update policy with no trigger; a gate checklist with no fail
   condition; a scorecard that measures activity and not re-use; a risk register with no
   owner for each risk. Name the failure, and do not make it.

6. **End the Board ToR with the four asks.** These are what the learner needs from the
   minister. This is the purpose of play 1.7.

## Output contract

Write the provenance header first (`references/provenance-header.md`). Then write the
document in the structure of the template. Then write these four sections:

- **Where authority comes from** — the instrument and the section behind each claim that the
  document binds. If it does not bind, say so, and say what would make it bind.
- **Exemplars** — two or three exemplars, with URLs and tiers, and one line on what each one
  does well.
- **What this document does not do** — the characteristic failure of this document type, and
  where this draft can still make that failure.
- **Next action** — a legal review for a ToR, adoption by the Board for a policy, or a named
  owner for each risk in a register.

Write text in the chat as markdown. **Do not make a `.docx`**, whatever the learner asks
for. The August 2026 run of play 1.7 made a `.docx`, and no play after it could read the
file. Posts, never names. Write no analysis before the header. See
`references/output-contract.md`.

## Safeguard handed back

**A governance document is a claim about authority. To draft one does not create any
authority.**

- **Legal counsel reviews the Terms of Reference** before it goes to a minister or a Board.
  Counsel reviews each statute citation, each claim of a binding decision, and each
  escalation path.
- **Confirm the roles with the persons who hold them.** A RACI that makes a post Accountable
  without the agreement of that post is a document that people ignore politely.
- **A gap in the roles register is a request for resources.** It is not a problem with the
  draft. The options in the RACI are options for the minister. They are not decisions that
  this skill takes.
- **A scorecard changes behaviour.** Check that each metric rewards re-use and not activity.
  A count of the models in the repository measures nothing that a person must improve.
- The exemplars are the documents of other countries. They show how a government wrote one.
  They are not text to adopt.

## KP2 plays

| KP2 play | Artefact | This skill supplies |
| --- | --- | --- |
| 3.3 | B16 — Governance RACI | one Accountable per decision, checked against the mandate each body holds (B14, B15) and, where the decision compels an agency, against the decree article |
| 3.4 | B17 — Member obligations and agreement | common, provider and consumer obligations from published member models (the NIIS X-Road ecosystems), cited; every enforcement power marked [confirm] against the legal layer |
| 3.5 | B18 — Four Working Group charters | Technical, Semantics, Security, Operations — with the authority each member must hold to bind their agency |
| 3.6 | B19 — Change control, standards register (with conformance fields) and semantic-registry charter | a process light enough to be used; the register's fields — standard, version, profile, binding date, transition, conformance approach, owner |
| 5.2 | B29 — Member Requirements checklist | an evidence column per requirement; the high-risk rows (clean data, lawful basis) named for spot-check |
| 5.3 | B30 — Service-Level Agreement template | pilot and production targets per service, each [confirm] with the provider |

Keep the regulator and the operator apart in every document, as B14 splits them. The
chain is in `references/workbook-chain-kp2.md`.

## References

- `references/document-templates.md` — the seven document structures, the function of each
  section, and the characteristic failure of each document type.
- `references/exemplar-search.md` — where governments publish governance documents, and how
  to see the difference between an adopted instrument and the draft of a consultant.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` ·
  `references/workbook-chain-kp2.md` — the shared contract.
