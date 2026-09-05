---
name: ea-legal-context
description: >-
  Assemble the national legal register that an EA programme touches: the data-protection
  act, the e-government or e-transactions law, the public procurement act, the statistics
  act, the civil registration and identity acts, the act that establishes the ICT agency or
  digital ministry, any e-government decree or cabinet directive, and the access-to-
  information act. Give each one with its citation, its status, the regulator that it
  creates, and the one line of it that matters for architecture. Serves the Governance Board
  ToR whose binding-decision scope must cite real statutes (1.7, 3.4), the principle card
  that dies if it cites the wrong statute (2.3), the body classification (2.4), the joint
  business-IT agenda's constraints (1.4) and the Discovery brief's legal collection area
  (4.2). Use when someone says "which laws apply", "what is the legal basis for sharing this
  data", "does the country have a data protection act", "cite the statute for this
  principle", "legal constraints on a shared platform", "can we share learner data", "what
  does the procurement law allow". Reads the national gazette and law portal first, then
  UNCTAD's Cyberlaw Tracker, DLA Piper's Data Protection Laws of the World, World Bank ID4D
  diagnostics and OGP action plans. It never drafts legal text and every output ends with
  the legal-counsel flag.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
---

## What this skill does

This skill builds the **legal register**. The register lists the instruments that an EA
programme touches. It gives the citation, the status, the regulator that the instrument
creates, and the one line of the instrument that constrains an architecture.

The skill exists because of one sentence in play 2.3: *a principle card that cites the
wrong statute will not survive its first challenge*. It also exists because a Governance
Board ToR with an invented scope for binding decisions does more damage than a ToR that
nobody wrote.

**This skill does not give legal advice. It does not write legal text.** It finds
instruments and says what they contain. Counsel does the interpretation.

## Inputs

The skill needs the country. It can also use a sector, which adds the sector act and the
data rules of that sector. It can also use a question, for example "can we share learner
data with the social register?". The skill then builds the register to answer that
question.

If the learner has A0 §7, add to it. Do not build it again. Section §7 is the first pass.
This skill adds the citation, the regulator, the history of amendments and the architecture
line.

## Procedure

1. **Search the national gazette or the law portal first** (T1). The gazette is the
   authority. A PDF on the site of a ministry can be an earlier version. If there is no
   portal, try the bill tracker of the parliament, then the ministry of justice, then
   FAOLEX, which contains much more than agriculture, then the legal repository of a
   regional body.

2. **Then search the trackers** (T2). They show what you did not find, and they help you to
   check a status. Use the UNCTAD Global Cyberlaw Tracker for data protection,
   e-transactions, cybercrime and consumer law. Use *Data Protection Laws of the World* by
   DLA Piper. Use the World Bank ID4D country diagnostics for identity law and civil-
   registration law. Use the OGP action plans for access-to-information and open-data
   commitments.

   A tracker tells you that an act **exists**. It does not give you the current text. Go
   from each tracker entry to the instrument.

3. **Record these items for each instrument**: the title · the year · the citation in its
   correct form · the **status**, which is in force, amended, bill, draft, repealed, or
   enacted but not commenced · the body that owns it · the **regulator that it creates**,
   if it creates one, and whether that regulator operates · **the one line that matters for
   EA**.

   *Enacted but not commenced* is a true state and a common one. The parliament passes an
   act, and a minister must make a commencement order that never comes. Use it as its own
   status. Never record it as *in force*.

4. **Establish that the text is current.** Search the title with the word "amendment", and
   then with the word "repeal". Look in the gazette index for the years after the act. Look
   at the site of the owning body for a later citation. If you cannot establish that the
   text is current, mark it ⚠ *currency not established*. Never give a clause as in force
   when you did not confirm it.

5. **Write the architecture line.** Write one sentence in the language of an architect on
   what the instrument does to a design. Do not summarise the act. Give the constraint.

   > *Data Protection Act 2023 §14: a legal basis is required for processing a minor's data;
   > parental consent is not sufficient for a statutory register, and is required for
   > anything beyond it. Consequence: a learner registry needs a statutory basis, not a
   > consent flow.*

6. **Record what a regulator can do. Do this separately from the existence of the law.** An
   act in force, and a regulator with six staff that has never enforced it, are two facts. A
   design depends on both facts. Say so.

7. **Run `cite-or-discard` before you give the output to the learner.** An invented section
   number in a Board ToR is the most damaging output that this kit can make.

## Output contract

Write the provenance header first (`references/provenance-header.md`). Then write this
table:

```
| Instrument | Citation | Year | Status | Owning body | Regulator created (operative?) | The one line that matters for EA | Source | Tier | Checked |
```

Then write these four sections in this order:

- **Answering the question asked**, if the learner asked a question. Give the instruments
  that apply, what each one permits, what each one forbids, and what the public record does
  not answer.
- **Gaps** — the instruments that an EA programme expects and that do not exist. Name them:
  no e-transactions act, no data-sharing regulation, no statistics act. An absence is a
  constraint on the design.
- **⚠ Currency not established** — each instrument whose history of amendments you could
  not confirm.
- **The legal-counsel flag**, which is below. Write it in each output. There is no
  exception.

Write text in the chat. Do not make a file. Posts, not names: cite the *office* that owns
an instrument, not the minister who signed it. Write no analysis before the header. See
`references/output-contract.md`.

## Safeguard handed back

**This register helps you to find instruments. It is not legal advice. No lawyer has read
it.**

Do these steps before any part of it goes into a Terms of Reference, a principle card, a
consent design, or a data-sharing agreement:

- **National counsel must confirm each citation and each status.** A search gives the
  original act more frequently than its amendments. A section that is repealed looks
  exactly like a section that is live.
- **Ask counsel the question. Do not give counsel the answer.** Ask "Does §14 permit this
  flow?". Do not write "we believe §14 permits this flow".
- Each item marked ⚠, *inferred*, or *currency not established* is not usable until a
  person confirms it.
- The register can say that an instrument does not exist. This means that there is no
  *public record* of the instrument. It does not mean that the instrument does not exist.

## References

- `references/instrument-checklist.md` — the instruments to look for, why each one applies
  to an architecture, and what its absence means.
- `references/law-sources.md` — where a country publishes its law, the trackers and what
  each one can prove, and how to establish that a text is current.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` — the shared contract.
