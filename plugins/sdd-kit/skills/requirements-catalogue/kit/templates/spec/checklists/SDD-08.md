---
standard: SDD-08
title: The Software Architecture Document
edition: "1.0"
document: SDD-08_The_Software_Architecture_Document_v1.0.md
sha256: 762846a7ae4bcc3d041cc04194a987c8cab1845c2e51e9aa08f57775ea6aba5f
produced_by: _working/2026-08-31_architecture_standard/docx_build/build_ar01.js at 2026-09-29T20:23:07Z
converted_from: SDD-08_The_Software_Architecture_Document_v1.0.docx sha256 e54fd381fb4da70eda91833310ec36eea5ff4d17edabec1b25f547a7452f4b48 (sdd-kit carries its text as Markdown)
---

# SDD-08 · The Software Architecture Document — the checklist

*Produced from the document named above by `_working/2026-09-28_the_checklists/extract_checklist.py`, as the last step of its build, and never edited by hand. Every line below is the document's own words, read from it, except the lines in italics, which are this program's.*

*Rules counted in the document: 31. The document states "Thirty-one rules, a form to fill" (31).*

## Gate — the program's half

### 8. The review gate — the words before its first subsection

A finished specification is reviewed in two halves, because the two halves fail in different ways and mixing them produces a review that checks the boxes are full rather than that the answers are right.

### 8.1 What a program can check

A program can tell whether an answer is present, whether a name follows a pattern, and whether two documents that must agree do agree. It cannot tell whether an answer is any good. What follows is what will be checked mechanically.

> These checks are described here and have not been built. Nothing in the table below runs today. It is written out so that an architect knows what will be read mechanically, and so that whoever builds the checks knows what to build. No result may be reported from any of them until they exist, and a check is trusted only after it has been seen to refuse something.

| Check | What it reads | It fails when |
|---|---|---|
| ARC-C1 | every line of the form | a line is empty and carries no written reason for being empty |
| ARC-C2 | the platform binding | the version, edition or database is not one of the permitted exact values |
| ARC-C3 | the edition | a capability the edition forbids is used anywhere in the specification |
| ARC-C4 | every component entry | it names no purpose, or does not say whether it is configured once or per use |
| ARC-C5 | every component configuration | a setting is not one the component accepts |
| ARC-C6 | the negative list | it is absent — a specification with no rejected components has not considered any |
| ARC-C7 | every process | it names no machinery |
| ARC-C8 | every state a process uses | the record model does not have it, and no finding is recorded |
| ARC-C9 | every state change | it names no party that makes it |
| ARC-C10 | every crossing | any field crossing it is unnamed |
| ARC-C11 | every borrowed field | it names no issuer, no name space, no validity or no checking rule |
| ARC-C12 | every crossing | any of the three situations — missing, out of date, unreachable — has no answer |
| ARC-C13 | every crossing | it states nothing about what must not be stored |
| ARC-C14 | the whole specification | anything in it matches the shape of a password, key or token |
| ARC-C15 | every bespoke entry | it names no forcing requirement, or names one that does not exist in the requirement register |
| ARC-C16 | every bespoke entry | it does not say what it reads and what it writes |
| ARC-C17 | every decision record | it does not say what would make the decision wrong |
| ARC-C18 | every finding | it has no named owner or no date |
| ARC-C19 | the whole specification | a statement fills no part of the application model and is read by no check |
| ARC-C20 | the counts in part 6 | nothing. This one reports and never fails |

## Gate — the person's half

### 8.2 What only a person can judge

No program will decide any of these, and a review that skips them has checked that the form is full rather than that the specification is right.

- Whether the purpose written against a component is the real reason it is switched on, or the reason that was easiest to write.
- Whether the negative list is honest, or contains only the components nobody wanted anyway.
- Whether what the machinery decides and what it does not have been separated correctly, or whether a business decision has been quietly handed to the routing.
- Whether the answer for a missing value is right — whether absence should be shown as absence, or whether the operation should fail.
- Whether a freshness limit is the limit the business actually needs, or the limit the far side happens to offer.
- Whether the forcing requirement on a bespoke entry really forces it, or whether it is a requirement that happens to exist and was attached afterwards.
- Whether a decision's reversal condition is one anybody would notice if it occurred.
- Whether the specification is complete against the material it was written from — for which there is no test, and which is the reason section 8 has two halves rather than one.

## Form

### 7. The form the architect fills

#### 7.1 Part 1 — the application, once

| line | rule |
|---|---|
| Application | ARC-1 |
| Version, date, finished | ARC-2 |
| Platform version | ARC-6 |
| Edition | ARC-6 |
| Database | ARC-6 |
| What the edition forbids | ARC-7 |
| Conventions | ARC-8 |
| Documents read | ARC-3 |

#### 7.2 Part 2 — once for each component

| line | rule |
|---|---|
| Component and version | ARC-9 |
| Switched on to do | ARC-9 |
| Configured | ARC-10 |
| Configuration | ARC-12 |

#### 7.3 Part 3 — once for each process

| line | rule |
|---|---|
| Process | ARC-13 |
| Machinery | ARC-13 |
| What the machinery decides | ARC-14 |
| What it does not decide | ARC-14 |
| States used | ARC-15 |
| Who changes each state | ARC-16 |

#### 7.4 Part 4 — once for each crossing

| line | rule |
|---|---|
| Direction | ARC-17 |
| Far side | ARC-17 |
| What crosses | ARC-17 |
| Meaning | ARC-21 |
| Format | ARC-21 |
| Issuer | ARC-18 |
| Name space | ARC-18 |
| Validity | ARC-18 |
| How it is checked | ARC-18 |
| Freshness shown | ARC-19 |
| If the value is missing | ARC-19 |
| If the value is out of date | ARC-19 |
| If the far side cannot be reached | ARC-19 |
| Must not be stored | ARC-20 |
| How both sides check it | ARC-22 |
| Authentication | ARC-23 |
| If an incoming instruction cannot be carried out | ARC-24 |

#### 7.5 Part 5 — once for each bespoke component

| line | rule |
|---|---|
| What it is | ARC-26 |
| What was tried first | ARC-25 |
| Forced by | ARC-26 |
| Reads / writes | ARC-27 |
| Wanted elsewhere | ARC-28 |

#### 7.6 Part 6 — decisions and findings, once at the end

| line | rule |
|---|---|
| Each decision | ARC-5, ARC-29, ARC-30 |
| Each finding | ARC-4 |
| Each withdrawal | ARC-31 |
| Counts, stated and not judged | — |

## Rules

| rule | words | program |
|---|---|---|
| ARC-1 | One specification for one application. The unit is | none |
| ARC-2 | The specification states its version, its date and | none |
| ARC-3 | Every statement in the specification either fills a | none |
| ARC-4 | Where the specification cannot answer a question, it | none |
| ARC-5 | Where the specification takes a decision, it records | none |
| ARC-6 | The specification names the platform version, the edition | none |
| ARC-7 | Where the chosen edition forbids something the application | none |
| ARC-8 | Conventions that apply across the whole application — | none |
| ARC-9 | Every component switched on is listed with what | none |
| ARC-10 | Every component states whether it is configured once | none |
| ARC-11 | The catalogue also lists components that were available | none |
| ARC-12 | A component is not entered in the catalogue | none |
| ARC-13 | Every business process names which machinery runs it | none |
| ARC-14 | For each process, the specification states which decisions | none |
| ARC-15 | A process never introduces a state the record | none |
| ARC-16 | Every change of state names the party that | none |
| ARC-17 | Every crossing is listed, in both directions, down | none |
| ARC-18 | Every field this application borrows rather than creates | none |
| ARC-19 | Every crossing states how fresh its information is, | none |
| ARC-20 | Every crossing states what this application must not | none |
| ARC-21 | The meaning of what crosses is stated separately | none |
| ARC-22 | Every crossing states what would let both sides | none |
| ARC-23 | No password, key, secret or credential appears anywhere | none |
| ARC-24 | An incoming instruction states what the application does | none |
| ARC-25 | Something is written specially only after both the | none |
| ARC-26 | Every bespoke entry names the requirement that forced | none |
| ARC-27 | Every bespoke entry names what it reads and | none |
| ARC-28 | A bespoke component that is needed by a | none |
| ARC-29 | A decision is recorded once, in one place, | none |
| ARC-30 | A decision record names what would make it | none |
| ARC-31 | Nothing is deleted. A withdrawn component, crossing, process | none |
