---
standard: SDD-05
title: The Use Case Model
edition: "2.1"
document: SDD-05_The_Use_Case_Model_v2.1.md
sha256: 122eb3aec02971a48996303325112c1c1a98069619335daea3c5d3ce30c0faee
produced_by: _working/2026-08-31_house_rebuild/build_house.js at 2026-09-22T19:42:32Z
converted_from: SDD-05_The_Use_Case_Model_v2.1.docx sha256 5fc156de61994b9d6255ee3e478cc582d7e271f68a0417eea1107190c038bdc7 (sdd-kit carries its text as Markdown)
---

# SDD-05 · The Use Case Model — the checklist

*Produced from the document named above by `_working/2026-09-28_the_checklists/extract_checklist.py`, as the last step of its build, and never edited by hand. Every line below is the document's own words, read from it, except the lines in italics, which are this program's.*

*Rules counted in the document: 22. The document states "Twenty-two rules, a model record" (22).*

## Gate — the program's half

*The document states no part of its gate for a program to perform.*

## Gate — the person's half

### 11 The review

Run this before a use case model is baselined, and before any slice cut from it enters delivery. The model's owner runs it with the architecture authority. A model passes only when every applicable line is satisfied. An unsatisfied line is a finding with a named owner, not an exception to be waved through.

| Rules | Checkpoint | Passed |
|---|---|---|
| M1–M3 | The system is named, exactly one boundary is drawn, and the design scope — organisation or software, black-box or white-box — is stated. | ☐ |
| M4–M6 | Actors are roles, each classified as primary, supporting or offstage; actors that are systems, devices or clocks are included. | ☐ |
| M7–M8 | Every use case derives from an actor goal and is named as an active verb and an object. | ☐ |
| M9 | Every use case at the level of a single sitting passes the manager's test, the single business event test and the size test. | ☐ |
| M10 | No functional decomposition — no use case per button, per field or per stored record. | ☐ |
| M9–M11 | Include, extend and generalisation are used only for genuine reuse or genuine optionality, and sparingly. | ☐ |
| M12–M13 | Large models are grouped into packages that hold together, and a survey exists carrying priority and status. | ☐ |
| M14 | Every primary actor's goals are covered; every supporting actor is called; nothing lacks a primary actor or a result. | ☐ |
| M15 | The trace runs in both directions: business goal, use case, slice, test. | ☐ |
| M16 | Every use case records the requirements it realises, and every stated requirement is realised by at least one use case. | ☐ |
| M17 | One entity model is named; every entity a use case refers to is defined in it; no field structure appears in any flow. | ☐ |
| M22 | One glossary exists beside the entity model, carrying the terms the entity model does not, with one term for each concept. | ☐ |
| M18 | Every business rule the model depends on is registered with an identifier and cited, not stated only inside prose. | ☐ |
| M21 | The survey states which use cases are written out in full and which are not, and the order was set by value, risk and architectural significance. | ☐ |
| M19–M20 | The model is held as versioned text with record headers and a generated survey, and behaviour changes were specified and agreed before they were realised. | ☐ |

What this review does not do. Every line above tests a structural property — that something is named, recorded, classified, bound or covered. None of them asks whether what is recorded is true. Section 14 states the limit that leaves.

## Form

### 9.1 The record header

| line | rule |
|---|---|
| Identifier | M13 |
| Name | M8 |
| Level | not stated |
| Primary actor | M5 |
| Status and priority | M13 |
| Format | M21 |
| Linked requirements | M16 |
| Entities | M17 |
| Business rules | M18 |
| Relationships | M11 |

## Rules

| rule | words | program |
|---|---|---|
| M1 | Name the system under discussion before listing anything | none |
| M2 | Separate the business model from the system model. | none |
| M3 | Record the design scope on the model. | none |
| M4 | Identify actors by the role played, not by | none |
| M5 | Classify every actor as primary, supporting or offstage. | none |
| M6 | Include actors that are not people, and actors | none |
| M7 | Derive use cases from actor goals. | none |
| M8 | Name use cases as an active verb and | none |
| M9 | Set granularity with three tests, and require all | none |
| M10 | Do not decompose functionally. | none |
| M11 | Prefer flows to relationships. | none |
| M12 | Group large models into packages that hold together. | none |
| M13 | Maintain a use case survey. | none |
| M14 | Define completeness explicitly. | none |
| M15 | Establish traceability in both directions. | none |
| M16 | Close the requirement binding in both directions. | none |
| M17 | Name exactly one entity model as the model's | none |
| M22 | Maintain one glossary beside the entity model. | none |
| M18 | Keep one register of business rules. | none |
| M19 | Hold the model as versioned text, and generate | none |
| M20 | Change the model before changing the system. | none |
| M21 | Decide across the model which use cases are | none |
