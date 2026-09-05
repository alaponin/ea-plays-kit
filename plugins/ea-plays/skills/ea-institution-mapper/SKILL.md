---
name: ea-institution-mapper
description: >-
  Find the public bodies that matter in a country and a sector. For each body, record its
  legal mandate with the instrument that grants it, the systems and registries that it
  operates, the post that heads it, and its PAERA Annex A1.2 classification with a
  confidence and a hybrid flag. Serves every play that begins "here are the main bodies in
  [sector]": the ministerial explainer (1.2), the phase RACI's roles input (1.6), classify a
  body (2.4), the sector BDAT skeleton (2.5), the demonstration canvas (4.1), the transfer
  plan (4.8) and the second-sector map (5.3). Use when someone says "who are the bodies in
  [country]'s [sector]", "classify this agency", "what is this ministry's legal mandate",
  "which body owns the learner registry", "build my roles register", "is this a registry or
  a service authority", "fill in the demonstration canvas". Returns the A5 bodies register,
  a roles register tagged confirmed/partial/gap, and the 4.1 canvas pre-filled. Reads
  official portals, establishing acts, national strategies, donor project documents, ID4D and
  CRVS assessments. Posts, never names.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
---

## What this skill does

The plays ask the learner to paste "the main bodies in the sector". This skill finds them
in the public record. For each body it gives the **legal mandate and the instrument that
grants it**, the systems and registries that the body operates, the post that heads the
body, and the position of the body in the PAERA taxonomy.

Play 2.4 ends with this safeguard: *confirm the classification against the body's actual
legal mandate*. This skill does that step. It is not homework for the learner.

## Inputs

The skill needs the country and the sector.

If the learner has A0 §6, read it and add to it. Do not start again. Section §6 is a first
pass with the tags confirmed and inferred. This skill adds the legal instrument, the
classification and the post that heads each body.

If the learner has neither input, build the list of bodies first. Use the site of the
sector ministry and the sector plan. Then continue.

## Procedure

1. **Find the bodies.** Look for the sector ministry or ministries; the bodies for
   examinations, licensing or regulation; the registries; and the providers of the shared
   platforms that the sector uses, which are identity, civil registration, payments and
   data exchange. Sources: official portals (T1); the national strategy and the sector plan
   (T1); donor project documents, because PADs and ICRs describe institutional arrangements
   in unusual detail (T2); ID4D and CRVS country assessments (T1/T2); Giga for education
   infrastructure (T1).

2. **Find the establishing instrument of each body.** This is the act, decree or statutory
   instrument that creates the body. Quote the one clause that gives its mandate. A mandate
   in your own words from an "about" page is *inferred*. A mandate quoted from an act is
   *confirmed*. Record which one it is.

   A body can exist in practice when you cannot find an instrument. Then say so. A unit
   that coordinates and has no legal basis is a finding. It is more important than a
   classification, because this pattern stops national EA programmes.

3. **Record the systems and the registries.** Record what the body operates and what it
   holds. Use strategy documents, donor project documents and the service catalogue of the
   body. For status, and not for existence, use `bb-landscape-check`. Show the difference
   between a system that the body **operates** and a system that the body **uses**.

4. **Classify each body against PAERA Annex A1.2.** Use the **full taxonomy of seven
   types**. Do not use the subset of five types from the videos. See
   `references/paera-a1-2.md`. Read Annex A1.2 again at paera.govstack.global when the
   country work needs the exact published words.

   Give four items with each classification:
   - the **type**;
   - the **nearest teaching type**, in brackets, from the five types in the videos, so that
     the learner can compare the output with the course;
   - a **confidence**, which is confirmed from the instrument, or inferred from behaviour;
   - a **hybrid flag**, when a body truly does two jobs. Hybrid bodies are common. They
     are not a failure of the taxonomy. A ministry that makes policy and also operates a
     national system is a Policy Unit **and** a Service-Delivery Authority. To say so is
     the finding. Never put a hybrid body into one box to make the table look better.

5. **Build the roles register.** Record each role by post. Give the status tag from the
   August 2026 runs, which is confirmed, partial or gap. Give the phase that each gap
   blocks. This register is the input to play 1.6.

6. **Fill in the 4.1 demonstration canvas** when the learner needs a canvas. Give the
   bodies, the systems, the registrations that occur two times or more, the points where
   staff put data on paper again, and the flagship programme that stopped.

7. **Run `cite-or-discard` before you give the output to the learner.** A wrong legal
   mandate does the most damage. A RACI built on a mandate that does not exist puts the
   learner in front of a Board to defend a fiction.

## Output contract

Write the provenance header first (`references/provenance-header.md`). Then write what the
learner asked for.

**A5 bodies register**

```
| Body | Mandate (quoted) | Instrument | Systems operated | Registries held | PAERA type [teaching type] | Confidence | Hybrid | Head post | Source |
```

**Roles register**

```
| Post | Institution | Mandate (one line) | Status | Blocks from phase | Source |
```

The status is confirmed, partial or gap. After the table, write **Roles an EA programme
needs that are missing**, with one line for each role.

**4.1 canvas**, when the learner asks for it — the bodies, the symptoms of fragmentation
that you observed, the flagship programme that stopped, and the baseline figures. Write it
as text with headings.

End each output with **Not found where one would be expected**. List the bodies and
functions whose absence is a finding.

Write text in the chat. Do not make a file, an image of a diagram, or a picture of an
organisation chart. **Posts, never names.** Sources give you the name of the person in the
post. Remove the name when you write the line. Write no analysis before the header. See
`references/output-contract.md`.

## Safeguard handed back

A classification is a hypothesis about the mandate of a body. Mandates are disputed inside
a government more frequently than outside it.

- **Confirm each mandate against the instrument.** Then confirm with a person inside the
  body that the instrument is the current one. A search rarely finds the amendments.
- **Check each hybrid body with the bodies concerned.** To tell a ministry that it is a
  registry, or to tell an agency that it moved into delivery with no mandate, is a
  political act. Have the clause ready.
- **A gap row in the roles register is a claim about an absence.** This is the most
  difficult claim to prove from public sources. Confirm each *gap* row inside the
  government before it becomes the membership section of a Board ToR.
- Each item marked ⚠ or *inferred* is not yet a fact.

## References

- `references/mandate-sources.md` — where each type of establishing instrument is
  published, and how to see the difference between an amended act and an act that is
  superseded.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` — the shared contract.

### Fixture material

- `references/paera-a1-2.md` — the taxonomy of seven types, the teaching subset of five
  types, how they map to each other, and when to read the published annex again. Its
  worked classification uses a fixture body.

  Progressa is the fictional demonstration country that each play shares. The canonical
  description is `tests/progressa.md` in the kit repo.
