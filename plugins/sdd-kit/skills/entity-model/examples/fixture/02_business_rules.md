<!--
standard: SDD-03
title: The Entity Model
edition: "0.6"
document: SDD-03_The_Entity_Model_v0.6.docx
sha256: 137b5c4b50c3509b042da74e1306c5bd8053173d70e7eea21e08a95a29e4def0
produced_by: _working/2026-08-31_house_rebuild/build_house.js at 2026-09-29T09:30:52Z
-->

# The register of business rules

*Written to SDD-03, The Entity Model, edition 0.6. Produced from the standard by `_working/2026-09-28_the_checklists/extract_checklist.py`, as the last step of its build; a copy of it is filled, and this file is never edited by hand. The quoted lines are the standard's own words.*

**The register's heading.** The register of business rules of the entity model of the loans module of the Eastbrook library system, `02_entity_model.md`, beside it. Version 0.2 · 22 September 2026.

## 5.5 For each business rule

### BR-1

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Identifier | The stable reference every use case, screen and computation cites. Allocated once, never reused | EM-40 | BR-1 |
| Statement | The rule, short, standing on its own, with nothing of the flow that invokes it | EM-41 | A loan may be renewed only while it is on loan and before its due date. |
| Settings it reads | None; or each, by the name its entry in the catalogue of settings in SDD-04 carries. The statement names the setting and carries no value of it | EM-42 | None. |
| Terms it uses | Every one of them, each already in the glossary or named in the entity model. A term in neither is a finding against the glossary | EM-42 | Loan and Renewal, records of the entity model; due date, an attribute of Loan; on loan, in the glossary. |
| What it constrains | The records, attributes or relationships it binds: ____ | EM-42 | The relationship of a renewal to the loan it extends. |
| Where its authority comes from | A statute or instrument with its citation; a published policy; or this organisation's own decision, with the ruling that took it | EM-42 | The library's loan policy, paragraph 5, a published policy. |
| From when it takes effect | A date — and where it has stopped applying, the date it stopped | EM-42 | 1 January 2025. |
| Status | Proposed; in force; withdrawn — and if withdrawn, the date, the reason, and what replaces it | EM-42, EM-43 | In force. |
| What cites it | The use cases, screens and computations citing this identifier. An empty answer is reported as a finding and is not a failure | EM-44 | The use case Renew a loan, UC-LN-02, in its header, at its step 3 and at its extension 3a. |

### BR-2

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Identifier | The stable reference every use case, screen and computation cites. Allocated once, never reused | EM-40 | BR-2 |
| Statement | The rule, short, standing on its own, with nothing of the flow that invokes it | EM-41 | A loan may be renewed no more times than the setting Renewal limit allows. |
| Settings it reads | None; or each, by the name its entry in the catalogue of settings in SDD-04 carries. The statement names the setting and carries no value of it | EM-42 | Renewal limit. The catalogue of settings of the module's shared registers carries no entry of that name yet: a finding against the shared registers, owned by the module's architect, by 30 October 2026. |
| Terms it uses | Every one of them, each already in the glossary or named in the entity model. A term in neither is a finding against the glossary | EM-42 | Loan and Renewal, records of the entity model. |
| What it constrains | The records, attributes or relationships it binds: ____ | EM-42 | The record Renewal: how many rows one loan may have. |
| Where its authority comes from | A statute or instrument with its citation; a published policy; or this organisation's own decision, with the ruling that took it | EM-42 | The library's loan policy, paragraph 5, a published policy. |
| From when it takes effect | A date — and where it has stopped applying, the date it stopped | EM-42 | 1 January 2025. |
| Status | Proposed; in force; withdrawn — and if withdrawn, the date, the reason, and what replaces it | EM-42, EM-43 | In force. |
| What cites it | The use cases, screens and computations citing this identifier. An empty answer is reported as a finding and is not a failure | EM-44 | The use case Renew a loan, UC-LN-02, in its header, at its step 4 and at its extension 4a. |

### BR-3

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Identifier | The stable reference every use case, screen and computation cites. Allocated once, never reused | EM-40 | BR-3 |
| Statement | The rule, short, standing on its own, with nothing of the flow that invokes it | EM-41 | Every loan is confirmed to the member on a ticket. |
| Settings it reads | None; or each, by the name its entry in the catalogue of settings in SDD-04 carries. The statement names the setting and carries no value of it | EM-42 | None. |
| Terms it uses | Every one of them, each already in the glossary or named in the entity model. A term in neither is a finding against the glossary | EM-42 | Loan, a record of the entity model; ticket, in the glossary, withdrawn. |
| What it constrains | The records, attributes or relationships it binds: ____ | EM-42 | The record Loan, at checkout. |
| Where its authority comes from | A statute or instrument with its citation; a published policy; or this organisation's own decision, with the ruling that took it | EM-42 | The library's invitation to tender, section 4.7. |
| From when it takes effect | A date — and where it has stopped applying, the date it stopped | EM-42 | 1 January 2025; it stopped applying on 15 September 2026. |
| Status | Proposed; in force; withdrawn — and if withdrawn, the date, the reason, and what replaces it | EM-42, EM-43 | Withdrawn on 15 September 2026, because the library stopped printing receipts under its paper policy of September 2026; nothing replaces it. |
| What cites it | The use cases, screens and computations citing this identifier. An empty answer is reported as a finding and is not a failure | EM-44 | Nothing. Reported as a finding about the rule, owned by the head of circulation, by 30 October 2026. |

### BR-4

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Identifier | The stable reference every use case, screen and computation cites. Allocated once, never reused | EM-40 | BR-4 |
| Statement | The rule, short, standing on its own, with nothing of the flow that invokes it | EM-41 | A loan still on loan is overdue once the day it is read falls later than its due date by more than the setting Grace period. |
| Settings it reads | None; or each, by the name its entry in the catalogue of settings in SDD-04 carries. The statement names the setting and carries no value of it | EM-42 | Grace period, by the name its entry in the catalogue of settings of the module's shared registers carries. |
| Terms it uses | Every one of them, each already in the glossary or named in the entity model. A term in neither is a finding against the glossary | EM-42 | Loan, a record of the entity model; due date, an attribute of Loan; on loan and overdue, in the glossary. |
| What it constrains | The records, attributes or relationships it binds: ____ | EM-42 | The attribute due date of Loan, as the computation Days overdue reads it. |
| Where its authority comes from | A statute or instrument with its citation; a published policy; or this organisation's own decision, with the ruling that took it | EM-42 | The library's loan policy, paragraph 4, a published policy. |
| From when it takes effect | A date — and where it has stopped applying, the date it stopped | EM-42 | 1 January 2025. |
| Status | Proposed; in force; withdrawn — and if withdrawn, the date, the reason, and what replaces it | EM-42, EM-43 | In force. |
| What cites it | The use cases, screens and computations citing this identifier. An empty answer is reported as a finding and is not a failure | EM-44 | The computation Days overdue of the module's shared registers. |

### BR-5

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Identifier | The stable reference every use case, screen and computation cites. Allocated once, never reused | EM-40 | BR-5 |
| Statement | The rule, short, standing on its own, with nothing of the flow that invokes it | EM-41 | A renewal gives the loan a due date later than the day it is granted by the setting Loan period. |
| Settings it reads | None; or each, by the name its entry in the catalogue of settings in SDD-04 carries. The statement names the setting and carries no value of it | EM-42 | Loan period. The catalogue of settings of the module's shared registers carries no entry of that name yet: the same finding as BR-2's, owned by the module's architect, by 30 October 2026. |
| Terms it uses | Every one of them, each already in the glossary or named in the entity model. A term in neither is a finding against the glossary | EM-42 | Loan and Renewal, records of the entity model; due date, an attribute of Loan. |
| What it constrains | The records, attributes or relationships it binds: ____ | EM-42 | The attribute due date given of Renewal, and so the due date of the loan it extends. |
| Where its authority comes from | A statute or instrument with its citation; a published policy; or this organisation's own decision, with the ruling that took it | EM-42 | The library's loan policy, paragraph 5, a published policy. |
| From when it takes effect | A date — and where it has stopped applying, the date it stopped | EM-42 | 1 January 2025. |
| Status | Proposed; in force; withdrawn — and if withdrawn, the date, the reason, and what replaces it | EM-42, EM-43 | In force. |
| What cites it | The use cases, screens and computations citing this identifier. An empty answer is reported as a finding and is not a failure | EM-44 | The use case Renew a loan, UC-LN-02, in its header and at its step 5. |
