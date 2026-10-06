# SDD-10 · The Sector Services Catalogue

*This copy is carried by sdd-kit, the SDD method's skills for the service design course. It keeps the edition stated below; where the edition drew an example from the method's author's own client work, this copy carries an example set in Progressa in its place and says so where it does.*

*The single statement of what the bodies of a sector owe and do for the people they serve: one boundary, every service, what each rests on, and the state it is in today*

*AN INTERNAL STANDARD  ·  VERSION 0.1  ·  25 SEPTEMBER 2026  ·  DRAFT FOR REVIEW*

*Twenty rules, a row header, and a review. Discharged once for the whole sector, never service by service.*

Field | Value
--- | ---
Document | SDD-10 · The Sector Services Catalogue. One boundary around a sector of several bodies, the customers outside it, every service the bodies owe or perform, what each rests on, and its state today.
Version and standing | Version 0.1 · 25 September 2026 · draft for review. It supersedes nothing: it is the first edition of a new standard, written under the ruling of 24 September 2026 that made the method for a sector's catalogue of services a standard of this series (rulings/2026-09-24-the-sector-services-catalogue.yaml). It comes into force only when the first catalogue written to it has claimed conformance rule by rule and passed its independent review, and the owner has accepted, as version 1.0, the edition that proof corrects. It is not in force and should not be quoted as binding. An internal standard of FiscalAdmin OÜ, owned and approved by Aare Lapõnin, for the work of FiscalAdmin OÜ.
Who writes the document it governs | One named architect, one catalogue for each sector.
Who reads it | The reviewer who decides whether a service may be specified from the catalogue, the analyst who extracts a register of requirements from a row, and the writer of a knowledge product drawn from it.
When it is written | Once for the sector, after the sector's instruments and record have been read, and before any service of it is specified or the register of requirements of any proof of concept is extracted.
Rules | SSC-1 to SSC-20, twenty rules, in sections 4 to 10, with the rules of SDD-05 that SSC-4 reads for a catalogue. None has yet been used by anybody who did not write it; section 15 says how firm they are.
What it does not cover | Section 1 names each boundary and where the subject belongs instead. The use case model of a service built beneath the catalogue is governed by SDD-05 as written, M9 and M16 included, and nothing here changes it.
Author | FiscalAdmin OÜ · Aare Lapõnin

---

Contents

1  What this standard is for

2  The words, defined once

3  The principles

4  Boundary and design scope

5  Actors

6  Identifying services and setting their size

7  Relationships

8  Structure, completeness and traceability

9  The catalogue record

10  From a row to what is built

11  The review

12  The ways catalogues go wrong

13  A worked catalogue

14  The questions this standard does not answer

15  Where these rules come from

Figures

Figure 1 — What the catalogue is written from, what it holds, and what is built from it.

Figure 2 — Three shapes a model of a sector could take, and the one this standard governs.

Figure 3 — Where a service sits: below a capability, above a goal completed in one sitting.

Figure 4 — One boundary around the sector, with a seam between two of its bodies drawn as a service.

Figure 5 — The one test of a service, set beside the three tests of a sitting.

Figure 6 — The order of precedence: what each kind of source may do in the catalogue.

Figure 7 — Completeness is checked outward and inward.

Figure 8 — The rows are the only part written by hand.

Figure 9 — Which parts of a row need direct access to the sector's bodies.

Figure 10 — From the row of a chosen service to a proof of concept.

Figure 11 — The worked catalogue: section 4 of one statute, read function by function.

## 1  What this standard is for

### What a sector services catalogue is

A sector services catalogue is the statement of what the bodies of one sector owe and do for the people and organisations they serve: one boundary drawn around the sector, the customers and counterparties outside it, every service the bodies inside it owe or perform, what each service rests on, which body owes it, and the state it is in today. Its unit is the service — one outcome that one body delivers to one kind of customer — and not the goal completed in one sitting at a system, which is the unit of a use case model.

It differs from a use case model in three things it carries and in everything it leaves out. It carries the obligation a service rests on, the body that owes it, and the state the service is in today, none of which the model of one system records. It carries no flows, no guarantees and no screens, because it states what a sector owes and does, and not how a system behaves.

There is one catalogue for each sector. Every obligation in this standard is discharged once across that catalogue, or once for each edition of it. None of them is discharged service by service. Where a rule needs something recorded on an individual row, it says what must be recorded and stops there.

The catalogue is the record of the sector's services and not the last word on any one of them. Beneath it stands one use case model for each service chosen to be built, governed by the use case model standard (SDD-05) as that standard is written, and seeded from the service's row. The catalogue holds what all those models share — one catalogue of actors, one vocabulary, one register of rules — so that they cannot come to disagree with one another.

![Figure 1](figures/SDD-10/SDD-10_fig01.png)

*Figure 1 — What the catalogue is written from, what it holds, and what is built from it.*

Why a catalogue with models beneath it, and not one model of the whole sector or a family of separate models. One use case model drawn around several bodies cannot keep to a goal completed in one sitting at one system without breaking every service into operations, and it cannot rise above that level without producing summary goals that return no result to a named actor. A family of independent models, one for each body, will disagree about who the actors are and what the registers hold, because nothing holds the models together. A catalogue with models beneath it gives every service that is built a model of its own, while one list of actors, one vocabulary and one register of rules stand above them all.

![Figure 2](figures/SDD-10/SDD-10_fig02.png)

*Figure 2 — Three shapes a model of a sector could take, and the one this standard governs.*

### Who designs it, and what they have in front of them

One person is accountable for the catalogue as a whole: an enterprise or solution architect, or a lead analyst, with the authority to settle where the sector's boundary runs and which bodies stand inside it. In front of them are the instruments that state what the sector's bodies owe — acts, regulations, orders and the treaties that bind the state — so far as they are held or can be retrieved; the record of what the bodies publish and are shown performing; the structure the catalogue is organised by, usually a capability map of the sector; and, where one exists, the sector's architecture, which names its registers, its systems and its roadmap. Every rule below is written to be applied from that position. Where a rule needs a decision that person cannot take alone, the rule says who takes it.

That person is not the one who writes the use case model of a service. Writing that model takes one row of the catalogue as its client's material, happens later, and answers to the use case model standard and to a different reviewer.

### What this standard does not cover

Several things belong elsewhere, and nothing here restates them. A rule written in two places is a rule that will drift, so where another standard governs, this one points at it and adds only what it does not say.

- The use case model of a service built beneath the catalogue. It is governed by SDD-05 as written, including its three tests of granularity (M9) and its binding to the register of requirements (M16). Nothing in this standard changes either of them or reads them differently.
- One use case written out in full, governed by SDD-06, and the screens that serve it, governed by SDD-07.
- The register of requirements of anything built from a row. It is extracted from the row by the separate act the requirements catalogue standard (SDD-02) describes; the row is its client's material and not a substitute for it.
- What a register means, what identifies one of its records and how its records relate. The catalogue names the sector's registers; the entity model standard (SDD-03) defines each one when a service that reads or changes it is specified, and the shared registers standard (SDD-04) governs them as seen from any application built beneath the catalogue, which reads them and does not own them.
- Flows, guarantees, screens, fields and any other design. A row carries none of them, and the boundary of a system is drawn in its specification and not in the catalogue.
- The matters of design and roadmap a sector's architecture answers: how an identifier is structured, how a register's integrity is controlled, where data is hosted, what a service costs and who operates a platform.
- A sector whose boundary holds one body only. Its services are the goals of one organisation, and it is modelled as a business use case model under SDD-05 (M2), not as a catalogue.

### What this standard promises, and what it does not

It promises that a catalogue built to it can be checked. Every condition it states is either something a reader can point at in the catalogue, or something the review in section 11 asks for by name and records an owner against when it is absent.

It does not promise that two architects cataloguing the same sector will write the same rows. What section 11 offers instead is the smaller thing: two catalogues built to this standard have answered the same questions about the same sector, so every difference between them can be pointed at and traced to a source.

It does not promise that a row's obligation truly is the service's mandate, or that its state is the state the service is in. The review tests that each is recorded, marked and bound; it does not test that what is recorded is true. Nor does it say when the sector's instruments and record have been read in full. Section 14 states both limits rather than leaving a reader to discover them.

### Claiming conformance

A catalogue conforms to this standard when it does three things.

- Declares the claim. “This catalogue claims conformance to the rules of this standard, SSC-1 to SSC-20.” The claim takes in the rules of SDD-05 that SSC-4 reads for a catalogue, and no others.
- States, rule by rule, how it satisfies each one and where. A claim without the line-by-line assessment is not checkable, and is therefore not a claim.
- Passes the review in section 11, with every line that does not pass recorded as a finding with a named owner. An owned finding does not defeat the claim; an unrecorded failure does.
A catalogue may conform to this standard with no use case model yet written beneath it. The catalogue and the models beneath it are reviewed separately, by different people, against different standards: a model beneath the catalogue claims conformance to SDD-05, and not to this standard.

## 2  The words, defined once

The rules rely on a small and precise vocabulary. Teams that blur these terms produce blurred catalogues, so the definitions below are normative. Every word defined here is defined here and nowhere else; where a word belongs to another standard of this series, that standard is named and its definition stands.

### 2.1  The core objects

- A sector. A field of public activity — education, health, justice, land — whose services are owed or performed by more than one public body, together with the people and organisations those bodies serve.
- A body. A public organisation that owes or performs services in the sector: a ministry, an agency, an authority, a commission.
- A service. One outcome that one body delivers to one kind of customer, named as an active verb and an object: *License a clinic*, *Register a birth*, *Verify a qualification*. A process that may take days and pass through several hands realises it. It is not a step, a screen, a stored record or a system.
- A catalogue. The organised whole: the sector's boundary, its actors, one row for each service, the gap rows, and the material that goes with them — the catalogue of actors, the vocabulary, the register of rules, and the survey and views generated from the rows. It is the record of the sector's services.
- A row. The catalogue's record of one service, or of one gap. It carries the row header of section 9.1.
- A gap row. A row that records a service the catalogue looked for and did not find: a group of the organising structure that no service realises, or a service a standard or a comparison expects that neither source supplies. It is not a service, it binds to no register row, and it names the person who answers for closing it.
- An instrument. A written legal text that creates duties or powers: an act, a regulation, an order, or a treaty that binds the state.
- An obligation. A duty an instrument places on a body, cited by the instrument and its section.
- An observed service. A service a body is seen to perform, because it publishes it or because the record shows it performed.
- A register, in two senses. First, an authoritative list of records of one kind — of institutions, of qualifications, of practitioners — kept by a named custodian, which other systems refer to and do not copy; the sector's registers are the catalogue's vocabulary (SSC-13). Second, a list the work keeps: the obligations register, the observed-services register, the register of rules. The sense is always plain from the name.
- The organising structure. The structure the catalogue is arranged by and reconciled against — usually a capability map of the sector, divided into areas and groups. It is never a source of rows.
- A model beneath. The use case model of one service chosen to be built, written under SDD-05 as that standard is written, and seeded from the service's row.
- A view. A presentation of the rows grouped or filtered another way — by life event, by customer, by body, by stage. A view is generated from the rows and is never a source of them.
- A life event. An event in the life of a person or a business that leads them to need one or more services: a birth, a move, a licence to operate.
- Direct access. Information obtained from a sector's bodies themselves — by demonstration, interview, database or contract — rather than from what they publish.
- A proof of concept. A small working application built from the row of one service under this organisation's method, to show that the row is enough to specify from.

### 2.2  Actors and stakeholders

The words actor and stakeholder, and the three kinds of actor — primary, supporting and offstage — are SDD-05's (its section 2.2) and mean what they mean there. For a catalogue they are applied through five further words.

- A customer. The person or organisation a service is delivered to, named by the role played: a patient, an employer, an institution, a practitioner. The customer is the service's primary actor.
- A subject. A body standing inside the sector's boundary, whose services the catalogue records. A subject may also be the customer of a service another subject renders it.
- A counterparty. A body with which the sector exchanges information or acts through an agreed interface, but whose own operations the sector does not plan. It stands at the boundary, outside it, and owns no row.
- The owning body. The one subject that owes a service and answers for its delivery.
- A seam. A place where one body of the sector serves another. A seam is recorded as a service the one body renders the other, and never as a second boundary.

### 2.3  The one level of a service

A use case model keeps three levels of goal — summary, user goal and subfunction — and anchors its backbone at the goal completed in one sitting (SDD-05, section 2.3). A catalogue keeps one level. Every service sits at the altitude of a customer's outcome delivered by one owning body: below a capability, which says what the sector must be able to do whoever does it, and above a goal completed in one sitting at one system, which belongs to the model beneath.

![Figure 3](figures/SDD-10/SDD-10_fig03.png)

*Figure 3 — Where a service sits: below a capability, above a goal completed in one sitting.*

The three levels of SDD-05 are not lost. They belong to the models beneath the catalogue, where each is used as that standard says. A catalogue records no level on its rows, because every row stands at the one level this section names.

### 2.4  The same ideas, as they are named elsewhere

Public administration has several names for a service and for the facts recorded about it. This table is the bridge, so that an architect reading another framework, or another country's inventory of services, can tell what they are looking at.

| What you will read elsewhere | What this standard calls it |
|---|---|
| business service, in a national enterprise architecture framework's metamodel: serving a customer, realised by a process, named as an action on a subject | a service |
| service, in the Public Administration Ecosystem Reference Architecture: “a defined performance of a person or organization that meets a customer's needs” | a service |
| public service, in the Core Public Service Vocabulary Application Profile (CPSV-AP) | a service |
| competent authority (CPSV-AP) | the owning body |
| addressee, target users | the customer |
| legal resource, legal basis (CPSV-AP) | the obligation's instrument and section |
| evidence, output, channel (CPSV-AP) | the same three fields of the row |
| status of a public service (CPSV-AP) | the state today, which also names the question that would settle it |
| life event, business event (CPSV-AP) | a view generated from the rows |
| reference use case (GovStack) | a use case model beneath the catalogue, or an example of one |
| business use case model (SDD-05, section 2.4) | not a catalogue: the model of a sector of one body (SSC-1) |
| capability map, capability group | the organising structure, a group of it |
| service portfolio, service inventory | a catalogue, when it keeps to this standard; a national inventory, where one exists, of which the catalogue is the sector's cut |

## 3  The principles

Eight principles underlie every rule that follows. Where a rule seems not to fit the sector in front of you, return to these: they say what the rules are for. The eight principles of SDD-05, section 3, hold as well, read for a catalogue under SSC-4.

SP1  Measure completeness against the sector's law and record, never against the catalogue's own structure.

The only honest test of whether a catalogue has captured everything is to go back to what the sector's bodies are obliged to do and what they are seen doing, and check the rows against it. A catalogue measured against its own groups will always be found complete, because the groups were drawn to fit it.

SP2  Take rows from two sources only.

A service enters the catalogue because an instrument obliges a body to render it, or because a body publishes it or the record shows it performed. Nothing else gives a row: not a capability map, not a standard, not another country's practice, and not a view.

SP3  Let the organising structure organise, and nothing more.

A capability map, or whatever structure the catalogue is arranged by, groups the rows and shows where the catalogue is thin. It is never a source of rows and never the measure of whether the work is finished.

SP4  Say where every row came from.

Every row carries a mark saying what kind of source it rests on, so that a reader can tell a duty in law from a practice observed, and either from a gap, without opening the source.

SP5  A row is complete without its state.

Whether and how a service is delivered today can be settled only by going to the body that delivers it. A row whose mandate, customer, owning body, group and registers are recorded is complete, with its state marked as not established and the question that would settle it named. The catalogue does not wait for direct access.

SP6  Carry no design.

The catalogue records what is owed and done, not how a system will do it. No screen, no field, no data structure and no roadmap decision belongs on a row, and the boundary of a system is drawn in its specification.

SP7  The row is the client's material for what is built beneath it.

For a service chosen to be built, the row is what the specification starts from: the register of requirements is extracted from it by a separate act, and its records seed the first pass of the entity model.

SP8  The models beneath are governed as they are written.

Every use case model built beneath the catalogue is a use case model under SDD-05, with every rule of that standard in force as written. The catalogue governs what stands above the models and nothing inside them.

## 4  Boundary and design scope

*Twenty rules follow, in six groups, in sections 4 to 10; section 7 adds none. Each carries an identifier for use in reviews and in traceability. Where a rule states an obligation that is discharged on an individual row rather than on the catalogue, it says what must be recorded and stops there.*

#### SSC-1 · Apply this standard to a sector whose boundary holds more than one body
Decide which bodies stand inside the sector. Where more than one does, catalogue the sector's services under this standard. Where only one does, the services are the goals of one organisation: model them as a business use case model under SDD-05 (M2), whose boundary is that organisation, and write no catalogue. The test is the boundary and not the size of the sector. A sector of many services owed by one body needs no catalogue; a sector of few services owed by several bodies does, because services cross the seams between them.

#### SSC-2 · Keep one catalogue for each sector, and name one architect who answers for it
Write one catalogue for the sector, and name the one person who answers for it as a whole. Do not keep a separate catalogue, or a separate model, for each body: separate models disagree about who the actors are and what the registers hold, and nothing reconciles them. Every obligation of this standard is discharged once across the catalogue, and the models beneath it take their actors, their vocabulary and their rules from it.

#### SSC-3 · Draw one boundary around the sector, and record each seam as a service
Draw one boundary. Place inside it the bodies of the sector, as subjects, and every service they owe or perform. Place each counterparty at it, outside, and every customer outside it. Where one body of the sector serves another — hands it findings, gives it advice, registers something on its behalf — record that as a service the one renders the other, with the second body as its customer. Never draw a second boundary around a body inside the sector: two boundaries in one catalogue make every service at the seam belong to both bodies or to neither. Name the sector, the bodies inside it and the counterparties at it on the catalogue itself, and state the design scope in SDD-05's terms: a business model, black-box, at the level of a service (M2, M3).

![Figure 4](figures/SDD-10/SDD-10_fig04.png)

*Figure 4 — One boundary around the sector, with a seam between two of its bodies drawn as a service.*

#### SSC-4 · Read the rules of SDD-05 that hold for a catalogue with three substitutions, and restate none of them
Rules M2 to M8, M10 to M15, M18 and M20 to M22 of SDD-05, and its eight principles, apply to the catalogue as they are written, read with three substitutions: a service for a use case, the sector for the system, and the customer for the primary actor. Where a rule so read speaks of a goal completed in one sitting, or of a level of goal, read the one level of section 2.3. Where it refers to a rule of SDD-05 this standard replaces, read the rule of this standard that stands in its place, as the table below gives it. No rule of SDD-05 is restated here, so that none can drift from its source.

| Rule of SDD-05 | For a catalogue |
|---|---|
| M1, one boundary | Replaced by SSC-3, which draws the one boundary around the sector. |
| M2 and M3, the business model and the design scope | Hold, read under SSC-4; SSC-3 states the scope they ask for. |
| M4 to M6, the actors | Hold, read under SSC-4; SSC-5 says who the actors are. |
| M7 and M8, goals first, and the name | Hold, read under SSC-4. |
| M9, the three tests of granularity | Does not reach the catalogue, which is not a use case model; SSC-7 carries the one test of a service. Every model beneath the catalogue meets M9 as written. |
| M10, no functional decomposition | Holds, read under SSC-4, the unit being the service. |
| M11, flows before relationships | Holds, read under SSC-4. |
| M12 and M13, the packages and the survey | Hold, read under SSC-4; SSC-10 says what the packages are drawn from, and SSC-15 that the survey is generated. |
| M14 and M15, completeness and the trace | Hold, read under SSC-4; SSC-11 says what completeness is measured against. |
| M16, the binding to the register of requirements | Does not reach the catalogue; SSC-12 carries the catalogue's own binding. Every model beneath the catalogue meets M16 as written. |
| M17, one entity model | Replaced by SSC-13, the vocabulary. |
| M18, one register of business rules | Holds, read under SSC-4; SSC-14 names the register. |
| M19, versioned text | Replaced by SSC-15, the record. |
| M20 to M22, the change made first, the significant few written out first, one glossary | Hold, read under SSC-4. |
| P1 to P8, the principles | Hold, read under SSC-4. P3 anchors the catalogue at the one level of section 2.3, where the whole set of services is the backbone. |

## 5  Actors

The actors of a catalogue are its customers, the bodies inside it where one serves another, the counterparties at its boundary, and the systems and clocks its services involve. SDD-05 already says how actors are identified, classified and kept (M4 to M6, read under SSC-4). The one rule here says who they are for a sector.

#### SSC-5 · Take the actors from the sector's customers, and from its bodies where one serves another
The primary actors of the catalogue are the sector's customers — the people and organisations its services are delivered to — and the bodies inside the boundary wherever one is the customer of a service another renders. Name each by the role it plays (M4), classify each as primary, supporting or offstage for each service it takes part in (M5), and include the systems, devices and clocks that start a service or that a service calls on (M6). Counterparties are actors outside the boundary: record each with its kind, and give none of them a row. Keep the actors in one catalogue of actors for the whole sector, from which every model beneath takes its own.

## 6  Identifying services and setting their size

A service is found in the sector's material and sized by one test. The four rules of this section say what a service is, how large it may be, where it may come from, and how its source is marked.

#### SSC-6 · Make the service the unit: one customer's outcome, delivered by one owning body
Every row other than a gap row records one service: an outcome a customer receives from one owning body, at the level section 2.3 describes. Derive services from what customers need the sector's bodies to deliver (M7), and name each as an active verb and an object in the words the sector uses (M8). A service is not a capability, which says what the sector must be able to do whoever does it, and not a goal completed in one sitting at one system, which is a use case of the model beneath.

#### SSC-7 · Size a service by one test, and do not decompose the catalogue
A service passes one test, and must pass all four of its parts: one customer, one owning body, one output, and one obligation or one observed practice. A candidate with two customers is two services. A candidate owed by two bodies is a service of the one that delivers the outcome, and a seam service rendered to it by the other (SSC-3). A candidate with two outputs is two services. Do not break the catalogue into steps, records or fields, and do not raise it to goals that return no result to a named customer: a single model of the sector does both, which is why the catalogue exists. The test is the catalogue's own. Each use case model beneath the catalogue is sized by the three tests of SDD-05 (M9), as that rule is written.

![Figure 5](figures/SDD-10/SDD-10_fig05.png)

*Figure 5 — The one test of a service, set beside the three tests of a sitting.*

#### SSC-8 · Take rows from two sources only
A service enters the catalogue from one of two sources: an obligation stated in an instrument that is held or has been retrieved, or a service a body publishes or the record shows it performing. Nothing else supplies a service. The organising structure organises the rows (SSC-10); a standard supplies the fields a row carries and the targets a service is checked against; a comparison with another sector or another country tests the catalogue's completeness; a view presents the rows. None of these is a source of a service, and a service any of them suggests enters the catalogue only as a gap row until an obligation or an observed practice supplies it. An instrument's list of functions is not a list of services: a power conferred on a body, or a function it performs on others, is recorded as a rule that governs a service (SSC-14), and gives a row only where it names an outcome delivered to a customer.

![Figure 6](figures/SDD-10/SDD-10_fig06.png)

*Figure 6 — The order of precedence: what each kind of source may do in the catalogue.*

#### SSC-9 · Mark every row with the kind of source it rests on
Every row carries one of four source marks, and the catalogue uses no other.

- obligation — the service rests on a duty an instrument places on its owning body, cited by the instrument and its section and bound to the row of the obligations register that quotes it.
- observed — the service rests on a practice the owning body publishes or the record shows it performing, bound to the row of the observed-services register that records it.
- derived — a gap row raised because a standard or a comparison expects a service that neither source supplies. It names the standard or comparison it came from and the group of the organising structure it stands against.
- searched — a gap row raised by the outward reconciliation of SSC-10: a group of the organising structure that no service realises, against which the sector's material was searched and nothing found. It records what was searched.
A service carries obligation or observed and nothing else; where it rests on both an obligation and an observed practice, it is marked obligation and bound to both registers. A gap row carries derived or searched, binds to no register row, is counted apart from the services, and names the person who answers for closing it — by retrieving the instrument that would supply it, by observing the practice, or by recording that the sector does not render it.

## 7  Relationships

Relationships between services are an optimisation for clarity and reuse, as they are between use cases, and they are rarer. A service is an outcome for a customer and not a piece of behaviour to be factored, so most rows carry no relationship at all. Where one service genuinely includes another, or genuinely extends another at a named point under a named condition, record it under M11 of SDD-05, read under SSC-4, with the point named on the row. This section adds no rule.

## 8  Structure, completeness and traceability

### 8.1  Packaging and the survey

The catalogue is packaged by its organising structure and indexed by its survey. The survey is M13's, read under SSC-4: one index listing, for every row, its identifier, its name, its customer, a one-line description, its priority, its status and the register rows it realises, generated from the rows (SSC-15). What the packages are drawn from is the subject of the one rule here.

#### SSC-10 · Organise the catalogue by a declared structure, reconcile the structure outward, and never take a row from it
Declare the structure the catalogue is organised by — a capability map of the sector, or whatever structure the sector's architecture uses — and name where it came from, as the requirements catalogue standard asks of a register's ordering (SDD-02, RQR-5). Record on every row the one group of that structure the service realises, and package the rows by the structure's areas (M12). Reconcile the structure outward against the catalogue: every group of it is realised by at least one service, or is recorded as a gap row against it with the name of the person who answers for it. Never take a row from the structure. A structure drawn for every sector of a kind expects services in each of its groups; whether this sector's bodies owe or perform them is a question for the two sources of SSC-8, and a catalogue derived from its own structure is complete by construction and describes services no body owes.

### 8.2  Completeness and traceability

![Figure 7](figures/SDD-10/SDD-10_fig07.png)

*Figure 7 — Completeness is checked outward and inward.*

#### SSC-11 · Measure completeness against the sector's law and record, outward and inward
The catalogue is complete when two conditions hold. Outward, every group of the organising structure is realised by a service or recorded as a gap row (SSC-10). Inward, every row of the obligations register and of the observed-services register is disposed of — realised by a service, cited by one as a rule that governs it, or recorded as not a service with the reason — and every service rests on at least one row of either register (SSC-12). The inward condition is the measure; the outward one shows where the measure has not yet been applied. Completeness is never measured against the catalogue's own structure, against a view, or against a list of life events: each of those will agree with the catalogue, because each was drawn from it or for it. The conditions M14 of SDD-05 adds on actors and results, read under SSC-4, hold as well.

#### SSC-12 · Bind every service, by identifier and in both directions, to the obligations register and the observed-services register
Keep the sector's obligations and its observed services in two registers, each published as one named list, in one place, in a form a program reads — the form SDD-02 describes for a register of requirements in RQR-27, cited here for its form and not for its content. Record on every service the identifiers of the register rows it realises, by those identifiers and by nothing else. From the other side, every row of either register is realised by a service, cited by one as a rule that governs it (SSC-14), or recorded in its register as not a service, with the reason. A service that realises no register row is either a service no body owes or a register row nobody has written; a register row disposed of in none of the three ways is either out of scope or a service nobody has catalogued. Both are findings. The binding is carried on the rows, not in a matrix beside them, so that a program can check it. It does not replace the register of requirements of anything built from a row: that register is extracted from the row, when its service is chosen to be built, by the separate act SDD-02 describes (SSC-19).

### 8.3  The vocabulary the catalogue uses

#### SSC-13 · Name the sector's registers as the catalogue's vocabulary, and keep one vocabulary for everything beneath it
The catalogue's vocabulary is the sector's registers — the authoritative lists of records of one kind that the sector's bodies keep or are to keep. Name each register once, with one line saying what it holds, until it is defined under the entity model standard (SDD-03) when a service that reads or changes it is specified. Record on every row the registers the service reads and the registers it changes, by those names and no others; a record outside the vocabulary is a finding. Keep one catalogue of actors (SSC-5), one vocabulary and one glossary (M22, read under SSC-4) for the whole catalogue, and let every model beneath take its words from them.

### 8.4  The rules the catalogue depends on

#### SSC-14 · Keep the obligations register as the catalogue's register of rules, and name separately what a row realises and what governs it
The register of rules that M18 of SDD-05 asks for is, for a catalogue, the obligations register: every duty, power and prohibition the sector's instruments state, each written once, with its instrument, its section and its words. A row names separately the register rows it realises — the duty its service discharges — and the register rows that govern it — the criteria, powers, prohibitions and procedures the service is carried out under — as SDD-05 section 9.1 keeps linked requirements and business rules apart. One register row may be realised by one service and govern another. For a service chosen to be built, the rules that govern it are the seed of the register of business rules of its model beneath (SSC-19).

## 9  The catalogue record

![Figure 8](figures/SDD-10/SDD-10_fig08.png)

*Figure 8 — The rows are the only part written by hand. The survey, the packages, every view and the checks are produced from them, which is what stops them disagreeing with the rows.*

#### SSC-15 · Hold the catalogue as versioned text, one row for each service and gap, and generate the survey and every view
Hold the catalogue as text under version control, in a place where version control exists, beside the two registers it binds to: one row for each service and for each gap. Generate the survey, the packages and every view — by life event, by customer, by body, by stage — from the rows, and keep none of them by hand, so that none can come to disagree with the rows. The completeness and traceability conditions of SSC-10 to SSC-12 then become checkable by a program instead of by inspection. When a service must change, change its row before the system that realises it, as M20 of SDD-05 requires, read under SSC-4.

#### SSC-16 · Carry the row header on every row, each value stated once
Every row carries the fields of section 9.1, and the survey and every check are generated from them. State each value once, on the row. Where a field takes its values from a closed list — the source marks, the states, the stages, the groups of the structure, the registers, the systems — declare the list on the catalogue with where it came from, and use no value outside it. A field with nothing to record carries its list's value for an absence — none, not established, not placed — and never an empty cell.

### 9.1  The row header

These are the fields every row carries. The survey is generated from them, and the catalogue's completeness and traceability checks run against them. A gap row carries its identifier; a name for what is missing; in its description, what was searched, or which standard or comparison expects the service, and the person who answers for closing the gap; its group; and its source mark. Its other fields read none.

| Field | What to record | Rule |
|---|---|---|
| Identifier | The stable reference by which the catalogue knows the row, allocated once and never reused. Its form is declared on the catalogue. | SSC-16 |
| Name | An active verb and an object, from the customer's viewpoint, in the sector's words. | SSC-6 |
| Description | One line stating the outcome the name stands for. | SSC-4 (M13) |
| Customer | The one role the service is delivered to, from the catalogue of actors. | SSC-5, SSC-7 |
| Owning body | The one subject that owes and delivers the service. | SSC-3, SSC-7 |
| Other parties | Every other party the service involves, each with its kind: supporting, offstage, or counterparty. | SSC-5 |
| Obligation | The identifiers of the register rows the service realises: of the obligations register, with the instrument and section, or of the observed-services register. | SSC-8, SSC-12 |
| Source mark | obligation, observed, derived or searched. | SSC-9 |
| Group | The one group of the organising structure the service realises; its area is the row's package. | SSC-10 |
| Registers read; registers changed | Two lists, by the names of the vocabulary. | SSC-13 |
| Evidence, output and channel | What the customer presents; what the service produces; the ways it is delivered. | SSC-7, SSC-19 |
| State today | How the service is delivered today, from the catalogue's declared list of states; or not established, with the question that would settle it. | SSC-17 |
| Realising system | The system that realises the service, by the identifier the sector's architecture gives it, or none. | SSC-16 |
| Stage | The stage of the sector's roadmap in which the service is to be delivered digitally, or not placed. | SSC-18 |
| Linked rules | The identifiers of the rows of the obligations register that govern the service. | SSC-14 |
| Relationships | Include, extend or generalisation to another service, with the point named; usually none. | SSC-4 (M11) |
| Life events | The events under which the life-event view groups the service, where the catalogue keeps that view. | SSC-15 |
| Priority | Set by business value, risk and architectural significance, on one scale for the whole catalogue. | SSC-4 (M13, M21) |
| Status and format | Draft, reviewed or baselined; and the format, which for a service is the row alone, or the row with a use case model beneath it. | SSC-4 (M21), SSC-19 |

This header is the catalogue's record of the service. It is written once for each row and it is read by machine: the survey is generated from it, and the catalogue's checks run against it. A value that appears both here and in prose about the service will come to disagree with itself. State it here only.

#### SSC-17 · Settle the state today only by direct access, count a row complete without it, and carry no design
Record the state of a service today only from direct access to the body that delivers it — a demonstration, an interview, a database, a contract. What a body publishes shows that it offers a service; it does not show how the service is delivered. Until direct access settles it, record the state as not established and name the question that would settle it. Such a row is complete, because its mandate, its customer, its owning body, its group and its registers do not depend on its state, and a first complete edition of a catalogue may carry no settled state at all. Carry no design or roadmap matter on a row: how an identifier is structured, how a register's integrity is controlled, where data is hosted, what a service costs and who operates a platform are questions the sector's architecture and roadmap answer.

![Figure 9](figures/SDD-10/SDD-10_fig09.png)

*Figure 9 — Which parts of a row need direct access to the sector's bodies.*

#### SSC-18 · Place no service in a stage before the register it reads
Where the sector has a roadmap, record for each service the stage in which it is to be delivered digitally, and place no service in a stage earlier than the stage in which a register it reads is to be established. A service that reads a register no stage yet holds is not placed, and stays not placed until that register is. Where the sector has no roadmap, the field reads not placed on every row and the rule is met.

## 10  From a row to what is built

The catalogue is not the end of the work for the services chosen to be built: it is where their specification starts. This section says what the row of a chosen service must carry, what is written beneath it, and what stays out of a specification altogether.

![Figure 10](figures/SDD-10/SDD-10_fig10.png)

*Figure 10 — From the row of a chosen service to a proof of concept.*

#### SSC-19 · Beneath the catalogue, write one use case model for each service to be built, from its row
For each service chosen to be built, write one use case model under SDD-05, as that standard is written, seeded from the service's row. The row is that model's client's material: the register of requirements is extracted from it by the separate act SDD-02 describes, and the first pass of the entity model is written from it before any goal is named. When a service is chosen, write beside its row a companion that carries, so that the row header stays the same for every row:

- the obligation's words with its section, quoted, or the published practice;
- every party, with its kind;
- the evidence, the output and the channel — the seed of the register of requirements;
- the records the service reads and changes, by name, mapped to the sector's registers — the seed of the first pass of the entity model;
- the rules the instrument states — the seed of the register of business rules;
- what the service must not do: a counterparty's operation, and anything a national shared service provides;
- the contracts of the sector's reference architecture it uses, where the sector has one;
- the settings it leaves to the jurisdiction, named and without values.
Neither the row nor its companion carries a screen, a field or any design. The boundary of the system that realises the service is drawn in its specification under M1 of SDD-05, not in the catalogue, and M9 and M16 apply to that model as they are written.

### 10.1  Slices belong to the models beneath

A catalogue is not cut into slices. Slices are cut from the use cases of a model beneath the catalogue, as SDD-05 section 10 describes, and delivered under it. This standard adds nothing to that.

### 10.2  Order by value and risk, and build in increments

Which services are built first, and in what order, is decided across the catalogue by business value, risk and architectural significance: M21 of SDD-05, read under SSC-4. The decision is recorded on the rows as their priority and their format, so that the catalogue states which services have models beneath them, which are next, and which are not yet planned.

### 10.3  How much of the catalogue is detailed, and when

A first complete edition of the catalogue names every service the two sources supply and every gap the reconciliation finds, and may carry no settled state for any of them (SSC-17). Each later edition settles states as direct access is obtained, turns gap rows into services as instruments are retrieved and practices observed, and adds the companion of SSC-19 to each service chosen to be built. A service is written out in full only when its own use case model exists beneath the catalogue; the catalogue itself is never written out further than its rows.

#### SSC-20 · Let a row resting on observed practice stand in the catalogue, and keep it out of a specification
A service marked observed stands in the catalogue: the catalogue records what the sector's bodies are seen to do as well as what they owe. It is not specified from until an obligation is found for it. A specification rests on a mandate, and an observed practice is evidence that something is done, not that it must be; building from it claims an authority without a source (SDD-01, section 14, rule 17).

## 11  The review

Run this before a catalogue is baselined, and before any service is specified from it. The catalogue's architect runs it with the architecture authority. A catalogue passes only when every applicable line is satisfied. An unsatisfied line is a finding with a named owner, not an exception to be waved through.

| Rules | Checkpoint | Passed |
|---|---|---|
| SSC-1–SSC-3 | The sector is named and holds more than one body; one architect answers for one catalogue; exactly one boundary is drawn, with the bodies inside it as subjects and the counterparties at it; every seam is a service one body renders another; the design scope is stated. | ☐ |
| SSC-4 | For each rule of SDD-05 that SSC-4 reads for a catalogue, the matching line of SDD-05's review passes, read with the three substitutions. | ☐ |
| SSC-5 | Actors are roles — the sector's customers, and its bodies where one serves another — each classified as primary, supporting or offstage; systems and clocks are included; counterparties own no row; one catalogue of actors serves the whole catalogue. | ☐ |
| SSC-6–SSC-7 | Every service is one customer's outcome delivered by one owning body, named as an active verb and an object, and passes the one test: one customer, one owning body, one output, one obligation or one observed practice. Nothing is decomposed into steps, records or fields. | ☐ |
| SSC-8–SSC-9 | Every service rests on an obligation or an observed practice and on nothing else; every row carries one of the four source marks; every gap row is marked derived or searched and names the person who answers for it. | ☐ |
| SSC-10 | The organising structure is declared with where it came from; every row names its group; every group is realised by a service or recorded as a gap row; no row was taken from the structure. | ☐ |
| SSC-11 | Completeness was measured against the two registers, outward and inward, and not against the structure, a view or a list of life events. | ☐ |
| SSC-12 | Every service binds by identifier to at least one row of the two registers; every register row is realised, cited as a rule, or recorded as not a service with the reason; both registers are published as named lists a program reads. | ☐ |
| SSC-13 | Every register a row reads or changes is named in the vocabulary with its one line; one catalogue of actors, one vocabulary and one glossary serve the whole catalogue. | ☐ |
| SSC-14 | The obligations register is the register of rules; every row names separately what it realises and what governs it; every rule is cited by at least one service. | ☐ |
| SSC-15 | The catalogue is held as versioned text, one row for each service and gap; the survey, the packages and every view are generated from the rows. | ☐ |
| SSC-16 | Every row carries the row header, each value once; every closed list is declared with where it came from, and no value falls outside its list. | ☐ |
| SSC-17 | Every state is from the declared list; every state not established names the question that would settle it; no row carries design or roadmap matter. | ☐ |
| SSC-18 | No service is placed in a stage before the register it reads. | ☐ |
| SSC-19–SSC-20 | Every service chosen to be built has a use case model beneath the catalogue under SDD-05, or is marked as not yet written; its companion carries what SSC-19 lists; no service resting only on observed practice has been specified. | ☐ |

What this review does not do. Every line above tests a structural property — that something is named, marked, bound, declared or generated. None of them asks whether a row's obligation truly is its service's mandate, whether a recorded state is the state the service is in, or whether the sector's material has been read in full. Section 14 states the limit that leaves.

## 12  The ways catalogues go wrong

These are the failures that recur, with the rule that corrects each one. They are the failures found by reading across the catalogue, by or for the person accountable for it. The failures found inside the use case model of one service are SDD-05's to name.

| The failure | How it shows | The rule that corrects it |
|---|---|---|
| One flat model of the sector | A use case model drawn around several bodies either breaks every service into operations, or rises to summary goals that return no result to a named customer. | Write a catalogue with models beneath it, and size each service by the one test (SSC-2, SSC-7, SSC-19). |
| A family of models that disagree | One model for each body, each with its own actors and its own names for the registers, and no way to reconcile them. | One catalogue, one catalogue of actors, one vocabulary (SSC-2, SSC-5, SSC-13). |
| A second boundary at a seam | A body inside the sector drawn with a boundary of its own, so that a service between two bodies belongs to both or to neither. | One boundary; the seam is a service one body renders another (SSC-3). |
| A catalogue derived from its own structure | Every group of the capability map has a row, and the rows describe services no body of the sector owes. | Rows from two sources only; the structure organises and reconciles (SSC-8, SSC-10, SSC-11). |
| A view mistaken for the catalogue | A list of life events kept by hand and treated as the list of services, which nothing says is finished and which invites services nobody owes. | Generate every view from the rows; measure completeness against the law and the record (SSC-11, SSC-15). |
| Powers mistaken for services | An instrument's list of functions copied into rows, so that a power to revoke or to oversee appears as a service to a customer. | A row is an outcome delivered to a customer; a power is a rule that governs one (SSC-6, SSC-8, SSC-14). |
| Two customers in one row | A service whose customer reads "institutions and awarding bodies", or whose output reads "a licence and a certificate". | Apply the one test, and split the row (SSC-7). |
| A gap filled locally | A service written in because the structure or another country expects it, with nothing in the sector's material behind it. | Record a gap row, marked, with a person against it (SSC-9, SSC-10). |
| A catalogue that waits for its state | No row is written until every body has been visited, and the catalogue is never finished. | A row is complete without its state; name the question and continue (SSC-17). |
| Design carried in a row | Fields, screens, identifier structures or hosting decisions written on the rows. | Carry no design; the boundary of a system is drawn in its specification (SSC-17, SSC-19). |
| A row specified directly | A system built from a row without its register of requirements extracted, or from a row resting only on observed practice. | Extract the register of requirements by a separate act; keep an observed row out of a specification (SSC-19, SSC-20). |
| A value stated twice | The same fact on the row and in a description of the service, and the two differ. | State each value once, on the row (SSC-16). |
| Traceability kept beside the catalogue | A matrix of services against obligations maintained apart from the rows, and no longer matching them. | Carry the binding on the rows as identifiers, and generate the survey (SSC-12, SSC-15). |

## 13  A worked catalogue

*This is a simulated case for Progressa, a fictional country; every institution, name, date and figure in it is invented. In this copy of the standard it replaces the worked catalogue of the edition of record, which was drawn from a real sector, so that the example rests on nothing outside the courses it is published with.*

The example is part of the catalogue of the higher-education sector of Progressa: the services that article 4 of Progressa's Higher Education Regulations, 2025, obliges PHEQA, the Progressa Higher Education Quality Authority, to render; the services that three further articles oblige the ministry of education, MoEYS, to render; one service PHEQA publishes that no article states; and one gap. It is used here because article 4 lists twelve functions of which only some are services, and because the sector's boundary holds three bodies — PHEQA, MoEYS and PDCA, the Progressa Digital Credentials Authority — so that a service one of them renders another appears within the first lines of the Regulations. Between them the rows exercise most of the rules above: rows resting on obligations, a row resting on observed practice, two seams, a row split by the one test, rows whose state is settled and rows whose state is not established, and a gap row.

The rows are drawn from four sources the sector's architect keeps: the obligations register, which quotes each lettered function of article 4, and articles 11, 14, 22 and 26, as one row each, OB-001 to OB-016, and which the Registrar of PHEQA accepted on 2 October 2026; the register of observed services, rows OS-01 to OS-04, written from PHEQA's and MoEYS's published pages; the sector's capability map, whose areas and groups are the organising structure; and the register of questions that only direct access settles. Where the example reads the Regulations, or raises a question of its own, it says so.

Article 4 opens "PHEQA is responsible for —" and lists its functions from (a) to (l). The table reads each of them, in brief, against SSC-6 and SSC-8: whether it names an outcome delivered to a customer, and so gives a row, or is a power, an internal function or a duty of governance, and so gives a rule that governs a row, or no row at all. The words of each function are quoted in full in the obligations register, under the identifier given.

| Art. 4 | The function, in brief | Register row | What the catalogue makes of it |
|---|---|---|---|
| (a) | registering private higher-education institutions, and licensing them provisionally and in full | OB-001 | Two services, S-01 and S-02: the paragraph names two outputs, an entry in the register and a licence (SSC-7) |
| (b) | recommending to the minister a decision on each application for a licence | OB-002 | Service S-03, a seam |
| (c) | inspecting an institution before it recommends | OB-003 | A power; a rule that governs S-02 and S-03 |
| (d) | suspending and cancelling licences on the minister's decision | OB-004 | A power; a rule that governs S-02 |
| (e) | setting the standards new institutions are judged against, and revising them | OB-005 | A rule that governs S-01 and S-02 |
| (f) | hearing an institution's appeal against a decision of PHEQA | OB-006 | Service S-04 |
| (g) | issuing a schedule of fees | OB-007 | A rule that governs S-02 |
| (h) | keeping the register of institutions, open to the public | OB-008 | A duty to keep registers; it names what the register of institutions holds (SSC-13), and gives no row |
| (i) | writing into the register a change of an institution's name that the minister has approved | OB-009 | Service S-05, a seam |
| (j) | collaborating with the quality authorities of other countries | OB-010 | An internal function; no row |
| (k) | conducting research on higher education | OB-011 | An internal function; no row |
| (l) | performing such other functions as the Regulations confer | OB-012 | No row: it names no function |

Four further rows of the register quote the articles that bind MoEYS. Article 11, the minister decides a licence on PHEQA's recommendation (OB-013), is a power and a rule that governs S-02 and S-03. Article 14(2), the minister publishes the list of registered institutions in the Gazette each year (OB-014), gives service S-08. Article 22, a person aggrieved by a decision of PHEQA may ask the minister to review it (OB-015), gives service S-09. Article 26(1), a change of an institution's name needs the minister's approval (OB-016), gives service S-07.

![Figure 11 — The worked catalogue: article 4 of one instrument, read function by function.](figures/SDD-10/SDD-10_fig11.png)

*Figure 11 — The worked catalogue: article 4 of one instrument, read function by function. Four of the twelve functions give five services; four govern a service; four give no row. One service comes from PHEQA's published services, and one group of the capability map is a gap.*

### 13.1  The actor catalogue

Every actor is a role, and each is classified (SSC-5). The three bodies of the sector stand inside the boundary as subjects. PDGA, the Progressa Digital Government Authority, which operates Linkup, stands at the boundary as a counterparty; none of these rows is its.

| Actor | Kind | Inside the boundary? | The service it receives, or the part it plays |
|---|---|---|---|
| Private higher-education institution | Primary | No — a customer | Its entry in the register (S-01); its licence (S-02); its appeal heard (S-04); a certified extract of the register (S-06); the approval of a new name (S-07) |
| The minister | Primary | Yes — MoEYS, a subject | A recommendation on each licence (S-03); an approved new name written into the register (S-05) |
| The public | Primary | No — a customer | The list of registered institutions (S-08) |
| A person aggrieved by a decision of PHEQA | Primary | No — a customer | The review of the decision (S-09) |
| PNIA's sign-in | Supporting | No — a system | Tells a service who a person is |
| The Payments block | Supporting | No — a system | Settles the application fee of S-02 |
| PHEQA | Owning body of S-01 to S-06 | Yes — a subject | Owes six services |
| MoEYS | Owning body of S-07 to S-09 | Yes — a subject | Owes three services |
| PDCA | Owns no row | Yes — a subject | The gap row S-10 stands against the group its service would realise |

### 13.2  The survey, at row-header precision

The survey is generated from the rows (SSC-15). The catalogue declares its closed lists (SSC-16): the four source marks of SSC-9; as its states, the list the sector's profile proposes — online, on paper, by letter, not offered, and not established with its question; as its stages, the three stages of the sector's roadmap, of which the first establishes the register of institutions; as its organising structure, the groups of the sector's capability map; and as its vocabulary, the three registers the sector's architecture names, of institutions, of learners and of credentials. The identifiers S-01 to S-10 are this example's own; the catalogue of record declares its form. The survey is shown in two parts, for the width of the page.

| Row | Name | Customer | Obligation | Mark |
|---|---|---|---|---|
| S-01 | Register an institution | Private higher-education institution | OB-001, art. 4(a) | obligation |
| S-02 | License an institution | Private higher-education institution | OB-001, art. 4(a); OS-01 | obligation |
| S-03 | Recommend a licence decision to the minister | The minister | OB-002, art. 4(b) | obligation |
| S-04 | Hear an institution's appeal | Private higher-education institution | OB-006, art. 4(f); OS-02 | obligation |
| S-05 | Write an approved new name into the register | The minister | OB-009, art. 4(i) | obligation |
| S-06 | Issue a certified extract of the register | Private higher-education institution | OS-04 | observed |
| S-07 | Approve a change of an institution's name | Private higher-education institution | OB-016, art. 26(1) | obligation |
| S-08 | Publish the list of registered institutions | The public | OB-014, art. 14(2); OS-03 | obligation |
| S-09 | Review a decision of PHEQA | A person aggrieved by a decision of PHEQA | OB-015, art. 22 | obligation |
| S-10 | No service of credential issuance | none | none | searched |

The same rows, continued: the group each realises, the registers it reads and changes, and its state today.

| Row | Group | Registers | State today |
|---|---|---|---|
| S-01 | 1.1 Institution register & licensing | changes Institutions | on paper: the register is a spreadsheet at PHEQA's registration desk |
| S-02 | 1.1 Institution register & licensing | reads Institutions; changes Institutions | on paper: the applicant brings printed documents to the desk |
| S-03 | 1.2 Quality assurance & inspection | reads Institutions | not established: how does a recommendation reach the minister today, and on what system? |
| S-04 | 2.1 Appeals & reviews | reads Institutions | by letter |
| S-05 | 1.1 Institution register & licensing | changes Institutions | not established: who writes the new name today, and when? |
| S-06 | 1.1 Institution register & licensing | reads Institutions | not established: is an extract issued on request at the desk, or by post? |
| S-07 | 2.2 Changes to an institution | reads Institutions | by letter, to both bodies |
| S-08 | 3.1 Publication & open data | reads Institutions | on paper: the ministry types the list from its own forms |
| S-09 | 2.1 Appeals & reviews | reads Institutions | by letter |
| S-10 | 4.1 Credential issuance & verification | none | none |

The states settled on the rows were settled by direct access: an interview with the head of PHEQA's registration desk on 14 September 2026, and one with the Director of Higher Education at MoEYS on 16 September 2026. One row, S-02, written out at the full precision of the row header:

| Field | S-02 |
|---|---|
| Identifier | S-02 |
| Name | License an institution |
| Description | PHEQA grants a private higher-education institution a provisional licence, and later a full one, on the minister's decision. |
| Customer | Private higher-education institution |
| Owning body | PHEQA |
| Other parties | The minister, supporting: decides each licence (OB-013); PNIA's sign-in, supporting; the Payments block, supporting |
| Obligation | OB-001: article 4(a) of the Regulations, "registering private higher-education institutions, and licensing them provisionally and in full"; and OS-01, the application PHEQA's published page tells an applicant to bring to the registration desk |
| Source mark | obligation |
| Group | 1.1 Institution register & licensing, in the area 1 Institutions |
| Registers read; registers changed | reads Institutions; changes Institutions |
| Evidence, output and channel | Evidence: the particulars article 6 lists, and the application fee of the schedule article 4(g) gives. Output: a licence, provisional or full. Channel: PHEQA's self-service, which article 6 names; today the registration desk |
| State today | on paper: the applicant brings printed documents to the desk |
| Realising system | none: PHEQA's application is to realise it |
| Stage | 1, the stage that establishes the register of institutions (SSC-18) |
| Linked rules | OB-003, art. 4(c): inspection before a recommendation; OB-004, art. 4(d): suspension and cancellation; OB-005, art. 4(e): the standards for new institutions; OB-007, art. 4(g): the schedule of fees; OB-013, art. 11: the minister decides |
| Relationships | none |
| Life events | none recorded: this example keeps no life-event view |
| Priority | first: set across the catalogue by the Director of Higher Education, with the Registrar of PHEQA (SSC-4, M21) |
| Status and format | reviewed; the row with a use case model beneath it, PHEQA's application (SSC-19) |

### 13.3  Reading the catalogue against the rules

The boundary holds three bodies, so the standard applies (SSC-1). PHEQA, MoEYS and PDCA are subjects; PDGA at the boundary owns none of these rows (SSC-3). Article 4 gives twelve functions and five services: the table shows each function read against SSC-6 and SSC-8, and the eight that are powers, internal functions or duties of governance become rules that govern a service, or no row, rather than services — the failure section 12 calls powers mistaken for services, avoided. Paragraph (a) names two outputs in one sentence, an entry in the register and a licence, and the one test splits it into two rows, S-01 and S-02, both bound to the same register row (SSC-7, SSC-12). S-03 and S-05 are seams: PHEQA renders the minister a recommendation, and writes into its register a name the minister approved, so each is a service one body of the sector renders another, recorded as a row and not drawn as a second boundary (SSC-3). S-06 rests on PHEQA's published page and on no article; it is marked observed, it stands in the catalogue, and until an obligation is found for it it is not specified from (SSC-9, SSC-20). S-10 is the reconciliation at work: the capability map expects a service that issues a learner's credential, PDCA is the body that will issue it, and neither the Regulations nor any published page supply one, because PDCA's founding instrument has not been retrieved. The group is recorded as a gap row marked searched, with the sector's architect named on the catalogue of record as the person who answers for retrieving the instrument, and it is not filled with a service nobody yet owes (SSC-9, SSC-10).

Every row is complete (SSC-17). Five rows carry a state settled by direct access; four carry not established, each with the question that would settle it, because what a body publishes shows that a service is offered and not how it is delivered. S-02 is placed in the first stage, the stage that establishes the register it reads; no row is placed before that register (SSC-18).

Two things in this example are worth arguing about rather than admiring, and they are left in for that reason. First, article 4 is not the whole of the Regulations. Article 11 gives the minister the decision of a provisional and of a full licence, on PHEQA's recommendation. Read from the whole of the Regulations, S-02 carries a second seam — the minister's decision crossing back to PHEQA — and the question whether the owning body of the licence is PHEQA, which grants it under article 4(a), or MoEYS, whose minister decides it. The catalogue of record reads the whole of the Regulations and answers that question under SSC-7; this example records the question and does not decide it. Second, whether the certified extract S-06 is a service of its own or only an output of the register's being open to the public under article 4(h) is not established. In a catalogue of record that is a question on the row, and the line of the review on what a row realises (SSC-12) records it until it is answered.

## 14  The questions this standard does not answer

A standard that hides what it cannot yet say is worse than one that names it. Three conditions change how this standard applies, and three things are unsettled.

Where the instruments of a sector enumerate its services, the law alone may supply every row, and the second source of SSC-8 adds nothing new; the standard still applies, and the observed-services register then checks the law rather than extending it. Where the boundary holds one body, the standard does not apply (SSC-1). Where a national inventory of public services already exists, the catalogue becomes that inventory's cut for the sector; how the two are kept from disagreeing is a question this standard does not answer.

### Whether what is recorded is true

The review in section 11 is a check of one kind only: every line in it is a structural property that a reader, and in time a program, can confirm by looking. Whether a row's obligation truly is the service's mandate, whether two rows with different names are one service, whether a state recorded from an interview is the state the service is in, whether a function was rightly read as a rule and not a service — none of these is asked by any line of section 11, and every one of them decides whether a catalogue is any good. A catalogue that passes the review has been shown to be well formed, and nothing more. A reviewer should read the result that way.

### When a catalogue is finished

No test says when the sector's material has been read in full. SSC-11 measures the catalogue against the obligations register and the observed-services register, and those registers are only as complete as the instruments held and the record read: an instrument not yet retrieved leaves the catalogue emptiest where the sector may be largest, and nothing inside the catalogue shows it. The organising structure cannot supply the test, because a catalogue measured against its own structure is complete by construction (SSC-10). What this standard offers is that every question it asks has an answer or carries a written reason for having none, and that every gap row names who answers for it.

### How many gap rows are too many

A catalogue has one level, so the question SDD-05 asks of a thin backbone does not arise. The nearest question is how many gap rows a first complete edition may carry and still be called complete. No published study establishes a threshold, and this standard does not offer one. A catalogue with many gap rows should be argued about — which instruments are missing, which practices were not observed — rather than passed or failed on the count.

## 15  Where these rules come from

This standard draws its rules from a method paper of 24 September 2026 on how to model the services of a sector, written for the education sector of one country — the sector section 13 reads — and from the standards of this series it cites. The paper recommended a profile of SDD-05; the ruling of the same day made its method a standard of this series instead, so that the use case model standard's rules stand as written for every model beneath a catalogue (rulings/2026-09-24-the-sector-services-catalogue.yaml). Every rule here rests on a claim of that paper that holds for any sector; the claims that hold only for the country it was written for appear in section 13 and nowhere else. The record of the round that wrote this draft lists, rule by rule, the claims each one rests on: _reports/REPORT_WRITE_the_sector_services_standard_2026-09-24.md.

- The requirements catalogue standard, SDD-02: its sections 1.3, 4.1, 4.3 and 4.4, and its rules RQR-5 and RQR-27. Completeness measured against the client's material and never against the register's own structure; a grouping declared with where it came from, and never the measure of whether the work is finished; a gap written down with a name against it; the register of requirements extracted by a separate act; a register published as one named list a program reads (SP1, SP3, SSC-10 to SSC-12, SSC-19).
- The use case model standard, SDD-05: the rules SSC-4 reads, the business model of M2 and section 2.4, and the form of this standard — its first page, its record, its review, its failures and its worked example. With it, by way of SDD-05, Alistair Cockburn, Ivar Jacobson and Craig Larman.
- The method standard, SDD-01: section 4 and figure 2, which name the customer's own documents as the one thing of the method's eleven this organisation does not govern — this standard governs them in the one case where this organisation writes them — and section 14, rule 17: an authority claimed without a source is an invention (SSC-20).
- The Public Administration Ecosystem Reference Architecture, published by GovStack: its definition of a service, and its first principle, the rule of law, by which a public body does only what law prescribes (SSC-6, SSC-8).
- The Core Public Service Vocabulary Application Profile, CPSV-AP, version 3.2.0: the fields evidence, output and channel, the competent authority and the legal resource, and the life event as a grouping of services (section 9.1, SSC-15).
- GovStack's reference use cases and their template: a use case of a public service, as a comparison for the models beneath (section 2.4).
- A national enterprise architecture framework's metamodel, whose business service serves a customer, is realised by a process and is named as an action on a subject: the first instance of the service this standard catalogues (SSC-6).
How firm these rules are. They were written from one paper, for one sector of one country, and none of them has yet been used by anybody who did not write it. Whether any meets this organisation's bar for adopting a rule — a recognised discipline stating it, and the same practice found in at least two independent fields — has not been searched, and every rule should be read as not tested. The first catalogue written to this draft, claiming conformance rule by rule and reporting every point at which the standard was silent, wrong or unclear, is the test on which the owner decides whether the standard comes into force; until then it is a draft and should not be quoted as binding.
