---
name: paera-reference-check
description: >-
  Check a draft model, an initiative list or a principle against the PAERA specification
  itself, and not against the simplification that the videos teach. Use the full Annex 2
  metamodel, the full Annex A1.2 taxonomy, the §5.2 principles as they are worded, and the
  section map behind the five foundations. Serves the metamodel conformance check (2.2), the
  five-foundations map (1.5) and the principle card (2.3). Use when someone says "check this
  against PAERA", "is this metamodel conformant", "map our initiatives to the five
  foundations", "which PAERA section covers this", "what does PAERA actually say about
  principles", "adopt a PAERA principle for my country", "is this entity type in the
  metamodel", "PAERA compliance check". Returns a conformance table against the full
  specification, the foundation-to-PAERA-section map, and a clear note wherever the
  learner's element is in the teaching subset but not in the full metamodel — the
  simplification is right for a four-minute video and wrong for a deliverable. Reads
  paera.govstack.global again when the published version differs from the one this kit
  records.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
---

## What this skill does

This skill checks work against **PAERA as published**. It also says when the video applied
a simplification.

The videos teach three simplifications. They are correct for a video. This skill holds the
full version:

| Taught | Actually |
| --- | --- |
| A metamodel of six entity types and five relationships (2.2) | Annex 2 in full |
| A five-type body taxonomy (2.4, 2.5, 4.1, 4.8) | Annex A1.2, seven types |
| "Five foundations" (1.5) | Foundations that map to named PAERA sections the tip does not cite |

The August 2026 run of play 1.5 made that section map: taxonomy → §4.6, metamodel → Annex
2, building blocks → the GovStack catalogue, principles → §5.2, and methodology → §5.1,
§5.4 and §5.7. The reviewers judged the map to be teaching content in itself. This skill
makes the map each time, and checks it against the version that is published now.

## Inputs

The skill takes one of these three inputs:

- a draft architecture model or a list of entities (2.2);
- the initiative list of the country, from A0 §2 (1.5);
- a principle that the learner wants to adopt, or has drafted (2.3).

If the learner pastes something else, say which of the three checks you can run on it. Then
run that check.

## Procedure

1. **Establish the PAERA version that you check against.** Read
   `references/paera-sections.md` for the version that this kit records. Then read
   **paera.govstack.global** and confirm the version. If the published version is
   different, use the published version. Say so in the output. Also record that the
   reference file of the kit is behind. A change of PAERA version is a minor version bump
   for this kit, and it goes in the CHANGELOG.

   Do not check against an embedded copy, because an embedded copy can be stale. The
   specification is the authority. This kit only knows where the specification is.

2. **For a metamodel conformance check (2.2):** take each entity and each relationship in
   the draft of the learner. Compare it against Annex 2 in full. Give each element one of
   three verdicts: **conformant** · **conformant to the teaching subset only** · **not in
   the metamodel**.

   The second verdict is the important one. An element can agree with the six types in the
   video and have no place in Annex 2. It fails the first review by a person who holds the
   specification. Name the element, and give the Annex 2 element that it must become.

   Also report the opposite case: the Annex 2 elements that the draft has **no** element
   for. A model that has no relationship class at all is a larger finding than an entity
   with the wrong label.

3. **For a five-foundations map (1.5):** make the map from foundation to PAERA section
   **first**. Then assess each initiative against each foundation. Write one row for each
   initiative and each foundation, and cite the section. An honest **not applicable** is a
   correct and useful result. To force an initiative into a foundation that it does not
   touch is worse than to say that it does not touch it.

4. **For a principle card (2.3):** quote the PAERA §5.2 principle **as it is worded**. Then
   write the card for the country below it. `ea-legal-context` gives the local statute that
   gives the principle its force. The learner adopts the principle. The learner does not
   draft it. This is the purpose of the subtopic. A card that puts the principle in other
   words has lost the reason to adopt one.

5. **Always state the simplification.** When a check touches one of the three
   simplifications, add this line: *"The video teaches N; the specification has M; your
   element sits here."* The learner must be able to compare this output with the course.

6. **Run `cite-or-discard` on the section citations.** A wrong PAERA section number in a
   deliverable is the failure that the safeguard of play 1.5 names.

## Output contract

Write the provenance header first (`references/provenance-header.md`). Then write these
sections.

**PAERA version checked** — the version, the URL, and the date that you read it. Write this
as the first line after the header, each time.

**Conformance table** (2.2)

```
| Element | Type in draft | Annex 2 element | Verdict | What to change |
```

The verdict is conformant, conformant to the teaching subset only, or not in the metamodel.
After the table, write **Annex 2 elements with no counterpart in the draft**.

**Foundation map** (1.5)

```
| Foundation | PAERA section | What the section requires |
```

then

```
| Initiative | Foundation | Coverage | Evidence | Gap |
```

The coverage is full, partial, none, or not applicable.

**Principle card** (2.3) — the §5.2 principle as a quotation, then the card for the
country: what the principle means here, the statute that gives it force, what it forbids,
and how to test conformance.

**Where the teaching subset was applied** — write this section each time, also when it is
empty. Then write "no simplification applies to this check".

Write text in the chat. Do not make a file. Write no analysis before the header. See
`references/output-contract.md`.

## Safeguard handed back

- **Read the section.** This output cites PAERA sections. Read the two or three sections
  that the argument depends on before you quote them to a person. The section numbers move
  between versions.
- **A conformance check is against a specification. It is not against reality.** A model can
  be fully conformant and describe a sector that does not work.
- **The teaching subset is not wrong.** A colleague learned the subset. To tell that
  colleague that their model is not conformant, without this context, is a bad
  conversation. Give the mapping first, then the verdict.
- **The published PAERA version can be later than the reference file of this kit.** Then
  trust the site, and record that the kit is behind.

## References

- `references/paera-sections.md` — the section map behind the five foundations, the PAERA
  version that this kit records, and why the kit references the annex text instead of
  copying it.
- `references/building-blocks.md` — the GovStack building-block catalogue. Inherited.
- `references/state-registries.md` — the state-registry material. Inherited.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` — the shared contract.
