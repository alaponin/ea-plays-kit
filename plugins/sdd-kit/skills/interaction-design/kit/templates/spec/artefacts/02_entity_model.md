<!--
standard: SDD-03
title: The Entity Model
edition: "1.0"
document: SDD-03_The_Entity_Model_v1.0.md
sha256: 7f128a3e0c2e599651a6e37164dbe6e7c472a8d72853abfef75feb1156a72fdc
produced_by: _working/2026-08-31_house_rebuild/build_house.js at 2026-09-29T22:04:38Z
converted_from: SDD-03_The_Entity_Model_v1.0.docx sha256 f0ec3c8e9e00310cbde3f985370d8858e95c483d8f7c206f53131b9be9eee52e (sdd-kit carries its text as Markdown)
-->

# The entity model

*Written to SDD-03, The Entity Model, edition 1.0. Produced from the standard by `_working/2026-09-28_the_checklists/extract_checklist.py`, as the last step of its build; a copy of it is filled, and this file is never edited by hand. The quoted lines are the standard's own words.*

## 5.1 For each record

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Name | A singular noun phrase in the words the business uses, unique across the whole model | EM-16 |  |
| Definition | One row per ____ . Singular, standing on its own, not repeating the name, carrying no rationale or procedure | EM-15 |  |
| Why it is a record | More than one row; more than one fact; means something on its own; can be told apart from every other kind. All four, or a written reason for the exception | EM-11 |  |
| Identified how | On its own; or only through ____ , and the relationship that supplies the identity is named in the relationship form | EM-12 |  |
| Special kinds | None; or branches ____ . Do the branches cover every row (yes / no)? May one row be in two at once (yes / no)? Both answered | EM-14 |  |
| Parts played | Any capacity a row acts in that is not exclusive is a link and not a branch. List them: ____ | EM-13 |  |
| Attributes, each with its least and most | For every attribute: the fewest that may be there and the most. Two separate decisions | EM-17 |  |
| What the minimums mean | Confirm the minimums are the model's floor and not one screen's rule | EM-18 |  |
| Attributes holding more than one value | None; or ____ , each of which becomes a record | EM-23 |  |
| Where each attribute belongs | For every attribute: it describes one row of this record. Where it describes another record, it moves there and the link between the two records is drawn | EM-52 |  |
| Attribute names | No attribute name repeats this record's name. Where a qualifier is needed to tell two attributes apart, it is the qualifier that distinguishes them and never the record's name | EM-53 |  |
| Made-up identifiers | None at this level; or ____ , each with the reason it is here | EM-25 |  |
| Coded attributes | For each: the governed list ____ , named as its row in the table of governed lists names it — or the named selection of one ____ , named as its entry in SDD-04 names it — and the strength of binding. Its owner was asked here until version 0.2; it is now the issuer on the list's row, cited and not repeated | EM-19, EM-47 |  |
| The governed lists used | For each: is it versioned, and are values retired rather than removed (yes / no / not known). Who issues it is on the list's row and is not repeated here | EM-20, EM-47 |  |
| History kept | None; when the fact was true; when the system was told; both. A none carries a reason | EM-21 |  |
| Coded values, as at | For each coded attribute the record stores: the stored value carries the date it was resolved as at, on the clock the record keeps — or the reason the record keeps neither clock covers it | EM-21 |  |
| Uniqueness | Over the identifier alone; or over the identifier and the period, where history is kept | EM-22 |  |
| Boundary | This system is the authority — and nobody else consumes it, or it is published for others, to ____ ; consumes it from ____ ; must not hold it — held instead by ____ . Then, on every answer but the first: who issues it ____ (the body, never the software); where the issuer publishes it ____ . And on every answer: the words in the client's material this was derived from ____ , or not stated by the client; asked of ____ on ____ | EM-2, EM-45, EM-48 to EM-50 |  |
| Groups it is read in | ____ (a record may be in more than one) | EM-3 |  |
| Facts deliberately recorded twice | None; or ____ , each with the reason and with how the copies are kept in step | EM-24 |  |
| Related to | The records this one is related to: ____ . Or the written reason it stands alone | EM-54 |  |

> A record that answers only the definition line has not been described. It has been named.

## 5.2 For each relationship

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Name, reading from this end | ____ (what the link is, plus the thing at the far end) | EM-26 |  |
| Name, reading from the far end | ____ — so that both directions read as complete sentences | EM-32 |  |
| Read back, in both directions | The two sentences as they were put to a business reader, in the form EM-32 states, and the answer each got. A reading nobody recorded cannot be told from a reading nobody did | EM-32 |  |
| Degree | ____ rows at this end go with ____ rows at the far end | EM-17 |  |
| Optionality | May this end be absent (yes / no)? May the far end (yes / no)? | EM-17 |  |
| If both ends are optional | The reason, written out — or the relationship is corrected | EM-33 |  |
| Identifying or referring | Does this relationship supply the far record's identity (yes / no)? | EM-12 |  |
| Facts of its own | None; or ____ — and if there are any, it is a record and is written up as one | EM-27 |  |
| If many at both ends | The record it resolves into: ____ | EM-28 |  |
| Excluded by another relationship | No; exclusive with ____ , and the exclusion is written in the model | EM-30 |  |
| On removal, replacement or correction | The far row goes too; the far row is left pointing at nothing; the removal is refused; the near row is never removed, only superseded | EM-31 |  |
| Loops back to the same record | No; yes, and the relation it carries is: is a kind of; is part of; is grouped with; supersedes | EM-29 |  |

## 5.3 For the model as a whole

> This is the part that is filled once, and the part that is most often not filled at all.

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Level | Naming the things the business deals with; structuring them into records with identifiers and relationships; describing how they are stored — and what is therefore excluded | EM-1 |  |
| What this model is of | The records this system keeps, and the records and lists it depends on, whoever keeps them. If the module must also publish what it exchanges with other systems, that is a second document, named here: ____ | — |  |
| Boundary statement | The records this system is the authority for and nobody else consumes ____ ; the records it is the authority for and publishes, and to whom ____ ; the records it consumes, and from whom ____ ; the kinds of thing it deliberately does not hold, and where each is held instead ____ | EM-2, EM-45 |  |
| Groups | The named groups, each small enough to read; the records appearing in more than one; and how a relationship crossing two groups is shown in both | EM-3 |  |
| Counts, stated and not judged | How many records; how many relationships; how many records carry no definition; how many relationships carry no name. No threshold is set and none may be inferred | EM-3, EM-6 |  |
| The two clocks | Which records keep when a fact was true, which keep when the system was told, which keep both, and which keep neither — with a reason for each neither | EM-21 |  |
| Normal form | The form the model is held to, and every place it is deliberately departed from, with the reason and with how the copies are kept in step | EM-24 |  |
| Extension rule | What a later version may change and what it may not — written before there is a later version | EM-4 |  |
| Notation | Which one notation this model uses ____ ; and what that notation cannot say, listed, with where each of those things is written instead | EM-9, EM-10 |  |
| Layout convention | The convention every generated picture follows: where the many end of a relationship is placed, where relationship names sit, and what the title of every picture carries | EM-55 |  |
| The pictures | Which pictures exist, what each is for, who reads each, and which single model they are all generated from | EM-7, EM-8 |  |
| The register beside the pictures | Where the definitions live; where the derivations live. Where the governed lists live was asked here until version 0.2 and is superseded by the table of governed lists on the next line | EM-7 |  |
| The table of governed lists | One row for every list any coded attribute names, in the columns laid out below this form, filled once for the model. A list an attribute names that has no row, and a row with no classification or no source line, is an unanswered line of this form | EM-47 to EM-51 |  |
| Written in the first pass | Confirm that every classification and its reference lines were written before any goal was named; where one was not, it is recorded as a finding with an owner | EM-51 |  |
| The two passes | Which lines of this form belong to the first pass and which to the second, wherever the assignment departs from the list in part 5; and whether this model is reported as finished for the first pass or finished outright | EM-56 |  |
| Owner and change procedure | Who owns the model; who may propose a change; who decides | EM-5 |  |
| Review | Who reviews it, against what list, and which items on that list a program cannot check | EM-6 |  |
| The depth worked at | The level of detail this model was drawn to, in the analyst's own words, applied consistently across every record. This standard does not yet say which depth to choose | not settled |  |
| Open questions | The decisions genuinely in dispute, each with a named owner and a date — never closed by a silent default | — |  |

> The table of governed lists — one row for every list any coded attribute names. These are its columns. A row is complete when every column has an answer or a written reason for having none, on the same test as every other line of this form.

| List | Classification | Issuer | Where the issuer publishes it | Source in the client's material | Consumers known |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

- **List** — The name the model uses for it, as the coded attributes name it (EM-47)
- **Classification** — This system's and nobody else's; this system's and published for others; held elsewhere, consumed here; not held at all — held instead by ____ . Made from this system's position (EM-2, EM-45, EM-46)
- **Issuer** — The body whose act makes a value a member — never the software that serves the list. Or not stated by the client; asked of ____ on ____ . Not asked where the list is this system's and nobody else's (EM-48, EM-50)
- **Where the issuer publishes it** — The document, register, view or service a reader goes to for the current edition, and the place in it. Or not stated by the client; asked of ____ on ____ . Not asked where the list is this system's and nobody else's (EM-49, EM-50)
- **Source in the client's material** — The document, the place, the words — or that the client was silent, and who was asked and when (EM-50)
- **Consumers known** — Only where the classification is published for others: who, from the client's material, or none named. On every other answer, not applicable (EM-45)
