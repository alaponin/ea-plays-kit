# SDD-06 · One System Use Case

*This copy is carried by sdd-kit, the SDD method's skills for the service design course. It keeps the edition stated below; where the edition drew an example from the method's author's own client work, this copy carries an example set in Progressa in its place and says so where it does.*

*One goal, written down in full: the story, every way it can be reached, and every way it can fail*

*AN INTERNAL STANDARD  ·  VERSION 1.2  ·  29 SEPTEMBER 2026  ·  IN FORCE*

*Twenty-one rules, a template written out in full, and a review gate in two halves.*

Field | Value
--- | ---
Document | SDD-06 · One System Use Case. One goal, written out in full: the story, the data, and what happens when things fail. It carried no code of its own, and was the file UC_definition_standard_v.1.0.docx, until the edition of 28 August 2026.
Version and standing | Version 1.2 · 29 September 2026 · in force. It supersedes version 1.1 of 22 September 2026, which is kept in x_archive/. What changed: a section 13 was added, what a use case owes the application model: two tables, from each thing a use case written out in full carries and from each thing the model of a goal reads from the documents settled once for the whole system, to the section of SDD-09 it lands in, saying whether the landing is mechanical or a judgement and what is written down when it cannot land. The line of this page that says who writes the document it governs now reads as the standard for the method reads in its figure 2 (SDD-01, section 4); until this edition it named the analyst. No rule was added, removed or renumbered. A claim of conformance made against version 1.1 remains a claim against version 1.1. An internal standard of FiscalAdmin OÜ, owned and approved by Aare Lapõnin, for the work of FiscalAdmin OÜ.
Who writes the document it governs | An assistant writes it; a person rules on it. One document for each goal the model decides to write out.
Who reads it | The reviewer who decides whether it may be built from, and the tester who derives the acceptance criteria.
When it is written | After the use case model, and before the screens of that goal.
Rules | U1 to U21.
What it does not cover | Section 1 names each boundary and where the subject belongs instead. What a person sees is covered by SDD-07.
Author | FiscalAdmin OÜ · Aare Lapõnin

---

Contents

1  What this standard is for

2  The same ideas, as they are named elsewhere

3  Choosing the form, and the record the use case carries

4  Writing the flows

5  What may and may not appear inside a use case

6  Deciding that it is ready

7  The template, written out in full

8  The review

9  The ways use cases go wrong

10  A worked example

11  The questions this standard does not answer

12  Where these rules come from

13  What it owes the application model

Figures

Figure 1 — What one use case is written from, and what is built from it.

Figure 2 — The three forms a use case may take, and who chooses between them.

Figure 3 — An extension leaves the main success scenario at a numbered step, and ends in one of three ways.

Figure 4 — The two parts of a use case written out in full, and who reads each.

Figure 5 — The two halves of the review, and the one decision they lead to.

## 1  What this standard is for

### What a use case specification is

A use case specification is one goal, written down. It says what one actor wants the system to do for them, every way that goal can be reached, and every way it can fail on the road there. One use case, one document. This standard says how to write it, how to review it, and how to tell when it is finished.

Everything in this standard is done once, for one use case. Nothing here is done across the system as a whole. Where a rule below rests on a decision that was taken across the whole system, it says where that decision was taken, and then stops. The standard that governs the use case model carries those decisions; this one carries the writing.

### What you need beside you before you start

This standard does not stand on its own, and it is not written as though it did. The words it uses, the principles behind it and the levels it refers to are set out once, in the standard that governs the use case model. They are not repeated here. A rule written in two places is a rule that will come, quietly, to say two different things.

Four things from that standard need to be in front of you before the rules below mean very much.

- The vocabulary. What a use case is, what a scenario is, what a slice is; what an actor is, and how an actor differs from a stakeholder. Every one of those words carries weight in the rules below. This standard uses them and does not gloss them.
- The principles. Eight of them. They stand behind both sets of rules, the model's and this one's, and they are what to return to when a rule seems not to fit the situation in front of you.
- The three levels of goal — summary, user goal and subfunction. This standard requires every use case to state which of the three it sits at. It does not tell you what the three are, or where the main body of the model should sit.
- The record header. The fields the model requires every use case to carry. That list is decided in the model's own standard and it is filled in here. Section 7 sets it out as the top of the template, because that is where a writer meets it.
And one thing about the work itself. If you are writing a use case that is not in a model, stop. It has no identifier, no primary actor and nowhere to be traced from or to. Nothing in this standard will supply what is missing. The model is where that is fixed, and going back for it costs a morning; not going back costs the rest of the project.

![Figure 1 — What one use case is written from, and what is built from it.](figures/SDD-06/SDD-06_fig01.png)

Figure 1 — What one use case is written from, and what is built from it.

### Who writes one, and what they have in front of them

Anyone who can write one goal well: an analyst, a product owner, a domain expert with an editor beside them. They do not need to know the other use cases in the model. They need this one goal, and five things to write it from.

- The survey row — the reference, the name, the primary actor, the level and the one-line brief.
- The boundary and the actor catalogue — who sits outside the system, and what each of them is there for.
- The entity model — the one word for every thing the system keeps a record of.
- The register of business rules — every constraint, written once, each with an identifier.
- The quality requirements that bind this particular goal.
All five belong to the model, and none of them is the writer's to decide. A writer who finds themselves deciding one — inventing a word, settling the level, choosing which requirement this use case realises — has found a defect in the model. The right response is to raise it. It is not to write a sentence that covers the gap over. That line runs through every rule below, and it is the single most useful thing to hold on to while writing.

That person is not the one who designs the model. Designing the model takes the whole system as its input, happens earlier, and answers to a different reviewer. It is governed separately.

### What this standard does not cover

Three things belong elsewhere, and nothing here restates them.

- How the model is designed. Which goals become use cases, how big they are, how they group and relate, where the boundary runs, and when the set of them is complete. A use case that looks like the wrong size, or like two goals wearing one name, is something to raise about the model. Rewriting the prose will not fix it.
- What the entity model contains. A use case names entities and carries no data structure at all. What an entity is, what definition it must carry, what its attributes may hold and how relationships between entities are bounded belong to the standard that governs the entity model.
- How the system is built, and how the tests are run. This standard says that acceptance tests are derived from the flows, and what they must cover. It does not say what form they take, what runs them, or how much coverage is enough.
Diagrams are a fourth case, and a softer one. A use case specification is prose and a table. A sequence, activity or state diagram may sit beside one usefully, and nothing here forbids it, but no rule below requires or governs one.

### What this standard promises, and what it does not

It promises that a use case written to it can be built from: that a developer, a tester and a reviewer reading it separately will describe the same behaviour, and that the tester can write acceptance criteria without having to ask a question first. That is not a hope. It is rule U15, and the review in section 8 turns away a use case that fails it.

It does not promise that two analysts writing the same goal produce the same prose. It promises something narrower and more useful: that two use cases written to this standard have answered the same questions about the same goal, so that wherever they differ, the difference can be pointed at and settled.

It does not promise that a use case which passes the review is correct. Most of the review tests things that can be seen: that a field is filled, that extensions are numbered against their step, that no vague word is hiding a decision. Whether what is written is true of the business is a judgement. Section 8.2 lists the judgements no check can make, so that they are asked deliberately rather than remembered by whoever happens to be in the room.

### Claiming conformance

A use case, or a set of them, conforms to this standard when it does four things.

- Declares the claim. “This specification claims conformance to the rules of this standard, U1 to U21.”
- Names the model it belongs to, and which version of it. A use case that cannot name its model cannot satisfy U18 to U21, and the claim fails at the first rule.
- States, rule by rule, how it satisfies each one and where. A claim without that line-by-line assessment cannot be checked, and so is not a claim. Where a set carries several use cases, the assessment is made once for each of them. A single scenario is a property of one use case, and a verdict given for the set would hide the one that fails.
- Passes the review in section 8, with every line that does not pass recorded as a finding against a named owner. A finding with an owner does not defeat the claim. An unrecorded failure does.
A claim made here says nothing about the model. The two are reviewed separately, by different people, at different moments, and a model may be sound while a use case written from it is not.

### The rules, at a glance

Twenty-one rules, in four groups. Each carries an identifier for use in reviews and in traceability. The identifiers do not run in numerical order through the document, because each rule keeps the number it has always had; this table is the index.

| Rule | In short | Section |
|---|---|---|
| U1 | Use the lightest form that is adequate | 3 |
| U2 | When the form is the full one, fill in every field | 3 |
| U18 | Carry the record header | 3 |
| U19 | Record the requirements this use case realises | 3 |
| U20 | Declare the entities it reads and the ones it changes | 3 |
| U3 | Write one main success scenario, with no conditions in it | 4 |
| U4 | Write steps that say who is acting, and show progress | 4 |
| U5 | Write about intent and responsibility, not screens or technology | 4 |
| U6 | Let the stakeholders' interests decide what complete means | 4 |
| U7 | State the preconditions and the guarantees precisely | 4 |
| U8 | Number each extension against the step it leaves | 4 |
| U9 | Look for every extension, but only ones the system can detect | 4 |
| U10 | Refer to data by name only | 5 |
| U11 | Use the model's word, and never invent another | 5 |
| U12 | Attach quality requirements to the use case they govern | 5 |
| U21 | Cite the business rules; never write them out | 5 |
| U13 | Keep out what belongs somewhere else | 5 |
| U16 | Do not leave a decision hidden inside a vague word | 5 |
| U17 | One rule to a step | 5 |
| U14 | Pair every use case with its acceptance tests | 6 |
| U15 | Test that it can be built from, before accepting it | 6 |

## 2  The same ideas, as they are named elsewhere

Use case writing has collected a good deal of vocabulary over thirty years, much of it figurative and some of it borrowed from one author's metaphor. A reader who has met the older words will recognise the ideas below; a reader who has not loses nothing. This standard uses the plain term in every case, and this table is the bridge.

| What you will read elsewhere | What this standard calls it |
|---|---|
| fully dressed use case | a use case written out in full |
| the basic flow, the happy path | the main success scenario |
| an alternative flow, an exception flow | an extension |
| kite level, sea level, clam level | summary, user goal, subfunction |
| nickname precision | referring to data by name only |
| who has the ball | who is acting at this step |
| the essential style, the black-box style | writing about intent and responsibility, not about screens or technology |
| a non-functional requirement | a quality requirement |
| special requirements | the quality requirements that bind this use case |
| a use case slice | one or a few flows, delivered end to end on their own |
| the postcondition | the success guarantee, or the minimal guarantee |

## 3  Choosing the form, and the record the use case carries

Two questions come before any writing. How much of this use case needs to be written down at all, and what must it carry so that the model can keep track of it? Neither answer is the writer's to invent. Both are already settled, and the first part of this section says where.

### State the level

Every use case states its level: summary, user goal or subfunction. The level is already decided, and it is written on this use case's row in the model's survey. State the same one.

Two signs that the level on the row is wrong. A use case that cannot be finished in one sitting is probably a summary. A use case that is a single step is probably a subfunction. Either is something to raise about the model. Neither is put right by rewriting the prose, and a writer who quietly corrects the level has hidden a defect rather than reported one.

![Figure 2 — The three forms a use case may take, and who chooses between them.](figures/SDD-06/SDD-06_fig02.png)

Figure 2 — The three forms a use case may take, and who chooses between them.

U1  Use the lightest form that is adequate.

Three forms are available. A brief is a single paragraph, for a use case still being scoped. A casual form is a few paragraphs, for one that carries little risk. Written out in full means the whole template of section 7, and is for a use case that is high in business value, high in risk, or one the architecture depends on.

Which form this use case gets is already written on its survey row, decided across the model before any of them were written. If you find yourself choosing the form, the model has not yet decided something it should have.

How much writing this one needs. Within the chosen form, match the amount of writing to the team. A small team sitting in one room can work from a light narrative, because the conversation fills the gaps. A large or widely spread team needs the fuller written form, because there is less conversation to fall back on. That is a judgement about *this* use case. Which use cases are written out in full at all is a decision taken across the model.

U2  When the form is the full one, fill in every field.

A use case written out in full carries all of these: its name, its scope, its level, its primary actor, the stakeholders and their interests, the preconditions, the minimal and success guarantees, the trigger, the main success scenario, the extensions, and any quality requirements that apply.

Leaving a field out is a decision to be taken deliberately and said out loud. It is not something that should happen by default, and an empty field with no explanation beside it is the commonest way for a question to go unasked until somebody is building from it.

U18  Carry the record header.

Every use case carries a short block of structured information at the top, in the form the model requires. At the least it holds the use case's identifier, its name, its level, its primary actor, the requirements it realises (U19), the entities it uses (U20), the business rules that govern it (U21), and its status.

This block is the model's record of the use case. It is read by software as well as by people: the model's survey is generated from these blocks rather than kept alongside them, which is why they have to be filled in the same way every time. Anything stated both in this block and in the prose below will eventually disagree with itself, so state it in the block and let the prose refer to it.

U19  Record the requirements this use case realises.

The header carries the identifiers of the functional requirements, the quality requirements and the constraints this use case realises. They are recorded here rather than in a separate table kept somewhere else, so that they cannot drift away from the behaviour they describe.

Recording none of them is a decision, not an empty field. A use case that realises no stated requirement is either work nobody asked for or a requirement nobody wrote down, and both are worth knowing. Raise it about the model rather than leaving the line blank.

U20  Declare the entities it reads and the ones it changes.

The header names the entities from the entity model that this use case reads, and separately those it changes. Names only. No attribute, no data type, no length and no validation rule appears anywhere in the use case.

The name is the reference and the entity model is where that reference is resolved. Keeping the two apart is what allows a field to be added to an entity without a single use case having to be rewritten.

## 4  Writing the flows

The flows are the use case. Everything else on the page exists to make them readable, testable and traceable. There is one main success scenario, and there are as many extensions as the system can detect conditions; the seven rules below say how each is written.

![Figure 3 — An extension leaves the main success scenario at a numbered step, and ends in one of three ways.](figures/SDD-06/SDD-06_fig03.png)

Figure 3 — An extension leaves the main success scenario at a numbered step, and ends in one of three ways.

U3  Write one main success scenario, with no conditions in it.

The main success scenario is the single path on which nothing goes wrong and every stakeholder interest is met. It is typically three to nine steps. It contains no “if” and no branching at all.

Every condition and every variation belongs in the extensions. A scenario with a branch inside it cannot be read straight through, cannot be numbered reliably, and gives a tester no single path to start from.

U4  Write steps that say who is acting, and show progress.

Each step is one plain sentence: somebody does something, or the system does something, and the goal moves measurably closer. Alternate between what the actor intends and what the system is responsible for.

Almost every action by an actor has a matching response from the system. A step that has none usually means the system's half of the exchange was left out, and whoever builds it will invent that half themselves.

U5  Write about intent and responsibility, not screens or technology.

Say what the actor is trying to do, and what the system is responsible for: “the system validates the return”. Do not say how it looks or how it is built — not “clicks the Submit button”, not “writes a row to the returns table”, and not the name of any product or protocol.

This keeps the requirement stable while the design is still open. A flow written in terms of screens has to be rewritten every time a screen changes, and it quietly settles design questions that nobody has yet been asked.

U6  Let the stakeholders' interests decide what complete means.

List the stakeholders and what each of them needs protected, before writing any flow. Taken together, those interests are exactly what the use case must guarantee, and they are the list the finished flows are judged against.

A stakeholder is a wider idea than an actor: some parties never touch the system and still have an interest that must be honoured. Leaving them off the list is the commonest way a use case comes to be complete in appearance and incomplete in fact.

U7  State the preconditions and the guarantees precisely.

A precondition is something already true when the use case starts, which is not checked again inside it. The minimal guarantee is what still holds when the use case fails. The success guarantee is what holds when it succeeds.

Between them, the guarantees must satisfy every interest listed under U6. The minimal guarantee is the one most often left thin, and it is the one that matters most on the day something goes wrong.

U8  Number each extension against the step it leaves.

Label each extension with the number of the step it branches from — 3a, 3b — and use \*a for a condition that can arise at any point rather than at one particular step. Each extension states its condition, then how it is handled, then what happens next.

There are only three things that can happen next: it rejoins the main success scenario, it ends in success by another route, or it ends in failure. Say which. An extension that does not say where it goes leaves the reader to guess, and two readers will guess differently.

U9  Look for every extension, but only ones the system can detect.

Go through the steps deliberately and ask, at each one, what the system can detect and how the step can fail. This is where requirements nobody has stated come to light, and it is the most productive hour in the whole exercise. Leave out conditions the system cannot detect: they may be real, but they are not requirements on this system.

Mark each extension as one of two kinds. A business alternative is something the business does differently — an inactive party, a missing permission, a closed period. A failure of the system or its environment is an outage, a timeout, a lost response. Both belong in the use case, and the second kind is where the minimal guarantee of U7 is earned. They are marked because they are reviewed by different people and tested differently — never so that one of them can be left out.

## 5  What may and may not appear inside a use case

A use case attracts material that belongs somewhere else. Data structure drifts in from the database design, constraints get written into a step instead of being registered, a second word appears for something that already had one, and a vague adverb stands in for a decision nobody wanted to take. Seven rules keep the page clear.

U10  Refer to data by name only.

Name the thing — “the return”, “the assessment” — and never describe how it is put together. No field list, data type, format, length or validation rule appears in a flow, in an extension or in a guarantee.

A reader who needs to know what a named thing holds looks it up in the entity model the header declares, and the standard that governs the entity model says what has to be there. A flow filled with data structure is a flow that has to be rewritten every time a field is added, and it will not be rewritten, so it will simply become wrong.

U11  Use the model's word, and never invent another.

Every concept has one word in the model: from the entity model if it is something the system keeps a record of, and from the glossary otherwise. Use that word. “Return”, “filing” and “submission” are not three names for one thing.

If the word you need is in neither place, raise it. Do not invent one to finish the sentence. A word invented under time pressure is indistinguishable, six months later, from a word that means something slightly different, and the cost of telling them apart falls on whoever reads both use cases.

U12  Attach quality requirements to the use case they govern.

Quality requirements that apply to this use case in particular — how fast, how secure, how many at once, how available — are recorded on it, so that they can be tested where they apply instead of being lost in a list at the back of another document.

Where a flow would otherwise say “quickly”, replace the word with a reference to the requirement that says how quickly. Business rules are not recorded here; they are cited under U21.

U21  Cite the business rules; never write them out.

Every business rule this use case depends on is cited by its identifier in the register: once in the header, and again at the step it governs. No rule is written out in the text.

If a constraint cannot be cited because it is not in the register, that is something to raise about the model. The answer is to register the rule, not to write it into the flow. A rule that lives inside one sentence of one flow is invisible to every other use case, to the reviewer, and to anything derived from the model later.

U13  Keep out what belongs somewhere else.

If a scenario covers more than one complete piece of business, split it. If a step belongs to a precondition, or to a different use case, move it there.

One use case, one goal, one sitting. A use case that has quietly become two cannot be sized, cannot be prioritised against anything, and cannot be tested without deciding which half is being tested.

U16  Do not leave a decision hidden inside a vague word.

Words such as *normally*, *usually*, *quickly*, *appropriately*, *as needed*, *if possible* and *should* conceal decisions that have not been taken. Replace each of them with the rule itself: say the condition under which the behaviour applies, and say what happens when it does not. Replace a word like “fast” with a reference to the requirement that quantifies it.

Vague wording does not stay vague further down the line. It gets resolved — quietly, and differently — by whoever reads it next, and nobody finds out which reading was used until the behaviour is in front of a user.

U17  One rule to a step.

A step joined by “and” or by “or” usually holds two behaviours that fail for different reasons, produce different results, and need different tests. Split them.

A step that covers several things cannot be the target of a numbered extension, because the extension cannot say which part of it failed, and it cannot be traced to a single business rule.

## 6  Deciding that it is ready

Two rules decide whether a use case is finished. They are kept apart from the rules above because they are applied by different people at a different moment: the first by whoever will test the use case, the second by the pair who accept it.

U14  Pair every use case with its acceptance tests.

Derive the tests from the main success scenario and from every extension. Those tests are what “done” means, both for the use case as a whole and for each piece of it that is delivered on its own.

The tests are written against the guarantees as well as against the steps. A set of tests that walks the steps and never checks the minimal guarantee has tested the good day and left the bad one to chance. A use case without tests is not ready to be built from.

U15  Test that it can be built from, before accepting it.

A use case is ready when three things are true. Two people reading it separately describe the same behaviour. A tester can write acceptance criteria from it without asking a question. And nothing further down the line — a developer, a generator, a reviewer — has to invent a rule the use case failed to state.

A use case that fails any of the three can be read but cannot be built from, and being readable is not the standard. Apply the test at the review, not while writing: the writer is the one person who cannot perform it, because they already know what they meant. Record a failure against the clause that caused it rather than against the use case as a whole, so that the fix is obvious to whoever picks it up.

U15 is the rule this standard is built around. Every other rule improves the odds that it passes, and none of them is a substitute for running it. It is a judgement made by people about one piece of prose, it cannot be automated, and section 8.2 is where it sits at the centre of the review.

## 7  The template, written out in full

Copy this template for any use case the model has decided to write out in full (U1). The left column is the field; the right column says what to write in it and which rule it satisfies. Delete the guidance once the field is filled.

The template is in two parts, and the division is not a matter of layout. The first part is the record header: the fields the model requires, from which its survey is generated and against which its automatic checks run. That list is decided in the standard that governs the model, and adding a field to it is a change to both standards at once. The second part is the narrative: the use case itself, which no program reads.

![Figure 4 — The two parts of a use case written out in full, and who reads each.](figures/SDD-06/SDD-06_fig04.png)

Figure 4 — The two parts of a use case written out in full, and who reads each.

### 7.1  The record header

| Field | What to record |
|---|---|
| Unique identifier | The stable reference the model knows this use case by. |
| Use case name | An active verb and its object, from the primary actor's point of view, in the words the business uses. The model settles the name; write the same one. |
| Level | Summary, user goal or subfunction, as written on the survey row. |
| Primary actor | The actor whose goal this use case exists to satisfy. |
| Status and priority | Draft, reviewed or baselined; and the priority the model set from business value and risk. |
| Requirements realised | The identifiers of the requirements, quality requirements and constraints this use case realises (U19). |
| Entities read or changed | The entities from the entity model this use case reads, and separately those it changes, by name (U20). |
| Business rules cited | The identifiers of the registered rules that govern this use case (U21). |
| Relationships | Which use cases this one includes, which ones extend it, and the point at which each extension attaches. |

State each of these once, here. A value written both in the header and in the prose below will come to disagree with itself within a quarter (U18).

### 7.2  The narrative fields

| Field | What to write |
|---|---|
| Scope | The system under discussion, and whether it is being treated from the outside only or from the inside as well. |
| Stakeholders and interests | Each stakeholder, and the interest they need protected. Taken together these decide what complete means (U6). |
| Preconditions | What is already true when the use case starts, and is not checked again inside it (U7). |
| Trigger | The business event that starts the use case. It may be a clock. |
| Minimal guarantee | What the system still guarantees if the use case fails (U7). |
| Success guarantee | What is true when it succeeds. It must satisfy every interest listed above (U7). |
| Main success scenario | The single path on which nothing goes wrong: three to nine numbered steps, no branching (U3 to U5). |
| Extensions | Numbered against the step each one leaves, stating the condition, the handling, and how it ends (U8, U9). |
| Quality requirements | The quality requirements that bind this use case, cited rather than written out again (U12). |
| Acceptance tests | Derived from the main success scenario and from every extension; they are what done means (U14). |

### 7.3  Two things that are not fields, and where they go instead

Supporting and offstage actors are not fields of this template. Which actors exist, and which kind each of them is, is settled across the model and held in its actor catalogue. A supporting actor appears in this document wherever the use case calls on it — in a step, or in the shared behaviour a step includes. An offstage actor appears among the stakeholders and their interests, which is where its interest is honoured (U6).

The business rules themselves are not written here either. The header carries their identifiers and the steps cite them, but each rule is written once, in the register, and nowhere else (U21).

## 8  The review

Run this on one use case, at its review, before it is accepted. The reviewer pair and the tester run it together. Run the whole of it once for each use case: a verdict given for a set hides the one member of the set that fails.

The review has two halves. The first is what a reader — and, in time, a program — can confirm by looking. The second is what only a person can judge, and it is not the lesser half.

![Figure 5 — The two halves of the review, and the one decision they lead to.](figures/SDD-06/SDD-06_fig05.png)

Figure 5 — The two halves of the review, and the one decision they lead to.

### 8.1  What a reader can check

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
| U19–U21 | Every identifier the header cites for something the shared registers publish resolves in the set its register publishes under the standard for the shared registers (SDD-04, IOS-15), read in the shape that standard's setting `registers.published_set_shape` names. The reviewer pair answers this line at the review; it is the point at which the shared registers are handed to this use case. | ☐ |
| U13 | Nothing out of scope and nothing belonging to a second business process appears: one use case, one goal, one sitting. | ☐ |
| U16–U17 | No decision hides inside a vague word, and each step carries one rule. | ☐ |
| U14 | Acceptance tests derived from the main success scenario and from every extension exist. | ☐ |
| U15 | The use case can be built from: the same behaviour on two independent readings, acceptance criteria derivable without a question, nothing left for a reader to invent. | ☐ |

A line that is not satisfied is a finding with a named owner. It is not an exception to be waved through.

### 8.2  What only a person can judge

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

### 8.3  The gate

Every line of section 8.1 is answered, and every question in section 8.2 has been asked out loud by the reviewer pair, before the use case is accepted.

## 9  The ways use cases go wrong

These are the failures that recur inside a single use case, found by the people who review it, test it or build from it, and fixable by them on the spot. The failures that can only be seen by reading across a whole model — decomposition, a model that has stopped being maintained, a use case nothing asked for — are a separate catalogue and are governed separately.

| The failure | How it shows | The rule that corrects it |
|---|---|---|
| Screens in the flow | Steps say “clicks Submit” or “chooses from the list”; the requirement has to be rewritten every time a screen changes. | Write about intent and responsibility only (U5). |
| Technology in the flow | Steps name databases, tables, interfaces or a query language; a design decision has been settled inside the requirement. | Say what happens, not how; leave the design to the design (U5). |
| The system's half missing | Only the actor's steps are written, and whoever builds it guesses what the system does in between. | Give almost every actor action a system response (U4). |
| A branch in the main scenario | “If … then …” inside the path where nothing goes wrong; the flow cannot be read straight through and has no single path to test. | One unconditional main scenario; every condition becomes a numbered extension (U3, U8). |
| An extension that goes nowhere | The extension states a condition and stops, without saying whether it rejoins the scenario, succeeds by another route, or fails. | Number each extension to its step and say how it ends (U8). |

Two more failures are met while reading one use case and corrected in the model rather than here: a word invented for something that already had one, and a constraint written into a step instead of being registered. Both are found on this page and fixed on another, and raising them is the whole of the writer's part.

## 10  A worked example

The example is a revenue administration system: a system that receives tax returns, assesses them, collects what is owed and pursues what is not. The model it belongs to is the worked model in the standard that governs the model, and it is worth reading first — the boundary, the actors and the shared behaviour this use case refers to are all decided there. What follows is the other half of the same piece of work: one goal from that model, written out in full to the template of section 7.

The use case is Submit a return, the first goal in the model at the level of a single sitting. It was chosen because it exercises the rules that are hardest to demonstrate on a simpler one. It draws on three pieces of shared behaviour and is extended by a fourth use case, so the alternation of actor and system in U4 has something to alternate against; and it has six extensions of both kinds, so the numbering of U8 and the marking of U9 have something to number and mark. A use case whose only extension is a validation failure teaches neither.

### 10.1  The record header

| Field | Content |
|---|---|
| Unique identifier | UC-RAS-01 |
| Use case name | Submit a return |
| Level | User goal — a goal completed in one sitting |
| Primary actor | Taxpayer |
| Status and priority | Baselined · High. It is required by statute, it runs at high volume, and it is the point at which revenue is recognised |
| Requirements realised | FR-FIL-011 *file a return for an open period*; FR-FIL-014 *issue a confirmation of filing*; QR-PRF-002 *throughput and response time on a peak filing day*; QR-SEC-006 *a record of filing that cannot be altered without detection*; CON-STA-003 *the statutory filing calendar* |
| Entities read or changed | Reads: Taxpayer, Filing obligation, Filing period, Tax register record. Reads and changes: Return, Assessment, Payment, Filing confirmation |
| Business rules cited | BR-FIL-04 *a return may be filed only against an open obligation*; BR-FIL-07 *how many attempts at proving identity are allowed*; BR-FIL-12 *what makes a return complete*; BR-FIL-19 *how the liability is derived*; BR-DBT-02 *when an unpaid balance becomes an obligation* |
| Relationships | Includes *Prove identity*, *Validate return data* and *Calculate the liability*. Extended by *Pay what is due*, at the point where a balance is due |

*The identifiers above belong to the example. They stand for entries in a requirements catalogue and a rules register that a real model would carry; no register is being quoted here.*

### 10.2  The narrative fields

Two of the ten narrative fields — the main success scenario and the extensions — are set out below the table rather than inside it, because of their length. That is a matter of layout. All ten fields are present.

| Field | Content |
|---|---|
| Scope | The revenue administration system, treated from the outside only |
| Stakeholders and interests | Taxpayer: to file accurately and be given proof of it. Tax officer: a complete and valid return, and a liability that can be assessed. Audit function: a record of what was filed and when, which cannot be altered without detection. Payment gateway: a well-formed request to settle. |
| Preconditions | The taxpayer holds a registered account and has an open filing obligation for the period. |
| Trigger | The taxpayer chooses to file a return for a period that is open. |
| Minimal guarantee | Every attempt to submit is recorded; no partial or unconfirmed return is ever treated as filed; nothing the taxpayer had already entered is lost. |
| Success guarantee | A validated return is recorded against the period, the liability is calculated and shown, a confirmation carrying a reference and a timestamp is issued and cannot afterwards be altered without detection, and any balance due is either settled or raised as an obligation. |
| Main success scenario | Eight steps — section 10.3 |
| Extensions | Six — section 10.4 |
| Quality requirements | The confirmation of filing cannot be altered without detection (QR-SEC-006). Throughput and response time on a peak filing day are as required by QR-PRF-002; the figures live there and are not repeated here. Every access is recorded for audit. |
| Acceptance tests | One test for each step below and one for each extension, including those that end in failure rather than rejoining. The tests are written against the guarantees as well as the steps: the minimal guarantee is asserted by the tests for 2a, 3a and \*a, and the success guarantee by the test for step 8. |

### 10.3  The main success scenario

1. The taxpayer asks to submit a return for the open period.
2. The system proves the taxpayer's identity (shared behaviour: *Prove identity*).
3. The system presents the return, already filled in with what it holds for the period.
4. The taxpayer supplies the figures and confirms them.
5. The system checks the return for completeness and consistency (shared behaviour: *Validate return data*).
6. The system calculates the liability and shows the result (shared behaviour: *Calculate the liability*).
7. The taxpayer confirms the submission.
8. The system records the return, issues a confirmation carrying a reference and a timestamp, and closes the obligation for the period.

### 10.4  The extensions

Each is numbered against the step it leaves, states its condition and how it is handled, says how it ends, and is marked as one of the two kinds U9 requires.

| Ref | What happens | Kind |
|---|---|---|
| 2a | Identity cannot be proved. The system offers a way to recover it and, after the allowed number of attempts, ends the use case reporting failure. The minimal guarantee holds. | business alternative |
| 3a | The tax register does not answer within the time allowed for the read. The system presents the return unfilled, records that it was filed without being pre-filled, and continues at step 4. The minimal guarantee holds. | system or environment failure |
| 5a | The checks find errors. The system reports each error against the item it belongs to; the taxpayer corrects them and the flow resumes at step 5. | business alternative |
| 6a | A balance is due once the liability is calculated. The taxpayer chooses to settle it now: *Pay what is due* runs, settling through the payment gateway, and the flow resumes before step 8. | business alternative |
| 8a | A balance is due and has not been settled. The system records the return and raises the balance as an obligation, which may later be pursued. The use case ends in success. | business alternative |
| \*a | At any step, the service becomes unavailable. The system keeps what has been entered as a draft the taxpayer can return to, and reports the interruption. The use case ends without filing, and the minimal guarantee holds. | system or environment failure |

### 10.5  Reading it against the rules

The header carries every field the model requires and states each of them once (U18). What this use case realises, what it touches and what governs it are identifiers, not prose (U19 to U21).

The main success scenario is one unconditional path of eight steps with no “if” in it, and every condition has become an extension (U3, U8). The steps alternate between what the taxpayer intends and what the system is responsible for, and each action by the taxpayer has a response (U4). No step names a screen, a control, a stored table or a protocol (U5).

Data appears by name and only by name — “the return”, “the liability”, “a confirmation carrying a reference and a timestamp” — and not one field, type or format appears anywhere, because the entity model the header declares is where a reader goes for that (U10, U20). Every rule the flows depend on is cited by its identifier and none is written out in a step (U21). The requirement about speed is a reference, not the word “quickly” (U12, U16).

The three supporting actors the model names are all reached from this use case: the identity service through the shared behaviour at step 2, the payment gateway through the use case that extends this one at 6a, and the tax register at step 3 and again at 3a. None of them is named in a step that does not call it, and none is classified here — that was settled across the model.

The extensions are numbered to their step, name their condition, and say whether they rejoin, succeed or fail. Both kinds are present, and the two failures of the system or its environment are where the minimal guarantee of U7 is earned (U8, U9).

One thing here is worth arguing about rather than admiring, and it is left in for that reason. Step 8 does three things. It records the return, it issues a confirmation, and it closes the obligation — three behaviours that fail for different reasons and would need three tests. Under U17 a reviewer would be right to ask for it to be split, and the fact that it reads smoothly is exactly why the rule exists.

## 11  The questions this standard does not answer

A standard that hides what it cannot yet say is worse than one that names it. Four things are unsettled.

### Only one of the three forms is written down

U1 names a brief, a casual form and the full form, and section 7 sets out the full form only. What a brief must contain, and the point at which a casual form stops being adequate, are not written down here. In practice the survey row serves as the brief and the casual form is whatever the team agrees between them — which is to say that the choice U1 makes is governed while the two lighter things it chooses between are not. That is a gap, not a position.

### Whether a use case is correct, as opposed to usable

U15 tests whether a use case can be built from: whether two readers agree, whether a tester can derive criteria, whether anything is left to be invented. All three can pass on a use case that describes behaviour the business does not actually want. Section 8.2 handles that by asking a person. No rule here closes it.

### Where supporting and offstage actors are recorded

Which actors exist and what kind each of them is belongs to the model, and this template accordingly has no field for supporting or offstage actors. They appear instead wherever the use case touches them: a supporting actor in the step that calls it, an offstage actor among the interests. Whether a use case written out in full should nonetheless carry them as a field of their own, so that a reader can see the whole cast without opening the model, is a fair question and is not settled here.

### Whether the two standards work as a pair

No analyst has yet been handed both standards and asked to write a use case from them. Until that has happened, the seam between them is a proposal rather than a finding, and the part of it most likely to be found wanting first is the list in section 1 of what has to be read before starting.

## 12  Where these rules come from

This standard draws the shape of the template, the discipline of the main success scenario and the treatment of extensions from the use case writing literature; the three forms and the style of writing a step from the object-modelling tradition and its published process guidance; and the readiness test, the discipline about vague words and the rule of one thing to a step from the more recent work on specifications that are meant to be built from directly.

- Alistair Cockburn, *Writing Effective Use Cases*. The template written out in full (section 7), the main success scenario and the extensions (U3, U8, U9), stakeholders and their interests (U6), and the guidance on writing a step (U4, U17).
- Craig Larman, *Applying UML and Patterns*, the use case chapter. The three forms a use case may take (U1), and writing about intent rather than about mechanism (U5).
- The Rational Unified Process, and its template for the written form of a use case. What the per-use-case document contains, and the fact that writing it is a separate job with a separate accountable owner (section 1).
- Simon Martinelli, *Spec-Driven Development*. The readiness test (U15), the discipline about words that hide a decision (U16), one rule to a step (U17), and the use case held as the artefact that later work is derived from (U18). One position of his is not adopted here: he leaves failures of the system and its environment out of a business use case, and U9 requires them to be written down and marked rather than left out.
- The catalogue in section 9 draws on the failures reported repeatedly in the practitioner literature on use case quality, rather than on any single source.
What these sources do not settle. None of them says when a use case is finished, and none is cited here as though it did. The published notation for use case diagrams does not standardise the written body of a use case at all, and nothing here rests on a claim that it does. Nobody has measured whether separating these two standards produces better work than keeping them together; the case for separating them rests on the two activities having different owners, different inputs and different moments, and it is argued on that ground alone.

## 13  What it owes the application model

The application model is written goal by goal, and a use case written out in full is the document written for the goal. This section says where each thing it carries lands in the model, and where each thing the model of a goal reads from the documents settled once for the whole system lands, so that whoever writes the model has one place to look for every kind of thing it is written from. Every section named in the tables is a section of the specification of the model, `SDD-09_The_Application_Model_v1.1.docx`. The standard for the shared registers states the same for its own contents in its section 10, and the rows here that cover those contents name that section rather than restate it. The things a set of screens carries have their rows in section 16 of the standard for the screens, SDD-07.

Four words are used in the tables in one sense only. A landing is **mechanical** when the thing lands in one place fixed by its kind, so that a program can check that it did. It is a **judgement** when whoever writes the model has to decide where it lands; a row that reads mechanical with a condition is a judgement for a thing only where the condition holds. Every judgement is written down as an **assumption**: the thing, where in the model it landed, the decision in one sentence, and its ground in the use case by identifier and section. An assumption overturned at the review of the model goes back to the use case as a finding, and never into the model as an edit. A thing that cannot land is written down as a **loss**: what it asked for, how it landed instead if any part of it did, and the construct of the model it would need. A loss is never worked around by an invention (SDD-01, section 14, rule 5). Where a row says that a thing is carried by its own document and is not a loss, nothing in the model is owed for it.

### 13.1  What a use case written out in full carries

| What the use case carries | Where this standard asks for it | Lands in the application model | Mechanical or judgement | Where it cannot land |
|---|---|---|---|---|
| The use case itself: its identifier and its name | 7.1, the identifier and the name | §6.2 `features[]`, one entry with its `id` and `name` | mechanical | never |
| Its level, its status and its priority | 7.1 | nowhere: the model carries no level, status or priority of a goal | — | carried by the use case, and not a loss |
| The primary actor | 7.1 | §7 `roles[]`: the role named wherever the goal's moves, menus and scenarios name who acts | mechanical | never |
| A requirement, a quality requirement, a constraint | 7.1, the requirements realised; 7.2, the quality requirements | §6.1 `requirements[]`, one entry each, with `source` naming the entry of the register of requirements; and §6.2, the feature's `requirements` | mechanical | never: the register of requirements is where the model's trace begins |
| A record the use case reads or changes | 7.1, the entities read or changed | §11 `entities[]`, one entry for each record | mechanical for the entry; a judgement for its `kind` (§11.1) where the entity model does not settle it | a loss naming the record |
| A business rule | 7.1, the business rules cited, and the step each one governs (U21) | one of four places: §11.3 an attribute's `required`, `unique` or `pattern`, where it holds one field against one value; §11.4 `validations[]`, where it makes values required on a condition; §12.2 a transition's `guard` and `guard_expr`, where it guards a move; §14 a form's `validation[]`, where it is a rule on a form | judgement: which of the four | a loss naming the rule and the construct it needs |
| The relationships to other use cases | 7.1 | nowhere: an included or an extending use case is a feature of its own (§6.2), and the point at which an extension attaches stays in the use case | — | carried by the use case, and not a loss |
| The scope | 7.2 | nowhere: the model is of one application, bound in §5 | — | carried by the use case, and not a loss |
| A stakeholder interest | 7.2, the stakeholders and their interests | nowhere | — | carried by the use case, and not a loss |
| A precondition | 7.2 | §22.2 a scenario's `given`: its fixture of starting records (§22.1) and its acting role | judgement | a loss where the precondition is not the state of a record of this model |
| The trigger | 7.2 | §12.2 the `trigger` of the move the goal's first act makes: a person, the system, a clock or a process | judgement | carried by the use case where the goal moves no record, and not a loss |
| A guarantee, minimal or success | 7.2 | §22.2 a scenario's `then[]`, in the kinds of assertion that section lists | judgement | a loss where the guarantee needs an assertion that §22.2 does not list |
| A numbered step of the main success scenario | 7.2, the main success scenario | §13.1 `activities[]`, where the goal has a process (§13); and §22.2, one scenario for the main success scenario | judgement for the activities; mechanical for the scenario | an assumption for the activities; never for the scenario |
| A variation, numbered against its step | 7.2, the extensions | §13.1 `outcomes[]` and §13 `routing[]`, where the goal has a process; §12.2 a transition, where the variation moves the record; and §22.2, one scenario for each extension | judgement for the process; mechanical for the scenario | an assumption for the process; never for the scenario |
| An acceptance test | 7.2, the acceptance tests (U14) | §22.2 `scenarios[]`, with its fixture in §22.1 | judgement | a loss where the test needs an assertion that §22.2 does not list |

### 13.2  What the model of a goal reads from the documents settled once

| Kind of thing | Written under | Lands in the application model | Mechanical or judgement | Where it cannot land |
|---|---|---|---|---|
| An attribute | SDD-03, part 5.1 | §11.3 `attributes[]`, its `type` taken from the entity model's answer | mechanical | a loss naming the attribute and the type the model lacks |
| A relationship | SDD-03, part 5.2 | §11.3 an attribute of type `ref`; or §11.2 `parent`, for a record that depends on another | mechanical | a loss |
| A governed list | SDD-03, part 5.3, the table of governed lists; SDD-04, part 5.5 | the binding on the attribute, §11.3 `vocabulary`, where SDD-04 section 10 lands it; the list itself as a vocabulary (§8), or as a record of kind `md_lookup` (§11.1) where each value carries more than a code and a label; the list's own entry lands nowhere, as that section states | mechanical | a loss for the list's own entry |
| A glossary term | SDD-03, part 5.4 | nowhere: the model carries no glossary | — | carried by the entity model, and not a loss |
| An identity rule: what makes two rows the same thing | SDD-04, part 5.1 | where SDD-04 section 10 lands it: §11.2 `pk` and `indexes[]`, §11.3 `unique` | mechanical | a loss |
| Who writes each fact | SDD-04, part 5.1 | nowhere, as SDD-04 section 10 states | — | a loss naming the construct that section asks for: a named party as the authority for one attribute |
| A state, and a move between states | SDD-04, part 5.1 | where SDD-04 section 10 lands them: §12 `states[]` and `transitions[]` | mechanical | never |
| An event | SDD-04, part 5.3 | no landing site of its own, as SDD-04 section 10 states; the nearest are a transition's `trigger` (§12.2) and an `emit_event` effect (§12.3), and an event published for another module lands nowhere | judgement | a loss naming the construct that section asks for |
| A computation | SDD-04, part 5.4 | where SDD-04 section 10 lands it, §11.3 an attribute of type `computed` with its `formula`; or a named query (§10), where the figure is read and not kept | judgement: which of the two | a loss for the fields of the catalogue that land nowhere |
| A setting | SDD-04, part 5.6 | nowhere, as SDD-04 section 10 states | — | a loss naming the construct that section asks for |
| A class of change | SDD-04, part 5.7 | nowhere, as SDD-04 section 10 states for a setting's class of change | — | a loss naming the construct that section asks for |
| A slice | SDD-05, section 10 | §6.2 the order of `features[]`, and their `depends_on` | judgement | an assumption |
| The application binding | SDD-08, part 7.1 | §5 the `app` section | mechanical | never |
| A component switched on | SDD-08, part 7.2 | §9 `catalog[]` | mechanical | never |
| A process with its machinery | SDD-08, part 7.3 | §13 `processes[]`, with its `realization` | mechanical for the realisation; its activities are a judgement, as 13.1 says | never for the realisation |
| A crossing of the boundary, field by field | SDD-08, part 7.4 | §20 `interfaces`, `inbound[]` or `outbound[]`; field by field it lands only as the attributes an inbound entry exposes (§20.1) | mechanical | a loss for the fields the model cannot carry |
| A bespoke component | SDD-08, part 7.5 | §23 the bespoke-plugin budget | mechanical | never |
| An architecture decision | SDD-08, part 7.6 | nowhere | — | carried by the architecture specification, and not a loss |
