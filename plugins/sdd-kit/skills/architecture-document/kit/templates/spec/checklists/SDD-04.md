---
standard: SDD-04
title: The Shared Registers
edition: "1.0"
document: SDD-04_The_Shared_Registers_v1.0.md
sha256: d167b5047937ff382d59d5297ed8c2b158e4e61e132c8b7cd9092862ee3592ef
produced_by: _working/2026-08-31_groundwork_standard/docx_build/build_gw01.js at 2026-09-29T22:04:39Z
converted_from: SDD-04_The_Shared_Registers_v1.0.docx sha256 810db7aac3f9ffffe935d550462864fdc4c48ae42a6e71062bc855dd0bcaf435 (sdd-kit carries its text as Markdown)
---

# SDD-04 · The Shared Registers — the checklist

*Produced from the document named above by `_working/2026-09-28_the_checklists/extract_checklist.py`, as the last step of its build, and never edited by hand. Every line below is the document's own words, read from it, except the lines in italics, which are this program's.*

*Rules counted in the document: 47. The document states the range IOS-1 to IOS-47, on the first page (47).*

## Gate — the program's half

### 6. The review gate — the words before its first subsection

Split in two, because the two halves fail differently.

### 6.1 What a program will refuse — once the checks exist

> None of the checks below is built. They are printed so that an analyst knows what will be read mechanically, and so that whoever builds them knows what to build. No result of any kind may be reported from this section until they exist. This is the house method's one governing rule on checks and SDD-03 §6.1's discipline, adopted rather than restated.

| Id | Reads | Fails when | Rule |
|---|---|---|---|
| IOS-C1 | every record's grain line | absent, or not of the form one row per ___ | IOS-1 |
| IOS-C2 | every record | no duplicate-rule answer, or an answer for the key-present path only | IOS-2 |
| IOS-C3 | every record with a merge answer | no statement of what re-points, or no statement of what becomes of the retired identifier | IOS-3 |
| IOS-C4 | every record with a merge answer and no split answer | no finding recorded for the missing direction | IOS-4 |
| IOS-C5 | every identifier | no issuer named | IOS-5 |
| IOS-C6 | every fact | no writer named | IOS-6 |
| IOS-C7 | every fact | neither stored nor worked out afresh | IOS-7 |
| IOS-C8 | every fact marked worked out afresh | it names a computation absent from the catalogue at §4F. This is the one check in this standard whose exact shape is already proved to work, because RCP-1 does it for computations today | IOS-7 |
| IOS-C9 | every consumed fact | no consumption pattern, a pattern outside the closed set, or no unreachable-behaviour | IOS-8 |
| IOS-C10 | every copy held | no freezing act, or no moment | IOS-9 |
| IOS-C11 | every record with states | zero or more than one initial state; a state with no inbound move; a non-terminal state with no outbound move | IOS-10, IOS-11 |
| IOS-C12 | every move | no trigger, or a user trigger on a move the register marks system-only | IOS-12 |
| IOS-C13 | every record | a state named in the state set that the register also declares a computation | IOS-13 |
| IOS-C14 | the register heading | no source, no owner, or no change procedure | IOS-15, IOS-16 |
| IOS-C15 | every stated count | recomputing it from the register's own tables gives a different number and no non-reproduction is recorded | IOS-17 |
| IOS-C16 | every column | no entry has a value in it | IOS-18 |
| IOS-C17 | the counts of Part 2 | nothing. This one reports and never fails | IOS-17 |
| IOS-C18 | every event entry | no record named, or no change named, or no statement of what makes two the same | IOS-20, IOS-21 |
| IOS-C19 | every event marked raised by this system | the fact it announces has a writer other than this system | IOS-23 |
| IOS-C20 | every computation named by a fact | no entry in the catalogue | IOS-24 |
| IOS-C21 | every computation entry | no fact names it | IOS-24 |
| IOS-C22 | every computation entry | no inputs listed, or a rule written out instead of cited by identifier | IOS-25, IOS-27 |
| IOS-C23 | the catalogue of computations | two entries producing the same fact | IOS-26 |
| IOS-C24 | every governed list bound by an attribute | no entry in the assignment | IOS-28 |
| IOS-C25 | every list entry marked shared | no owning authority named | IOS-28 |
| IOS-C26 | every list entry | no retirement answer | IOS-31 |
| IOS-C27 | every binding at the strongest strength | the list it binds has no named owner | IOS-32 |
| IOS-C28 | every list entry | nothing. It reports the bindings and their strengths so that two strengths on one list are visible | IOS-30 |
| IOS-C29 | every list entry | no identifier and no recorded ask; or no edition in use | IOS-28 |
| IOS-C30 | every consumed list | no consumption pattern, or no behaviour when the authority is unreachable | IOS-29 |
| IOS-C31 | every list entry | no steward and no nobody yet; or no closed-or-extensible answer | IOS-32, IOS-34 |
| IOS-C32 | every selection entry | no list named, or no definer named | IOS-33 |
| IOS-C33 | every setting a use case, screen, rule or computation names | no entry in the catalogue of settings | IOS-36 |
| IOS-C34 | every entry of the catalogue of settings | nothing names it. This one reports and never fails | IOS-36 |
| IOS-C35 | every setting entry | no kind; or a key naming a list with no entry in Part 5 | IOS-37 |
| IOS-C36 | every setting entry | no default and no placeholder; or a placeholder with no owner | IOS-38 |
| IOS-C37 | every setting entry | no class, or a class Part 7 does not define | IOS-40 |
| IOS-C38 | every setting entry | no path; or a path naming a use case the model does not carry | IOS-41 |
| IOS-C39 | every setting that selects from a list | the value is not a member of the list's entry, or no admitting fact is named | IOS-45 |
| IOS-C40 | every switch | no built, on or lawful answer | IOS-46 |
| IOS-C41 | every setting naming a constraint | the other setting's entry does not name it back | IOS-47 |
| IOS-C42 | every frozen value drawn from a list or a setting | no list identifier and edition, or no setting name and version | IOS-9 |

What actually runs today, stated so that nobody reads the table above as a status report. Nothing in it runs. lint_ucd.py shape-checks transition tokens and refuses a malformed one; it resolves no entity name, transition or grain against this register, and says so in its own comments. check_foundation.py reads entities in the other direction and reports rather than refusing by default — its reporting mode exits 0, and --fail-on-findings restores a refusing exit, so it is a reporting check that can be made to refuse and is not run that way. Of the forty-two checks above, one — IOS-C8 — has a shape already proved to work elsewhere, and forty-one have not been attempted. Eleven of the forty-two are new in version 0.2 and fourteen in version 0.3, and none of those has been attempted either. The count of built checks is still nought, and adding twenty-five specifications to it changed nothing about what runs.

And a condition the checks cannot be built without, which is not this standard's to meet. A check can resolve a name only where the register publishes a named set in one shape a parser can read without knowing the document. The reference programme's three data-model views do not share a declaration shape, and that is the named obstacle. This standard requires the register to publish its sets (IOS-15) and does not specify the publication format, which is a gap in this standard and is recorded as one at §8.

## Gate — the person's half

### 6.2 What only a person can judge

No program will ever decide these, and a review that skips them has checked that the boxes are full rather than that the answers are right.

- Whether the grain sentence is the grain the business would recognise, or the grain the table happens to have.
- Whether the duplicate rule is the rule, as opposed to a rule that catches the cases somebody thought of.
- Whether the threshold on the key-absent path is set where a false match costs more than a missed one, or the other way round, and whether anybody decided that on purpose.
- Whether the named writer is the real writer, or the module that noticed first.
- Whether a fact called stored should be worked out afresh, and whether a stored derivation's recompute trigger is one that will actually fire.
- Whether a state set is the business's lifecycle or one project's stages.
- Whether an inherited spine was inherited or copied.
- Whether a finding recorded against another document is a real gap or this analyst declining to decide.
- Whether an event is one happening or two, in the case the rule does not reach: a correction issued after the fact, which may be a second event or an amendment of the first.
- Whether a computation produces the figure the business means by that word, as opposed to a defensible figure with the same name.
- Whether a list is really shared, or is one this system happens to have given to somebody else once.
- Whether a binding is at the strength somebody chose, or at the strength the first attribute happened to use.
- Whether a selection is the module's to define, or a slice somebody else already publishes under a name.
- Whether a figure inside a rule, a trigger or a screen is a setting at all — could it lawfully be otherwise tomorrow by this administration's act, would the statement stay true, and is what changes a value and not a meaning — or a fact of law, a decision, or a member of a list.
- Whether a class of change was chosen for a setting or defaulted to the one nearest to hand; and whether the classes a module defined are its own or one product's administration screens under other names.
- Whether a switch's barred rests on legal advice received or on a reading of the provision by whoever filled the entry.
- Whether a setting's default is an answer with a ground or a guess that was not marked as one.
- Whether the register is finished, for which no published test exists, and the answer is the entity model standard's: every line answered or carrying a written reason.

## Form

### 5.1 Part 1 — once for each record

| line | rule |
|---|---|
| Grain | IOS-1 |
| Two rows are the same when — key present | IOS-2 |
| Two rows are the same when — key absent or wrong | IOS-2 |
| Grade at which a match may be acted on without a person | IOS-19 |
| Merge | IOS-3 |
| Split | IOS-4 |
| Other identifiers | IOS-5 |
| Writer | IOS-6 |
| Facts written elsewhere | IOS-6 |
| Stored or worked out | IOS-7 |
| Consumption pattern | IOS-8 |
| Copies held | IOS-9 |
| Deletion | IOS-9 |
| States | IOS-10 |
| Moves | IOS-11, IOS-12 |
| Moves no person may fire | IOS-12 |
| States that are computations | IOS-13 |
| States inherited | IOS-14 |
| Created by | IOS-6 |
| Open questions | — |

### 5.2 Part 2 — once for the register as a whole

| line | rule |
|---|---|
| Generated from | IOS-15 |
| Owner and change procedure | IOS-16 |
| Counts, stated and not judged | IOS-17 |
| Columns never filled | IOS-18 |
| Counts that did not reproduce | IOS-17 |
| Asks and answers | IOS-16 |
| Level | — |
| Depth | — |
| What refuses | — |

### 5.3 Part 3 — once for each event

| line | rule |
|---|---|
| Name | IOS-20 |
| Raised or consumed | IOS-20, IOS-23 |
| The record and the change | IOS-21 |
| What makes two the same | IOS-21 |
| What it carries | IOS-22 |
| Who consumes it | IOS-22 |
| Delivery | IOS-22 |
| Status | IOS-15 to IOS-18 |

### 5.4 Part 4 — once for each computation

| line | rule |
|---|---|
| Identifier | IOS-24 |
| What it produces | IOS-25 |
| Inputs | IOS-25 |
| Settings it reads | IOS-25 |
| Rules it applies | IOS-27 |
| When it is evaluated | IOS-25 |
| Produced anywhere else | IOS-26 |

### 5.5 Part 5 — once for each governed list, and once for each named selection of one

| line | rule |
|---|---|
| The list | IOS-28 |
| Classification and issuer | IOS-28 |
| Selection of | IOS-33 |
| Consumed or copied | IOS-29 |
| Edition | IOS-28 |
| Closed or extensible | IOS-34 |
| Bindings and their strength | IOS-30 |
| Retirement | IOS-31 |
| Steward | IOS-32 |
| What else this name carries | IOS-35 |

### 5.6 Part 6 — once for each setting

| line | rule |
|---|---|
| Name | IOS-36 |
| Readers | IOS-36 |
| Kind of value | IOS-37 |
| Unit and bounds | IOS-37 |
| Key | IOS-37 |
| Default | IOS-38 |
| Ground | IOS-38 |
| Authority and reach | IOS-39 |
| Provisional | IOS-39 |
| Class of change | IOS-40 |
| Path | IOS-41 |
| Whose | IOS-42 |
| Defined by · set by | IOS-42 |
| Dated | IOS-43 |
| Record of change | IOS-43 |
| Work in flight | IOS-44 |
| Selects from | IOS-45 |
| Switch | IOS-46 |
| Constrained by | IOS-47 |
| Open questions | — |

### 5.7 Part 7 — once for each class of change

| line | rule |
|---|---|
| Class | IOS-40 |
| Occasion | IOS-40 |
| Who may change | IOS-40 |
| Who seconds | IOS-40 |
| What is tried before | IOS-40 |
| Settings in the class | IOS-40, IOS-15 |

## Rules

| rule | words | program |
|---|---|---|
| IOS-1 | Every record states its grain as one sentence | none |
| IOS-2 | Every record declares its duplicate rule: the attribute | none |
| IOS-3 | A record whose rows may be merged declares | none |
| IOS-4 | A record that may be split declares the | none |
| IOS-5 | Where one thing is identified by more than | none |
| IOS-19 | A proposed match carries a grade. A match | none |
| IOS-6 | Every fact has exactly one writer, named, and | none |
| IOS-7 | Every fact declares whether it is stored or | none |
| IOS-8 | A fact this system consumes names the authority | none |
| IOS-9 | A fact this system does not write may | none |
| IOS-10 | A record that has states declares them as | none |
| IOS-11 | Every move is fully declared — from, to, | none |
| IOS-12 | A move no person may fire declares what | none |
| IOS-13 | A state worked out from other facts rather | none |
| IOS-14 | The register states, per record, which states are | none |
| IOS-15 | The register is a view generated from a | none |
| IOS-16 | The register names its owner and the written | none |
| IOS-17 | A count is measured at the moment it | none |
| IOS-18 | A column no entry has ever filled is | none |
| IOS-20 | Every event this module raises, and every event | none |
| IOS-21 | The entry says what makes two events the | none |
| IOS-22 | Every entry carries: the name · the record | none |
| IOS-23 | An event about a fact this system does | none |
| IOS-24 | *Every fact declared worked out afresh under IOS-7 | none |
| IOS-25 | Every entry carries: what it produces · every | none |
| IOS-26 | One figure has one implementation. Where the same | none |
| IOS-27 | A computation that applies a business rule cites | none |
| IOS-28 | Every governed list any attribute points at under | none |
| IOS-29 | A list this system does not own is | none |
| IOS-30 | The entry states, in one place, the binding | none |
| IOS-31 | The entry states what happens to rows already | none |
| IOS-32 | A list with no named issuer is a | none |
| IOS-33 | A named selection of a governed list has | none |
| IOS-34 | The entry states whether the list is closed | none |
| IOS-35 | A governed list is a set of meanings | none |
| IOS-36 | Every setting the module's behaviour turns on has | none |
| IOS-37 | The entry states what kind of value the | none |
| IOS-38 | The entry states the default and the ground | none |
| IOS-39 | The entry states where the authority to choose | none |
| IOS-40 | Every setting names the class of change its | none |
| IOS-41 | The entry states by what path the value | none |
| IOS-42 | The entry states whose the setting is — | none |
| IOS-43 | A change to a setting is a new | none |
| IOS-44 | The entry states what becomes of work already | none |
| IOS-45 | A setting whose value selects from a governed | none |
| IOS-46 | A switch's entry states whether the capability behind | none |
| IOS-47 | Where two settings constrain each other, the entry | none |
