<!--
standard: SDD-03
title: The Entity Model
edition: "0.6"
document: SDD-03_The_Entity_Model_v0.6.docx
sha256: 137b5c4b50c3509b042da74e1306c5bd8053173d70e7eea21e08a95a29e4def0
produced_by: _working/2026-08-31_house_rebuild/build_house.js at 2026-09-29T09:30:52Z
-->

# The entity model

*Written to SDD-03, The Entity Model, edition 0.6. Produced from the standard by `_working/2026-09-28_the_checklists/extract_checklist.py`, as the last step of its build; a copy of it is filled, and this file is never edited by hand. The quoted lines are the standard's own words.*

**The model's heading.** The entity model of the loans module of the Eastbrook library system. Its glossary is `02_glossary.md` and its register of business rules is `02_business_rules.md`, both beside this file. Version 0.2 · 22 September 2026 · a draft, read with the head of circulation.

## 5.1 For each record

### Member

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Name | A singular noun phrase in the words the business uses, unique across the whole model | EM-16 | Member |
| Definition | One row per ____ . Singular, standing on its own, not repeating the name, carrying no rationale or procedure | EM-15 | One row per person registered by the town to borrow from the library. |
| Why it is a record | More than one row; more than one fact; means something on its own; can be told apart from every other kind. All four, or a written reason for the exception | EM-11 | All four: many members; each holds more than one fact; a member means something on their own; each is told apart from every other by the number the town's register gives them. |
| Identified how | On its own; or only through ____ , and the relationship that supplies the identity is named in the relationship form | EM-12 | On its own, by the number the town's register gives the member. |
| Special kinds | None; or branches ____ . Do the branches cover every row (yes / no)? May one row be in two at once (yes / no)? Both answered | EM-14 | None. |
| Parts played | Any capacity a row acts in that is not exclusive is a link and not a branch. List them: ____ | EM-13 | None: a member acts in no capacity but borrowing in this module. |
| Attributes, each with its least and most | For every attribute: the fewest that may be there and the most. Two separate decisions | EM-17 | Number: exactly one. Name: exactly one. Address: exactly one. Each as the town's register holds it. |
| What the minimums mean | Confirm the minimums are the model's floor and not one screen's rule | EM-18 | Confirmed: the minimums are the model's floor, read from the town's register, and not the rule of any one screen. |
| Attributes holding more than one value | None; or ____ , each of which becomes a record | EM-23 | None. |
| Where each attribute belongs | For every attribute: it describes one row of this record. Where it describes another record, it moves there and the link between the two records is drawn | EM-52 | Each describes one member. The loans a member holds are not drawn here; they are the record Loan, linked to the member. |
| Attribute names | No attribute name repeats this record's name. Where a qualifier is needed to tell two attributes apart, it is the qualifier that distinguishes them and never the record's name | EM-53 | Number, name, address: none repeats the record's name. |
| Made-up identifiers | None at this level; or ____ , each with the reason it is here | EM-25 | None at this level: the number is the town's, and has meaning outside this system. |
| Coded attributes | For each: the governed list ____ , named as its row in the table of governed lists names it — or the named selection of one ____ , named as its entry in SDD-04 names it — and the strength of binding. Its owner was asked here until version 0.2; it is now the issuer on the list's row, cited and not repeated | EM-19, EM-47 | None. |
| The governed lists used | For each: is it versioned, and are values retired rather than removed (yes / no / not known). Who issues it is on the list's row and is not repeated here | EM-20, EM-47 | None. |
| History kept | None; when the fact was true; when the system was told; both. A none carries a reason | EM-21 | None here: the record is consumed, and the clocks are the town's register's, which this model does not restate. |
| Coded values, as at | For each coded attribute the record stores: the stored value carries the date it was resolved as at, on the clock the record keeps — or the reason the record keeps neither clock covers it | EM-21 | The record stores no coded value. |
| Uniqueness | Over the identifier alone; or over the identifier and the period, where history is kept | EM-22 | Over the identifier alone: the number. |
| Boundary | This system is the authority — and nobody else consumes it, or it is published for others, to ____ ; consumes it from ____ ; must not hold it — held instead by ____ . Then, on every answer but the first: who issues it ____ (the body, never the software); where the issuer publishes it ____ . And on every answer: the words in the client's material this was derived from ____ , or not stated by the client; asked of ____ on ____ | EM-2, EM-45, EM-48 to EM-50 | Consumes it from the town's register of members. Who issues it: the town council's registry, whose act of registration makes a person a member. Where the issuer publishes it: the town's register of members, the service Members in force, entry by number. The words: the library's invitation to tender · section 3.1 · 'Members are registered by the town council's registry; the library system reads them from the town's register of members.' |
| Groups it is read in | ____ (a record may be in more than one) | EM-3 | Circulation. |
| Facts deliberately recorded twice | None; or ____ , each with the reason and with how the copies are kept in step | EM-24 | None. |
| Related to | The records this one is related to: ____ . Or the written reason it stands alone | EM-54 | Loan. |

### Copy

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Name | A singular noun phrase in the words the business uses, unique across the whole model | EM-16 | Copy |
| Definition | One row per ____ . Singular, standing on its own, not repeating the name, carrying no rationale or procedure | EM-15 | One row per physical item the library holds and may lend. |
| Why it is a record | More than one row; more than one fact; means something on its own; can be told apart from every other kind. All four, or a written reason for the exception | EM-11 | All four: many copies; each holds more than one fact; a copy means something on its own; each is told apart by the number on its label. |
| Identified how | On its own; or only through ____ , and the relationship that supplies the identity is named in the relationship form | EM-12 | On its own, by the number on its label. |
| Special kinds | None; or branches ____ . Do the branches cover every row (yes / no)? May one row be in two at once (yes / no)? Both answered | EM-14 | None. |
| Parts played | Any capacity a row acts in that is not exclusive is a link and not a branch. List them: ____ | EM-13 | None. |
| Attributes, each with its least and most | For every attribute: the fewest that may be there and the most. Two separate decisions | EM-17 | Number: exactly one. Title: exactly one. Home branch: exactly one. Each as the catalogue module holds it. |
| What the minimums mean | Confirm the minimums are the model's floor and not one screen's rule | EM-18 | Confirmed: the model's floor, read from the catalogue module. |
| Attributes holding more than one value | None; or ____ , each of which becomes a record | EM-23 | None. |
| Where each attribute belongs | For every attribute: it describes one row of this record. Where it describes another record, it moves there and the link between the two records is drawn | EM-52 | Each describes one copy. The title is kept on the copy as the catalogue module publishes it; the work it is a copy of is the catalogue module's record and is not drawn here. |
| Attribute names | No attribute name repeats this record's name. Where a qualifier is needed to tell two attributes apart, it is the qualifier that distinguishes them and never the record's name | EM-53 | Number, title, home branch: none repeats the record's name. |
| Made-up identifiers | None at this level; or ____ , each with the reason it is here | EM-25 | None at this level: the number is printed on the copy's label. |
| Coded attributes | For each: the governed list ____ , named as its row in the table of governed lists names it — or the named selection of one ____ , named as its entry in SDD-04 names it — and the strength of binding. Its owner was asked here until version 0.2; it is now the issuer on the list's row, cited and not repeated | EM-19, EM-47 | Home branch: the governed list Branch libraries, as its row in the table of governed lists names it, bound must use. |
| The governed lists used | For each: is it versioned, and are values retired rather than removed (yes / no / not known). Who issues it is on the list's row and is not repeated here | EM-20, EM-47 | Branch libraries: versioned, and values retired rather than removed: yes. |
| History kept | None; when the fact was true; when the system was told; both. A none carries a reason | EM-21 | None here: the record is consumed, and the catalogue module keeps its clocks. |
| Coded values, as at | For each coded attribute the record stores: the stored value carries the date it was resolved as at, on the clock the record keeps — or the reason the record keeps neither clock covers it | EM-21 | Home branch is stored by the catalogue module and read here; the date it was resolved as at is the catalogue module's, which neither clock of this model covers. |
| Uniqueness | Over the identifier alone; or over the identifier and the period, where history is kept | EM-22 | Over the identifier alone: the number. |
| Boundary | This system is the authority — and nobody else consumes it, or it is published for others, to ____ ; consumes it from ____ ; must not hold it — held instead by ____ . Then, on every answer but the first: who issues it ____ (the body, never the software); where the issuer publishes it ____ . And on every answer: the words in the client's material this was derived from ____ , or not stated by the client; asked of ____ on ____ | EM-2, EM-45, EM-48 to EM-50 | Consumes it from the catalogue module of the same library system. Who issues it: the library's acquisitions office, whose act of accessioning a copy makes it valid. Where the issuer publishes it: the catalogue module's list Copies held, entry by number. The words: the library's invitation to tender · section 4.1 · 'Loans are made of the copies the catalogue holds.' |
| Groups it is read in | ____ (a record may be in more than one) | EM-3 | Circulation. |
| Facts deliberately recorded twice | None; or ____ , each with the reason and with how the copies are kept in step | EM-24 | None. |
| Related to | The records this one is related to: ____ . Or the written reason it stands alone | EM-54 | Loan. |

### Loan

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Name | A singular noun phrase in the words the business uses, unique across the whole model | EM-16 | Loan |
| Definition | One row per ____ . Singular, standing on its own, not repeating the name, carrying no rationale or procedure | EM-15 | One row per handing of one copy to one member, from the day it leaves the library until it comes back or is declared lost. |
| Why it is a record | More than one row; more than one fact; means something on its own; can be told apart from every other kind. All four, or a written reason for the exception | EM-11 | All four: many loans; each holds more than one fact; a loan means something on its own; each is told apart by its number. |
| Identified how | On its own; or only through ____ , and the relationship that supplies the identity is named in the relationship form | EM-12 | On its own, by its number. |
| Special kinds | None; or branches ____ . Do the branches cover every row (yes / no)? May one row be in two at once (yes / no)? Both answered | EM-14 | None. |
| Parts played | Any capacity a row acts in that is not exclusive is a link and not a branch. List them: ____ | EM-13 | None. |
| Attributes, each with its least and most | For every attribute: the fewest that may be there and the most. Two separate decisions | EM-17 | Number: exactly one. Checkout date: exactly one. Due date, the one in force: exactly one. Returned date: none or one. Branch of checkout: exactly one. |
| What the minimums mean | Confirm the minimums are the model's floor and not one screen's rule | EM-18 | Confirmed: the model's floor. A returned date is absent until the copy comes back. |
| Attributes holding more than one value | None; or ____ , each of which becomes a record | EM-23 | None. |
| Where each attribute belongs | For every attribute: it describes one row of this record. Where it describes another record, it moves there and the link between the two records is drawn | EM-52 | Each describes one loan. The member's name and the copy's title are not drawn here: they belong to Member and to Copy, and the links are drawn. |
| Attribute names | No attribute name repeats this record's name. Where a qualifier is needed to tell two attributes apart, it is the qualifier that distinguishes them and never the record's name | EM-53 | Number, checkout date, due date, returned date, branch of checkout: none repeats the record's name. |
| Made-up identifiers | None at this level; or ____ , each with the reason it is here | EM-25 | None at this level: the number is quoted to the member and at the counter, and has meaning outside the system. |
| Coded attributes | For each: the governed list ____ , named as its row in the table of governed lists names it — or the named selection of one ____ , named as its entry in SDD-04 names it — and the strength of binding. Its owner was asked here until version 0.2; it is now the issuer on the list's row, cited and not repeated | EM-19, EM-47 | Branch of checkout: the governed list Branch libraries, as its row in the table of governed lists names it, bound must use. |
| The governed lists used | For each: is it versioned, and are values retired rather than removed (yes / no / not known). Who issues it is on the list's row and is not repeated here | EM-20, EM-47 | Branch libraries: versioned, and values retired rather than removed: yes. |
| History kept | None; when the fact was true; when the system was told; both. A none carries a reason | EM-21 | When the fact was true: the checkout, due and returned dates are the days each thing happened in the library. |
| Coded values, as at | For each coded attribute the record stores: the stored value carries the date it was resolved as at, on the clock the record keeps — or the reason the record keeps neither clock covers it | EM-21 | Branch of checkout carries the checkout date as the date it was resolved as at. |
| Uniqueness | Over the identifier alone; or over the identifier and the period, where history is kept | EM-22 | Over the identifier alone: the number. A loan is the period itself and is never held as two rows for two periods. |
| Boundary | This system is the authority — and nobody else consumes it, or it is published for others, to ____ ; consumes it from ____ ; must not hold it — held instead by ____ . Then, on every answer but the first: who issues it ____ (the body, never the software); where the issuer publishes it ____ . And on every answer: the words in the client's material this was derived from ____ , or not stated by the client; asked of ____ on ____ | EM-2, EM-45, EM-48 to EM-50 | This system is the authority, and it is published for others: to the fines module of the same library system, which reads every loan that comes back. Classification written from this module's position. The words: the library's invitation to tender · section 4.3 · 'Each loan of a copy to a member is recorded with its due date, and the fines system is told when it comes back.' |
| Groups it is read in | ____ (a record may be in more than one) | EM-3 | Circulation. |
| Facts deliberately recorded twice | None; or ____ , each with the reason and with how the copies are kept in step | EM-24 | The due date in force, which the loan's latest renewal also carries as its due date given. Kept on the loan so that every reader of a loan reads it without walking its renewals; kept in step because the one act that records a renewal writes both. |
| Related to | The records this one is related to: ____ . Or the written reason it stands alone | EM-54 | Member, Copy, Renewal. |

### Renewal

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Name | A singular noun phrase in the words the business uses, unique across the whole model | EM-16 | Renewal |
| Definition | One row per ____ . Singular, standing on its own, not repeating the name, carrying no rationale or procedure | EM-15 | One row per extension of a loan's due date, granted at the request of the member who holds it. |
| Why it is a record | More than one row; more than one fact; means something on its own; can be told apart from every other kind. All four, or a written reason for the exception | EM-11 | All four: many renewals; each holds more than one fact; a renewal means something on its own; each is told apart by its loan and the moment it was granted. |
| Identified how | On its own; or only through ____ , and the relationship that supplies the identity is named in the relationship form | EM-12 | Only through the loan it extends, together with the moment it was granted; the relationship 'extends a loan' supplies the identity. |
| Special kinds | None; or branches ____ . Do the branches cover every row (yes / no)? May one row be in two at once (yes / no)? Both answered | EM-14 | None. |
| Parts played | Any capacity a row acts in that is not exclusive is a link and not a branch. List them: ____ | EM-13 | None. |
| Attributes, each with its least and most | For every attribute: the fewest that may be there and the most. Two separate decisions | EM-17 | Granted at: exactly one. Due date given: exactly one. Channel: exactly one. |
| What the minimums mean | Confirm the minimums are the model's floor and not one screen's rule | EM-18 | Confirmed: the model's floor. |
| Attributes holding more than one value | None; or ____ , each of which becomes a record | EM-23 | None. |
| Where each attribute belongs | For every attribute: it describes one row of this record. Where it describes another record, it moves there and the link between the two records is drawn | EM-52 | Each describes one renewal. The due date in force is the loan's, and is not drawn here. |
| Attribute names | No attribute name repeats this record's name. Where a qualifier is needed to tell two attributes apart, it is the qualifier that distinguishes them and never the record's name | EM-53 | Granted at, due date given, channel: none repeats the record's name. |
| Made-up identifiers | None at this level; or ____ , each with the reason it is here | EM-25 | None at this level. |
| Coded attributes | For each: the governed list ____ , named as its row in the table of governed lists names it — or the named selection of one ____ , named as its entry in SDD-04 names it — and the strength of binding. Its owner was asked here until version 0.2; it is now the issuer on the list's row, cited and not repeated | EM-19, EM-47 | Channel: the governed list Renewal channels, as its row in the table of governed lists names it, bound must use. |
| The governed lists used | For each: is it versioned, and are values retired rather than removed (yes / no / not known). Who issues it is on the list's row and is not repeated here | EM-20, EM-47 | Renewal channels: versioned, and values retired rather than removed: yes. |
| History kept | None; when the fact was true; when the system was told; both. A none carries a reason | EM-21 | When the fact was true, which is also when the system was told: a renewal exists only by the act that records it, so the one moment serves both clocks. |
| Coded values, as at | For each coded attribute the record stores: the stored value carries the date it was resolved as at, on the clock the record keeps — or the reason the record keeps neither clock covers it | EM-21 | Channel carries the moment granted at as the date it was resolved as at. |
| Uniqueness | Over the identifier alone; or over the identifier and the period, where history is kept | EM-22 | Over the loan and the moment granted at, together. |
| Boundary | This system is the authority — and nobody else consumes it, or it is published for others, to ____ ; consumes it from ____ ; must not hold it — held instead by ____ . Then, on every answer but the first: who issues it ____ (the body, never the software); where the issuer publishes it ____ . And on every answer: the words in the client's material this was derived from ____ , or not stated by the client; asked of ____ on ____ | EM-2, EM-45, EM-48 to EM-50 | This system is the authority, and nobody else consumes it. Classification written from this module's position. The words: the library's loan policy · paragraph 5 · 'A loan may be renewed online or at any counter, as often as the policy allows.' |
| Groups it is read in | ____ (a record may be in more than one) | EM-3 | Circulation. |
| Facts deliberately recorded twice | None; or ____ , each with the reason and with how the copies are kept in step | EM-24 | None. |
| Related to | The records this one is related to: ____ . Or the written reason it stands alone | EM-54 | Loan. |

> A record that answers only the definition line has not been described. It has been named.

## 5.2 For each relationship

### Loan made to Member

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Name, reading from this end | ____ (what the link is, plus the thing at the far end) | EM-26 | Made to a member (reading from Loan). |
| Name, reading from the far end | ____ — so that both directions read as complete sentences | EM-32 | Holder of a loan (reading from Member). |
| Read back, in both directions | The two sentences as they were put to a business reader, in the form EM-32 states, and the answer each got. A reading nobody recorded cannot be told from a reading nobody did | EM-32 | 'Each and every Loan must be made to one and only one Member -- is that true?' Yes. 'Each and every Member may be the holder of one or more Loans -- is that true?' Yes. 'A Loan that is not made to a uniquely identifiable Member can never exist.' Agreed. Put to the head of circulation on 2 September 2026. |
| Degree | ____ rows at this end go with ____ rows at the far end | EM-17 | Many loans at this end go with one member at the far end. |
| Optionality | May this end be absent (yes / no)? May the far end (yes / no)? | EM-17 | A member may hold no loan: yes. A loan without its member: no. |
| If both ends are optional | The reason, written out — or the relationship is corrected | EM-33 | Not optional at both ends. |
| Identifying or referring | Does this relationship supply the far record's identity (yes / no)? | EM-12 | Referring: a loan is identified by its own number. |
| Facts of its own | None; or ____ — and if there are any, it is a record and is written up as one | EM-27 | None. |
| If many at both ends | The record it resolves into: ____ | EM-28 | Not many at both ends. |
| Excluded by another relationship | No; exclusive with ____ , and the exclusion is written in the model | EM-30 | No. |
| On removal, replacement or correction | The far row goes too; the far row is left pointing at nothing; the removal is refused; the near row is never removed, only superseded | EM-31 | The near row is never removed, only superseded: a loan outlives its member's removal from the town's register, and keeps the member's number as it stood. |
| Loops back to the same record | No; yes, and the relation it carries is: is a kind of; is part of; is grouped with; supersedes | EM-29 | No. |

### Loan of Copy

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Name, reading from this end | ____ (what the link is, plus the thing at the far end) | EM-26 | Of a copy (reading from Loan). |
| Name, reading from the far end | ____ — so that both directions read as complete sentences | EM-32 | Lent in a loan (reading from Copy). |
| Read back, in both directions | The two sentences as they were put to a business reader, in the form EM-32 states, and the answer each got. A reading nobody recorded cannot be told from a reading nobody did | EM-32 | 'Each and every Loan must be of one and only one Copy -- is that true?' Yes. 'Each and every Copy may ever be lent in one or more Loans -- is that true?' Yes. 'A Loan that is not of a uniquely identifiable Copy can never exist.' Agreed. Put to the head of circulation on 2 September 2026. |
| Degree | ____ rows at this end go with ____ rows at the far end | EM-17 | Many loans, over time, at this end go with one copy at the far end. |
| Optionality | May this end be absent (yes / no)? May the far end (yes / no)? | EM-17 | A copy may never have been lent: yes. A loan without its copy: no. |
| If both ends are optional | The reason, written out — or the relationship is corrected | EM-33 | Not optional at both ends. |
| Identifying or referring | Does this relationship supply the far record's identity (yes / no)? | EM-12 | Referring. |
| Facts of its own | None; or ____ — and if there are any, it is a record and is written up as one | EM-27 | None. |
| If many at both ends | The record it resolves into: ____ | EM-28 | Not many at both ends. |
| Excluded by another relationship | No; exclusive with ____ , and the exclusion is written in the model | EM-30 | No. |
| On removal, replacement or correction | The far row goes too; the far row is left pointing at nothing; the removal is refused; the near row is never removed, only superseded | EM-31 | The near row is never removed, only superseded: a loan outlives the copy's withdrawal from the catalogue, and keeps the copy's number as it stood. |
| Loops back to the same record | No; yes, and the relation it carries is: is a kind of; is part of; is grouped with; supersedes | EM-29 | No. |

### Renewal extends Loan

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Name, reading from this end | ____ (what the link is, plus the thing at the far end) | EM-26 | Extends a loan (reading from Renewal). |
| Name, reading from the far end | ____ — so that both directions read as complete sentences | EM-32 | Extended by a renewal (reading from Loan). |
| Read back, in both directions | The two sentences as they were put to a business reader, in the form EM-32 states, and the answer each got. A reading nobody recorded cannot be told from a reading nobody did | EM-32 | 'Each and every Renewal must extend one and only one Loan -- is that true?' Yes. 'Each and every Loan may ever be extended by one or more Renewals -- is that true?' Yes. 'A Renewal that does not extend a uniquely identifiable Loan can never exist.' Agreed. Put to the head of circulation on 22 September 2026. |
| Degree | ____ rows at this end go with ____ rows at the far end | EM-17 | Many renewals at this end go with one loan at the far end. |
| Optionality | May this end be absent (yes / no)? May the far end (yes / no)? | EM-17 | A loan may have no renewal: yes. A renewal without its loan: no. |
| If both ends are optional | The reason, written out — or the relationship is corrected | EM-33 | Not optional at both ends. |
| Identifying or referring | Does this relationship supply the far record's identity (yes / no)? | EM-12 | Identifying: it supplies the renewal's identity. |
| Facts of its own | None; or ____ — and if there are any, it is a record and is written up as one | EM-27 | None. |
| If many at both ends | The record it resolves into: ____ | EM-28 | Not many at both ends. |
| Excluded by another relationship | No; exclusive with ____ , and the exclusion is written in the model | EM-30 | No. |
| On removal, replacement or correction | The far row goes too; the far row is left pointing at nothing; the removal is refused; the near row is never removed, only superseded | EM-31 | The near row is never removed, only superseded: a loan is never removed, so no renewal is left without its loan. |
| Loops back to the same record | No; yes, and the relation it carries is: is a kind of; is part of; is grouped with; supersedes | EM-29 | No. |

## 5.3 For the model as a whole

> This is the part that is filled once, and the part that is most often not filled at all.

### The loans module of the Eastbrook library system

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Level | Naming the things the business deals with; structuring them into records with identifiers and relationships; describing how they are stored — and what is therefore excluded | EM-1 | The second of the three: the things structured into records with identifiers and relationships. Excluded: how anything is stored -- column types, indexes, storage hints, and identifiers made up for storage. |
| What this model is of | The records this system keeps, and the records and lists it depends on, whoever keeps them. If the module must also publish what it exchanges with other systems, that is a second document, named here: ____ | — | The records the loans module keeps, Loan and Renewal, and the records and lists it depends on, Member, Copy, Branch libraries and Renewal channels. What the module publishes to another system is carried by the catalogue of events of the module's shared registers; no second document is needed. |
| Boundary statement | The records this system is the authority for and nobody else consumes ____ ; the records it is the authority for and publishes, and to whom ____ ; the records it consumes, and from whom ____ ; the kinds of thing it deliberately does not hold, and where each is held instead ____ | EM-2, EM-45 | The authority, nobody else consuming: Renewal. The authority, and published: Loan, to the fines module of the same library system. Consumed: Member, from the town's register of members; Copy, from the catalogue module; the list Branch libraries, from the town council's register of places. Deliberately not held: a member's fines and payments, held instead by the fines module. |
| Groups | The named groups, each small enough to read; the records appearing in more than one; and how a relationship crossing two groups is shown in both | EM-3 | One group, Circulation, holding all four records; no record is in more than one group, and no relationship crosses a group. This model keeps a group to no more than nine records. |
| Counts, stated and not judged | How many records; how many relationships; how many records carry no definition; how many relationships carry no name. No threshold is set and none may be inferred | EM-3, EM-6 | Four records; three relationships; no record without a definition; no relationship without a name. Counted on this file, 02_entity_model.md, on 29 September 2026, by reading its tables when the fixture was written. No threshold is set. |
| The two clocks | Which records keep when a fact was true, which keep when the system was told, which keep both, and which keep neither — with a reason for each neither | EM-21 | When the fact was true: Loan. Both, as one moment: Renewal, whose reason is on its record. Neither: Member and Copy, which are consumed and keep their authorities' clocks. |
| Normal form | The form the model is held to, and every place it is deliberately departed from, with the reason and with how the copies are kept in step | EM-24 | Third normal form, with one departure, recorded on the record Loan: the due date in force is held on the loan as well as on its latest renewal, with the reason and how the two are kept in step. |
| Extension rule | What a later version may change and what it may not — written before there is a later version | EM-4 | A later version may add records, attributes and relationships, and may widen a least or a most; it may not rename, remove or narrow anything already published. |
| Notation | Which one notation this model uses ____ ; and what that notation cannot say, listed, with where each of those things is written instead | EM-9, EM-10 | Information engineering, drawn with the crow's foot. What it cannot say -- the boundary answers, the clocks a record keeps, and what happens at the far end on removal -- is written in the lines of this file and nowhere on a picture. |
| Layout convention | The convention every generated picture follows: where the many end of a relationship is placed, where relationship names sit, and what the title of every picture carries | EM-55 | The many end of every relationship sits below or to the right of the one end; each relationship's name sits above the line at the end it reads from; every picture's title carries the module, the group and the version of this file. |
| The pictures | Which pictures exist, what each is for, who reads each, and which single model they are all generated from | EM-7, EM-8 | None drawn yet: the program that draws the picture of the group Circulation from this file is not written. A finding, owned by the analyst, by 30 October 2026. |
| The register beside the pictures | Where the definitions live; where the derivations live. Where the governed lists live was asked here until version 0.2 and is superseded by the table of governed lists on the next line | EM-7 | The definitions live in the lines of this file for each record. The derivations live in the catalogue of computations of the module's shared registers, where days overdue is worked out. |
| The table of governed lists | One row for every list any coded attribute names, in the columns laid out below this form, filled once for the model. A list an attribute names that has no row, and a row with no classification or no source line, is an unanswered line of this form | EM-47 to EM-51 | Two rows, in the table below this form. |
| Written in the first pass | Confirm that every classification and its reference lines were written before any goal was named; where one was not, it is recorded as a finding with an owner | EM-51 | Confirmed: every classification and its reference lines were written on 2 September 2026, before any goal was named. |
| The two passes | Which lines of this form belong to the first pass and which to the second, wherever the assignment departs from the list in part 5; and whether this model is reported as finished for the first pass or finished outright | EM-56 | The assignment of part 5 is followed without departure. The first pass was written on 2 September 2026 and the second on 22 September 2026; the model is reported finished outright. |
| Owner and change procedure | Who owns the model; who may propose a change; who decides | EM-5 | Owned by the head of circulation. The analyst or any librarian may propose a change, as a written request; the head of circulation decides. |
| Review | Who reviews it, against what list, and which items on that list a program cannot check | EM-6 | Reviewed by the head of circulation and the module's architect, against the gate of part 6. Every line is judged by a person: no check of part 6.1 is built. |
| The depth worked at | The level of detail this model was drawn to, in the analyst's own words, applied consistently across every record. This standard does not yet say which depth to choose | not settled | Every fact a loan's screen shows or a rule reads, and nothing below that, applied to every record alike. |
| Open questions | The decisions genuinely in dispute, each with a named owner and a date — never closed by a silent default | — | Whether a lost loan may return to being on loan when its copy is found: the head of circulation, by 30 October 2026. |

> The table of governed lists — one row for every list any coded attribute names. These are its columns. A row is complete when every column has an answer or a written reason for having none, on the same test as every other line of this form.

| List | Classification | Issuer | Where the issuer publishes it | Source in the client's material | Consumers known |
|---|---|---|---|---|---|
| Branch libraries | Held elsewhere, consumed here | The town council, whose resolution opens or closes a branch | The town council's register of places, the list ECL-BRANCH, in its current dated edition | The library's invitation to tender · section 4.3 · 'Each loan records the branch where it was made, from the council's list of branches.' | Not applicable |
| Renewal channels | This system's and nobody else's | Not asked: the list is this system's and nobody else's | Not asked: the list is this system's and nobody else's | The library's loan policy · paragraph 5 · 'A loan may be renewed online or at any counter, as often as the policy allows.' | Not applicable |

- **List** — The name the model uses for it, as the coded attributes name it (EM-47)
- **Classification** — This system's and nobody else's; this system's and published for others; held elsewhere, consumed here; not held at all — held instead by ____ . Made from this system's position (EM-2, EM-45, EM-46)
- **Issuer** — The body whose act makes a value a member — never the software that serves the list. Or not stated by the client; asked of ____ on ____ . Not asked where the list is this system's and nobody else's (EM-48, EM-50)
- **Where the issuer publishes it** — The document, register, view or service a reader goes to for the current edition, and the place in it. Or not stated by the client; asked of ____ on ____ . Not asked where the list is this system's and nobody else's (EM-49, EM-50)
- **Source in the client's material** — The document, the place, the words — or that the client was silent, and who was asked and when (EM-50)
- **Consumers known** — Only where the classification is published for others: who, from the client's material, or none named. On every other answer, not applicable (EM-45)
