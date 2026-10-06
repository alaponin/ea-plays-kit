# Play 1.5 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes when
each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** A5 — PAERA foundation coverage map · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** paera-reference-check v<version> · **Consumed** A0 §2, the initiatives list, A1 · **Feeds** <play ids from workbook-chain.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The artefact

a per-initiative coverage table plus a coverage summary

The prompt of the play says: per-initiative table plus 3-bullet summary

## The safeguard, given back as the next action for the learner

An initiative that says 'we have principles' may not have PAERA-aligned principles — confirm coverage by reading the actual document, not the marketing summary.

## What the PAERA look-up adds

- **PAERA version checked** is the first line after the header: what the entry page
  shows (a version, or the words *no version shown*), the address
  `https://paera.govstack.global/` and the date read.
- **The foundation map comes first.** It has one row for each of the five foundations, and
  each row gives the section **and the public address of its page**: taxonomy → §4.6 and
  A1.2; metamodel → Annex 2; building blocks → the GovStack catalogue; principles → §5.2;
  methodology → §5.1, §5.4 and §5.7.
- **The look-up answer** gives the section (§4.6, with A1.2 for the full taxonomy), what
  it says, the address of its page and the date read. A quotation is one sentence at most,
  in quotation marks. A paraphrase says that it is one.
- **No PAERA text from memory.** A page that could not be fetched keeps its section and
  its address, carries ⚠, and gives no words of PAERA.
- No passage of PAERA longer than one sentence appears in the output.

## Contract checks, for each play

- Text in the chat only: no file, no chart, no image, no screenshot.
- Posts, not names. The output names no real office-holder.
- The output has no analysis by the model before the provenance header.
- Each claim about the outside world carries its URL, its tier and its access date in the
  same line.
- The ⚠ count on line 3 of the header is equal to the number of ⚠ marks in the body.
