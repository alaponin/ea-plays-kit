---
standard: SDD-11
title: The Interaction Design
edition: "0.1"
document: SDD-11_The_Interaction_Design_v0.1.md
sha256: 24ad9b91baaa5f5aa134a1b457107a4339ee12a2b312d0b6ccabf82e62bb7cd2
produced_by: _working/2026-08-31_house_rebuild/build_house.js at 2026-09-25T12:52:30Z
converted_from: SDD-11_The_Interaction_Design_v0.1.docx sha256 f6c718d6d135ed2a538acd7f6740873dc327e3857192685d2ecb69b4ab8ce7d5 (sdd-kit carries its text as Markdown)
---

# SDD-11 · The Interaction Design — the checklist

*Produced from the document named above by `_working/2026-09-28_the_checklists/extract_checklist.py`, as the last step of its build, and never edited by hand. Every line below is the document's own words, read from it, except the lines in italics, which are this program's.*

*Rules counted in the document: 29. The document states "IXD-1 to IXD-29, twenty-nine rules" (29).*

## Gate — the program's half

### 8 The gate after the step — the words before its first subsection

The owner's word is that the step is not to be skipped, and a step that rests on a person remembering it can be skipped by a person forgetting it. So the step is closed by a program, at the one point every application passes: the admission of its application model to generation. This section describes what the delivery kit enforces. The refusal is the kit's, and not a rule of this standard, and it is built in the kit by a round of its own; until that round is done, it is described here and is not yet enforced.

### 8.1 What the model names

The application model's model section carries one entry, interaction_design, which names the accepted document by its path relative to the model and by its SHA-256 checksum. Whoever writes the model writes the entry from the accepted document. It is the model's statement of what it was compiled from, which SDD-07, section 15, already requires of a model, and which no model has yet carried.

### 8.2 What the kit refuses

A rule of the kit's validator, reported as an error and never as a warning, refuses a model:

1. that names no interaction design;

2. that names a file which is not there;

3. whose checksum is not the file's;

4. whose document's header does not stand at baselined, with a name and a date;

5. whose document does not cover a goal the model's forms and lists name;

6. whose lists disagree with the Lists table: maintained or fixed, the role that maintains, the categories of a long list, or the code shown as its label, other than the decision;

7. whose references disagree with the References table: a reference the table says is found by a search, placed as a drop-down, a group of radio buttons or a check-box; or fills and locks other than the table's;

8. whose moves disagree with the Moves table: a move the table lists with no act on its record's form carrying the table's words and role, or an act for a move the table does not list as a person's;

9. whose acts disagree with the Acts table: an act the table says carries a record that does not carry it, or its form on a visible menu where the table says it may not stand there.

Checks 6 to 9 compare each row of a table with the construct of the model that carries it. How a row names that construct, and the words the gate reads in each column it compares, are fixed by the template of the document that the delivery kit's round building the gate adds; this standard fixes the headings and what each column means.

### 8.3 Where it refuses, and what cannot turn it off

The refusal stands in the kit's validation, and — because a check made by one command is skipped by calling another — at the start of generation, of the build and of the deployment, each of which calls the same check before anything else and refuses on it. No switch turns it off: not a key in the model, not a line of the kit's settings, not the custody mode, not a flag on a command. The kit's worked reference, its test fixtures and a model harvested from a running application are no exception: each is given an interaction design, or is refused.

## Gate — the person's half

### 9 The review

Run this before the document is put to the owner for acceptance, and again whenever it is brought forward for an increment of the model. Its writer runs it. The document is put to the owner only when every applicable line is satisfied or recorded as a finding with a named owner; a line that is not satisfied is not an exception to be set aside.

| Rules | Checkpoint | Passed |
|---|---|---|
| IXD-1, IXD-5 | Every goal the document covers is accepted, its description and its screen record at baselined with a name and a date, each named with its version. No goal that is not accepted is designed. Earlier decisions are carried forward, and any that is re-opened is a finding put to the owner. | ☐ |
| IXD-2, IXD-29 | The document's path and checksum are those the application model will name; nothing in it has changed since it was accepted without being accepted again. | ☐ |
| IXD-3, IXD-4 | One document for the application or the increment; its status in the three words; when baselined, the owner's name and the date. | ☐ |
| IXD-6 | Nothing the entity model or the groundwork owns is decided in the document; every silence or disagreement there is a finding with that document's owner. | ☐ |
| IXD-7, IXD-8 | Every silence of the goals is stated with its recommended answer and the row that carries it; every finding names its document and its owner; nothing the step read was changed. | ☐ |
| IXD-9 | No row decides what every application is given; each row names its pattern and only the particulars that pattern needs. | ☐ |
| IXD-10 to IXD-14 | Every list in the first listing has a row of the Lists table, saying whether it is maintained or fixed and by whom, where its first values come from, whether its code is shown as its label, and what it depends on and how; every long list has its categories, none holding more than nine. | ☐ |
| IXD-15 to IXD-18 | Every reference a person picks in the second listing has a row of the References table, with its record set and its size, how it is found, its keys and the columns of its result where it is searched, what it fills and locks, and what the person is told when nothing is found. | ☐ |
| IXD-19 to IXD-22 | Every move a person makes, of every record in the third listing, has a row of the Moves table, with its goal and act, its role as the groundwork gives it, the words of its button and the words of its guard; every state in which values become read-only has a row of the Read-only table. | ☐ |
| IXD-23 | Every act in the fourth listing that opens a form has a row of the Acts table; no form that needs a record stands on a menu. | ☐ |
| IXD-24, IXD-25 | The four listings were produced by the program the header names, and compared with the screen records as sets; every pattern the application uses has its page, produced by a program. | ☐ |
| IXD-26 to IXD-28 | The document has its seven parts, in order; it opens with the answer; the five tables carry their headings exactly; the owner is asked to read the header, the answer, the tables and the pages. | ☐ |

What this review does not do. Every line above tests something that is recorded, measured or named. None of them asks whether a decision is the right one — whether a list's categories are those the business uses, whether a guard's words will be understood, whether a search's keys are those the officers have at hand. That is the owner's reading, and section 11 states the limit it leaves.

## Form

### 7 The form of the document

| line | rule |
|---|---|
| 1. The header: its identifier, its version and its status in the three words, with the owner's name and the date when it is baselined; every goal it covers, each by its identifier, with the version of its description and of its screen record; and the program that produced its listings, by path and checksum. | not stated |
| 2. The answer in one paragraph: how many lists, references a person picks, records with a state and acts that open a form the goals hold; what the owner is asked to accept; and on what the goals were silent. | not stated |
| 3. The decisions, in the five tables below. | not stated |
| 4. The pages, one for each pattern the application uses (IXD-25). | IXD-25 |
| 5. Where the goals were silent, each with the recommended answer and the row of a decision table that carries it (IXD-7). | IXD-7 |
| 6. The findings raised, each against the document that owns the fact, with its owner (IXD-8). | IXD-8 |
| 7. The appendix: the four listings, and the program's comparison of them with the screen records (IXD-24). | IXD-24 |

| line | rule |
|---|---|
| Lists | IXD-27 |
| References | IXD-27 |
| Moves | IXD-27 |
| Read-only | IXD-27 |
| Acts | IXD-27 |

## Rules

| rule | words | program |
|---|---|---|
| IXD-1 | Write the interaction design after the owner has | none |
| IXD-2 | Admit no application model to generation without an | none |
| IXD-3 | Write one document for the application, and put | none |
| IXD-4 | Record the owner's acceptance as baselined, with his | none |
| IXD-5 | Take the step again for every increment of | none |
| IXD-6 | Read what the entity model and the groundwork | none |
| IXD-7 | Where the goals are silent, say so and | none |
| IXD-8 | Raise findings against what the step reads, and | none |
| IXD-9 | Do not ask what every application is given | none |
| IXD-10 | Decide whether each list is maintained in the | none |
| IXD-11 | Say where each list's first values come from | none |
| IXD-12 | Decide whether each list's code is what the | none |
| IXD-13 | Decide whether each list depends on another value, | none |
| IXD-14 | Give every long list its categories | none |
| IXD-15 | Name the record set each reference points at, | none |
| IXD-16 | State what each search takes, and what its | none |
| IXD-17 | State what choosing a record fills on the | none |
| IXD-18 | State what the person is told when nothing | none |
| IXD-19 | Name the act of the goal that makes | none |
| IXD-20 | Give each move's button the goal's own words, | none |
| IXD-21 | State which values become read-only in which state | none |
| IXD-22 | Read who may make each move from the | none |
| IXD-23 | For every act that opens a form, state | none |
| IXD-24 | Produce the four listings by a program from | none |
| IXD-25 | Show each pattern the application uses on a | none |
| IXD-26 | Open the document with the answer in one | none |
| IXD-27 | Hold the decisions in five tables with fixed | none |
| IXD-28 | Put before the owner the answer, the decision | none |
| IXD-29 | Have a document changed after acceptance accepted again, | none |
