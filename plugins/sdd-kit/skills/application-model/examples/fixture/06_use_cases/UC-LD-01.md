<!--
standard: SDD-06
title: One System Use Case
edition: "1.2"
document: SDD-06_One_System_Use_Case_v1.2.docx
sha256: 4f3d6ac19817d798b9804bed57c35b6554364f66463eb5a6ab9e5301ba063c1b
produced_by: _working/2026-08-31_house_rebuild/build_house.js at 2026-09-29T09:30:52Z
-->

# One use case, written out in full

*A fixture of the method's application-model skill: the lending desk of the library of a town
called Eastbrook, which does not exist; it belongs to no engagement. Filled from the kit's template
of the use case; the screens of this goal are `../07_screens/UC-LD-01.md`.*

## 7.1 The record header

| Field | What to record | Rule | Answer |
|---|---|---|---|
| Unique identifier | The stable reference the model knows this use case by. | not stated | UC-LD-01 |
| Use case name | An active verb and its object, from the primary actor's point of view, in the words the business uses. The model settles the name; write the same one. | not stated | Lend an item to a member |
| Level | Summary, user goal or subfunction, as written on the survey row. | not stated | user goal |
| Primary actor | The actor whose goal this use case exists to satisfy. | not stated | the desk librarian |
| Status and priority | Draft, reviewed or baselined; and the priority the model set from business value and risk. | not stated | version 1 · baselined · accepted by Mara Lind on 22 September 2026; priority high |
| Requirements realised | The identifiers of the requirements, quality requirements and constraints this use case realises (U19). | U19 | RQ-LD-01, a member borrows an item at the desk |
| Entities read or changed | The entities from the entity model this use case reads, and separately those it changes, by name (U20). | U20 | reads: member, item; changes: loan |
| Business rules cited | The identifiers of the registered rules that govern this use case (U21). | U21 | BR-LD-01, a member holds at most the number of items the library allows, at step 4 |
| Relationships | Which use cases this one includes, which ones extend it, and the point at which each extension attaches. | not stated | none |

## 7.2 The narrative fields

| Field | What to write | Rule | Answer |
|---|---|---|---|
| Scope | The system under discussion, and whether it is being treated from the outside only or from the inside as well. | not stated | the lending desk application, from the outside |
| Stakeholders and interests | Each stakeholder, and the interest they need protected. Taken together these decide what complete means (U6). | U6 | the member wants the item with a clear due date; the library wants every item on loan held against one member |
| Preconditions | What is already true when the use case starts, and is not checked again inside it (U7). | U7 | the member is registered and the item is on the shelf |
| Trigger | The business event that starts the use case. It may be a clock. | not stated | a member brings an item to the desk |
| Minimal guarantee | What the system still guarantees if the use case fails (U7). | U7 | no loan is recorded |
| Success guarantee | What is true when it succeeds. It must satisfy every interest listed above (U7). | U7 | a loan stands on loan, holding the member, the item and the due date |
| Main success scenario | The single path on which nothing goes wrong: three to nine numbered steps, no branching (U3 to U5). | U3, U5 | 1. The desk librarian finds the member by the card number. 2. The librarian chooses the member. 3. The librarian finds the item by its barcode and picks the loan period. 4. The librarian lends the item; the application shows the due date. |
| Extensions | Numbered against the step each one leaves, stating the condition, the handling, and how it ends (U8, U9). | U8, U9 | 4a. The member already holds the most items allowed: the application refuses the loan and says why; the goal ends with no loan. |
| Quality requirements | The quality requirements that bind this use case, cited rather than written out again (U12). | U12 | none |
| Acceptance tests | Derived from the main success scenario and from every extension; they are what done means (U14). | U14 | T1: a loan made for a member holding fewer than the most items stands on loan. T2: a loan refused at 4a leaves no loan. |
