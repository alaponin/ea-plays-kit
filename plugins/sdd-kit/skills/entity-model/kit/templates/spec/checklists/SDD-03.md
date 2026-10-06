---
standard: SDD-03
title: The Entity Model
edition: "1.0"
document: SDD-03_The_Entity_Model_v1.0.md
sha256: 7f128a3e0c2e599651a6e37164dbe6e7c472a8d72853abfef75feb1156a72fdc
produced_by: _working/2026-08-31_house_rebuild/build_house.js at 2026-09-29T22:04:38Z
converted_from: SDD-03_The_Entity_Model_v1.0.docx sha256 f0ec3c8e9e00310cbde3f985370d8858e95c483d8f7c206f53131b9be9eee52e (sdd-kit carries its text as Markdown)
---

# SDD-03 · The Entity Model — the checklist

*Produced from the document named above by `_working/2026-09-28_the_checklists/extract_checklist.py`, as the last step of its build, and never edited by hand. Every line below is the document's own words, read from it, except the lines in italics, which are this program's.*

*Rules counted in the document: 56. The document states "Fifty-six rules, a form in five parts" (56).*

## Gate — the program's half

### 6 The quality check, which is also the review gate — the words before its first subsection

Run this before an entity model is agreed, and before anything is built from it. A model passes when every line of the form in part 5 has an answer or a written reason for having none. An unanswered line is recorded with an owner, not waved through.

### 6.1 What a program will refuse, once the checks are built

None of the checks below is built. They are printed here so that an analyst knows what will be read mechanically, and so that whoever builds them knows what to build. No result of any kind may be reported from this section until they exist.

|  | What the program reads | What makes it fail | Rule |
|---|---|---|---|
| C1 | every record's definition | absent, empty, or the record's own name with nothing else | EM-15 |
| C2 | every record's definition | it defines itself — the name followed by is a and nothing further | EM-15 |
| C3 | every record's definition | it carries usage or rationale: used by, so that, in order to, because | EM-15 |
| C4 | every record's name | plural, or the same as another record's name | EM-16 |
| C5 | every attribute | no least and most stated | EM-17 |
| C6 | every relationship end | no degree, or no optionality, stated at that end | EM-17 |
| C7 | every relationship | no name, or a name that is related to, associated with, linked to, has, refers to | EM-26 |
| C8 | every relationship | many at both ends, unresolved | EM-28 |
| C9 | every relationship whose two ends are the same record | no statement of what the loop carries | EM-29 |
| C10 | every relationship | no statement of what happens at the far end when a row is removed | EM-31 |
| C11 | every relationship | it carries attributes of its own and is not declared a record | EM-27 |
| C12 | every record with special kinds | the covering answer or the overlap answer is missing | EM-14 |
| C13 | every coded attribute | it names no governed list, or names one with no strength of binding | EM-19 |
| C14 | every record | no boundary answer — authority, consumes, or does not hold | EM-2 |
| C15 | every record answering does not hold | no statement of where it is held instead | EM-2 |
| C16 | the model's heading | no level declared | EM-1 |
| C17 | a model declared at the highest level | a record carries an identifier, a column type or an index | EM-1 |
| C18 | the group assignments | a record is in no group; or a group holds more records than the size the model itself stated | EM-3 |
| C19 | the group assignments | a relationship crosses two groups and is shown in neither, or in only one | EM-3 |
| C20 | the model's heading | no extension rule stated | EM-4 |
| C21 | every record | no history answer | EM-21 |
| C22 | every record that keeps history | uniqueness stated over the identifier alone | EM-22 |
| C23 | the model's heading | no owner, or no change procedure | EM-5 |
| C24 | the counts | nothing. This one reports and never fails | EM-3, EM-6 |
| C25 | the model's heading | no glossary named, or no register of business rules named | EM-34, EM-40 |
| C26 | every glossary entry | no definition, an empty one, or one that is the term itself with nothing else | EM-36 |
| C27 | every glossary entry | no status, or no statement of where the term comes from | EM-36 |
| C28 | the glossary | two entries carrying the same term, or one concept carried by two preferred terms | EM-34, EM-37 |
| C29 | every term named in the entity model and in the glossary | it is in both | EM-35 |
| C30 | every withdrawn term and every withdrawn rule | no date, or no reason | EM-38, EM-43 |
| C31 | every business rule | no identifier, or an identifier already used by another rule | EM-40 |
| C32 | every term used in a rule statement | it appears in neither the glossary nor the entity model | EM-42 |
| C33 | every business rule | no statement of where its authority comes from, or no date it takes effect from | EM-42 |
| C34 | every business rule | nothing cites its identifier. This one reports and never fails | EM-44 |
| C35 | every record answering that this system is the authority | no statement whether anybody else consumes it; or published for others with no consumer named and no none named | EM-45 |
| C36 | every record not this system's and nobody else's | no issuer named, and no statement that the client was silent with who was asked | EM-48, EM-50 |
| C37 | every governed list any coded attribute names | it has no row in the table of governed lists | EM-47 |
| C38 | every row of the table of governed lists | no classification, or no source line | EM-47, EM-50 |
| C39 | every attribute name | it repeats the name of the record that holds it | EM-53 |
| C40 | every record | it is related to no other record and carries no written reason for standing alone | EM-54 |
| C41 | the model's heading | no layout convention declared | EM-55 |
| C42 | every relationship | no read-back recorded, in either direction | EM-32 |
| C43 | every line the form marks as first-pass | unanswered, where the model reports itself finished for the first pass | EM-56 |

Two of these report and never fail, deliberately. C24 is a count: no evidence was found for any threshold on the number of records or relationships a model should have, so none is enforced, and writing one would mean inventing a number nobody has counted. C34 is the other: a rule nothing cites may be dead or may be one nobody is maintaining, and a program cannot tell which. Both report and the owner decides.

Thirty-six of the fifty-six rules are named by a check above, counted on 14 September 2026 as the distinct rules the Rule column cites. The remaining twenty are judged by a person until checks exist for them. Version 0.2 gave the first of those two figures as twenty-six of forty-four; the same count taken the same way on that edition's table gives twenty-seven, and the difference is recorded here rather than corrected silently.

Version 0.4's table named thirty-one. The five checks version 0.5 added name five rules no check had named before: EM-53, EM-54, EM-55 and EM-56, which are new, and EM-32, which has been in the standard since version 0.1 and had no check until the read-back gave it something a program can read. EM-52 is not named by any check and cannot be: no program can read whether an attribute describes the record it is drawn on.

Four checks that cannot be written, said plainly so that nobody implies otherwise. No program can read whether the boundary was drawn in the right place; whether one name is carrying two things; whether a claim of nobody else's is true; or whether the body named as an issuer is a body rather than the software that serves the list. Each of those is a person's judgement, and each is on the list in part 6.2. The four checks above read whether the answers are present. They cannot read whether they are right, and a check result — once any exists — says nothing about that.

## Gate — the person's half

### 6.2 What only a person can judge

A program can see that a field is filled. It cannot see that what fills it is true. These stay on the review list however many checks are built.

- Whether a definition is true, as opposed to present.
- Whether the thing described is really one kind of thing, or two that have been run together.
- Whether the degree and the optionality on a relationship match how the business actually behaves, rather than how the first example behaved.
- Whether the boundary is drawn in the right place — whether a record this system claims authority over is really somebody else's register.
- Whether a claim that a record is this system's and nobody else's is true. A program can see that the answer was given and cannot see that nobody consumes the record; the actor catalogue and the catalogue of events are where a consumer the claim missed will surface.
- Whether one name is carrying two things — a shared code and a set of values this module configures under the same word — which a row of the table of governed lists cannot show and the second question on this list can.
- Whether the body named as an issuer is a body at all, and not the platform, database or service that stores and serves the list.
- Whether the branches of a special kind are the branches the business would recognise, and whether what is drawn as a branch is really a part somebody plays.
- Whether the governed list a coded attribute points at is the right list — and, where it points at a named selection, whether the selection is the module's to define.
- Whether a figure inside a rule's statement is a fact of law or a setting the administration may change. A program can see a number; it cannot see who may change it.
- Whether the picture, read aloud in both directions, says something a person from the business agrees with.
- Whether one notation has been used throughout, and whether what that notation cannot say has been written down somewhere else.
- Whether a relationship optional at both ends is meant.
- Whether each attribute describes the record it is drawn on, or the record the paper form printed it on.
- Whether a record that stands alone is genuinely standalone, or one whose relationships nobody has drawn yet.
- Whether the read-back was put to a business reader as a question, or recited at him.
- Whether the model is finished. No published test for this exists in any discipline or any of the six fields; the answer this standard uses is that every question is answered, or carries a written reason for having none.

### 6.3 The gate

Every line is answered before the model is agreed.

| Rules | Checkpoint | Passed |
|---|---|---|
| EM-1, EM-2 | The level is declared, and every record says whether this system is its authority, consumes it, or does not hold it — with the holder named where it does not | ☐ |
| EM-3 | The records are grouped into named groups small enough to read, and every relationship crossing two groups is shown in both | ☐ |
| EM-4, EM-5 | An extension rule is written, and the model names an owner and a procedure for changing it | ☐ |
| EM-6 | Every rule the model is judged against says whether a program reads it or a person judges it | ☐ |
| EM-7, EM-8 | The pictures carry what a reader can check, the rest is in the register beside them, and every picture is generated from one model | ☐ |
| EM-9, EM-10 | One notation is declared and used throughout, and what it cannot say is written down elsewhere | ☐ |
| EM-11, EM-15, EM-16 | Every record passes the four tests, carries a definition that says what one row is, and has a singular, unique name | ☐ |
| EM-12, EM-13, EM-14 | Dependence is declared at both ends; parts played are not drawn as special kinds; and every special kind answers both the covering and the overlap question | ☐ |
| EM-17, EM-18 | Every attribute and every relationship end states the least and the most, as two decisions; the minimums are the model's floor and not one screen's | ☐ |
| EM-19, EM-20 | Every coded attribute names its governed list, or a named selection of one, and the strength of the binding; a setting that selects from a list is bound at the strongest strength; and every list named is versioned with values retired rather than removed | ☐ |
| EM-21, EM-22 | Every record says which clock or clocks it keeps, every stored coded value carries the date it was resolved as at, and uniqueness on a record that keeps history is stated over the period | ☐ |
| EM-23, EM-24, EM-25 | No attribute holds more than one value at once; the normal form is stated with every deliberate departure recorded; made-up identifiers are absent or justified | ☐ |
| EM-26, EM-27, EM-28 | Every relationship is named; one carrying facts of its own is a record; none is left many at both ends | ☐ |
| EM-29, EM-30, EM-31 | Loops say what they carry; exclusive choices are in the model and not in a note; every relationship says what happens at its far end | ☐ |
| EM-32, EM-33 | Every relationship reads as a sentence in both directions, was read back to a business reader in the form EM-32 states with the answer recorded, and any relationship optional at both ends carries its reason | ☐ |
| EM-34, EM-35 | One glossary is named; one term carries each concept; and no word is in both the glossary and the entity model | ☐ |
| EM-36 to EM-39 | Every glossary entry carries a definition, other names, where the term comes from and a status; withdrawn terms keep their entries; statutory terms are reproduced and cited | ☐ |
| EM-40 to EM-44 | One register of business rules is named; every rule is written once with an identifier, short and free of its flow, carrying its terms, its authority, its effective date and its status; a rule that reads a setting names it and carries no value of it; withdrawn rules keep their entries; a rule nothing cites is reported | ☐ |
| EM-45 to EM-51 | Every record this system keeps says whether anybody else consumes it; every classification is made from this system's own position; every list a coded attribute names has one row carrying its classification, its issuer, where the issuer publishes it and the words it was derived from; every issuer named is a body and not a system; and all of it was written in the first pass | ☐ |
| EM-52, EM-53, EM-54 | Every attribute describes the record it is drawn on; no attribute name repeats that record's name; and every record is related to at least one other or carries the written reason it stands alone | ☐ |
| EM-55, EM-56 | One layout convention is stated and every generated picture follows it; and the form states which of its lines belong to the first pass, with the model reported as finished for that pass or outright | ☐ |
| The form | Every line of the five-part form, and every column of every row of the table of governed lists, has an answer or a written reason for having none | ☐ |

## Form

### 5.1 For each record

| line | rule |
|---|---|
| Name | EM-16 |
| Definition | EM-15 |
| Why it is a record | EM-11 |
| Identified how | EM-12 |
| Special kinds | EM-14 |
| Parts played | EM-13 |
| Attributes, each with its least and most | EM-17 |
| What the minimums mean | EM-18 |
| Attributes holding more than one value | EM-23 |
| Where each attribute belongs | EM-52 |
| Attribute names | EM-53 |
| Made-up identifiers | EM-25 |
| Coded attributes | EM-19, EM-47 |
| The governed lists used | EM-20, EM-47 |
| History kept | EM-21 |
| Coded values, as at | EM-21 |
| Uniqueness | EM-22 |
| Boundary | EM-2, EM-45, EM-48 to EM-50 |
| Groups it is read in | EM-3 |
| Facts deliberately recorded twice | EM-24 |
| Related to | EM-54 |

### 5.2 For each relationship

| line | rule |
|---|---|
| Name, reading from this end | EM-26 |
| Name, reading from the far end | EM-32 |
| Read back, in both directions | EM-32 |
| Degree | EM-17 |
| Optionality | EM-17 |
| If both ends are optional | EM-33 |
| Identifying or referring | EM-12 |
| Facts of its own | EM-27 |
| If many at both ends | EM-28 |
| Excluded by another relationship | EM-30 |
| On removal, replacement or correction | EM-31 |
| Loops back to the same record | EM-29 |

### 5.3 For the model as a whole

| line | rule |
|---|---|
| Level | EM-1 |
| What this model is of | — |
| Boundary statement | EM-2, EM-45 |
| Groups | EM-3 |
| Counts, stated and not judged | EM-3, EM-6 |
| The two clocks | EM-21 |
| Normal form | EM-24 |
| Extension rule | EM-4 |
| Notation | EM-9, EM-10 |
| Layout convention | EM-55 |
| The pictures | EM-7, EM-8 |
| The register beside the pictures | EM-7 |
| The table of governed lists | EM-47 to EM-51 |
| Written in the first pass | EM-51 |
| The two passes | EM-56 |
| Owner and change procedure | EM-5 |
| Review | EM-6 |
| The depth worked at | not settled |
| Open questions | — |

| column | rule |
|---|---|
| List | EM-47 |
| Classification | EM-2, EM-45, EM-46 |
| Issuer | EM-48, EM-50 |
| Where the issuer publishes it | EM-49, EM-50 |
| Source in the client's material | EM-50 |
| Consumers known | EM-45 |

### 5.4 For each glossary entry

| line | rule |
|---|---|
| Term | EM-34, EM-37 |
| Definition | EM-36 |
| Why it is not a record | EM-35 |
| Other names for it | EM-37 |
| Where the term comes from | EM-36, EM-39 |
| Drawn from legislation | EM-39 |
| Status | EM-36, EM-38 |
| Where it is used | EM-36 |

### 5.5 For each business rule

| line | rule |
|---|---|
| Identifier | EM-40 |
| Statement | EM-41 |
| Settings it reads | EM-42 |
| Terms it uses | EM-42 |
| What it constrains | EM-42 |
| Where its authority comes from | EM-42 |
| From when it takes effect | EM-42 |
| Status | EM-42, EM-43 |
| What cites it | EM-44 |

## Rules

| rule | words | program |
|---|---|---|
| EM-1 | The model declares its level, and nothing belonging | none |
| EM-2 | Every record says whether this system is the | none |
| EM-3 | The records are grouped into named groups small | none |
| EM-4 | A published model is extended by adding, never | none |
| EM-5 | The model has a named owner and a | none |
| EM-6 | Every rule the model is judged against declares | none |
| EM-7 | The picture carries what a person reading it | none |
| EM-8 | There is one model, and every picture is | none |
| EM-9 | A picture must not be used to assert | none |
| EM-10 | One notation is chosen for a model, stated, | none |
| EM-55 | One layout convention is stated for the model, | none |
| EM-56 | The form in part 5 is answered in | none |
| EM-11 | A record is a kind of thing that | none |
| EM-12 | Dependence is declared at both ends. | none |
| EM-13 | A part somebody plays is not a kind | none |
| EM-14 | Special kinds answer two separate questions and both | none |
| EM-15 | Every record and every attribute carries a written | none |
| EM-16 | A record's name is a singular noun phrase | none |
| EM-17 | Every attribute and every relationship end states the | none |
| EM-18 | The model states the least that must be | none |
| EM-19 | A coded attribute is a reference to a | none |
| EM-20 | A governed list is versioned, and its values | none |
| EM-21 | There are two clocks, not one — when | none |
| EM-22 | A fact that is true for a period | none |
| EM-23 | An attribute that would hold more than one | none |
| EM-24 | The model is held to third normal form, | none |
| EM-25 | An identifier the system makes up, with no | none |
| EM-52 | An attribute describes the record it is drawn | none |
| EM-53 | An attribute's name does not repeat the name | none |
| EM-54 | Every record is related to at least one | none |
| EM-26 | Every relationship is named, and the name is | none |
| EM-27 | A relationship that carries facts of its own | none |
| EM-28 | A many-to-many relationship is resolved into a record | none |
| EM-29 | A record related to itself states which relation | none |
| EM-30 | Where two relationships may not both be present, | none |
| EM-31 | What happens at the far end when a | none |
| EM-32 | Every relationship is named in both directions, so | none |
| EM-33 | A relationship optional at both ends is suspect | none |
| EM-34 | The model names one glossary, and one term | none |
| EM-35 | If the system keeps a record of it, | none |
| EM-36 | Every glossary entry carries the term, one definition, | none |
| EM-37 | A concept has one preferred term, and every | none |
| EM-38 | A term is versioned, and it is withdrawn | none |
| EM-39 | A term drawn from legislation is reproduced as | none |
| EM-40 | There is one register of business rules for | none |
| EM-41 | A rule is written short, self-contained, and free | none |
| EM-42 | Every entry carries the identifier, the statement, the | none |
| EM-43 | A rule is versioned, and it is withdrawn | none |
| EM-44 | A rule nothing cites is reported as a | none |
| EM-45 | A record this system is the authority for | none |
| EM-46 | A classification is made from the position of | none |
| EM-47 | Every governed list any coded attribute names has | none |
| EM-48 | A record or a list that is not | none |
| EM-49 | A record or a list that is not | none |
| EM-50 | Every classification, every issuer and every place of | none |
| EM-51 | The classification of every record and every list, | none |
