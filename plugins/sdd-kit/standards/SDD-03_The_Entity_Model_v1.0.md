# SDD-03 · The Entity Model

*This copy is carried by sdd-kit, the SDD method's skills for the service design course. It keeps the edition stated below; where the edition drew an example from the method's author's own client work, this copy carries an example set in Progressa in its place and says so where it does.*

*Which records the system keeps, what one record of each kind means, what identifies it, how the records relate, what the system depends on whoever keeps it — and the glossary and the register of business rules kept beside it*

*AN INTERNAL STANDARD  ·  VERSION 1.0  ·  29 SEPTEMBER 2026  ·  IN FORCE*

*Fifty-six rules, a form in five parts answered in two passes, with a table of governed lists, and a review gate in two halves. For public-administration applications.*

Field | Value
--- | ---
Document | SDD-03 · The Entity Model. Which records the system keeps, what one record of each kind means, what identifies it, and how the records relate — together with the glossary that carries the words the model does not, the register of business rules that carries the constraints it cannot express, and, since version 0.3, the statement of what the system depends on, whoever keeps it. It carried no code of its own, and was the file Entity_Model_standard_v.0.1.docx, until the edition of 31 August 2026.
Version and standing | Version 1.0 · 29 September 2026 · in force. It comes into force by the owner's ruling of 29 September 2026, rulings/2026-09-29-four-draft-standards-in-force.yaml, which accepts its rules as version 0.6 stated them. It supersedes version 0.6 of 29 September 2026, which is kept in x_archive/. What changed: it came into force by the owner's ruling of 29 September 2026, and no rule changed; one other sentence changed: the last paragraph of part 9 called the standard a draft for review, and now says it came into force by that ruling before it had been used to draw a model or followed by a reader unfamiliar with this work. Version 0.6 had added one sentence at the head of part 5, saying how the records are found in the module's written descriptions. An internal standard of FiscalAdmin OÜ, owned and approved by Aare Lapõnin, for the work of FiscalAdmin OÜ.
Who writes the document it governs | The analyst, one model for each module, with one glossary and one register of business rules beside it.
Who reads it | The person who reviews the model, and the builder who reads it afterwards.
When it is written | In two passes: the first before any goal is named, the second as the goals turn out to need detail. The classification of every record and list, and its reference lines, belong to the first pass (EM-51). Since version 0.5 the form in part 5 says which of all its lines belong to the first pass, and a model is finished for a pass when that pass's lines are answered (EM-56).
Rules | EM-1 to EM-56, in part 4. Thirty-nine of them cleared this organisation's evidence bar and seventeen did not: four of the first thirty-three rest on a discipline and this organisation's judgement rather than on two fields, three of the eleven added in version 0.2 do the same, five of the seven added in version 0.3, and all five added in version 0.5. Part 9 gives all four tallies and names every rule in each, and tallies separately the four clauses version 0.4 added to EM-19, EM-21 and EM-42 — two cleared, two on judgement — and the clause version 0.5 added to EM-32.
What it does not cover | Part 1 names each boundary and where the subject belongs instead. Identity, ownership and state, and the assignment of shared code lists, are all covered by SDD-04; since version 0.3 the list's entry there cites this document for whose a list is, who issues it and where it is published. What a specification owes a setting, and the entry that carries it, are the catalogue of settings in SDD-04; this standard names a setting and defines none.
Author | FiscalAdmin OÜ · Aare Lapõnin

---

## Contents

1   What this standard is for

2   The words, defined once

3   The principles

4   The rules

5   The form the analyst fills

6   The quality check, which is also the review gate

7   The ways people get it wrong

8   The questions this standard does not answer

9   Where these rules come from

10   Recording the result of a review

11   Conformance

## 1   What this standard is for

### What an entity model is

An entity model is the written statement of which records a system keeps, what one record of each kind means, what identifies it, and how the records relate to one another. A record is one kind of thing the system stores — a taxpayer, a case, a payment, a notice. It is not a table, not a screen and not a form.

The model is written first and drawn second. The picture is one view of the model, made for a person who is being asked to agree or disagree with it. The model itself is the written statement, and that is what this standard governs.

![Figure 1](figures/SDD-03/SDD-03_fig01.png)

*Figure 1  —  Where the entity model sits, and the three things it states*

*Figure 1 was drawn for version 0.1, when the model stated what the system keeps and nothing about what it depends on. Since version 0.3 it states a fourth thing, part 4.6. Redrawing the figure is a finding against this document and not a licence to read it as the whole of what the model states.*

### Who draws it, and what she has in front of her

The reader this standard is written for is a system analyst with no years of experience, one module's written descriptions in front of her, and nobody to ask. Every rule below is written to be applied from that position. Where a rule needs a decision she cannot make alone, the standard says so and says who makes it.

### What this standard promises, and what it does not

This standard promises that two analysts drawing the same module answer the same questions. It does not promise that they draw the same model.

That is the smaller of two promises, and it is worth explaining why the larger one was set aside, because a reader who is not told will hear the smaller one as an evasion.

The work behind this standard read sixty-four published sources across seven modelling disciplines and six public-sector fields — health, customs, tax, financial services, justice and education. It looked, in every one of them, for a published test that says when an entity model is finished. It found none. Not one discipline and not one of the six fields states such a test. What it found instead were checklists that test whether a model was made carefully, which is a different question. And it found the strongest published position running the other way: that drawing a data model is a design activity in which more than one defensible model answers the same requirements.

So the promise is this. A model is finished when every question this standard asks has an answer, or carries a written reason for having none. That is a test a model can actually be put to, and the form in part 5 is the shape of it.

What follows from it is not small. Two analysts who both finish will have answered the same questions about the same module, so their two models can be compared question by question, and every difference between them can be pointed at and argued about. A difference nobody could point at was the real failure the larger promise was meant to prevent, and this promise prevents it just as well. What it does not do is make the two models identical, and no evidence was found that any standard can.

*This claim has not yet been tested on a reader. Nobody who has never seen an entity model drawn here has been given this standard and asked to draw one. Until that happens, everything in this document is a proposal about how an inexperienced analyst works rather than a finding about how one does.*

### What it governs: what the system keeps, and what it depends on, whoever keeps it

This standard is about the records a system keeps, and about every record and list the system depends on, whoever keeps it. It is not about what crosses a boundary between one system and another.

The distinction matters more than it sounds. Three of the six public-sector fields these rules were tested against — health, justice and financial services — publish models of what is exchanged between systems, and those models deliberately break two rules the modelling disciplines state plainly: they let one attribute hold several values in place, and they record one fact in several places on purpose, so that a single message stands on its own without needing others beside it. Both choices are right for a model of what is sent. Neither is right for a model of what is kept.

A model of what a system exchanges with other systems is a different document, and this standard does not govern it. If a module must publish one, the two are written separately and the difference between them is stated.

**The wider scope, and what stops it letting in what it should not.** Until version 0.3 the first sentence above read *the records a system keeps* and nothing more. It now reaches every record and list the system depends on, because a specification that says nothing about what its system reads from elsewhere has nothing against which the design can be measured for it. The sentence after it has not changed, and it is the sentence that does the excluding: the shape of what crosses a boundary is a different document, so the receipt a messaging gateway returns, the file a bank sends and the message another system posts are never records of this model, however carefully a source could be written for each. The rules already here refuse the rest. Take the case this scope was tested on: another system's database holds a taxpayer lookup table, this system reads it, and a source for it can be written. Offered as a record of this model it carries a classification, an issuer, a place of publication and a source line, and passes every line of the new form — and it is refused twice over: by EM-1, because a table is storage, and another system's storage at that; and by EM-11, because a table is not a kind of thing the business deals with. The right entry is the taxpayer record, held elsewhere, consumed from the body that issues it, with that table named on the line that asks where the issuer publishes it. What the wider scope admits is the thing the system depends on. What it refuses is the vessel the thing arrives in.

### What this standard also covers, and why it is here rather than in a document of its own

Two things sit beside the entity model and are not part of it: **the glossary**, which carries the words the model does not, and **the register of business rules**, which carries the constraints the model cannot express. Both are governed by parts 4.4 and 4.5 of this standard.

They are here because a standard in force already requires them and nothing described them. `SDD-05_The_Use_Case_Model_v2.0.docx` M22 requires one glossary kept beside the entity model, and M18 requires one register of business rules. Neither says what an entry carries, how a term or a rule is identified, versioned or withdrawn, or who owns either. Until this edition, an analyst told to keep a glossary had nothing telling her what to put in it.

They are in this document rather than in two of their own by the owner's ruling of 1 September 2026, `rulings/2026-09-01-the-extension-reversal.yaml`, XR-1. The case against that ruling is recorded in it: these two subjects are not the entity model, and a reader may reasonably say they have been put under a cover that does not describe them.

**What is not restated here.** The four rules about registers in general — that a register is a view generated from a named source and never hand-edited, that it names an owner and a written procedure for changing it, that a count is measured at the moment it is written, and that a column no entry has ever filled is reported as a finding — are IOS-15 to IOS-18 of `SDD-04`, and they apply to the glossary and to the register of business rules exactly as they apply to any other register. They are cited and not repeated, by the ruling of 31 August 2026 recorded at `rulings/2026-08-31-gw01-frame.yaml`, GF-1.

### What this standard does not cover

**One companion document** covers the ground excluded below, and nothing here restates it. A rule written in two places is a rule that will drift, so where it governs, this standard points at it and adds only what it does not say. The document is `SDD-04`, and it covers all four of these:

- Identity and uniqueness — what one record represents, what identifies it, what makes two rows the same thing, which copy is authoritative, merging and splitting, identity as it changes over time. IOS-1 to IOS-5 and IOS-19.
- Shared lists and reference data — how a coded value is bound and consumed, how a list is versioned, retired and copied, and the list's entry. IOS-28 to IOS-32. **This subject was covered by nothing when version 0.1 of this standard was issued, and this document said four companion documents covered the ground when one existed. Both are corrected in this edition.** Since version 0.3, whose a list is, who issues it and where the issuer publishes it are stated first in this standard, on the list's row (part 4.6), and the list's entry in `SDD-04` cites that row for those three things and carries everything else. Since version 0.4 an attribute may be bound to a named selection of a list rather than to the whole of it (EM-19); the selection's entry — which list it selects from and who defines it — is `SDD-04`'s, beside the list's entry.
- Settings — a value inside a rule, a computation or a screen that the administration may change by its own act. What a specification owes one setting, and the entry that carries it, are the catalogue of settings in `SDD-04`. This standard names a setting where a rule reads one (EM-42) or a setting selects from a governed list (EM-19), and defines none.
- Ownership — who is the authoritative owner of each value, and whether a value is stored or worked out afresh. IOS-6 to IOS-9.
- States — the states a record moves through and the moves between them. IOS-10 to IOS-14.
This standard also does not cover how the records are stored: tables, indexes, storage and performance belong to whoever builds the database.

## 2   The words, defined once

The rules rely on a small number of words used precisely. Every specialist word this standard needs is defined here and nowhere else. The trade has two or three names for most of them, so the second table gives the bridge: it lets an analyst reading a textbook or a published model tell what she is looking at.

![Figure 2](figures/SDD-03/SDD-03_fig02.png)

*Figure 2  —  A record, a row, an attribute and a relationship*

### The words this standard uses

A record — one kind of thing the system keeps: a taxpayer, a case, a payment, a notice. Not a table, not a screen, not a form.

A row — one particular thing of that kind. A particular taxpayer, not taxpayers in general.

The entity model — the written statement of which records exist, what one row of each means, what identifies it, and how the records relate.

An attribute — one fact held about a record.

A relationship — a stated link between two records, or between a record and itself.

A term — a word or a short phrase the model uses in one settled sense. Every record’s name is a term; not every term is a record’s name.

The glossary — the document kept beside the model carrying the terms the model itself does not, one entry for each.

A business rule — a constraint the business states, which holds whatever screen or flow invokes it. Not a step in a process, and not a check on one field.

The register of business rules — the document carrying those constraints, one entry each, each with an identifier by which a use case can cite it.

Degree — how many rows at one end of a relationship go with one row at the other end.

Optionality — whether the far end of a relationship may be absent altogether. This is a separate question from degree and is answered separately. Running the two together is how one of them stops being answered.

A dependent record — a record that cannot be identified without the record it hangs from.

An identifying relationship — the relationship that supplies a dependent record's identity. A relationship that merely points at another record is a different thing.

A special kind of a record — a more particular kind of a general record, where being that kind is structural: it changes what the row is, not merely how it is labelled.

A part somebody plays — a capacity a row acts in for a time: applicant, officer, guarantor, representative. A part is not a special kind, and part 4 gives the test that tells them apart.

A link that has become a record — a relationship that is a record in its own right because it carries facts of its own.

A governed list — a list of coded values with a named owner, which a record refers to rather than copies.

A named selection — a named subset of a governed list, to which an attribute is bound as if the subset were the list. It selects; it never adds a member. Its entry, naming the list it selects from and who defines it, is in `SDD-04`.

A setting — a value inside a rule, a computation or a screen that the administration may change by its own act while the statement it sits in stays true. It is not a record, not a term and not a member of a list. Its entry is in the catalogue of settings in `SDD-04`, and this standard names a setting by the name that entry carries and defines none.

The classification — the answer a record or a governed list gives to whose it is: this system's and nobody else's; this system's and published for others; held elsewhere and consumed here; not held at all, and held instead by a named other. Four answers, closed.

The issuer — the body whose act makes a row valid or a value a member of a governed list: a registrar, a legislature, a standards body, an office. A body, never the software that stores or serves the thing.

Where the issuer publishes it — the document, register, view or service a reader goes to for the current edition of a record or a list somebody else issues, and the place in it.

The table of governed lists — the part of the model, filled once, that carries one row for every governed list any coded attribute names.

The level of a model — whether the model names the things the business deals with, structures them into records with identifiers and relationships, or describes how they are stored.

The analyst — the reader this standard is written for: no years of experience, one module's written descriptions in front of her, nobody to ask.

### The same things, as the trade names them

| What you will read elsewhere | What this standard calls it |
|---|---|
| entity, entity type, class, concept | a record |
| instance, occurrence, tuple | a row |
| property, element, data element, field | an attribute |
| cardinality, multiplicity | degree |
| participation, minimum cardinality at the far end | optionality |
| weak entity, identifier-dependent entity, child entity | a dependent record |
| identifying relationship (drawn solid); non-identifying (drawn dashed) | a relationship that supplies identity; one that merely points |
| associative entity, intersection entity, association class | a link that has become a record |
| non-specific relationship | a many-to-many relationship not yet resolved into a record |
| recursive relationship | a record related to itself |
| generalisation, specialisation, super-type and sub-type | a general record and the special kinds of it |
| complete and incomplete category cluster | whether the branches cover every row |
| disjoint and overlapping | whether one row may be in two branches at once |
| exclusive arc, choice, exclusive-or constraint | two relationships that may not both be present |
| normalisation, first / second / third normal form | removing the ways one fact can be recorded twice |
| denormalisation | deliberately recording one fact twice, for a stated reason |
| grain | what one row represents — the same idea as a record's written definition |
| surrogate key | an identifier the system makes up, with no meaning outside it |
| natural key, business key | an identifier the world already issues |
| referential action — cascade, restrict, set null | what happens at the far end when a row is removed |
| valid time | when the fact was true |
| transaction time | when the system was told |
| bitemporal | keeping both clocks |
| effective dating | holding a fact together with the period it holds for |
| slowly changing dimension | the named ways of keeping or discarding history |
| value set, code list, reference data | a governed list |
| subset, filter, slice, a value set drawn from a code system | a named selection |
| parameter, configuration item, feature flag, switch, threshold | a setting |
| terminology, controlled vocabulary, term base, data dictionary | the glossary |
| preferred term, descriptor | the one name a concept carries in this model |
| synonym, non-preferred term, alternative label | another name for the same concept, recorded against the entry |
| decision rule, constraint, policy statement, decision logic | a business rule |
| rule repository, rulebook, decision model | the register of business rules |
| binding strength | how strictly a coded attribute must draw from its list |
| subject area, module, information package | a named group of records small enough to read |
| conceptual, logical, physical | the three levels of a model |
| system of record | the one place a fact is authoritative |
| authentic source, base registry, maintenance agency, registration authority, register owner | the issuer |
| canonical URL, resolvable identifier, register entry, endpoint | where the issuer publishes it |
| consumer, subscriber, downstream system | a system named as consuming what this one publishes |
| internal and external entity, owned and sourced, master and consumed | the classification |
| profile, usage specification, extension | the named ways of adapting a published model |

## 3   The principles

Eight principles underlie every rule in this standard. Where a rule seems not to fit the module in front of you, return to these: they say what the rules are for.

P1   The model says what the system keeps, and what it depends on, whoever keeps it.

It is not a description of the world and it is not a picture of a screen. Two people arguing about whether a model is right are usually arguing about the world; the question the model answers is narrower and can be settled — what does this system store, and what does one row of it mean. Since version 0.3 the same narrow question is asked of what the system does not keep: not what the world holds, but what this system reads from elsewhere, who is the authority for it, and where. The principle read *what the system keeps* until version 0.3; the words *and what it depends on, whoever keeps it* were added with part 4.6.

P2   Every record and every link is a sentence somebody from the business can agree or disagree with.

That is the whole reason for writing a definition and for naming a relationship. A record with no definition and a line with no name are not agreed to; they are looked at.

P3   The model states the least that must be true. A particular use of it may demand more, and may never demand less.

What a screen requires and what the model requires are two different rules. A model whose minimums were copied from one screen has to be broken by the second use of it.

P4   Where the boundary runs is a decision, and one of its three answers is that this system does not hold the thing at all.

A model with no boundary statement grows until somebody stops it for reasons of time. The third answer — we do not hold this, and here is who does — is the one most often missing.

P5   What is governed elsewhere is pointed at, never copied.

A coded value refers to its governed list; a record somebody else is the authority for is consumed and not re-kept. Two copies of anything drift, and the copy that drifts is always the one nobody is watching.

P6   There is one model, and every picture is generated from it.

Once a model needs more than one picture, pictures kept by hand guarantee that at least one is wrong and nothing says which.

P7   Every rule a model is judged against is one of two kinds: one a program reads, or one a person judges.

A model checked only by the first kind passes while being empty — a program can see that a definition is filled in and cannot see that what fills it is true.

P8   A model is finished when every question this standard asks has an answer, or carries a written reason for having none.

Not when the automatic checks are quiet.

Since version 0.5 the question is asked twice, because the form is answered in two passes (EM-56). A model is finished for the first pass when every line the form marks as first-pass has an answer or a written reason, and finished outright when every line does. A model written before any goal was named and judged against the whole form is reported as unfinished when it is only early, and that is a misreading of this standard rather than a defect in the model.

## 4   The rules

Fifty-six rules, in six groups: the rules for the model as a whole, the rules for one record, the rules for relationships, the rules for the glossary, the rules for the register of business rules, and the rules for what the system depends on. Each rule is a statement, followed by what applying it means in practice.

The first three groups are the entity model itself and are unchanged from version 0.1. The fourth and fifth were added in version 0.2 and carry the two subjects part 1 says this standard also covers. The sixth is new in version 0.3 and carries the wider scope part 1 now states. **The numbering continues and no rule was renumbered**: a reader holding a citation to any of EM-1 to EM-44 finds the same rule, in the same words. Version 0.4 added no rule and added a clause to three — EM-19, which gained two, EM-21 and EM-42. Every sentence a rule carried before is carried still, word for word; each added sentence follows the sentence it joins, and the explanation under the rule says it was added and what it rests on.

Version 0.5 added five rules, EM-52 to EM-56, and renumbered none. They are not gathered into a group of their own. Each is placed in the group whose subject it belongs to, so EM-55 and EM-56 stand at the end of the rules for the model as a whole and EM-52 to EM-54 at the end of the rules for one record. The numbers therefore run out of order inside those two groups, and that is deliberate: a reader looking for a rule about an attribute should find it among the rules about attributes, and the group headings mean what they say. Version 0.5 also added one clause, to EM-32, and one sentence to EM-26 that carries no obligation.

### 4.1   The rules for the model as a whole

These are the rules most often left unanswered. A model that answers every question about each record and leaves this group unanswered is the common case, and it is the case this standard mainly exists to catch.

EM-1   The model declares its level, and nothing belonging to a lower level appears at a higher one.

A model that names the things the business deals with does not carry identifiers, column types or storage hints. Declare which of the three levels this model is, and what is therefore excluded from it.

EM-2   Every record says whether this system is the authority for it, consumes it from an authority elsewhere, or must not hold it at all.

Three answers, not two. Where the answer is that the system must not hold it, the model names who does hold it. This is what stops a model growing until somebody stops it for reasons of time.

EM-3   The records are grouped into named groups small enough for a person to read. A record may appear in more than one group.

A relationship whose two ends fall in different groups is shown in both of them. No threshold on group size is set by this standard; the model states its own and keeps to it.

EM-4   A published model is extended by adding, never by changing what is already there.

The changes a later version may make are written down before there is a later version. Otherwise every reader of the model has to guess what is safe to build on.

EM-5   The model has a named owner and a written procedure for changing it, and a change is a request rather than an edit.

Who owns it, who may propose a change, and who decides. A model with no owner is a model whose contradictions nobody resolves.

EM-6   Every rule the model is judged against declares which of two kinds it is: one a program reads, or one a person judges.

This is what stops a model being declared finished because the automatic checks are quiet.

EM-7   The picture carries what a person reading it can check. Everything else lives in the register beside it.

Definitions, governed lists and derivations belong in the register, not crowded onto the drawing. The model states where each of them lives.

EM-8   There is one model, and every picture is generated from it.

Pictures maintained by hand beside the model guarantee that at least one is wrong and nothing says which.

EM-9   A picture must not be used to assert what its notation cannot express, and must not be read as asserting it either.

Every notation has things it cannot say. The model lists what its own notation cannot say, and says where each of those things is written instead.

EM-10   One notation is chosen for a model, stated, and never mixed with another.

Two notations in one model mean that the same mark means two things, and no reader can tell which.

EM-55   One layout convention is stated for the model, and every generated picture follows it.

EM-8 says every picture is generated from one model and says nothing about what the generator should do, so the arrangement of a picture is whatever the tool defaults to and it changes between drawings. The convention states at least three things: where the many end of a relationship is placed, whether relationship names sit at the ends of the line and on which side, and what the title of every picture carries. The reason to fix it is not tidiness. With the arrangement fixed, records of similar shape land near one another, and two records that are the same thing under two names — the failure EM-34 names and leaves without a method — become findable by being adjacent. A picture drawn to no stated convention is still a picture. It is one whose positions carry no information, and a model whose positions carry no information has to be read record by record to find what reading across would have shown. Added in version 0.5, on one discipline and on no field.

EM-56   The form in part 5 is answered in two passes, and the form states which of its lines belong to the first.

Until this version every line of the form was equally required, so a model written before any goal was named could be reported only as unfinished, whatever had been done to it. EM-51 already made one group of lines first-pass work and said that a classification first written in the second pass is a finding; this rule generalises the idea and part 5 carries the list. A model is finished for the first pass when every first-pass line has an answer or a written reason for having none, and finished outright when every line does. **What this rule does not do is say how much detail a record carries.** Whether a record is drawn with three attributes or thirty is still the question part 8.1 states and does not answer, and a line answered in the first pass may be answered thinly. Added in version 0.5, on one discipline and on no field.

### 4.2   The rules for one record

EM-11   A record is a kind of thing that can be told apart from every other thing of its kind, that has more than one row, that holds more than one fact, and that means something on its own.

All four tests, or a written reason for the exception. A report, a screen, a step in a process or a moment in time is not a record.

EM-12   Dependence is declared at both ends.

A record that cannot be identified without its parent says so, and the relationship that supplies its identity is named as the one that does.

EM-13   A part somebody plays is not a kind of person.

Where the parts are not exclusive — one person can be two of them at once, or move between them over time — model the part as a link held for a period, never as a branch.

EM-14   Special kinds answer two separate questions and both are answered.

Must every row fall in one of the branches? May one row be in two branches at once? A model that answers one and not the other has left the harder half open.

![Figure 3](figures/SDD-03/SDD-03_fig03.png)

*Figure 3  —  The test that separates a special kind of thing from a part somebody plays*

EM-15   Every record and every attribute carries a written definition, and the definition is singular, stands on its own, and does not repeat the name.

Write it as: one row per ____ . It says what the thing is, not why it exists, who uses it or what happens to it.

EM-16   A record's name is a singular noun phrase in the words the business uses, unique across the whole model.

Singular, because the record is a kind of thing and the row is one of them.

EM-17   Every attribute and every relationship end states the least and the most that may be there.

The fewest and the most are two separate decisions and both are made. A line with no marks on it is completed differently by every reader.

EM-18   The model states the least that must be true. A particular use of the model may demand more; it may never demand less.

If an attribute is required because one screen requires it, that is the screen's rule and not the model's.

EM-19   A coded attribute is a reference to a governed list, and the model states how strongly it is bound to it. The list it refers to is a governed list or a named selection of one. Where a setting selects its value from a governed list, the setting is bound to that list at the strongest strength.

Must use the list; must use it where it covers the case; recommended; illustrative. Without the strength, nobody can tell whether a value outside the list is an error.

The second and third sentences were added in version 0.4. A named selection is a subset of a governed list that the module binds to as if it were the list — a control offering three closure reasons of the thirty a shared list carries is bound to the selection and not to the list, and a module that could not say so minted a list of its own for the slice. The attribute names the selection as its entry in `SDD-04` names it; the selection's entry names the list it selects from and who defines the selection, and the list keeps its one row in the table of governed lists (EM-47). A setting whose value is chosen from a governed list is a use of the list like any attribute's, and it is bound at the first strength only: it selects a member the list carries and never a value outside it, and it never adds one — a setting that could add a member would be changing a meaning, which is the list's business under EM-20 and its issuer's under EM-48. Which member a recorded fact admits, and the rest of what the setting owes, are its entry's in the catalogue of settings in `SDD-04`. Neither sentence changes what an attribute writes; both say what it may point at.

EM-20   A governed list is versioned, and its values are retired rather than removed.

Deleting a code silently rewrites what older rows mean.

EM-21   There are two clocks, not one — when a fact was true, and when the system was told — and the model says which it keeps. A coded value the record stores carries the date it was resolved as at, on the clock the record keeps.

Neither, one, or both. A record that keeps neither carries the reason it does not.

The second sentence was added in version 0.4, on this organisation's judgement and on no outside field. A code stored in a row was read against its list as the list stood on some date, and the list moves under it (EM-20): without the date on the value, a label shown two years later is resolved against today's list, and a value retired since cannot be told from one that was never valid. The screen states which clock decides what it offers (`SDD-07` rule 18) and the list's entry states what becomes of a retired value (`SDD-04` IOS-31); this sentence is the record's side, and it is the side a value that arrives by a crossing and never crosses a screen would otherwise lack. A record that keeps neither clock carries no such date, and the reason it keeps neither covers the value.

![Figure 4](figures/SDD-03/SDD-03_fig04.png)

*Figure 4  —  When the fact was true, and when the system was told*

EM-22   A fact that is true for a period is held together with the period, and uniqueness is then stated over the identifier and the period together.

A record that keeps history and states uniqueness over the identifier alone cannot hold its own history.

EM-23   An attribute that would hold more than one value at once is a record that has not been drawn yet.

Draw it. This holds because the model describes what the system keeps; a model of what a system sends to other systems answers this differently, and is a different document.

EM-24   The model is held to third normal form, and every place it is deliberately departed from is recorded with the reason and with how the copies are kept in step.

Departing on purpose is allowed. Departing silently is how one fact ends up recorded in two places that disagree.

EM-25   An identifier the system makes up, with no meaning outside the system, belongs to the model of how things are stored.

It appears at a higher level only when the business itself issues it and shows it to people, and then the reason is written down.

EM-52   An attribute describes the record it is drawn on. Where it describes another record, the attribute moves to that record and the link between the two is drawn.

This rule exists because the analyst's source is almost always a printed form or a screen, and a printed form puts on one page facts about several records. A seat number printed on a boarding pass is a fact about the seat and about the aircraft, not about the pass; written as an attribute of the pass, the model has copied the stationery. The test is to read the record's definition aloud and the attribute after it: where the sentence describes something other than one row of that record, the attribute belongs elsewhere, and the relationship between the two records is the thing that was missing. Where the fact is genuinely about the association between two records and about neither of them alone, EM-27 applies instead and the relationship is a record. This is the rule that catches a model built from tax returns, declarations and notices, where the paper is the only source the analyst has. Added in version 0.5, on one discipline and on no field, and no program can read it.

EM-53   An attribute's name does not repeat the name of the record that holds it.

A record named taxpayer holds a name, not a taxpayer name. A record named case holds a status, not a case status. The repetition costs nothing in one record and a great deal across a model, because it conceals the moment when the same fact appears on two records under two spellings, and because every artefact generated from the model carries the repetition afterwards. Where the unqualified name would be ambiguous inside the record — two dates, two amounts — the qualifier is the one that tells them apart and never the record's own name. Added in version 0.5, on one discipline and on no field, and a program reads it.

EM-54   Every record is related to at least one other record, or carries a written reason for standing alone.

A record connected to nothing is one of three things: a list that belongs in the table of governed lists rather than among the records, a record whose relationships nobody has drawn yet, or a genuine standalone. The model cannot tell which until somebody writes it down, and a reviewer reading the picture cannot either. Where there is a reason, it is usually that the record is consumed whole from elsewhere and this system relates nothing to it, which EM-2 already asks for in other words and which this rule makes visible on the picture rather than only in the form. A program reads whether the record has a relationship or a reason. Only a person reads whether the reason is true. Added in version 0.5, on one discipline and on no field.

### 4.3   The rules for relationships

![Figure 5](figures/SDD-03/SDD-03_fig05.png)

*Figure 5  —  Degree and optionality are answered separately, at both ends*

EM-26   Every relationship is named, and the name is built so that it reads as a phrase: what the link is, plus the thing at the far end.

Never related to, associated with, linked to, has or refers to. Those are not names; they are the absence of one.

Added in version 0.5, and carrying no obligation. The founding discipline publishes a vocabulary of paired end names — the subject of and context for, based on and basis for, part of and composed of, responsible for and responsibility of, covered by and cover for, and some forty further pairs — with two cautions attached: that the ownership pair is reserved for legal ownership, and that several of the pairs assume one end is a person or an organisation. A model that keeps such a vocabulary beside it, extended with the pairs this estate's own work needs, gives two analysts the same words for the same kind of link and makes EM-26 easier to obey than to break. **This is a resource and not a rule.** It is not claimed under part 11, and nothing is in breach for keeping no vocabulary.

EM-27   A relationship that carries facts of its own is a record, and it is drawn as one.

A line that has quietly grown three attributes is a record the model has not named.

![Figure 6](figures/SDD-03/SDD-03_fig06.png)

*Figure 6  —  A link carrying facts of its own is a record that has not been drawn*

EM-28   A many-to-many relationship is resolved into a record before the model is called finished.

Leaving it unresolved hands the decision to whoever builds the database, and the record they invent will have no definition.

EM-29   A record related to itself states which relation the loop carries.

Is a kind of, is part of, is grouped with, supersedes. A loop with no statement of what it means is read four different ways.

EM-30   Where two relationships may not both be present, the model says so, inside the model rather than in a note beside the picture.

A constraint written in a note is a constraint nothing enforces and nothing generates.

![Figure 7](figures/SDD-03/SDD-03_fig07.png)

*Figure 7  —  The four answers to what happens at the far end*

EM-31   What happens at the far end when a row is removed, replaced or corrected is a decision the model records.

One of four: the far row goes too; the removal is refused; nothing is ever removed and rows are superseded; or the far row is left pointing at nothing — which is rarely right and never by accident.

EM-32   Every relationship is named in both directions, so that each direction reads as a complete sentence. The sentence has a stated form, and the relationship is read back to a business reader in that form, in both directions.

Reading a model aloud in both directions is the cheapest review there is, and it only works when both names exist.

The second sentence was added in version 0.5. The form is: *each and every* RECORD *must be* or *may be* [the name of this end] *one and only one* or *one or more* RECORD AT THE FAR END — *is that true?* Four devices in it do the work, and each catches a different error. *Each and every* moves the reader off the case in front of her and onto the whole population, which is where the exception lives. *Must be* against *may be* carries the optionality and *one and only one* against *one or more* carries the degree, so that EM-17's two decisions cannot both be left unmade by a reader who never noticed there were two. *Ever*, added to the sentence wherever the record keeps history, extends the assertion backwards in time and catches the constraint that is true today and false of rows written three years ago — which is the failure EM-22 exists for. And *is that true?* turns a statement the counterpart can nod at into a question he has to answer.

The relationship is then read in the other direction as an impossibility: a RECORD that is not for a uniquely identifiable RECORD AT THE FAR END can never exist. The two readings are not the same review done twice. A person accepts a positive statement far more readily than he accepts its negative consequence, so each reading catches errors the other leaves. The answer each reading got is written on the relationship's form in part 5.2, because a reading nobody recorded cannot be told from a reading nobody did. The form of words is not this organisation's: it is the founding discipline's, and it is written out here because a standard whose reader has nobody to ask needs the words and not only the instruction to read aloud.

EM-33   A relationship optional at both ends is suspect and is reviewed before the model is finished.

It may be right. It is more often two relationships run together, or a link that belongs somewhere else.

### 4.4   The rules for the glossary

The glossary is required by `SDD-05` M22, which is in force: one glossary, kept beside the entity model, with one term for each concept across the whole model. M22 requires that it exists. These six rules say what is in it.

EM-34   The model names one glossary, and one term carries each concept across the whole model.

One glossary for one model, named in the model's own heading. Where two words are found meaning the same thing, one is chosen and the other is recorded against it under EM-37; the choice is never left to whoever writes next. Two names for one thing can only be found by reading across the model, never inside one record.

EM-35   If the system keeps a record of it, the entity model names it. Otherwise the glossary carries it.

That is the whole of the boundary and it is a test, not a preference. Role names, statuses, process names and terms drawn from legislation are the four kinds that come up most and none of them is a record. Where a word is on the line — the system keeps rows of it and it is also a word in the business's mouth — the entity model names it and the glossary does not repeat it. A term in both places is the drift P5 exists to prevent.

EM-36   Every glossary entry carries the term, one definition, where the term comes from, its status, and where it is used.

The definition is written to the same test as a record's definition in EM-15: singular, standing on its own, not repeating the name, carrying no rationale and no procedure. Where the term comes from means the instrument, the published vocabulary or the conversation it was taken from, or this organisation where it was settled here. Its status is one of proposed, in use, or withdrawn. Where it is used means the records, use cases or rules that rely on it — which is what makes an unused term visible.

EM-37   A concept has one preferred term, and every other name for it is recorded against that entry rather than left to be discovered.

The other names are what a reader will actually meet: in an older document, in a statute, in the words one office uses. Recording them is what lets a reader arriving with the wrong word find the right entry. A name recorded this way is never the name the model uses.

EM-38   A term is versioned, and it is withdrawn rather than deleted.

A withdrawn entry stays in the glossary, carrying the date it was withdrawn, the reason, and the term that replaces it where one does. A term that governed a document written last year has to stay readable, or that document stops meaning what it meant.

EM-39   A term drawn from legislation is reproduced as the instrument has it, cited to the instrument, and not rewritten into house words.

Where the statutory word is unusable in ordinary work, the entry carries both: the statutory term as the preferred term with its citation, and the working word recorded against it under EM-37. Rewriting a statutory term silently is how a system comes to mean something the law does not say.

### 4.5   The rules for the register of business rules

The register is required by `SDD-05` M18, which is in force: every business rule the model depends on is written once, given a stable identifier, and cited rather than restated. M18 also requires that a rule is cited from a use case by its identifier and never written out inside a flow, and that requirement is not repeated here. These five rules say what is in the register.

EM-40   There is one register of business rules for the model, and every rule it depends on appears in it once, with a stable identifier.

One register, named in the model's heading beside the glossary. The identifier is what a use case, a screen and a computation all cite; it is allocated once and never reused, including after the rule is withdrawn.

EM-41   A rule is written short, self-contained, and free of the flow that invokes it.

The test is whether the rule can be pointed at and understood without reading anything around it. A rule stated only inside the prose of one flow is invisible to every other use case, to the reviewer, and to everything derived downstream. If it cannot be pointed at directly, it is not yet a rule.

EM-42   Every entry carries the identifier, the statement, the terms it uses, what it constrains, where its authority comes from, when it takes effect, and its status. A rule that reads a setting names the setting in its statement, by the name its entry carries, and carries no value of it.

Every term the statement uses is in the glossary or is a record of the entity model; a rule using a word neither of them carries is a finding against the glossary. What it constrains means the records, attributes or relationships it binds. Where its authority comes from is a statute or instrument with its citation, a published policy, or this organisation's own decision with the ruling that took it. When it takes effect is a date, and where it stops applying, a second one. Its status is one of proposed, in force, or withdrawn.

The second sentence was added in version 0.4. A rule is a statement that stays true while the administration changes a value inside it — *a debt above the threshold becomes a case* is the rule and the threshold is a setting — and the value has an entry of its own in the catalogue of settings in `SDD-04`, carrying its default, its authority and who may change it. Written into the statement, the value is a second copy that drifts from the entry: the failure `SDD-04` IOS-27 names for a computation, which nothing here prevented for a rule. The statement carries the name and the entry carries the value. This is `SDD-01` rule 6 — every figure that comes from policy is a setting with a marked default — applied to the register that holds the rules those figures sit in. A figure only the legislature can change is not a setting; it stays in the statement, and the rule's authority line cites the instrument that fixes it.

EM-43   A rule is versioned, and it is withdrawn rather than deleted.

A withdrawn rule keeps its entry, its identifier, the date it stopped applying and the reason. A decision taken last year was taken under the rule as it then stood, and somebody will have to read that rule to explain the decision. A register that deletes a withdrawn rule cannot explain its own past.

EM-44   A rule nothing cites is reported as a finding about the rule, with an owner.

It is either dead or a rule nobody is maintaining, and the register cannot tell which. Reporting it is not deleting it; the owner decides.

### 4.6   The rules for what the system depends on

EM-2 stands as it is written, with its three answers, and is not rewritten. These seven rules add what it did not ask: whether anybody else consumes what this system keeps; from whose position a classification is made; where a shared list is stated once; and what a reader who was not in the room needs in order to find the authority behind a record or a list this system does not own. The words *the classification*, *the issuer* and *where the issuer publishes it* are defined in part 2 and used here in that sense only.

The failures these rules prevent were not imagined. Each was counted in the material of one public-administration programme during the work that settled this subject, and each is named under the rule it belongs to, so that a reader can see what the rule is for.

EM-45   A record this system is the authority for says further whether any other system consumes it: nobody else does, or it is published for others, and the others are named.

EM-2's first answer becomes two, and the two are not one answer with a list of consumers that may be empty. An empty list reads as *not yet looked*; *nobody else's* reads as *looked and found none*; and only the second is a claim that can be wrong, which is what makes it worth writing. *Nobody else's* is a claim from the client's material at a date, and it is revisited when the actor catalogue of the use case model or the catalogue of events names a consumer the record does not: the consumer is then added under EM-4, never left silent. The failure this prevents: a system that hands its outcomes to two other systems — an accounting module and a scoring platform — and says so on no record, so that the first the entity model hears of a consumer is when a change breaks it.

EM-46   A classification is made from the position of the system this model is of, and states that system's position and never another's.

The same list is *held elsewhere, consumed here* for the module that reads it and *published for others* for the service that maintains it. Each model says its own. A reader who misses this writes the wrong answer on every row. Where two models of two systems disagree about who is the authority for one thing, that is a finding against both, with an owner, and not something either model resolves alone.

EM-47   Every governed list any coded attribute names has one row of its own in the model's table of governed lists, and the row carries the classification and its reference lines once. The attribute names the list and its strength of binding, and states nothing else about the list.

A list is one thing and a field is one use of it. Carried per use, the facts about a list are carried as many times as it is used, and the copies drift: the programme this was tested on carried its bindings per description, and its final gate found four fields naming the right list under the wrong identifier. The strength of binding under EM-19 stays on the attribute, because it is a fact about the use and not about the list. What the row does not carry — the edition in force, how the list is consumed, whether it may be extended, who looks after it locally, how fresh it must be, and its number in any central register — belongs to the list's entry in `SDD-04`, which cites this row for what the row carries and does not restate it.

EM-48   A record or a list that is not this system's and nobody else's names who issues it: the body whose act makes a row valid or a value a member, never the software that stores or serves it. It is stated here first, and every later document cites this row.

The failure: a ratified register carried a system of record on every one of its rows, and on nine of them named the platform that serves the lists, because the people keeping it had been given no answer for a list the platform itself invents. A platform is where a list is published; it issues nothing. Where the client's material does not name the body, the line says so under EM-50 and names who was asked. The obligation to name an issuer is `SDD-04` IOS-28's and cleared the bar there; what this rule adds is the place it is stated first — the first pass of this model, written before any goal is named and one of the two measures the method keeps — so that the list's entry in `SDD-04` and the record of a screen cite it rather than restate it.

EM-49   A record or a list that is not this system's and nobody else's names where the issuer publishes it: the document, register, view or service a reader goes to for the current edition, and the place in it.

A reference that resolves only in the head of the person who wrote it is not a reference. The failure: on the programme this was tested on, two sets of values stopped a change from landing because no address for either list existed anywhere in the material, and the programme's own rule that every frozen snapshot cites its source could not be kept for them. The address is stated in the form the issuer gives it: an identifier that resolves at a registry is an address; *the shared database* is not. Where the client's material names a database or an interface rather than a place a reader can go, that is not the answer, and the line says so under EM-50 and names who was asked.

EM-50   Every classification, every issuer and every place of publication cites the words in the client's material it was derived from — the document, the place, the words — or says that the client was silent, and names who was asked and when.

This is what tells a classification the client stated from one the analyst supplied, and it is what makes a classified model measurable against the client's material sentence by sentence, as the register of requirements already is. It also makes the silences countable: how many classifications rest on a sentence of the client's, how many on an answer from a named office, how many on nothing yet. The count is stated and not judged. The failure: a list the client wrote as two values inside one of its own records, which a reader classifies as this system's own from the page and which a ruling later made a published list bound to an international standard. Both are defensible; only the source line shows which was read and which was known.

EM-51   The classification of every record and every list, and its reference lines, are written in the first pass of the model, before any goal is named. A classification first written in the second pass is a finding.

The first pass is one of the two measures the method writes before any goal exists; the second pass is written from the goals. A classification added in the second pass is the design writing its own measure, and nothing else in this standard prevents it. The strength of a binding under EM-19 may wait for the second pass, because it is a fact about a use; the name of the list may not, because it is the row's key. This is the one rule in the group that says when rather than what.

## 5   The form the analyst fills

**How the records are found.** The analyst reads the module's written descriptions sentence by sentence and asks of each thing they say the business deals with whether it passes the four tests of EM-11: a thing that passes is given a form of part 5.1, a thing that does not is written where it belongs — an attribute of a record, a relationship, an entry of the glossary or of the register of business rules — and in either case the words of the descriptions that named it are written as its source line, in the form EM-50 asks for.

This part is the centre of the standard, not an appendix to it. The promise is that two analysts answer the same questions, and these are the questions. A model is finished when every line below has an answer or carries a written reason for having none.

The form has five parts. The first is filled once for each record, the second once for each relationship, the third once for the model as a whole, the fourth once for each glossary entry and the fifth once for each business rule. Since version 0.3 the third part carries a table of governed lists, one row per list, laid out at the end of part 5.3. Each line names the rule it serves, so that a reviewer can go from an unanswered line straight to the rule that requires it.

**The two passes.** Since version 0.5 the form is answered in two passes (EM-56). The lines named below belong to the first pass, which is written before any goal is named; every other line of the form belongs to the second. A model is finished for the first pass when every line in this list has an answer or a written reason for having none, and finished outright when every line of the form does. The assignment is this organisation's own and rests on no field: a reader who holds that a line is in the wrong pass moves it and records why.

In part 5.1: the name, the definition, why it is a record, how it is identified, the special kinds and the parts played, the record or records it is related to, and the whole of the boundary line — the classification, the issuer, where the issuer publishes it and the words in the client's material it was derived from, which EM-51 already placed here. In part 5.2: both names, the degree, the optionality, and whether the relationship is identifying or referring. In part 5.3: the level, what this model is of, the boundary statement, the groups, the notation, the layout convention, the owner and the change procedure, the extension rule, and every column of every row of the table of governed lists. Everything else — the attributes and their least and most, the clocks, the uniqueness, the read-back, the normal form, the counts, the pictures, the depth worked at — belongs to the second pass.

![Figure 8](figures/SDD-03/SDD-03_fig08.png)

*Figure 8  —  The three parts of the form, and the test for finished*

*Figure 8 was drawn for version 0.1 and shows the three parts of the model's own form. Parts 5.4 and 5.5 are new in version 0.2 and are not in it. Redrawing it is a finding against this document and not a licence to read the picture as the whole of the form.*

### 5.1   For each record

| Line | What to write | Rule |
|---|---|---|
| Name | A singular noun phrase in the words the business uses, unique across the whole model | EM-16 |
| Definition | One row per ____ . Singular, standing on its own, not repeating the name, carrying no rationale or procedure | EM-15 |
| Why it is a record | More than one row; more than one fact; means something on its own; can be told apart from every other kind. All four, or a written reason for the exception | EM-11 |
| Identified how | On its own; or only through ____ , and the relationship that supplies the identity is named in the relationship form | EM-12 |
| Special kinds | None; or branches ____ . Do the branches cover every row (yes / no)? May one row be in two at once (yes / no)? Both answered | EM-14 |
| Parts played | Any capacity a row acts in that is not exclusive is a link and not a branch. List them: ____ | EM-13 |
| Attributes, each with its least and most | For every attribute: the fewest that may be there and the most. Two separate decisions | EM-17 |
| What the minimums mean | Confirm the minimums are the model's floor and not one screen's rule | EM-18 |
| Attributes holding more than one value | None; or ____ , each of which becomes a record | EM-23 |
| Where each attribute belongs | For every attribute: it describes one row of this record. Where it describes another record, it moves there and the link between the two records is drawn | EM-52 |
| Attribute names | No attribute name repeats this record's name. Where a qualifier is needed to tell two attributes apart, it is the qualifier that distinguishes them and never the record's name | EM-53 |
| Made-up identifiers | None at this level; or ____ , each with the reason it is here | EM-25 |
| Coded attributes | For each: the governed list ____ , named as its row in the table of governed lists names it — or the named selection of one ____ , named as its entry in `SDD-04` names it — and the strength of binding. *Its owner* was asked here until version 0.2; it is now the issuer on the list's row, cited and not repeated | EM-19, EM-47 |
| The governed lists used | For each: is it versioned, and are values retired rather than removed (yes / no / not known). Who issues it is on the list's row and is not repeated here | EM-20, EM-47 |
| History kept | None; when the fact was true; when the system was told; both. A none carries a reason | EM-21 |
| Coded values, as at | For each coded attribute the record stores: the stored value carries the date it was resolved as at, on the clock the record keeps — or the reason the record keeps neither clock covers it | EM-21 |
| Uniqueness | Over the identifier alone; or over the identifier and the period, where history is kept | EM-22 |
| Boundary | This system is the authority — and nobody else consumes it, or it is published for others, to ____ ; consumes it from ____ ; must not hold it — held instead by ____ . Then, on every answer but the first: who issues it ____ (the body, never the software); where the issuer publishes it ____ . And on every answer: the words in the client's material this was derived from ____ , or *not stated by the client; asked of ____ on ____* | EM-2, EM-45, EM-48 to EM-50 |
| Groups it is read in | ____ (a record may be in more than one) | EM-3 |
| Facts deliberately recorded twice | None; or ____ , each with the reason and with how the copies are kept in step | EM-24 |
| Related to | The records this one is related to: ____ . Or the written reason it stands alone | EM-54 |

*A record that answers only the definition line has not been described. It has been named.*

### 5.2   For each relationship

| Line | What to write | Rule |
|---|---|---|
| Name, reading from this end | ____ (what the link is, plus the thing at the far end) | EM-26 |
| Name, reading from the far end | ____ — so that both directions read as complete sentences | EM-32 |
| Read back, in both directions | The two sentences as they were put to a business reader, in the form EM-32 states, and the answer each got. A reading nobody recorded cannot be told from a reading nobody did | EM-32 |
| Degree | ____ rows at this end go with ____ rows at the far end | EM-17 |
| Optionality | May this end be absent (yes / no)? May the far end (yes / no)? | EM-17 |
| If both ends are optional | The reason, written out — or the relationship is corrected | EM-33 |
| Identifying or referring | Does this relationship supply the far record's identity (yes / no)? | EM-12 |
| Facts of its own | None; or ____ — and if there are any, it is a record and is written up as one | EM-27 |
| If many at both ends | The record it resolves into: ____ | EM-28 |
| Excluded by another relationship | No; exclusive with ____ , and the exclusion is written in the model | EM-30 |
| On removal, replacement or correction | The far row goes too; the far row is left pointing at nothing; the removal is refused; the near row is never removed, only superseded | EM-31 |
| Loops back to the same record | No; yes, and the relation it carries is: is a kind of; is part of; is grouped with; supersedes | EM-29 |

### 5.3   For the model as a whole

This is the part that is filled once, and the part that is most often not filled at all.

| Line | What to write | Rule |
|---|---|---|
| Level | Naming the things the business deals with; structuring them into records with identifiers and relationships; describing how they are stored — and what is therefore excluded | EM-1 |
| What this model is of | The records this system keeps, and the records and lists it depends on, whoever keeps them. If the module must also publish what it exchanges with other systems, that is a second document, named here: ____ | — |
| Boundary statement | The records this system is the authority for and nobody else consumes ____ ; the records it is the authority for and publishes, and to whom ____ ; the records it consumes, and from whom ____ ; the kinds of thing it deliberately does not hold, and where each is held instead ____ | EM-2, EM-45 |
| Groups | The named groups, each small enough to read; the records appearing in more than one; and how a relationship crossing two groups is shown in both | EM-3 |
| Counts, stated and not judged | How many records; how many relationships; how many records carry no definition; how many relationships carry no name. No threshold is set and none may be inferred | EM-3, EM-6 |
| The two clocks | Which records keep when a fact was true, which keep when the system was told, which keep both, and which keep neither — with a reason for each neither | EM-21 |
| Normal form | The form the model is held to, and every place it is deliberately departed from, with the reason and with how the copies are kept in step | EM-24 |
| Extension rule | What a later version may change and what it may not — written before there is a later version | EM-4 |
| Notation | Which one notation this model uses ____ ; and what that notation cannot say, listed, with where each of those things is written instead | EM-9, EM-10 |
| Layout convention | The convention every generated picture follows: where the many end of a relationship is placed, where relationship names sit, and what the title of every picture carries | EM-55 |
| The pictures | Which pictures exist, what each is for, who reads each, and which single model they are all generated from | EM-7, EM-8 |
| The register beside the pictures | Where the definitions live; where the derivations live. *Where the governed lists live* was asked here until version 0.2 and is superseded by the table of governed lists on the next line | EM-7 |
| The table of governed lists | One row for every list any coded attribute names, in the columns laid out below this form, filled once for the model. A list an attribute names that has no row, and a row with no classification or no source line, is an unanswered line of this form | EM-47 to EM-51 |
| Written in the first pass | Confirm that every classification and its reference lines were written before any goal was named; where one was not, it is recorded as a finding with an owner | EM-51 |
| The two passes | Which lines of this form belong to the first pass and which to the second, wherever the assignment departs from the list in part 5; and whether this model is reported as finished for the first pass or finished outright | EM-56 |
| Owner and change procedure | Who owns the model; who may propose a change; who decides | EM-5 |
| Review | Who reviews it, against what list, and which items on that list a program cannot check | EM-6 |
| The depth worked at | The level of detail this model was drawn to, in the analyst's own words, applied consistently across every record. This standard does not yet say which depth to choose | not settled |
| Open questions | The decisions genuinely in dispute, each with a named owner and a date — never closed by a silent default | — |

**The table of governed lists — one row for every list any coded attribute names.** These are its columns. A row is complete when every column has an answer or a written reason for having none, on the same test as every other line of this form.

| Column | What to write | Rule |
|---|---|---|
| List | The name the model uses for it, as the coded attributes name it | EM-47 |
| Classification | This system's and nobody else's; this system's and published for others; held elsewhere, consumed here; not held at all — held instead by ____ . Made from this system's position | EM-2, EM-45, EM-46 |
| Issuer | The body whose act makes a value a member — never the software that serves the list. Or *not stated by the client; asked of ____ on ____* . Not asked where the list is this system's and nobody else's | EM-48, EM-50 |
| Where the issuer publishes it | The document, register, view or service a reader goes to for the current edition, and the place in it. Or *not stated by the client; asked of ____ on ____* . Not asked where the list is this system's and nobody else's | EM-49, EM-50 |
| Source in the client's material | The document, the place, the words — or that the client was silent, and who was asked and when | EM-50 |
| Consumers known | Only where the classification is *published for others*: who, from the client's material, or *none named*. On every other answer, *not applicable* | EM-45 |

### 5.4   For each glossary entry

| Line | What to write | Rule |
|---|---|---|
| Term | The one name this model uses for the concept | EM-34, EM-37 |
| Definition | What the thing is. Singular, standing on its own, not repeating the name, carrying no rationale and no procedure | EM-36 |
| Why it is not a record | The system keeps no rows of it. Where it does keep rows of it, the entry is deleted and the entity model names it instead | EM-35 |
| Other names for it | ____ — every other name a reader may arrive with, including the one an older document used | EM-37 |
| Where the term comes from | The instrument, the published vocabulary, or this organisation — and for an instrument, its citation | EM-36, EM-39 |
| Drawn from legislation | No; or yes, reproduced as the instrument has it, cited ____ , with the working word recorded as another name | EM-39 |
| Status | Proposed; in use; withdrawn — and if withdrawn, the date, the reason, and what replaces it | EM-36, EM-38 |
| Where it is used | The records, use cases or rules relying on it: ____ | EM-36 |

### 5.5   For each business rule

| Line | What to write | Rule |
|---|---|---|
| Identifier | The stable reference every use case, screen and computation cites. Allocated once, never reused | EM-40 |
| Statement | The rule, short, standing on its own, with nothing of the flow that invokes it | EM-41 |
| Settings it reads | None; or each, by the name its entry in the catalogue of settings in `SDD-04` carries. The statement names the setting and carries no value of it | EM-42 |
| Terms it uses | Every one of them, each already in the glossary or named in the entity model. A term in neither is a finding against the glossary | EM-42 |
| What it constrains | The records, attributes or relationships it binds: ____ | EM-42 |
| Where its authority comes from | A statute or instrument with its citation; a published policy; or this organisation's own decision, with the ruling that took it | EM-42 |
| From when it takes effect | A date — and where it has stopped applying, the date it stopped | EM-42 |
| Status | Proposed; in force; withdrawn — and if withdrawn, the date, the reason, and what replaces it | EM-42, EM-43 |
| What cites it | The use cases, screens and computations citing this identifier. **An empty answer is reported as a finding and is not a failure** | EM-44 |

### 5.6   One row of the table, filled: one kind of licence

*A simulated case for Progressa, a fictional country; every institution, name, date and figure in it is invented. In this copy of the standard it replaces the row of the edition of record, which was filled from a real client's document.*

This is not a sixth part of the form. It is one row of the table of governed lists, filled from a client's document — the terms of reference PHEQA, Progressa's quality authority for higher education, gave its supplier for the application that registers and licenses private institutions — for the list that document names most often and defines nowhere. It is printed so that the table has been filled once before anybody is asked to fill it, and so that a reader can see how a line that cannot be answered is written.

| Column | Entry |
|---|---|
| List | kind of licence |
| Classification | held elsewhere, consumed here — with the source line marked as a question, because the client's words place the kinds of licence in Progressa's Higher Education Regulations and never say whether PHEQA may add one |
| Issuer | *not stated by the client.* To be asked of the Registrar of PHEQA, whom the client's own table of responsibilities names as the owner of PHEQA's rules. Not yet asked on the date this row was written |
| Where the issuer publishes it | *not stated by the client.* The client names the Regulations, published in the Gazette, which state two kinds, a provisional and a full licence, and a page of PHEQA's website that lists *"the licences we grant"*. Neither is a place a reader goes for the current list. To be asked with the issuer |
| Source in the client's material | The terms of reference, section 4.2, the table of the records PHEQA keeps, row *Licences*; section 6.1, the list of the rules the service follows, row *article 11*; and the absence of any definition — the phrase occurs 37 times in the document and is defined in none of them, counted on 21 September 2026 |
| Consumers known | not applicable — the classification is *held elsewhere* |

**What a reader could fill from the client's words.** That *kind of licence* is a value a field takes and not a record of this system: it appears as a key, a filter and a breakdown, and never as a heading in the client's own table of records. That the values come from elsewhere: the client says the kinds of licence are those the Regulations state, and the Regulations are not PHEQA's to change. That this system may not add one: the same document lets the Registrar configure the standards new institutions are judged against and says nothing of the kind for a kind of licence. Every one of those is derived, and the source line says from which sentences, so that a reviewer can disagree with the derivation and point at the sentence.

**What stays open, and how the open lines are written.** Who issues a kind of licence — the minister, since each exists by the Regulations, or PHEQA, which grants it — and where the current list is published. The client's document does not say, and no amount of reading it will. The two lines are written as *not stated by the client*, with the office to be asked named from the client's own table of responsibilities, and the date added when the question is put. A row written that way is complete under P8: every line has an answer or a written reason for having none, and the reasons can be counted — one classification from the client's words, two lines waiting on a named office, none resting on nothing.

**What the row cannot show, and the review must.** PHEQA's later register carries the kind of licence as a list issued under the Regulations, and the period for which each kind is granted as PHEQA's own setting. One word of the client's is a list held elsewhere and a set of values configured here, and the client's document never separates them. The act that fills the row produces one row; the reviewer's question in part 6.2 — whether the thing described is one kind of thing or two run together — is what splits it. That is not a failure of the row. It is the reason the review has a human half.

## 6   The quality check, which is also the review gate

Run this before an entity model is agreed, and before anything is built from it. A model passes when every line of the form in part 5 has an answer or a written reason for having none. An unanswered line is recorded with an owner, not waved through.

### 6.1   What a program will refuse, once the checks are built

*None of the checks below is built. They are printed here so that an analyst knows what will be read mechanically, and so that whoever builds them knows what to build. No result of any kind may be reported from this section until they exist.*

|  | What the program reads | What makes it fail | Rule |
|---|---|---|---|
| C1 | every record's definition | absent, empty, or the record's own name with nothing else | EM-15 |
| C2 | every record's definition | it defines itself — the name followed by is a and nothing further | EM-15 |
| C3 | every record's definition | it carries usage or rationale: used by, so that, in order to, because | EM-15 |
| C4 | every record's name | plural, or the same as another record's name | EM-16 |
| C5 | every attribute | no least and most stated | EM-17 |
| C6 | every relationship end | no degree, or no optionality, stated at that end | EM-17 |
| C7 | every relationship | no name, or a name that is related to, associated with, linked to, has, refers to | EM-26 |
| C8 | every relationship | many at both ends, unresolved | EM-28 |
| C9 | every relationship whose two ends are the same record | no statement of what the loop carries | EM-29 |
| C10 | every relationship | no statement of what happens at the far end when a row is removed | EM-31 |
| C11 | every relationship | it carries attributes of its own and is not declared a record | EM-27 |
| C12 | every record with special kinds | the covering answer or the overlap answer is missing | EM-14 |
| C13 | every coded attribute | it names no governed list, or names one with no strength of binding | EM-19 |
| C14 | every record | no boundary answer — authority, consumes, or does not hold | EM-2 |
| C15 | every record answering does not hold | no statement of where it is held instead | EM-2 |
| C16 | the model's heading | no level declared | EM-1 |
| C17 | a model declared at the highest level | a record carries an identifier, a column type or an index | EM-1 |
| C18 | the group assignments | a record is in no group; or a group holds more records than the size the model itself stated | EM-3 |
| C19 | the group assignments | a relationship crosses two groups and is shown in neither, or in only one | EM-3 |
| C20 | the model's heading | no extension rule stated | EM-4 |
| C21 | every record | no history answer | EM-21 |
| C22 | every record that keeps history | uniqueness stated over the identifier alone | EM-22 |
| C23 | the model's heading | no owner, or no change procedure | EM-5 |
| C24 | the counts | nothing. This one reports and never fails | EM-3, EM-6 |
| C25 | the model's heading | no glossary named, or no register of business rules named | EM-34, EM-40 |
| C26 | every glossary entry | no definition, an empty one, or one that is the term itself with nothing else | EM-36 |
| C27 | every glossary entry | no status, or no statement of where the term comes from | EM-36 |
| C28 | the glossary | two entries carrying the same term, or one concept carried by two preferred terms | EM-34, EM-37 |
| C29 | every term named in the entity model and in the glossary | it is in both | EM-35 |
| C30 | every withdrawn term and every withdrawn rule | no date, or no reason | EM-38, EM-43 |
| C31 | every business rule | no identifier, or an identifier already used by another rule | EM-40 |
| C32 | every term used in a rule statement | it appears in neither the glossary nor the entity model | EM-42 |
| C33 | every business rule | no statement of where its authority comes from, or no date it takes effect from | EM-42 |
| C34 | every business rule | nothing cites its identifier. This one reports and never fails | EM-44 |
| C35 | every record answering that this system is the authority | no statement whether anybody else consumes it; or *published for others* with no consumer named and no *none named* | EM-45 |
| C36 | every record not this system's and nobody else's | no issuer named, and no statement that the client was silent with who was asked | EM-48, EM-50 |
| C37 | every governed list any coded attribute names | it has no row in the table of governed lists | EM-47 |
| C38 | every row of the table of governed lists | no classification, or no source line | EM-47, EM-50 |
| C39 | every attribute name | it repeats the name of the record that holds it | EM-53 |
| C40 | every record | it is related to no other record and carries no written reason for standing alone | EM-54 |
| C41 | the model's heading | no layout convention declared | EM-55 |
| C42 | every relationship | no read-back recorded, in either direction | EM-32 |
| C43 | every line the form marks as first-pass | unanswered, where the model reports itself finished for the first pass | EM-56 |

Two of these report and never fail, deliberately. C24 is a count: no evidence was found for any threshold on the number of records or relationships a model should have, so none is enforced, and writing one would mean inventing a number nobody has counted. C34 is the other: a rule nothing cites may be dead or may be one nobody is maintaining, and a program cannot tell which. Both report and the owner decides.

Thirty-six of the fifty-six rules are named by a check above, counted on 14 September 2026 as the distinct rules the *Rule* column cites. The remaining twenty are judged by a person until checks exist for them. Version 0.2 gave the first of those two figures as twenty-six of forty-four; the same count taken the same way on that edition's table gives twenty-seven, and the difference is recorded here rather than corrected silently.

Version 0.4's table named thirty-one. The five checks version 0.5 added name five rules no check had named before: EM-53, EM-54, EM-55 and EM-56, which are new, and EM-32, which has been in the standard since version 0.1 and had no check until the read-back gave it something a program can read. EM-52 is not named by any check and cannot be: no program can read whether an attribute describes the record it is drawn on.

**Four checks that cannot be written, said plainly so that nobody implies otherwise.** No program can read whether the boundary was drawn in the right place; whether one name is carrying two things; whether a claim of *nobody else's* is true; or whether the body named as an issuer is a body rather than the software that serves the list. Each of those is a person's judgement, and each is on the list in part 6.2. The four checks above read whether the answers are present. They cannot read whether they are right, and a check result — once any exists — says nothing about that.

### 6.2   What only a person can judge

A program can see that a field is filled. It cannot see that what fills it is true. These stay on the review list however many checks are built.

- Whether a definition is true, as opposed to present.
- Whether the thing described is really one kind of thing, or two that have been run together.
- Whether the degree and the optionality on a relationship match how the business actually behaves, rather than how the first example behaved.
- Whether the boundary is drawn in the right place — whether a record this system claims authority over is really somebody else's register.
- Whether a claim that a record is this system's and nobody else's is true. A program can see that the answer was given and cannot see that nobody consumes the record; the actor catalogue and the catalogue of events are where a consumer the claim missed will surface.
- Whether one name is carrying two things — a shared code and a set of values this module configures under the same word — which a row of the table of governed lists cannot show and the second question on this list can.
- Whether the body named as an issuer is a body at all, and not the platform, database or service that stores and serves the list.
- Whether the branches of a special kind are the branches the business would recognise, and whether what is drawn as a branch is really a part somebody plays.
- Whether the governed list a coded attribute points at is the right list — and, where it points at a named selection, whether the selection is the module's to define.
- Whether a figure inside a rule's statement is a fact of law or a setting the administration may change. A program can see a number; it cannot see who may change it.
- Whether the picture, read aloud in both directions, says something a person from the business agrees with.
- Whether one notation has been used throughout, and whether what that notation cannot say has been written down somewhere else.
- Whether a relationship optional at both ends is meant.
- Whether each attribute describes the record it is drawn on, or the record the paper form printed it on.
- Whether a record that stands alone is genuinely standalone, or one whose relationships nobody has drawn yet.
- Whether the read-back was put to a business reader as a question, or recited at him.
- Whether the model is finished. No published test for this exists in any discipline or any of the six fields; the answer this standard uses is that every question is answered, or carries a written reason for having none.

### 6.3   The gate

Every line is answered before the model is agreed.

| Rules | Checkpoint | Passed |
|---|---|---|
| EM-1, EM-2 | The level is declared, and every record says whether this system is its authority, consumes it, or does not hold it — with the holder named where it does not | ☐ |
| EM-3 | The records are grouped into named groups small enough to read, and every relationship crossing two groups is shown in both | ☐ |
| EM-4, EM-5 | An extension rule is written, and the model names an owner and a procedure for changing it | ☐ |
| EM-6 | Every rule the model is judged against says whether a program reads it or a person judges it | ☐ |
| EM-7, EM-8 | The pictures carry what a reader can check, the rest is in the register beside them, and every picture is generated from one model | ☐ |
| EM-9, EM-10 | One notation is declared and used throughout, and what it cannot say is written down elsewhere | ☐ |
| EM-11, EM-15, EM-16 | Every record passes the four tests, carries a definition that says what one row is, and has a singular, unique name | ☐ |
| EM-12, EM-13, EM-14 | Dependence is declared at both ends; parts played are not drawn as special kinds; and every special kind answers both the covering and the overlap question | ☐ |
| EM-17, EM-18 | Every attribute and every relationship end states the least and the most, as two decisions; the minimums are the model's floor and not one screen's | ☐ |
| EM-19, EM-20 | Every coded attribute names its governed list, or a named selection of one, and the strength of the binding; a setting that selects from a list is bound at the strongest strength; and every list named is versioned with values retired rather than removed | ☐ |
| EM-21, EM-22 | Every record says which clock or clocks it keeps, every stored coded value carries the date it was resolved as at, and uniqueness on a record that keeps history is stated over the period | ☐ |
| EM-23, EM-24, EM-25 | No attribute holds more than one value at once; the normal form is stated with every deliberate departure recorded; made-up identifiers are absent or justified | ☐ |
| EM-26, EM-27, EM-28 | Every relationship is named; one carrying facts of its own is a record; none is left many at both ends | ☐ |
| EM-29, EM-30, EM-31 | Loops say what they carry; exclusive choices are in the model and not in a note; every relationship says what happens at its far end | ☐ |
| EM-32, EM-33 | Every relationship reads as a sentence in both directions, was read back to a business reader in the form EM-32 states with the answer recorded, and any relationship optional at both ends carries its reason | ☐ |
| EM-34, EM-35 | One glossary is named; one term carries each concept; and no word is in both the glossary and the entity model | ☐ |
| EM-36 to EM-39 | Every glossary entry carries a definition, other names, where the term comes from and a status; withdrawn terms keep their entries; statutory terms are reproduced and cited | ☐ |
| EM-40 to EM-44 | One register of business rules is named; every rule is written once with an identifier, short and free of its flow, carrying its terms, its authority, its effective date and its status; a rule that reads a setting names it and carries no value of it; withdrawn rules keep their entries; a rule nothing cites is reported | ☐ |
| EM-45 to EM-51 | Every record this system keeps says whether anybody else consumes it; every classification is made from this system's own position; every list a coded attribute names has one row carrying its classification, its issuer, where the issuer publishes it and the words it was derived from; every issuer named is a body and not a system; and all of it was written in the first pass | ☐ |
| EM-52, EM-53, EM-54 | Every attribute describes the record it is drawn on; no attribute name repeats that record's name; and every record is related to at least one other or carries the written reason it stands alone | ☐ |
| EM-55, EM-56 | One layout convention is stated and every generated picture follows it; and the form states which of its lines belong to the first pass, with the model reported as finished for that pass or outright | ☐ |
| The form | Every line of the five-part form, and every column of every row of the table of governed lists, has an answer or a written reason for having none | ☐ |

## 7   The ways people get it wrong

Each of these is a failure seen repeatedly, with the rule that corrects it. The fourth group — the failures about the model as a whole — is the one most often missing from a catalogue of this kind; the fifth is new in version 0.2 and the sixth in version 0.3.

#### About what is a record

| The failure | The rule |
|---|---|
| A record that is really a report, a screen or a step in a process | EM-11 |
| A record with exactly one row in it, forever | EM-11 |
| A record holding one fact, which belongs as an attribute of its neighbour | EM-11 |
| Four near-identical records for four parts one person plays | EM-13 |
| A branch structure that cannot hold a person who is two things at once | EM-13, EM-14 |
| A link that has quietly grown three attributes and is still drawn as a line | EM-27 |

#### About what a record holds

| The failure | The rule |
|---|---|
| A record drawn and never defined | EM-15 |
| A definition that repeats the name, defines two things at once, or explains why the attribute exists instead of what it is | EM-15 |
| Every attribute marked required because one screen required it | EM-18 |
| A coded attribute whose list has no owner, or whose strength of binding is not stated | EM-19 |
| An attribute bound to a whole list when it is bound to a selection of it, so that a control offers thirty values where three apply — or a list minted locally to carry the slice | EM-19 |
| A code value deleted rather than retired, silently rewriting what older rows mean | EM-20 |
| A stored code with no date on it, resolved against today's list when it is read | EM-21 |
| An attribute written on the record the paper form printed it on, not the record it describes | EM-52 |
| An attribute whose name repeats the name of the record holding it, so that the same fact on two records is not seen to be the same fact | EM-53 |

#### About relationships

| The failure | The rule |
|---|---|
| An unnamed line | EM-26 |
| A line named related to or associated with | EM-26 |
| A line with no marks on it, which every reader completes differently | EM-17 |
| A many-to-many line left unresolved and handed to whoever builds the database | EM-28 |
| A loop back to the same record with no statement of what the loop means | EM-29 |
| An exclusive choice written in a note beside the picture instead of in the model | EM-30 |
| No decision about what happens at the far end when a row is removed | EM-31 |
| A record connected to nothing, left in the model because nobody was asked whether it stands alone | EM-54 |

#### About the model as a whole

| The failure | The rule |
|---|---|
| No boundary statement, so the model grows until somebody stops it for reasons of time | EM-2 |
| A second copy of a register somebody else is the authority for | EM-2 |
| One picture of the whole model, printed large, admired, never read | EM-3, EM-7 |
| A model at the highest level carrying identifiers, column types and storage hints | EM-1 |
| Several pictures maintained by hand beside the model, at least one wrong and nothing saying which | EM-8 |
| Two notations mixed in one model | EM-10 |
| A model with no owner and no written procedure for changing it | EM-5 |
| A model declared finished because the automatic checks are quiet | EM-6, P8 |
| Pictures generated to no stated convention, so that the same model reads differently every time it is drawn and nothing can be found by reading across it | EM-55 |
| A model written before any goal was named, judged against the whole form, and reported as unfinished when it is only early | EM-56 |

#### About the glossary and the register of rules

| The failure | The rule |
|---|---|
| A glossary required by a standard in force, kept as a list of words with no definitions | EM-36 |
| One concept carrying two names in two parts of the model, found by nobody because it can only be found by reading across | EM-34, EM-37 |
| A word in the glossary that the system in fact keeps rows of, so that two documents define it and they drift | EM-35 |
| A statutory term quietly rewritten into house words, so that the system means something the law does not say | EM-39 |
| A term deleted when it fell out of use, leaving last year's document meaning nothing | EM-38 |
| A business rule stated inside the prose of one flow, invisible to every other use case | EM-41 |
| A rule with no identifier, cited by nothing and citable by nothing | EM-40 |
| A rule carrying no statement of where its authority comes from, so nobody can tell a statute from a preference | EM-42 |
| A threshold written into a rule's statement and into the catalogue of settings, the two drifting, and nothing saying which one the system applied | EM-42 |
| A rule withdrawn by deletion, so that a decision taken under it can no longer be explained | EM-43 |
| A register of rules nobody cites, growing because adding is easier than checking | EM-44 |

#### About what the system depends on

| The failure | The rule |
|---|---|
| A system that posts its outcomes to two other systems, and no record says so | EM-45 |
| A model that writes another system's answer on its own rows — the service's *published* copied onto the module that reads it | EM-46 |
| The facts about one list carried on every attribute that uses it, and drifting; four fields naming the right list under the wrong identifier | EM-47 |
| A register naming the platform that serves a list as the authority that issues it | EM-48 |
| A published list with no address anywhere, so that a change cannot land and a snapshot has nothing to cite | EM-49 |
| A classification nobody can tell from one the client stated; a silence nobody can count | EM-50 |
| A classification added when a goal turned out to need it, so that the design wrote its own measure | EM-51 |

## 8   The questions this standard does not answer

A standard that hides what it cannot yet say is worse than one that names it. Eight things are unsettled, and nine further questions are asked by a reviewer without being rules.

### 8.1   What is not yet settled

How much detail a model carries

Whether a record is drawn with three attributes or thirty is the one question this standard states and does not answer. Until it is settled, the analyst records the depth she worked at and keeps to it consistently within one model.

Version 0.5 added EM-56, which says when the lines of the form must be answered, and it is worth saying plainly that this does not answer the question above. A line answered in the first pass may still be answered thinly, and nothing in this standard says how thin is too thin. What EM-56 removes is a different complaint: that a model written before any goal was named could only be reported as unfinished.

Which level this standard is itself written for

The standard requires every model to declare its level. It does not yet say which of the three levels it is written for.

How an entity model is cut for delivery

The companion standard for use cases explains how a use case is cut into pieces small enough to build. Nothing equivalent is written here, because nothing was found on it. It is a gap, and it should be filled by somebody who has looked.

Whether a term may be withdrawn while a document still in force uses it

EM-38 says a withdrawn term keeps its entry so that older documents stay readable. It does not say whether the withdrawal may happen at all while something in force still depends on the term. The register's owner decides, under IOS-16, and this standard offers no test.

Whether a rule that changed is a new version or a new rule

EM-43 requires a rule to be versioned. It does not say whether a rule whose substance changed keeps its identifier at a new version or is withdrawn in favour of a new identifier. Both are defensible, the two answers make different things easy to trace, and no field was found stating either. The register states which convention it follows and keeps to it.

Whether a relationship may join three or more records

The words in part 2 say a relationship is a link between two records, or between a record and itself, and every rule in part 4.3 is written for that shape. A relationship that genuinely holds between three records at once, and cannot be split into two-way links without losing what it says, is neither governed nor forbidden here: the question was never asked of the disciplines or of the six fields. An analyst who meets one records it as an open question against her model and says so, rather than forcing it into pairs quietly.

The founding discipline's own metamodel offers a shape that would settle part of this, and it is recorded here as a candidate rather than adopted. In that metamodel the relationship end, not the relationship, is the thing the model holds: a relationship is made up of exactly two ends, an exclusive choice between relationships is made up of more than one end drawn from several, and a unique identifier is made up of components each of which is either an attribute or a relationship end. Read that way, EM-30 would have a structure instead of an instruction, EM-12 and identity would meet in one place rather than two, and a relationship joining three records would have a definite answer. It is not adopted because adopting it changes part 2's definition of a relationship, on which every rule in part 4.3 is written, and nothing has been tested against that change.

What a value another system writes inside a record this system owns is

A record this system is the authority for may carry a value another system writes — an outstanding amount refreshed from a ledger, a priority computed by a scoring platform. The record's classification is this system's; the value's is not. This standard classifies records and lists and has no line for a fact inside a record; `SDD-04` asks who writes each fact, three documents later. It is a third kind of thing beside the record and the list, and whether the first pass of this model should say so is not settled. It was considered as a fifth answer to the classification and refused, because it is a fact about an attribute and not about the record, and the refusal is recorded so that its absence is not read as a judgement that it does not matter.

What constrains an attribute that carries no code

EM-19 and EM-47 govern the coded attribute: it names a governed list, or a named selection of one, and states how strongly it is bound. Nothing governs the attribute that carries no code and is nonetheless constrained — a money amount whose currency, scale and permitted sign are the same on forty attributes across the model, a date that may not precede another, an identifier with a published check character. The founding discipline holds all of these in one place, a domain, which carries the format, the unit of measure, the permitted range, the validation rule and what a null means, and which may itself be a subset of another domain — the same relation version 0.4 introduced for a named selection of a governed list. Adopting it would give a constraint one statement instead of forty. What stops it being adopted here is EM-1: a format and a length read as the storage level, and a model at the highest level may not carry them. Whether a constraint the business states — amounts in this model are in lei to two places and are never negative — is a business fact or a column type is the question, and it is not settled. It is recorded rather than decided because deciding it wrongly either lets storage into the highest level or leaves the model silent about constraints the business actually states.

### 8.2   The questions a reviewer asks, which are not rules

Each of these was considered as a rule and did not clear the bar of evidence this standard sets. A reviewer asks about them; the analyst records her answer; nobody is in breach for answering differently.

1.   Is anything in this model really a report, a screen, a step in a process, a value worked out from other values, or a moment in time? The list of what may not be a record is stated nowhere.
2.   Does any record carry so many relationships that it is really two records? No threshold exists and none has been measured.
3.   Is the model finished? No published test exists.
4.   Does the model carry attributes that exist only to make the picture join up?
5.   Is the model too small or too large? The published surveys measure what models are, not what they should be.
6.   What happens to rows already carrying a value that has since been retired from its list?
7.   When the model is split across several pictures, is a relationship whose ends fall in two of them shown in both? Three widely used tools behave three different ways, and one loses the relationship entirely.
8.   Is the picture being used to assert something it cannot express? The general rule is stated; the list of forbidden assertions is not.
9.   Would an approach built for change rather than for clarity suit this module better?

## 9   Where these rules come from

Every rule in this standard had to clear one bar before it was written down: a recognised modelling discipline states it, and the same pattern recurs in at least two independent public-sector fields. Confident prose was not accepted as evidence, and a rule that could show only one field was not written as a rule.

The disciplines read were the founding work on entity-relationship modelling and the notations that came from it; relational design and the normal forms; class modelling and its treatment of multiplicity and generalisation; data-warehouse modelling and its idea of what one row represents; the published collections of recurring model patterns; the international standard on what a good definition of a data element is; and the literature on holding facts together with the periods they hold for.

The six public-sector fields every rule was tested against were health, customs, tax, financial services, justice and education. Where a discipline and a field disagreed, both were written down and the disagreement was kept rather than averaged away.

Four of the first thirty-three rules rest on a recognised discipline and on the judgement of the people who wrote it, rather than on two fields. They are: that a relationship is named in both directions; that a relationship optional at both ends is reviewed; that a made-up identifier belongs to the model of how things are stored; and that one notation is chosen and never mixed. They are named here so that a later reader can see exactly which rules would fall if that judgement turned out to be wrong.

### The eleven rules added in version 0.2, and how many of them cleared the bar

The eleven rules of parts 4.4 and 4.5 were put to the same bar, on 1 September 2026, against the same six public-sector fields. **Eight cleared it and three did not.** The tally is stated here rather than averaged into the paragraph above, because the two sets of rules were tested by different people at different times and a reader is entitled to see which is which.

| | Rules |
|---|---|
| **Cleared** — a recognised discipline states it and two or more independent fields state it too | **8** — EM-34, EM-36, EM-37, EM-38, EM-40, EM-41, EM-42, EM-43 |
| **This organisation's judgement** — a discipline or a standard of this estate's own states it, and fewer than two fields do | **3** — EM-35, EM-39, EM-44 |

The disciplines read for these eleven were terminology work and its standards for what a definition must be and for how a concept carries one preferred name and other names beside it; the metadata-registry standard on the formulation of data definitions; the registration procedures that govern how an item in a register is proposed, superseded and retired; and the business-rules discipline, which states that a rule is a statement standing on its own rather than a step inside a process. The fields the eight were found to recur across were health informatics, official statistics, register governance together with land administration, and the delivery of government services where legislation is expressed as rules that a system reads.

**The three that did not clear, and what each rests on instead.** **EM-35**, the boundary between the model and the glossary, is stated by `SDD-05` M22 in the same words and by nothing outside this estate; it is here because a standard in force requires it, not because a field does. **EM-39**, on terms drawn from legislation, is stated by no field: the nearest position running the other way is the rules-as-code literature, which translates statutory language into working terms as a matter of course, and a reviewer should read that before accepting this rule. **EM-44**, that a rule nothing cites is reported, has the same standing as `SDD-04` IOS-18, which did not clear either: the nearest external corroboration is a published data-quality check catalogue, which is a tool vendor's list and not a discipline's statement. **All three should be attacked first.**

**Two qualifications, carried over from the estate's own practice and true of this tally as well.** Register governance and land administration both sit under one international committee's programme and were counted as one field, not two. And **not one outside source was read in the original**; every locator above is as a searching tool reported it, and the exact clauses of the registration procedures were read only in a published preview of that standard.

### The seven rules added in version 0.3, and how many of them cleared the bar

The seven rules of part 4.6 were put to the bar on 2 September 2026, in two steps. The obligations they carry had been listed and tested by two runs earlier the same day against the nine fields fixed on 1 September, and three of the lines were found to rest on nothing anybody had read: where the issuer publishes it, the consumers known, and the answer *published for others*. This edition read for those three, against three of the nine fields chosen in advance — official statistics, public-sector base registries, and geospatial register governance — with three questions written down before anything was opened: whether a discipline requires a consumer to record where the data it uses is published; whether one requires a holder to record who consumes its data; and whether one distinguishes an authority that publishes from one that does not. **Two of the seven cleared the bar and five did not.**

| | Rules |
|---|---|
| **Cleared** — a recognised discipline states it and two or more independent fields state it too | **2** — EM-47, EM-48 |
| **This organisation's judgement** — a discipline or a standard of this estate's own states it, and fewer than two fields do | **5** — EM-45, EM-46, EM-49, EM-50, EM-51 |

**The two that cleared, and what each rests on.** EM-47's grain — that a list is a thing of its own, kept apart from the concept it codes and from the record that binds to it, with one entry — is stated by official statistics and by health informatics, and was located by this estate's earlier sweeps at `SDD-04` IOS-1 and IOS-28. EM-48's obligation — that a list somebody else governs names the body that governs it — is stated by register governance, official statistics and health informatics, located at IOS-28; what EM-48 adds, the place it is stated first, is a decision the owner took on 2 September 2026, and a decision removes an objection without supplying evidence.

**The five that did not, and what each rests on instead.** **EM-49**, where the issuer publishes it: no field read requires the consumer's own document to carry the address. Official statistics makes the reference itself resolve — a list is named by agency, identifier and version, and a registry turns that name into a location; base registries put the address in one national catalogue, written by the provider, with consumers recorded against it. The line is here on this organisation's judgement and on a measured need: two sets of values on one programme stopped a change from landing because no address for either existed anywhere. **EM-45**, the fourth answer and its consumers: one field, base registries, records for every service a system provides which bodies use it; the other two fields read do not. The two fields that speak at all treat being the authority for a fact as implying that others may take it, which is why *nobody else's* is written as a claim at a date and not as a state. **EM-46**, the position a classification is made from: base registries make the same datum basic in one database and derived in every other by construction, and nothing else read states it; the rule rests on that and on the method's own shape, one model per system. **EM-50**, the source line: it did not clear when the register of requirements asked the same of its entries, with one industry behind it, and it rests here on the method's own principle that a measure must be checkable against the client's material. **EM-51**, the first pass: stated by the method volume and by nothing outside this estate. **EM-49 and EM-45 should be attacked first.**

**What the reading did not do, so that nobody reads more into the tally than it holds.** Not one source was read by eye; every quotation and every clause number is as a fetching tool reported it, and one document in the third field — the sub-clauses on the provenance of code lists held by third parties and on referencing a list rather than downloading it — could not be opened past its contents page by any means available, and is recorded as unread. Two fields of the nine were not read at all for these rules, because the commission fixed three. The reading and its verdicts, question by question, are kept with this edition's working papers.

### The four clauses added in version 0.4, and what each rests on

Version 0.4 added no rule. It added four sentences to three rules, on 6 September 2026, from two answers settled earlier in the same week — what a specification owes a fact it shares rather than owns, and what it owes a value the administration may change — each of which had swept its obligations against fields fixed before searching. A clause is claimed with the rule it joined and is not tallied as a rule; what each rests on is stated here so that a reader can see which sentence falls if its footing does.

**EM-42's clause and EM-21's should be attacked first.** Both rest on nothing outside this estate. A reader who holds that the screen's clock (`SDD-07` rule 18) and the list's retirement outcome (`SDD-04` IOS-31) between them cover the stored value reverses EM-21's clause on that ground, and the case against that reading is the value that never crosses a screen. A reader who holds that a rule's authority line already covers the figure inside it reverses EM-42's clause, and the case against is the figure the administration changed on the day while the rule still carried the old one.

| | Clauses |
|---|---|
| **Cleared** — a recognised discipline states it and two or more independent fields state it too | **2** — EM-19's selection: health informatics binds an element to a value set drawn from a code system, and official statistics exchanges a partial code list extracted from the full one (the master-data sweep of 2 September, K-17). EM-19's binding of a setting to a member the list carries: health informatics, register governance and telecommunications catalogues, for membership and for a status fact on the member that admits it or not (the configurability sweep of 3 September, K-16) |
| **This organisation's judgement** — tested against the fields, and no field states it | **2** — EM-21's date on a stored coded value: the fields date the *list's* versions and none puts the date on the stored value (K-07 of 2 September, the record's side); adopted for a measured need, one attribute on one programme carrying two clocks, *frozen on the posting* in the record and *today* on the worklist, and no date on the value to say which. EM-42's naming of a setting in a rule's statement: no field states it, and tax administration names rates and rules together as things configured, which cuts the other way (K-15 of 3 September); adopted for this estate's own case, a threshold sent by `SDD-04` IOS-27 to a register that had no line for it |

### The five rules added in version 0.5, and how many of them cleared the bar
The five rules of version 0.5 were put to the same bar on 14 September 2026. **None of them cleared it. All five rest on this organisation's judgement.** The tally is stated first because it is the weakest of the four, and a reader deciding how much of this version to trust should begin here rather than at the rules.

|  | Rules |
|---|---|
| **Cleared** — a recognised discipline states it and two or more independent fields state it too | **0** — none |
| **This organisation's judgement** — a discipline or a standard of this estate's own states it, and fewer than two fields do | **5** — EM-52, EM-53, EM-54, EM-55, EM-56 |

The discipline behind all five is one: the founding work on entity-relationship modelling and the conventions published with it — the chapter on basic conventions and definitions, and the appendix carrying the detailed definitions of entity, relationship, domain and attribute. Every one of the five is stated there, and this is the first source in this standard's history that was read from the printed page rather than through a searching tool. **Not one of the five was tested against the six public-sector fields**, because no sweep was run for this edition, and a rule that has not been tested cannot clear a bar that requires two fields. That is a statement about what was done and not a claim that the fields are silent. A later edition that runs the sweep may move some or all of the five, and may equally find nothing.

**What each rests on.** EM-52, that an attribute describes the record it is drawn on, has the firmest footing of the five: the discipline states it, and the normal forms already behind EM-24 state the same thing in other words, since an attribute dependent on something other than its record's identifier is exactly what the second and third normal forms forbid. That is one discipline and one restatement of it, not two fields, so it does not clear. EM-53 and EM-54 are stated by the discipline and by nothing else read. Both are cheap to keep and cheap to check, which is why they are rules rather than reviewer's questions in part 8.2, and either could be dropped without touching anything else in the standard.

**EM-55 and EM-56 should be attacked first.** EM-55 rests on a layout convention written for diagrams drawn by hand, and its whole value here is the claim that fixed positions make duplicate records findable by adjacency — a claim this organisation has not measured, and one that a generated picture may not reproduce at all. A reader who holds that the convention is taste reverses it and loses only the sentence in EM-34 that had no method. EM-56 is the more serious of the two, because it changes the completeness test the whole standard turns on, on the authority of two column headings in one appendix. A reader who holds that one bar is better than two reverses it, and nothing else in the standard falls with it.

**The clause added to EM-32, and the sentence added to EM-26.** The clause gives the form of words a relationship is read back in. It adds no obligation the rule did not already carry — EM-32 has required both directions since version 0.1 and part 6.2 has asked since then whether the picture read aloud says something a business person agrees with — and it is claimed with EM-32, as version 0.4's clauses are claimed with the rules they joined. It rests on the same single discipline and is not separately tallied. The sentence added to EM-26 carries no obligation at all: it names a published vocabulary of paired end names as a resource and says plainly that nothing is in breach for keeping none. It is not claimed under part 11, and it is recorded here so that its absence from the conformance claim is not read as an oversight.

**What this reading did not do.** No field was swept. No other discipline was opened. The three earlier tallies are untouched and none of their verdicts was revisited, although the discipline read for this edition is the same one the four rules of version 0.1 named in the paragraph above already rest on — which means that reading confirmed the discipline half of EM-32 and added nothing to the field half of anything.

It has not been used to draw a model, and no reader unfamiliar with this work has yet been asked to follow it. It came into force by the owner's ruling of 29 September 2026 before either had been done. Both of those are the next things to do, and what they find is the fix list.

## 10   Recording the result of a review

### 10.1   How a review result is written down

When a model is reviewed against this standard, the result is written rule by rule.

For each of the fifty-six rules, the reviewer writes down whether the model meets it. Where the model does not meet a rule, the reviewer writes what is wrong and the name of the person who will settle it.

A problem that has been written down, with a name against it, does not stop the model from being agreed. A problem that was found and not written down does. The difference matters. A model with three recorded problems and three named people is a model somebody is working on. A model with three unrecorded problems is a model nobody can rely on.

Three things follow.

1.   No review may report a result from the checks in part 6.1. None of those checks has been built. A review that says the checks passed is a statement about a program that does not exist.
2.   A review that records no problems at all is a warning and not a result. Every model of any size meets something it cannot settle. A review that reports nothing has probably not looked.
3.   A model that meets every rule is complete. It is not, by that fact, correct. Part 6.2 lists what only a person can judge, and part 1 states the promise this standard makes: that the questions were answered, not that the answers are right.

### 10.2   Whether the model carries enough detail

Part 8.1 states that this standard does not say how much detail a model should carry, and that no published test for it was found in any of the disciplines or fields read. That remains true. Nothing here settles it.

Until it is settled, the working test is the next document.

The model carries enough detail when the two documents written from it can be written without returning to the analyst for a fact the model should have held: the screens of a use case, and the application model. Where either has to come back for such a fact, the model was drawn too thin. The missing fact is written down, with the name of the person who will decide whether it belongs in every model or only in this one.

This is a working test and not a rule. It is written here because it can be applied today, and because what it turns up is the evidence a real answer would need. It is expected to be replaced by what use shows, and until then no model is in breach for failing it.

## 11   Conformance

A claim that an entity model conforms to this standard is made rule by rule, or it is not a claim.

To claim conformance is to state, for each of EM-1 to EM-56 in part 4, that the model satisfies it — and, where it does not, to have recorded a finding with a named owner and a date. **A finding with an owner does not defeat the claim. A failure that was never recorded does.** The seven rules of part 4.6 are claimed on exactly the terms the forty-four before them are claimed on, and on no others. A sentence added to a rule in version 0.4 is claimed with the rule it joined, as part of it, and a model that meets the rule's first sentence and not its second has not met the rule.

The five rules added in version 0.5 are claimed on exactly the terms the fifty-one before them are claimed on, and on no others. The clause version 0.5 added to EM-32 is claimed with EM-32, on the same terms as version 0.4's clauses: a model that names a relationship in both directions and records no read-back has met the rule's first sentence and not its second, and has therefore not met the rule. The sentence added to EM-26 carries no obligation and is not claimed, and no conformance claim may cite it.

Three things follow.

1.   No conformance claim may cite a check result. None of the checks in part 6.1 has been built; part 6.1 is written as what a program will refuse once the checks are built. A claim that says the checks pass is a claim about a program nobody has written.
2.   A count of zero findings is a warning and not a result. Every model of any size meets something it cannot settle. A model that reports none has probably not looked.
3.   Conformance says the standard was followed. It does not say the model is right. That is what part 6.2 is for, and it needs a person; the gate in part 6.3 is passed by a person and not by a count.

A claim made here says nothing about identity, ownership and state, or about the three registers beside them. Those are covered by `SDD-04` and are claimed against that document, separately. A claim about a list's row in the table of governed lists says what the row states and nothing about the list's entry in `SDD-04`, which is claimed there.

**Why this part exists, and what it is not.** Until version 0.2 this standard had no conformance clause at all, while six of the nine standards of the method carried one in the same words. Part 10.1 already required a review to be written rule by rule, which is the substance; what was missing was the sentence saying what a claim is. This part is that sentence, in the words the other six use, and adds no obligation the document did not already carry. It is a new final part, so no existing part number moves and no citation written against this document is invalidated. Version 0.3 changed one number in it, forty-four to fifty-one, and added two sentences; version 0.4 added one sentence, on how a clause is claimed; version 0.5 changed the same number again, fifty-one to fifty-six, and added one paragraph, on how the five new rules and the clause added to EM-32 are claimed. Nothing else about it has moved.
