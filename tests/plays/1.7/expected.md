# Play 1.7 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes when
each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** A7 — EA Governance Board ToR · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** ea-governance-drafter v<version> · **Consumed** A0 §4, A0 §7, A3, A6 · **Feeds** <play ids from workbook-chain.md>
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The artefact

a structured ToR document

The prompt of the play says: structured Terms of Reference ready to circulate for cabinet approval

## The safeguard, given back as the next action for the learner

Have the country's legal counsel review the document before it is formally adopted — particularly the 'binding decision scope' section, which interacts with existing sectoral legislation.

## The minister's page — `decision-cards`

A second output, after A7. Its provenance header names `Decision page — the four asks` in
**Artefact**, `decision-cards v<version>` in **Skill**, `A7` in **Consumed** and `—` in
**Feeds**. All nine fields are present.

- **Inputs supplied by the learner**: who rules (the Minister of ICT, by post), and by
  when.
- **The cards, as a numbered list in the chat**: one card for each ask — the team, the
  Board's binding authority, the budget envelope, the promise. Each card has its
  background, a question in one sentence, two to four options that each say what follows,
  a note, the post that rules, and a `Touches` line.
- **No figure is invented.** The budget card may offer *about two per cent of the
  digital-government budget, for five years*, because the play page states it. Any other
  figure is *a share that you set — type it in the note*.
- **Not yours to rule**: whether a board under one minister can bind other ministries is a
  question for legal counsel, as the safeguard of the play says. It is shown in grey, with
  who closes it.
- **The page**: the name of one HTML file, built from the skill's template, and one line
  on how to answer. If no file can be made, the numbered list alone, with the options as
  a., b., c.
- **The safeguard**: the minister rules; the page only records; each answer goes into the
  ToR.
- No option is pre-selected. No card names a person.

## Contract checks, for each play

- Text in the chat only: no file, no chart, no image, no screenshot. The one
  exception is the decision page of `decision-cards`: one HTML file, with the
  same cards as a numbered list in the chat.
- Posts, not names. The output names no real office-holder.
- The output has no analysis by the model before the provenance header.
- Each claim about the outside world carries its URL, its tier and its access date in the
  same line.
- The ⚠ count on line 3 of the header is equal to the number of ⚠ marks in the body.
