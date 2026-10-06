# SDD-01 · Specification-Driven Development

*This copy is carried by sdd-kit, the SDD method's skills for the service design course. It keeps the edition stated below; where the edition drew an example from the method's author's own client work, this copy carries an example set in Progressa in its place and says so where it does.*

*How a written requirement becomes working software, and how anyone can tell that nothing was lost on the way*

Field | Value
--- | ---
Document | SDD-01 · Specification-Driven Development. The method: which documents are written, in what order, who writes each of them, what is checked when one is handed to the next, and when the work is finished. It carried the code S2C-04 until version 3.1.
Version and standing | Version 3.5 of 29 September 2026 · in force. It replaces version 3.4 of 29 September 2026, which is kept in x_archive/. What changed: four of the standards it rests on — the entity model, the shared registers, the software architecture document and the application model — came into force by the owner's ruling of 29 September 2026 (rulings/2026-09-29-four-draft-standards-in-force.yaml), and what this document says of the standing of the standards, in sections 4, 16 and 17, appendices A and B and figure 2, now says so, with the condition the same ruling sets for the other three; and figure 2 says of the application model that an assistant writes it and a person reviews it and approves it or asks for adjustments, by the owner's ruling of the same day (rulings/2026-09-29-what-an-assistant-writes-a-person-approves.yaml). No rule changed: section 14 still carries nineteen standing rules, and no numbered section was added, removed or renumbered. An internal standard of FiscalAdmin OÜ, owned and approved by Aare Lapõnin, for the work of FiscalAdmin OÜ. There is no external approver and none is required.
Who writes the document it governs | Nobody. This document governs the other eleven that appendix B names, and each of those says who writes the document it in turn governs.
Who reads it | The analyst, the architect and the assistant who begin a piece of work, and the reviewer who decides whether it may be built from.
When it is written | Before any of the work it describes, and read again whenever one of the eleven documents beneath it changes.
Rules | None of its own. It carries nineteen standing rules in section 14 and names the rule families of the eleven documents it rests on in appendix B.
What it does not cover | Section 1 names each boundary. It does not repeat any of the eleven; where one of them settles something, this document says so and stops.
Author | FiscalAdmin OÜ · Aare Lapõnin

---

**Contents**

**1** What this document is for

**2** The problem a method has to solve

**3** The three rules everything else follows from

**4** The twelve things that carry the work

**5** The order in which they are written

**6** How completeness is measured

**7** What one use case contains when it is written out

**8** What the screens add, and how anyone can see that three documents agree

**9** Where this method departs from the standards, and why

**10** What is checked at each handover

**11** The review

**12** When a specification is good enough

**13** How a correction travels

**14** The rules that always hold

**15** How progress is measured

**16** What this method does not claim

**17** What is still missing

**A** The words used in this document

**B** The standards this method rests on

## 1  What this document is for

*This is the working manual for turning what a customer asks for into software that does it. It is written to be read by somebody who was not present when any of it was decided.*

One word first. A goal is one thing that one person wants the system to do for them, complete in itself — registering a taxpayer, writing off a debt, answering an objection. The standards call the same thing a use case. The two words mean the same thing, and this document uses the plainer one.

A large piece of public administration software is not built by one person in one sitting. It passes through several hands, and each pair of hands writes something down for the next pair. This document says which things are written down, who writes each one, in what order, and — most importantly — what is checked at each point where one document is handed to the next.

It does not tell you how to design well. It tells you what has to exist, what may not be left unsaid, and how anybody looking at the work can tell whether it is finished. Those are different questions, and only the second one can be settled by a rule.

#### What this document does not cover

It stops at the point where a complete, checked description of the application exists. Everything after that point — generating the software, putting it on a server, testing it there — is settled elsewhere and is unchanged by anything written here.

It also does not repeat the standards it relies on. Eleven other documents govern individual pieces of the work: how to lay out the whole set of goals, how to write one of them, how to write down what the customer asked for, how to describe the records a system keeps, what makes two of those records the same thing and who writes each fact of one, what the application is built on, how to work out the screens of one goal and show them to a person, what a person sees, the rules an assistant generates screens under, how a person picks a value, finds a record, moves a record from one state to the next and acts on a record across every goal the application model carries, and how the application is finally described to the machine that builds it. A twelfth governs a sector's catalogue of services, which this method does not yet count among the things it names. Those documents are listed at the end. Where one of them settles something, this document says so and stops.

## 2  The problem a method has to solve

*Good documents still produce disappointing software, and the reason is not a shortage of writing.*

A requirements document says what somebody wants. It does not say how the system will behave. Between those two things there is a wide space, and every question in that space has to be answered by somebody before the software can run. What states can a case be in? Exactly which figures go into this total, and as of what date? What happens when the system we depend on is unavailable? What makes two records the same record?

If the method does not force those questions to be asked, they are answered anyway — quietly, by whoever happens to be at the keyboard on the day, and without a record. The work still gets delivered. It simply does not do what anybody agreed it would do, and nobody can point at the moment where the two parted company.

An intention travels through three handovers on its way from somebody's head to a running service, and it can be lost at each one in a different way.

![Figure 1. Three ways an intention is lost, and what this method puts in the way of each.](figures/SDD-01/SDD-01_fig01.png)

*Figure 1. Three ways an intention is lost, and what this method puts in the way of each.*

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>The one sentence this document exists to make true</strong></p>
<p>A silence that is named, owned and counted is a specification. A silence that has been filled in with a plausible answer is a fault dressed as a specification.</p></td>
</tr>
</tbody>
</table>

## 3  The three rules everything else follows from

*The rest of this document is machinery. These three rules are the reasons the machinery has the shape it has.*

#### The first rule: what a person reviews must be a story

There is more than one way to write down a complete specification, and they are not equally useful. A list of eighty separate decisions can be complete and still be impossible to review, because a reader cannot see what is missing from a list. A story can be reviewed, because absence is visible in a story: a step with no response, a person who never appears again, a way things can go wrong that is never mentioned.

So the form is fixed, and it is fixed for the sake of the reader rather than for the convenience of the machine. The part a program reads is taken from the story, and never the other way round.

#### The second rule: completeness is measured against something the design did not write

If the list of things that must be covered is drawn up from the design itself, then measuring the design against it will always show that the design is complete. This is the most common way a project reports full coverage of a system that is missing half of what it needed.

The answer is that the two lists used to measure completeness are both written by a separate act, before the design exists. Section 6 explains them.

#### The third rule: at least one check must end by looking at the running system

Most checks compare one document with another. Those checks are necessary and they share one blind spot: a set of documents can agree with each other perfectly and describe something that does not work. So in every piece of work, at least one check has to end somewhere other than in a document — a query that finds a column on a real server, a test that runs against a live system, a task that a person actually finishes.

## 4  The twelve things that carry the work

*Ten are written once and afterwards amended. Two nobody writes at all. None of them is ever edited from below.*

Twelve things carry the work. They are listed here in the order they come into existence, which is also the order in which each one feeds the next; the twelfth, the interaction design, added in version 3.3, is numbered 8a, so that nothing already numbered is renumbered. The mark on the right says one thing only: whether a written standard governs that thing. One of the twelve is not this organisation’s to govern. **All eleven of the rest have a standard**, which became true of ten of them on 1 September 2026 and was not true in version 3.1 of this document. Until then two rows were governed only in part: the second named three things and only the entity model had a standard, its glossary and its register of business rules having none; and the fifth named five things and only one of them was governed. The two standards that covered those rows were extended rather than joined by new ones, so the set was then still nine documents. **Two of the standards behind these rows are drafts** — the requirements catalogue and the interaction design — **and the mark does not say otherwise. It says a standard exists, not that it is in force.**

The mark deliberately says nothing about how confident a standard is in itself, and the reason to keep it that way has grown stronger. Of the nine standards this method rested on on 1 September 2026, five stated on their own covers that they were drafts, and three of those five said further that nobody unfamiliar with the work had yet been asked to follow them. Four said nothing at all about their own standing, two of those four saying nothing about a version or a date either. Marking the honest ones differently from the silent ones would reward silence. What each standard says about itself belongs in section 16, and is there.

The rule that binds all twelve, and the one most often broken when time is short: a fault is corrected in the document that owns the fact, and everything below it is produced again. Nobody corrects the output of a machine; they correct what the machine was given and run it again. The same principle applies ten times over in this chain.

![Figure 2. The twelve things, who writes each of them, which two nobody writes, and how firmly each is governed.](figures/SDD-01/SDD-01_fig02.png)

*Figure 2. The twelve things, who writes each of them, which two nobody writes, and how firmly each is governed.*

Two of the twelve are halves of the same thing, and it is worth seeing them together. The second is what the system keeps — the records, and what one record of each kind means, together with the glossary that carries the words the model does not and the register of the business rules it cannot express. The fifth is everything else a use case draws on but does not own: the catalogue of events the system publishes and consumes, the catalogue of computations, which code lists are shared with other systems and which belong here, the vocabulary a screen may be built from, and the three things the standard for the second one explicitly leaves out — who owns each fact, what states a record moves through, and what makes a record unique. **Both halves now have a standard.** The first is the standard for the entity model, which took the glossary and the register of business rules into itself on 1 September 2026. The second is the standard for identity, ownership and state, which on the same day took the two catalogues and the assignment of shared code lists and was retitled because its old title no longer described it. The one subject of the fifth that neither took is the vocabulary a screen may be built from, and it is governed where it always belonged: the enterprise standard for what a person sees constrains it and hands its drawing to a pattern library, and that library exists. **What is thin there is the library, not the governance, and section 17 says so rather than calling for a standard nobody has asked for.**

Both halves have to exist before the sixth is written, because the sixth draws on them. A use case that needs a record, an event, a computation or a screen pattern that the groundwork does not have may not invent one: it records the gap, gives it an owner, and stops.

The sixth is the one most of the work goes into. It is one use case, written out in full, and there is one of them for each goal that the model of goals decided to write out — which is not necessarily every goal the model names.

#### The seventh and the eighth, which are new

The seventh is the set of screens of that one goal: which screens there are, which numbered step or which variation of the story each of them serves, what appears on each one, where every value on it came from, and what the person is allowed to change. It is written beside the use case it serves, by whoever wrote the use case or by somebody reading it beside them, and it is worked out by walking the story and never by walking the records the system keeps. It has an owner of its own, a written procedure for changing it, and a review of its own, which is why it cannot be a section inside something else.

The eighth is the walk-through: the same screens as pages that open in an ordinary web browser, in which a person can follow the acts that take them from one screen to the next. Nobody writes it. It is produced from the seventh, it adds nothing to it, and a fault found in it is corrected in the seventh and the walk-through is produced again. It is the first thing in this order that software makes rather than a person writes, and it is not the last.

#### The interaction design, which is the twelfth

The interaction design is written once for each increment of the application model, after the owner of the work has accepted the description and the screens of every goal that increment carries, and before the model is written. One analyst writes it, reading the screens of those goals together, and settles once for the application how a person picks a coded value, finds one record among many, moves a record from one state to the next, and acts on a record. It is written across goals rather than for one, by a different hand and at a different moment from the screens, and the owner accepts it on its own, which is why it is a document of its own and not a section of the screens or of the application model. It is numbered 8a, after the walk-through, so that nothing already numbered is renumbered. The standard that governs it, SDD-11 · The Interaction Design, is a draft, version 0.1 of 25 September 2026, and it comes into force once the education demonstration application is ready, by the owner's ruling of 29 September 2026.

#### A word about the three at the end

The application model is the point at which the specification stops being written for people and becomes something a program reads. It is the last thing a person edits at all, and it is written only from an interaction design the owner has accepted, which it names. On either side of it sit the two things nobody writes: the walk-through, produced from the screens, and the working application at the end, generated from the model. Neither is ever touched by hand, and if something about either of them is wrong, the fault is above it.

#### Where each of the twelve lives, and what each standard's build produces

When a specification is begun, the delivery kit — the set of programs that builds a working application from its description — makes one folder for each of the twelve things. The kit's register, the one file its programs read to learn what the twelve are and what governs each of them, renders the name of each folder, and the table gives the folder each thing lives in, as the register renders it. The folders a person opens are therefore this standard's rendering and not a file beside it: a folder renamed in the register is a change to this table, and the two are changed together.

| **In figure 2** | **The thing**                                              | **The folder it lives in** |
|-----------------|------------------------------------------------------------|----------------------------|
| 0               | The customer's own documents                               | 00_customer_documents      |
| 1               | The register of requirements                               | 01_requirements_register   |
| 2               | The entity model, its glossary and its register of rules   | 02_entity_model            |
| 3               | The use case model                                         | 03_use_case_model          |
| 4               | The software architecture specification                    | 04_architecture            |
| 5               | The rest of the shared groundwork                          | 05_shared_groundwork       |
| 6               | One use case, written out in full                          | 06_use_cases               |
| 7               | The screens of that use case                               | 07_screens                 |
| 8               | The walk-through a person clicks through                   | 08_walkthrough             |
| 8a              | The interaction design, across the goals the model carries | 08a_interaction_design     |
| 9               | The application model                                      | 09_application_model       |
| 10              | The working application                                    | 10_application             |

**Each standard's build produces its checklist and its template.** When the document of a standard is built, the same build reads the document it has just made and writes the standard's checklist, which carries the standard's rules and its review questions in the document's own words, and the template of each thing the standard has a person write, with the record header the standard fixes already laid out. Neither is ever typed. A fault found in either is corrected in the standard, or in the program that reads it, and the build is run again. The delivery kit holds both, copied unchanged, and its register names them. Two things take their template from the delivery kit itself and not from a build: the application model, whose template is the kit's description of the model's structure, and the interaction design.

## 5  The order in which they are written

*A ratchet, not a one-way march. Any step may be entered again, but only from above.*

The order matters for one reason above all others: two of the documents exist to be the measure of the others, and a measure written after the thing it measures is not a measure. The register of requirements and the first pass of the entity model are therefore written before any goal is named.

![Figure 3. The order of work: what is settled once, what is walked again for every goal, the two things that run alongside, the review the whole of it passes through, and the interaction design that stands between the accepted goals and the application model.](figures/SDD-01/SDD-01_fig03.png)

*Figure 3. The order of work: what is settled once, what is walked again for every goal, the two things that run alongside, the review the whole of it passes through, and the interaction design that stands between the accepted goals and the application model.*

#### Why the model of goals comes before the descriptions

Without a document that says how many goals there are, a team writes out the goals it happens to think of. A professional module of this kind carries somewhere between twenty-five and thirty distinct things a person needs to do; a team working from memory typically produces three or four of them and believes it is finished. The model of goals is the document that makes the size of the work visible before the work starts, and it decides which goals are written out in full and in what order.

#### Why the screens come after the use case and not beside it

A screen worked out while the story is still moving is a screen that will be drawn again, and drawing is the most expensive thing in this sequence to repeat. There is a second reason and it is the stronger one. The screens are measured against four lists that the use case itself writes: its numbered steps, its variations, the records it says it reads and separately those it says it changes, and the requirements it realises. A measure written after the thing it measures is not a measure. That is the rule the whole of this order rests on, and it applies here exactly as it applies at the top.

#### Why the walk-through is produced and never drawn

Two pictures kept by hand guarantee that one of them is wrong and that nothing says which. So there is one written record and the walk-through is made from it. Every page of the walk-through carries the version of the record it came from. A walk-through whose version is not the record’s is stale, and nothing is reviewed from it, agreed on it, or built from it until it has been made again.

#### Why the entity model is written in two passes

The first pass names the records the system keeps and defines what each of them means. That is enough to write the model of goals against, and it is written before the goals so that it can serve as a measure of them.

The second pass adds detail — the fields, the exact identity of a record, the relationships — as the goals turn out to need it. Adding detail is allowed at any time. Changing what the first pass already said is a different act: it needs the agreement of whoever owns the model, because other work has been built on it.

#### Why the architecture specification runs alongside

What the application is built on is a different question from what the application is for, and the two are settled by different people at the same time. The architecture specification does not feed the entity model or the goals; it feeds the build. One condition attaches to it: it has to be finished before the application model is written. If it is not, its decisions get taken inside that step by whoever is writing, which is exactly the failure this whole method exists to prevent.

#### Why the interaction design comes after the screens are accepted and before the model

The screens of one goal are worked out beside that goal and reviewed for it alone. Four things a person does are left unsettled by that: how a coded value is picked, how one record among many is found and what choosing it fills, how a record is moved from one state to the next, and what an act carries to the form it opens. Each of them exists only across goals — a list of values is kept once for the application, the moves of one record are made by the acts of several goals, and a form that belongs to a record is opened from several places — so no single set of screens can settle them. If nothing settles them before the application model, they are decided inside that step by whoever writes the model, or by the program that generates the application, by default. That is what happened in the first application built this way, and it is exactly the failure this method exists to prevent.

So once the owner of the work has accepted the description and the screens of every goal an increment of the model will carry, one analyst reads those screens together and writes the interaction design, and the owner accepts it on its own. Only then is the application model written, and it names the accepted document by its path and its checksum. The step is taken again for every increment of the model, and the decisions already accepted are carried forward. The owner’s word of 25 September 2026 is that the step belongs to the method and is not skipped. The delivery kit is to refuse a model that does not name an accepted interaction design; until that refusal is built, the step rests on whoever commissions the model, as section 10 shows.

## 6  How completeness is measured

*Three times, against three lists, and not one of them is written by the people being measured.*

This is the part of the method that is most often skipped and least often understood. Measuring a design against a list the designers wrote themselves is not measurement. It produces a number that always says the same thing.

![Figure 4. The three measures, the list each of them uses, and why no one of them catches another's failure.](figures/SDD-01/SDD-01_fig04.png)

*Figure 4. The three measures, the list each of them uses, and why no one of them catches another's failure.*

The outward measure runs in both directions and both directions matter. A goal that satisfies nothing the customer asked for is either work nobody wanted or a request that was never written down. A request that no goal satisfies is either out of scope or a goal nobody thought of. Neither of those is a matter of opinion; both are findings, and both belong to whoever owns the model of goals.

The downward measure asks a narrower question: does the design mention only things that actually exist? A description that needs a record, an event, a screen pattern or a computation that the shared groundwork does not have may not invent one. It records the gap, gives it an owner, and stops. This single rule is what turns the most common failure of assisted writing — inventing something plausible — into an event that somebody counts.

The third measure works one level lower and applies to one goal at a time. A set of screens is measured against four lists that the use case wrote, earlier, for another purpose. The next section is about it, because it is the reason the screens are worked out at all.

## 7  What one use case contains when it is written out

*One goal, one use case, one document, read by one person in one sitting.*

The description is the centre of the method. Everything above it exists to make it possible to write; the screens are worked out from it, and everything below them is derived. It carries three things a reader can hold in mind at once: a header a program can read, the story of the goal, and the data a developer needs in order to build it without asking anybody anything. What it no longer carries is the screens: those are worked out from it, into a document of their own, and the description names that document and says nothing else about them.

![Figure 5. What one description carries, the two sections that carry the weight, and the one that has left it.](figures/SDD-01/SDD-01_fig05.png)

*Figure 5. What one description carries, the two sections that carry the weight, and the one that has left it.*

#### Why the header is written first

The header is written before any prose. This looks like a formality and is not: naming every record, every event, every setting and the set of screens that serves this goal, before writing a word of explanation, forces each of those decisions to be taken deliberately. It also means every entry in it can be checked against the shared groundwork before the explanation is written, so an invention is caught at the beginning rather than at the end.

#### How long it should be

A simple goal takes ninety to a hundred and twenty lines. A demanding one takes a hundred and eighty to two hundred and twenty. Far above that and the writer is restating the story instead of specifying it; far below and questions are going unanswered.

#### The measure of depth

There is one test, and it is worth remembering in these words: pointing at a section of another document is not an answer, and the developer must not have to work anything out. A description that satisfies that test is deep enough. A description that fails it is not finished, however complete it looks.

## 8  What the screens add, and how anyone can see that three documents agree

*A story can be read. It cannot be checked against itself. This is the section that says why the screens are worked out at all.*

A use case written out in prose can be reviewed, and the first rule this method rests on is the reason: absence is visible in a story. A reader can see that a step has no response, that a person appears once and never again, that a way of going wrong is never mentioned.

What a reader cannot see in prose is whether the story and the records agree. A use case may say that the officer records the assessment and never say which record that writes. It may claim to realise five requirements and put four of them in front of nobody. It may declare that it reads a record that no person ever sees and that nothing explains. None of those is visible in a story, and every one of them reaches the build.

The screens make it visible, and they make it visible because they are measured against four lists that the screens did not write. All four are in the use case, written earlier, by somebody else, for another purpose: the numbered steps of the main path; the variations, with their kinds and how each of them ends; the records the use case declares it reads and, separately, those it declares it changes; and the requirements it says it realises.

Against each of the four the same question is asked, and there are two admissible answers and no third. Every step and every variation is reached by a screen or by a variation of one, or carries a written reason for needing none. Every record the goal changes is reachable on some screen; every record it reads is shown, or is declared as not needed by this person, with the reason. Every requirement reaches at least one screen, or carries a written reason for reaching none.

A written reason is a proper answer here, and it is often the right one. A requirement may be realised entirely inside a step that shows nobody anything; a constraint may govern how something is stored rather than how it is shown. Neither is a fault. What is not admitted is silence: a requirement the goal says it realises, that no screen serves and that nothing explains, is either a requirement the goal does not in fact realise, or a screen nobody drew.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>What the four lists establish, and what they do not</strong></p>
<p>No figure comes out of this. No percentage is stated and none may be inferred. What the screens contribute is the statement that every step, every variation, every record and every requirement is either reached or reasoned about in writing — and that is a different and more useful thing than a number.</p></td>
</tr>
</tbody>
</table>

One thing on the list is not a list at all, and it is the part no program will ever do. Before any flow was written, the use case named the people with an interest in the goal and what each of them needs protected. The screens are read once against that list, by a person, who writes one sentence against each interest answering one question: can the person doing the work see it? An interest that the system protects, and that the person doing the work never sees and is never told about, is protected by the system and not by them. That may be exactly right, and the sentence records it. What the reading prevents is nobody having asked.

The walk-through is what makes all of it reviewable by somebody who did not write it. A still drawing shows one screen and can say nothing about what follows it, about which act takes the person there, or about where a way of going wrong puts them — and the order in which a person meets the screens is most of what a counterpart is being asked to agree to. When a drawing cannot carry that, it is agreed in conversation instead, and each party leaves the room remembering a different agreement.

## 9  Where this method departs from the standards, and why

*Two rules of the standards this organisation wrote are deliberately not followed. Naming them is the price of relying on the rest.*

Until this version there were four, and two of them are now withdrawn. The description of a goal used to carry the screens, and because it did there was no separate screen document, so the standard governing screens governed nothing here and stood written, checked and unused. Both of those are over. The screens are a document of their own, they are governed, and this method is the first thing in this organisation that instantiates that standard.

Two departures remain, and they are one fact seen twice. A description carries data at field level, and it therefore carries detail that the entity model was meant to hold. Two rules say it should not, and both are sound: they exist so that a requirements document does not settle design questions prematurely, and so that a specification does not have to be rewritten every time an attribute changes.

This method breaks them, on purpose, and the reason is the one it always gave. The description here is not a requirements document; it is the specification a developer builds from, and the field table is where a great many faults live. Keeping it beside the story, in one document that one person reads in one sitting, is judged to prevent more faults than moving it would. That judgement was put again when the screens moved out, and it was made again.

The cost is stated plainly, because a departure that is not declared becomes a departure nobody remembers deciding:

- A description carries data at field level, against the rule that says it should not.

- A description carries the detail that the entity model was meant to hold, against the rule that sends the reader there for it.

Everything the standards say about how large a goal should be, how a goal is named, when a set of goals is complete, and how the screens of a goal are worked out and shown to a person is followed without exception, because those are the rules that keep the whole thing reviewable.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>What follows from a declared departure</strong></p>
<p>Anybody claiming that a document here follows one of these standards must name these two departures as part of the claim. A claim of conformance that does not go rule by rule is not a claim; it is an opinion.</p></td>
</tr>
</tbody>
</table>

One thing stands in the way of finishing that claim, and it is named here rather than left out. A claim is made rule by rule and against one edition of a standard. The standard that governs the screens carries a date and neither a version nor a statement of its own standing, its rules are numbered without a prefix of their own so that a citation to one of them cannot be told from a citation to another standard’s rule of the same number, and a reader picking up the document it replaced cannot tell that it is out of date. Until that is put right, the claim against that standard is owed rather than made, and the gap belongs to whoever owns the standard.

## 10  What is checked at each handover

*The promise is not that the documents are correct. The promise is that nothing crosses a handover in silence.*

There are sixteen points where one document is handed to the next. At each of them something specific is checked, and the honest position is that they are not all checked equally: some are checked by a program that refuses to let the work continue, some are checked in part, and some rest entirely on a person's judgement because no program for them has been written.

![Figure 6. The sixteen handovers, what is checked at each, and how much of that checking a machine actually does.](figures/SDD-01/SDD-01_fig06.png)

*Figure 6. The sixteen handovers, what is checked at each, and how much of that checking a machine actually does.*

The colours are not decoration. A green handover will stop bad work on its own. An amber one will stop some of it. A red one will stop none of it, and the only thing standing there is a person who knows what to look for. Anybody planning a piece of work should read that column before deciding where to spend review time.

Three of the fourteen were new with version 3.0, and all three are red. Nothing mechanical stands between a use case and its screens, between the records the system keeps and what a screen demands of a value, or between a set of screens and the walk-through made from it. Checks for the first of those are specified and some of them are written; not one of them is wired into anything that stops work. Saying so is the whole point of that column, and a layer whose three seams are all red is a real cost of adding it.

Two more were added in version 3.3, with the interaction design. They are numbered after the last, so that no handover is renumbered, although in the order of work they stand between the walk-through and the application model. At the fifteenth, the accepted screens of every goal an increment of the model carries are read together into the interaction design, and a person stands there: the analyst who writes it, measuring its decisions against four listings a program produced from those screens, and the owner who accepts it. At the sixteenth, the accepted interaction design is handed to the application model, which names it by its path and its checksum. That one is meant to stand at a program — the delivery kit refusing, in every mode and with no switch to turn the refusal off, a model that names no accepted interaction design or contradicts the one it names — and it is drawn red because that refusal is not yet built. Until it is, the commission that has the model written names the accepted document among what it reads.

#### The one behaviour that makes any of this worth having

When a check refuses, the refusal is answered, not worked around. The temptation at that moment — to set the finding aside so that the light turns green — is the single behaviour that turns a working method into paperwork. It is named here so that nobody can claim afterwards that they did not know.

## 11  The review

*A step with people in it, not a property a document either has or has not.*

Until this version this method treated review as something a document was good enough to survive. That is no longer tenable, and it was never quite right. A goal now has a use case, a set of screens and a walk-through, and no single document is the thing being reviewed.

So review is a step of the work. It is run before a set of screens is agreed and before anything is built from it, and it has the same four parts every time.

#### Who is in the room

Three people, and none of them is optional. Whoever owns the set of screens. Whoever will build from it. And the counterpart whose work the screens describe — the person from the business side who will have to live with what is agreed. Two of the three can hold a useful conversation and cannot hold this one: the builder and the owner agreeing with each other is how a specification comes to describe something nobody wanted.

#### What they are given beforehand

Everything a program can establish is established before anybody arrives, and it is read rather than discussed: that every step and every variation is reached or reasoned about in writing, that every value says where it came from, that every rule cited resolves in the register, that every reference resolves, and that the walk-through was made from the version of the record now in force. A meeting that spends its time on what a program already knows has spent it badly, and a reviewer who reopens a line a program has already settled is asking the wrong question of the wrong document.

#### What only a person can settle

Whether the screens follow the story, or the story was fitted to the screens afterwards. Whether a value that first enters the organisation at this screen could have come from somewhere the organisation already holds, or whether its justification merely restates what the value is for. Whether a reason given for needing no screen is true, or is the reason somebody reached for. Whether the words are the words the business uses, in the sense the business uses them. Whether anybody who did not write it actually opened the walk-through and followed it, from the first screen to each of its endings. And whether the interests the goal exists to protect are visible to the person who has to protect them.

#### What is recorded afterwards

Every line that was not satisfied, with a name against it, a date, and what would close it. A finding that has an owner does not defeat the work. A failure that nobody wrote down does. Nothing is set aside to let the meeting end, and that is the same rule as everywhere else in this document; it is stated again here because this is the moment it is hardest to keep.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>What passing this review establishes, and what it does not</strong></p>
<p>Everything a program checked establishes that something is named, recorded, resolved or reached. None of it establishes that what is recorded is true. A set of screens that has passed the mechanical half has been shown to be well formed, and nothing more.</p></td>
</tr>
</tbody>
</table>

## 12  When a specification is good enough

*Three tests and one rule about honesty. All four have to hold.*

- The developer test. Somebody can build this without working anything out and without asking anybody anything.

- The review test. The review of the previous section has been held, with the three people in the room, and every line that was not satisfied left it with a name and a date against it.

- The refusal test. Every gap that remains is written down, has somebody's name against it, and is counted.

And the rule about honesty, which is the one that fails first when a deadline is close: an unanswered question that is named, owned and counted is part of a specification. An unanswered question that has been filled in with a plausible answer is a fault, and it is a worse fault than the blank would have been, because the blank was visible.

## 13  How a correction travels

*Always upward to the document that owns the fact, then downward again by producing everything below it afresh.*

Seven kinds of correction arise, and each has one place it is allowed to land.

| **What was found**                                                | **Where the correction goes**                                                                                                                                                                                                                                                                                       |
|-------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Something is wrong on the running system                          | Into the description of the goal, and everything below it is produced again.                                                                                                                                                                                                                                        |
| Something is wrong on a screen                                    | Into the set of screens, and the walk-through is made again from it. Never into the walk-through, and never into what was built.                                                                                                                                                                                    |
| The behaviour itself has to change                                | Into the use case first, where it is agreed. Then the screens are brought into line. Then the walk-through is made again. Only then is what has been built changed. The order matters more here than anywhere else, because a screen is what people notice first and therefore what they ask to have changed first. |
| Something is wrong in the application model                       | Into the description or the set of screens that asserted it, not into the model.                                                                                                                                                                                                                                    |
| A description needs something the shared groundwork does not have | Into the groundwork, as a finding with an owner. Never into the description as an invention.                                                                                                                                                                                                                        |
| Something is wrong in what the software generated                 | Into the pattern, the generator or the model — in that order of preference. Never into the generated file.                                                                                                                                                                                                          |
| A standard changes                                                | Every document governed by it is read again against the changed rule, or the version it was written against is recorded and the debt is named. Silence is not a third option.                                                                                                                                       |

The last of the seven matters more than it looks. Eleven standards now govern this work, four of them carrying a date of 29 September 2026 on their own first pages, and changes to them have been proposed and not signed, five to the standard for the model of goals alone, as section 17 records. A standard that is altered underneath a body of documents that nobody reads again turns every claim about those documents quietly false.

## 14  The rules that always hold

*Nineteen. They are short because they are meant to be remembered, not looked up.*

1.  What software generated is never edited by hand.

2.  A correction lands in the document that owns the fact, never in the document where it was noticed.

3.  The screens of a goal are worked out by walking the story, and never by walking the records the system keeps.

4.  When behaviour changes, the story changes first, then the screens, then what a person is shown, and only then what was built.

5.  A gap is a finding with an owner, never something invented locally. This is the most important rule of all when an assistant is doing the writing, because inventing something plausible is the thing an assistant does best.

6.  Every figure that comes from policy is a setting with a marked default. A rate, a threshold, a period or a limit written directly into the design is a fault however sensible the number looks.

7.  Never invent a figure in order to keep a flow moving.

8.  A decision that has been taken is cited, never argued again. A decision that is genuinely open is flagged, never quietly answered.

9.  Where two signed documents contradict each other, that is a decision for a person, not a defect to be tidied away.

10. Gaps stay open and counted. They are never signed off to turn a light green.

11. A refusal is answered, not worked around.

12. A description with errors outstanding is not finished. Warnings may be carried, with a note saying why.

13. A check is never altered to make its number look better.

14. Where the work stands is read from the work, never remembered.

15. An empty column is information. It is usually the most useful thing on the page.

16. Not applicable, with a stated reason, is a proper answer, and is sometimes the most useful one.

17. A goal that claims an authority names where that authority comes from. An authority claimed without a source is an invention in uniform.

18. A claim that something follows a standard is made rule by rule, or it is not a claim.

19. The application model is written only from an interaction design the owner has accepted.

## 15  How progress is measured

*Eight measures. Each of them can be read from the work itself rather than reported by the people doing it.*

| **Measure**                                      | **What it tells you**                                                                                                                                                                                                                                                         |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Errors in the descriptions                       | Whether the descriptions obey the rules of their own subject. Read from the checks, not from a report.                                                                                                                                                                        |
| Findings raised                                  | Whether people are challenging the shared groundwork instead of quietly working around it. A count of zero is a bad sign, not a good one.                                                                                                                                     |
| Settings still holding a placeholder             | How many policy figures are still guesses rather than answers.                                                                                                                                                                                                                |
| Gaps recorded at the model step                  | Whether the step that turns descriptions into the application model is being honest. An empty list here is suspicious.                                                                                                                                                        |
| Checks that end in an observation                | How many pieces of the work have been proved against a running system rather than against another document.                                                                                                                                                                   |
| Screens specified against screens built          | Whether what was built is what was specified. It reads the set of screens of each goal. For goals written out before the screens became a document of their own, it still reads the screen section of the description, and it will read two shapes for as long as both exist. |
| Walk-throughs made from the record now in force  | Whether the thing the counterpart looked at is the thing the builder will receive. A count smaller than the number of screen sets means somebody has agreed to something stale.                                                                                               |
| Conformance claimed against conformance assessed | For each document: how many rules it claims to follow, how many were actually checked one by one, and which failed and to whom they belong.                                                                                                                                   |

The last measure is the newest and the most uncomfortable. Eight of the eleven standards this method relies on define conformance the same way: a finding that has an owner does not defeat a claim, but a failure that was never written down does. The other three define it not at all: the application model, the standard for what a person sees, and the ruleset an assistant generates screens under. The entity model, which had no conformance clause of any kind when this measure was first written, has carried one since 1 September 2026. By the definition the eight share, no document of this organisation's work yet carries a conformance claim — the only files of that kind are worked examples, written over example documents to show the form — and this one does not either: section 9 declares two departures, which is a smaller thing.

## 16  What this method does not claim

*A method that hides its own limits teaches the wrong lesson to everybody who reads it.*

- It does not claim the standards it rests on work well together. No analyst has yet been handed all of them and asked to produce a description from them. Until that has happened, the joins between them are a proposal rather than a finding.

- It does not claim that two of the eleven standards it rests on, the register of requirements and the interaction design, are more than drafts, and it does not claim that the four the owner's ruling of 29 September 2026 brought into force — the entity model, the shared registers, the software architecture document and the application model — have been tested by use: they came into force with their rules as they stood. Three of the eleven — the entity model, the register of requirements, and the shared registers — each say on their own face that until somebody unfamiliar with the work has been given the document and asked to do the work from it, everything in it is a proposal about how an inexperienced practitioner works rather than a finding about how one does. The fourth, the architecture specification, states a different untested test: whether a specification written to it can be told from one written without it. The fifth, the interaction design, states that none of its rules has yet been used by anybody who did not write it. Four of them go further and set their rules against this organisation’s own bar for adopting one: the register of requirements states that not one of its twenty-five rules meets it; the entity model, that thirty-nine of its fifty-six rules cleared it and seventeen did not; the shared registers, that twenty-nine of its forty-seven rules cleared it and eighteen did not — six are stated once by a discipline outside this estate and did not clear on that alone, eight were tested against the bar and failed it, and four were never tested against it; and the interaction design, that none of its twenty-nine rules has yet been searched against it, so that every one of them is to be read as not tested.

- It does not claim that any existing body of work conforms to anything. No document produced so far carries a conformance claim made rule by rule.

- It does not claim the order in section 5 is the only defensible one. It claims that the order does not measure the design against itself, and that its weakest join rests on a point the relevant standard itself calls unsettled.

- It does not claim that everything is checked. Section 10 shows exactly which handovers are checked by a machine and which are not, and several of the most important ones are not.

- It does not claim that the work written before this version has been brought into the shape described here. Goals written out earlier still carry their screens inside them. This method now describes two shapes at once, and that was decided deliberately rather than overlooked.

- It does not claim to be cheap. Twelve things means nine places a correction can land, and the ratchet in section 5 is the only thing keeping that from becoming permission to patch wherever the fault was noticed.

## 17  What is still missing

*What is missing is named here with an owner each, and nothing on this list is written in passing.*

| **What is missing**                                                                      | **What it would have to settle**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A pattern library with a claim about what it covers                                      | The vocabulary a screen may be built from is governed — the enterprise standard for what a person sees constrains it and names the pattern library that draws it, and that library exists. What the library does not do is say what it covers. It is at version 0, holds eight patterns, and a reader cannot tell from it whether a control they need is absent because it was decided against or because nobody has got to it yet. This is the only thing the extension of 1 September 2026 could not finish, and it is a quantity of work rather than a missing document.                                                                                                                                                                                                                                                                                                                                                                                       |
| A convention for what a standard says about itself                                       | A version, a date, a plain statement of standing — draft, in review, or in force — and what the document supersedes. Measured on the nine shipped documents on 1 September 2026: all nine state a version, a date and a standing, which was not true a week ago and is the result of the rebuild that gave every one of them the same eight lines on its first page. Six also state what they supersede, or that they supersede nothing; a seventh names its predecessor without saying it supersedes it; two say nothing about supersession at all. So the form has converged on three of its four parts by practice, and none of it is written down anywhere as a convention a tenth document could be held to. That is what remains: not the covers, which are now nearly uniform, but the absence of a stated rule that made them so. This is still the cheapest gap on this list to close, and it is the one blocking the conformance claim in section 9.    |
| A prefix for the rules of the standard that governs the screens                          | That standard numbers its thirty-two rules 1 to 32 with no prefix of its own, while every other rule-bearing standard in the set prefixes its rules — M, U, EM, IOS, RQR, ARC, and the families of the enterprise standard for what a person sees. A citation to its rule 8 cannot be told from a citation to any other standard's rule 8; and the enterprise standard for what a person sees still cites four rules of the document it replaced, by identifiers the replacing document does not carry.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| A standard for accessibility, and one for delivery in more than one language             | Neither exists as a standard of its own. Both have a partial home: the enterprise standard for what a person sees carries an accessibility family that adopts a published external baseline by reference, a rule requiring that no user-facing text is written into the build, and a second rule requiring translations to be kept in parity. What neither has is a home in the register of requirements. A screen cites the quality requirements that bind what a person sees, and the register is where such a requirement belongs — but a citation is only as good as the register it cites, and where the register carries neither, a set of screens satisfies the obligation in silence. The standard for the screens says in its own §1 that it makes no accessibility claim and no language claim, and declines to invent one. What would close it is a standard for each, or a ruling that the register must carry both for every goal a person performs. |
| Nobody has read either of the two extended standards who had not seen the subject before | The glossary, the register of business rules, the catalogue of events, the catalogue of computations and the assignment of shared code lists all gained rules on 1 September 2026, and both documents carrying them are in force by the owner's ruling of 29 September 2026. Neither has been given to a reader unfamiliar with its subject and neither has been used to write the thing it governs. Until that happens both are proposals about how the work is done rather than findings about how it is done, and each says so on its own face.                                                                                                                                                                                                                                                                                                                                                                                                                |

One further thing is open. Five changes to the standard that governs the model of goals have been proposed and are not signed. Two of them alter the wording of rules this document relies on. Until they are settled, this document is written against those rules as they currently stand, and if they are signed, what is written here about them is read again.

## Appendix A The words used in this document

*Every term that carries weight, defined once, in the sense used here.*

| **Word**               | **What it means here**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A goal, or a use case  | One thing that one person wants the system to do for them, complete in itself. Not a screen, not a button, not a step. The two words mean the same thing; the standards say use case and this document says goal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| A description          | The document that specifies one goal completely: the story, the data, and what happens when things fail. It names the set of screens that serves the goal and says nothing else about them. It is one use case, written out in full. There is one for every goal the model of goals decided to write out, and not necessarily one for every goal in the model.                                                                                                                                                                                                                                                                                                                                                                                                   |
| A set of screens       | The written statement of what a person sees while reaching one goal: which screens there are, which numbered step or which variation each of them serves, what appears on each one, where every value came from, and what the person may change. There is one for each goal a person completes in one sitting, and it has an owner of its own.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| The walk-through       | The screens as pages that open in an ordinary web browser, in which the acts that take a person from one screen to the next can be followed. It is made from the set of screens and is never written or corrected by hand.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| The review             | The step at which a set of screens is agreed: three named people in a room, everything a program can establish established beforehand, everything only a person can settle asked out loud, and every unsatisfied line recorded with an owner and a date.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| The shared groundwork  | Everything a use case draws on but does not own. It has two halves. One is the entity model — the records the system keeps — and it has a standard, which since 1 September 2026 also carries the glossary and the register of business rules. The other is the catalogue of events, the catalogue of computations, the shared code lists, the vocabulary of screens, and who owns each fact, what states a record moves through and what makes a record unique. Of that half, all but the vocabulary of screens are in one standard, which took the two catalogues and the code lists on the same day. The vocabulary of screens is governed by the enterprise standard for what a person sees, which constrains it and hands its drawing to a pattern library. |
| The entity model       | The written statement of which records the system keeps, what one record of each kind means, what identifies it, and how the records relate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| The model of goals     | The single statement of what the whole system is for: one boundary, the people outside it, every goal they need, and how those goals group together. There is one per system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| The interaction design | The statement, made once for each increment of the application model, of how a person picks a coded value, finds one record among many, moves a record from one state to the next and acts on a record, across every goal the model carries. It is written after the owner of the work has accepted those goals and before the model is written, the owner accepts it on its own, and the model names it.                                                                                                                                                                                                                                                                                                                                                        |
| The application model  | The point at which the description stops being written for people and becomes something a program reads and builds from.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| A finding              | A gap, recorded, with somebody's name against it. The only permitted response to something the groundwork does not have.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| A departure            | A rule of a governing standard that this method deliberately does not follow, declared together with the reason.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| A conformance claim    | A statement that a document follows a standard, made rule by rule. Anything less is not a claim.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| A refusal              | A check stopping the work because something is wrong. It is answered, never worked around.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| A reporting check      | A check that runs, prints what it finds and does not stop the work — used where stopping the work would be premature. It always states what would turn it into a refusal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Appendix B The standards this method rests on

*Eleven documents govern parts of this work and are not repeated here. Where one of them settles something, this document says so and stops. Two of the eleven say on their own faces that they are drafts; that is stated on each row below, beside the edition the row names, rather than left to the reader to find. A twelfth standard of the set is named after the table, with the reason it is not yet one of them.*

| **Standard**                                | **Rules**                                | **What it governs**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|---------------------------------------------|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SDD-05 · The Use Case Model                 | M1 to M22                                | The single statement of what a system is for. Discharged once for the whole system, never goal by goal. Version 2.1 of 22 September 2026, in force.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| SDD-06 · One System Use Case                | U1 to U21                                | One goal, written down: the story, every way it can be reached and every way it can fail. Version 1.2 of 29 September 2026, in force.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| SDD-03 · The Entity Model                   | EM-1 to EM-56                            | Which records the system keeps and what each of them means, and — since version 0.2 — the glossary kept beside it and the register of business rules, both required by SDD-05 and described by nothing before then, and, since version 0.3, what the system depends on, whoever keeps it. Version 1.0 of 29 September 2026, in force by the owner's ruling of that day, its rules as version 0.6 stated them. Thirty-nine of its fifty-six rules cleared this organisation’s bar for adopting a rule and seventeen did not.                                                                                         |
| SDD-02 · The Requirements Catalogue         | RQR-3 to RQR-29, twenty-five rules       | What one entry of a register carries, how entries are identified, how priority and status are expressed, and what the register publishes. Version 0.3 of 29 September 2026, a draft for review, and it states that not one of its rules meets this organisation's bar for adopting a rule; by the owner's ruling of 29 September 2026 it comes into force once the education demonstration application is ready.                                                                                                                                                                                                    |
| SDD-04 · The Shared Registers               | IOS-1 to IOS-47                          | What makes two rows the same thing, who writes each fact, and the states a record moves through, together with the catalogue of events, the catalogue of computations, the assignment of shared code lists and, since version 0.3, the catalogue of settings. It covers the whole of the part of the shared groundwork the entity model standard leaves out. Version 1.0 of 29 September 2026, in force by the owner's ruling of that day, its rules as version 0.4 stated them; it was titled Identity, Ownership and State until 1 September 2026. Twenty-nine of its rules cleared the bar and eighteen did not. |
| SDD-08 · The Software Architecture Document | ARC-1 to ARC-31                          | What an application is built on: the platform binding, the components it switches on, the machinery that runs its processes, what crosses its boundaries, and the bespoke-code budget. Version 1.0 of 29 September 2026, in force by the owner's ruling of that day, its rules as version 0.1 stated them.                                                                                                                                                                                                                                                                                                          |
| SDD-07 · The Screens of a Use Case          | 1 to 32, unprefixed                      | What a person sees while reaching one goal, and the walk-through made from it. Instantiated by this method — see section 4. Its rules carry no prefix of their own, which is the gap named in section 17. Version 1.3 of 29 September 2026, in force.                                                                                                                                                                                                                                                                                                                                                               |
| UX-01 · The Enterprise UX Standard          | families of rules                        | How a screen behaves, what it may show and what it must earn the right to show. Version 1.3 of 13 July 2026, with two of its rules amended on the owner's word on 25 September 2026.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| UX-02 · The Generation Ruleset              | the rules of UX-01, by their identifiers | The rules an assistant generates screens under: UX-01 condensed into instructions, with the analysis the assistant writes before any screen and the review it passes before it hands one over. Version 1.4 of 28 September 2026, in force.                                                                                                                                                                                                                                                                                                                                                                          |
| SDD-11 · The Interaction Design             | IXD-1 to IXD-29                          | How a person picks a value, finds a record, moves a state and acts on a record, across every goal an application model carries: settled once from the screens the owner has accepted, and accepted by the owner before the model is written. Version 0.1 of 25 September 2026, a draft for review; by the owner's ruling of 29 September 2026 it comes into force once the education demonstration application is ready.                                                                                                                                                                                            |
| SDD-09 · The Application Model              | —                                        | How the application is finally described to the software that builds it. Version 1.2 of 29 September 2026, in force by the owner's ruling of that day; version 1.1, which it supersedes, called itself a draft for customer review.                                                                                                                                                                                                                                                                                                                                                                                 |

One standard of the set is not a row of this table. SDD-10 · The Sector Services Catalogue, SSC-1 to SSC-20, governs a sector's catalogue of services: one boundary around the several bodies of a sector, the customers outside it, every service the bodies owe or perform, what each rests on and its state today, written once for a sector before any service of it is specified. Version 0.1 of 25 September 2026, a draft for review; it changes no rule of SDD-05. This method does not yet count that catalogue among its twelve things, and it does not rest on SDD-10 until SDD-10 comes into force, which, by the owner's ruling of 29 September 2026, it does once the education demonstration application is ready.

Measured on the nine shipped documents on 1 September 2026, by reading the block on each first page: **all nine now state a version, a date and a standing.** That was not true when version 3.1 of this document was written, and the paragraph that stood here described the position before the rebuild of 31 August 2026 gave every one of them the same eight lines. **What they still do not agree on is supersession.** Six state in as many words what they replace or that they replace nothing; a seventh names its predecessor without saying it supersedes it; and two say nothing about it at all. The standard governing the screens, which this paragraph previously reported as the worst case, now states all four. That the set has converged on three of the four and not on the fourth is what section 17 still carries, and it is the one that keeps section 9's claim from being finished.
