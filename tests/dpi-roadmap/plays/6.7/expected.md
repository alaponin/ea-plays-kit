# Education DPI roadmap course 6.7 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes
when each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** Decision page — the response matrix · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** decision-cards v<version> · **Consumed** — · **Feeds** —
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The cards

- **One card for each comment** — five cards. No two comments share a card.
- The proposed decision of each row is the **recommendation in the note**. It is not
  pre-selected.
- The options are *accepted*, *accepted in part* and *not accepted*. Each says what
  follows: for the comment on the interoperability score, *accepted* lowers the score and
  the domain score, and the change is recorded beside the maturity table.
- The words of each card say what the row is about in plain words — *the interoperability
  score of the assessment*, *the high estimate of the learner-register line*. `CM-02`,
  `F-INT-1`, `I2`, `V-02`, `C-14` and `INV-06` appear only in `Touches`.
- Commenters are named by role. No card names a person.

## Not yours to rule

The three figures to verify are shown in grey as *establish the fact first*: each figure is
checked at its source before the card that depends on it is ruled. The cards on the
interoperability score and on the high estimate say that they wait for that check.

## The page

The name of one HTML file, built from the skill's template, and one line on how to answer.
If no file can be made, the numbered list alone, with the options as a., b., c.

## The safeguard, given back as the next action for the learner

Every figure that changes is verified at its source before it is accepted, and a person
approves the answer to each comment. The page only records. Each answer goes into the
response matrix, and the change into the section that it revises.

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
