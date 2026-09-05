---
name: ea-method-runner
description: >-
  Run the five-phase EA lifecycle on a sector — Discover, Assess, Adapt, Plan, Execute and
  Govern — reading the A-numbered artefacts from the country workbook as inputs instead of
  asking for pastes, and writing each of the six deliverables back with a provenance header.
  Serves the whole of Module 4: the Discovery brief (4.2), the ranked gap analysis (4.3),
  the sourcing matrix (4.4), the target architecture (4.5), the wave roadmap (4.6) and the
  gate decision (4.7), plus the transfer plays — the transfer plan (4.8), the second-sector
  map (5.3) and the national rollout waves (5.6). Use when someone says "run the method on
  my sector", "draft my Discovery brief", "rank these gaps", "build the sourcing matrix",
  "design the target architecture", "sequence the roadmap", "run a gate decision", "take
  this to another sector", "what phase am I in". Calls bb-landscape-check at sourcing,
  target and gate — the 'authoritative and available' test is a fact, not a claim — and
  cite-or-discard when it audits a Discovery brief's source column. It holds the chain: for
  4.7 use this rather than ea-governance-drafter, which is for a gate with no workbook
  behind it.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
---

## What this skill does

Runs the five-phase method and produces its six deliverables, as `ea-lifecycle-method`
already does. What this extension adds is **chain discipline**: it reads the workbook
instead of asking for pastes, writes every output back with a provenance header, enforces
the output contract, and calls the two verification skills at the phases where the
safeguards demand them.

## Inputs

The A-numbered artefacts, per `references/workbook-chain.md`. Read what exists; name what
does not.

| Phase | Reads | Produces |
| --- | --- | --- |
| Discover (4.2) | A22 canvas, A0 §6, A0 §7 | A23 Discovery brief |
| Assess (4.3) | A23, A14 | A14 rev.2 ranked gap analysis |
| Adapt (4.4) | A14 rev.2, **BB status register** | A24 sourcing matrix |
| Plan — target (4.5) | A24, A11 principles, **BB status register** | A25 target architecture |
| Plan — roadmap (4.6) | A25, A3 cost case | A26 wave roadmap |
| Execute & Govern (4.7) | A26, A19 gate checklist, A7 rev.2 ToR, **BB status register** | A27 gate decision paper |
| Transfer (4.8, 5.3, 5.6) | A26, A0 §6 for the next sector | A28 transfer plan, A28 rev.2, A31 |

**No artefact, no guess.** If a phase's input is missing, name the artefact and the play
that produces it and stop — *"4.4 needs A14 rev.2; run 4.3 first"*. Never invent the input,
and never quietly proceed on a thinner one.

**Record the clarifying answers.** Where a phase needs a decision the workbook does not
carry, ask at most three questions at once and write the answers into the deliverable as an
*Inputs supplied by the learner* block. They are part of the artefact.

## Procedure

1. **Say which phase you are in and what it consumes**, in one line, before starting. A
   learner mid-chain loses track; the method's value is that it is sequential.

2. **Discover (4.2).** Build the brief from A22 and A0. Then **run `cite-or-discard` in
   audit mode** over it: which lines are sourced and which are the learner's or the model's
   assertion. That audit *is* the brief's source column — the play promises the column and
   this is what populates it.

3. **Assess (4.3).** Score and rank. The model ranks only what it was given: state, above
   the table, what was **not** captured and therefore could not be scored. A severity that
   touches a politically powerful body is flagged for the decision-maker, never softened.

4. **Adapt (4.4).** **Call `bb-landscape-check` first.** The build/buy/share/sandbox call
   depends on what is live, not on what is planned, and *share* against a block that is
   actually a pilot is the most expensive error in the whole method. For blocks the country
   does not have, `bb-sourcing-researcher` supplies the product options.

5. **Plan — target (4.5).** The path-to-acquire for each element depends on the BB status
   register; re-read it rather than trusting the matrix's copy if any time has passed.
   Check the target against the A11 principles.

6. **Plan — roadmap (4.6).** Sequence into waves. A wave that depends on a *planned* or
   *pilot* block carries that dependency explicitly, with the date the block must be live by.
   Cost from A3.

7. **Execute & Govern (4.7).** Run the gate against A19 and A7 rev.2. **Re-run
   `bb-landscape-check`** — the "authoritative and available" test is the gate's substance,
   and a status three months old has already been wrong once in this course's test runs.
   The gate decision states the decision, the evidence for it, and the conditions.

8. **Transfer (4.8, 5.3, 5.6).** Reuse A0 and the BB status register from the first sector;
   rebuild only the sector-specific bodies (hand off to `ea-institution-mapper` for the new
   sector's A0 §6). See `references/domain-transfer-guide.md`. The transferable part is the
   method and the shared blocks; the institutions are new every time.

9. **Each deliverable ends in its sign-off question** — the first four phases do, per
   `references/deliverable-templates.md`. Do not drop it. It is what returns the decision to
   the learner.

## Output contract

Provenance header first on **every** deliverable (`references/provenance-header.md`), with
**Consumed** naming the actual artefacts read, then the deliverable in the shape
`references/deliverable-templates.md` sets.

**Strip your own reasoning.** "The search confirms… let me now produce the matrix" is the
model talking to itself, and this output is the next phase's input. Nothing precedes the
header.

Text in the chat: tables and headed sections. No file, no diagram image, no chart — a
target architecture is a table of elements and relationships, not a picture. Posts, not
names. See `references/output-contract.md`.

Close each deliverable with its **sign-off question** and the safeguard.

## Safeguard handed back

The method produces defensible drafts. It does not produce decisions.

- **Every deliverable is signed off by a person.** The sign-off question at the end of each
  phase is not decoration — an unsigned Discovery brief means the Assess phase is ranking
  something nobody agreed to.
- **The model ranks only what you captured.** A gap not in the brief cannot be scored, and
  the highest-value gap is often the one nobody wrote down.
- **A share call needs a live block and an open door.** Confirm availability with the
  operator, not with the register — see the safeguard in `bb-landscape-check`.
- **A severity judgement that touches a powerful body** is validated with the decision-maker,
  not softened here. The honesty of the assessment is yours to defend.
- **A gate decision is the Board's**, not this skill's. It prepares the paper.

## References

- `references/deliverable-templates.md` — the six deliverables' shapes and their sign-off
  questions. Inherited from `ea-lifecycle-method`.
- `references/domain-transfer-guide.md` — what transfers between sectors and what does not.
  Inherited.
- `references/chain-discipline.md` — reading the workbook, what to do when an artefact is
  missing, and where the two verification skills are called.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` — the shared contract.
