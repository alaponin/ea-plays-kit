# SDD-02 · The Requirements Catalogue

*This copy is carried by sdd-kit, the SDD method's skills for the service design course. It keeps the edition stated below; where the edition drew an example from the method's author's own client work, this copy carries an example set in Progressa in its place and says so where it does.*

*How to write down what a client has asked for, so that everyone who builds the system afterwards is working from the same list*

*AN INTERNAL STANDARD · VERSION 0.3 · 29 SEPTEMBER 2026 · DRAFT FOR REVIEW*

*This document is a draft. It has not been approved and you should not quote it as binding. Section 12 explains its standing and tells you how much confidence each rule deserves. Please read that section before you rely on anything here.*

Field | Value
--- | ---
Document | SDD-02 · The Requirements Catalogue. How to write down what a client has asked for, so that everyone who builds the system afterwards works from the same list: what one entry carries, how entries are identified, how priority and status are expressed, and what the catalogue publishes. It carried the code RQ-01 until the edition of 31 August 2026.
Version and standing | Version 0.3 · 29 September 2026 · draft for review. It supersedes version 0.2 of 22 September 2026, which is kept in x_archive/. What changed: the line of this page that says who writes the document it governs now reads as the standard for the method reads in its figure 2 (SDD-01, section 4): an assistant extracts the catalogue from the client's material, and the analyst rules on it. Until this edition the line named the analyst alone. No rule was added, removed or renumbered, and how firm each rule is has not changed. It is not in force and should not be quoted as binding. An internal standard of FiscalAdmin OÜ, owned and approved by Aare Lapõnin, for the work of FiscalAdmin OÜ.
Who writes the document it governs | An assistant extracts it; the analyst rules on it. One catalogue for each system.
Who reads it | Everybody who builds from the list: whoever designs the screens, whoever designs the processes, and whoever decides what is delivered first.
When it is written | First of all the documents, and before any goal is named, because it is the measure the goals are counted against.
Rules | RQR-3 to RQR-29, twenty-five rules, in section 5. Not one of them has met this organisation's own bar for adopting a rule; section 12 says so on its face and states how firm the ground is under each.
What it does not cover | Section 2 names each boundary and where the subject belongs instead. The catalogue is not the specification document.
Author | FiscalAdmin OÜ · Aare Lapõnin

---

---

## 1. Why this document exists

### 1.1 The problem it addresses

When an organisation buys or builds a large system, the client writes down what the
system must do. The client usually writes it across several documents: an invitation
to tender, a specification, a policy paper, notes from meetings, a vendor's proposal.
These documents are written by different people, at different times, for different
readers. They repeat each other. They contradict each other. They are not a list.

Somebody then has to turn that material into a list. That list is what this document
calls **a register of requirements**: one numbered entry for each separate thing the
client asked for.

Everything built afterwards depends on that list. The people who design the screens
need to know which requirements a screen must satisfy. The people who design the
processes need to know which requirements a process must satisfy. The people who
test the system need to know what they are testing against. If the list is
unreliable, every piece of work that refers to it is unreliable as well, and nobody
finds out until the system is delivered.

### 1.2 What goes wrong when there is no agreed way of writing the list

These are not imagined problems. Each has been observed in real projects.

- The same number identifies different requirements in different documents, so a
  reference to "requirement 14" is ambiguous and cannot be resolved.
- Nobody records which sentence of the client's own documents a requirement came
  from, so nobody can check whether the list is complete.
- Every requirement is marked "must have", because no one recorded who decided the
  priority or when.
- A requirement is dropped, and a year later nobody can find out who decided that,
  or why.
- The list is embedded inside a much larger design document, and the design document
  measures itself against its own list, which proves nothing.

### 1.3 Where the register sits in the work

![Figure 1. Where the register sits in the work.](figures/SDD-02/SDD-02_fig01.png)

*Figure 1.  Where the register sits in the work.*

The register is written early, before the design begins, and it is written by a
separate act. Somebody reads the client's documents and extracts what the client
asked for. That person is not designing anything. They are recording.

Everything that comes later points back at the register. That is why the register
must be stable, and why an entry, once numbered, keeps its number for good.

---

## 2. What this document covers, and what it does not

### 2.1 What it covers

This document governs **the form of the register**: what one entry contains, how
entries are numbered, how priority and status are recorded, how an entry is changed
or withdrawn and by whom, what the register as a whole has to publish so that other
documents can refer to it, and what a person has to judge that no computer program
can judge.

It does not tell you *which* requirements to write. That depends on the client. It
tells you what shape the register has to be in, so that the work after it can be
done properly.

### 2.2 The register is not the specification document

![Figure 2. Why the register is kept separate from the design document.](figures/SDD-02/SDD-02_fig02.png)

*Figure 2.  Why the register is kept separate from the design document.*

Many organisations keep the requirements inside one large specification document,
together with the process model, the data model and the interface descriptions. This
document takes a different position: the register is a separate thing.

The reason is simple. If the list of things that must be covered is drawn from the
design itself, then measuring the design against that list will always show that the
design is complete. A document that contains both the requirements and the design,
and then compares one with the other, is agreeing with itself.

### 2.3 Subjects governed elsewhere

Each of these is deliberately left out, because another document governs it. Where
that other document does not yet exist, this is said plainly rather than filled in
here.

| Subject | Where it is governed |
|---|---|
| Whether a requirement has actually been built, and by which part of the system | The use case model, and the use case description |
| What a business rule, a glossary term or a data entity contains | The business rule register, the glossary, and the entity model |
| What makes two records the same thing, who may change each fact, and the statuses a record moves through | The standard for identity, ownership and state |
| Interfaces between systems, and anything specific to the technology platform | The architecture specification. **This document has not been written yet** |
| What a configurable value may be set to, and who may set it | The parameter register. **This document has not been written yet** |
| How a requirement becomes a test | The use case description, which pairs tests with the process they test |
| What a user sees on screen | The user experience standard |
| How to prove that a register is complete | **Nowhere. See section 10.** |

---

## 3. The words used here

These words have exact meanings in this document. Everywhere else, ordinary English
is intended.

| Word | Meaning in this document |
|---|---|
| **The client** | The organisation that asked for the system and is paying for it. Sometimes a government ministry, sometimes a company |
| **The register** | One numbered set of entries, each recording one thing the client asked for, taken from the client's own documents |
| **An entry** | One row of the register. Everything in this document is decided for one entry at a time |
| **The statement** | The sentence that says what was asked for. One for each entry |
| **The source** | The client's document, the place in that document, and the words there, from which the entry was taken |
| **The kind** | Which of three an entry is. A **function** the system must perform; a **quality** it must have, such as speed or availability; or a **constraint** it must respect, such as a law |
| **The identifier** | The short name by which an entry is referred to from outside the register, for example `REG-FR-014` |
| **The ordering** | The sequence the entries are read in and grouped by — for example, by business area, or by chapter of the client's own document |
| **The priority** | How strong a claim an entry has on being delivered, using one scale fixed for the whole register |
| **The person who set it** | The person or role who decided a priority. Not the person who wrote the entry, unless they also hold that authority |
| **The status** | Where an entry has reached in its own life: proposed, in force, amended, withdrawn, or set aside |
| **Set aside** | The client asked for it, and it will not be delivered. The entry stays in the register, with a signature and a reason |
| **A test of observation** | One sentence saying what somebody would see if the requirement were satisfied. It is not a test script |
| **A parameter** | A value that differs from one country or one installation to another, and is fixed outside the register |
| **A recorded gap** | Something this document cannot answer, written down with a named person responsible for answering it, and a date. This is the only permitted response to a question this document does not settle |

---

## 4. The four ideas the rules come from

Every rule in section 5 exists because of one of these four ideas. If you understand
the four, most of the rules will seem obvious.

### 4.1 Completeness is measured against the client's material, never against the register itself

![Figure 3. How completeness is measured, and how it must not be measured.](figures/SDD-02/SDD-02_fig03.png)

*Figure 3.  How completeness is measured, and how it must not be measured.*

The only honest way to ask "have we captured everything?" is to go back to the
client's own documents and check them, sentence by sentence, against the register.
That is possible only if every entry records where it came from.

If instead you measure the register against its own structure — its own chapters, its
own groups — you will always find that it is complete, because you drew the structure
from the register in the first place. This is the single most important idea in this
document, and the reason the source field is required.

### 4.2 The identifier is the only thing the outside world holds

Every document written after the register refers to entries by their identifiers, and
by nothing else. A screen design cites an identifier. A test cites an identifier. A
progress report counts identifiers.

So an identifier that means one thing in one document and something else in another
is not merely untidy. It breaks every count and every reference built on it. In one
project examined while this document was being prepared, 243 of the 248 quality
requirements carried a number that meant nothing outside the document it appeared in,
and 31 of those numbers referred to different requirements in different documents.

### 4.3 The register puts things in an order; it does not make decisions

A register groups its entries somehow, and any grouping is a choice. This document
asks you to declare the choice and say where it came from. It does not tell you which
grouping to use, and it does not allow the grouping to become the measure of whether
the work is finished.

### 4.4 A gap is written down with a name against it, never filled in locally

When this document does not tell you what to do, the correct response is to record
the gap, name the person who has to decide, and continue. Inventing a local answer
produces two organisations working to two different rules, and nobody notices for a
year.

---

## 5. The rules

There are twenty-five rules, in six groups. Each is written as an instruction, with
the failure it prevents, and a plain statement of how firm the ground beneath it is.

> **The line marked HOW FIRM on each rule tells you what stands behind it.** There are four possibilities, and section 12 explains them in full.
>
> **SUPPORTED OUTSIDE** — a recognised profession outside this organisation states it. **OUR OWN POSITION** — we looked for such a statement and did not find one; the rule is our considered judgement. **NOT YET TESTED** — nobody has yet looked for outside evidence at all. **REQUIRED BY OUR OWN METHOD ALREADY** — another document of ours states it, and the rule here adds only what that document does not say.
>
> **No rule in this document is supported by two independent industries**, which is what our method normally requires before a rule is adopted. That is the plain position and section 12 does not soften it.

### Group A · What the register is as a whole

#### RQR-3 · Mark any wording that is not the client's own
Where an entry's statement is not in the client's own words, mark it as a paraphrase
and give the client's words alongside it.
- prevents: A register of the analyst's sentences that looks exactly like a register of the client's sentences, so that a reader cannot tell which is which and cannot tell whether meaning has been lost.
- firm: OUR OWN POSITION, AND UNUSUAL. We have not found any published standard that requires this, and we have not found any organisation that does it. In the project we examined, 1,086 of 1,090 entries were written in the system's voice and not one was shown to be in the client's. This rule asks for something that has not been demonstrated anywhere. Adopt it only if you believe it on its merits.

#### RQR-4 · Say which of the three kinds each entry is
The register carries functions, qualities and constraints, and every entry says
which of the three it is.
- prevents: Qualities and constraints kept as a list at the back of the document, where they are given careless numbers and then cannot be referred to reliably. This is how quality requirements come to be ignored.
- firm: OUR OWN POSITION, NOT YET TESTED. We have not looked for outside evidence about this rule.

#### RQR-5 · Declare how the register is ordered, and where that ordering came from
State the ordering the register uses, and name the thing outside the register that
the ordering was taken from — for example, a published model for the industry, or the
chapter structure of the client's own specification. If you invented the ordering
yourself, say so.
- prevents: A grouping invented by the analyst quietly becoming the standard against which the analyst's own work is judged complete.
- firm: PARTLY SUPPORTED OUTSIDE. We found one documented case, in healthcare, of a requirement set ordered on a published industry model with the ordering declared. That supports declaring and attributing the ordering. It does not support any ranking of one source of ordering above another, so this rule gives none.

### Group B · What each entry contains

![Figure 4. What one entry contains.](figures/SDD-02/SDD-02_fig04.png)

*Figure 4.  What one entry contains.*

#### RQR-6 · One identifier for each entry, allocated once and never reused
Each entry has exactly one identifier. It is allocated once, it is never given to
another entry, and it is never renumbered.
- prevents: The same number identifying two requirements, which makes every reference to it ambiguous.
- firm: OUR OWN POSITION, WITH STRONG INTERNAL EVIDENCE. Our own method already asks for a stable identifier; what this rule adds is that it is never reused or renumbered. In the project we examined, every clash of identifiers was caused by the way identifiers were formed, and one family of requirements that used a properly scoped identifier had no clashes at all across eleven documents.

#### RQR-7 · Each entry declares its kind
Each entry states whether it is a function, a quality or a constraint.
- prevents: A constraint being read as a function by the only document that had to act on it.
- firm: OUR OWN POSITION, NOT YET TESTED.

#### RQR-8 · Each entry carries the statement in a field of its own
The sentence saying what was asked for is a field of the entry, not prose written
around it.
- prevents: Statements living in the paragraphs between the rows, where nothing can read them and nothing can count them.
- firm: REQUIRED BY OUR OWN METHOD ALREADY. What this rule adds is that the statement is a field.

#### RQR-9 · Each entry names its source
Give the client's document, the place within it, and the words there.
- prevents: The failure that everything in section 4.1 depends on. A register that cannot be compared with the material it came from can only be compared with itself.
- firm: SUPPORTED OUTSIDE, IN ONE INDUSTRY. A European standard for space engineering requires that the party responsible for each technical requirement is identified, together with traceability back to sources and a unique identifier. That is the strongest outside support any rule in this document has. Note two things. First, that standard allows the information to be held in a separate file rather than on the entry itself, so the obligation may be about being able to *find* the source rather than about *printing* it on the entry; this is unresolved. Second, in the project we examined, only about a quarter of the entries that should have carried a source did so.

#### RQR-10 · Each entry carries a test of observation
Write one sentence, in the language of observation, saying what somebody would see
if the requirement were satisfied. Do not use the word "shall". This is not a test
script.
- prevents: An entry that nobody can tell has been met, which is discovered at acceptance, when it is expensive.
- firm: OUR OWN POSITION. In the project we examined, this field was filled in every single case where the column existed, and the sentences were genuinely different from the requirement statements rather than restatements of them. That shows the practice is possible and was followed consistently. It does not show that it is correct.

#### RQR-11 · Each entry carries a priority, and records who set it
Record the priority, and record the person or role who decided it.
- prevents: A register in which everything is marked "must have" and nothing records who said so. A priority that nobody signed carries no information and cannot be discussed.
- firm: PARTLY SUPPORTED OUTSIDE, IN ONE INDUSTRY. Two widely used approaches in public administration both place the ordering of work with one named accountable role, and both make that role's decisions visible. Neither says anything about recording what the priority was set *against*, so this rule does not require that.

#### RQR-12 · Each entry carries a status
One of: proposed, in force, amended, withdrawn, set aside.
- prevents: An entry that was decided against looking exactly like an entry that was never considered.
- firm: OUR OWN POSITION. In the project we examined, no entry carried a status at all.

#### RQR-13 · Declare where variation is described, and make every parameter name resolve
Some requirements behave differently in different countries or installations. State
where the register describes that variation — either in a separate variation model
that refers to entries, or as a marker on the entry itself. Whichever you choose,
every parameter name used must refer to exactly one entry in the parameter register.
- prevents: A behaviour that differs between installations, with nothing recording what controls the difference; and a set of parameter names that nobody maintains.
- firm: OUR OWN POSITION, AND DELIBERATELY CAUTIOUS. Published practice appears to favour a separate variation model over markers on the entries, and one published standard for this subject recommends keeping variation separate. We have therefore written the rule so that it does not require either arrangement, only that you declare which you use and that the names resolve. Note also that the parameter register does not yet exist, so the second half of this rule cannot be checked by any program today.

#### RQR-14 · An entry contains no design
An entry does not contain a field list, a data type, a screen, a protocol or anything
specific to the technology. Where it would, it refers to the document that governs
that subject instead.
- prevents: A requirements register that has quietly become a design, and design decisions taken by whoever happened to be writing requirements that week.
- firm: OUR OWN POSITION, SUPPORTED BY OUR OWN METHOD. We found no outside evidence either way.

### Group C · How identifiers are formed

#### RQR-15 · The identifier names the kind and a number, and nothing else
Use one series of numbers for each kind within each register.
- prevents: Identifiers that stop making sense when the thing they describe is renamed.
- firm: OUR OWN POSITION, NOT YET TESTED, WITH STRONG INTERNAL EVIDENCE. See RQR-6.

#### RQR-16 · The subject of an entry is a field, not part of its identifier
Record the business area, module or subject as a field. Do not put it inside the
identifier.
- prevents: The commonest cause of clashing identifiers. Two documents each choose the same abbreviation for their own subject, and their numbering collides invisibly.
- firm: OUR OWN POSITION, NOT YET TESTED.

#### RQR-17 · An identifier survives renaming, withdrawal and merging
An identifier keeps its meaning when the subject is renamed, when the entry is
withdrawn, and when two registers are combined.
- prevents: References that stop working because somebody renamed a module.
- firm: OUR OWN POSITION.

### Group D · Priority and status

![Figure 5. The life of one entry, from proposed to withdrawn or set aside.](figures/SDD-02/SDD-02_fig05.png)

*Figure 5.  The life of one entry, from proposed to withdrawn or set aside.*

#### RQR-19 · One priority scale for the whole register
Fix one scale and define it once. Do not redefine it document by document.
- prevents: A scale defined twelve times in two incompatible forms, with levels that nobody ever uses because nobody agrees what they mean.
- firm: OUR OWN POSITION. We found no outside statement of this obligation.

#### RQR-20 · The priority is set by whoever holds the authority, and an unset priority is recorded as unset
Record who has the authority to set priorities, and let only that person set them.
Where nobody has set a priority, record it as not set. Never apply a default.
- prevents: Priorities that appear to be decisions and are in fact the setting the form arrived with.
- firm: PARTLY SUPPORTED OUTSIDE, IN ONE INDUSTRY. A public sector service manual separates the people who write requirements from the person who orders them. It also states that this is not the user's or the client's decision to make, so this rule does not say the client sets priorities — only that whoever holds the authority does. We found no study anywhere comparing priorities set by clients with priorities set by analysts.

#### RQR-21 · Setting something aside is a status, not a priority level
Do not add a lowest priority level that means "not doing this". Use the status.
- prevents: A priority scale asked to carry a decision it was not designed for. In the project we examined, the lowest priority level was defined twelve times and used zero times.
- firm: OUR OWN POSITION, NOT YET TESTED.

#### RQR-22 · Setting aside is signed, dated and explained, and the entry stays
Record who signed the decision, when, and why. The entry remains in the register.
- prevents: A requirement quietly deleted, so that a year later nobody can find the decision and the requirement returns.
- firm: OUR OWN POSITION. We found no outside support for the signature. We did find, in a related field, the practice of keeping the number of a withdrawn item and marking it as unused, which supports keeping the entry.

### Group E · Changing the register

#### RQR-23 · An entry is amended, never overwritten
Record what changed, and against which version of the register.
- prevents: A requirement changing underneath a document that was already written against it, with nothing recording that this has happened.
- firm: OUR OWN POSITION, NOT YET TESTED.

#### RQR-24 · A withdrawn entry is never deleted, and its identifier is never issued again
References to a withdrawn entry still resolve, and report that it is withdrawn.
- prevents: A reference that resolves to a completely different requirement because its number was given to something else. This is worse than a reference that fails, because nothing looks wrong.
- firm: OUR OWN POSITION. We tested this rule against outside sources and found neither support nor contradiction.

#### RQR-25 · A version of the register is its entries at their statuses on a given date
When another document claims to follow the register, it names the version it followed.
- prevents: Two documents claiming to follow "the register" and meaning two different things.
- firm: OUR OWN POSITION, NOT YET TESTED.

### Group F · What the register publishes

These three rules exist because other documents have to read the register mechanically.
They are the rules with the least evidence behind them, and that is stated plainly.

#### RQR-27 · Publish the entries as one named list, in one place, in one machine-readable form
A program must be able to read the whole list without knowing anything about the
document it lives in.
The published list is read by the use case model, which the standard for the use case model (SDD-05) governs: its rule M16 binds every goal to entries of this list by identifier, in both directions, and no other document is the measure of the goals' completeness.
- prevents: The inability to answer "how many requirements are not yet covered?", because there is no reliable total to count against.
- firm: OUR OWN POSITION, NOT YET TESTED.

#### RQR-28 · Every identifier resolves without the document it appears in
- prevents: The failure described in section 4.2. A screen design that refers to "quality requirement 4" refers to eleven different things.
- firm: OUR OWN POSITION, NOT YET TESTED.

#### RQR-29 · Every entry can be referred to individually
A reference to a group of entries is not a reference.
- prevents: Coverage that cannot be calculated, because a group is not a member of a list.
- firm: OUR OWN POSITION, NOT YET TESTED.

### One more rule, held back

There is a twenty-sixth idea that is deliberately **not** a rule of this document: that
an entry taken from existing material should carry its previous identifiers, so that
old references still work. It is a sensible idea, we found nobody who does it, and
nobody has measured what it would cost. It is recorded here so that it is not lost,
and it will not become a rule until somebody decides that it should.

---

## 6. The record sheet for one entry

Fill this in once for each entry. Every line names the rule that requires it. Where a
line has no answer, write the reason there is no answer. An entry is finished when
every line has either an answer or a written reason.

| Line | What to write | Required by |
|---|---|---|
| **Identifier** | The kind, and a number from this register's series for that kind | RQR-6, RQR-15 |
| **Kind** | Function · quality · constraint | RQR-4, RQR-7 |
| **Subject** | The business area or module. As a field, never inside the identifier | RQR-16 |
| **Statement** | The sentence saying what was asked for, in the client's words | RQR-8 |
| **Paraphrased?** | No; or yes, together with the client's own words | RQR-3 |
| **Source** | The client's document · the place in it · the words | RQR-9 |
| **Test of observation** | One sentence, in the language of observation, without "shall" | RQR-10 |
| **Priority** | A value of this register's scale; or *not set* | RQR-11, RQR-19 |
| **Set by** | The person or role, and the date; or *nobody — not set* | RQR-11, RQR-20 |
| **Status** | Proposed · in force · amended · withdrawn · set aside | RQR-12 |
| **If set aside** | Who signed it · the date · the reason | RQR-21, RQR-22 |
| **If amended** | What changed · against which version | RQR-23 |
| **Varies by installation?** | No; or the parameter names it depends on, each resolving to one parameter register entry | RQR-13 |
| **Recorded gaps** | Anything unresolved, with a named person and a date | Section 4.4 |

---

## 7. The record sheet for the register as a whole

Fill this in once for the register.

| Line | What to write | Required by |
|---|---|---|
| **Ordering** | What the register is ordered on, and the thing outside it the ordering came from; or *chosen by the analyst*, marked as such | RQR-5 |
| **Priority scale** | The fixed set of values, defined once | RQR-19 |
| **Where variation is described** | A separate variation model, or markers on entries — and where it is kept | RQR-13 |
| **Parameter register used** | Its name and version; or a recorded gap, with a named person, stating that none exists | RQR-13 |
| **Published as** | The name of the list · where it is kept · the form a program reads | RQR-27 |
| **Version, date and status** | As required of every document in this organisation | — |
| **Counts, stated and not judged** | How many entries; how many with no source; how many with no priority setter; how many with a parameter name that does not resolve; how many set aside. State the file each count was made on and when. **Set no target for any of them, and do not let anyone infer one** | Section 4.4 |
| **Columns never used** | List them. Each is a recorded gap with a named person | Section 4.4 |

---

## 8. Checking the work

![Figure 6. The two halves of checking, and why only one of them can be automated.](figures/SDD-02/SDD-02_fig06.png)

*Figure 6.  The two halves of checking, and why only one of them can be automated.*

Checking has two halves, and they fail in different ways. One half can eventually be
done by a computer program. The other half never can.

### 8.1 What a program will refuse, once such a program exists

> ⚠ **Please read this before the table.** No program described below has been written.
> ⚠ Nothing here runs today. The list is printed so that an analyst knows what will
> ⚠ eventually be read mechanically, and so that whoever writes the program knows what
> ⚠ to write. **No result of any kind may be reported from this section, and nobody may
> ⚠ claim that a register "passes the checks", until the program exists.**

| The check | It refuses when |
|---|---|
| Required fields | A required line of section 6 is empty and has no written reason |
| Identifier uniqueness | The same identifier appears twice in one series |
| Identifier reuse | An identifier that once belonged to a withdrawn entry has been given to another |
| Reference resolution | A reference into the register does not resolve, or resolves without reporting the status |
| Group references | A reference names a group of entries rather than one entry |
| Source | A source names no document, or names one without saying where in it |
| Priority values | A priority is not a value of the register's scale |
| Priority attribution | A priority is set and no setter is recorded, or absent and not recorded as *not set* |
| Status values | A status is not one of the five |
| Setting aside | A set-aside entry has no signature, no date or no reason |
| Parameter names | A parameter name does not resolve in the parameter register. **This check cannot be written at all until the parameter register exists** |
| Publication | The register does not publish one list in one machine-readable form |
| Test of observation | The sentence is missing, or contains the word "shall" |
| Ordering | The register does not declare its ordering, or declares one with no outside source and no mark saying it was chosen |
| Counts | *Nothing. This one reports the counts and never refuses* |

### 8.2 What only a person can judge

No program will ever settle these. A review that skips them has confirmed that the
boxes are full, not that the answers are right.

- Is the statement what the client meant, or what the analyst understood?
- Was the paraphrase necessary, or would the client's own sentence have served?
- Is the source the place the requirement really came from, or the nearest place that
  mentions it?
- Would anybody actually observe what the test of observation describes?
- Did the person who set the priority hold the authority to set it?
- Is the declared ordering the reason the register is arranged this way, or an
  explanation written afterwards?
- **Are these two entries the same requirement?** No mechanical method exists for
  this, and none is proposed here.
- Is the register complete against the client's material? See section 10.

---

## 9. Mistakes that happen often

Named so that a reviewer knows what to look for.

1. **A number with no scope.** A requirement numbered simply `14`, in a project with
   fourteen documents. Inside its own document it looks perfectly clear.
2. **A shared abbreviation.** Two documents each choose the same three letters for
   their own subject, and their numbering collides. Nobody sees this, because nobody
   reads two documents at once.
3. **A convention that is written down and not enforced.** A project may declare a
   format for citing sources and then use it in fewer than one entry in twenty —
   including in the very documents that declared it.
4. **A priority level that nobody uses.** Usually the lowest one, because it is really
   a way of saying "not doing this", which is a status and not a priority.
5. **A marker with its useful half missing.** A requirement is marked as varying by
   country, and does not say what controls the variation. About a quarter of them, in
   the project examined.
6. **A default priority.** Everything marked "must have", because that was the first
   value in the list and nobody recorded a decision.
7. **A reference to a group.** "Requirements 100 to 140 are covered by this process."
   This cannot be checked, and it is usually not true.
8. **A count made with the wrong detector.** A report that "no document has a change
   history" may mean that no document has one, or that the search looked only for a
   heading and missed the three that used a bold label instead. **Always record how a
   count was made.** A wrong zero looks exactly like a correct one.

---

## 10. Questions this document does not answer

These are recorded here so that nobody discovers them in the middle of the work.

1. **How to know that a register is complete.** This is the largest gap. Published,
   tested methods for measuring the completeness of a list of things that already
   exist do exist — they come from official statistics and from the science of
   research reviews, and both work by comparing two independently assembled lists.
   Neither has been examined to see whether it can be applied to requirements. Until
   somebody does that, completeness is a matter of careful reading.
2. **Whether the source must be printed on the entry, or merely findable from it.**
   See RQR-9.
3. **Whether the test of observation is always required, or only where the requirement
   is not already plain.** A register that filled the field in every single case has
   never tested whether the field is sometimes unnecessary.
4. **Whether a priority set by the client is better judged than one set by an analyst.**
   No study comparing the two appears to exist.
5. **Whether the register must always carry an accessibility requirement and a language
   requirement.** The screen standard says the register is the only route by which
   either can enter the design, and only if the register carries one. Somebody has to
   decide this.
6. **Where the background information lives that makes a single requirement
   understandable.** A requirement about a configurable identifier format is not
   understandable on its own; it makes sense beside the table of national variations
   it came from. This document relies on the source reference to solve that, and does
   not settle it.
7. **What the register is, physically** — a document, a set of files, or a table in a
   system. Deliberately open. RQR-27 says what it must publish, not what it must be.

---

## 11. How to say that you have followed this document

**A claim to have followed this document is made rule by rule, or it is not a claim.**

To claim that a register follows this document is to state, for each of the
twenty-five rules, that the register satisfies it — and where it does not, to have
recorded a gap with a named person and a date.

**A recorded gap does not defeat the claim. A failure that nobody recorded does.**

Three things follow.

1. **A count of zero recorded gaps is a bad sign, not a good one.** Work that finishes
   with nothing refused has almost certainly lowered the standard rather than met it.
2. **No claim may cite a check result.** None of the programs in section 8.1 exists.
3. **A claim made today says that the document was followed, not that the document
   works.** Section 12 explains the difference.

---

## 12. The standing of this document, and how much confidence each rule deserves

This section is the one to read before relying on anything above.

### 12.1 This is a draft

Version 0.2, dated 22 September 2026. It supersedes version 0.1 of 31 August 2026 and differs from it by one sentence, in RQR-27.
It is not in force and should not be quoted as binding.

### 12.2 The evidence behind the rules is thin, and each rule says how thin

This organisation's method requires that a rule enters a standard only where a
recognised profession states it and the same practice is found in at least two
independent industries. **Not one rule in this document meets that requirement.**

![Figure 7. How firm the ground is under the twenty-five rules.](figures/SDD-02/SDD-02_fig07.png)

*Figure 7.  How firm the ground is under the twenty-five rules.*

- **Four rules** — RQR-5, RQR-9, RQR-11 and RQR-20 — have published support from one
  industry, and only for part of what they say. They are offered for adoption on
  judgement, and adopting them is a decision somebody has to take.
- **Twenty-one rules** are this organisation's own position. We looked and found no
  profession that states them as rules. Several are supported by what we have
  measured in our own past work, which shows that a practice is possible, or that
  neglecting it causes harm — but not that anybody else considers it correct.
- **Ten of those twenty-one** have not been tested at all: nobody has yet searched
  for evidence about them. They are marked *not yet tested* on the rules themselves,
  and they are not the same as rules that were tested and found unsupported.

Some of the reading that would settle these questions has not been done. This is not
a claim that the evidence does not exist. It is a statement that we have not yet
looked in the places where it would most likely be found.

### 12.3 The test that has not been done

The most important test of a document like this one is to give it to somebody who has
never seen the subject, ask them to build a register from a client's documents, and
compare what they produce with what an experienced person produces. **This has not been
done.** Until it has, every difference between the two would count as a fault in this
document rather than in the reader.

**This document does not come into force until that test has been carried out.**

### 12.4 What this document does promise

It does not promise that two analysts given the same client documents will produce
the same register. No published profession promises that, and there is good reason to
think none can.

What it promises is smaller and is worth having:

> **Two analysts who have both finished will have answered the same questions about
> the same material.** Every difference between their registers can therefore be
> pointed at, and discussed, one question at a time. A register is finished under this
> document when every line of the record sheets in sections 6 and 7 carries an answer,
> or carries a written reason for having none. Nothing else counts as finished, and
> nothing more is required.
