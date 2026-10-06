<!--
standard: SDD-03
title: The Entity Model
edition: "1.0"
document: SDD-03_The_Entity_Model_v1.0.md
sha256: 7f128a3e0c2e599651a6e37164dbe6e7c472a8d72853abfef75feb1156a72fdc
produced_by: _working/2026-08-31_house_rebuild/build_house.js at 2026-09-29T22:04:38Z
converted_from: SDD-03_The_Entity_Model_v1.0.docx sha256 f0ec3c8e9e00310cbde3f985370d8858e95c483d8f7c206f53131b9be9eee52e (sdd-kit carries its text as Markdown)
-->

# The register of business rules

*Written to SDD-03, The Entity Model, edition 1.0. Produced from the standard by `_working/2026-09-28_the_checklists/extract_checklist.py`, as the last step of its build; a copy of it is filled, and this file is never edited by hand. The quoted lines are the standard's own words.*

## 5.5 For each business rule

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Identifier | The stable reference every use case, screen and computation cites. Allocated once, never reused | EM-40 |  |
| Statement | The rule, short, standing on its own, with nothing of the flow that invokes it | EM-41 |  |
| Settings it reads | None; or each, by the name its entry in the catalogue of settings in SDD-04 carries. The statement names the setting and carries no value of it | EM-42 |  |
| Terms it uses | Every one of them, each already in the glossary or named in the entity model. A term in neither is a finding against the glossary | EM-42 |  |
| What it constrains | The records, attributes or relationships it binds: ____ | EM-42 |  |
| Where its authority comes from | A statute or instrument with its citation; a published policy; or this organisation's own decision, with the ruling that took it | EM-42 |  |
| From when it takes effect | A date — and where it has stopped applying, the date it stopped | EM-42 |  |
| Status | Proposed; in force; withdrawn — and if withdrawn, the date, the reason, and what replaces it | EM-42, EM-43 |  |
| What cites it | The use cases, screens and computations citing this identifier. An empty answer is reported as a finding and is not a failure | EM-44 |  |
