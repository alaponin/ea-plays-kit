---
name: paera-reference-check
description: >-
  Look up what PAERA says, and check work against PAERA as published — the section, its
  words and its public address, read on the day, never from memory — and not against the
  simplification that the videos teach. It carries the map of PAERA's sections with their
  public addresses, the ten principles and the capability ladder as tests, and a glossary;
  it carries no PAERA text. Serves the five-foundations map (1.5), the metamodel
  conformance check (2.2) and the principle card (2.3) of the EA course, runs beside
  `ea-comparator-evidence` in the interoperability plays 1.7 and 4.3, and answers a PAERA
  question on any course page that cites a PAERA section. Use when someone says "what does
  PAERA say about", "cite PAERA on", "which PAERA section covers this", "check this
  against PAERA", "is this metamodel conformant", "map our initiatives to the five
  foundations", "what does PAERA actually say about principles", "adopt a PAERA principle
  for my country", "which principle covers this", "what capability level is this body",
  "the capability ladder", "is this entity type in the metamodel", "PAERA compliance
  check".
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
---

## What this skill does

This skill does two jobs with **PAERA as published**.

1. **It looks up.** A learner asks what PAERA says on a point. The skill finds the
   section, reads the public page today, and gives the section number, what the section
   says, the public address and the date it read the page.
2. **It checks.** A learner gives a draft model, an initiative list, a principle or a
   plan. The skill checks it against PAERA as published, and says where the video
   applied a simplification.

The two jobs use the same discipline. The skill never gives PAERA's words from memory.
It gives them from the public page that it read today, or it says that it could not
read the page.

**This skill carries no PAERA text.** The licence of PAERA's text is not confirmed. On
6 October 2026 the footer of the GovStack specification site read "Apache-2.0 license";
this kit does not say what that means for the text. So the skill carries only what
points to the text: the map of sections and their addresses
(`references/paera-index.md`), the principles and the capability ladder written as
tests in the kit's own words (`references/paera-tests.md`), and a glossary in the kit's
own words (`references/paera-glossary.md`). It reads PAERA itself from the public page
each time.

The videos teach three simplifications. They are correct for a video. This skill holds
the full version:

| Taught | Actually |
| --- | --- |
| A metamodel of six entity types and five relationships (2.2) | Annex 2 in full |
| A five-type body taxonomy (2.4, 2.5, 4.1, 4.8) | Annex A1.2, seven types |
| "Five foundations" (1.5) | Foundations that map to named PAERA sections the tip does not cite |

The August 2026 run of play 1.5 made the section map behind the five foundations:
taxonomy → §4.6, metamodel → Annex 2, building blocks → the GovStack catalogue,
principles → §5.2, and methodology → §5.1, §5.4 and §5.7. The reviewers judged the map
to be teaching content in itself. This skill makes the map each time, and checks it
against the version that is published now.

## Inputs

The skill takes one of these inputs:

- a question about PAERA, in the learner's own words (any course, any page);
- a draft architecture model or a list of entities (2.2);
- the initiative list of the country, from A0 §2 (1.5);
- a principle that the learner wants to adopt, or has drafted (2.3);
- a design, a roadmap or a plan to test against the ten principles or the capability
  ladder.

If the learner pastes something else, say which of these jobs you can do with it. Then do
that job.

## Procedure

1. **Establish the PAERA version that you read.** Read `references/paera-sections.md` for
   the version that this kit records. Then open the entry page in
   `references/paera-index.md`. If the page shows a version, and it is different, use the
   published version and say so. Also record that the kit is behind. If the page shows no
   version, say what the page shows, and give the date that you read it. A change of
   PAERA version is a minor version bump for this kit, and it goes in the CHANGELOG.

   Do not check against a copy. A copy can be stale. The specification is the
   authority. This kit only knows where the specification is.

2. **For a look-up:** find the section in `references/paera-index.md`. The index gives
   the section number and the address of its page. Open that page. Read the section. Then
   answer with four things, in one line or one short block:

   > §5.2, Principle #5 — Once-Only · what the section says · public address · the date
   > you read it

   Quote one sentence at most, in quotation marks. Otherwise write a paraphrase, and say
   that it is a paraphrase. If the question needs two or three sections, read each one.
   Keep PAERA's split between the national level (Chapter 3) and the organisation level
   (Chapter 4). Cite the level that you mean.

   If PAERA does not cover the point, say so. Do not make up a position for it. PAERA
   does not choose technologies, vendors or specific standards.

3. **For a metamodel conformance check (2.2):** take each entity and each relationship in
   the draft of the learner. Compare it against Annex 2 as published. Give each element
   one of three verdicts: **conformant** · **conformant to the teaching subset only** ·
   **not in the metamodel**.

   The second verdict is the important one. An element can agree with the six types in the
   video and have no place in Annex 2. It fails the first review by a person who holds the
   specification. Name the element, and give the Annex 2 element that it must become.

   Also report the opposite case: the Annex 2 elements that the draft has **no** element
   for. A model that has no relationship class at all is a larger finding than an entity
   with the wrong label.

4. **For a five-foundations map (1.5):** make the map from foundation to PAERA section
   **first**. Give each section its address from `references/paera-index.md`. Then assess
   each initiative against each foundation. Write one row for each initiative and each
   foundation, and cite the section. An honest **not applicable** is a correct and useful
   result. To force an initiative into a foundation that it does not touch is worse than
   to say that it does not touch it.

5. **For a principle card (2.3):** read the §5.2 principle on the public page today. Quote
   its title and one sentence of it, **as it is worded**, with the address and the date.
   Then write the card for the country below it. `ea-legal-context` gives the local
   statute that gives the principle its force. The learner adopts the principle. The
   learner does not draft it. This is the purpose of the subtopic. A card that puts the
   principle in other words has lost the reason to adopt one.

   The ten titles of §5.2 are in `references/paera-tests.md`. If the learner names a
   principle that is not one of the ten, say so. Give the nearest §5.2 principle, and do
   not quote §5.2 for a principle that it does not contain.

6. **For a test against the principles or the ladder:** read `references/paera-tests.md`.
   It gives each principle and each level as a test, and what failing looks like. Before
   you write a finding, read the principle's *Implications*, or the level's indicators,
   on the public page. Write each finding as `§ → what is wrong → what PAERA requires
   instead`, with the address. Where PAERA does not settle a question, write it as an open
   question for a named post. Do not invent PAERA's position.

7. **Always state the simplification.** When a check touches one of the three
   simplifications, add this line: *"The video teaches N; the specification has M; your
   element sits here."* The learner must be able to compare this output with the course.

8. **Run `cite-or-discard` on the section citations.** A wrong PAERA section number in a
   deliverable is the failure that the safeguard of play 1.5 names. If you cannot fetch a
   page, keep the section number and the address from the index, mark the line ⚠
   *unverified — learner to confirm*, and do not write PAERA's words from memory.

## Output contract

Write the provenance header first (`references/provenance-header.md`). A look-up that is
not a workbook artefact names itself in the **Artefact** field, for example
`PAERA look-up — once-only`. Then write these sections.

**PAERA version checked** — the version (or what the entry page shows), the URL, and the
date that you read it. Write this as the first line after the header, each time.

**Look-up** — for each section: section number · what it says · public address · date
read. A quotation is one sentence at most and is in quotation marks. A paraphrase says
that it is one.

**Conformance table** (2.2)

```
| Element | Type in draft | Annex 2 element | Verdict | What to change |
```

The verdict is conformant, conformant to the teaching subset only, or not in the metamodel.
After the table, write **Annex 2 elements with no counterpart in the draft**.

**Foundation map** (1.5)

```
| Foundation | PAERA section | Public address | What the section requires |
```

then

```
| Initiative | Foundation | Coverage | Evidence | Gap |
```

The coverage is full, partial, none, or not applicable.

**Principle card** (2.3) — the §5.2 principle's title and one sentence of it, as a
quotation with its address and date, then the card for the country: what the principle
means here, the statute that gives it force, what it forbids, and how to test conformance.

**Findings** (a test against the principles or the ladder)

```
| § | Public address | What is wrong | What PAERA requires instead |
```

**Where the teaching subset was applied** — write this section each time, also when it is
empty. Then write "no simplification applies to this check".

Write text in the chat. Do not make a file. Write no analysis before the header. See
`references/output-contract.md`.

## Safeguard handed back

- **Read the section.** This output cites PAERA sections. Read the two or three sections
  that the argument depends on before you quote them to a person. The section numbers move
  between versions.
- **A quotation here is one sentence.** For the full wording, open the address. Do not
  copy long passages of PAERA into a deliverable. The licence of its text is not
  confirmed (see `references/paera-index.md`).
- **A conformance check is against a specification. It is not against reality.** A model can
  be fully conformant and describe a sector that does not work.
- **The teaching subset is not wrong.** A colleague learned the subset. To tell that
  colleague that their model is not conformant, without this context, is a bad
  conversation. Give the mapping first, then the verdict.
- **The published PAERA version can be later than the reference files of this kit.** Then
  trust the site, and record that the kit is behind.

## Interoperability course plays

The interoperability course cites PAERA at §3.4.3 (interoperability framing), §5.2 Principle #5 (Once-Only),
§3.1.3 (institutional setup) and §3.2 (the legal layer). When an interoperability play names one of
these, check the anchor as published and report where the simplification in the interoperability course departs from
the text, as this skill does for the EA course. The chain is in `references/workbook-chain-gif.md`.

## Other courses

The education DPI roadmap course and the service design course cite PAERA on many pages,
for example §5.4 for the steps to an action plan, and §4.5 for digital co-creation. Those
pages have no artefact of this kit. For them, do the look-up of step 2 and stop. Give no
provenance fields that the page does not have: write `—` in **Consumed** and **Feeds**.

## References

- `references/paera-index.md` — the map of PAERA's sections, with the public address of
  each page, as read on 6 October 2026, and which section answers which question.
- `references/paera-tests.md` — the ten principles of §5.2, the capability ladder of §5.1
  and the roadmap phases of §5.7, written as tests in the kit's own words.
- `references/paera-glossary.md` — the abbreviations of the introduction and the classes of
  Annex 2, in the kit's own words, with where each term is defined.
- `references/paera-sections.md` — the section map behind the five foundations, the PAERA
  version that this kit records, and why the kit references the annex text instead of
  copying it.
- `references/building-blocks.md` — the GovStack building-block catalogue. Inherited.
- `references/state-registries.md` — the state-registry material. Inherited.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` ·
  `references/workbook-chain-gif.md` — the shared contract.
