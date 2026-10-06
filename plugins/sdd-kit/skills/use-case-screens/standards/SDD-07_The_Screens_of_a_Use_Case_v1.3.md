# SDD-07 · The Screens of a Use Case

*This copy is carried by sdd-kit, the SDD method's skills for the service design course. It keeps the edition stated below; where the edition drew an example from the method's author's own client work, this copy carries an example set in Progressa in its place and says so where it does.*

*What a person sees while reaching one goal, and the clickable walk-through produced from it*

*AN INTERNAL STANDARD  ·  VERSION 1.3  ·  29 SEPTEMBER 2026  ·  IN FORCE*

*Thirty-two rules, a record for each screen, and a review of twelve questions a person answers.*

Field | Value
--- | ---
Document | SDD-07 · The Screens of a Use Case. How the screens of a use case are worked out from it, what the record of one screen must contain, where every value on it comes from, what the set of them must reach, what the clickable walk-through may assert, and who owns the set and changes it. Section 1 says why this method carries a document for it. It carried the code WF-01, and was the file Wireframing_a_Use_Case.docx, until the edition of 31 August 2026.
Version and standing | Version 1.3 · 29 September 2026 · in force. It supersedes version 1.2 of 25 September 2026, which is kept in x_archive/. What changed: a section 16 was added, what the set owes the application model: tables from each thing the record of a set carries to the section of SDD-09 it lands in, saying whether the landing is mechanical or a judgement and what is written down when it cannot land. In section 15, under what produces the walk-through, the delivery kit's program that produces it is named: kit screens walk. No rule was added, removed or renumbered. A claim of conformance made against version 1.2 remains a claim against version 1.2. Version 1.0 superseded WF-01 v3.0 of 30 August 2026, whose rule identifiers W1 to W30 name different rules and must not be cited against this document. An internal standard of FiscalAdmin OÜ, owned and approved by Aare Lapõnin, for the work of FiscalAdmin OÜ.
Who writes the document it governs | Whoever wrote the use case, or somebody reading it beside them. One set of screens for each goal a person completes in one sitting.
Who reads it | The reviewer who decides whether the screens may be built from, and the counterpart asked to agree that this is how the work will be done.
When it is written | After the use case is written out in full, and never beside it.
Rules | 1 to 32, in section 10. They carry no prefix of their own.
What it does not cover | Section 1 names each boundary and where the subject belongs instead.
Author | FiscalAdmin OÜ · Aare Lapõnin

---

## Contents

| Section | What it covers |
|---|---|
| 1  What this standard is for | What a screen set is, the gap it fills, who writes one and what they need beside them, what it does not cover, what it promises, and what it means to claim conformance to it |
| 2  The words this standard uses | The words that are already defined elsewhere, and the six that are defined here |
| 3  The principles | The six statements a rule is read against wherever it does not obviously fit the work in hand |
| 4  Working out the screens | How the numbered steps become screens, how the variations of the flow are placed, and how one screen may serve two use cases |
| 5  What a screen records | The header every screen carries, the discipline about naming, and the two things that never appear in a screen record |
| 6  Where every value comes from | The six questions asked of every value: its origin, whether it points at another record, the governed list it is drawn from, what the screen demands, what this person may see, and how a rule appears |
| 7  What the set must reach | The four lists the set is measured against, none of which it writes itself, and the one reading that no list produces |
| 8  The clickable walk-through | How the walk-through is produced, why it is clicked through rather than looked at, what a person must be able to do in it, what it never carries, and what agreeing to it commits the parties to |
| 9  Holding it, changing it, and who owns it | Identifiers, retirement, the order in which a change is made, and who decides |
| 10  The thirty-two rules | Every rule in one line, in the order they are read, with the number each is cited by |
| 11  What to write down | The questions every screen answers, and the questions the set answers once |
| 12  The review | What a program establishes before the meeting, what only a person can judge, and the limit of what passing establishes |
| 13  The ways screen sets go wrong | The failures that recur, how each of them shows itself, and which rule corrects it |
| 14  A worked example | One use case of a revenue administration system, worked through from beginning to end |
| 15  The questions this standard does not answer | What is unsettled, what the standards beneath this one do not carry, and the questions a reviewer asks that are not rules |
| 16  What it owes the application model | Where each thing the record of a set carries lands in the application model, whether the landing is mechanical or a judgement, and what is written down when it cannot land |

### Figures

Figure 1.  The three standards, what each of them leaves out, and the one thing that is therefore left over.

Figure 2.  Eight numbered steps becoming four screens.

Figure 3.  The two questions that decide what a variation becomes, and why the second one is there.

Figure 4.  A screen that serves two use cases, and why an undeclared second use case is caught from the other side.

Figure 5.  The four answers a value may give to the question of where it came from.

Figure 6.  Why a versioned list has no single answer to which of its values may be offered.

Figure 7.  What the entity model requires, what a screen may demand, and the two ways the relation is got wrong.

Figure 8.  The four things a screen set must reach, and the one reading that no program can perform.

Figure 9.  The written record and the clickable walk-through: which one binds, and which one is produced.

Figure 10.  What a person must be able to do in the walk-through.

Figure 11.  What agreeing to a walk-through commits the parties to, and what it does not.

Figure 12.  The order in which a change is made, and the failure that ignoring it produces.

Figure 13.  The two kinds of rule, and the limit of what passing the review establishes.

## 1  What this standard is for

### What a screen set is

A screen set is the written statement of what a person sees while achieving one goal. It says which screens there are, which numbered step or which variation of the use case each of them serves, what appears on each one, where every value on it came from, and what the person is allowed to change.

There is one screen set for each use case that a person completes in one sitting. Every obligation in this standard is discharged once across that set, or once for each version of it. Where an obligation needs something recorded on an individual screen, it says what must be recorded and stops there.

The set is written first and shown second. What is shown is a clickable walk-through: the screens laid out as pages that open in a web browser, in which a person can follow the acts that take them from one screen to the next. The walk-through is produced from the written record and adds nothing to it. The written record is what this standard governs, and the written record is what a builder eventually receives.

### The gap this standard fills

Three standards already govern the work that comes before this one, and each of them deliberately leaves out the same thing. Understanding that omission is the whole of the reason this standard exists, so it is worth setting out carefully rather than asserting.

The standard for the use case model governs which goals the system serves, how those goals group and relate to one another, who the actors are, and when the set of use cases is complete. It is written about the shape of the model and not about any one piece of behaviour, and it does not describe screens.

The standard for writing one use case governs what the actor is trying to do, step by step, what happens when each step goes wrong, and what still holds when the whole attempt fails. It states in as many words that a use case is not written in terms of screens, and that no field list, data type, format, length or validation rule appears in a flow. The reason it gives is practical: a statement of required behaviour written in terms of screens has to be rewritten every time a screen changes, and in practice it will not be rewritten, so it will simply become untrue.

The standard for the entity model governs what the business keeps a record of, what each record means, and the least that must be true of it. It states that the model expresses the least that must be true, that a particular use of the model may demand more, and that no use of it may demand less. Where an attribute is required because one screen requires it, that requirement belongs to the screen and not to the model.

What a person actually sees, in what order, with what they may change and what they may not, therefore belongs to none of the three. It has to be written down somewhere, and until this standard there was nowhere for it to be written. Each of the three omissions was made in order to keep something out, and none of them says where that something should go instead.

![Figure 1. The three standards, what each of them leaves out, and the one thing that is therefore left over.](figures/SDD-07/SDD-07_fig01.png)

Figure 1.  The three standards, what each of them leaves out, and the one thing that is therefore left over.

### Who specifies a screen set, and what they need beside them

Whoever writes the use case, or someone reading it beside them: an analyst, a designer, or a domain expert with an editor. They do not need to know the other use cases in the model, with one exception, which is a screen shared with a second use case. What they do need is this one use case, written out in full, and four things beside it.

- The use case itself: its header, its main path with the steps numbered, its variations numbered against the steps they leave and marked with their kinds, its preconditions, both its guarantees, and the stakeholders it lists with what each of them needs protected.
- The entity model: the one word for every thing the system keeps a record of, and, for every value the screens will show, whether this system is the authority for it, consumes it from somewhere else, or must not hold it at all.
- The register of business rules: every constraint the behaviour depends on, written once, each with an identifier by which it can be cited.
- The requirement catalogue: the functional requirements, the quality requirements and the constraints that this use case realises.
All four of these belong to the model, and none of them is the specifier's to decide. A specifier who finds that they are deciding one of them — inventing a word for something, settling which requirement a screen realises, writing a business rule into a screen — has found a defect in the model. The correct response is to raise it. It is not to write a screen that covers the gap over, because a screen written to cover a gap hides the gap and keeps it.

### What this standard does not cover

Four things belong elsewhere, and nothing here restates them.

How the model is designed. Which goals become use cases, how large each of them is, how they relate, where the boundary of the system runs, and when the set of them is complete. A use case that appears to be the wrong size is raised as a question about the model; drawing screens for it will not correct it.

How one use case is written. Its flows, its guarantees, its variations, and the test that establishes it is ready to be built from. This standard consumes those and adds nothing to them.

What the entity model contains. A screen names entities and attributes and carries no data structure. What an attribute may hold, what its governed list is and how strongly it is bound to that list all belong to the entity model.

How the screen looks, and how it is built. Arrangement, spacing, colour, typography, and the control that renders a choice. These are matters of design and of the platform, and they are governed separately.

### What this standard promises, and what it does not

It promises that a screen set built to it can be checked. Every condition it states is either something a reader can point at in the record, or something the review asks for by name and records an owner against when it is absent.

It does not promise that two analysts specifying the same use case will produce the same screens. It promises the narrower and more useful thing: that two screen sets built to this standard have answered the same questions about the same use case, so that wherever they differ, the difference can be pointed at and argued about.

It does not promise that passing the review is sufficient. The review establishes structural properties — that something is named, recorded, resolved, bound or reached. It does not establish that what is recorded is true.

And it makes no claim about accessibility and no claim about language. None of the three standards beneath it carries an obligation of either kind, and this standard does not invent one. Both are quality requirements: they belong in the requirement catalogue, are attached to the use case they govern, and are cited on the screen they bind. Where the catalogue carries neither, a screen set can satisfy every line of the review and still be unusable, and section 15 states that plainly rather than leaving it to be discovered.

### What it means to claim conformance

A screen set conforms to this standard when it does four things. It declares the claim. It names the use cases it belongs to and the version of each. It states, rule by rule, how it satisfies each one and where. And it passes the review, with every line that does not pass recorded as a finding against a named owner.

A finding that has an owner does not defeat the claim. A failure that has not been recorded does. The difference matters, because a screen set with three open findings and three named owners is a document somebody is working on, and a screen set with three unrecorded failures is a document nobody can rely on.

A claim made here says nothing about the use case or about the model. Those are reviewed separately, by different people, at different moments. A use case may be sound while a screen set worked out from it is not, and, more often, the reverse.

## 2  The words this standard uses

Almost every word this standard needs is already defined, once, in one of the three standards beneath it, and is not defined again here. A word defined in two places is a word that will come to mean two things, and the standards beneath this one say so about their own vocabulary.

Those standards define: a use case, a scenario, the main path and the variations of it, an actor, a stakeholder and the interests a stakeholder needs protected, the record header, the index of use cases, a business rule and the register that holds it, a quality requirement, the two kinds of variation, the guarantee that holds when the attempt fails and the guarantee that holds when it succeeds, a precondition, a record, an attribute, a relationship, a governed list, the strength with which a value is bound to such a list, what tells one record apart from every other of its kind, and the two clocks — when a fact was true, and when the system was told about it.

Six words are this standard's own, and are defined here and nowhere else. Two of them, the wireframe and the walk-through, are the trade's own names for the things this standard produces, and they are given a plain meaning here so that nobody has to guess at one.

| The word | What it means in this standard |
|---|---|
| A screen | One thing a person sees at one time while working through one use case, and from which they may act. Not a file, not a page template, and not a component that appears inside other screens. |
| A screen set | The whole of the screens of one use case: which they are, which step or variation each of them serves, and the record of each. |
| A value | One thing shown on a screen, or one thing the person supplies there. A value renders one attribute of one record of the entity model, or it is worked out from several of them. |
| The origin of a value | Which of four answers applies to the question of where that value came from. This is a different question from what the person may do with the value, and running the two together is how one of them stops being answered. |
| A wireframe | The drawing of one screen: what is present on it, how those things are grouped, and in what order the person meets them. It asserts nothing about size, colour, typography or spacing, and it says so. |
| The walk-through | The whole set of wireframes as pages that open in a web browser, in which the acts that take a person from one screen to the next can be followed. It is produced from the written record and is never written by hand. |

## 3  The principles

Six statements underlie every rule that follows. Where a rule appears not to fit the use case in front of you, return to these, because they say what the rules are for.

|  | The principle |
|---|---|
| One | The screens follow the use case, and never the other way round. A screen exists because a step or a variation needs one. A screen that nothing in the use case reaches is either a defect in the screen set or a step nobody wrote down, and both of those are worth knowing about. The same statement runs in the other direction as well: the screens are not worked out by walking the records of the entity model and drawing one for each of them. |
| Two | A defect found here is raised where it belongs, and never repaired here. A missing word, a missing rule, a missing variation, a use case that turns out to be two goals: the specifier's whole part is to raise it. |
| Three | Where a value came from is a property of the value, and it is not the same question as who may change it. Whether a figure was declared by the taxpayer, supplied by a register, or worked out by the system decides how far a person may rely on it. A screen that presents all three in the same way is misleading in a way that no rule about editing will catch. |
| Four | The record binds, and the walk-through is produced from it and states what it cannot say. Neither of them is authored twice. A correction is made in the record, and the walk-through is produced again. |
| Five | What the screen demands is the screen's own, and it never travels back into the model. A screen may require more than the model requires. It must never require less, and it must never be the reason the model is tightened. |
| Six | A silence is a question with a named owner, and never a default. Working screens out from a use case produces more unanswered questions than anything else in this sequence of documents, and an unanswered question filled in with a plausible answer is the failure the whole exercise exists to prevent. |

## 4  Working out the screens

### The main path becomes screens

The main path of a use case is a numbered list of steps that alternate between what the actor intends and what the system is responsible for. Almost every action by an actor has a matching response from the system, and that alternation is what the screens follow.

Every step at which the actor supplies, chooses or confirms something is reached by exactly one screen. A step that is wholly the system's responsibility carries a screen only where it presents something the actor must read before the next step can begin. Two consecutive steps may share a screen where the flow puts no response from the system between them; where it does put one, they do not share a screen.

That last judgement is a reading of the flow rather than a property of it, and it is one of the five things in this standard that a person decides and no program can. Two specifiers may read the same flow differently, and the review asks the question out loud for that reason.

![Figure 2. Eight numbered steps becoming four screens. Two steps share a screen only where the flow puts no response from the system between them.](figures/SDD-07/SDD-07_fig02.png)

Figure 2.  Eight numbered steps becoming four screens. Two steps share a screen only where the flow puts no response from the system between them.

### The variations become screens, or variations of screens

A variation of the flow is a condition the system can detect, numbered against the step it leaves. Every one of them is either a variation of a screen already in the set or a screen of its own, and the record says which it is and why. Two questions decide it, asked in this order.

The first question is how the variation ends. There are exactly three answers: it rejoins the main path, it ends in success by another route, or it ends in failure. A variation that rejoins the main path is a variation of the screen at the step it left, because the person is in the same place, being told something different. A variation that ends in success by another route, or that ends in failure, is a variation of the screen the person is on when the condition arises.

The second question is whether the flow moves the person somewhere else. Where it does, the variation is a screen of its own. Where the use case ends without the person seeing anything further, the record says so and no screen is created.

The second question is not decoration. Deciding on the ending alone gives a screen of its own to every failure, and a use case with six failure variations then acquires six screens that a person never navigates to and never leaves. A set of that shape is one nobody can read, and the second question is what prevents it.

![Figure 3. The two questions that decide what a variation becomes, and why the second one is there.](figures/SDD-07/SDD-07_fig03.png)

Figure 3.  The two questions that decide what a variation becomes, and why the second one is there.

What a variation carries follows from its kind, and the two kinds carry different things. A business alternative carries what the actor may do about the condition: the condition stated in the words the use case uses, and either how the actor corrects it or where the flow goes instead. A failure of the system or of its environment carries what still holds despite the failure, stated to the actor in the words of the guarantee.

That second kind is where the guarantee that holds on failure is earned, and it is the part of a screen set most often left thin. A specification that treats every failure as an error having occurred loses the distinction between a failure after which nothing was written and a failure after which something was written and can be retrieved — and those two are not the same thing to the person the guarantee protects.

### One screen set for one use case, and the screen that serves two

A use case that a person completes in one sitting has a screen set. A use case that exists only to group others has none, because it owns no behaviour of its own. A use case factored out of a base use case has none either: its steps are steps of the base at the point where the base uses it, and giving it screens of its own would break one piece of behaviour into several specifications that then drift apart.

One screen may nevertheless serve more than one use case. Where it does, it names every one of them, and against each of them the numbered steps and variations of that use case which it serves. The screen sets of those use cases then overlap, and the screen belongs to both of them.

The reason this matters is not tidiness. The trace in this body of work is carried on the artefacts themselves rather than in a table kept beside them, precisely so that it cannot decay without anyone noticing. A screen that serves two use cases and is recorded against one of them is invisible to the second, and the second use case's account of what its screens reach is then overstated by exactly the steps that screen serves.

![Figure 4. A screen that serves two use cases, and why an undeclared second use case is caught from the other side.](figures/SDD-07/SDD-07_fig04.png)

Figure 4.  A screen that serves two use cases, and why an undeclared second use case is caught from the other side.

The omission is caught from the other side. The second use case's own account shows steps that nothing reaches, and that is visible to anyone reading that use case's set, whether or not the person who specified the first one knew the second existed.

## 5  What a screen records

The set is held as versioned text, beside the use case it serves and under the same version control, so that a change to one can be reviewed against the other. The index of the screens is produced from the screens' own headers rather than kept beside them. A value held in two places will disagree with itself within a quarter, and an index maintained by hand beside the thing it indexes is the commonest example.

### The record header

Every screen carries a header, and every value in that header is stated once, in the header, and never again in the prose below it.

| The line | What is recorded |
|---|---|
| Identifier | The stable reference by which the set knows this screen. |
| Name | What the person is doing here, in the words the business uses, from the actor's point of view. |
| Use cases | Every use case this screen serves, each with its version, and against each of them the numbered steps and variations of that use case which this screen serves. Usually there is one. |
| Primary actor | The actor of the use case. It is not a separate decision. Where a screen serves two use cases, both name the same actor, or the screen is really two screens, because a screen is what one person has in front of them. |
| Entities | The entities of the entity model this screen shows, and separately those it changes, by name only. |
| Requirements realised | The identifiers of the requirements this screen serves, which are a subset of those the use case declares. |
| Business rules cited | The identifiers of the registered rules that govern this screen, which are a subset of those the use case cites. |
| Quality requirements cited | The identifiers of the quality requirements that bind what a person sees here — or none, and none is an answer rather than an empty line. |
| Status and version | Draft, reviewed or baselined, and the version. Those three words are the ones the standards beneath this one use, and no fourth word is used. |

### Naming only what the use case declares

The entities a screen names are a subset of those its use case declares. The requirements it names are a subset of those the use case declares. The business rules it cites are a subset of those the use case cites. A screen never names something its use case does not.

Where a screen appears to need an entity, a requirement or a rule that the use case does not declare, that is a defect in the use case and is raised there. It is a common and useful finding: a step that says the officer records the assessment, and does not say which record that writes, will produce exactly this situation, and the correct outcome is that the use case gains a declaration rather than the screen gaining an undeclared entity.

Every concept a screen names uses the model's one word for it: the entity model's word where the system keeps a record of the thing, and the glossary's word otherwise. No word is invented at this stage. Two words for one thing anywhere across a screen set is a finding against the glossary, and it is a finding that can only be made by reading across the whole set rather than by reading any one screen.

### The two things a screen record never contains

No data structure. No definition, no data type, no length, no format, no list of permitted values and no validation expression appears on a screen or in its record. A reader who needs to know what a named thing may hold looks it up in the entity model. The reason is the one the use case standard gives for the same prohibition: a specification filled with data structure has to be rewritten every time an attribute changes, and it will not be rewritten, so it will become wrong.

And no quality requirement stated here. Where a quality requirement governs what appears on a screen — how quickly, how reliably, in which languages, to what standard of accessibility — the screen cites it by its identifier. It never states one, and it never quantifies one with an adjective such as fast or straightforward, because an adjective in a requirement is a decision that has been hidden rather than taken.

## 6  Where every value comes from

This is the part of the work that neither the use case nor the entity model holds, and it is the reason this standard exists. Six questions are asked of every value, and they are different questions. Answering one of them does not answer any of the others, and the commonest defect in this part of a screen set is an answer to the first question standing in for an answer to the second.

### The first question: where did it come from?

Every value declares exactly one of four answers, and the four are the entity model's own distinctions rather than new ones.

![Figure 5. The four answers a value may give to the question of where it came from, and the one answer that never appears on a screen.](figures/SDD-07/SDD-07_fig05.png)

Figure 5.  The four answers a value may give to the question of where it came from, and the one answer that never appears on a screen.

This system is the authority for it, and holds it. Or it is consumed from an authority elsewhere and is pointed at rather than copied into this system's own records. Or it is worked out from other values this system holds, in which case the screen carries a pointer to where that derivation is written and never the arithmetic itself. Or it enters the organisation at this screen, through this person, at this moment, and this system becomes the authority for it here.

There is a fifth answer that the entity model admits and that never appears on a screen: that this system must not hold the value at all. A screen showing such a value is showing a copy of somebody else's register, which is precisely what that answer exists to prevent.

A value that enters the organisation here carries one further statement: why it can be obtained in no other way. The question it answers is why this cannot be read from a register the organisation already consumes, from a governed list, or from other values the system already holds. It is a sentence, it is recorded against the value, and a person judges at the review whether it answers the question or merely restates what the value is for. A screen most of whose values enter the organisation here is a screen that has not looked for its sources.

### The second question: is it a reference to another record?

Where a value points at another record, the screen record declares two things: that the reference is chosen from a result rather than typed, and which attribute of the referenced record is the thing that tells it apart from every other thing of its kind.

A typed name is not a reference. It is a transcription of something the organisation already holds, made by a person who cannot see what they are transcribing against, and it fails in the two ways transcriptions always fail. It is sometimes wrong. And it is sometimes right, but in a form that nothing can resolve: four words typed into a box are not a taxpayer, they are four words that may identify one taxpayer, or several, or none. What was stored is what every later reading depends on, and if what was stored is a name, every later reading is a search.

This is a different question from the first one, and running the two together is how one of them stops being answered. The first question asks where a value came from. This one asks, of a value that points at a record, how the pointing was captured and what was kept. A value may be consumed from an authority elsewhere and still be typed, and that is exactly the case this obligation exists for.

### The third question: is it drawn from a governed list?

A value drawn from a governed list names the list, names the list's owner, and names how strongly it is bound to it. The entity model admits four strengths: the list must be used; the list must be used wherever it covers the case; the list is recommended; the list is illustrative. Without the strength, nobody can tell whether a value outside the list is an error.

A governed list is versioned, and a value withdrawn from it is retired rather than removed, because deleting a code silently rewrites what older records mean. Two consequences follow, and the second of them is the one most often missed.

The first is that a retired value stays visible on the records that already carry it. A code that vanishes from the screens showing older records does exactly what retirement was meant to prevent: the person reading such a record sees a gap where a decision used to be.

The second is that a versioned list has no single answer to the question of which of its values may be offered. That question has an answer only once a date is chosen, and there are two dates available: when the fact was true, and when the system was told about it. The screen record says which of the two decides, and why that one.

![Figure 6. Why a versioned list has no single answer to the question of which of its values may be offered, and what settles it.](figures/SDD-07/SDD-07_fig06.png)

Figure 6.  Why a versioned list has no single answer to the question of which of its values may be offered, and what settles it.

Neither answer is safe by default, which is why the record must state one. A screen that offers today's list while recording a fact that was true two years ago records a value that the rules did not admit then. A screen that offers a list as it stood two years ago, for a fact being recorded now, refuses a value that is currently correct. Which of those two errors matters depends on what the record is for, and that is a judgement about the value rather than about the screen.

### The fourth question: what does the screen demand?

For every value the screen states two things, and they are two separate decisions. The least it demands: whether the person must supply the value, may supply it, or may only read it. And the most it admits.

![Figure 7. What the entity model requires, what a screen may demand, and the two ways the relation between them is got wrong.](figures/SDD-07/SDD-07_fig07.png)

Figure 7.  What the entity model requires, what a screen may demand, and the two ways the relation between them is got wrong.

What the screen demands never falls below what the entity model requires. A screen that makes optional something the entity model requires does not fail. It succeeds, and it writes a record that the entity model says cannot exist, which is a defect of a particularly quiet kind: nothing reports it, and it is found only by reading the screen's minimum against the model's, value by value.

A screen may legitimately demand more than the entity model requires, and often should. What is recorded in that case is that the demand belongs to this screen and not to the model. The failure this prevents is a common one: an attribute marked as required in the entity model because one screen required it, which is a defect the entity model itself cannot see, because from inside the model the requirement looks like a decision somebody took about the business.

### The fifth question: may this person see it at all?

A screen never shows a value that a registered rule forbids its actor to see. That prohibition is declared once, against the attribute, in the register of rules, and it is never a question asked at each review, because a question asked at thirty reviews will be answered inconsistently at least once, and in a public administration the once may be the one that reaches a court.

Three things are regularly confused with that prohibition, and separating them is what makes it work. Concealing part of a value the person is entitled to see is a matter of presentation. Whether the person needs the value in order to do this step is a judgement about one screen, and it is asked at the review. A prohibition is neither: it is a standing rule of the domain that a class of person must not be shown a value at all.

### The sixth question: how does a cited rule appear?

A rule appears on a screen as its effect, and never as its text. The effect takes one of three forms: a value withheld or shown differently, an act that is unavailable or is refused with a statement of what the person is told, or a warning stated.

The register holds the rule's text once. A screen that restates that text has made a second copy, and the copy that drifts will be the one on the screen, because nobody reviews a screen when a rule changes. What the person meets is the effect, and the effect is also the only part of the rule they need. A citation with no visible effect is a rule the screen has recorded and not applied, and a reader has no way to check such a citation at all.

## 7  What the set must reach

Four lists, and the screen set writes none of them. All four are written by somebody else, at another time, in the use case itself, and that is what makes them worth measuring against. A count taken against a list the same person wrote for the same purpose establishes nothing.

![Figure 8. The four things a screen set must reach, and the one reading that no program can perform.](figures/SDD-07/SDD-07_fig08.png)

Figure 8.  The four things a screen set must reach, and the one reading that no program can perform.

The numbered steps of the main path. The variations, with their kinds and their endings. The entities the use case declares that it reads and, separately, those it declares that it changes. And the requirements the use case realises.

Every step and every variation is reached by a screen or a variation of one, or carries a written reason for needing none. Every entity the use case changes is reachable on some screen. Every entity it reads is shown on some screen, or is declared as not needed by this actor, with the reason. And every requirement reaches at least one screen, or carries a written reason for reaching none.

That last written reason is more often correct than the others, and it is worth saying why. A requirement may be realised entirely inside a step that is wholly the system's responsibility and that presents nothing to anybody. A constraint may govern how something is stored rather than how it is shown. Neither of those is a defect. What is not admitted is silence: a requirement the use case says it realises, that no screen serves and that nothing explains, is either a requirement the use case does not in fact realise, or a screen nobody drew.

None of this calculates a figure. Completeness is defined by the standard for the use case model and is reviewed there. What a screen set contributes to that review is the statement that every step, every variation, every entity and every requirement is either reached or reasoned about. No percentage is stated, and none may be inferred from what is stated.

### And one reading that no list produces

Before any flow was written, the use case listed its stakeholders and what each of them needs protected. Those interests are the test of what completeness means for that use case, and the guarantees are written to satisfy them.

The screen set is read once against that list, by a person, and the reading is recorded with the name of whoever made it and the date. One question is asked of each interest: is it visible to the actor who has to protect it?

An interest that the guarantees protect, that the person doing the work cannot see and is never told about, is protected by the system and not by them. That may be entirely correct, and the reading records it as a sentence rather than raising it as a finding. What the reading prevents is the case where nobody asked. A screen set can satisfy every mechanical line of the review while leaving the one interest that the whole use case exists to protect invisible to the only person in a position to act on it.

## 8  The clickable walk-through

### One record, and the walk-through produced from it

There is one record, and the walk-through is produced from it. Nothing appears in the walk-through that is not in the record. The walk-through is never authored and never corrected by hand: a defect is corrected in the record and the walk-through is produced again.

![Figure 9. The written record and the clickable walk-through: which one binds, and which one is produced.](figures/SDD-07/SDD-07_fig09.png)

Figure 9.  The written record and the clickable walk-through: which one binds, and which one is produced.

Two artefacts kept by hand guarantee that one of them is wrong and that nothing says which. That is the whole of the reason, and it is the reason a great deal of specification work goes stale: the drawing is the thing people look at, so the drawing is the thing that gets corrected, and the written statement quietly stops describing what anyone intends.

### Why the walk-through is clickable, and why a still drawing is not enough

A screen set is shown as a walk-through that can be clicked through, and a set of still drawings is not a form this standard accepts. The reason is not fashion, and it is worth stating plainly.

A still drawing shows one screen at a time. It can say what is present on that screen and how it is grouped, and it can say nothing at all about what follows it, about which act takes the person there, or about where a variation puts them. Yet the order in which a person meets the screens, and what each act does, is the largest part of what a counterpart is being asked to agree to. When the drawings cannot carry it, it is agreed in conversation instead, and each party leaves the meeting remembering a different agreement. The walk-through carries it, so it is agreed from the same thing.

There is a second reason, and it is the more useful one. A still drawing annotated with where every value came from, what the person may change and which rule is in force is unreadable; the annotations crowd out the screen. A clickable page can hold all of it and show it only when the reader asks for it. So the walk-through can carry the part of the record a reader most needs in order to disagree usefully, which a drawing could never carry without ceasing to be a drawing.

### What a person must be able to do in the walk-through

Four things, and a walk-through that fails any of them has not been produced from the record.

![Figure 10. What a person must be able to do in the walk-through.](figures/SDD-07/SDD-07_fig10.png)

Figure 10.  What a person must be able to do in the walk-through.

Reach every screen of the set, starting at the first screen and using only the acts the use case says the person may perform. Follow every act that the use case says takes the person from one screen to another, including the acts that raise a variation. See, for every value, where it came from, what the person may do with it and which rules are in force at that place, without leaving the screen they are on. And read what the walk-through cannot say, and what agreeing to it does and does not commit them to.

The walk-through shows no behaviour the record does not state. Nothing is calculated, nothing is stored, and no value appears that the record does not carry. A walk-through that invents behaviour in order to look convincing is a demonstration, and a demonstration is agreed to as though it were a specification, which is the failure that the whole of this section exists to prevent.

### What the walk-through never carries

A property whose only reader is the walk-through is not a property of the record. A width, a weight, a colour and whether something is collapsed answer no question that the header, the use case or the entity model asks, and none of them belongs in a written specification of what a person sees. Where the walk-through needs such a choice in order to appear on a page at all, the choice is made once for every set produced in the same way, and it is never recorded against a screen.

The test runs in the other direction as well. Where a reader can check something, it belongs in the record and the walk-through shows it. Where a reader cannot check it, the walk-through does not assert it.

### One notation, and what it cannot say

One notation is chosen for a set, stated once, and never mixed with another. A set drawn half as outlines and half as finished screens carries two notations, and a reader cannot tell which parts have been decided.

Every notation has things it cannot express. The set lists what its own notation cannot say, states where each of those things is written instead, and puts that list in the walk-through itself. A reader learns what not to read into a drawing from the drawing, or not at all: a list held in a register beside it is a list that the person being asked to agree has not read.

### What agreeing to a walk-through commits the parties to

A wireframe asserts what is present, how it is grouped and in what order. The walk-through adds which screen follows which, and after what act. It asserts nothing else, and it says so where the person agreeing will read it.

![Figure 11. What agreeing to a walk-through commits the parties to, and what it does not.](figures/SDD-07/SDD-07_fig11.png)

Figure 11.  What agreeing to a walk-through commits the parties to, and what it does not.

This statement is not a disclaimer added to protect the specifier. It is the part of the walk-through that makes agreement worth having: a counterpart who knows exactly what they are agreeing to can agree to it firmly, and a counterpart who does not will later believe they agreed to the wording, the colours and the arrangement they happened to see.

### Where the walk-through is held, and how it is opened

The walk-through is held with the record it was produced from, under the same version control, and is produced again whenever that record changes. It opens in an ordinary web browser, with nothing to install and nothing fetched from anywhere else, so that a counterpart can open it on the machine in front of them, in a building this project does not control, without asking anybody's permission.

Every page of the walk-through carries the identifier and version of the record it was produced from, that record's status in the three words used throughout — draft, reviewed or baselined — and the screen's own identifier together with the use case, step or variation it serves. A page that carries none of this is a picture somebody sent, and a picture somebody sent will be read a year later as though it were current.

## 9  Holding it, changing it, and who owns it

### Identifiers, and what they are for

Every screen and every value carries a stable identifier, and every reference made anywhere in the set resolves: to something declared in the same record, or to an entity or attribute of the entity model, a requirement of the catalogue, a registered rule, or a numbered step or variation of the use case.

The trace is carried as identifiers recorded on the artefacts themselves rather than in a table maintained beside them, so that it can be checked at any moment and cannot decay without anyone noticing. What is required of an identifier is that it is stable. This standard does not require an identifier to be meaningless, and it is worth saying why, because the opposite rule is often assumed. The entity model places identifiers that the system invents, and that mean nothing outside it, at the level of how things are stored; it admits them higher up only where the business itself issues them and shows them to people. The identifiers this body of work uses for its own use cases, rules and requirements all carry meaning by design, and a rule condemning them would have to be argued for rather than assumed.

### Retiring a screen, and writing down what may change

A screen that ceases to exist is retired, and its identifier still resolves — to a record naming what replaced it, or naming the reason nothing did. Nothing is deleted and no identifier is ever reused, because a reused identifier makes every earlier statement about the original screen ambiguous.

Before there is a later version, the set writes down what a later version may change and what it may not. At the least it says which changes require a new identifier and which do not. A change to the use case a screen belongs to, or to the steps or variations it serves, produces a new screen and supersedes the old one, because those are what the screen is. A change to a name, a hint, or the order of values does not. Adding a use case to a screen does not require a new identifier: the screen is the same thing, now known to serve more than was known before. Removing one does, because for that use case the screen has ceased to be what it was.

A change that the written rule does not cover is not classified by judgement at the moment it arises. It goes to the owner, and the written rule is amended.

### The owner, and the order in which things change

The set has a named owner. Who owns it, who may propose a change and who decides are all written down, and a change is a request rather than an edit. A set with no owner is a set whose contradictions nobody resolves.

![Figure 12. The order in which a change is made, and the failure that ignoring it produces.](figures/SDD-07/SDD-07_fig12.png)

Figure 12.  The order in which a change is made, and the failure that ignoring it produces.

When behaviour must change, the use case is amended and reviewed first. Then the screen set is brought into line and reviewed. Then the walk-through is produced again from the amended record. Only then is what has been built brought into line with the screens. The order matters more here than anywhere else in the sequence, because a screen is the thing people notice first and therefore the thing they ask to have changed first.

The screens are brought into line with the change rather than worked out again from the whole use case, so that the change to the screens is the size of the change to the behaviour and can be reviewed as such.

## 10  The thirty-two rules

Every rule in one line, in the order they are read. A rule is cited by its number in a review, in a finding, and in any statement that a screen set conforms to this standard.

Every rule declares which of two kinds it is. A rule that a program reads is one where a program reads the record and establishes something about it. A rule that a person judges is one where no program decides it. There is no third kind, and the division is settled here rather than negotiated at a review: a reviewer who reopens a line that a program has already decided is asking the wrong question of the wrong artefact.

### Working out the screens, and what the set must reach

|  | The rule | Which kind |
|---|---|---|
| 1 | The screens are worked out by walking the use case, and never by walking the entity model. | a person judges it |
| 2 | There is one screen set for each use case that a person completes in one sitting, and none for a use case that merely groups others or is factored out of another. A screen may serve more than one use case, and where it does it names every one of them. | a program reads it |
| 3 | The screens follow the numbered steps of the main path. | a person judges it |
| 4 | Every variation of the flow is either a variation of a screen already in the set or a screen of its own, and the record says which it is and why. | a person judges it |
| 5 | What a variation carries follows from its kind: what the actor may do about the condition, or what still holds despite the failure. | a program reads it |
| 6 | Every numbered step and every variation is reached by a screen or by a variation of one, or carries a written reason for needing none; and every screen serves at least one step or variation. | a program reads it |
| 7 | Every entity the use case declares is reached by the set, or carries a written reason for needing no screen. | a program reads it |
| 8 | Every requirement the use case realises reaches at least one screen, or carries a written reason for reaching none. | a program reads it |
| 9 | The set is read once, by a person, against the interests of the stakeholders the use case lists. | a person judges it |

### What a screen records

|  | The rule | Which kind |
|---|---|---|
| 10 | The set is held as versioned text beside the use case it serves, and the index of screens is produced from the screens' own headers rather than kept beside them. | a program reads it |
| 11 | Every screen carries the record header, and every value in that header is stated once. | a program reads it |
| 12 | A screen names only what its use case declares, and uses the model's own word for everything it names. | a program reads it |
| 13 | A screen names entities and attributes, and carries no data structure of any kind. | a program reads it |
| 14 | A screen cites the quality requirements that bind what a person sees, and states none of its own. | a program reads it |

### Where every value comes from

|  | The rule | Which kind |
|---|---|---|
| 15 | Every value declares exactly one of the four answers to the question of where it came from. | a program reads it |
| 16 | A consumed value names the authority it is consumed from; a value drawn from a governed list names the list, its owner, and how strongly it is bound to it. | a program reads it |
| 17 | A reference to another record is chosen from a result and stored as the thing that tells that record apart. It is never captured by typing. | a program reads it |
| 18 | A value drawn from a governed list is offered as at the clock that decides, and a retired value stays visible on the records that already carry it. | a program reads it |
| 19 | A value that enters the organisation at this screen says why it can be obtained in no other way. | a person judges it |
| 20 | The screen states the least it demands of a value and the most it admits, never demands less than the entity model requires, and records everything it demands above that as its own. | a program reads it |
| 21 | A screen never shows a value that a registered rule forbids its actor to see. | a program reads it |
| 22 | A cited rule appears on a screen as its effect, and never as its text. | a program reads it |

### The clickable walk-through

|  | The rule | Which kind |
|---|---|---|
| 23 | There is one record, and the walk-through is produced from it. It is never authored and never corrected by hand. | a program reads it |
| 24 | Every screen of the set is a page of the walk-through, and every act the use case says takes the person from one screen to another can be followed there, in an ordinary web browser, with nothing to install and nothing fetched from anywhere else. | a program reads it |
| 25 | The walk-through makes each value's origin, what the person may do with it and the rules in force at that place available without leaving the screen, and it shows no behaviour the record does not state. | a program reads it |
| 26 | A property whose only reader is the walk-through is not a property of the record. | a program reads it |
| 27 | One notation is declared and never mixed with another; what that notation cannot say, what agreeing to the walk-through commits the parties to, and the identifier, version and status of the record are carried in the walk-through itself. | a program reads it |

### Identity and change

|  | The rule | Which kind |
|---|---|---|
| 28 | Every screen and every value carries a stable identifier, and every reference resolves. | a program reads it |
| 29 | A screen is superseded and never deleted, and the set writes down what a later version may change before there is a later version. | a program reads it |
| 30 | The set has a named owner and a written change procedure: the use case changes first, then the screens, then the walk-through, and only then what has been built. | a program reads it |

### The review

|  | The rule | Which kind |
|---|---|---|
| 31 | Every rule of this standard declares which of the two kinds it is. | a program reads it |
| 32 | Every rule is answered on a numbered line, against one version, and an unsatisfied line is a finding with a named owner. | a program reads it |

## 11  What to write down

This is the centre of the standard, and the promise it makes is that two specifiers answer the same questions. These are the questions. A screen set is finished when every line below has an answer or carries a written reason for having none.

### For each screen

- The identifier, unique across the set, and the name — what the person is doing here, in the words the business uses.
- The use cases this screen serves, each with its version, and against each of them the numbered steps and variations it serves.
- For a variation: whether it is a variation of a screen already in the set or a screen of its own, and why; and what it carries — what the actor may do about the condition, or what still holds despite the failure.
- The entities shown and, separately, the entities changed, by name only.
- The requirements realised, the business rules cited, and the quality requirements cited, by identifier — or none, and none is an answer rather than an empty line.
- For every value, where it came from, in one of the four ways; the authority, where it is consumed; the list, its owner, the strength of the binding and the clock that decides, where it is drawn from a governed list; that it is chosen and what tells the record apart, where it points at another record; and why it can be obtained no other way, where it enters the organisation here.
- For every value, the least the screen demands and the most it admits, as two decisions — confirmed to be neither below the entity model's minimum nor mistaken for it.
- For every rule cited, where it is cited and what its effect is at that place. No rule text.
- Which act takes the person from this screen to which other screen, and which act raises which variation.
- The status and the version.
A screen that answers only the name line has not been specified. It has been named.

### For the set as a whole

This is the part filled in once, and it is the part most often not filled in at all.

- How the set was worked out, and from what.
- The use case and the version of it the set was worked out from; and which screens, if any, are shared with another use case.
- How many steps and variations there are, which of them are reached, and the written reason wherever one is not.
- The two lists of entities, and what reaches each of them.
- The requirements, and what reaches each of them.
- The stakeholders' interests, with one sentence against each saying whether it is visible to the actor, together with who read them and when.
- How the walk-through is produced from the record, by whom, and when it was last produced.
- Which notation is used, and what that notation cannot say, with where each of those things is written instead.
- The statement of what agreeing to the walk-through commits the parties to, and what it does not.
- What a later version may change and what it may not, written before there is a later version.
- Which screens are retired, and for each of them what replaced it or why nothing did.
- Who owns the set, who may propose a change, and who decides.
- The level of detail the set was worked at, in the specifier's own words, applied consistently across every screen.
- The questions genuinely in dispute, each with a named owner and a date, and never closed by a silent default.

## 12  The review

Run this before a screen set is baselined, and before anything is built from it. The owner of the set runs it with whoever will build from it and with the counterpart whose work the screens describe. A set passes only when every applicable line is satisfied. A line that is not satisfied is a finding with a named owner, and not an exception to be set aside.

The review has two halves. The first is what a program has already established before the meeting: twenty-seven numbered lines, read together and not discussed. Every rule that a program reads is enforced by at least one of them, and every line names the rules it enforces. The second half is what only a person can judge, and it is not the lesser half.

### The twelve questions a person answers

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

![Figure 13. The two kinds of rule, and the limit of what passing the review establishes.](figures/SDD-07/SDD-07_fig13.png)

Figure 13.  The two kinds of rule, and the limit of what passing the review establishes.

### What this review does not do

Every line that a program reads establishes a structural property: that something is named, recorded, resolved, bound or reached. None of them establishes that what is recorded is true. Whether the screens are the screens a person would want, whether a value's stated origin is the origin it really has, whether a reason given for needing no screen is honest — none of these is asked by any mechanical line, and every one of them decides whether a screen set is any good.

A screen set that passes the mechanical half has been shown to be well formed, and nothing more. A reviewer should read the result that way, and the standards for the use case model and for one use case state the same limit about their own reviews.

There is one further limit, and it belongs to this standard alone. There is no line about accessibility and no line about language, because this body of work carries no standard for either. A screen set can satisfy every line above and be unusable by a person who cannot see it, and unreadable by a person who works in the administration's second language. The only route by which either can enter is as a quality requirement in the catalogue, cited on the screen it binds — and only if the catalogue carries one.

What was built is not read by this review, which runs before anything is built. Once something has been built from the set, its owner answers for that reading: whether each screen was built as its record states is recorded against the screen, every difference is a finding with a named owner, and that record is what the standard for the method (SDD-01, section 15) reads as screens specified against screens built. By what act a built screen is set beside its record, this standard does not say.

## 13  The ways screen sets go wrong

These are the failures that recur. Most of them are invisible inside any one screen and are found by reading the set against the use case it was worked out from.

| The failure | How it shows itself | Rules |
|---|---|---|
| The set worked out from nothing | A list of screens that came from a demonstration, a solution concept or a habit. No screen names a step. | 3, 6 |
| The set worked out from the records | One screen for each record, each with create, amend and remove on it, and a step number written against each of them afterwards. | 1 |
| The shared screen recorded once | One screen serving two use cases, recorded against one of them, so that the second use case shows steps reached by nothing. | 2, 6 |
| The set that covers only the successful path | Every screen serves a step of the main path, and nothing serves a variation. | 4, 5 |
| The variation nothing reaches | Six variations in the use case, one in the screen set, and nothing saying what became of the other five. | 6 |
| The screen no step reaches | A screen everyone agrees is needed that no step and no variation reaches. It is either scope added without a decision, or a step nobody wrote down. | 6 |
| The factored-out use case given screens | A screen set for a use case that is factored out of others, so that the same behaviour is specified twice and the two specifications drift. | 2 |
| The value with no stated origin | A figure on a screen with nothing saying whether the person declared it, a register supplied it, or the system worked it out. | 15 |
| The second copy of another register | A value this system keeps that another authority owns, so that two copies drift and the one nobody watches is the one that is wrong. | 16 |
| The typed reference | A record referred to by a name somebody types rather than chooses, so that what was stored identifies nothing and every later reading is a search. | 17 |
| The list read at the wrong moment | A statutory list offered as it stands today against a fact that was true two years ago — or a list as it stood two years ago refusing a value that is correct now. | 18 |
| The value that disappeared | A code retired from a governed list, gone from the screens that show the records carrying it, so that a decision taken then now reads as a gap. | 18 |
| The rule copied onto the screen | The sentence of a registered business rule printed on a screen, drifting from the register within a quarter because nobody reviews a screen when a rule changes. | 22 |
| The screen that relaxes the model | Something the entity model requires, left optional on the screen, so that the screen succeeds in writing records the model says cannot exist. | 20 |
| The model tightened for a screen | An attribute marked as required in the entity model because one screen required it. | 20 |
| The forbidden value on the screen | A figure that a rule of the domain forbids this person to see, on a screen, because nobody remembered the rule. | 21 |
| The entity nothing reaches | An entity the use case declares it changes that no screen puts in front of anybody, because the step said that the officer records the assessment and did not say what that writes. | 7 |
| The requirement that reaches nothing | Five requirements on the use case's header, two of them cited on screens, and silence about the other three. | 8 |
| The set nobody read for the stakeholders | A set that satisfies every mechanical line, in which the interest of the party who never touches the system is protected by the system and invisible to the person who has to protect it. | 9 |
| Data structure written into the screen | Types, lengths, formats and permitted values specified on a screen, so that every change to an attribute means rewriting screens. | 13 |
| The pages that cannot be clicked through | A page for every screen and nothing joining them, so that the one thing a still drawing could never carry is the one thing the walk-through still does not carry. | 24 |
| The walk-through nobody could open | A walk-through that needs something installed, or that fetches what it needs from a place the counterpart cannot reach, so that they agree to what they were told it shows. | 24 |
| The walk-through that invented behaviour | Figures that add up, searches that return results and messages nobody wrote in the record, agreed to as though they had been specified. | 25 |
| The specification written into the drawing | Origins, rules and volumes annotated onto the pages, asserting what the notation cannot express. | 26, 27 |
| The walk-through corrected by hand | A defect corrected in the pages rather than in the record, so that the two now disagree and nothing says which is right. | 23 |
| The walk-through that promised more | A counterpart who agreed to it and expected the layout, the wording and the colours it happened to have. | 27 |
| The invented word | A screen using a second word for a concept that already has one, because the first one did not fit the space. | 12 |
| The set with no owner | Nobody can say who decides a change, so changes are made as edits. | 30 |
| The deleted screen | A screen removed from the set, its identifier used again for something else, and every earlier statement about it now ambiguous. | 29 |
| The review of two versions | A report run against one version and a walk-through produced from another, both of them satisfactory. | 32 |
| The screen changed first | Screens redrawn to match what was built, with the use case amended afterwards or not at all. | 30 |

## 14  A worked example

The example is a revenue administration system, and the use case is one a person completes in a single sitting: submitting a return. The actor is the taxpayer. The main path has eight numbered steps and there are six variations.

### The screens

Eight steps produce four screens. The taxpayer asks to submit a return for the open period, and that is the first screen. The system then proves identity, which is behaviour factored out and shared with several other use cases, so it has no screens of its own and its steps appear here. The system presents the return already filled in as far as it can be, and the taxpayer supplies the figures: those two steps share the second screen, because nothing passes between them. The system checks the return and presents nothing; what it found is what the next step shows. The system shows the liability and the taxpayer confirms the submission: those two share the third screen. The system records the return and issues a confirmation, which the taxpayer must be shown, and that is the fourth screen.

The two places where steps share a screen are not judgements about tidiness. In each case the flow puts no response from the system between the two steps, so the person does not leave the screen.

### The variations

Identity cannot be proved. This ends by reporting failure and the flow moves the person, so it is a screen of its own. What the taxpayer is told is the guarantee that holds on failure: every attempt is recorded, and nothing has been treated as filed.

The register does not answer within the time allowed. This is a failure of the system's environment, and the flow continues, so it is a variation of the second screen. It carries what still holds: the return is presented unfilled, it is stated that the return was not pre-filled, and nothing already entered has been lost.

The checks find errors. This rejoins the main path, so it is a variation of the second screen, with the errors reported against the items they belong to.

A balance is due and is settled now. This is behaviour that extends the use case, and its steps belong to its own set, so no screen is created here and the reason is recorded against the variation.

A balance is due and is not settled. This ends in success, and the person is already looking at the confirmation, so it is a variation of the fourth screen, which states that a balance has been raised.

The service becomes unavailable. This can arise anywhere, so it is a variation of every screen in the set and is recorded once against the set. What the person is told is what still holds: whatever was entered is kept as a draft they can return to.

### One screen, and four of its values

The third screen — confirming the liability and submitting — serves steps six and seven, shows the taxpayer, the filing obligation, the filing period and the return, changes the return, realises two requirements, cites two business rules and one quality requirement, and stands at draft.

| The value | Where it came from | And the rest of what is recorded |
|---|---|---|
| The taxpayer's registered name | Consumed from an authority elsewhere | The authority is the taxpayer register. No governed list. The person may only read it. |
| The filing period | Consumed from an authority elsewhere | The authority is the taxpayer register. It is chosen from the open periods and never typed, and what is stored is the obligation period's identifier rather than the words describing it. The governed list is the statutory filing calendar, owned by the revenue authority, and the list must be used. It is offered as at when the fact was true — the period being filed for — because a calendar amended this year does not retrospectively create or remove periods that were open then. The person may only read it. |
| The figures the taxpayer supplied | They enter the organisation here | The figures are the taxpayer's own declaration and exist nowhere in the organisation before this moment. The person must supply them. |
| The liability | It is worked out | It is derived by a registered rule, which lives in the register beside the entity model. The screen carries a pointer to that rule and not the arithmetic. The person may only read it. |

Everything the entity model would carry about each of these — the definition, the type, the length, the permitted values — is absent, and that absence is the standard working rather than an omission.

### The walk-through of this set

The walk-through has five pages: the four screens and the screen of its own that the failure to prove identity produces. From the first page, asking to submit takes the reader to the second. From the second, supplying figures and continuing takes them to the third; two acts on that same page raise the two variations it carries, and each of them can be entered and left again. From the third, confirming takes them to the fourth, where the variation raising a balance can be entered. The variation for the service becoming unavailable can be raised from every page, because that is what the record says about it.

On every page, each of the four values named above can be asked about without leaving the page, and what comes back is what the record says: where the value came from, what the person may do with it, and the rules in force at that place. Nothing on any page is calculated. The liability shown is the figure the record carries as an example, and the page says so, because a page that quietly computes a liability will be agreed to as though the calculation had been specified.

Each page carries the identifier and version of the screen record, its status of draft, the use case and the steps or variation it serves, and the statement of what agreeing to this walk-through commits the parties to. The whole of it opens from a single place in a browser, with nothing installed.

### What the set reaches

Eight steps and six variations: thirteen of them reached, and one carrying a written reason. Four entities read and one changed. The changed one is reached on three screens. Three of the four read are shown, and the fourth — the status of the obligation itself, consulted only in order to decide whether the period is open — is declared as not needed by the taxpayer, who is told that the period is closed and never sees the status. Two requirements reach the third screen, and a constraint governing how the return is stored carries the reason that it is realised at the final step, which is wholly the system's.

### Two judgements here that a reviewer could reasonably dispute

The second screen carries two steps and two variations, and one of those variations belongs to a step that is not on that screen. It is placed there because the variation resumes at that step, and the person correcting an error is looking at what they entered a moment earlier. That reading is defensible and it is not the only one. A reviewer would be right to ask whether the second screen is now doing three things, and whether the honest answer is that the checking step wants a screen after all. The standard does not settle it, and it is left here for that reason.

And the reading against the stakeholders' interests is where the example stops being comfortable. The stakeholders include the taxpayer, who is the actor, and the revenue authority, which is not. The authority's interest — that a return once filed cannot be silently altered — is protected by the system and is visible to nobody on any of these four screens. That may be entirely correct. The reading records it as a sentence rather than raising it as a finding, which is what is asked for and the whole of what is asked for.

## 15  The questions this standard does not answer

A standard that conceals what it cannot yet say is worse than one that names it. Seven things are unsettled, and the first two are the ones a reviewer should press on.

### There is no standard for accessibility and none for language

Neither the standard for the use case model, nor the standard for one use case, nor the standard for the entity model carries an obligation about accessibility or about delivery in more than one language, and this standard is not entitled to import an outside standard as though it were one of them.

The obligation is real and it currently has nowhere binding to live. A screen cites the quality requirements that bind what a person sees, and the requirement catalogue is where such requirements belong. But a citation is only as good as the catalogue it cites, and where the catalogue carries no requirement about accessibility, a screen set satisfies that obligation in silence. What would close this is a standard for each, or a ruling that the requirement catalogue must carry both for every use case with a human actor.

The walk-through sharpens the question rather than answering it. A set of pages that open in a browser can be examined by the tools that test for accessibility, which a drawing never could, so for the first time the obligation would be testable if it existed. It still does not exist, and a walk-through that could be tested and is not tested is no better than a drawing that could not be.

### Who owns a screen that two use cases share

A screen may serve more than one use case, and every set names an owner. A screen in two sets therefore has two owners, who may rule differently on the same change, and nothing in this standard or beneath it says which of them decides.

The position taken meanwhile is a narrow one. Each set owns its own declaration — what that use case serves of the screen — and a change to anything else on the screen is a change to both sets, and is agreed by both owners or it does not happen. That is a working procedure rather than a rule, because no clause supports one, and it will not survive its first genuine disagreement.

### What tells a record apart is required and is nowhere declared

A reference to another record is stored as the thing that tells that record apart, and the entity model requires every record to have such a thing. Between the two there is a gap: nothing requires the entity model to say which attribute it is.

The consequence is small and exact. A specifier who names the wrong attribute is caught by no program, and a reviewer catches it only by knowing the entity model well enough to supply the answer the model does not state.

### How much detail a screen carries

Whether a screen is specified with six values or sixty is the one question this standard states and does not answer. Until it is settled, the specifier records the level of detail worked at and keeps to it consistently within one set, so that two screens of the same set are at least comparable with each other.

### Where a screen set sits on the trace

The standard for the use case model traces business goals to use cases, use cases to increments of delivery, and those to acceptance tests and to what is built. A set of screens stands on the chain of traceability between the goal it serves and what is built from it: the set names the goal's identifier and version, the application model (SDD-09) names the set it was compiled from by identifier and version, and the use case model's trace (SDD-05) names the link from the goal to its set. Before the application model is written, the accepted sets of every goal it carries are read together by the interaction design (SDD-11), which the model names. A set that no link names is a finding. One consequence is practical: a reviewer reading the index of use cases cannot tell whether a given use case has been taken to the point where a person could look at the work.

### What produces the walk-through, and how much it may decide

The walk-through is required to be produced from the record and never written by hand. The means is the delivery kit's program for it, reached as `kit screens walk` with the record of the set as its argument (`tools/screens_walk.py` in the kit), which produces the walk-through from the whole of the written record and from nothing else. This standard names that program so that a specifier has one means to reach for, and binds no set to it, because the means will change: a set produced by any other means says which, as the last sentence of this section asks. What it does not yet say, and should, is how much the means may decide on its own.

Some choices have to be made somewhere in order for a page to appear at all: where a value sits, how a group is separated from the next, what a control looks like. The record does not carry them, because they are not properties of the record. So they are decided by whatever produces the walk-through, once, for every set produced the same way. That is the right place for them. But nothing currently requires those choices to be written down, or to be the same from one set to the next, and until something does, two sets produced by different means may look different for reasons that no record explains. Each set therefore records how its walk-through was produced and by whom.

### What a person agreeing to a walk-through is agreeing to

The record binds, and the walk-through is what a person looks at. What they agreed to is therefore not, in every particular, what will be built from. Requiring the walk-through to carry only what a reader can check, and to state in itself what its notation cannot express, reduces that gap and does not close it. Nothing in the three standards beneath this one says anything about what a reviewer's agreement commits them to, and this is the gap that costs the most.

### And the questions a reviewer asks that are not rules

Each of these was considered as a rule and did not meet the standard's own test for one. A reviewer asks; the specifier records an answer; nobody is in breach for answering differently.

- Is any screen in this set really a report, a component that appears inside other screens, or a step that belongs on another screen?
- Does any screen carry so many values that it is really two? No threshold exists and none has been measured.
- Does the set name a kind for each screen, and if it does, are those kinds the business's words or the specifier's?
- Would this use case be better served by fewer and denser screens than the steps produced?
- Is the notation chosen the right notation for what this set has to show?
- Is the walk-through the shape a person would actually work in, or only the shape the steps fell into?

## 16  What it owes the application model

A set of screens is one of the documents the application model is written from, and this section says where each thing its record carries lands in the model. The words **mechanical**, **judgement**, **assumption** and **loss** are used here as the standard for one use case defines them in its section 13, and every section named in the tables is a section of the specification of the model, `SDD-09_The_Application_Model_v1.1.docx`. The rows follow section 11 of this standard: what is written down for each screen, and what is written down once for the set. A thing a screen names that is settled in another document — a record, a requirement, a business rule, an attribute, a relationship, a governed list — lands where its row in section 13 of the standard for one use case says, and has no second row here.

### 16.1  For each screen

| What the record carries | Where this standard asks for it | Lands in the application model | Mechanical or judgement | Where it cannot land |
|---|---|---|---|---|
| A screen: its identifier and its name | 5, the record header; 11, for each screen | §14 `forms[]` for a screen that shows one record, or §15 `lists[]` for a screen that shows many, each with its `id` and `name` | judgement: a form or a list | an assumption |
| A variation carried on a screen already in the set, or on a screen of its own | 4; 11, for each screen | as a screen: a variation of a screen lands in the form or list of that screen | judgement | an assumption |
| The use cases the screen serves, with the steps and variations it serves | 5; 11, for each screen | §14 a form's and §15 a list's `feature` (§6.2); §13.1 a human activity's `form`, where the step is a step of a process. The use case and its step land on the screen as `use_case`, a field the delivery kit's schema of the model carries and SDD-09 version 1.1 does not yet describe | mechanical | never |
| The entities shown and the entities changed | 5; 11, for each screen | §14 a form's `entity`, §15 a list's `source`; a value shown and not changed is `readonly` (§14.1) | mechanical | never |
| The requirements realised, the business rules cited and the quality requirements cited | 5; 11, for each screen | where section 13 of the standard for one use case lands each | as there | as there |
| A value | 6; 11, for every value | §14.1 `fields[]`, bound by `attr` to the attribute it shows; its control (§14.2) follows from the attribute's type | mechanical; a judgement for the control where the type admits more than one | a loss naming the answer the model cannot carry |
| — where the value came from | 6, the first question | no field in SDD-09 version 1.1. The delivery kit's schema of the model carries it on the field as `provenance`, with `justification` for a value that enters the organisation here; it records an origin, which is not the party that writes the fact | mechanical | a loss, until the specification of the model carries the field |
| — a reference to another record, chosen from a result | 6, the second question | §11.3 an attribute of type `ref`, whose `display` is the attribute that tells the record apart; §14.2 a `lookup` or `smart_search` control | mechanical | never |
| — a value drawn from a governed list | 6, the third question | §11.3 the attribute's `vocabulary`; §14.2 a `select` or `radio` control. The list's owner, the strength of the binding and the date that decides which values are offered land nowhere | mechanical for the list | a loss for the owner, the strength and the date |
| — the least the screen demands, and the most it admits | 6, the fourth question | §14.1 `required` and `readonly`, for the least; the most the screen admits beyond the entity model lands nowhere | mechanical | a loss for the most |
| — whether this person may see it at all | 6, the fifth question | §14 a form's and §15 a list's `permissions`; a prohibition held against one attribute for a class of person lands nowhere | mechanical for the permissions | a loss naming the rule |
| — how a cited rule appears | 6, the sixth question | where the rule lands, with its `message` (§11.4; §14 `validation[]`); an act made unavailable lands as the move's `roles` and `guard` (§12.2) | judgement | an assumption |
| An act that takes the person from one screen to another, and an act that raises a variation | 11, for each screen | §16 `menus[]`; §15 a list's `actions[]`, which open a form, make a move or start a process; §12.2 the move's `trigger` and `roles` | judgement | an assumption |
| The status and the version of a screen | 5; 11, for each screen | nowhere: the model names the set it was written from by identifier and version (section 15), and SDD-09 version 1.1 has no field for either | — | carried by the set, and not a loss |

### 16.2  For the set as a whole

| What the record carries | Where this standard asks for it | Lands in the application model | Mechanical or judgement | Where it cannot land |
|---|---|---|---|---|
| How the set was worked out and from what; the use case and the version of it the set was worked out from; the screens shared with another use case | 11, for the set | nowhere: the set's identifier and version are what the model names (section 15) | — | carried by the set, and not a loss |
| What the set reaches: the steps and variations, the two lists of entities, the requirements, and the reading against the stakeholders' interests | 7; 11, for the set | nowhere: they are the measure of the set, read at its review | — | carried by the set, and not a loss |
| How the walk-through is produced; the notation and what it cannot say; what agreeing to the walk-through commits the parties to | 8; 11, for the set | nowhere: they concern the walk-through, which the model is not written from | — | carried by the set, and not a loss |
| What a later version may change; the retired screens; the owner; the level of detail; the questions in dispute | 9; 11, for the set | nowhere; a screen retired from the set is a screen the model no longer carries | — | carried by the set, and not a loss |

### 16.3  Written once for the whole application

Four kinds of thing are written once for the whole application, before the screens of the first goal, in a part of the screens that this standard does not yet carry: a group of screens with the roles allowed and the goal each starts, an overview figure with the statement of where its figures come from, a whole-record screen, and a printed document. Their rows are given here so that where each lands is stated before that part is written.

| What the part carries | Lands in the application model | Mechanical or judgement | Where it cannot land |
|---|---|---|---|
| A group of screens, with the roles allowed and the goal each starts | §16 `categories[]`, with their `roles` and `menus[]` | mechanical | never |
| An overview figure, with the statement of where its figures come from | §17 `tiles[]`, each reading a named query (§10) written from that statement | judgement: the query | an assumption |
| A whole-record screen | §18 a composite view of kind `detail`, or §14 a form with the `detail_360` layout | mechanical | never |
| A printed document | §19 `reports[]`, each reading a named query (§10) | judgement: the query | an assumption |
