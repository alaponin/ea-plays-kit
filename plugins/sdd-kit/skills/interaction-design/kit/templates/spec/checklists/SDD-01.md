---
standard: SDD-01
title: Specification-Driven Development
edition: "3.5"
document: SDD-01_Specification_Driven_Development_v3.5.md
sha256: b14cf9b6ba88c725a664e25a5ff080bd21c0b8554abe2e49d27d2bb230391a5b
produced_by: _working/2026-08-31_consistency_pass/docx_build/build.js at 2026-09-29T20:23:05Z
converted_from: SDD-01_Specification_Driven_Development_v3.5.docx sha256 31a5b5135b9d2f0126a622fd7e8cb812a75f8d0fe1b886c5af10374fd4cef136 (sdd-kit carries its text as Markdown)
---

# SDD-01 · Specification-Driven Development — the checklist

*Produced from the document named above by `_working/2026-09-28_the_checklists/extract_checklist.py`, as the last step of its build, and never edited by hand. Every line below is the document's own words, read from it, except the lines in italics, which are this program's.*

*Rules counted in the document: 19. The document states "It carries nineteen standing rules in section 14" (19).*

## Gate — the program's half

### 11 The review — What they are given beforehand

Everything a program can establish is established before anybody arrives, and it is read rather than discussed: that every step and every variation is reached or reasoned about in writing, that every value says where it came from, that every rule cited resolves in the register, that every reference resolves, and that the walk-through was made from the version of the record now in force. A meeting that spends its time on what a program already knows has spent it badly, and a reviewer who reopens a line a program has already settled is asking the wrong question of the wrong document.

## Gate — the person's half

### 11 The review — the words before its first subsection

A step with people in it, not a property a document either has or has not.

Until this version this method treated review as something a document was good enough to survive. That is no longer tenable, and it was never quite right. A goal now has a use case, a set of screens and a walk-through, and no single document is the thing being reviewed.

So review is a step of the work. It is run before a set of screens is agreed and before anything is built from it, and it has the same four parts every time.

### 11 The review — Who is in the room

Three people, and none of them is optional. Whoever owns the set of screens. Whoever will build from it. And the counterpart whose work the screens describe — the person from the business side who will have to live with what is agreed. Two of the three can hold a useful conversation and cannot hold this one: the builder and the owner agreeing with each other is how a specification comes to describe something nobody wanted.

### 11 The review — What only a person can settle

Whether the screens follow the story, or the story was fitted to the screens afterwards. Whether a value that first enters the organisation at this screen could have come from somewhere the organisation already holds, or whether its justification merely restates what the value is for. Whether a reason given for needing no screen is true, or is the reason somebody reached for. Whether the words are the words the business uses, in the sense the business uses them. Whether anybody who did not write it actually opened the walk-through and followed it, from the first screen to each of its endings. And whether the interests the goal exists to protect are visible to the person who has to protect them.

### 11 The review — What is recorded afterwards

Every line that was not satisfied, with a name against it, a date, and what would close it. A finding that has an owner does not defeat the work. A failure that nobody wrote down does. Nothing is set aside to let the meeting end, and that is the same rule as everywhere else in this document; it is stated again here because this is the moment it is hardest to keep.

> What passing this review establishes, and what it does not
>
> Everything a program checked establishes that something is named, recorded, resolved or reached. None of it establishes that what is recorded is true. A set of screens that has passed the mechanical half has been shown to be well formed, and nothing more.

### 12 When a specification is good enough

Three tests and one rule about honesty. All four have to hold.

- The developer test. Somebody can build this without working anything out and without asking anybody anything.
- The review test. The review of the previous section has been held, with the three people in the room, and every line that was not satisfied left it with a name and a date against it.
- The refusal test. Every gap that remains is written down, has somebody's name against it, and is counted.

And the rule about honesty, which is the one that fails first when a deadline is close: an unanswered question that is named, owned and counted is part of a specification. An unanswered question that has been filled in with a plausible answer is a fault, and it is a worse fault than the blank would have been, because the blank was visible.

## Form

*The document governs no written thing of its own and fixes no form.*

## Rules

| rule | words | program |
|---|---|---|
| §14 rule 1 | What software generated is never edited by hand. | none |
| §14 rule 2 | A correction lands in the document that owns | none |
| §14 rule 3 | The screens of a goal are worked out | none |
| §14 rule 4 | When behaviour changes, the story changes first, then | none |
| §14 rule 5 | A gap is a finding with an owner, | none |
| §14 rule 6 | Every figure that comes from policy is a | none |
| §14 rule 7 | Never invent a figure in order to keep | none |
| §14 rule 8 | A decision that has been taken is cited, | none |
| §14 rule 9 | Where two signed documents contradict each other, that | none |
| §14 rule 10 | Gaps stay open and counted. They are never | none |
| §14 rule 11 | A refusal is answered, not worked around. | none |
| §14 rule 12 | A description with errors outstanding is not finished. | none |
| §14 rule 13 | A check is never altered to make its | none |
| §14 rule 14 | Where the work stands is read from the | none |
| §14 rule 15 | An empty column is information. It is usually | none |
| §14 rule 16 | Not applicable, with a stated reason, is a | none |
| §14 rule 17 | A goal that claims an authority names where | none |
| §14 rule 18 | A claim that something follows a standard is | none |
| §14 rule 19 | The application model is written only from an | none |
