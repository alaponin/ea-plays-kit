<!--
standard: SDD-06
title: One System Use Case
edition: "1.2"
document: SDD-06_One_System_Use_Case_v1.2.md
sha256: b414e78337ac134cf51a3cbe6477e6653b2c7aabd585de0130bc9df703c6f50a
produced_by: _working/2026-08-31_house_rebuild/build_house.js at 2026-09-29T09:30:52Z
converted_from: SDD-06_One_System_Use_Case_v1.2.docx sha256 4f3d6ac19817d798b9804bed57c35b6554364f66463eb5a6ab9e5301ba063c1b (sdd-kit carries its text as Markdown)
-->

# One use case, written out in full

*Written to SDD-06, One System Use Case, edition 1.2. Produced from the standard by `_working/2026-09-28_the_checklists/extract_checklist.py`, as the last step of its build; a copy of it is filled, and this file is never edited by hand. The quoted lines are the standard's own words.*

## 7.1 The record header

| Field | What to record | Rule | Answer |
|---|---|---|---|
| Unique identifier | The stable reference the model knows this use case by. | not stated |  |
| Use case name | An active verb and its object, from the primary actor's point of view, in the words the business uses. The model settles the name; write the same one. | not stated |  |
| Level | Summary, user goal or subfunction, as written on the survey row. | not stated |  |
| Primary actor | The actor whose goal this use case exists to satisfy. | not stated |  |
| Status and priority | Draft, reviewed or baselined; and the priority the model set from business value and risk. | not stated |  |
| Requirements realised | The identifiers of the requirements, quality requirements and constraints this use case realises (U19). | U19 |  |
| Entities read or changed | The entities from the entity model this use case reads, and separately those it changes, by name (U20). | U20 |  |
| Business rules cited | The identifiers of the registered rules that govern this use case (U21). | U21 |  |
| Relationships | Which use cases this one includes, which ones extend it, and the point at which each extension attaches. | not stated |  |

> State each of these once, here. A value written both in the header and in the prose below will come to disagree with itself within a quarter (U18).

## 7.2 The narrative fields

| Field | What to write | Rule | Answer |
|---|---|---|---|
| Scope | The system under discussion, and whether it is being treated from the outside only or from the inside as well. | not stated |  |
| Stakeholders and interests | Each stakeholder, and the interest they need protected. Taken together these decide what complete means (U6). | U6 |  |
| Preconditions | What is already true when the use case starts, and is not checked again inside it (U7). | U7 |  |
| Trigger | The business event that starts the use case. It may be a clock. | not stated |  |
| Minimal guarantee | What the system still guarantees if the use case fails (U7). | U7 |  |
| Success guarantee | What is true when it succeeds. It must satisfy every interest listed above (U7). | U7 |  |
| Main success scenario | The single path on which nothing goes wrong: three to nine numbered steps, no branching (U3 to U5). | U3, U5 |  |
| Extensions | Numbered against the step each one leaves, stating the condition, the handling, and how it ends (U8, U9). | U8, U9 |  |
| Quality requirements | The quality requirements that bind this use case, cited rather than written out again (U12). | U12 |  |
| Acceptance tests | Derived from the main success scenario and from every extension; they are what done means (U14). | U14 |  |
