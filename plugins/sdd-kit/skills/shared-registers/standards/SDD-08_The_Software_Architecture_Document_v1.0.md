# SDD-08 · The Software Architecture Document

*This copy is carried by sdd-kit, the SDD method's skills for the service design course. It keeps the edition stated below; where the edition drew an example from the method's author's own client work, this copy carries an example set in Progressa in its place and says so where it does.*

*What an application is built on: the platform it is bound to, the components it switches on, the machinery that runs its processes, everything that crosses its boundary, and the code that has to be written specially*

*AN INTERNAL STANDARD  ·  VERSION 1.0  ·  29 SEPTEMBER 2026  ·  IN FORCE*

*Thirty-one rules, a form to fill, and a review gate in two halves. Written to be used on Monday and corrected by whoever uses it.*

Field | Value
--- | ---
Document | SDD-08 · The Software Architecture Document. What an application is built on: the platform it is bound to, the ready-made components it switches on, the machinery that runs its processes, everything that crosses its boundary, and the code that has to be written specially. It carried the code AR-01 until this edition
Version and standing | Version 1.0 · 29 September 2026 · in force. It comes into force by the owner's ruling of 29 September 2026, rulings/2026-09-29-four-draft-standards-in-force.yaml, which accepts its rules as version 0.1 stated them. It supersedes version 0.1 of 31 August 2026, which is kept in x_archive/. What changed: it came into force by the owner's ruling of 29 September 2026, and no rule changed; the one other sentence changed is the last of the fifth question of section 11, which said this standard is a draft until that question is tested, and now says that it came into force before the test, which stays open. An internal standard of FiscalAdmin OÜ, owned and approved by Aare Lapõnin, for the work of FiscalAdmin OÜ. Use it; tell the owner where it fails you
Who writes the document it governs | The solution architect, one document for each application
Who reads it | The person who writes the application model, and after them the software that turns that model into a working application
When it is written | Alongside the documents that say what the application is for, and finished before the application model is started
Rules | ARC-1 to ARC-31, in section 6
What it does not cover | Section 10 names each boundary and the document that holds it instead
Author | FiscalAdmin OÜ · Aare Lapõnin

---

> **What this standard promises.** Not that two architects given the same material will write the same document — no engineering discipline anywhere promises that, and where the work is a design there is nothing for two people to converge on. It promises something smaller and more useful: **two architects who have both finished will have answered the same questions about the same material.** Every difference between their documents can then be pointed at and argued about, one question at a time. A specification is finished when every line of the form in section 7 carries an answer, or carries a written reason for having none.

---

## 1. What this document is for

### 1.1 Why an architecture document here is not the usual thing

In most organisations an architecture document is read by a person, who then builds something, or approves something, or evaluates something. Every well-known way of writing one assumes that reader.

Here the reader is different. An application in this organisation is not built by hand. An author writes an **application model** — a single structured file that describes the whole application — and software turns that file into a working application. Below the model, nothing is written by hand and nothing is corrected by hand.

That one fact changes what an architecture document is for. A diagram that helps a person picture the system, but from which no part of the model can be written, does not belong in this document. It may still be worth drawing. It belongs in a briefing or a presentation, not here.

### 1.2 What the architecture specification says

It says what the application is **built on**, as against what it is **for**. Five things:

- which version and edition of the platform the application runs on, and on which database;
- which ready-made components are switched on, and what each one is switched on to do;
- how each business process is actually run — which machinery carries it;
- what enters the application from outside and what leaves it, described down to the individual field;
- what the application must have written specially for it, because nothing already available can express the requirement — and which requirement forced that.

### 1.3 What it does not say

It does not say what the business does. It does not carry the wording of a rule, the design of a screen, or the steps of a procedure. Those belong to other documents, and section 10 names them.

**One qualification, and it is important enough to state on the first page.** Business behaviour is excluded. **Behaviour at a boundary is not.** What a component does when the far side is slow, silent, or returns something out of date is part of what the application is built on, and it belongs in this document. Rules ARC-19 and ARC-24 require it.

### 1.4 Why it has to be finished first

The condition is not a preference about scheduling. If the architecture specification is unfinished when someone starts writing the application model, the missing decisions do not wait. They are taken inside that step, by whoever happens to be writing, at the moment they are needed, and they are not recorded anywhere.

*Finished before the model* therefore means something stronger than *finished before the build*. It means the specification must be complete enough that the person writing the model has to invent nothing. A specification that leaves a question to "detailed design" is not leaving it to a later stage. It is leaving it to whoever writes the file.

### 1.5 How you know you have finished

There is no published test that tells you a design is complete, and this standard does not invent one. What it gives you instead is a list of questions. **The specification is finished when every line of the form in section 7 carries an answer, or carries a written reason for having none.** Nothing else counts as finished, and nothing more is required.

---

## 2. The words used here

Each is used in exactly this sense throughout.

| Word | What it means in this standard |
|---|---|
| **The application** | One deployable thing, described by one application model file, generated as one unit. The unit this standard is written for |
| **The application model** | The single structured file that describes the whole application and from which the software is generated |
| **A landing site** | A named part of the application model that every application must fill. Because every application must fill it, something must decide what goes there — and this document is where that is decided |
| **The platform** | The software the application runs on: a version, an edition and a database, each an exact value |
| **The edition** | Which commercial level of the platform is licensed. The choice removes capabilities as well as granting them |
| **A component** | A ready-made piece of function the platform offers, switched on and configured rather than written |
| **The catalogue** | The list of components this application switches on, together with those it deliberately does not |
| **A process realisation** | The choice of which machinery runs a business process. Which machinery runs it is an architecture decision; what it decides is not |
| **A crossing** | One flow of information across the application's boundary, in one direction, carrying named fields |
| **The far side** | Whoever is on the other end of a crossing: another system, another organisation, another team |
| **The issuer** | Whoever creates and owns a value that this application borrows rather than creates. The issuer decides what the value means and when it stops being valid |
| **Freshness** | How old the copy of a borrowed value may be before it stops being usable, and how the reader can tell |
| **A bespoke component** | Something written specially for this application because nothing available could express the requirement |
| **A deviation** | Any departure from what the platform and the catalogue already provide. A bespoke component is one kind |
| **A finding** | A question this specification cannot answer, written down with a named owner and a date. **The only permitted response to something this standard cannot settle** |
| **A decision** | A choice with more than one defensible answer, taken by somebody with the authority to take it, and recorded |

---

## 3. Where this document sits

The application model is written from four documents, and this is one of them. The other three describe what the application is **for**. This one describes what it is **built on**. They meet only in the model.

![Figure 1. Where the architecture specification sits. Three documents say what the application is for; this one says what it is built on. They meet only in the application model, and this one has to be finished first.](figures/SDD-08/SDD-08_fig01.png)

*Figure 1.  Where the architecture specification sits. Three documents say what the application is for; this one says what it is built on. They meet only in the application model, and this one has to be finished first.*

Three things follow from the picture, and each is a rule later on.

**This document does not feed the ones above it.** It does not shape the use cases, and it does not shape the record model. It reads them and it feeds the build. If writing it makes you want to change a use case, that is a finding against the use case, not a change you make here.

**It has to be complete before the model is written**, for the reason section 1.4 gives.

**Everything in it lands somewhere, or it is not in it.** The five parts of section 4 are the five places it lands. A statement that lands in none of them, and that no check reads, does not belong in this document.

---

## 4. The five places the work lands

The application model has a fixed set of named parts. Five of them cannot be filled by anyone but the architect, and those five are what this document exists to decide.

![Figure 2. The five parts of the application model that nobody but the architect can fill — and therefore the five things this document exists to decide.](figures/SDD-08/SDD-08_fig02.png)

*Figure 2.  The five parts of the application model that nobody but the architect can fill — and therefore the five things this document exists to decide.*

| The part of the model | What sits there | What this document owes it |
|---|---|---|
| **The binding** | The platform version, the edition, the database, and the conventions that apply across the whole application | Three exact values, **and what each of them costs**. Naming an edition without naming what that edition forbids binds the application without saying what was given up |
| **The catalogue** | Each component switched on, its version, whether it is configured once or separately for each use, and its configuration | The list of components **and what each one is switched on to do** — and the list of components that were available and were deliberately not used |
| **The processes** | For each business process: the machinery that runs it, who takes part, what the steps are, how work is routed, and what the deadlines are | **The choice of machinery, for each process.** This is the one place where an architecture decision and a business decision sit side by side, and the standard separates them: which machinery runs the process is ours; what the process decides is not |
| **The interfaces** | Everything entering and leaving, stated field by field, with how each is authenticated | **Every crossing, in both directions, down to the field** — and, for each, what happens when the far side is absent, out of date or unreachable |
| **The bespoke code** | Each specially written component, what forced it, what it reads and what it writes | **The budget** — and the rule that every entry names the requirement that forced it and why nothing already available could express that requirement |

---

## 5. The principles

Five. Each is the reason a family of rules exists.

**P1 · Everything written here must land somewhere.** A statement that fills no part of the application model, and that no check reads, is decoration however true it is. It is removed from the specification and put where it belongs — a briefing, a note, a conversation. This is what rule ARC-3 enforces and it is the hardest of the five to apply honestly, because a good diagram feels like it must be earning its place.

**P2 · What the application is built on, not what it does — with behaviour at the boundary as the stated exception.** The wording of a rule, the design of a screen and the steps of a business procedure are specified elsewhere. But what a component does when the far side does not answer is not business behaviour. It is a property of the thing being built, nobody else specifies it, and if this document does not carry it nothing does.

**P3 · Nothing is left to be decided later.** There is no later. The next step writes the model, and a question this document leaves open is answered there, silently, by whoever is writing.

**P4 · A gap is a finding with an owner, never a local invention.** Where this specification cannot say what to do, it says so, names who decides, and dates it. It never fills an empty space with something plausible. An empty space that is marked is information; an empty space that has been filled in quietly is a defect nobody can see.

**P5 · A decision is written as a decision.** Much of what an architecture specification contains has more than one defensible answer. Where that is so, the document says which answer was taken, who took it, and what would make it wrong. A reader who cannot tell a decision from a finding cannot argue with either.

---

## 6. The rules

Thirty-one, in seven families. Each carries the failure it prevents, because a rule whose failure you cannot picture is a rule you will not follow under pressure.

### A · The document as a whole

| # | The rule | The failure it prevents |
|---|---|---|
| **ARC-1** | **One specification for one application.** The unit is the thing that is generated as one unit, and it is not a release, a subsystem, a programme or a department | A document whose scope nobody can state, so that two people disagree about whether something is in it without either being wrong |
| **ARC-2** | The specification **states its version, its date and whether it is finished**, on its first page | A model written from a draft that somebody believed was final |
| **ARC-3** | **Every statement in the specification either fills a named part of the application model, or is read by a named check.** Anything else is moved out of the document | A specification that grows until nobody reads it, in which the three paragraphs that matter are indistinguishable from the thirty that do not |
| **ARC-4** | Where the specification cannot answer a question, it **records a finding**: the question, a named owner and a date. It does not answer the question locally | A decision taken by whoever noticed the gap, at the moment they noticed it, recorded nowhere and discovered months later by its consequences |
| **ARC-5** | Where the specification takes a decision, it records **who took it and what would make it wrong** | A decision that cannot be revisited, because nobody can now say what it was weighing against |

### B · The platform binding

| # | The rule | The failure it prevents |
|---|---|---|
| **ARC-6** | The specification names **the platform version, the edition and the database, as exact values**. Not a range, not "the current one" | A model that will not validate, and an argument about which environment was meant |
| **ARC-7** | Where the chosen edition **forbids something the application would otherwise use**, the specification lists what is forbidden and what will be used instead | Discovering at build time that a capability the design assumed is not licensed, when the design is already finished |
| **ARC-8** | Conventions that apply across the whole application — naming, dates, numbering, language — are **stated once, here** | The same convention decided three times, differently, by three people who each thought they were the first |

### C · The component catalogue

| # | The rule | The failure it prevents |
|---|---|---|
| **ARC-9** | Every component switched on is listed **with what it is switched on to do**: one sentence naming the requirement or the use case it serves | A component nobody can remove, because nobody can say what would break |
| **ARC-10** | Every component states **whether it is configured once for the whole application, or separately at each place it is used** | Configuration written once where it needed to vary, or written many times where one setting would have done |
| **ARC-11** | The catalogue also lists **components that were available and were deliberately not used**, with the reason in one line | A component that is absent because it was rejected looks exactly like one that nobody ever considered. The second is a gap; the first is a decision, and only writing it down keeps them apart |
| **ARC-12** | A component is not entered in the catalogue until **its configuration has been checked against what that component actually accepts** | A catalogue that reads well and does not validate |

### D · The process realisations

| # | The rule | The failure it prevents |
|---|---|---|
| **ARC-13** | Every business process names **which machinery runs it** | A process that exists in the requirements and in nobody's build |
| **ARC-14** | For each process, the specification states **which decisions the machinery takes and which it does not** | The one confusion this part of the model invites: an architecture decision and a business decision sitting in adjacent fields, and being made by the same person in the same minute without either being labelled |
| **ARC-15** | A process **never introduces a state the record model does not already have**. Where one is needed, that is recorded as a finding against the record model | A record whose real set of states is larger than the set anybody documented, discovered when a report will not add up |
| **ARC-16** | Every change of state names **the party that makes it** — a person in a role, a scheduled job, or an incoming instruction from outside | A state that changes and nobody can say what changed it, which cannot be tested and cannot be audited |

### E · The boundaries

**The longest family, and the one that carries the most.** A boundary is where this application depends on something it does not control, and almost every expensive failure in this kind of work is a boundary that was described in less detail than it was relied upon.

![Figure 3. What one crossing must state. Section 7.4 turns this picture into the lines of the form, one line at a time.](figures/SDD-08/SDD-08_fig03.png)

*Figure 3.  What one crossing must state. Section 7.4 turns this picture into the lines of the form, one line at a time.*

| # | The rule | The failure it prevents |
|---|---|---|
| **ARC-17** | Every crossing is listed, **in both directions, down to the individual field**. A crossing described at the level of the system, the interface or the message is not described | "We take the taxpayer details from the register" — a sentence that four people read four different ways, all of them reasonably |
| **ARC-18** | Every field this application **borrows rather than creates** names four things: **who issues it, which name space it belongs to, how long it stays valid, and how it is checked** | A borrowed key that arrives as an unrestricted piece of text, with no validation on any screen, so that the first quality report on the module counts nothing because there is nothing to count against |
| **ARC-19** | Every crossing states **how fresh its information is**, and states separately what happens in **three different situations: the value is missing, the value is out of date, and the far side cannot be reached** | Treating three conditions as one. They have three different right answers, and merging them produces an application that shows an old figure as if it were current, or shows nothing as if it were zero |
| **ARC-20** | Every crossing states **what this application must not store**, and for how long it may hold anything it is permitted to keep | A copy of somebody else's data becoming a second source of truth, and then being wrong |
| **ARC-21** | **The meaning of what crosses is stated separately from the mechanism that carries it.** What a field means is written once; the format it travels in is written beside it and may be replaced without touching the meaning | A change of transport format being treated as a change of meaning, or the reverse — and either way a negotiation with the far side that starts from the wrong document |
| **ARC-22** | Every crossing states **what would let both sides check it independently**, without either seeing the other's implementation: what is published, what a test would read, and what a passing result would mean | A boundary that only one side can test, so that a disagreement about whether it works cannot be settled by either party |
| **ARC-23** | **No password, key, secret or credential appears anywhere in the specification.** The specification names where the credential is kept and who may fetch it | The obvious one, and it still happens |
| **ARC-24** | An **incoming instruction** states what the application does with it, **including what it does when it cannot comply** | An instruction the application accepts, records and then quietly ignores, with nothing failing anywhere to say so |

### F · The bespoke-code budget

| # | The rule | The failure it prevents |
|---|---|---|
| **ARC-25** | Something is written specially **only after both the model and the catalogue have been shown unable to express the requirement**, and the specification records what was tried | Building something that already exists, which happens often enough that looking first is a rule and not a courtesy |
| **ARC-26** | Every bespoke entry **names the requirement that forced it** — the requirement, cited, not a preference and not a habit | A count of exceptions that grows every release and that nobody can shorten, because no entry says what would remove it |
| **ARC-27** | Every bespoke entry names **what it reads and what it writes** | Something written specially that turns out to read a record it was never meant to see, discovered by an incident |
| **ARC-28** | A bespoke component that is needed by **a second application** is recorded as a candidate for the catalogue | The same thing built twice, then maintained twice, then found to behave differently in the two places |

### G · Decisions, findings and change

| # | The rule | The failure it prevents |
|---|---|---|
| **ARC-29** | A decision is recorded **once, in one place, and is not edited after it is agreed.** A changed decision is a new record naming the one it replaces | A record that now describes something nobody decided, because it was quietly brought up to date |
| **ARC-30** | A decision record names **what would make it wrong** | A decision that outlives the conditions that justified it, because nothing was ever written that would signal the conditions had changed |
| **ARC-31** | **Nothing is deleted.** A withdrawn component, crossing, process or decision stays in the document, marked withdrawn, with the reason and the date | A reader who comes looking for something finds a gap instead of finding out what happened to it, and raises it again |

---

## 7. The form the architect fills

Six parts. Part 1 is filled once for the application; parts 2 to 5 once for each item of that kind; part 6 once at the end. **Every line names the rule that requires it**, because a form line whose origin nobody can state is how a form grows until people stop filling it in.

### 7.1 Part 1 — the application, once

| Line | What to write | Rule |
|---|---|---|
| **Application** | The name of the one thing this specification covers | ARC-1 |
| **Version, date, finished** | The version, the date, and *finished* or *draft* | ARC-2 |
| **Platform version** | The exact value | ARC-6 |
| **Edition** | The exact value | ARC-6 |
| **Database** | The exact value | ARC-6 |
| **What the edition forbids** | Each capability the design would have used and the edition does not allow, with what will be used instead | ARC-7 |
| **Conventions** | Naming, dates, numbering, language — stated once for the whole application | ARC-8 |
| **Documents read** | The requirement register, the use case model and the record model this specification was written from, each with its version | ARC-3 |

### 7.2 Part 2 — once for each component

| Line | What to write | Rule |
|---|---|---|
| **Component and version** | Which one, at which version | ARC-9 |
| **Switched on to do** | One sentence naming the requirement or use case it serves | ARC-9 |
| **Configured** | *Once for the whole application*, or *separately at each place it is used* | ARC-10 |
| **Configuration** | The settings, checked against what the component accepts | ARC-12 |

**And once at the end of part 2, the negative list.** Each component that was available and is deliberately not used, with the reason in one line. *(ARC-11.)*

### 7.3 Part 3 — once for each process

| Line | What to write | Rule |
|---|---|---|
| **Process** | Which business process this is | ARC-13 |
| **Machinery** | Which machinery runs it | ARC-13 |
| **What the machinery decides** | The routing and timing choices that belong to the machinery | ARC-14 |
| **What it does not decide** | The business choices that are specified elsewhere and are only carried here | ARC-14 |
| **States used** | Each state the process moves a record through, and confirmation that the record model already has it — or a finding | ARC-15 |
| **Who changes each state** | For each change: a person in a named role, a scheduled job, or an incoming instruction | ARC-16 |

### 7.4 Part 4 — once for each crossing

The longest part of the form, and the one that repays the most care. Figure 3 in section 6 shows the same thing as a picture.

| Line | What to write | Rule |
|---|---|---|
| **Direction** | *In* or *out* | ARC-17 |
| **Far side** | Which system, organisation or team is on the other end | ARC-17 |
| **What crosses** | Every field, listed individually | ARC-17 |
| **Meaning** | What each field means, in words, independent of how it travels | ARC-21 |
| **Format** | The format the fields travel in, written beside the meaning and not merged with it | ARC-21 |
| **Issuer** | For each borrowed field, who creates and owns it | ARC-18 |
| **Name space** | Which set of names the value belongs to, so that two identical strings from different sources are not confused | ARC-18 |
| **Validity** | How long the value stays valid, on the issuer's terms | ARC-18 |
| **How it is checked** | The rule that tells a correct value from an incorrect one | ARC-18 |
| **Freshness shown** | How the reader can tell how old the information is | ARC-19 |
| **If the value is missing** | What the application does. *Absence returned as absence* is an answer; a substituted default is not, unless the specification says so and says why | ARC-19 |
| **If the value is out of date** | What the application does. Carrying an old value forward silently is the failure this line exists to prevent | ARC-19 |
| **If the far side cannot be reached** | What the application does, and what the user sees | ARC-19 |
| **Must not be stored** | What this application may never keep, and how long it may keep anything it is permitted to hold | ARC-20 |
| **How both sides check it** | What is published, what a test would read, and what a passing result would mean | ARC-22 |
| **Authentication** | How the caller is identified, and **where the credential is kept** — never the credential itself | ARC-23 |
| **If an incoming instruction cannot be carried out** | What the application does, what it records, and what fails so that somebody notices | ARC-24 |

### 7.5 Part 5 — once for each bespoke component

![Figure 5. The order every departure passes through. A specially written component is what is left when the first two steps have both been tried and recorded.](figures/SDD-08/SDD-08_fig04.png)

*Figure 5.  The order every departure passes through. A specially written component is what is left when the first two steps have both been tried and recorded.*

| Line | What to write | Rule |
|---|---|---|
| **What it is** | The component, and what kind of thing it is | ARC-26 |
| **What was tried first** | The parts of the model and the catalogue components that were examined, and why each could not express the requirement | ARC-25 |
| **Forced by** | The requirement, cited, that makes this necessary | ARC-26 |
| **Reads / writes** | Which records it reads and which it writes | ARC-27 |
| **Wanted elsewhere** | Whether another application needs the same thing | ARC-28 |

### 7.6 Part 6 — decisions and findings, once at the end

| Line | What to write | Rule |
|---|---|---|
| **Each decision** | What was decided, by whom, on what date, **and what would make it wrong** | ARC-5, ARC-29, ARC-30 |
| **Each finding** | The question, a named owner, a date, and what the application does in the meantime | ARC-4 |
| **Each withdrawal** | What was withdrawn, when, why, and what replaced it | ARC-31 |
| **Counts, stated and not judged** | How many crossings; how many carry a freshness answer; how many bespoke entries; how many findings are open. **No target is set on any of these and none should be inferred** | — |

---

## 8. The review gate

A finished specification is reviewed in two halves, because the two halves fail in different ways and mixing them produces a review that checks the boxes are full rather than that the answers are right.

![Figure 4. The two halves of the review gate. Only one half can ever be automated, and none of that half has been built yet.](figures/SDD-08/SDD-08_fig05.png)

*Figure 4.  The two halves of the review gate. Only one half can ever be automated, and none of that half has been built yet.*

### 8.1 What a program can check

A program can tell whether an answer is present, whether a name follows a pattern, and whether two documents that must agree do agree. It cannot tell whether an answer is any good. What follows is what will be checked mechanically.

> **These checks are described here and have not been built.** Nothing in the table below runs today. It is written out so that an architect knows what will be read mechanically, and so that whoever builds the checks knows what to build. **No result may be reported from any of them until they exist**, and a check is trusted only after it has been seen to refuse something.

| Check | What it reads | It fails when |
|---|---|---|
| **ARC-C1** | every line of the form | a line is empty and carries no written reason for being empty |
| **ARC-C2** | the platform binding | the version, edition or database is not one of the permitted exact values |
| **ARC-C3** | the edition | a capability the edition forbids is used anywhere in the specification |
| **ARC-C4** | every component entry | it names no purpose, or does not say whether it is configured once or per use |
| **ARC-C5** | every component configuration | a setting is not one the component accepts |
| **ARC-C6** | the negative list | it is absent — a specification with no rejected components has not considered any |
| **ARC-C7** | every process | it names no machinery |
| **ARC-C8** | every state a process uses | the record model does not have it, and no finding is recorded |
| **ARC-C9** | every state change | it names no party that makes it |
| **ARC-C10** | every crossing | any field crossing it is unnamed |
| **ARC-C11** | every borrowed field | it names no issuer, no name space, no validity or no checking rule |
| **ARC-C12** | every crossing | any of the three situations — missing, out of date, unreachable — has no answer |
| **ARC-C13** | every crossing | it states nothing about what must not be stored |
| **ARC-C14** | the whole specification | anything in it matches the shape of a password, key or token |
| **ARC-C15** | every bespoke entry | it names no forcing requirement, or names one that does not exist in the requirement register |
| **ARC-C16** | every bespoke entry | it does not say what it reads and what it writes |
| **ARC-C17** | every decision record | it does not say what would make the decision wrong |
| **ARC-C18** | every finding | it has no named owner or no date |
| **ARC-C19** | the whole specification | a statement fills no part of the application model and is read by no check |
| **ARC-C20** | the counts in part 6 | **nothing. This one reports and never fails** |

### 8.2 What only a person can judge

No program will decide any of these, and a review that skips them has checked that the form is full rather than that the specification is right.

- Whether the **purpose written against a component** is the real reason it is switched on, or the reason that was easiest to write.
- Whether the **negative list** is honest, or contains only the components nobody wanted anyway.
- Whether **what the machinery decides** and **what it does not** have been separated correctly, or whether a business decision has been quietly handed to the routing.
- Whether the **answer for a missing value** is right — whether absence should be shown as absence, or whether the operation should fail.
- Whether a **freshness limit** is the limit the business actually needs, or the limit the far side happens to offer.
- Whether the **forcing requirement** on a bespoke entry really forces it, or whether it is a requirement that happens to exist and was attached afterwards.
- Whether a **decision's reversal condition** is one anybody would notice if it occurred.
- Whether the specification is **complete against the material it was written from** — for which there is no test, and which is the reason section 8 has two halves rather than one.

---

## 9. The ways this work goes wrong

Named so that a reviewer can look for them, and so that an architect can recognise one while writing rather than at review.

**1 · The boundary described in less detail than it is relied upon.** A crossing written as one sentence about a system, which four people then read four different ways. The cost appears months later, in a screen that cannot validate a field and a report that counts nothing.

**2 · Three conditions treated as one.** A value that is missing, a value that is out of date, and a far side that cannot be reached are three situations with three different right answers. Merging them produces an application that shows a stale figure as though it were current, or an absence as though it were zero.

**3 · The half-finished marker.** A field is marked as coming from outside, and nothing says who issues it. The half of the statement that does the work is the half most often left out, because the marker alone looks complete on the page.

**4 · The edition named without its cost.** The commercial level of the platform is written down as though it only granted capabilities. It also removes them, and a design that assumed a removed capability is discovered at build time, when it is finished.

**5 · The component nobody can remove.** Something is switched on, nobody wrote down what for, and now no one can say what would break if it were switched off. Every such component is permanent.

**6 · The exception with no requirement behind it.** Something written specially, justified by a preference or by the way it was done last time. The list of exceptions then grows every release and can never be shortened, because no entry says what would remove it.

**7 · Silence read as permission.** A specification says nothing about whether something may be stored, and everyone concludes it may be. What was not written was not decided, and the safe reading of silence is that the question is open.

**8 · The decision brought quietly up to date.** A decision record is edited when the decision changes, so the document now describes something nobody ever decided, and the reasoning behind the original choice is gone.

**9 · The diagram that lands nowhere.** A picture that helps a person understand the system and from which no part of the model can be written. It is not wrong, and it does not belong in this document. Put it in the briefing.

**10 · The gap filled quietly.** An empty space that gets a plausible answer instead of a finding. A marked gap is information that somebody can act on. A filled one is a decision that nobody took and nobody can see.

---

## 10. What this standard does not cover, and where instead

One sentence for each boundary.

- **What the customer asked for.** → the register of requirements. *This specification cites requirements; it never restates one and never adds one.*
- **What the application is for, and who uses it.** → the use case model, and the description of each use case. *If writing this specification makes you want to change a use case, that is a finding against the use case.*
- **What the records are, what fields they have, and what makes two rows the same thing.** → the record model, and the standard on identity, ownership and state. *This specification names states and fields; it does not define them.*
- **What a person sees.** → the screen documents and the interface standards. *A screen never appears in this specification, in any form.*
- **The wording of a business rule, and what it decides.** → the use case descriptions. *This specification says which machinery reads a rule. It never says what the rule says.*
- **The language the application model is written in.** → the application model specification. *This document decides what goes into the model; that document decides how it is written.*
- **Where the line runs between what is decided once for the whole platform and what is decided for each application.** → **not settled.** Until it is, an architecture specification records anything it must take as given, names who owns it, and does not decide it locally.

---

## 11. What this standard does not yet answer

Named here rather than discovered at review.

**1 · How you know a specification is complete.** There is no test, in this organisation or in published practice, that says a design covers everything it should. The form in section 7 gives a list of questions and no denominator. Section 1.5 is the honest limit of what is promised.

**2 · Where the platform line runs.** What an application's specification may say about the platform, and what it must take as given, is not settled. Rule ARC-4 tells you what to do in the meantime: record it as a finding with an owner.

**3 · Whether a decision record should be a separate document.** This standard requires decisions to be recorded and does not require them to live in a separate file. Both arrangements are in use elsewhere and neither is shown to be better.

**4 · What forces a quality requirement to be answered.** Requirements about speed, availability, safety and auditability reach this document, and nothing in it obliges the architecture to answer one rather than note it. Elsewhere that binding is done by a review meeting, which is not something this way of working can use. **The gap is real and it is open.**

**5 · Whether a specification written to this standard can be told from one written without it.** That has not yet been tested. This standard came into force before it was, by the owner's ruling of 29 September 2026, and the question stays open until it is.

---

## 12. Conformance

**A claim that a specification conforms to this standard is made rule by rule, or it is not a claim.**

To claim conformance is to state, for each of the thirty-one rules in section 6, that the specification satisfies it — and, where it does not, to have recorded a finding with a named owner and a date.

**A finding with an owner does not defeat the claim. A failure that was never recorded does.**

Three things follow.

1. **No conformance claim may cite a check result.** None of the checks in section 8.1 has been built. A claim that says *the checks pass* is a claim about a program nobody has written.
2. **A count of zero findings is a warning, not a result.** Every specification of any size meets something it cannot settle. A specification that reports none has probably not looked.
3. **Conformance says the standard was followed.** It does not say the specification is right. That is what section 8.2 is for, and it needs a person.

---

## 13. Where these rules come from

Three sources, and it is worth knowing which is which.

**A few of the rules rest on published engineering practice**, where a recognised discipline states the same thing and more than one field does it. The rules about stating a boundary so that both sides can check it independently, and about keeping the meaning of what crosses separate from the format it travels in, are the clearest of these.

**Most of them are this organisation's own position.** They were arrived at by examining what published practice offers and finding that it mostly does not reach this case, because published practice assumes a person reads the architecture document and then builds something. Here a person reads it and then writes a model, and software builds from the model. A rule that exists because of that difference is ours, and it stands or falls on our judgement rather than on anybody else's evidence.

**Everything in this standard that refuses is ours.** No published practice anywhere was found that sends an architecture document back to its author. There is a great deal of published machinery that refuses things — it refuses systems, deployments, certificates and written claims of conformance — but not descriptions. So every check in section 8.1 that would send a specification back is this organisation's own, and if that judgement is wrong the checks are wrong with it.

**And several rules come from what has gone wrong here.** The boundary rules in family E, in particular, were written from real cases: a borrowed key that shipped as unrestricted text with no validation anywhere; an incoming instruction contract that nothing enforced, where no check refused an implementation that ignored it and no test failed; and a figure published in one month that could not be reproduced in another because nothing recorded what had been included in it.

---

*`AR-01` · version 1.0 · 29 September 2026 · in force. Comments to the owner.*
