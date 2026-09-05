---
name: paera-reference-check
description: >-
  Check a draft model, an initiative list or a principle against the PAERA specification
  itself rather than against the teaching simplification used on video — the full Annex 2
  metamodel, the full Annex A1.2 taxonomy, the §5.2 principles as worded, and the section
  map behind the five foundations. Serves the metamodel conformance check (2.2), the
  five-foundations map (1.5) and the principle card (2.3). Use when someone says "check this
  against PAERA", "is this metamodel conformant", "map our initiatives to the five
  foundations", "which PAERA section covers this", "what does PAERA actually say about
  principles", "adopt a PAERA principle for my country", "is this entity type in the
  metamodel", "PAERA compliance check". Returns a conformance table against the full
  specification, the foundation-to-PAERA-section map, and an explicit note wherever the
  learner's element maps to the teaching subset but not the full metamodel — the
  simplification is right for a four-minute video and wrong for a deliverable. Re-reads
  paera.govstack.global when the published version differs from the one this kit records.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
---

## What this skill does

Checks work against **PAERA as published**, and says explicitly when the video's
simplification has been applied.

Three simplifications are taught on video and are correct for their purpose. This skill
holds the full version:

| Taught | Actually |
| --- | --- |
| A metamodel of six entity types and five relationships (2.2) | Annex 2 in full |
| A five-type body taxonomy (2.4, 2.5, 4.1, 4.8) | Annex A1.2, seven types |
| "Five foundations" (1.5) | Foundations that map to named PAERA sections the tip does not cite |

The August 2026 run of 1.5 produced that section map — taxonomy → §4.6, metamodel →
Annex 2, building blocks → the GovStack catalogue, principles → §5.2, methodology →
§5.1/5.4/5.7 — and it was judged teaching content in its own right. This skill produces it
every time, and checks it against the current published version.

## Inputs

One of: a draft architecture model or entity list (2.2); the country's initiative list, from
A0 §2 (1.5); a principle the learner wants to adopt or has drafted (2.3).

If the learner pastes something that is none of these, say which of the three checks you can
run on it and run that one.

## Procedure

1. **Establish which PAERA version you are checking against.** Read
   `references/paera-sections.md` for the version this kit records. Then fetch
   **paera.govstack.global** and confirm. If the published version differs, use the
   published one, say so in the output, and note that the kit's reference file is behind —
   a PAERA version change is a minor version bump for this kit and belongs in the CHANGELOG.

   Do not check against an embedded copy that may be stale. The specification is the
   authority; this kit only knows where it is.

2. **For a metamodel conformance check (2.2):** take each entity and relationship in the
   learner's draft and resolve it against Annex 2 in full. Three verdicts per element:
   **conformant** · **conformant to the teaching subset only** · **not in the metamodel**.

   The middle verdict is the one that matters. An element that is fine against the six types
   taught on video but has no place in Annex 2 will fail the first review by anyone holding
   the specification. Name it, and give the Annex 2 element it should become.

   Also report the reverse: Annex 2 elements the draft has **no** counterpart for. A model
   missing a whole relationship class is a bigger finding than a mislabelled entity.

3. **For a five-foundations map (1.5):** produce the foundation → PAERA section map **first**,
   then assess each initiative against each foundation. One row per initiative per
   foundation, with the section cited. An honest **not applicable** is a valid and useful
   result — force-fitting an initiative to a foundation it does not touch is worse than
   saying it does not touch it.

4. **For a principle card (2.3):** quote the PAERA §5.2 principle **as worded**, then produce
   the country-tailored card beneath it, with the local statute that gives it force supplied
   by `ea-legal-context`. The principle is adopted, not drafted — that is the whole point of
   the subtopic. A card that paraphrases the principle has lost the reason for adopting one.

5. **Always state the simplification.** Wherever a check touches one of the three
   simplifications, add a line: *"The video teaches N; the specification has M; your element
   sits here."* The learner has to be able to reconcile this output with the course.

6. **Run `cite-or-discard`** on the section citations. A wrong PAERA section number in a
   deliverable is the failure mode the 1.5 safeguard names.

## Output contract

Provenance header first (`references/provenance-header.md`), then:

**PAERA version checked** — the version, the URL, and the date fetched. First line after the
header, always.

**Conformance table** (2.2)

```
| Element | Type in draft | Annex 2 element | Verdict | What to change |
```

Verdict: conformant / conformant to the teaching subset only / not in the metamodel.
Follow with **Annex 2 elements with no counterpart in the draft**.

**Foundation map** (1.5)

```
| Foundation | PAERA section | What the section requires |
```

then

```
| Initiative | Foundation | Coverage | Evidence | Gap |
```

Coverage: full / partial / none / not applicable.

**Principle card** (2.3) — the §5.2 principle quoted, then the country card: what it means
here, the statute that gives it force, what it forbids, how conformance is tested.

**Where the teaching subset was applied** — always present, even when empty ("no
simplification applies to this check").

Text in the chat. No file. No reasoning before the header. See
`references/output-contract.md`.

## Safeguard handed back

- **Open the section.** This output cites PAERA sections; read the two or three the argument
  rests on before quoting them to anyone. Section numbering moves between versions.
- **A conformance check is against a specification, not against reality.** A model can be
  perfectly conformant and describe a sector that does not work.
- **The teaching subset is not wrong**, and telling a colleague their model is
  non-conformant when they were taught the subset is a bad conversation to have without
  this context. Lead with the mapping, not the verdict.
- **Where the published PAERA version has moved past this kit's reference file**, trust the
  site and flag the kit.

## References

- `references/paera-sections.md` — the section map behind the five foundations, the PAERA
  version this kit records, and why the annex text is referenced rather than embedded.
- `references/building-blocks.md` — the GovStack building-block catalogue as carried by
  `paera-assessor`. Inherited.
- `references/state-registries.md` — the state-registry material. Inherited.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` — the shared contract.
