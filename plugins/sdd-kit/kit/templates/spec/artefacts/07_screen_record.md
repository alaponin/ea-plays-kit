<!--
standard: SDD-07
title: The Screens of a Use Case
edition: "1.3"
document: SDD-07_The_Screens_of_a_Use_Case_v1.3.md
sha256: f3602240be8516e29266fe0a86cca91448d4c14305f67379a10e1fc8ea3ae6be
produced_by: _working/2026-08-31_house_rebuild/build_house.js at 2026-09-29T09:30:53Z
converted_from: SDD-07_The_Screens_of_a_Use_Case_v1.3.docx sha256 edff1a9b30fa99a2f5737f572f477369bea31a3f2ea8de31254595c39c82f050 (sdd-kit carries its text as Markdown)
-->

# The screens of a use case

*Written to SDD-07, The Screens of a Use Case, edition 1.3. Produced from the standard by `_working/2026-09-28_the_checklists/extract_checklist.py`, as the last step of its build; a copy of it is filled, and this file is never edited by hand. The quoted lines are the standard's own words.*

## 5 What a screen records — The record header

> Every screen carries a header, and every value in that header is stated once, in the header, and never again in the prose below it.

| The line | What is recorded | Rule | Answer |
|---|---|---|---|
| Identifier | The stable reference by which the set knows this screen. | not stated |  |
| Name | What the person is doing here, in the words the business uses, from the actor's point of view. | not stated |  |
| Use cases | Every use case this screen serves, each with its version, and against each of them the numbered steps and variations of that use case which this screen serves. Usually there is one. | not stated |  |
| Primary actor | The actor of the use case. It is not a separate decision. Where a screen serves two use cases, both name the same actor, or the screen is really two screens, because a screen is what one person has in front of them. | not stated |  |
| Entities | The entities of the entity model this screen shows, and separately those it changes, by name only. | not stated |  |
| Requirements realised | The identifiers of the requirements this screen serves, which are a subset of those the use case declares. | not stated |  |
| Business rules cited | The identifiers of the registered rules that govern this screen, which are a subset of those the use case cites. | not stated |  |
| Quality requirements cited | The identifiers of the quality requirements that bind what a person sees here — or none, and none is an answer rather than an empty line. | not stated |  |
| Status and version | Draft, reviewed or baselined, and the version. Those three words are the ones the standards beneath this one use, and no fourth word is used. | not stated |  |

## 11 What to write down

> This is the centre of the standard, and the promise it makes is that two specifiers answer the same questions. These are the questions. A screen set is finished when every line below has an answer or carries a written reason for having none.

### For each screen

| Line | Rule | Answer |
|---|---|---|
| The identifier, unique across the set, and the name — what the person is doing here, in the words the business uses. | not stated |  |
| The use cases this screen serves, each with its version, and against each of them the numbered steps and variations it serves. | not stated |  |
| For a variation: whether it is a variation of a screen already in the set or a screen of its own, and why; and what it carries — what the actor may do about the condition, or what still holds despite the failure. | not stated |  |
| The entities shown and, separately, the entities changed, by name only. | not stated |  |
| The requirements realised, the business rules cited, and the quality requirements cited, by identifier — or none, and none is an answer rather than an empty line. | not stated |  |
| For every value, where it came from, in one of the four ways; the authority, where it is consumed; the list, its owner, the strength of the binding and the clock that decides, where it is drawn from a governed list; that it is chosen and what tells the record apart, where it points at another record; and why it can be obtained no other way, where it enters the organisation here. | not stated |  |
| For every value, the least the screen demands and the most it admits, as two decisions — confirmed to be neither below the entity model's minimum nor mistaken for it. | not stated |  |
| For every rule cited, where it is cited and what its effect is at that place. No rule text. | not stated |  |
| Which act takes the person from this screen to which other screen, and which act raises which variation. | not stated |  |
| The status and the version. | not stated |  |

> A screen that answers only the name line has not been specified. It has been named.

### For the set as a whole

> This is the part filled in once, and it is the part most often not filled in at all.

| Line | Rule | Answer |
|---|---|---|
| How the set was worked out, and from what. | not stated |  |
| The use case and the version of it the set was worked out from; and which screens, if any, are shared with another use case. | not stated |  |
| How many steps and variations there are, which of them are reached, and the written reason wherever one is not. | not stated |  |
| The two lists of entities, and what reaches each of them. | not stated |  |
| The requirements, and what reaches each of them. | not stated |  |
| The stakeholders' interests, with one sentence against each saying whether it is visible to the actor, together with who read them and when. | not stated |  |
| How the walk-through is produced from the record, by whom, and when it was last produced. | not stated |  |
| Which notation is used, and what that notation cannot say, with where each of those things is written instead. | not stated |  |
| The statement of what agreeing to the walk-through commits the parties to, and what it does not. | not stated |  |
| What a later version may change and what it may not, written before there is a later version. | not stated |  |
| Which screens are retired, and for each of them what replaced it or why nothing did. | not stated |  |
| Who owns the set, who may propose a change, and who decides. | not stated |  |
| The level of detail the set was worked at, in the specifier's own words, applied consistently across every screen. | not stated |  |
| The questions genuinely in dispute, each with a named owner and a date, and never closed by a silent default. | not stated |  |
