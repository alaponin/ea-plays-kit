# Service design course 4.5 — expected output shape

This file gives the **shape** of the output. It does not give the wording. A run passes
when each line below is present. The words are different in each run.

## Provenance header — the first three lines of the output

```
> **Artefact** Decision page — the review of the application model · **Country** Progressa · **Sector** Education · **Built** <ISO date>
> **Skill** decision-cards v<version> · **Consumed** — · **Feeds** —
> **Sources** <n> × Tier 1, <n> × Tier 2, <n> × Tier 3 · **Unverified lines** <n>
```

All nine fields must be present. Write `—` in a field with no value. Never leave it blank.

## The cards

- **One card for each line** — two cards. The assumption and the loss are not merged.
- Each card quotes the line's own words in quotation marks, unchanged.
- Each card has two options, *yes* and *no*. *Yes* says, in one plain sentence, what the
  running service will do. *No* says what must happen instead, and names the document that
  is corrected: the goal's story. The file is then written again, and the cards read again.
- Each card names the post that rules: the Director of Higher Education.
- Nothing on the cards answers the question. No option is pre-selected.

## The page

The name of one HTML file, built from the skill's template, with the *Ruled by* and *Date*
fields left empty for the Director to fill in, and one line on how to answer. If no file
can be made, the numbered list alone, with the options as a. and b.

## The safeguard, given back as the next action for the learner

A question must keep the loss's own words; a question in other words can draw a "yes" that
was not meant. Record each answer with the post that ruled and the date before the model
is approved. A "no" goes back to the goal's story, never into the file.

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
