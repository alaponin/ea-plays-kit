---
standard: SDD-06
title: One System Use Case
edition: "1.2"
document: SDD-06_One_System_Use_Case_v1.2.md
sha256: b414e78337ac134cf51a3cbe6477e6653b2c7aabd585de0130bc9df703c6f50a
produced_by: _working/2026-08-31_house_rebuild/build_house.js at 2026-09-29T09:30:52Z
converted_from: SDD-06_One_System_Use_Case_v1.2.docx sha256 4f3d6ac19817d798b9804bed57c35b6554364f66463eb5a6ab9e5301ba063c1b (sdd-kit carries its text as Markdown)
---

# SDD-06 · One System Use Case — the checklist

*Produced from the document named above by `_working/2026-09-28_the_checklists/extract_checklist.py`, as the last step of its build, and never edited by hand. Every line below is the document's own words, read from it, except the lines in italics, which are this program's.*

*Rules counted in the document: 21. The document states "Twenty-one rules, a template written out in full" (21).*

## Gate — the program's half

### 8 The review — the words before its first subsection

Run this on one use case, at its review, before it is accepted. The reviewer pair and the tester run it together. Run the whole of it once for each use case: a verdict given for a set hides the one member of the set that fails.

The review has two halves. The first is what a reader — and, in time, a program — can confirm by looking. The second is what only a person can judge, and it is not the lesser half.

### 8.1 What a reader can check

Rule references point to the clause each line enforces. Every rule of this standard is enforced by at least one line.

| Rules | Checkpoint | Passed |
|---|---|---|
| U1–U2 | The form matches the risk the model set for this use case, and a use case written out in full carries every field of the template deliberately. | ☐ |
| U18 | The record header is present, and every field in it is filled or carries a written reason for being empty. | ☐ |
| U19 | The requirements, quality requirements and constraints this use case realises are recorded in the header by identifier. | ☐ |
| U20 | Every entity the use case reads or changes is named in the header, and every name is one the entity model defines. | ☐ |
| U3 | There is exactly one main success scenario, of three to nine steps, with no branching in it. | ☐ |
| U4 | Each step says who is acting and shows progress; almost every actor action has a system response. | ☐ |
| U5 | No screen, no control, no stored record and no technology appears in any flow. | ☐ |
| U6–U7 | The stakeholders' interests are listed and fully covered by the guarantees; the preconditions and both guarantees are precise. | ☐ |
| U8–U9 | Extensions are numbered to their step, are exhaustive and detectable, are marked as a business alternative or a system failure, and each says whether it rejoins, succeeds or fails. | ☐ |
| U10–U11 | Data appears by name only; every concept uses the model's one word and no word is invented here. | ☐ |
| U12 | The quality requirements that bind this use case are attached to it, and are quantified by reference rather than by adjective. | ☐ |
| U21 | Every business rule the use case depends on is cited by its register identifier; none is written out in a step. | ☐ |
| U19–U21 | Every identifier the header cites for something the shared registers publish resolves in the set its register publishes under the standard for the shared registers (SDD-04, IOS-15), read in the shape that standard's setting registers.published_set_shape names. The reviewer pair answers this line at the review; it is the point at which the shared registers are handed to this use case. | ☐ |
| U13 | Nothing out of scope and nothing belonging to a second business process appears: one use case, one goal, one sitting. | ☐ |
| U16–U17 | No decision hides inside a vague word, and each step carries one rule. | ☐ |
| U14 | Acceptance tests derived from the main success scenario and from every extension exist. | ☐ |
| U15 | The use case can be built from: the same behaviour on two independent readings, acceptance criteria derivable without a question, nothing left for a reader to invent. | ☐ |

A line that is not satisfied is a finding with a named owner. It is not an exception to be waved through.

## Gate — the person's half

### 8.2 What only a person can judge

A program can see that a field is filled. It cannot see whether what fills it is true. These questions stay on the review list however many automatic checks are built, and U15 is the first of them — it is a rule, it is a line of the review above, and it is a judgement made by two people about one piece of prose. Nothing automates it.

- Can it be built from? Do two people, reading it separately, describe the same behaviour? Can a tester write acceptance criteria without asking a question? Is there nothing left that a developer or a reviewer has to invent? Ask it at the review, and record a failure against the clause that caused it (U15).
- Are the stakeholders' interests the whole of what this use case must guarantee, or only the part somebody thought of (U6)?
- Is each precondition genuinely already true when the use case starts, or is it a check that has quietly been left out of the flow (U7)?
- Are the extensions exhaustive, as opposed to merely numerous? Did anyone go step by step and ask what else the system can detect here (U9)?
- Does a step that reads as one action really contain two, which fail for different reasons (U17)?
- Are these the words the business itself uses, in the sense the business uses them — or the model's words applied correctly to the wrong thing (U11)?
- Do the acceptance tests test the guarantees, or only the steps (U14, U7)?
- Is this one goal at one level, or two goals that have been run together under one name? If it is two, that is raised about the model rather than solved by writing (U13).
- Is the use case finished? No published test says when it is. The answer this standard uses is U15: it is finished when it can be built from.

### 8.3 The gate

Every line of section 8.1 is answered, and every question in section 8.2 has been asked out loud by the reviewer pair, before the use case is accepted.

## Form

### 7.1 The record header

| line | rule |
|---|---|
| Unique identifier | not stated |
| Use case name | not stated |
| Level | not stated |
| Primary actor | not stated |
| Status and priority | not stated |
| Requirements realised | U19 |
| Entities read or changed | U20 |
| Business rules cited | U21 |
| Relationships | not stated |

### 7.2 The narrative fields

| line | rule |
|---|---|
| Scope | not stated |
| Stakeholders and interests | U6 |
| Preconditions | U7 |
| Trigger | not stated |
| Minimal guarantee | U7 |
| Success guarantee | U7 |
| Main success scenario | U3, U5 |
| Extensions | U8, U9 |
| Quality requirements | U12 |
| Acceptance tests | U14 |

## Rules

| rule | words | program |
|---|---|---|
| U1 | Use the lightest form that is adequate. | none |
| U2 | When the form is the full one, fill | none |
| U18 | Carry the record header. | none |
| U19 | Record the requirements this use case realises. | none |
| U20 | Declare the entities it reads and the ones | none |
| U3 | Write one main success scenario, with no conditions | none |
| U4 | Write steps that say who is acting, and | none |
| U5 | Write about intent and responsibility, not screens or | none |
| U6 | Let the stakeholders' interests decide what complete means. | none |
| U7 | State the preconditions and the guarantees precisely. | none |
| U8 | Number each extension against the step it leaves. | none |
| U9 | Look for every extension, but only ones the | none |
| U10 | Refer to data by name only. | none |
| U11 | Use the model's word, and never invent another. | none |
| U12 | Attach quality requirements to the use case they | none |
| U21 | Cite the business rules; never write them out. | none |
| U13 | Keep out what belongs somewhere else. | none |
| U16 | Do not leave a decision hidden inside a | none |
| U17 | One rule to a step. | none |
| U14 | Pair every use case with its acceptance tests. | none |
| U15 | Test that it can be built from, before | none |
