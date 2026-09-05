---
name: ea-institution-mapper
description: >-
  Find the public bodies that matter in a country and sector, and record for each one its
  legal mandate with the instrument that grants it, the systems and registries it is known
  to operate, the post that heads it, and its PAERA Annex A1.2 classification with a
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
---

## What this skill does

Turns "the main bodies in the sector" from something the learner is asked to paste into
something sourced: each body's **legal mandate with the instrument that grants it**, the
systems and registries it runs, the post that heads it, and where it sits in the PAERA
taxonomy.

The safeguard in 2.4 — *confirm the classification against the body's actual legal
mandate* — becomes this skill's own step rather than the learner's homework.

## Inputs

Country and sector. If the learner has A0 §6, read it and deepen it rather than starting
again; §6 is a first pass with confirmed/inferred, and this skill adds the legal instrument,
the classification and the head post.

If neither is available, build the body list first from the sector ministry's own site and
the sector plan, then proceed.

## Procedure

1. **Find the bodies.** The sector ministry or ministries; examinations, licensing or
   regulatory bodies; the registries; and the shared-platform providers the sector depends
   on (identity, civil registration, payments, data exchange). Sources: official portals
   (T1), the national strategy and sector plan (T1), donor project documents — PADs and
   ICRs describe institutional arrangements in unusual detail (T2), ID4D and CRVS country
   assessments (T1/T2), Giga for education infrastructure (T1).

2. **Find the establishing instrument** for each body — the act, decree or statutory
   instrument that creates it — and quote the one clause that states its mandate. A mandate
   paraphrased from an "about" page is *inferred*; a mandate quoted from an act is
   *confirmed*. Record which.

   Where a body exists in practice but you cannot find an instrument, say so. A unit with
   a coordinating role and no legal basis is a finding that matters more than a
   classification: it is exactly the pattern that stalls national EA programmes.

3. **Record systems and registries.** What it runs, what it holds. From strategy documents,
   donor project documents, the body's own service catalogue, and — for status rather than
   existence — `bb-landscape-check`. Distinguish a system the body **operates** from one it
   **consumes**.

4. **Classify against PAERA Annex A1.2**, using the **full seven-type taxonomy**, not the
   five-type teaching subset. See `references/paera-a1-2.md`, and re-read Annex A1.2 at
   paera.govstack.global when the country work justifies the authoritative wording.

   Each classification carries:
   - the **type**;
   - in brackets, the **nearest teaching type** from the five used in the videos, so the
     learner can reconcile the output with the course;
   - a **confidence** — confirmed (from the instrument) / inferred (from behaviour);
   - a **hybrid flag** where a body genuinely does two jobs. Hybrids are common and are not
     a failure of the taxonomy: a ministry that both sets policy and runs a national system
     is a Policy Unit **and** a Service-Delivery Authority, and saying so is the finding.
     Never force a hybrid into one box to make the table tidy.

5. **Build the roles register** — by post, with the confirmed / partial / gap status tag
   the August 2026 runs produced, and the phase each gap blocks. This is the input to 1.6.

6. **Pre-fill the 4.1 demonstration canvas** when a canvas is what the learner needs: the
   bodies, the systems, the duplicate registrations, the paper re-entry points, and the
   stalled flagship.

7. **Run `cite-or-discard`** before returning. Legal mandates are the claims most damaging
   to get wrong — a RACI built on a mandate that does not exist puts the learner in front
   of a Board defending a fiction.

## Output contract

Provenance header first (`references/provenance-header.md`), then, as the learner asked:

**A5 bodies register**

```
| Body | Mandate (quoted) | Instrument | Systems operated | Registries held | PAERA type [teaching type] | Confidence | Hybrid | Head post | Source |
```

**Roles register**

```
| Post | Institution | Mandate (one line) | Status | Blocks from phase | Source |
```

Status is confirmed / partial / gap. Follow it with **Roles an EA programme needs that are
missing**, one line each.

**4.1 canvas** (when asked) — bodies, the fragmentation symptoms observed, the stalled
flagship, and the baseline figures, as headed text.

Close every output with **Not found where one would be expected** — the bodies and
functions whose absence is a finding.

Text in the chat. No file, no diagram image, no org chart picture. **Posts, never names** —
sources will hand you the current holder; drop the name at the point of writing. No
reasoning before the header. See `references/output-contract.md`.

## Safeguard handed back

A classification is a hypothesis about a body's mandate, and mandates are contested inside
governments more often than outside them.

- **Confirm each mandate against the instrument itself**, and confirm with someone inside
  the body that the instrument is the current one — amendments rarely surface in search.
- **Check the hybrids with the bodies concerned.** Telling a ministry it is a registry, or
  an agency that it has drifted into delivery without a mandate, is a political act. Have
  the clause ready.
- **A gap in the roles register is a claim about an absence** — the hardest thing to
  evidence from public sources. Confirm every *gap* row internally before it becomes the
  membership section of a Board ToR.
- Anything marked ⚠ or *inferred* is not yet a fact.

## References

- `references/paera-a1-2.md` — the seven-type taxonomy, the five-type teaching subset, how
  they map, and when to re-read the published annex.
- `references/mandate-sources.md` — where establishing instruments are published, by
  document type, and how to tell an amended act from a superseded one.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` — the shared contract.
