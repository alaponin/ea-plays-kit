---
standard: SDD-07
title: The Screens of a Use Case
edition: "1.3"
document: SDD-07_The_Screens_of_a_Use_Case_v1.3.md
sha256: f3602240be8516e29266fe0a86cca91448d4c14305f67379a10e1fc8ea3ae6be
produced_by: _working/2026-08-31_house_rebuild/build_house.js at 2026-09-29T09:30:53Z
converted_from: SDD-07_The_Screens_of_a_Use_Case_v1.3.docx sha256 edff1a9b30fa99a2f5737f572f477369bea31a3f2ea8de31254595c39c82f050 (sdd-kit carries its text as Markdown)
---

# SDD-07 · The Screens of a Use Case — the checklist

*Produced from the document named above by `_working/2026-09-28_the_checklists/extract_checklist.py`, as the last step of its build, and never edited by hand. Every line below is the document's own words, read from it, except the lines in italics, which are this program's.*

*Rules counted in the document: 32. The document states "Thirty-two rules, a record for each screen" (32).*

## Gate — the program's half

*The document states no part of its gate for a program to perform.*

## Gate — the person's half

### 12 The review

Run this before a screen set is baselined, and before anything is built from it. The owner of the set runs it with whoever will build from it and with the counterpart whose work the screens describe. A set passes only when every applicable line is satisfied. A line that is not satisfied is a finding with a named owner, and not an exception to be set aside.

The review has two halves. The first is what a program has already established before the meeting: twenty-seven numbered lines, read together and not discussed. Every rule that a program reads is enforced by at least one of them, and every line names the rules it enforces. The second half is what only a person can judge, and it is not the lesser half.

#### The twelve questions a person answers

|  | The question |
|---|---|
| One | Do the screens follow the steps, or the other way round? Was this set worked out by walking the use case, or by walking the entity model and finding a step for each screen afterwards? Was any step made into a screen because a screen was wanted, or were two steps run together because they happened to fit? |
| Two | Is every value that enters the organisation here genuinely unobtainable from a register this organisation already consumes — or does its justification restate what the value is for instead of answering the question? |
| Three | Is the walk-through doing work that the record should be doing, so that the person agreeing to it is agreeing to something the builder will not receive? |
| Four | Did anybody actually click through it? Was the walk-through opened and followed, from the first screen to each of its endings, by somebody who did not write it? |
| Five | Is any value shown that this person does not need in order to complete this step? |
| Six | Are these the words the business itself uses, in the sense the business uses them — or the model's words applied correctly to the wrong thing? |
| Seven | Where a step or a variation carries a written reason for needing no screen, is the reason true, or is it the reason a specifier reached for? |
| Eight | Is any screen carrying so many values that it is really two? And for every variation carried on a screen already in the set, did the flow really leave the person where the record says it did? |
| Nine | Is the set finished? No published test says when a set is finished. The answer this standard uses is that every line of section 11 has an answer or a written reason for having none. |
| Ten | Against each of the stakeholders' interests: is it visible to the actor who has to protect it? And is the sentence recorded against it a reading of these screens, or the use case's guarantee copied out again? |
| Eleven | Is the effect recorded against each cited rule the effect that rule actually has — or the effect the specifier assumed it had without opening the register? |
| Twelve | Where an entity the use case reads is recorded as not needed by this actor, is the reason true, or is it that nobody could think where to put it? |

#### What this review does not do

Every line that a program reads establishes a structural property: that something is named, recorded, resolved, bound or reached. None of them establishes that what is recorded is true. Whether the screens are the screens a person would want, whether a value's stated origin is the origin it really has, whether a reason given for needing no screen is honest — none of these is asked by any mechanical line, and every one of them decides whether a screen set is any good.

A screen set that passes the mechanical half has been shown to be well formed, and nothing more. A reviewer should read the result that way, and the standards for the use case model and for one use case state the same limit about their own reviews.

There is one further limit, and it belongs to this standard alone. There is no line about accessibility and no line about language, because this body of work carries no standard for either. A screen set can satisfy every line above and be unusable by a person who cannot see it, and unreadable by a person who works in the administration's second language. The only route by which either can enter is as a quality requirement in the catalogue, cited on the screen it binds — and only if the catalogue carries one.

What was built is not read by this review, which runs before anything is built. Once something has been built from the set, its owner answers for that reading: whether each screen was built as its record states is recorded against the screen, every difference is a finding with a named owner, and that record is what the standard for the method (SDD-01, section 15) reads as screens specified against screens built. By what act a built screen is set beside its record, this standard does not say.

## Form

### 5 What a screen records — The record header

| line | rule |
|---|---|
| Identifier | not stated |
| Name | not stated |
| Use cases | not stated |
| Primary actor | not stated |
| Entities | not stated |
| Requirements realised | not stated |
| Business rules cited | not stated |
| Quality requirements cited | not stated |
| Status and version | not stated |

### 11 What to write down

#### For each screen

| line | rule |
|---|---|
| The identifier, unique across the set, and the name — what the person is doing here, in the words the business uses. | not stated |
| The use cases this screen serves, each with its version, and against each of them the numbered steps and variations it serves. | not stated |
| For a variation: whether it is a variation of a screen already in the set or a screen of its own, and why; and what it carries — what the actor may do about the condition, or what still holds despite the failure. | not stated |
| The entities shown and, separately, the entities changed, by name only. | not stated |
| The requirements realised, the business rules cited, and the quality requirements cited, by identifier — or none, and none is an answer rather than an empty line. | not stated |
| For every value, where it came from, in one of the four ways; the authority, where it is consumed; the list, its owner, the strength of the binding and the clock that decides, where it is drawn from a governed list; that it is chosen and what tells the record apart, where it points at another record; and why it can be obtained no other way, where it enters the organisation here. | not stated |
| For every value, the least the screen demands and the most it admits, as two decisions — confirmed to be neither below the entity model's minimum nor mistaken for it. | not stated |
| For every rule cited, where it is cited and what its effect is at that place. No rule text. | not stated |
| Which act takes the person from this screen to which other screen, and which act raises which variation. | not stated |
| The status and the version. | not stated |

#### For the set as a whole

| line | rule |
|---|---|
| How the set was worked out, and from what. | not stated |
| The use case and the version of it the set was worked out from; and which screens, if any, are shared with another use case. | not stated |
| How many steps and variations there are, which of them are reached, and the written reason wherever one is not. | not stated |
| The two lists of entities, and what reaches each of them. | not stated |
| The requirements, and what reaches each of them. | not stated |
| The stakeholders' interests, with one sentence against each saying whether it is visible to the actor, together with who read them and when. | not stated |
| How the walk-through is produced from the record, by whom, and when it was last produced. | not stated |
| Which notation is used, and what that notation cannot say, with where each of those things is written instead. | not stated |
| The statement of what agreeing to the walk-through commits the parties to, and what it does not. | not stated |
| What a later version may change and what it may not, written before there is a later version. | not stated |
| Which screens are retired, and for each of them what replaced it or why nothing did. | not stated |
| Who owns the set, who may propose a change, and who decides. | not stated |
| The level of detail the set was worked at, in the specifier's own words, applied consistently across every screen. | not stated |
| The questions genuinely in dispute, each with a named owner and a date, and never closed by a silent default. | not stated |

## Rules

| rule | words | program |
|---|---|---|
| 1 | The screens are worked out by walking the | none |
| 2 | There is one screen set for each use | none |
| 3 | The screens follow the numbered steps of the | none |
| 4 | Every variation of the flow is either a | none |
| 5 | What a variation carries follows from its kind: | none |
| 6 | Every numbered step and every variation is reached | none |
| 7 | Every entity the use case declares is reached | none |
| 8 | Every requirement the use case realises reaches at | none |
| 9 | The set is read once, by a person, | none |
| 10 | The set is held as versioned text beside | none |
| 11 | Every screen carries the record header, and every | none |
| 12 | A screen names only what its use case | none |
| 13 | A screen names entities and attributes, and carries | none |
| 14 | A screen cites the quality requirements that bind | none |
| 15 | Every value declares exactly one of the four | none |
| 16 | A consumed value names the authority it is | none |
| 17 | A reference to another record is chosen from | none |
| 18 | A value drawn from a governed list is | none |
| 19 | A value that enters the organisation at this | none |
| 20 | The screen states the least it demands of | none |
| 21 | A screen never shows a value that a | none |
| 22 | A cited rule appears on a screen as | none |
| 23 | There is one record, and the walk-through is | none |
| 24 | Every screen of the set is a page | none |
| 25 | The walk-through makes each value's origin, what the | none |
| 26 | A property whose only reader is the walk-through | none |
| 27 | One notation is declared and never mixed with | none |
| 28 | Every screen and every value carries a stable | none |
| 29 | A screen is superseded and never deleted, and | none |
| 30 | The set has a named owner and a | none |
| 31 | Every rule of this standard declares which of | none |
| 32 | Every rule is answered on a numbered line, | none |
