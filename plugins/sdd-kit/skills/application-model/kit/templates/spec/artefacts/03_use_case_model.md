<!--
standard: SDD-05
title: The Use Case Model
edition: "2.1"
document: SDD-05_The_Use_Case_Model_v2.1.md
sha256: 122eb3aec02971a48996303325112c1c1a98069619335daea3c5d3ce30c0faee
produced_by: _working/2026-08-31_house_rebuild/build_house.js at 2026-09-22T19:42:32Z
converted_from: SDD-05_The_Use_Case_Model_v2.1.docx sha256 5fc156de61994b9d6255ee3e478cc582d7e271f68a0417eea1107190c038bdc7 (sdd-kit carries its text as Markdown)
-->

# The use case model

*Written to SDD-05, The Use Case Model, edition 2.1. Produced from the standard by `_working/2026-09-28_the_checklists/extract_checklist.py`, as the last step of its build; a copy of it is filled, and this file is never edited by hand. The quoted lines are the standard's own words.*

## 9.1 The record header

> These are the fields the model requires every use case to carry. The survey is generated from them, and the model's completeness and traceability checks run against them.

| Field | What to record | Rule | Answer |
|---|---|---|---|
| Identifier | The stable reference by which the model knows this use case (M13). | M13 |  |
| Name | An active verb and an object, from the primary actor's viewpoint (M8). | M8 |  |
| Level | Summary, user goal or subfunction (section 2.3). | not stated |  |
| Primary actor | The actor whose goal this use case satisfies (M5). | M5 |  |
| Status and priority | Draft, reviewed or baselined; priority set by value and risk (M13). | M13 |  |
| Format | Brief, outline, or written out in full — the decision recorded under M21. | M21 |  |
| Linked requirements | The identifiers of the requirements, non-functional requirements and constraints this use case realises (M16). | M16 |  |
| Entities | The entities of the named entity model that this use case reads or changes, by name only (M17). | M17 |  |
| Business rules | The identifiers of the registered rules that govern this use case (M18). | M18 |  |
| Relationships | Include, extend or generalisation, with the extension points named (M11). | M11 |  |

> This header is the model's record of the use case. It is written once for each use case and it is read by machine: the survey is generated from it, and the model's checks run against it. A value that appears both here and in the prose of the use case will come to disagree with itself within a quarter. State it here only.
