---
name: ea-comparator-evidence
description: >-
  Find comparator countries that truly resemble the learner's country, and record what each
  one built, from its published EA framework or its digital-government coordination
  instrument. Give three to five cards, a Tier 1 source for each claim, one transferable
  mechanism for each country, and a minimum of one contested or mixed case with both sides
  cited. Serves the comparator signposts play (1.8) and the evidence play (5.1), and feeds
  the proof section of the ministerial business case (5.4) and the closing case (5.7).
  Use when someone says "which countries are like mine", "find comparator countries", "has
  anyone actually done this", "is this proven or just theory", "what did Rwanda/Ghana/
  Estonia actually build", "give me evidence for the minister", "show me a country that
  failed at this", "signpost countries for my context". Selects by World Bank income
  classification, population band, governance type and region, with priority to African and
  developing-country examples; reads published national EA frameworks, the UN EGDI, the
  World Bank GovTech Maturity Index and the OECD Digital Government Index. Runs
  cite-or-discard on itself before returning — the 1.8 test run produced comparators sourced
  to document mirrors and blog posts, and this is the fix.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
---

## What this skill does

This skill selects comparator countries against criteria that it states. For each country
it records what the country built. Each claim has a primary source. Each card gives one
mechanism that the learner's country can adopt.

The August 2026 run of play 1.8 gave five comparators with URLs. This was better than the
four signposts in the video, which had no sources. But some of those URLs were document
mirrors and Medium posts. This skill makes the sources survive a check. It also stops the
set from becoming a list of successes.

## Inputs

**A0 §5, the country-characteristics one-liner.** This is the only input.

If the learner does not have §5, build it, or use `country-context-pack`. Comparators
selected without §5 come from the impression that the model has of the country. That is how
Estonia becomes a comparator for a country of 200 million people.

If the learner has A8 from an earlier run, add to it and verify it again. Do not start
again.

## Procedure

1. **State the selection criteria before you select.** Write the income classification, the
   population band, the type of governance, the region, and the maturity signal. For the
   type of governance, give unitary or federal, and the level of sub-national autonomy.
   Then say which countries agree with the criteria. Nobody can argue with a comparator set
   that does not state its criteria, and somebody will argue with it.

2. **Give priority to examples from Africa and from developing countries.** A minister who
   sees Estonia and Singapore sees countries with a different fiscal reality and a different
   institutional reality, and knows it. Estonia earns a place for one transferable
   mechanism, such as X-Road governance or the once-only obligation in law. It does not earn
   a place as a general model.

3. **Use the maturity indices as the signal for comparability. Do not use them as the
   finding.** The indices are the UN E-Government Survey EGDI, the World Bank GovTech
   Maturity Index, and the OECD Digital Government Index. They tell you that a country is
   comparable. They do not tell you what the country built.

4. **Find what each comparator built.** Use its **published EA framework** or its
   digital-government coordination instrument (T1). These are known starting points: the
   GEA of Kenya, the GEA of Ghana, the GWEA of South Africa, the RISA framework of Rwanda,
   IndEA of India, and the X-Road governance of Estonia. Search for other countries. Do not
   use only this list. Peer-reviewed case studies are T1. Donor evaluations are T2.

   The card records **the instrument**, not the intention. Give the framework as published,
   the act or directive that made it binding, and what the record says happened after it.

5. **Find the transferable mechanism.** Give one mechanism for each card. It is the specific
   device that this country used and that the learner's country can adopt. The 2026 test run
   found the "Technical Clearance" of Liberia and a spending-gate authority. That is the
   level of detail to give. "They had political commitment" is not a mechanism.

6. **Include a minimum of one contested or mixed case. Cite both sides.** This is
   mandatory. Examples are a national ID that a court ruled unlawful, a platform that
   stopped, a framework that a government published and never applied, and a cost overrun
   that a government disputes. Cite the judgment of the court or the report of the auditor
   **and** the response of the government. Journalism with a named outlet (T3) is correct
   here, and you must add the primary source to it.

   A set of five successes is not evidence. It is a brochure, and an advisor to a minister
   will find the counter-example that you left out.

7. **Bring the recurring elements together.** Give what is in three cards or more. This
   synthesis goes into plays 5.4 and 5.7. The individual cards do not.

8. **Run `cite-or-discard` on your own output before you give it to the learner.** Read
   every URL. Follow every mirror to its primary source. Grade every claim. This step is
   mandatory, and you name it in the output.

## Output contract

Write the provenance header first (`references/provenance-header.md`). Then write these
five sections.

**Selection criteria** — the five criteria with the values for the learner's country, and
the countries that agree with them.

**Comparator cards** — three to five cards. Use this shape:

```
### <Country> — <one-line why it is comparable>
| | |
| --- | --- |
| **Comparable because** | income · population · governance · region · maturity index and rank |
| **What it built** | the framework or instrument, with its year |
| **Made binding by** | the act, directive or spending gate — or "not binding" |
| **Documented since** | what the record says happened, with dates |
| **Transferable mechanism** | the one device this country could adopt |
| **Sources** | URL · tier · checked on — one row per claim above |
```

**Contested case** — its own card, with both sides cited, and one line on what the dispute
means for the learner's country.

**Recurring elements** — what is in three cards or more, and what is in no card.

**Verification summary** — the result from `cite-or-discard`: how many claims you kept,
wrote again, dropped and marked ⚠; which sources were mirrors; and whether you found the
primary source.

Write text in the chat. Use tables, not charts. Posts, not names. Write no analysis before
the header. See `references/output-contract.md`.

## Safeguard handed back

Comparators persuade people. This is why they are dangerous.

- **Read the two or three sources that the argument depends on** before this output goes to
  a minister. A framework that a government published is not a framework that a government
  applies. Every comparator argument fails at that difference under questioning.
- **Check the dates.** A framework from 2019 can be superseded. The agency can have changed
  its structure two times after it.
- **Prepare for the counter-example.** You included one contested case. The room can know
  another one. It is better to have searched for it.
- **A mechanism transfers only with the conditions that it needs.** The technical clearance
  of Liberia works because something gives it power. Name that thing in your country, or say
  that it is missing. That absence is the true finding.
- Each item marked ⚠ is unverified. It is not verified as true.

## References

- `references/comparator-selection.md` — the five criteria, how to make bands from them, and
  how each one fails.
- `references/known-frameworks.md` — the national EA frameworks and coordination instruments
  that were published when this file was written, what each one is and is not, and the
  contested cases to know. Use it to start a search. Do not use it in place of a search.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` — the shared contract.
