<!--
standard: SDD-03
title: The Entity Model
edition: "0.6"
document: SDD-03_The_Entity_Model_v0.6.docx
sha256: 137b5c4b50c3509b042da74e1306c5bd8053173d70e7eea21e08a95a29e4def0
produced_by: _working/2026-08-31_house_rebuild/build_house.js at 2026-09-29T09:30:52Z
-->

# The glossary

*Written to SDD-03, The Entity Model, edition 0.6. Produced from the standard by `_working/2026-09-28_the_checklists/extract_checklist.py`, as the last step of its build; a copy of it is filled, and this file is never edited by hand. The quoted lines are the standard's own words.*

**The glossary's heading.** The glossary of the entity model of the loans module of the Eastbrook library system, `02_entity_model.md`, beside it. Version 0.2 · 22 September 2026.

## 5.4 For each glossary entry

### On loan

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Term | The one name this model uses for the concept | EM-34, EM-37 | On loan |
| Definition | What the thing is. Singular, standing on its own, not repeating the name, carrying no rationale and no procedure | EM-36 | The status of a loan whose copy has left the library with the member and has not come back. |
| Why it is not a record | The system keeps no rows of it. Where it does keep rows of it, the entry is deleted and the entity model names it instead | EM-35 | The system keeps no rows of it: it is a status a loan is in, declared among the loan's states in the module's shared registers. |
| Other names for it | ____ — every other name a reader may arrive with, including the one an older document used | EM-37 | Out, the counter's own word. |
| Where the term comes from | The instrument, the published vocabulary, or this organisation — and for an instrument, its citation | EM-36, EM-39 | The library's loan policy, paragraph 2. |
| Drawn from legislation | No; or yes, reproduced as the instrument has it, cited ____ , with the working word recorded as another name | EM-39 | No. |
| Status | Proposed; in use; withdrawn — and if withdrawn, the date, the reason, and what replaces it | EM-36, EM-38 | In use. |
| Where it is used | The records, use cases or rules relying on it: ____ | EM-36 | The record Loan; the rule BR-1; the use case Renew a loan. |

### Overdue

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Term | The one name this model uses for the concept | EM-34, EM-37 | Overdue |
| Definition | What the thing is. Singular, standing on its own, not repeating the name, carrying no rationale and no procedure | EM-36 | The condition of a loan still on loan after the day the rule BR-4 fixes. |
| Why it is not a record | The system keeps no rows of it. Where it does keep rows of it, the entry is deleted and the entity model names it instead | EM-35 | The system keeps no rows of it: it is worked out when a loan is read, by the computation Days overdue of the module's shared registers. |
| Other names for it | ____ — every other name a reader may arrive with, including the one an older document used | EM-37 | Late, the word of the library's leaflet for members. |
| Where the term comes from | The instrument, the published vocabulary, or this organisation — and for an instrument, its citation | EM-36, EM-39 | The library's loan policy, paragraph 4. |
| Drawn from legislation | No; or yes, reproduced as the instrument has it, cited ____ , with the working word recorded as another name | EM-39 | No. |
| Status | Proposed; in use; withdrawn — and if withdrawn, the date, the reason, and what replaces it | EM-36, EM-38 | In use. |
| Where it is used | The records, use cases or rules relying on it: ____ | EM-36 | The rule BR-4; the computation Days overdue. |

### Counter clerk

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Term | The one name this model uses for the concept | EM-34, EM-37 | Counter clerk |
| Definition | What the thing is. Singular, standing on its own, not repeating the name, carrying no rationale and no procedure | EM-36 | A member of the library's staff who serves members at the counter of a branch. |
| Why it is not a record | The system keeps no rows of it. Where it does keep rows of it, the entry is deleted and the entity model names it instead | EM-35 | The loans module keeps no rows of the library's staff; who holds the part is kept in the town's directory of staff. |
| Other names for it | ____ — every other name a reader may arrive with, including the one an older document used | EM-37 | Desk assistant, the title the job descriptions of 2019 used. |
| Where the term comes from | The instrument, the published vocabulary, or this organisation — and for an instrument, its citation | EM-36, EM-39 | This organisation: the library's staffing plan of 2024. |
| Drawn from legislation | No; or yes, reproduced as the instrument has it, cited ____ , with the working word recorded as another name | EM-39 | No. |
| Status | Proposed; in use; withdrawn — and if withdrawn, the date, the reason, and what replaces it | EM-36, EM-38 | In use. |
| Where it is used | The records, use cases or rules relying on it: ____ | EM-36 | The move of a loan from on loan to returned, in the module's shared registers. |

### Ticket

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Term | The one name this model uses for the concept | EM-34, EM-37 | Ticket |
| Definition | What the thing is. Singular, standing on its own, not repeating the name, carrying no rationale and no procedure | EM-36 | The paper slip once handed to a member at checkout, naming the copy and its due date. |
| Why it is not a record | The system keeps no rows of it. Where it does keep rows of it, the entry is deleted and the entity model names it instead | EM-35 | The system keeps no rows of it, and never did. |
| Other names for it | ____ — every other name a reader may arrive with, including the one an older document used | EM-37 | Receipt, the word of the library's invitation to tender, section 4.7. |
| Where the term comes from | The instrument, the published vocabulary, or this organisation — and for an instrument, its citation | EM-36, EM-39 | The library's invitation to tender, section 4.7. |
| Drawn from legislation | No; or yes, reproduced as the instrument has it, cited ____ , with the working word recorded as another name | EM-39 | No. |
| Status | Proposed; in use; withdrawn — and if withdrawn, the date, the reason, and what replaces it | EM-36, EM-38 | Withdrawn on 15 September 2026, because the library stopped printing receipts under its paper policy of September 2026; nothing replaces it. |
| Where it is used | The records, use cases or rules relying on it: ____ | EM-36 | Nothing since it was withdrawn; the withdrawn rule BR-3 used it. |
