<!--
standard: SDD-04
title: The Shared Registers
edition: "1.0"
document: SDD-04_The_Shared_Registers_v1.0.md
sha256: d167b5047937ff382d59d5297ed8c2b158e4e61e132c8b7cd9092862ee3592ef
produced_by: _working/2026-08-31_groundwork_standard/docx_build/build_gw01.js at 2026-09-29T22:04:39Z
converted_from: SDD-04_The_Shared_Registers_v1.0.docx sha256 810db7aac3f9ffffe935d550462864fdc4c48ae42a6e71062bc855dd0bcaf435 (sdd-kit carries its text as Markdown)
-->

# The shared registers — identity, ownership and state, and the catalogues of events, computations, shared code lists and settings

*Written to SDD-04, The Shared Registers, edition 1.0. Produced from the standard by `_working/2026-09-28_the_checklists/extract_checklist.py`, as the last step of its build; a copy of it is filled, and this file is never edited by hand. The quoted lines are the standard's own words.*

## 5.1 Part 1 — once for each record

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Grain | One row per ___ | IOS-1 |  |
| Two rows are the same when — key present | The attribute set | IOS-2 |  |
| Two rows are the same when — key absent or wrong | The attribute set and the threshold; or duplicates cannot arise, with the reason | IOS-2 |  |
| Grade at which a match may be acted on without a person | certain only; or the declared exception, with who approved it | IOS-19 |  |
| Merge | Not possible; or who may · what re-points · what happens to the surviving identifier · what happens to the retired one · what record is made | IOS-3 |  |
| Split | Not possible; or the same five answers. If one direction only, the finding and its owner | IOS-4 |  |
| Other identifiers | None; or each as issuer + value, resolved through ___ , primary is ___ | IOS-5 |  |
| Writer | This system, naming the act that writes; or ___ , read-only | IOS-6 |  |
| Facts written elsewhere | The list, each with its authority | IOS-6 |  |
| Stored or worked out | Per fact: stored; or worked out by ___ . If stored and derivable: what recomputes it, and when | IOS-7 |  |
| Consumption pattern | Per consumed fact: one of the closed set, and the behaviour when the authority is unreachable | IOS-8 |  |
| Copies held | None; or each: frozen by ___ , at ___ | IOS-9 |  |
| Deletion | Never; or the named authority under which a row may be physically deleted, and where the deletion is recorded | IOS-9 |  |
| States | None; or the closed set, the initial one, every terminal one marked — and where the set is declared | IOS-10 |  |
| Moves | Per move: from · to · fired by · who may | IOS-11, IOS-12 |  |
| Moves no person may fire | None; or each, with what fires it instead | IOS-12 |  |
| States that are computations | None; or each, naming its computation | IOS-13 |  |
| States inherited | None; or from ___ , and which are this module's own | IOS-14 |  |
| Created by | The use cases that create a row, and what distinguishes their contexts | IOS-6 |  |
| Open questions | Each with a named owner and a date | — |  |

## 5.2 Part 2 — once for the register as a whole

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Generated from | The named source documents | IOS-15 |  |
| Owner and change procedure | Who owns it · who may propose · who decides | IOS-16 |  |
| Counts, stated and not judged | How many records · how many with no writer declared · how many with states · how many with no duplicate rule · how many with no grain sentence. Each with the file it was counted on and the moment it was counted. No threshold is set on any of them and none may be inferred | IOS-17 |  |
| Columns never filled | The list, each as a finding with an owner | IOS-18 |  |
| Counts that did not reproduce | Each, with both figures and neither reconciled | IOS-17 |  |
| Asks and answers | Every request made of an issuer, of another register's owner or of the client about an entry: what was asked, of whom, when, and what came back — or no answer yet | IOS-16 |  |
| Level | Which of the entity model's three levels this register is written for | — |  |
| Depth | The detail worked at, in the analyst's own words, applied consistently | — |  |
| What refuses | Which lines a program reads, and the plain statement that it does not read them yet | — |  |

## 5.3 Part 3 — once for each event

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Name | The happening, named for what happened and not for what reacts to it | IOS-20 |  |
| Raised or consumed | Raised by this system; or consumed from ___ | IOS-20, IOS-23 |  |
| The record and the change | Which record, and which state move or fact change constitutes the event | IOS-21 |  |
| What makes two the same | The record · the change · the moment stamped. A redelivery is not a second event | IOS-21 |  |
| What it carries | Every field of the payload, by record and attribute | IOS-22 |  |
| Who consumes it | The named consumers; or none known | IOS-22 |  |
| Delivery | Guaranteed; or best effort — and what a consumer does when it is missed | IOS-22 |  |
| Status | Proposed; in use; withdrawn — and if withdrawn, the date and the consumers told | IOS-15 to IOS-18 |  |

## 5.4 Part 4 — once for each computation

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Identifier | The name every fact marked worked out afresh cites | IOS-24 |  |
| What it produces | The fact, by record and attribute | IOS-25 |  |
| Inputs | Every input, by record and attribute, including the ones drawn from another system | IOS-25 |  |
| Settings it reads | None; or each, by the name its entry in Part 6 carries. Never the value | IOS-25 |  |
| Rules it applies | The identifiers of the business rules, from the register SDD-03 EM-40 governs. Never the rule text | IOS-27 |  |
| When it is evaluated | On read; on a named event; on a schedule — and if stored as well as derivable, what recomputes it, under IOS-7 | IOS-25 |  |
| Produced anywhere else | Nowhere; or ___ , recorded as a finding against this catalogue | IOS-26 |  |

## 5.5 Part 5 — once for each governed list, and once for each named selection of one

> A selection's entry carries the Selection of line and the Bindings and their strength line, and cites the list's entry for everything else.

| Line | What to write | Rule | Answer |
|---|---|---|---|
| The list | Its name as the entity model's table of governed lists names it, and the identifier its issuer gives it — or not yet numbered, with the ask recorded in Part 2 | IOS-28 |  |
| Classification and issuer | Cited from the list's row in the entity model (SDD-03 EM-46 to EM-48), and not restated here. Shared, owned by ___ was written here until version 0.2 | IOS-28 |  |
| Selection of | Not a selection; or the list this entry selects from, who defines the selection, and the members it selects or the fact that selects them | IOS-33 |  |
| Consumed or copied | Consumed live from ___ , by the pattern ___ from IOS-8's closed set, and what the module does when the authority is unreachable, the list is stale or a value is missing; or copied, with the act that froze it and the moment, under IOS-9 | IOS-29 |  |
| Edition | How the list is versioned, which edition is in use here, and where the edition in use is recorded | IOS-28 |  |
| Closed or extensible | Closed by statute, citing the instrument; closed by its issuer; or extensible — by whom, and by what path a member is proposed | IOS-34 |  |
| Bindings and their strength | Every attribute pointing at this list or this selection, each with its strength: must use · must use where it covers the case · recommended · illustrative. Two strengths on one list is not an error and is not a silence either | IOS-30 |  |
| Retirement | Rows keep the value and it stays readable; or rows are migrated under ___ , recorded at ___ ; or a value may not be retired while any row carries it. And the date of every retirement | IOS-31 |  |
| Steward | The person or unit here who answers for the list; or nobody yet, which is a finding with an owner of its own. The issuer is on the list's row in the entity model and is not repeated, and an unknown issuer forbids the strongest binding | IOS-32 |  |
| What else this name carries | Nothing; or the value this module sets under the same word — rates keyed by these codes, boundaries keyed by these bands — named as a setting with its entry in Part 6, and whose it is | IOS-35 |  |

## 5.6 Part 6 — once for each setting

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Name | The one name every reader cites, unique across the module's registers. Never the name of a list, a rule, a record or a term | IOS-36 |  |
| Readers | Every use case, screen, rule and computation that reads it, produced from their own declarations; none is a finding with an owner | IOS-36 |  |
| Kind of value | A switch; a choice from ___ (a named set, or a governed list with its entry in Part 5); a quantity; a role; a period | IOS-37 |  |
| Unit and bounds | The unit, and the least and the most the value may be — or not applicable, for a switch or a role | IOS-37 |  |
| Key | One value for the installation; or one per member of ___ , a governed list; or one per class of ___ | IOS-37 |  |
| Default | The value in force until the administration changes it; or a placeholder, marked as one | IOS-38 |  |
| Ground | Why that default: the client's words, a ruling, an operational reason — or, for a placeholder, the owner and the occasion on which it will be filled | IOS-38 |  |
| Authority and reach | A statute with its citation; a published policy; or this administration's decision with the ruling — and the range the law allows and the direction the value may move | IOS-39 |  |
| Provisional | No; or yes, on the question ___ , owned by ___ , and what the entry becomes if the answer is no | IOS-39 |  |
| Class of change | The class, as Part 7 names it | IOS-40 |  |
| Path | Through ___ , a use case of this model; at installation; or not without a change to the build, in which case this is a decision and not an entry | IOS-41 |  |
| Whose | This module's own; consumed from ___ , by the crossing ___ of SDD-08; or must not be held here | IOS-42 |  |
| Defined by · set by | The same party; or the party who defines it ___ and the party who sets it ___ | IOS-42 |  |
| Dated | That a change is a new version with an effective date, and where the value in force at any moment is read back from | IOS-43 |  |
| Record of change | Where the record is kept — an event of Part 3 or a record of the entity model, named — and that it carries who, from what to what, when, from when, on whose second name, on what ground | IOS-43 |  |
| Work in flight | Keeps the value it was done under; re-evaluated under ___ , with what the change would touch enumerated first; or the change is refused while ___ depends on it | IOS-44 |  |
| Selects from | Not from a list; or the list ___ , with its entry in Part 5, and the recorded fact on a member that admits it ___ | IOS-45 |  |
| Switch | Not a switch; or built (yes / no) · on here (yes / no) · lawful (established · unestablished, owned by ___ · barred), and where off: why, what turns it on, and which use cases run only when it is on | IOS-46 |  |
| Constrained by | Nothing; or the setting ___ , and how | IOS-47 |  |
| Open questions | Each with a named owner and a date | — |  |

## 5.7 Part 7 — once for each class of change

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Class | Its name, as the entries of Part 6 cite it | IOS-40 |  |
| Occasion | When changes of this class are made: on a policy decision; on legal advice received; on an operational need; on a cycle | IOS-40 |  |
| Who may change | The actor of the use case model who makes the change | IOS-40 |  |
| Who seconds | Nobody; or the actor whose second name a change of this class carries | IOS-40 |  |
| What is tried before | What is done before a change of this class takes effect: the affected work enumerated; the value tried outside production; nothing | IOS-40 |  |
| Settings in the class | Produced from Part 6, never kept here | IOS-40, IOS-15 |  |
