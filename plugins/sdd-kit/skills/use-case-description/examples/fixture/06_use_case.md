<!--
standard: SDD-06
title: One System Use Case
edition: "1.2"
document: SDD-06_One_System_Use_Case_v1.2.docx
sha256: 4f3d6ac19817d798b9804bed57c35b6554364f66463eb5a6ab9e5301ba063c1b
produced_by: _working/2026-08-31_house_rebuild/build_house.js at 2026-09-29T09:30:52Z
-->

# One use case, written out in full

*Written to SDD-06, One System Use Case, edition 1.2. Produced from the standard by `_working/2026-09-28_the_checklists/extract_checklist.py`, as the last step of its build; a copy of it is filled, and this file is never edited by hand. The quoted lines are the standard's own words.*

## 7.1 The record header

| Field | What to record | Rule | Answer |
|---|---|---|---|
| Unique identifier | The stable reference the model knows this use case by. | not stated | UC-LN-02 |
| Use case name | An active verb and its object, from the primary actor's point of view, in the words the business uses. The model settles the name; write the same one. | not stated | Renew a loan |
| Level | Summary, user goal or subfunction, as written on the survey row. | not stated | User goal, as written on the survey row. |
| Primary actor | The actor whose goal this use case exists to satisfy. | not stated | Member |
| Status and priority | Draft, reviewed or baselined; and the priority the model set from business value and risk. | not stated | Draft · High, as the model set it. |
| Requirements realised | The identifiers of the requirements, quality requirements and constraints this use case realises (U19). | U19 | F-1. |
| Entities read or changed | The entities from the entity model this use case reads, and separately those it changes, by name (U20). | U20 | Reads: Member, Copy, Loan. Changes: Loan, Renewal. |
| Business rules cited | The identifiers of the registered rules that govern this use case (U21). | U21 | BR-1, BR-2, BR-5. |
| Relationships | Which use cases this one includes, which ones extend it, and the point at which each extension attaches. | not stated | Includes Prove a member's identity, UC-MB-01, at step 2. Extended by no use case. |

> State each of these once, here. A value written both in the header and in the prose below will come to disagree with itself within a quarter (U18).

## 7.2 The narrative fields

| Field | What to write | Rule | Answer |
|---|---|---|---|
| Scope | The system under discussion, and whether it is being treated from the outside only or from the inside as well. | not stated | The loans module of the Eastbrook library system, treated from the outside only. |
| Stakeholders and interests | Each stakeholder, and the interest they need protected. Taken together these decide what complete means (U6). | U6 | Member: to keep the copy longer and to be told the new due date. Head of circulation: that no loan is renewed against the library's loan policy. Fines module: that the due date it works overdue days from is the one the renewal gave. A member waiting for the copy: that a renewal keeps the copy from them no longer than the policy allows. |
| Preconditions | What is already true when the use case starts, and is not checked again inside it (U7). | U7 | The member is registered in the town's register of members and holds at least one loan. |
| Trigger | The business event that starts the use case. It may be a clock. | not stated | The member asks to renew one of their loans. |
| Minimal guarantee | What the system still guarantees if the use case fails (U7). | U7 | No loan's due date changes unless a renewal is recorded for it; a refused or interrupted request leaves the loan as it was; the member is told why a request was refused. |
| Success guarantee | What is true when it succeeds. It must satisfy every interest listed above (U7). | U7 | A renewal the loan policy allows is recorded against the loan, the loan carries the due date the renewal gave, and the member has been shown that date. |
| Main success scenario | The single path on which nothing goes wrong: three to nine numbered steps, no branching (U3 to U5). | U3, U5 | Eight steps, set out below the table. |
| Extensions | Numbered against the step each one leaves, stating the condition, the handling, and how it ends (U8, U9). | U8, U9 | Five, set out below the table. |
| Quality requirements | The quality requirements that bind this use case, cited rather than written out again (U12). | U12 | None binds this goal: the register of requirements carries no quality requirement on renewal. A finding against the register of requirements, owned by the analyst, by 30 October 2026. |
| Acceptance tests | Derived from the main success scenario and from every extension; they are what done means (U14). | U14 | AT-1 for the main success scenario, asserting the success guarantee. AT-2 to AT-6 for the extensions 2a, 3a, 4a, 6a and *a, each asserting the minimal guarantee: the loan's due date is unchanged and no renewal is recorded. |

## The main success scenario

1. The member asks to renew one of their loans.
2. The system proves the member's identity (shared behaviour: Prove a member's identity).
3. The system confirms that the loan is still on loan and not yet due (BR-1).
4. The system confirms that the loan's renewals are within the limit (BR-2).
5. The system shows the member the due date the renewal would give (BR-5).
6. The member confirms the renewal.
7. The system records the renewal against the loan.
8. The system shows the member the loan's new due date.

## The extensions

| Ref | What happens | Kind |
|---|---|---|
| 2a | The member's identity cannot be proved. The included use case ends in failure, and so does this one. The minimal guarantee holds. | business alternative |
| 3a | The loan is not on loan, or its due date has passed (BR-1). The system refuses the renewal and tells the member why. The use case ends in failure. | business alternative |
| 4a | The loan has been renewed as many times as the setting Renewal limit allows (BR-2). The system refuses the renewal and tells the member why. The use case ends in failure. | business alternative |
| 6a | The member does not confirm. The system records nothing, and the use case ends in failure. The minimal guarantee holds. | business alternative |
| *a | At any step before step 7, the loans module becomes unavailable. The system records nothing and tells the member that the request was interrupted. The use case ends in failure, and the minimal guarantee holds. | system or environment failure |
