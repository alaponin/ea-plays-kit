---
name: gif-four-layer-map
description: >-
  Assess one planned cross-agency data exchange at the four layers of interoperability of
  the European Interoperability Framework — technical, semantic, organisational, legal — and
  name the binding constraint: the KP2 play 1.2 that produces the four-layer exchange map
  (B2). Grades each layer from the registers the kit keeps rather than from the learner's
  description alone. Use when someone says "four layers", "which layer is missing", "is this
  exchange ready", "layer readiness", "what is blocking this exchange", "technical semantic
  organisational legal", "binding constraint", "EIF layers", "map this exchange", or names
  KP2 play 1.2.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
---

## What this skill does

This skill makes **B2, the four-layer exchange map**: one planned exchange, graded at the
four layers of the European Interoperability Framework — Ready, Partial or Missing — with
what is missing at each, the one action that closes it, and the single layer that is the
binding constraint right now.

The play's safeguard says why the skill exists: *a 'Ready' on the legal layer means you
told it a mandate exists, not that counsel has confirmed it*. The bare play grades from
the description. This skill grades from the **registers**: the BB status register
(`bb-landscape-check`) says whether a shared bus is live; the Bodies register
(`ea-institution-mapper`) says whether the provider has the mandate and whether a governing
body exists; the Legal register (`ea-legal-context`) says whether a lawful basis exists and
in which instrument. The integration map (A0 §9) says how the exchange happens today. A
grade with a register behind it carries the citation; a grade with only the learner's
description behind it carries ⚠.

The four layers are also the frame the whole KP2 uses: the decree is the legal layer's
configuration, the Governance Pack the organisational, the semantic map the semantic, the
contracts and wiring the technical. B2 is where a learner sees, for one exchange, which of
those four the later modules must build.

## Inputs

| Play | Makes | Needs |
| --- | --- | --- |
| 1.2 | B2 Four-layer exchange map | A0 §1 (the landscape); A0 §9 (the integration map — the row for this exchange); **the exchange, in 2–4 sentences** — which agency needs what from which, for what citizen-facing purpose |

Also useful: the three registers, dated within three months; A0 §7 and §10 for the legal
layer if the Legal register is absent; A0 §4 and §6 for the organisational layer.

If the learner names no exchange, ask for one, or offer the highest-value once-only
exchange from B3 if they have it. Ask at most three questions, together: the exchange; the
providing and consuming bodies if unclear; which registers exist. Record the answers in
the artefact.

## Procedure

1. **Name the exchange precisely.** Provider body · the register it holds · consumer body ·
   the service that needs the data · the entity exchanged · the citizen-facing purpose.
   Take the row from A0 §9 if it is there, and say how the exchange happens today.

2. **Grade the technical layer from the BB status register.** Is there a shared exchange
   layer, is it *live* (not pilot, not planned), is either body a member, does it carry
   REST or SOAP services, is there an approved standard both sides can use? Cite the
   register row. If no register: search the public sources the register would use and cite
   them, or mark ⚠.

3. **Grade the semantic layer from evidence.** Ready only if a published vocabulary or a
   national data standard for the entity is adopted by both bodies, with a citation. Partial
   if one side documents its schema. Missing if neither does, or if the two use different
   identifiers for the entity (A0 §1 usually says). Never grade the semantic layer Ready from
   the learner's description alone; say what evidence would change the grade.

4. **Grade the organisational layer from the Bodies register.** Does the provider have a
   mandate to serve the data to another body? Is there an agreement, a service level, a
   body that governs exchanges? Cite the register's mandate line and the governance line
   from A0 §4 (an ICT Steering Committee that met twice and not since is Missing, with a
   source).

5. **Grade the legal layer from the Legal register.** Is there a lawful basis for the
   provider to disclose and the consumer to process this entity for this purpose? Which
   instrument and section? Is the instrument in force? Does the data-protection act
   require anything more for this entity (a minor's data; a statutory basis rather than
   consent)? Cite it. If the register is absent, use A0 §7 and §10, mark ⚠ *register not
   consulted*, and say so.

6. **For each layer, write what is missing and the one action that closes it** — and name
   the KP2 module that builds it (legal → Module 2; organisational → Module 3; semantic and
   technical → Module 4).

7. **Name the binding constraint.** One layer. Say why it binds now: the layer whose
   absence stops the exchange even if the other three were ready today. State the
   evidence. If two layers tie, choose the one with the longer calendar (a decree takes
   longer than a service contract) and say so.

8. **Run `cite-or-discard`** on the citations before you give the output.

## Output contract

Write the provenance header first (`references/provenance-header.md`). Then:

- **The exchange** — the six-part statement of step 1, with today's mechanism.
- The map: `| Layer | Status (Ready / Partial / Missing) | Evidence (register row or source, tier, date) | What is missing | The one action that closes it | Built in |`
- **The binding constraint** — the layer, why, the evidence.
- **Inputs supplied by the learner**, then the safeguard.

Text in the chat, never a file. Posts, not names. Write no analysis before the header. See
`references/output-contract.md`.

## Safeguard handed back

**A grade reflects the register and the sources on the date in the header. A register more
than three months old is not evidence; run its skill again.**

- A legal-layer *Ready* means a cited instrument exists and is recorded as in force. It does
  not mean counsel has confirmed it applies to this exchange. Ask counsel that question
  (2.1 builds the fuller assessment).
- A technical-layer *Ready* means the bus is live. It does not mean either body is
  connected. Membership is an organisational and a legal act as much as a technical one.
- The binding constraint is a judgement on the evidence. Test it with the two bodies
  before it drives the sequence in B5.

## References

- `references/layer-rubric.md` — the grading rules per layer, the evidence each grade
  needs, and the typical "one action".
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` ·
  `references/workbook-chain-kp2.md` — the shared contract.
