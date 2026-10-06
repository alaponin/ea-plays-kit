# Interoperability play 2.4 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes when
each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** B11 — Operative article draft · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** gif-decree-draft v<version> · **Consumed** B9, B5 · **Feeds** <play ids from workbook-chain-gif.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The artefact

a draft article with [confirm] placeholders and flagged terms

The prompt of the play says: the draft article, then a list of every [confirm] and every flagged term

## The safeguard, given back as the next action for the learner

If you cannot supply a published model for an article, do not let the AI generate it from scratch — invented legal text reads convincingly and can be harmful.

## What the reference on Estonian law adds — the second run

- The article adapts the duty of § 43⁹(3) and § 43⁹(5) of the Public Information Act as
  read today. The citation names the text that was read: the Estonian text in force, and
  the English translation with its own dates, which can be of an older text.
- Each subsection that the article uses is read in the Estonian text too, because the
  English text is not official.
- Every section number has its superscript: § 43⁹, never "§ 439".
- The bodies that must connect come from B5's first wave, not from the model. The coverage
  table after the article maps each catalogue exchange to its clause.

## Contract checks, for each play

- Text in the chat only: no file, no chart, no image, no screenshot.
- Posts, not names. The output names no real office-holder.
- The output has no analysis by the model before the provenance header.
- Each claim about the outside world carries its URL, its tier and its access date in the
  same line.
- Every identifier, code value and legal citation the country's own registries or statutes
  must confirm is marked `[confirm]`; the skill invents none.
- The ⚠ count on line 3 of the header is equal to the number of ⚠ marks in the body.
