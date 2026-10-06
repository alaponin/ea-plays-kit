# Service design course 3.6 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes
when each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** Decision page — the review of the licence screens · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** decision-cards v<version> · **Consumed** — · **Feeds** —
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The cards

- **Decisions**: line 2, the name after a cancelled licence; and whether the Registrar
  accepts the screens now, with owned lines open, or when every line is closed.
- **Quick answers**: line 5, the printed confirmation, with *establish the fact first* —
  read the register of requirements — as the recommended option.
- **Not yours to rule**, in grey: lines 1 and 3, which the supplier's analyst changes, and
  line 4, which the head of the ICT unit of PHEQA decides after PNIA gives its service
  hours. Each says who closes it, and by when.
- Each card names the post that rules: the Registrar of PHEQA, or the owner of the line.
- The words of a card say *the second screen*, *the identity service*; `S2`, `S3`, `S5`
  and the line numbers appear only in `Touches`.
- The card on accepting the screens says that it is ruled after the card on the printed
  confirmation.

## The page

The name of one HTML file, built from the skill's template, and one line on how to answer.
If no file can be made, the numbered list alone, with the options as a., b., c.

## The safeguard, given back as the next action for the learner

The Registrar rules; the page only records her answers. Each answer goes into the document
that owns the fact: the shared groundwork for line 2, the architecture for line 4, the
register of requirements for line 5. An owner is named only where the record names one.

## Contract checks, for each run

- The record is text in the chat: the numbered list. The one file is the decision page;
  there is no other file, no chart, no image, no screenshot.
- Posts, not names. The output names no real office-holder, and fills in no name on the
  page.
- The output has no analysis by the model before the provenance header.
- No identifier, code or section number appears in the words of a card; each one is in
  its `Touches` line.
- No option is pre-selected. No figure is invented.
- The ⚠ count on line 3 of the header is equal to the number of ⚠ marks in the body.
