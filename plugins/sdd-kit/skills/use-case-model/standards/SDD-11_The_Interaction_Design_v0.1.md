# SDD-11 · The Interaction Design

*This copy is carried by sdd-kit, the SDD method's skills for the service design course. It keeps the edition stated below; where the edition drew an example from the method's author's own client work, this copy carries an example set in Progressa in its place and says so where it does.*

*How a person picks a value, finds a record, moves a state and acts on a record, across every goal an application model carries — settled once, from the accepted screens, and accepted by the owner before the model is written*

*AN INTERNAL STANDARD  ·  VERSION 0.1  ·  25 SEPTEMBER 2026  ·  DRAFT FOR REVIEW*

*Twenty-nine rules, five tables with fixed headings, a gate and a review. Settled once for an application, never goal by goal.*

Field | Value
--- | ---
Document | SDD-11 · The Interaction Design. How a person picks a value, finds a record, moves a state and acts on a record, across every goal an application model carries: settled once, from the screens the owner has accepted, and accepted by the owner before the application model is written. Its rules are prefixed IXD.
Version and standing | Version 0.1 · 25 September 2026 · draft for review. It supersedes nothing: it is the first edition of a new standard, written under the ruling of 25 September 2026 that gave the method an interaction design step and made its rules this standard (rulings/2026-09-25-the-interaction-design-step.yaml). It comes into force only when the first interaction design written to it has been accepted by the owner, the application model written from that document has been admitted by the delivery kit's gate while the model before it is refused, and the owner has accepted, as version 1.0, the edition that proof corrects; that last decision the ruling reserves to him. The gate of section 8 is built in the delivery kit by a round of its own, and until then it is described here and not enforced. It is not in force and should not be quoted as binding. Corrected on 25 September 2026 as its review directs (_reviews/REVIEW_WRITE_the_interaction_design_standard_2026-09-25.md). An internal standard of FiscalAdmin OÜ, owned and approved by Aare Lapõnin, for the work of FiscalAdmin OÜ.
Who writes the document it governs | One analyst, reading together the accepted screens of every goal the application model is to carry. One document for each application, brought forward for each increment of its model.
Who reads it | The owner, who accepts it; whoever writes the application model from it; and the delivery kit's gate, which refuses a model that does not name the accepted document or contradicts it.
When it is written | After the owner has accepted the use case description and the screen record of every goal the model will carry, and before the model is written; and again for every increment of the model that takes in goals newly accepted.
Rules | IXD-1 to IXD-29, twenty-nine rules, in sections 3 to 8, each with its source beneath it. None has yet been used by anybody who did not write it; section 12 says how firm they are.
What it does not cover | What a screen does, which is UX-01's; the screens of one goal, which are SDD-07's; which lists exist and whose they are, which is SDD-03's; the states and moves of a record and who may make each, which are SDD-04's; the application model, which is SDD-09's and the delivery kit's; and what the kit generates for every application without design. Section 1 names each boundary.
Author | FiscalAdmin OÜ · Aare Lapõnin

---

Contents

1  What this standard is for

2  The words, defined once

3  The step and its document

4  What every application is given, and is never asked

5  The four questions

6  The listings and the pages

7  The form of the document

8  The gate after the step

9  The review

10  A worked example

11  The questions this standard does not answer

12  Where these rules come from

Figures

Figure 1 — Where the step stands: after the owner accepts the goals, and before the application model is written.

Figure 2 — What the step reads, what it settles, and who reads what it hands on.

Figure 3 — What every application is given without design, and what each application decides.

Figure 4 — The seven parts of the document, and who reads which.

Figure 5 — The gate after the step: what the model names, and the four places the kit refuses it.

Figure 6 — The worked example: the moves a person makes on one record, each by a named act.

## 1  What this standard is for

### What an interaction design is

An interaction design is the statement, made once for an application, of how a person using it picks a coded value, finds one record among many, moves a record from one state to the next, and acts on a record. It is written across every goal the application model is to carry, from the screens of those goals as the owner accepted them, and it is accepted by the owner before the model is written. Its unit is the application, or the part of it that one writing of the model covers, and not the goal: a list of values is maintained once for the application, the moves of one record are made by the acts of several goals, and a form that belongs to a record may be opened from several places, so the questions it answers exist only across goals.

It settles only what each application decides. Everything that is the same for every application — how a list of values is administered, how a coded value, a yes-or-no and a date are shown, that a state is shown and never chosen, that a move is made by a button named after it, that a record among many is found by a search, that an act carries its record to the form it opens — is generated by the delivery kit for every application without design, under the house rules for what a person sees, UX-01. Section 4 draws the line between the two halves and says where each is kept.

The step exists because four things were found unsettled in a running application built by this method: its lists of values, the finding of one record among hundreds of thousands, the state of a record, and the forms an act opens. None of the documents written before the application model settled them, the model did not decide them, and the program that turns the model into an application decided them by default, differently from what the house rules require. The owner's word of 25 September 2026 made the analysis of these four things a step of the method, taken after the use case descriptions and screens are accepted and before the application model is written, and not to be skipped (rulings/2026-09-25-the-interaction-design-step.yaml).

![Figure 1](figures/SDD-11/SDD-11_fig01.png)

*Figure 1 — Where the step stands: after the owner accepts the goals, and before the application model is written.*

### Where it stands in the method

The step stands between two acts of the owner. Before it, he accepts the use case description and the screen record of every goal the model is to carry; a goal he has not accepted is left out of that writing of the model and is not designed provisionally. After it, he accepts the interaction design itself; and the application model, which names the accepted document by its path and its checksum, is admitted to generation only when the delivery kit finds that document there, accepted, unchanged and not contradicted (section 8). The step is taken again for every increment of the model that takes in goals newly accepted.

In the method's order it is a twelfth thing, placed after the walk-through of a goal's screens and numbered 08a, so that nothing already numbered is renumbered. Two handovers are added after the fourteen the method counts: the fifteenth, from the accepted screens to the interaction design, stands at a person; the sixteenth, from the accepted interaction design to the application model, stands at a program. The method standard, SDD-01, places the step in its next edition, and the delivery kit's register of the method's things gains the slot and the two handovers in the round that builds the gate of section 8.

### Why it is a standard of its own

The interaction design has its own writer, one analyst reading every accepted set of screens of the increment; its own readers, the owner who accepts it, the writer of the application model and the delivery kit's gate; its own moment, after the goals are accepted and before the model; its own review, which is the owner's acceptance; and its own procedure for change, which is acceptance again. By the method's own test that makes it a document of its own and not a section of another (SDD-01, section 4). It is not a section of the standard for the screens of a use case, SDD-07, because a set of screens is written for one goal, beside it, and reviewed for that goal alone. It is not a part of the application model, SDD-09, because the model is written last, and a part of it cannot be accepted before the model exists.

### Who writes it, and what they have in front of them

One analyst writes the interaction design of an application and answers for it. In front of them are six things, none of them the analyst's to decide:

- the accepted descriptions and screen records of the goals, with their walk-throughs, each named by path and version;
- the entity model's table of governed lists, which says for each list whose it is, who issues it and where it is published (SDD-03, EM-19 and EM-46 to EM-48);
- the shared groundwork's states and moves, which declare for every move what fires it and who may make it (SDD-04, IOS-10 to IOS-12), and its assignment of shared code lists (IOS-28, IOS-29);
- the architecture specification's platform binding and the components it switches on (SDD-08), which say what the platform and its library of components can realise;
- the house rules for what a person sees, UX-01 and UX-02, with the rulings in force on them, among them the ruling that a list longer than nine is chosen by category (rulings/2026-09-25-long-lists-are-chosen-by-category.yaml);
- the sample values the screen records already use, from which the clickable pages are built.
Every rule below is written to be applied from that position. Where a question needs a decision the analyst cannot take, the rule says who takes it; where the goals are silent, the document says so and recommends an answer, which the owner accepts or amends (IXD-7).

![Figure 2](figures/SDD-11/SDD-11_fig02.png)

*Figure 2 — What the step reads, what it settles, and who reads what it hands on.*

### What this standard does not cover

Several things belong elsewhere, and nothing here restates them. A rule written in two places is a rule that will drift, so where another standard governs, this one points at it and adds only what it does not say.

- What a screen does. How a value is chosen, a record is found, a state is shown and an act is placed are ruled by UX-01 — IDR-01 to IDR-07, PRE-03, PRE-05, STA-01 to STA-03, CTX-01, CTX-02, CTX-04, PRD-02 and TRM-02 — and this standard cites those rules and restates none of them.
- The screens of one goal, what a person sees while reaching it and its clickable walk-through, governed by SDD-07.
- Which lists exist, whose each one is and who issues it, governed by the entity model standard, SDD-03; and the states and moves of a record, what fires each move and who may make it, governed by the shared registers standard, SDD-04. The step reads them and decides none of them again (IXD-6).
- The application model, governed by SDD-09 and by the delivery kit's schema, which prevails over SDD-09's text. The model carries what the interaction design decided, in the constructs the schema gives it; how the model is written is not this standard's subject.
- What the delivery kit generates for every application without design. Section 4 names it; the kit and UX-01 keep it.

### What this standard promises, and what it does not

It promises that an interaction design written to it can be checked. Every decision it requires sits in a table with fixed headings that a program reads; every table is measured against listings a program produced from the accepted screens; and the delivery kit's gate refuses a model that skips the document or contradicts it.

It does not promise that two analysts will reach the same decisions for the same application. What it offers instead is the smaller thing: two documents written to it have asked the same questions of the same goals, so every difference between them can be pointed at. Nor does it promise that a decision is a good one — that a list's categories are those the business uses, that a guard's words will be understood, that a search's keys are the ones the officers have at hand. Those are settled by the owner's reading, and section 11 says so rather than leaving a reader to discover it.

### Claiming conformance

An interaction design conforms to this standard when it does three things.

- Declares the claim. "This interaction design claims conformance to the rules of this standard, IXD-1 to IXD-29."
- States, rule by rule, how it satisfies each one and where. A claim without the line-by-line assessment is not checkable, and is therefore not a claim.
- Passes the review in section 9, with every line that does not pass recorded as a finding with a named owner. An owned finding does not defeat the claim; an unrecorded failure does.

## 2  The words, defined once

The rules rely on a small and precise vocabulary, and the definitions below are normative. Every word defined here is defined here and nowhere else; where a word belongs to another standard of this series, that standard is named and its definition stands.

- The interaction design. The document this standard governs: for one application, or for the part of it one writing of the model covers, the decisions of the four questions, with the listings they are measured against, the pages that show them working, the places where the goals were silent and the findings raised.
- The step. The act of writing the interaction design and having it accepted. It stands between the owner's acceptance of the goals and the writing of the application model.
- A goal. A goal a person completes in one sitting, written out in full under SDD-06 and given its screens under SDD-07. The goals an application model is to carry are the goals of its interaction design.
- Accepted. Standing at *baselined*, with the name of the person who accepted and the date. *Baselined* is the third of the three status words the standards of this series use — draft, reviewed, baselined (SDD-07, section 5).
- An increment of the model. The goals one writing of the application model takes in. The step is taken for each increment.
- A list of values. A governed list of coded values, as the entity model defines it: this administration's own, or held elsewhere and consumed here. A small closed set of values the entity model fixes on one attribute of one record is a list the model fixes.
- A member in force. A member of a list that has taken effect and has not been retired. A retired member stays on the records that carry it and is not offered on new ones.
- A long list. A list of values with more than nine members in force. It is divided into categories, each of no more than nine members, and a person chooses the category first and then the value (the ruling on long lists, point 1).
- A reference a person picks. A value on a screen that points at another record, and that the person, not the application, chooses.
- A record set that grows with operations. A set of records that grows as the administration works, such as its parties or its cases, as against a bounded set of stable size (UX-01, IDR-05).
- A record with a state. A record whose screens show a state that changes over its life, as the shared groundwork declares it.
- A move. A change of a record from one state to another, as the shared groundwork declares it, with what fires it and who may make it (SDD-04, IOS-11). A move a person makes is one fired by an act on a screen; every other move is the application's own, made at a run, a sweep or a refresh.
- A guard. The condition on which a move may be made, beyond the state it leaves from.
- An act. A thing a person can do on a screen, as the screen record lists it. An act that opens a form either carries a record to it, or opens a screen of its own that needs none.
- The carried record. The record an act carries to the form it opens. The form shows it filled and locked, and the record saved names it.
- A listing. One of the four tables a program produces from the accepted screen records: every coded value, every reference, every record with a state and every act (section 6).
- A pattern. One of the ways of doing a thing that the house rules require of every application and the delivery kit generates: a coded value chosen from a list of the right size and kind, a record found by a search and filling the form, a state moved only by a named act, an act carried on its record (section 4).
- A page. A clickable page that shows one pattern working with the application's own decisions, on the sample values its screen records use.
- A finding. A silence or a disagreement found in a document the step reads, recorded against that document with its owner.
- The delivery kit. The programs that validate an application model, generate the application from it, build it and deploy it. Its schema is the normative statement of what a model may say.
- The gate before, and the gate after. The owner's acceptance of the goals, which opens the step; and the delivery kit's refusal of a model that does not name the accepted interaction design, which closes it (section 8).

## 3  The step and its document

*Twenty-nine rules follow, in sections 3 to 8. Each carries an identifier for use in reviews and in traceability, and each names beneath it the source it rests on; section 12 says where the sources are kept.*

#### IXD-1 · Write the interaction design after the owner has accepted every goal the model will carry, and before the model is written
Open the step only when the owner has accepted the use case description and the screen record of every goal the application model is to carry. A goal that is not accepted is not in the step: leave it out of the model's increment rather than design it provisionally. Write no application model until its interaction design is accepted. The step comes after the review of each set of screens that SDD-01 describes, because that review is held for one goal at a time and the step reads the goals together.

*Source:* the owner's word of 25 September 2026, PROMPT_ANALYSE_the_interaction_patterns_2026-09-25.md, section 2, "The owner's decision"; the instruction that designed the step, PROMPT_DESIGN_the_interaction_design_step_2026-09-25.md, "The owner's word, 25 September 2026"; the ruling on the interaction design step, rulings/2026-09-25-the-interaction-design-step.yaml, point 2, and the plan it accepted, section 1.1.

#### IXD-2 · Admit no application model to generation without an accepted interaction design
The step cannot be skipped. An application model is admitted to generation only when it names an interaction design the owner has accepted, and the delivery kit refuses it otherwise (section 8). A step that rests on a person remembering it can be skipped by a person forgetting it, so the refusal is made by a program, at the one point every application passes.

*Source:* the owner's word, PROMPT_DESIGN_the_interaction_design_step_2026-09-25.md, "must not be skipped".

#### IXD-3 · Write one document for the application, and put it to the owner to accept
Write the step's decisions into one document for the application, or for the increment of it that the writing of the model covers, and put that document to the owner. He reviews it, and accepts it or amends it.

*Source:* the owner's word, PROMPT_ANALYSE_the_interaction_patterns_2026-09-25.md, section 2, "into one document he reviews".

#### IXD-4 · Record the owner's acceptance as baselined, with his name and the date
Give the document's status in its header in the three words the standards use — draft, reviewed or baselined — and, when it is baselined, the name of the person who accepted it and the date. A goal the step reads is accepted in the same way: its description and its screen record each stand at baselined, with a name and a date.

*Source:* SDD-07, section 5, the three status words; the operational manual, section 6.2; the owner's word, IXD-3.

#### IXD-5 · Take the step again for every increment of the model, and carry the earlier decisions forward
Whenever the application model is written again to take in goals newly accepted, bring the interaction design forward to cover them, and have it accepted again before the model is written. Carry the earlier decisions forward unchanged. Re-open one only where a new goal contradicts it, and then as a finding put to the owner.

*Source:* the owner's word, IXD-1, applied to every writing of the model; the first instance's implementation plan, IMPLEMENTATION_PLAN.md, section 5, "Six rounds for each increment of the model"; the plan the ruling accepted, section 1.3, 'The earlier decisions are carried forward and not re-opened unless a new goal contradicts one, which is then a finding with the owner'.

#### IXD-6 · Read what the entity model and the groundwork own, and decide none of it again
A list's owner and its issuer are the entity model's (SDD-03, EM-19 and EM-46 to EM-48). A record's states and moves, what fires each move and who may make it, are the shared groundwork's (SDD-04, IOS-10 to IOS-12), and so is the assignment of shared code lists (IOS-28, IOS-29). Read each from its document. Where one is silent, or disagrees with the goals, record a finding against that document with its owner, and give no answer of the step's own.

*Source:* SDD-01, section 14, "A gap is a finding with an owner, never something invented locally"; SDD-07, section 1, a specifier deciding what the model owns "has found a defect in the model".

#### IXD-7 · Where the goals are silent, say so and give the recommended answer
Where a question needs something the goals do not state — how many records a set holds, what a search takes when the identifier is not at hand, the words shown when a guard fails — say in the document that the goals are silent, give the recommended answer, and carry it in its row of the decision tables. The owner accepts it or amends it with the rest of the document.

*Source:* the owner's instruction recorded in PROMPT_ANALYSE_the_interaction_patterns_2026-09-25.md, section 5.

#### IXD-8 · Raise findings against what the step reads, and change none of it
Record every silence or disagreement found in a goal, in the entity model, in the shared groundwork or in the delivery kit as a finding against that document, with its owner. The step changes nothing it reads. A pattern the application needs that the house rules and the kit do not give is a finding against the kit, with the recommended answer stated.

*Source:* PROMPT_ANALYSE_the_interaction_patterns_2026-09-25.md, section 5, "Analyse and propose; change nothing"; SDD-01, section 14.

## 4  What every application is given, and is never asked

The step asks only what each application decides. Everything else the delivery kit generates for every application under the house rules, with no design in the application's model, and a document that decided it again would be a second copy of a rule that is kept elsewhere. The table draws the line for each subject, and says where the division comes from.

![Figure 3](figures/SDD-11/SDD-11_fig03.png)

*Figure 3 — What every application is given without design, and what each application decides.*

| Subject | Given to every application — the kit and the house rules, never asked | Decided for each application, in the step | Where the division comes from |
|---|---|---|---|
| Lists of values | the storage, the list, the form and the first values of every list; the administration of lists of values for the role that maintains them — add, relabel, reorder and retire, never delete; a retired value kept on the records that carry it and not offered on new ones; a drop-down reading its list when the form opens and offering the values in force; a cascading list filtered by its parent | whether a list is maintained or fixed, and by which role; where its first values come from; whether its code is shown as its label | the owner's word of 25 September 2026, "LOVs management should be a standard part of any application without need for manual design", and that the model may say a list is fixed or name the role that maintains it, as the instruction on the administration of lists of values records it in its section 1 |
| Long lists | no step of a selection offers more than nine values; a longer list is chosen category first; the administration of the lists grouped the same way; a check of the kit refusing a long list that has no categories | the categories of each long list | the ruling on long lists, points 1 to 3; its applied_by gives the categories to the application's own model |
| A value shown | the label only; a yes-or-no as a word; a date day first, as DD/MM/YYYY | which lists show their code as the label | the owner's findings of 25 September 2026, as the instruction for the analysis of the first instance records them in its section 2, item 1; the analysis, section 2.4; the ruling on the interaction design step, point 4 |
| A record among many | a reference to a record set that grows with operations is found by a search and never offered as a drop-down; a choice fills the form's mapped values and locks those the References table says it locks; the reference stored under the key its look-up reads | which references a person picks; how many records each set holds; whether it is searched or chosen from a bounded list; the keys of the search; the columns of the result; what the choice fills and locks; what the person is told when nothing is found | UX-01, IDR-01 to IDR-07, PRE-03 and PRE-05; SDD-09, section 14.2; the analysis of the first instance, sections 3.1 and 3.3 |
| A record's state | the state shown as a badge, never as a control; each move a button, offered only in the states it leaves and to its roles, and shown disabled with its guard's words where the guard fails; no single drop-down of actions | which act of which goal makes each move; the words of the button; the words of the guard; the values read-only in each state | UX-01, STA-01 to STA-03; the analysis of the first instance, sections 4.2 to 4.5; the states, the moves and the roles themselves are the groundwork's (SDD-04, IOS-10 to IOS-12) |
| An act that opens a form | the record carried as a read-only value, checked against its table when the form is saved; the form refused when it is reached without its record; a form that needs a record never on a visible menu | what each act carries; where it stands; what the opened form shows filled and locked; where the person returns; which forms stand on a menu | UX-01, CTX-01, CTX-02, CTX-04 and PRD-02; the analysis of the first instance, section 5.2 |

Two things the owner asked of the step stand on the given side, and the table says why: the administration of lists of values, on his word, and the three conventions for showing a value, which are his findings and the same for every application. One thing that looks given is decided for each application: the categories of a long list, because the ruling gives them to the application's model, and no program can invent a classification the business uses.

#### IXD-9 · Do not ask what every application is given
Ask nothing in the step about the administration of lists of values; the showing of a coded value by its label, of a yes-or-no as a word and of a date day first; or that a state is shown as a badge, that a move is made by a button, that an act carries its record, and that a record set that grows with operations is found by a search. The step decides only the particulars sections 5.1 to 5.4 ask of these — among them the words of a button, the record an act carries and the keys of a search. The Lists and References tables name the pattern each list and each reference takes, and the document decides nothing about a pattern's own behaviour.

*Source:* the owner's word, PROMPT_GENERATE_the_lists_of_values_administration_2026-09-25.md, section 1; the owner's findings, PROMPT_ANALYSE_the_interaction_patterns_2026-09-25.md, section 2, item 1; PROMPT_REALISE_the_interaction_patterns_in_the_kit_2026-09-25.md, "It is generic".

### 4.1  The patterns, and the three conventions

The house rules require of every application the patterns below, and the delivery kit is being made to generate each of them (PROMPT_REALISE_the_interaction_patterns_in_the_kit_2026-09-25.md). They are named here once, by the rules they rest on and by the construct of the kit's schema that realises each, so that a document can say which pattern each thing takes without describing it. The constructs are those the kit's schema carries once that round is done. Where an application needs a pattern the house does not have, IXD-8 applies.

| Pattern | What a person sees | The house rules it rests on | What realises it in the kit |
|---|---|---|---|
| L1 · a short fixed list | a drop-down, or for two or three values a group of radio buttons, showing each value's label and storing its code; where the value may only be read, a labelled value and never a disabled drop-down | UX-01, IDR-05 and TRM-02 | a vocabulary of the model and an attribute bound to it; a read-only coded value projected as text showing its label |
| L2 · a list the administration maintains | a drop-down whose values are read from the list when the form opens, offering the values in force; a retired value kept on the records that carry it | UX-01, IDR-05 and TRM-02 | the administration of lists of values the kit generates for every vocabulary; a vocabulary marked fixed, or naming the role that maintains it |
| L3 · a list that depends on another value | a drop-down whose values follow a value already on the screen, never offered whole | UX-01, IDR-05 | by equality, a vocabulary naming its parent; by a rule, a field naming the query that yields its values |
| L4 · a list held elsewhere | the label the body that holds the list gives; no screen of the application maintains it | UX-01, MDM-02 | a vocabulary consumed from its source, and marked so |
| A long list, chosen by category | two drop-downs: the category, then the values of that category in force | UX-01, IDR-05, as the ruling on long lists amends it | a vocabulary naming the vocabulary of its categories, each value naming its category |
| S1 · the search | a record of a set that grows with operations, found by its identifier or by a fragment of its name, from a result whose columns tell two records of the same name apart; a message with the next steps when nothing is found | UX-01, IDR-01 to IDR-07 | a look-up on a typed key; a search control over a register; a pop-up search over a list of the application's own records |
| S2 · the filling-in | the choice fills the form from the record chosen, and locks what the References table says it locks, shown as labelled values | UX-01, PRE-03 and PRE-05 | the prefill of a form, with its mappings |
| T · the lifecycle | the state shown as a badge, with since when; each move a button named after it, offered only in the state it leaves and to its roles, and disabled with the guard's words where the guard fails; no single drop-down of actions | UX-01, STA-01 to STA-03 and CTX-02 | the lifecycle's transitions, with their roles and guards; the acts of a form, projected as buttons, each firing its move through a trigger form of its own |
| A · the act on its record | an act that belongs to a record is offered only on that record and carries it to the form it opens, which shows the record's standing header filled and locked; the person is returned where the goal says; the menu offers only what stands without a record | UX-01, CTX-01, CTX-02, CTX-04 and PRD-02 | the acts of a form, each naming what it carries; the carried reference, a read-only field checked when the form is saved; a hidden category of the navigation for the forms a row opens |

The three conventions for showing a value are given to every application and not asked. A coded value shows its label only, unless its list is marked to show its code as its label (IXD-12). A yes-or-no shows as the word Yes or No where it is read, and as a check-box where it is entered. A date shows day first, as DD/MM/YYYY, which the ruling of 25 September 2026 on the interaction design step settles at its point 4.

## 5  The four questions

The step asks four questions, one of each kind of thing a person does that the goals leave unsettled. Each is asked once for each thing the goals hold: each list once, and not each value that draws on it; each place a person picks a record; each record with a state; each act that opens a form. Each part of each question either reads its answer from a document the step takes in, or is decided in the step and accepted by the owner. The answers go into the five tables of section 7.

### 5.1  Of every list of values the goals draw on

Read where the list is kept — this administration's own, or held elsewhere and consumed here — from the entity model's table of governed lists and the groundwork's assignment of shared code lists, and count its members in force. Then decide what the five rules below ask. The list's row of the Lists table carries what was read and what was decided.

#### IXD-10 · Decide whether each list is maintained in the application or fixed by the model, and which role maintains it
For each list of values the goals draw on, decide whether the application maintains it or the model fixes it, and name the role that maintains a list the application maintains. When nothing else is said, the list is maintained by the administrator.

*Source:* the owner's word, PROMPT_GENERATE_the_lists_of_values_administration_2026-09-25.md, section 1.

#### IXD-11 · Say where each list's first values come from
For each list, name where the values it starts with come from: the entity model's own members of the list, for instance, or, for a list held elsewhere, the values the screen records use, marked as starting data until the list is read from the body that holds it.

*Source:* PROMPT_ANALYSE_the_interaction_patterns_2026-09-25.md, section 4, item 1; the analysis of the first instance, INTERACTION_PATTERNS.md, section 2.1.

#### IXD-12 · Decide whether each list's code is what the officers say, and so shown as its label
A coded value shows its label only. Where a list's own code is itself what the officers say and write — a category known by its letter and number, a tax known by its abbreviation — decide that the list shows its code as its label, and record the decision on the list's row.

*Source:* the analysis of the first instance, INTERACTION_PATTERNS.md, section 2.4; PROMPT_TIDY_the_kit_second_pass_2026-09-25.md, item 13, the owner's word amending TRM-02.

#### IXD-13 · Decide whether each list depends on another value, and whether by equality or by a rule
Where the values a person may choose follow a value the record already holds, name that value, and say whether the dependence is an equality — the values whose parent is the value held — or a rule, such as the values available at a level at or below the record's and switched on. A list that depends on another value is never offered whole. A dependence by a rule that the kit cannot yet express is a finding against the kit (IXD-8).

*Source:* the analysis of the first instance, INTERACTION_PATTERNS.md, section 2.3, pattern L3, and section 7.3.

#### IXD-14 · Give every long list its categories
Give a list of values with more than nine members in force its categories, none holding more than nine; a person chooses the category first and then the value, and with more than nine categories a further level is added. The categories are the application's to give, because no program can invent a classification the business uses: give them in the Lists table, and name each value's category. The categories are themselves a list of values, maintained like any other.

*Source:* rulings/2026-09-25-long-lists-are-chosen-by-category.yaml, points 1 and 2 and applied_by.

### 5.2  Of every reference a person picks

For each place on the goals' screens where a person picks a record, read the record set pointed at and its size, and decide how the record is found, what a search takes, what the result shows, what choosing it fills and locks, and what the person is told when nothing is found. That a record set growing with operations is found by a search and never chosen from a drop-down is given to every application (section 4); the step decides which references a person picks, and their search, result and filling.

#### IXD-15 · Name the record set each reference points at, and how many records it holds
For each reference a person picks, name the record set it points at, and state its size at the median and at the ninety-ninth in a hundred (P50 and P99), or that it grows with operations. Where the goals do not state it, say so, and give the best figure available with where it came from (IXD-7). The size decides whether the record is found by a search or chosen from a bounded list.

*Source:* UX-01, section 5, question 6, and IDR-05; PROMPT_ANALYSE_the_interaction_patterns_2026-09-25.md, section 4, item 2.

#### IXD-16 · State what each search takes, and what its result shows
For each reference found by a search, state its keys: the identifier first (IDR-02), and, as the fallback where no identifier is at hand, the attributes a person may search by, a fragment of the name among them (IDR-03). State the columns of the result, chosen so that two records of the same name can be told apart. A search by name returns a list to choose from, and the person chooses from it.

*Source:* UX-01, IDR-02, IDR-03.

#### IXD-17 · State what choosing a record fills on the form, and which of the filled values are then locked
For each reference a person picks, state which values of the form are filled from the record chosen, and which of those are locked once filled. A filled value is carried and never typed again; a locked value is shown as a labelled value.

*Source:* UX-01, PRE-03, PRE-05; SDD-07, section 6, the second question; PROMPT_ANALYSE_the_interaction_patterns_2026-09-25.md, section 4, item 2.

#### IXD-18 · State what the person is told when nothing is found
For each search, state what the person is told when nothing is found, and the next steps offered: the criteria to widen, the document to check, the way a record is registered where the person may use it, or whom to ask. Never offer a way to type the reference in instead.

*Source:* UX-01, IDR-07.

### 5.3  Of every record with a state that the goals' screens show

Read each record's states and moves, what fires each move and who may make it, from the shared groundwork. Decide, for each move a person makes, the act that makes it, the words of its button and the words of its guard; and, for each state, which values become read-only. Every other move is the application's own, and no screen offers it.

#### IXD-19 · Name the act of the goal that makes each move a person makes
For each move of a record that a person makes, name the goal, and the act on its screen, that makes it.

*Source:* PROMPT_ANALYSE_the_interaction_patterns_2026-09-25.md, section 4, item 3; the analysis of the first instance, INTERACTION_PATTERNS.md, section 4.2.

#### IXD-20 · Give each move's button the goal's own words, and each guard the words shown when it fails
The button that makes a move carries the goal's own words for the act. Where the state allows the move and its guard does not, the button is shown disabled, with the guard's reason in words a person reads. State both in the Moves table.

*Source:* UX-01, STA-01, STA-02; the analysis of the first instance, INTERACTION_PATTERNS.md, section 4.5.

#### IXD-21 · State which values become read-only in which state
For each record with a state, state which of its values become read-only in each state, in the Read-only table.

*Source:* PROMPT_ANALYSE_the_interaction_patterns_2026-09-25.md, section 4, item 3; the analysis of the first instance, INTERACTION_PATTERNS.md, section 4.4.

#### IXD-22 · Read who may make each move from the groundwork, and decide it nowhere else
The role that may make a move is the shared groundwork's, which requires it of every move. Carry it into the Moves table as it is read there. A move for which the groundwork names no role is a finding against the groundwork, and not a role the step supplies.

*Source:* SDD-04, IOS-11, "Every move is fully declared — from, to, what fires it, who may".

### 5.4  Of every act that opens a form

#### IXD-23 · For every act that opens a form, state where it stands, what it carries, what the form shows filled and locked, where the person returns, and whether it may stand on a menu
For each act of the goals' screens that opens a form, state where it stands — on a row of a list, on a record's own screen, or on a menu; the record it carries; what the opened form shows filled and locked from that record; where the person returns afterwards; and whether the form may stand on a menu, which it may only when it needs no record.

*Source:* PROMPT_ANALYSE_the_interaction_patterns_2026-09-25.md, section 4, item 4; UX-01, CTX-01, CTX-02, CTX-04, PRD-02.

## 6  The listings and the pages

The decisions are measured against something the step did not write. The screen records of the goals already name, for another purpose, every coded value, every reference, every record with a state and every act, and a program lists them. Every list in the first listing has a row of the Lists table; every reference a person picks in the second has a row of the References table; every record in the third has its rows of the Moves and Read-only tables; and every act that opens a form in the fourth has a row of the Acts table. The pages show the decisions working, for the owner to try before he accepts them.

#### IXD-24 · Produce the four listings by a program from the accepted screen records, and compare them with the records as sets
Produce, by a program and never by typing, four listings from the accepted screen records: every coded value, with the list it draws on; every value that points at another record, with whether the person picks it; every record whose state a screen shows; and every act, with where it stands and where it leads. Compare each listing with the screen records as sets, and not by counts alone. Name the program in the document's header by its path and its checksum, so that it can be run again. The program reads the form the application's screen records are written in, and is kept with the application's other programs.

*Source:* PROMPT_ANALYSE_the_interaction_patterns_2026-09-25.md, section 6, A2; the analysis report, REPORT_ANALYSE_the_interaction_patterns_2026-09-25.md, section 5, the sixth correction; SDD-01, section 3, the second rule; the plan the ruling accepted, section 3.2, 'The program is named in the document by path and checksum so that it can be run again'.

#### IXD-25 · Show each pattern the application uses on a clickable page produced by a program
For each pattern the application uses, produce one clickable page that shows the application's own decisions working on the sample values its screen records use. Each page is one file that opens in an ordinary browser with nothing fetched. It is produced by a program and never edited by hand.

*Source:* PROMPT_ANALYSE_the_interaction_patterns_2026-09-25.md, section 4, item 5; SDD-01, section 14, "What software generated is never edited by hand"; SDD-07, rules 23 and 24, which say this of the walk-through, applied to the pages as the plan's section 3.4 applies them.

## 7  The form of the document

The document has seven parts, in this order.

1. The header: its identifier, its version and its status in the three words, with the owner's name and the date when it is baselined; every goal it covers, each by its identifier, with the version of its description and of its screen record; and the program that produced its listings, by path and checksum.
2. The answer in one paragraph: how many lists, references a person picks, records with a state and acts that open a form the goals hold; what the owner is asked to accept; and on what the goals were silent.
3. The decisions, in the five tables below.
4. The pages, one for each pattern the application uses (IXD-25).
5. Where the goals were silent, each with the recommended answer and the row of a decision table that carries it (IXD-7).
6. The findings raised, each against the document that owns the fact, with its owner (IXD-8).
7. The appendix: the four listings, and the program's comparison of them with the screen records (IXD-24).

![Figure 4](figures/SDD-11/SDD-11_fig04.png)

*Figure 4 — The seven parts of the document, and who reads which.*

#### IXD-26 · Open the document with the answer in one paragraph
Open the document, after its header, with one paragraph that says how many lists, references a person picks, records with a state and acts that open a form the goals hold; what the owner is asked to accept; and on what the goals were silent.

*Source:* PROMPT_ANALYSE_the_interaction_patterns_2026-09-25.md, section 4 and criterion A1; the plan the ruling accepted, section 3.4, part 2.

#### IXD-27 · Hold the decisions in five tables with fixed column headings
Hold every decision in one of the five tables below, with the column headings exactly as they stand, because a program reads them: the delivery kit's gate compares the application model with them (section 8). Add no column and rename none.

*Source:* the operational manual, section 6.2.

| Table | One row for | Its columns |
|---|---|---|
| Lists | each list the goals draw on | List · Kept where · Members in force · Maintained or fixed · Maintained by · First values from · Code shown as label · Depends on · Categories · Pattern |
| References | each place a person picks a record | Place · Record set · How many · Found by · Searched by · Result shows · Fills · Locks · When nothing is found · Pattern |
| Moves | each move a person makes | Record · From · To · Made by (goal, act) · Role · Button · Guard, in the words shown |
| Read-only | each record with a state | Record · State · Values read-only in it |
| Acts | each act that opens a form | Act · Stands on · Carries · Opens · Filled and locked · Returns to · On a menu |

A set of values the entity model fixes on one attribute of one record is a row of the Lists table like any other list, fixed by the model. A list held elsewhere is fixed here: the application does not maintain it (UX-01, MDM-02), and its *Maintained by* says that it is read from the body that holds it. In the Moves table, *Button* is the words of the button on the record's screen, and *Made by (goal, act)* names the goal and the act that makes the move, which may be the act of a form the button opens. A move the application makes by itself has no row of the Moves table, because no person makes it. Where a record's values become read-only in more than one state, the record has a row of the Read-only table for each such state; where the same values are read-only in every state, one row whose *State* reads 'every state' stands for them.

#### IXD-28 · Put before the owner the answer, the decision tables and the pages
What the owner reads, and accepts, is the header, the answer, the decision tables and the pages. The listings and their comparison are for the writer of the application model and for the gate; the owner is not asked to read them.

*Source:* PROMPT_DESIGN_the_interaction_design_step_2026-09-25.md, section 3, item 3.

## 8  The gate after the step

The owner's word is that the step is not to be skipped, and a step that rests on a person remembering it can be skipped by a person forgetting it. So the step is closed by a program, at the one point every application passes: the admission of its application model to generation. This section describes what the delivery kit enforces. The refusal is the kit's, and not a rule of this standard, and it is built in the kit by a round of its own; until that round is done, it is described here and is not yet enforced.

![Figure 5](figures/SDD-11/SDD-11_fig05.png)

*Figure 5 — The gate after the step: what the model names, and the four places the kit refuses it.*

### 8.1  What the model names

The application model's `model` section carries one entry, `interaction_design`, which names the accepted document by its path relative to the model and by its SHA-256 checksum. Whoever writes the model writes the entry from the accepted document. It is the model's statement of what it was compiled from, which SDD-07, section 15, already requires of a model, and which no model has yet carried.

### 8.2  What the kit refuses

A rule of the kit's validator, reported as an error and never as a warning, refuses a model:

1. that names no interaction design;
2. that names a file which is not there;
3. whose checksum is not the file's;
4. whose document's header does not stand at baselined, with a name and a date;
5. whose document does not cover a goal the model's forms and lists name;
6. whose lists disagree with the Lists table: maintained or fixed, the role that maintains, the categories of a long list, or the code shown as its label, other than the decision;
7. whose references disagree with the References table: a reference the table says is found by a search, placed as a drop-down, a group of radio buttons or a check-box; or fills and locks other than the table's;
8. whose moves disagree with the Moves table: a move the table lists with no act on its record's form carrying the table's words and role, or an act for a move the table does not list as a person's;
9. whose acts disagree with the Acts table: an act the table says carries a record that does not carry it, or its form on a visible menu where the table says it may not stand there.
Checks 6 to 9 compare each row of a table with the construct of the model that carries it. How a row names that construct, and the words the gate reads in each column it compares, are fixed by the template of the document that the delivery kit's round building the gate adds; this standard fixes the headings and what each column means.

### 8.3  Where it refuses, and what cannot turn it off

The refusal stands in the kit's validation, and — because a check made by one command is skipped by calling another — at the start of generation, of the build and of the deployment, each of which calls the same check before anything else and refuses on it. No switch turns it off: not a key in the model, not a line of the kit's settings, not the custody mode, not a flag on a command. The kit's worked reference, its test fixtures and a model harvested from a running application are no exception: each is given an interaction design, or is refused.

### 8.4  How it is shown to work

By controls, each run by the kit's tests, each failing on the kit before the gate is built and passing after it, in every custody mode. The model of an application written before this step, which names no interaction design, is refused at all four places. The kit's worked reference, given a small interaction design of its own, is admitted. The worked reference with its entry removed, with its checksum one character off, with its document set back to reviewed, and with one change for each of the checks 6 to 9, is refused each time, naming the check and the row of the document it disagrees with.

The gate rests on the owner's word that the step is not to be skipped (IXD-2); on SDD-07, section 15, which requires a model to name what it was compiled from; and on SDD-01, section 14: "A refusal is answered, not worked around".

#### IXD-29 · Have a document changed after acceptance accepted again, and named again, before a model is admitted
What the owner accepted is the document he read. A document changed after it was accepted is accepted again before any model is written from it, and the model names it again by its new checksum. A model that names the old checksum is refused, because that checksum is no longer the file's.

*Source:* the owner's word, IXD-3, what he accepts is the document he read; SDD-01, section 5, a version not the record's "is stale, and nothing is reviewed from it, agreed on it, or built from it".

## 9  The review

Run this before the document is put to the owner for acceptance, and again whenever it is brought forward for an increment of the model. Its writer runs it. The document is put to the owner only when every applicable line is satisfied or recorded as a finding with a named owner; a line that is not satisfied is not an exception to be set aside.

| Rules | Checkpoint | Passed |
|---|---|---|
| IXD-1, IXD-5 | Every goal the document covers is accepted, its description and its screen record at baselined with a name and a date, each named with its version. No goal that is not accepted is designed. Earlier decisions are carried forward, and any that is re-opened is a finding put to the owner. | ☐ |
| IXD-2, IXD-29 | The document's path and checksum are those the application model will name; nothing in it has changed since it was accepted without being accepted again. | ☐ |
| IXD-3, IXD-4 | One document for the application or the increment; its status in the three words; when baselined, the owner's name and the date. | ☐ |
| IXD-6 | Nothing the entity model or the groundwork owns is decided in the document; every silence or disagreement there is a finding with that document's owner. | ☐ |
| IXD-7, IXD-8 | Every silence of the goals is stated with its recommended answer and the row that carries it; every finding names its document and its owner; nothing the step read was changed. | ☐ |
| IXD-9 | No row decides what every application is given; each row names its pattern and only the particulars that pattern needs. | ☐ |
| IXD-10 to IXD-14 | Every list in the first listing has a row of the Lists table, saying whether it is maintained or fixed and by whom, where its first values come from, whether its code is shown as its label, and what it depends on and how; every long list has its categories, none holding more than nine. | ☐ |
| IXD-15 to IXD-18 | Every reference a person picks in the second listing has a row of the References table, with its record set and its size, how it is found, its keys and the columns of its result where it is searched, what it fills and locks, and what the person is told when nothing is found. | ☐ |
| IXD-19 to IXD-22 | Every move a person makes, of every record in the third listing, has a row of the Moves table, with its goal and act, its role as the groundwork gives it, the words of its button and the words of its guard; every state in which values become read-only has a row of the Read-only table. | ☐ |
| IXD-23 | Every act in the fourth listing that opens a form has a row of the Acts table; no form that needs a record stands on a menu. | ☐ |
| IXD-24, IXD-25 | The four listings were produced by the program the header names, and compared with the screen records as sets; every pattern the application uses has its page, produced by a program. | ☐ |
| IXD-26 to IXD-28 | The document has its seven parts, in order; it opens with the answer; the five tables carry their headings exactly; the owner is asked to read the header, the answer, the tables and the pages. | ☐ |

What this review does not do. Every line above tests something that is recorded, measured or named. None of them asks whether a decision is the right one — whether a list's categories are those the business uses, whether a guard's words will be understood, whether a search's keys are those the officers have at hand. That is the owner's reading, and section 11 states the limit it leaves.

## 10  A worked example

*This is a simulated case for Progressa, a fictional country; every institution, name, date and figure in it is invented. In this copy of the standard it replaces the worked example of the edition of record, which was drawn from a real application, so that the example rests on nothing outside the courses it is published with.*

The example is the interaction design of PHEQA's application: the application of the Progressa Higher Education Quality Authority, across the six goals of its first increment. The goals are those of PHEQA's application in the courses' fact sheet: an applicant applies for a provisional licence, the finance officer records the fee, an inspector records a visit, the registration officer recommends a decision to the minister, an institution appeals against a decision of PHEQA, and the registration officer records the minister's decision on a licence.

The rows below are cut from the document's five tables, and only some rows are shown; where the goals did not decide a column, the cell says so. It shows the form; the document the Registrar of PHEQA accepts is written to this standard in full.

### 10.1  The header and the answer

| Part of the header | In the example |
|---|---|
| Identifier, version and status | IXD-PHEQA, version 0.1; draft |
| The goals covered | Apply for a provisional licence (G-01), its description at version 1; Record the application fee (G-02), version 1; Record an inspection visit (G-03), version 1; Recommend a decision to the minister (G-04), version 1; Appeal against a decision of PHEQA (G-05), version 1; Record a decision on a licence (G-07), version 1. Their screen records: G-01, G-02, G-03, G-04 and G-05 at version 1; the record of G-07 states no version at its head, which is a finding against the goals |
| Their status | baselined, all twelve documents, each with the name of the Registrar of PHEQA and the date she accepted it, 27 November 2026 (IXD-1, IXD-4) |
| The program of the listings | the interaction design skill's program of the listings, named by its path and its checksum (IXD-24) |

The answer. The six goals draw on six lists: three PHEQA decides, two held elsewhere and fixed by Progressa's Higher Education Regulations, and one set of values the entity model fixes on the licence. One of them has more than nine members: the matters PHEQA advises the minister on, with twenty. At four places a person picks one record out of others, the largest an institution among the entries of the register of institutions. One record carries a state a screen shows, and the goals move it: the licence, by five moves, each recorded by the registration officer on a decision someone is entitled to make. Of the 48 acts on the screens, 9 open a form or a screen: 6 on a row of a list and 2 on an application from its workspace carry a record, and 1 opens a screen of its own. The Registrar of PHEQA is asked to accept the decision tables, the four pages, and the recommendations where the goals are silent.

### 10.2  The decisions, in part

The tables are shown in two parts where they are wider than this page, each part carrying the table's first column; the document itself keeps each table whole, because a program reads it.

The Lists table, its first part:

| List | Kept where | Members in force | Maintained or fixed | Maintained by |
|---|---|---|---|---|
| kind of institution | PHEQA's own, a shared code list | 3 | maintained | the Registrar of PHEQA |
| kind of licence | held elsewhere, read here: the Regulations | 2 | fixed here | nobody here: fixed by the Regulations |
| matter of advice | held elsewhere, read here: the Regulations | 20 | fixed here | nobody here: fixed by the Regulations |
| outcome of an inspection | PHEQA's own | 4 | maintained | the Registrar of PHEQA |
| ground of appeal | PHEQA's own | 6 | maintained | the Registrar of PHEQA |
| state of a licence | fixed by the entity model on the licence | 3 | fixed | nobody: the model fixes it |

The Lists table, its second part:

| List | First values from | Code shown as label | Depends on | Categories | Pattern |
|---|---|---|---|---|---|
| kind of institution | the entity model's members | no | nothing | none: three members | L2 |
| kind of licence | the Regulations, as starting data | no | nothing | none | L4 |
| matter of advice | the Regulations, as starting data | no | nothing | given: licences, eight; suspension and cancellation, seven; other matters, five | L4, a long list |
| outcome of an inspection | the entity model's members | yes: A to D are what the inspectors write on their reports | nothing | none: four members | L2 |
| ground of appeal | the entity model's members | no | the kind of decision appealed against, by a rule: only the grounds the Regulations allow against that kind of decision | none: six | L3, by a rule |
| state of a licence | the entity model's members | no | nothing | none: three | L1 |

The References table, its first part:

| Place | Record set | How many | Found by | Searched by |
|---|---|---|---|---|
| Find the institution an application concerns (G-03, screen S1) | the institutions, in PHEQA's register of institutions | 214 entries today; it grows with operations | a search | the register number, written like INS-00217; the goals are silent on the name |
| Choose the inspector for a visit (G-03, screen S2) | the officers who hold the inspector's role | six in the sample; about a dozen in life | a bounded list | nothing: by name; the goals are silent on how the list is narrowed |
| Find the application a fee is recorded against (G-02, screen S1) | the applications PHEQA has received | it grows with operations | a search | the application's number |
| Choose the decision an appeal is against (G-05, screen S1) | the decisions of PHEQA on the institution | one to a few | a bounded list | nothing: shown whole |

The References table, its second part:

| Place | Result shows | Fills | Locks | When nothing is found | Pattern |
|---|---|---|---|---|---|
| Find the institution an application concerns | register number, name, kind, and the state of its licence | the institution's register number, name and kind | all of them | "No institution is registered under INS-00999. Check the number against the letter it came from, or search by a part of the name" | S1, S2 |
| Choose the inspector for a visit | the officer's name, and the visits she holds this month | the visit's inspector | the inspector, once the visit is set | the act names the missing inspector | S2, from a bounded list |
| Find the application a fee is recorded against | number, institution, date received, and whether a fee is recorded | the application's number and institution; the fee due | all of them | "No application has the number given. Check it against the receipt the applicant holds" | S1, S2 |
| Choose the decision an appeal is against | each decision's kind, date and reference | the appeal's decision | the decision | the act names the missing decision | S2, from a bounded list |

The Moves table, the licence's rows:

| Record | From | To | Made by (goal, act) | Role | Button | Guard, in the words shown |
|---|---|---|---|---|---|---|
| licence | none | granted | in G-07 the act Record the grant, reached from Record the minister's decision | the registration officer, on the minister's decision | Record the grant | "No decision of the minister to grant this licence has been received from MoEYS." |
| licence | granted | suspended | in G-07 the act Record the suspension | the registration officer, on the minister's decision | Record the suspension | "No decision of the minister to suspend this licence has been received from MoEYS." |
| licence | suspended | granted | in G-07 the act Record the end of the suspension | the registration officer, on the minister's decision, given on PHEQA's advice | End the suspension | "No decision of the minister to end this suspension has been received from MoEYS." |
| licence | granted or suspended | cancelled | in G-07 the act Record the cancellation | the registration officer, on the minister's decision | Record the cancellation | "No decision of the minister to cancel this licence has been received from MoEYS." |
| licence | cancelled | the state it held before | in G-07 the act Record that the cancellation is set aside | the registration officer, on a decision on appeal or on review | Set the cancellation aside | silent on the words, which the goals do not give |

A licence moves only on a decision someone is entitled to make: the minister's under article 11 of the Regulations, or a decision on appeal or on review. No move of the licence is the application's own, and no screen offers a move without the decision it rests on.

![Figure 6 — The worked example: the moves a person makes on one record, each by a named act.](figures/SDD-11/SDD-11_fig06.png)

*Figure 6 — The worked example: the moves a person makes on one record, each by a named act.*

The Read-only table, in part:

| Record | State | Values read-only in it |
|---|---|---|
| licence | every state | the institution, the kind of licence, and the decision that set the state; a person changes the state only through the acts of G-07 |
| application | received | every particular the applicant gave; a correction is a new version of the application, which names the one it corrects |
| inspection record | recorded | everything; a correction is a new record that names the one it corrects |

The Acts table, in part:

| Act | Stands on | Carries | Opens | Filled and locked | Returns to | On a menu |
|---|---|---|---|---|---|---|
| Record a visit (G-03, screen S1, act A02) | a row of the inspector's list of applications awaiting a visit | the application, by its number | screen S2 of G-03 | the application's header | the inspector's list | no |
| Recommend a decision (G-04, screen S1, act A04) | the application's act bar | the application, by its number | screen S2 of G-04 | the application's header, and the outcome of its inspection | the application's workspace | no |
| Record the fee (G-02, act A01) | a row of the finance officer's list of fees awaiting confirmation | the application, by its number | screen S1 of G-02 | the application's header, and the fee due | the finance officer's list | no |
| Record the minister's decision (G-07, act A01) | a row of the registration officer's list of decisions received from MoEYS | the licence, by the institution's register number | screen S1 of G-07 | the institution's header, and the decision received | the registration officer's list | no |
| Applications awaiting a visit (G-03, screen S0, act A00) | the inspector's work list, a screen of its own | nothing but the signed-in person | the list of applications awaiting a visit | nothing | silent | yes: a screen that stands without a record |

The application's act bar is the row of acts on the application's workspace, and the application's header is its standing header (UX-01, CTX-02): its number, its institution, the kind of licence asked for, the version of PHEQA's standards it was made under, and the date it was received. The institution's header carries its register number, its name, its kind and the state of its licence.

### 10.3  Where the goals were silent, and the findings raised

The goals are silent on three things a question needs, and the document recommends an answer to each:

- how an institution is found when its register number is not at hand. Recommended: the search takes the number or a fragment of the name, and a search by name returns a list to choose from. It is carried in the institution's row of the References table;
- how the list of inspectors for a visit is narrowed. Recommended: the officers who hold the inspector's role, by name, with the visits each holds this month. It is carried in the visit's row;
- the categories of the one long list, the matters PHEQA advises the minister on, which the ruling on long lists gives to the application's model. Recommended: licences, suspension and cancellation, and other matters, the words PHEQA's officers already use. They are carried in the list's row.
The findings raised, each against the document that owns the fact:

- against the shared groundwork: its table of the licence's moves names the decision that fires the move that sets a cancellation aside, and not who records it, so the role of the Moves table is taken from the goals until it does (IXD-22);
- against the entity model: a member of a list PHEQA decides carries no date it took effect or was retired, so no drop-down can offer the members in force at the moment a screen names;
- against the goals: the act that opens the form to record a fee does not say what it carries, and the words shown when a cancellation is set aside are not given;
- against the goals: the screen record of G-07 states no version at its head, so the header cannot name the version of every screen record it covers (IXD-4).

### 10.4  Reading the example against the rules

The example shows the two halves of the step. What it decides is on the rows: the matters of advice are a long list, whose categories are the application's to give (IXD-14); the outcome of an inspection is known to the inspectors by its letter, and is shown with its code as its label (IXD-12); the grounds of appeal depend on the decision appealed against by a rule, which the row names (IXD-13). What it does not decide is absent: no row says how a list is administered, how a date is shown, or that the licence's state is a badge, because every application is given those (IXD-9). The licence has five moves, all made by a person on a decision, and each has its row of the Moves table (IXD-19). The role on the last row comes from the goals because the shared groundwork names none, which is a finding against the groundwork and not a role the step supplies (IXD-22). And the example can be accepted only once the finding against the goals on the version of G-07's screen record is answered: until then the header cannot name every version it covers (IXD-4).

## 11  The questions this standard does not answer

A standard that hides what it cannot yet say is worse than one that names it. Five things are not settled here.

### Whether a decision is the right one

The review of section 9 and the gate of section 8 test that every decision is recorded, measured against the listings, and carried into the model. Neither tests whether it is the right decision: whether a list's categories are those the business uses, whether the words of a guard will be understood, whether the keys of a search are those the officers have at hand. The owner's reading of the answer, the tables and the pages is the only test of that, and a document that passes the review has been shown to be complete and nothing more. A reviewer should read the result that way.

### What holds the step before the gate is built

Until the delivery kit's gate is built, nothing mechanical stands between a model and its generation, and IXD-2 rests on the order in which the work is commissioned. The procedure by which the writing of a model is commissioned, and the plan of each application, are brought into line with the step by the rounds that place this standard in the method; they are not this standard's to write.

### A pattern the house does not have

The step can find that an application needs a pattern the house rules and the delivery kit do not yet give, as the first instance found a list narrowed by a rule. It records a finding against the kit, with the recommended answer (IXD-8), and the model cannot carry the decision until the kit can say it. How long an application waits on such a finding is not settled here.

### A date written month first into a model

Every application is given dates shown day first, as DD/MM/YYYY. Nothing in this standard refuses a model that writes a month-first format into its conventions; that refusal belongs to the kit's schema, and until the kit has it the question stays open.

### How the listings are read from a screen record

The delivery kit holds no template of a screen record, so the program that produces the listings reads the form in which each application's screen records are written, and it is the application's own (IXD-24). An application whose screen records are written in another form needs a program of its own, until the method has one form for a screen record.

## 12  Where these rules come from

This standard draws its rules from the plan of 25 September 2026 for the interaction design step, _working/2026-09-25_interaction_design_step/PLAN.md, its Appendix B, written on the owner's word of the same day and accepted by the ruling that made the step and this standard (rulings/2026-09-25-the-interaction-design-step.yaml). Every rule names its source beneath it. The sources are of four kinds: the owner's word, as a ruling or an instruction records it; a rule of the house rules, UX-01; a finding of the analysis of the first instance, or of the report on it; and a statement of a standard of this series or of the method's operational manual. Where a rule carries a particular that the plan settled and the source Appendix B gives does not state, its source line also names the plan's section, which the ruling accepted. What holds only for the application the analysis was written for appears in section 10 and nowhere else.

- The rulings: rulings/2026-09-25-the-interaction-design-step.yaml, which made the step and this standard, settled the date convention at its point 4, and reserved to the owner, at its point 5, whether this standard comes into force; and rulings/2026-09-25-long-lists-are-chosen-by-category.yaml.
- The owner's word on the administration of lists of values, as the instruction that carried it records it: _prompts/PROMPT_GENERATE_the_lists_of_values_administration_2026-09-25.md, section 1. The instruction that designed this step: _prompts/PROMPT_DESIGN_the_interaction_design_step_2026-09-25.md. The rounds that make the delivery kit give every application its patterns: _prompts/PROMPT_REALISE_the_interaction_patterns_in_the_kit_2026-09-25.md and _prompts/PROMPT_TIDY_the_kit_second_pass_2026-09-25.md.
- The first instance: the analysis, INTERACTION_PATTERNS.md; the instruction it answered, PROMPT_ANALYSE_the_interaction_patterns_2026-09-25.md, which records the owner's word and his findings of 25 September 2026; the report on it, REPORT_ANALYSE_the_interaction_patterns_2026-09-25.md; and the implementation plan of its application, IMPLEMENTATION_PLAN.md. They stand in the engagement where the step was first taken, and are not part of this kit; section 10 of this copy carries a simulated example in their place.
- The house rules for what a person sees, UX-01: its section 5, and its rules IDR-01 to IDR-07, PRE-03, PRE-05, STA-01 to STA-03, CTX-01, CTX-02, CTX-04, PRD-02, TRM-02 and MDM-02.
- The standards of this series: SDD-01, sections 3, 4, 5 and 14; SDD-03, EM-19 and EM-46 to EM-48; SDD-04, IOS-10 to IOS-12, IOS-28 and IOS-29; SDD-07, sections 1, 5, 6 and 15, and rules 23 and 24; SDD-09, section 14.2. And the operational manual of the method, Specification_Driven_Development_Method_Operational_Manual_v2.docx, section 6.2.
The rules of this standard carry the plan's rules as follows.

| Rule | The plan's rule |
|---|---|
| IXD-1 | P01 |
| IXD-2 | P02 |
| IXD-3 | P03 |
| IXD-4 | P04 |
| IXD-5 | P05 |
| IXD-6 | P06 |
| IXD-7 | P07 |
| IXD-8 | P30 |
| IXD-9 | P31 |
| IXD-10 | P08 |
| IXD-11 | P09 |
| IXD-12 | P10 |
| IXD-13 | P11 |
| IXD-14 | P12 |
| IXD-15 | P13 |
| IXD-16 | P15 |
| IXD-17 | P16 |
| IXD-18 | P17 |
| IXD-19 | P18 |
| IXD-20 | P20 |
| IXD-21 | P21 |
| IXD-22 | P22 |
| IXD-23 | P23 |
| IXD-24 | P25 |
| IXD-25 | P26 |
| IXD-26 | P27 |
| IXD-27 | P28 |
| IXD-28 | P29 |
| IXD-29 | P36 |

Nine of the plan's thirty-eight rules land elsewhere and are not rules of this standard. That a record set growing with operations is found by a search (P14), that a state is shown and changed only by a named act (P19), and that an act belonging to a record opens only from it (P24) are given to every application, and section 4 names them. That the model names the accepted document (P32), and that the delivery kit refuses a model that does not, or that contradicts it, at every entry point and in every custody mode (P33 to P35), are the gate of section 8, which is the kit's. Where the thing takes its place in the method's order (P37) is SDD-01's, and when the writing of a model may be commissioned (P38) is the orchestrator's procedure.

How firm these rules are. They were written from one analysis of one application, and none of them has yet been used by anybody who did not write it. Whether any meets this organisation's bar for adopting a rule — a recognised discipline stating it, and the same practice found in at least two independent fields — has not been searched, and every rule should be read as not tested. The first interaction design written to this draft, claiming conformance rule by rule and reporting every point at which the standard was silent, wrong or unclear, is the test; after it the owner decides whether the standard comes into force as version 1.0, which is the point the ruling reserves to him. Until then it is a draft and should not be quoted as binding.
