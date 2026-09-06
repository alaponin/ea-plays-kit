---
name: ea-method-runner
description: >-
  Run the five-phase EA lifecycle on a sector: Discover, Assess, Adapt, Plan, and Execute
  and Govern. Read the A-numbered artefacts from the country workbook as the inputs, instead
  of asking the learner to paste them. Write each of the six deliverables back with a
  provenance header. Serves all of Module 4: the Discovery brief (4.2), the ranked gap
  analysis (4.3), the sourcing matrix (4.4), the target architecture (4.5), the wave roadmap
  (4.6) and the gate decision (4.7). It also serves the transfer plays: the transfer plan
  (4.8), the national rollout waves (5.3) and the second-sector map (5.3b). Use when someone
  says "run the method on my sector", "draft my Discovery brief", "rank these gaps", "build
  the sourcing matrix", "design the target architecture", "sequence the roadmap", "run a
  gate decision", "take this to another sector", "what phase am I in". Calls
  bb-landscape-check at sourcing, target and gate, because the 'authoritative and available'
  test is a fact and not a claim. Calls cite-or-discard when it audits the source column of
  a Discovery brief. It holds the chain: for 4.7 use this skill and not
  ea-governance-drafter, which is for a gate with no workbook behind it.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
---

## What this skill does

This skill runs the five-phase method and makes its six deliverables. It adds **chain
discipline** to a bare method run. It reads the workbook instead of asking for pastes. It
writes each output back with a provenance header. It applies the output contract. It calls
the two verification skills at the phases where the safeguards need them.

## Inputs

The inputs are the A-numbered artefacts in `references/workbook-chain.md`. Read the
artefacts that exist. Name the artefacts that do not exist.

| Phase | Reads | Produces |
| --- | --- | --- |
| Discover (4.2) | A22 canvas, A0 §6, A0 §7 | A23 Discovery brief |
| Assess (4.3) | A23, A14 | A14 rev.2 ranked gap analysis |
| Adapt (4.4) | A14 rev.2, **BB status register** | A24 sourcing matrix |
| Plan — target (4.5) | A24, A11 principles, **BB status register** | A25 target architecture |
| Plan — roadmap (4.6) | A25, A3 cost case | A26 wave roadmap |
| Execute & Govern (4.7) | A26, A19 gate checklist, A7 rev.2 ToR, **BB status register** | A27 gate decision paper |
| Transfer (4.8, 5.3, 5.3b) | A26, A0 §6 for the next sector | A28 transfer plan, A28 rev.2, A31 |

**No artefact, no guess.** If the input to a phase is missing, name the artefact and the
play that makes it. Then stop. An example is *"4.4 needs A14 rev.2; run 4.3 first"*. Never
invent the input. Never continue with less input and say nothing.

**Record the answers to your questions.** A phase can need a decision that the workbook does
not contain. Then ask a maximum of three questions at the same time. Write the answers into
the deliverable in an *Inputs supplied by the learner* block. The answers are part of the
artefact.

## Procedure

1. **Say which phase you are in, and what the phase consumes.** Write one line before you
   start. A learner in the middle of the chain loses the sequence. The value of the method
   is that it is sequential.

2. **Discover (4.2).** Build the brief from A22 and A0. Then **run `cite-or-discard` in
   audit mode** on the brief. The audit says which lines have a source, and which lines are
   an assertion by the learner or the model. That audit is the source column of the brief.
   The play promises the column, and this step fills it.

3. **Assess (4.3).** Score the gaps and rank them. The model ranks only the material that
   you gave it. Above the table, say what you did **not** capture and therefore could not
   score. If a severity applies to a body with political power, flag it for the
   decision-maker. Never make it weaker.

4. **Adapt (4.4).** **Call `bb-landscape-check` first.** The decision to build, buy, share
   or sandbox depends on the blocks that are live, not on the blocks that are planned. To
   share against a block that is only a pilot is the most expensive error in the method. For
   the blocks that the country does not have, `bb-sourcing-researcher` gives the product
   options.

5. **Plan — target (4.5).** The path to acquire each element depends on the BB status
   register. If time has passed, read the register again. Do not trust the copy in the
   matrix. Check the target against the A11 principles.

6. **Plan — roadmap (4.6).** Put the work into waves. If a wave depends on a *planned* block
   or a *pilot* block, write that dependency, with the date on which the block must be live.
   Take the costs from A3.

7. **Execute and Govern (4.7).** Run the gate against A19 and A7 rev.2. **Run
   `bb-landscape-check` again.** The test for "authoritative and available" is the substance
   of the gate. In the test runs of this course, a status three months old was already wrong
   one time. The gate decision gives the decision, the evidence for it, and the conditions.

8. **Transfer (4.8, 5.3, 5.3b).** Use A0 and the BB status register from the first sector
   again. Build only the bodies of the new sector again, and use `ea-institution-mapper` for
   the A0 §6 of that sector. See `references/domain-transfer-guide.md`. The method and the
   shared blocks transfer. The institutions are new each time.

9. **End each deliverable with its sign-off question.** The first four phases each have one,
   in `references/deliverable-templates.md`. Do not remove it. It gives the decision back to
   the learner.

## Output contract

Write the provenance header first on **each** deliverable
(`references/provenance-header.md`). In **Consumed**, name the artefacts that you read.
Then write the deliverable in the shape that `references/deliverable-templates.md` gives.

**Remove your own analysis.** "The search confirms… let me now make the matrix" is the model
that speaks to itself. This output is the input to the next phase. Nothing comes before the
header.

Write text in the chat: tables and sections with headings. Do not make a file, an image of a
diagram, or a chart. A target architecture is a table of elements and relationships. It is
not a picture. Posts, not names. See `references/output-contract.md`.

End each deliverable with its **sign-off question** and its safeguard.

## Safeguard handed back

The method makes drafts that you can defend. It does not make decisions.

- **A person signs off each deliverable.** The sign-off question at the end of each phase
  has a function. If nobody signs the Discovery brief, the Assess phase ranks material that
  nobody agreed to.
- **The model ranks only what you captured.** It cannot score a gap that is not in the
  brief. The gap with the highest value is frequently the gap that nobody wrote down.
- **A share decision needs a live block and an open door.** Confirm availability with the
  operator, not with the register. See the safeguard in `bb-landscape-check`.
- **Validate a severity that applies to a powerful body with the decision-maker.** Do not
  make it weaker here. You must defend the honesty of the assessment.
- **The gate decision belongs to the Board.** It does not belong to this skill. This skill
  prepares the paper.

## References

- `references/deliverable-templates.md` — the shape of the six deliverables and their
  sign-off questions. Inherited.
- `references/domain-transfer-guide.md` — what transfers between sectors and what does not.
  Inherited.
- `references/chain-discipline.md` — how to read the workbook, what to do when an artefact
  is missing, and where to call the two verification skills.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` — the shared contract.
