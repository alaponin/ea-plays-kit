---
name: ea-governance-drafter
description: >-
  Draft the institutional documents an EA practice runs on, from the kit's own templates
  rather than from general knowledge, with the roles taken from a real roles register and
  the binding scope citing real statutes. Covers the Governance Board terms of reference
  (1.7, 3.4), the phase RACI and role-gap list (1.6), the repository structure (3.1) and its
  update policy (3.3), the architecture review-gate checklist (3.5), the EA health scorecard
  (3.6) and the sustainment risk register (3.7, 5.2). Use when someone says "draft the Board
  ToR", "terms of reference for an architecture board", "build a RACI for the EA phases",
  "how should the repository be structured", "write the update policy", "review gate
  checklist", "EA metrics", "what will kill this programme in year two", "sustainment
  risks", "what do I ask my minister for". Consumes the legal register so the
  binding-decision scope cites statutes that exist, and the roles register so the RACI names
  posts that exist. Cites two or three published real-world exemplars per document type.
  For a gate decision inside a running workbook chain (4.7), use ea-method-runner instead —
  this skill drafts the standing instrument, that one takes the decision.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
---

## What this skill does

Drafts the family of documents that recur across Modules 1, 3 and 5 — one skill, because
they are one artefact family, not seven unrelated ones.

Unlike the rest of the kit it is **reference-grounded rather than web-heavy**: the drafting
authority is the templates in `references/`, and the web is used for **exemplars only** —
two or three published real-world documents per type, so the learner can see how an actual
government wrote it.

## Inputs

| Document | Needs |
| --- | --- |
| Board ToR (1.7, 3.4) | The **legal register** from `ea-legal-context` — the binding-decision scope must cite statutes that exist. The **roles register** — membership. A3, A6, A8 where they exist. |
| Phase RACI (1.6) | The **roles register** from `ea-institution-mapper` or A0 §4, with its confirmed/partial/gap tags. A4, A5. |
| Repository structure (3.1) | A13, the BDAT skeleton — the repository holds what the architecture describes. |
| Update policy (3.3) | A16 and the Board ToR — the policy has to name who enforces it. |
| Review-gate checklist (3.5) | The ToR, the principles (A11), and the **BB status register** — a gate can only point at blocks that exist. |
| Health scorecard (3.6) | A16 and A18 — you can only measure what the repository records. |
| Sustainment risk register (3.7, 5.2) | A20 and A6 — the role gaps are the largest sustainment risk in most countries. |

**Do not draft a ToR without the legal register.** A binding-decision scope that cites a
statute which does not exist, or an agency mandate that is coordinating where the ToR
assumes binding, is the single most damaging document this kit can produce. If the register
is missing, say so and hand off to `ea-legal-context`.

Same rule for the RACI: without a roles register it names posts that may not exist.

## Procedure

1. **Load the template** for the document type from `references/document-templates.md`.
   Draft from it, not from what a governance document generally looks like.

2. **Fill the roles from the register, by post**, carrying the status tag through. A RACI
   row against a *gap* role is written as a gap with the phase it blocks and two or three
   resolution options — that is the pattern the August 2026 run produced and it is more
   useful than a tidy matrix.

3. **Fill the binding scope from the legal register.** Quote the instrument and the section.
   Where the coordinating body's mandate is *coordinating* rather than *binding* — check the
   verb in the functions clause — the ToR cannot assert authority the instrument does not
   grant. Say so, and draft the alternative: authority borrowed from a spending gate, a
   cabinet directive, or a procurement condition. That paragraph is usually the most
   valuable one in the document.

4. **Find two or three published exemplars** per document type (T1): a national EA
   governance charter, a digital spend-control policy, an architecture review board mandate,
   a published repository policy. Cite them with URLs and one line each on what to steal
   from them. **Illustration only** — never merge exemplar text into the draft.
   Run `cite-or-discard` on the exemplar URLs.

5. **Write what the document must not contain.** Every one of these has a characteristic
   failure: a ToR with no quorum and no escalation path; a RACI with two Accountables; an
   update policy with no trigger; a gate checklist with no fail condition; a scorecard
   measuring activity instead of re-use; a risk register with no owner per risk. Name the
   failure and avoid it.

6. **End with the four asks** where the document is the Board ToR — what the learner needs
   from the minister. That is 1.7's actual purpose.

## Output contract

Provenance header first (`references/provenance-header.md`), then the document, in the
template's structure, then:

- **Where authority comes from** — the instrument and section behind every binding claim,
  or the explicit statement that it is not binding and what would make it so.
- **Exemplars** — two or three, with URLs, tiers, and one line each on what they do well.
- **What this document does not do** — the characteristic failure mode, and where this
  draft could still fall into it.
- **Next action** — legal review for a ToR, Board adoption for a policy, a named owner per
  risk for a register.

Text in the chat, as markdown — **not a `.docx`**, whatever the learner asks. The August
2026 run of 1.7 produced a `.docx` and nothing downstream could read it. Posts, never names.
No reasoning before the header. See `references/output-contract.md`.

## Safeguard handed back

**A governance document is a claim about authority, and drafting one does not create any.**

- **Legal counsel reviews the Terms of Reference** before it goes to a minister or a Board.
  Every statute citation, every binding-decision claim, every escalation path.
- **The roles must be confirmed with the people in them.** A RACI that makes a post
  Accountable without that post's agreement is a document that will be ignored, politely.
- **A gap in the roles register is a resourcing ask**, not a drafting problem. The
  resolution options in the RACI are options for the minister, not decisions taken here.
- **A scorecard changes behaviour.** Check that each metric rewards re-use rather than
  activity — a count of models in the repository measures nothing anyone should optimise.
- The exemplars are other countries' documents. They are illustrations of how a real
  government wrote it, not text to adopt.

## References

- `references/document-templates.md` — the seven document structures, what each section is
  for, and the characteristic failure of each document type.
- `references/exemplar-search.md` — where published governance documents live and how to
  tell an adopted instrument from a consultant's draft.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` — the shared contract.
