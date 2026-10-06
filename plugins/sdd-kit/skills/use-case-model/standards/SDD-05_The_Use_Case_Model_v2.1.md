# SDD-05 · The Use Case Model

*This copy is carried by sdd-kit, the SDD method's skills for the service design course. It keeps the edition stated below; where the edition drew an example from the method's author's own client work, this copy carries an example set in Progressa in its place and says so where it does.*

*The single statement of what a system is for: one boundary, the people outside it, every goal they need, and how those goals group together*

*AN INTERNAL STANDARD  ·  VERSION 2.1  ·  22 SEPTEMBER 2026  ·  IN FORCE*

*Twenty-two rules, a model record, and a review. Discharged once for the whole system, never goal by goal.*

Field | Value
--- | ---
Document | SDD-05 · The Use Case Model. One boundary, the people outside it, every goal they need, and how those goals group together. It carried no code of its own, and was the file Use_Case_Model_Standard_v2.0.docx, until the edition of 28 August 2026.
Version and standing | Version 2.1 · 22 September 2026 · in force. It supersedes version 2.0 of 28 August 2026, which is kept in x_archive/. What changed: one sentence was added to rule M15, naming the set of screens that serves a use case, governed by SDD-07, as a link of the trace between the use case and what is built; and one sentence was added to rule M16, naming the list a use case binds to as the register of requirements published under SDD-02, rule RQR-27. No rule was added, removed or renumbered. A claim of conformance made against version 2.0 remains a claim against version 2.0. An internal standard of FiscalAdmin OÜ, owned and approved by Aare Lapõnin, for the work of FiscalAdmin OÜ.
Who writes the document it governs | One named architect, one model for each system.
Who reads it | The reviewer who decides whether the model may be built from, and the analyst who writes a use case out of it.
When it is written | Before any use case is written out in full, and after the first pass of the entity model.
Rules | M1 to M22.
What it does not cover | Section 1 names each boundary and where the subject belongs instead. How one use case is written is covered by SDD-06.
Author | FiscalAdmin OÜ · Aare Lapõnin

---

Contents

1  What this standard is for

2  The words, defined once

3  The principles

4  Boundary and design scope

5  Actors

6  Identifying use cases and setting granularity

7  Relationships

8  Structure, completeness and traceability

9  The model record

10  Slicing and delivery

11  The review

12  The ways models go wrong

13  A worked model

14  The questions this standard does not answer

15  Where these rules come from

Figures

Figure 1 — What the model is designed from, what it contains, and what is built from it.

Figure 2 — The three levels of goal, and which of them a model is mostly made of.

Figure 3 — One boundary, with the kinds of actor outside it.

Figure 4 — The three relationships, and which way each arrow runs.

Figure 5 — Completeness is a two-way condition.

Figure 6 — The trace is carried on the artefacts themselves.

Figure 7 — The record header is the only part written by hand.

Figure 8 — A slice is one or a few flows taken from a use case, running end to end.

Figure 9 — The worked model.

## 1  What this standard is for

### What a use case model is

A use case model is the system-level statement of what a system is for: one boundary drawn around it, the actors outside it, every goal those actors need it to serve, how those goals group and relate to one another, and the record that keeps the whole of it complete, traceable and current.

There is one use case model per system. Every obligation in this standard is discharged once across that model, or once for each release of it. None of them is discharged use case by use case. Where a rule needs something recorded on an individual use case, it says what must be recorded and stops there.

![Figure 1](figures/SDD-05/SDD-05_fig01.png)

*Figure 1 — What the model is designed from, what it contains, and what is built from it.*

### Who designs it, and what they have in front of them

One person is accountable for the model as a whole: a solution or enterprise architect, or a lead analyst. They have the business goals and processes, the requirement or capability catalogue, the landscape of people and systems around the system, and the architecture's boundaries — and they have the authority to settle where the boundary runs. Every rule below is written to be applied from that position. Where a rule needs a decision that person cannot take alone, the rule says who takes it.

That person is not the one who writes an individual use case. Writing one use case takes a single row of the survey as its input, happens later, and answers to a different reviewer. This standard does not cover it.

### What this standard does not cover

Three things belong elsewhere, and nothing here restates them. A rule written in two places is a rule that will drift, so where another standard governs, this one points at it and adds only what it does not say.

- How an individual use case is written — its format, its flows, its guarantees, its writing style and the test that says it is ready to build from. That is a separate activity with a separate reader, and it is governed separately.
- What the entity model contains. This standard requires the model to name exactly one entity model and to have every entity its use cases refer to defined in it. What an entity is, what definition it must carry, what its attributes may hold and how its relationships are named and bounded belong to the standard that governs entity models.
- How the system is designed, built and stored. Design and realisation follow the model. Rule M20 says only which of them comes first.

### What this standard promises, and what it does not

It promises that a model built to it can be checked. Every condition it states is either something a reader can point at in the model, or something the review in section 11 asks for by name and records an owner against when it is absent.

It does not promise that two architects modelling the same system will draw the same model. There is no published test for when a use case model is finished, and this standard does not offer one. What section 11 offers instead is the smaller and more honest thing: two models built to this standard have answered the same questions about the same system, so every difference between them can be pointed at and argued about.

It also does not promise that passing the review is sufficient. Section 11 tests structural properties — that something is named, recorded, classified, bound or covered. It does not ask whether what is recorded is true. Section 14 states that limit rather than leaving a reader to discover it.

### Claiming conformance

A use case model conforms to this standard when it does three things.

- Declares the claim. “This model claims conformance to the model-level rules of this standard, M1 to M22.”
- States, rule by rule, how it satisfies each one and where. A claim without the line-by-line assessment is not checkable, and is therefore not a claim.
- Passes the review in section 11, with every line that does not pass recorded as a finding with a named owner. An owned finding does not defeat the claim; an unrecorded failure does.
A model may conform to this standard and carry no written use cases at all. The model and the individual use cases are reviewed separately, by different people, at different moments.

## 2  The words, defined once

The rules rely on a small and precise vocabulary. Teams that blur these terms produce blurred models, so the definitions below are normative. Every word defined here is defined here and nowhere else.

### 2.1  The core objects

- A use case. The complete set of ways of using a system to achieve one goal for one actor — every success and every failure for that goal, taken together. A use case is a container of behaviour. It is not a feature, a screen, a function or a stored record.
- A use case model. The organised whole: the system boundary, the actors outside it, all the use cases inside it, their relationships, and the supporting material that goes with them. The model states the total value the system provides and fixes its scope.
- A scenario, or flow. One specific path through a use case — one sequence of interactions between the actors and the system. The single unconditional successful path is the main success scenario; every variation and every failure is an extension.
- A slice. One or a few related flows drawn out of a use case to form an independently deliverable, end-to-end, testable unit of value. Slices, not whole use cases, are the unit of planning and delivery on enterprise work. Section 10 explains how they are cut.

### 2.2  Actors and stakeholders

An actor is anything with behaviour outside the system boundary that interacts with the system: a person named by the role they play, another system, a device, or a clock. A stakeholder is anyone or anything with an interest in the system's behaviour, whether or not it interacts. Every actor is a stakeholder; not every stakeholder is an actor.

This standard uses three kinds of actor:

- Primary — the actor whose goal the use case exists to satisfy. It normally starts the use case.
- Supporting — an external party the system calls on in order to reach the goal, such as a payment service or an identity service.
- Offstage — a party with a real interest in the outcome that neither starts the use case nor is called by it, such as an audit or regulatory function. It is recorded so that its interest is honoured rather than forgotten.
An actor may also be a system, a device or a clock. Rule M6 requires those to be modelled as actors wherever they apply, and Figure 3 in section 5 shows all five together.

### 2.3  Goal levels

Goal levels keep a model at a consistent altitude, and make granularity a deliberate choice rather than an accident. The main body of any model — its backbone — sits at the level of a goal completed in one sitting. The other two levels exist only to group that set or to factor it.

![Figure 2](figures/SDD-05/SDD-05_fig02.png)

*Figure 2 — The three levels of goal, and which of them a model is mostly made of.*

Every use case declares which of the three levels it sits at. Where the model keeps its backbone is a rule of this standard (section 6).

### 2.4  The same ideas, as they are named elsewhere

The literature has two or three names for most of these things. This table is the bridge, so that an architect reading a textbook or another organisation's model can tell what they are looking at.

| What you will read elsewhere | What this standard calls it |
|---|---|
| fully dressed use case | a use case written out in full |
| basic flow, happy path | the main success scenario |
| alternative flow, exception flow | an extension |
| kite level, sea level, clam level | summary, user goal, subfunction |
| the Boss test | the manager's test (M9) |
| Elementary Business Process, EBP | the single business event test (M9) |
| essential style, black box | intent and responsibility only, no mechanism (P4) |
| use case realisation | a design realisation |
| system under discussion, SuD | the system under discussion (M1) |
| use case survey, use case index | the survey (M13) |
| business use case model | a model whose boundary is the organisation (M2) |

## 3  The principles

Eight principles underlie every rule that follows. Where a rule seems not to fit the system in front of you, return to these: they say what the rules are for.

P1  Model behaviour and goals, not features.

A use case names a goal an actor wants, and captures the whole behaviour of reaching it — the successes and the failures together. It is never a screen, a function, a stored record or a menu item.

P2  Every use case returns an observable result.

If you cannot name the actor and state the result the use case delivers to them, it is not a use case. Value to a party you can name is the test of whether it exists at all.

P3  Anchor the model at the level of a single sitting.

The backbone of the model is the set of goals a primary actor completes without leaving the task. The levels above and below exist only to group that set or to factor it.

P4  Keep intent above mechanism.

Describe what the actor intends and what the system guarantees — not the user interface, the technology or the internal design. This keeps the requirement stable while the solution is still open.

P5  Requirements are a conversation, written down as narrative.

Use cases are a shared account that the business and the delivery team both read. Readability wins: a complete and readable model with imperfections in it is worth more than a perfect one nobody reads.

P6  Make scope an explicit decision.

The system boundary, the list of what is in and what is out, and the design scope are chosen deliberately and recorded. None of them is left implicit.

P7  Work across the whole system first, and add detail on demand.

Establish every actor and every goal across the system before writing any one use case in depth. Add precision only where value and risk justify it.

P8  Slice for delivery, and keep the model current.

Enterprise systems are built and delivered in thin, end-to-end slices of use cases. The model is an asset maintained across the life of the system, not a document written once and filed.

## 4  Boundary and design scope

*Twenty-two rules follow, in seven groups. Each carries an identifier for use in reviews and in traceability. Where a rule states an obligation that is discharged on an individual use case rather than on the model, it says what must be recorded and stops there; how that use case is written is governed elsewhere.*

M1  Name the system under discussion before listing anything else, and draw exactly one boundary.

Decide and name the system whose behaviour you are modelling. Draw one boundary. Place every actor outside it and every use case inside it. An unstated boundary is the root cause of most modelling disputes: two people arguing about whether something is a use case are usually arguing about where the boundary runs.

M2  Separate the business model from the system model.

Decide whether the boundary is the organisation or the software. If it is the organisation, the actors are customers and partners and the use cases are business goals. If it is the software, the actors include users and other systems. Keep the two in separate models. Organisation-level goals and software interactions drawn on one diagram cannot both be read correctly, and no note explaining the mixture survives the second reader.

M3  Record the design scope on the model.

State whether the treatment is black-box — external behaviour only — or white-box, and at what level the model sits. The same real-world activity yields different use cases at different scopes, so the reader must be told which of them they are looking at.

## 5  Actors

![Figure 3](figures/SDD-05/SDD-05_fig03.png)

*Figure 3 — One boundary, with the kinds of actor outside it. Everything the system does sits inside; everything with behaviour towards it sits outside.*

M4  Identify actors by the role played, not by the person or the job title.

An actor is a role. One person may play several roles, and one role may be played by many people or by another system. Model *Approver*, not *Senior Manager*. A model built on job titles has to be redrawn whenever the organisation is reorganised, and says nothing that survives it.

M5  Classify every actor as primary, supporting or offstage.

Mark which actor's goal each use case serves, which external parties the system calls on to reach that goal, and which interested parties never interact but must still be satisfied. A missing supporting or offstage actor is one of the commonest sources of missed requirements, because nothing in the flows draws attention to its absence.

M6  Include actors that are not people, and actors that are clocks.

Other systems, devices and a scheduler are actors whenever they are external sources or destinations of data, or whenever they start behaviour. A use case that begins on a schedule has time as its primary actor, and saying so is what stops it being attributed to whichever person happens to watch it run.

## 6  Identifying use cases and setting granularity

Keep the backbone at the level of a single sitting. The set of use cases at that level is the model's backbone; summary and subfunction use cases exist only to group it or to factor it. A model whose backbone is thinner than half its rows has been decomposed rather than designed.

M7  Derive use cases from actor goals.

For every actor, ask what goals that actor needs the system to fulfil. List the goals first. Use cases follow from goals — never from screens, and never from the records the system happens to store.

M8  Name use cases as an active verb and an object.

Name each use case from the primary actor's viewpoint, in the words the business uses: *Submit a return*, *Reconcile a payment*. Never a noun on its own, never a screen name, and never a create-read-update-delete operation on a field. As you name it, state to yourself the outcome the name stands for — “assign an open task to an active user”, not “assign task”. If the outcome carries a condition the name hides, that condition is a business rule (M18) or a precondition, and it has not yet been recorded.

M9  Set granularity with three tests, and require all three.

A use case at the level of a single sitting must pass every one of them.

The manager's test. Would the actor's manager agree that completing this was a worthwhile use of part of the working day?

The single business event test. One actor, in one place, in one sitting, started by a business event, delivering a measurable result and leaving the data consistent.

The size test. A real use case has several steps — typically three to ten pages when written out in full.

*Log in* and *Enter an item code* fail all three. *Process a sale* passes all three.

M10  Do not decompose functionally.

A use case is not a function call. Resist one use case per button, one per stored record and one per step. Two hundred use cases for a system of modest size is a sign of decomposition, not of thoroughness, and it is only visible when the set is read as a whole — which is why it is a rule of the model and not of any one use case.

## 7  Relationships

Relationships are an optimisation for reuse and for clarity. They are not a tool for decomposition. Prefer flows inside a single use case, and reach for a relationship only when it removes genuine duplication or genuine clutter.

![Figure 4](figures/SDD-05/SDD-05_fig04.png)

*Figure 4 — The three relationships, and which way each arrow runs. Reversing the arrow reverses the meaning, which is the commonest error on a use case diagram.*

| Relationship | Use it when | Direction and rule |
|---|---|---|
| «include» | Two or more use cases share the same mandatory behaviour, factored out to avoid writing it twice. | The arrow runs from the base to the included use case. The included behaviour runs every time the base reaches that point. |
| «extend» | Optional or conditional behaviour is inserted at a defined point in a base use case. | The arrow runs from the extension to the base. Name the point and the condition. Use sparingly. |
| Generalisation | A specialised use case genuinely replaces one or more flows of a more general one. | The child is a kind of the parent. Prefer alternative flows within one use case to a family of specialised ones. |

M11  Prefer flows to relationships.

A model that is mostly include and extend arrows has been over-engineered. Keep variation inside a use case as extensions, unless the behaviour is genuinely reused, in which case use include, or genuinely optional at a defined point, in which case use extend.

## 8  Structure, completeness and traceability

### 8.1  Packaging and the survey

M12  Group large models into packages that hold together.

For a large system, group use cases by actor, by business area or subsystem, or by product capability. Keep each package internally cohesive and loosely coupled to the others, and give each one an overview a reader can start from.

M13  Maintain a use case survey.

Keep one index listing, for every use case: its identifier, its name, its primary actor, its level, a one-line description, its priority, its status, and the requirements it realises. Set priority by business value, risk and architectural significance. This index is what planning and coverage are read from. Generate it from the use cases' record headers (M19) rather than maintaining it separately, so that it cannot come to disagree with the use cases it indexes.

### 8.2  Completeness and traceability

![Figure 5](figures/SDD-05/SDD-05_fig05.png)

*Figure 5 — Completeness is a two-way condition. Coverage that closes in only one direction leaves either unmodelled goals or unrecorded scope, and neither is visible from the other side.*

M14  Define completeness explicitly.

The model is complete when every primary actor's goals are covered, every supporting actor is called by at least one use case, no use case lacks a primary actor or an observable result, and the set reconciles against the business processes or capabilities it supports. Completeness is also checked inward: every stated requirement is realised by at least one use case, every use case realises at least one stated requirement (M16), and every entity a use case refers to is defined in the entity model (M17).

![Figure 6](figures/SDD-05/SDD-05_fig06.png)

*Figure 6 — The trace is carried on the artefacts themselves. A matrix kept beside them is a second copy, and the second copy is the one that goes stale.*

M15  Establish traceability in both directions.

Trace business goals and processes to use cases, use cases to slices, and slices to acceptance tests and design realisations — and back again. Every requirement should reach at least one use case, and every use case should reach at least one business goal. Carry the trace as stable identifiers recorded on the artefacts themselves (M16, M18, M19) rather than in a matrix maintained beside the model, so that it can be checked at any moment and cannot decay without anyone noticing. The trace runs from a business goal to its use case, from the use case to the set of screens that serves it, governed by the standard for the screens (SDD-07), from that set to the increment that builds it, and from the increment to its acceptance tests and to what is built.

M16  Close the requirement binding in both directions.

Every stated functional requirement, non-functional requirement and constraint is realised by at least one use case, and every use case realises at least one of them. The list a goal binds to is the register of requirements as published under the standard for the requirements catalogue (SDD-02), rule RQR-27 — one named list, in one place, in a form a program reads — and the binding names entries by their identifiers in that list and by nothing else. A use case that satisfies no stated requirement is either scope creep or an unrecorded requirement. A requirement realised by no use case is either out of scope or a goal nobody has modelled. Both are findings against the model, and both are visible only because the binding is carried on the use cases themselves rather than in a matrix beside them.

### 8.3  The vocabulary the model uses

M17  Name exactly one entity model as the model's vocabulary.

The model names one entity model, and every domain concept its use cases refer to is defined there. What that entity model contains, and how it is judged, is governed by the standard for entity models; this standard neither restates it nor adds to it. What this standard requires is only that there is one, that it is named, that every entity a use case refers to appears in it, and that no field structure appears in any flow. Terms that are not entities — role names, statuses, process names and terms drawn from legislation — are carried by the glossary (M22), which the entity model supplements and does not replace.

M22  Maintain one glossary beside the entity model.

The model carries one glossary and uses one term for each concept across the whole of it. For a domain concept, the entity model supplies that term; the glossary carries everything the entity model does not. Two names for one thing anywhere in the model is a finding, and it can only be found by reading across use cases, never inside a single one.

Where the boundary between them runs. If the system keeps a record of it, the entity model names it. Otherwise the glossary does.

### 8.4  The rules the model depends on

M18  Keep one register of business rules.

Every business rule the model depends on is written once in a register, given a stable identifier, and written short, self-contained and free of the flow that invokes it. A rule stated only inside the prose of one flow is invisible to every other use case, to the reviewer, and to anything derived downstream. The review question is whether the rule can be pointed at directly; if it cannot, it is not yet a rule. Every registered rule is cited by at least one use case and asserted by at least one test. A rule that nothing cites is either dead or a rule nobody is maintaining.

## 9  The model record

![Figure 7](figures/SDD-05/SDD-05_fig07.png)

*Figure 7 — The record header is the only part written by hand. The survey and the automatic checks are produced from it, which is what stops them disagreeing with it.*

M19  Hold the model as versioned text, and generate what can be generated.

Hold the model as text under version control, beside the design and the code it governs: one file for each use case; diagrams stored as diagram source rather than as pictures, so that a change to one is reviewable and the picture can be regenerated from the use case list; and the survey (M13) generated from the use cases' record headers rather than kept by hand. The completeness and traceability conditions of M14, M15 and M16 then become checkable automatically instead of by inspection. Section 9.1 lists what each use case must carry for this to work.

M20  Change the model before changing the system.

When behaviour must change, amend and review the affected use case first, and only then bring the realisation into line with it. Review the specification and the realisation together and in that order — is the specified behaviour correct, and only then does the realisation match it — so that an implementation is never approved before the behaviour it implements has been agreed. Synchronise realisations to the changed behaviour rather than regenerating them from the whole use case, so that the change in the system is the size of the change in the model and can be reviewed as such.

### 9.1  The record header

These are the fields the model requires every use case to carry. The survey is generated from them, and the model's completeness and traceability checks run against them.

| Field | What to record |
|---|---|
| Identifier | The stable reference by which the model knows this use case (M13). |
| Name | An active verb and an object, from the primary actor's viewpoint (M8). |
| Level | Summary, user goal or subfunction (section 2.3). |
| Primary actor | The actor whose goal this use case satisfies (M5). |
| Status and priority | Draft, reviewed or baselined; priority set by value and risk (M13). |
| Format | Brief, outline, or written out in full — the decision recorded under M21. |
| Linked requirements | The identifiers of the requirements, non-functional requirements and constraints this use case realises (M16). |
| Entities | The entities of the named entity model that this use case reads or changes, by name only (M17). |
| Business rules | The identifiers of the registered rules that govern this use case (M18). |
| Relationships | Include, extend or generalisation, with the extension points named (M11). |

This header is the model's record of the use case. It is written once for each use case and it is read by machine: the survey is generated from it, and the model's checks run against it. A value that appears both here and in the prose of the use case will come to disagree with itself within a quarter. State it here only.

## 10  Slicing and delivery

A use case model is not a one-off artefact. It is the spine along which the system is planned, built, tested and maintained, and this section explains how the same model is delivered under an iterative, an incremental or a plan-driven approach.

### 10.1  Cut the use cases into slices

![Figure 8](figures/SDD-05/SDD-05_fig08.png)

*Figure 8 — A slice is one or a few flows taken from a use case, running end to end. Slices, not use cases, are what a team commits to.*

A whole use case is usually too large to build in one increment, so split it into slices. Each slice is one or a few related flows — at minimum the main success scenario, later the valuable extensions — forming an independently deliverable, end-to-end, testable thread of value. Every slice must run through the system from one end to the other so that it delivers something that can be demonstrated, and every slice carries its own acceptance tests.

Slices move through a small set of states that make readiness visible: scoped, prepared, analysed, implemented, verified. On a board these become columns; in a time-boxed iteration they populate the backlog; in a plan-driven programme they give fine-grained scope control inside the phases.

### 10.2  Order by value and risk, and deliver in increments

Order slices by business value, risk and architectural significance, and deliver in increments that each build on the last. The main success scenario of a high-value use case is usually an early slice; expensive or rare extensions are deferred until their value justifies them. This is how the model stays aligned with delivery: what is most valuable is specified in most detail first, and lower-value variation is left named but thin until it is needed.

M21  Decide across the model which use cases are written out in full, and in what order.

Write out in full the significant ten to thirty per cent first, rather than everything at once, and order the rest by business value, risk and architectural significance. Record the decision on the survey row as the use case's format and status, so that the model states what is written, what is deliberately thin, and what is simply not done yet. A model in which every row has been written out in full before the priorities are known has committed its effort before it knew where the risk lay.

### 10.3  How much of the model is detailed, and when

Early, while the shape of the system is being settled, name close to all the use cases and write out in full only the architecturally significant few. As the architecture is proved, detail perhaps thirty to seventy per cent of them, using those to drive and test the architecture. During construction, build the remaining slices with only minor refinement. In service and maintenance, keep the model current: every change request and every defect links back to the affected slice for impact assessment. The survey carries which use cases are written out and which are not (M21).

How much written detail a given use case then needs is a choice made about that use case and not about the model, and it is governed separately.

## 11  The review

Run this before a use case model is baselined, and before any slice cut from it enters delivery. The model's owner runs it with the architecture authority. A model passes only when every applicable line is satisfied. An unsatisfied line is a finding with a named owner, not an exception to be waved through.

| Rules | Checkpoint | Passed |
|---|---|---|
| M1–M3 | The system is named, exactly one boundary is drawn, and the design scope — organisation or software, black-box or white-box — is stated. | ☐ |
| M4–M6 | Actors are roles, each classified as primary, supporting or offstage; actors that are systems, devices or clocks are included. | ☐ |
| M7–M8 | Every use case derives from an actor goal and is named as an active verb and an object. | ☐ |
| M9 | Every use case at the level of a single sitting passes the manager's test, the single business event test and the size test. | ☐ |
| M10 | No functional decomposition — no use case per button, per field or per stored record. | ☐ |
| M9–M11 | Include, extend and generalisation are used only for genuine reuse or genuine optionality, and sparingly. | ☐ |
| M12–M13 | Large models are grouped into packages that hold together, and a survey exists carrying priority and status. | ☐ |
| M14 | Every primary actor's goals are covered; every supporting actor is called; nothing lacks a primary actor or a result. | ☐ |
| M15 | The trace runs in both directions: business goal, use case, slice, test. | ☐ |
| M16 | Every use case records the requirements it realises, and every stated requirement is realised by at least one use case. | ☐ |
| M17 | One entity model is named; every entity a use case refers to is defined in it; no field structure appears in any flow. | ☐ |
| M22 | One glossary exists beside the entity model, carrying the terms the entity model does not, with one term for each concept. | ☐ |
| M18 | Every business rule the model depends on is registered with an identifier and cited, not stated only inside prose. | ☐ |
| M21 | The survey states which use cases are written out in full and which are not, and the order was set by value, risk and architectural significance. | ☐ |
| M19–M20 | The model is held as versioned text with record headers and a generated survey, and behaviour changes were specified and agreed before they were realised. | ☐ |

What this review does not do. Every line above tests a structural property — that something is named, recorded, classified, bound or covered. None of them asks whether what is recorded is *true*. Section 14 states the limit that leaves.

## 12  The ways models go wrong

These are the failures that recur, with the rule that corrects each one. They are the failures found by reading across the model, by or for the person accountable for it. The failures found inside a single use case are a separate catalogue and are governed separately.

| The failure | How it shows | The rule that corrects it |
|---|---|---|
| Functional decomposition | Dozens or hundreds of tiny use cases; one per button, per field or per stored record. | Model goals at the level of a single sitting, and apply the three granularity tests (M8–M10). |
| Logging in treated as a use case | Standalone use cases with no measurable result; they fail the manager's test. | Fold it into a precondition, or include it as a subfunction. Keep the backbone at the level of a single sitting (M9, P2). |
| Too many relationships | The diagram is a web of dashed arrows and no reader can follow it. | Prefer flows to relationships; factor out only genuine reuse or genuine optionality (M11). |
| Inconsistent vocabulary | The same concept carries several different names across use cases. | Maintain one glossary and one term for each concept across the model (M22). |
| Detailing everything at once | Every use case written out in full before the priorities are known. | Work across the whole system first; decide which use cases are written out and in what order (M21, P7). |
| No primary actor, or no result | A use case names no actor, or no outcome anyone can observe. | Every use case has a primary actor and returns a result (P1, P2, M14). |
| A model nobody maintains | The model is written once, then drifts away from what is built. | Slice, deliver and maintain the model across the life of the system (P8, section 10). |
| A use case bound to nothing | A use case realising no stated requirement, or a requirement realised by no use case. | Bind use cases to requirements and check both directions (M16, M14). |
| Undefined vocabulary | Terms used in flows that are defined nowhere; the same entity described differently in two use cases. | One entity model, named by the model and referred to by name (M17). |
| A rule buried in prose | A constraint that matters is stated inside one sentence of one flow, and other use cases contradict it. | Register every rule once, with a stable identifier (M18). |
| Traceability kept beside the model | The trace exists only in a separately maintained matrix, and no longer matches the model. | Carry the trace on the artefacts as identifiers, and generate the survey (M15, M19). |

## 13  A worked model

The example is a revenue administration system: a system that receives tax returns, assesses them, collects what is owed and pursues what is not. It is used here because it has several human actors, a system that acts on a calendar rather than on a person's instruction, behaviour shared between use cases, and behaviour that runs only under a condition — which between them exercise most of the rules above.

What follows is the model: the boundary, the actor catalogue, the goals at their levels, the packages and the relationships. It carries no flows, no guarantees and no acceptance tests, because none of those belong to the model.

![Figure 9](figures/SDD-05/SDD-05_fig09.png)

*Figure 9 — The worked model. Every actor sits outside the boundary and is classified; every use case sits inside it and is named as an active verb and an object; shared behaviour is factored with include and conditional behaviour with extend.*

### 13.1  The actor catalogue

Every actor is a role, sits outside the boundary and is classified (M4, M5). All five kinds that M5 and M6 require are present.

| Actor | Kind | Is it a person? | The goal it brings, or the service it gives |
|---|---|---|---|
| Taxpayer | Primary | Yes | To file for an open period and receive proof of it |
| Tax officer | Primary | Yes | To assess a filed return and settle the liability |
| Filing calendar | Primary | No — a clock | To open and close filing periods on the statutory calendar |
| Identity service | Supporting | No — a system | Confirms who is in front of the system |
| Payment service | Supporting | No — a system | Settles a payment the system requests |
| Taxpayer register | Supporting | No — a system | Holds the taxpayer and obligation data the system reads |
| Audit function | Offstage | Yes | Never interacts; requires a complete and tamper-evident record |

### 13.2  The survey, at record-header precision

The model's record of each use case. The survey is generated from these rows rather than kept beside them (M13, M19). All three levels are present.

| Identifier | Name | Level | Primary actor | Package | Relationships |
|---|---|---|---|---|---|
| UC-01 | Resolve liability for a year | Summary | Filing calendar | Filing | — |
| UC-02 | Submit a return | User goal | Taxpayer | Filing | includes UC-06, UC-07, UC-08; extended by UC-04 |
| UC-03 | Assess a return | User goal | Tax officer | Filing | extended by UC-05 |
| UC-04 | Pay the balance | User goal | Taxpayer | Debt | extends UC-02 when a balance is due |
| UC-05 | Raise a debt case | User goal | Tax officer | Debt | extends UC-03 when the balance is unpaid |
| UC-06 | Authenticate | Subfunction | Taxpayer | Filing | included by UC-02 |
| UC-07 | Validate return data | Subfunction | Taxpayer | Filing | included by UC-02 |
| UC-08 | Calculate liability | Subfunction | Taxpayer | Filing | included by UC-02 |

The remaining fields of the record header — status and priority, format, linked requirements, entities and business rules — are carried on every row in a real model. They are left out here only to keep the example readable, and leaving them out is not a licence: M16, M17, M18 and M21 are all lines of the review.

### 13.3  Reading the model against the rules

The boundary is named and every actor sits outside it (M1). Actors are roles, and each is classified; a clock and an offstage party are both present (M4–M6). Every use case is named as an active verb and an object (M8). The use cases sit in two packages, each internally cohesive and loosely coupled to the other (M12). All three levels are present (section 2.3). Shared mandatory behaviour is factored with include and conditional behaviour with extend, each used once and each naming its condition (M11). Nothing is decomposed to the level of a screen or a field (M10).

One thing in this example is worth arguing about rather than admiring, and it is left in for that reason. Four of the eight rows sit at the level of a single sitting — exactly on the line section 6 draws, and no better than it. In a model this small the right review question is whether *Validate return data* and *Calculate liability* are genuinely reused by a second use case, or were factored out of a single flow from habit. If the second, they are decomposition (M10), and the backbone is thinner than it looks.

## 14  The questions this standard does not answer

A standard that hides what it cannot yet say is worse than one that names it. Three things are unsettled.

### Whether what is recorded is true

The review in section 11 is a check of one kind only: every line in it is a structural property that a reader — and in time a program — can confirm by looking. Whether the boundary is drawn in the right place, whether two use cases with different names are the same goal, whether the survey's priorities are the priorities the business would recognise, whether a completeness claim is true rather than merely present — none of these is asked by any line of section 11, and every one of them decides whether a model is any good. Until a second half of the review exists that names the judgements only a person can make, a model that passes section 11 has been shown to be well formed, and nothing more. A reviewer should read the result that way.

### When a model is finished

No published test says when a use case model is complete in the sense of being finished, as opposed to complete in the sense M14 defines. This standard does not offer one. What it offers is that every question it asks has an answer, or carries a written reason for having none — which is a test a model can actually be put to, and which makes two models comparable question by question even when they differ.

### How thin a backbone is too thin

Section 6 states that a model whose backbone is thinner than half its rows has been decomposed rather than designed. That threshold is a judgement rather than a measurement. No published study establishes it, and a model close to the line should be argued about rather than passed or failed on the arithmetic.

## 15  Where these rules come from

This standard draws its model-level discipline and its relationship semantics from the object-modelling tradition and its published process guidance; its granularity and naming discipline from the use case writing literature; and its slicing, delivery and maintenance discipline from the incremental delivery literature. Where those traditions differ, this document states one rule and treats the alternatives as commentary. Each source below is the primary reference for the discipline noted against it.

- Alistair Cockburn, *Writing Effective Use Cases*. The goal levels and the discipline of keeping a model at one altitude (section 2.3).
- Ivar Jacobson and others, *Use-Case 2.0*. Slices, the states a slice moves through, incremental delivery and scaling to enterprise work (section 10).
- Craig Larman, *Applying UML and Patterns*, the use case chapter. The kinds of actor (section 2.2) and the three granularity tests (M9).
- The Rational Unified Process, *Find Actors and Use Cases* and *Structure the Use-Case Model*. Identifying actors and use cases, packaging, the survey and prioritisation (sections 5, 6 and 8.1).
- The Object Management Group's UML specification, and the published guides to the use case diagram. The notation, and the semantics of include, extend and generalisation (section 7).
- Simon Martinelli, *Spec-Driven Development*. The entity model as shared vocabulary (M17), business rules as identified artefacts (M18), traceability carried on the artefacts (M15, M16), and the model held under version control as the point at which change is controlled (M19, M20).
The catalogue in section 12 draws on the recurring failures reported in the practitioner literature on use case quality rather than on any single source.
