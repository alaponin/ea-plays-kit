<!--
standard: SDD-10
title: The Sector Services Catalogue
edition: "0.1"
document: SDD-10_The_Sector_Services_Catalogue_v0.1.docx
sha256: 2def397fff4d5128b1cab9753a8731394fbf2f752c18edbaeec310c27a262051
produced_by: _working/2026-08-31_house_rebuild/build_house.js at 2026-09-25T07:55:07Z
-->

# The sector's catalogue of services

*Written to SDD-10, The Sector Services Catalogue, edition 0.1. Produced from the standard by `_working/2026-09-28_the_checklists/extract_checklist.py`, as the last step of its build; a copy of it is filled, and this file is never edited by hand. The quoted lines are the standard's own words.*

## 9.1 The row header

> These are the fields every row carries. The survey is generated from them, and the catalogue's completeness and traceability checks run against them. A gap row carries its identifier; a name for what is missing; in its description, what was searched, or which standard or comparison expects the service, and the person who answers for closing the gap; its group; and its source mark. Its other fields read none.

### LIB-S01 · Join the library

| Field | What to record | Rule | Answer |
|---|---|---|---|
| Identifier | The stable reference by which the catalogue knows the row, allocated once and never reused. Its form is declared on the catalogue. | SSC-16 | LIB-S01 |
| Name | An active verb and an object, from the customer's viewpoint, in the sector's words. | SSC-6 | Join the library |
| Description | One line stating the outcome the name stands for. | SSC-4 (M13) | A resident of the county becomes a member of a town library and receives a library card |
| Customer | The one role the service is delivered to, from the catalogue of actors. | SSC-5, SSC-7 | A resident of the county |
| Owning body | The one subject that owes and delivers the service. | SSC-3, SSC-7 | The town library the resident chooses |
| Other parties | Every other party the service involves, each with its kind: supporting, offstage, or counterparty. | SSC-5 | The County Library Service, supporting; the state's register of residents, counterparty |
| Obligation | The identifiers of the register rows the service realises: of the obligations register, with the instrument and section, or of the observed-services register. | SSC-8, SSC-12 | OBL-03 — the County Libraries Act (fictitious), section 4 |
| Source mark | obligation, observed, derived or searched. | SSC-9 | obligation |
| Group | The one group of the organising structure the service realises; its area is the row's package. | SSC-10 | Membership |
| Registers read; registers changed | Two lists, by the names of the vocabulary. | SSC-13 | Read: the register of residents. Changed: the register of members |
| Evidence, output and channel | What the customer presents; what the service produces; the ways it is delivered. | SSC-7, SSC-19 | Evidence: proof of residence. Output: a library card. Channel: at the desk; online |
| State today | How the service is delivered today, from the catalogue's declared list of states; or not established, with the question that would settle it. | SSC-17 | at the desk, on paper |
| Realising system | The system that realises the service, by the identifier the sector's architecture gives it, or none. | SSC-16 | none |
| Stage | The stage of the sector's roadmap in which the service is to be delivered digitally, or not placed. | SSC-18 | Stage 1 |
| Linked rules | The identifiers of the rows of the obligations register that govern the service. | SSC-14 | OBL-03 |
| Relationships | Include, extend or generalisation to another service, with the point named; usually none. | SSC-4 (M11) | none |
| Life events | The events under which the life-event view groups the service, where the catalogue keeps that view. | SSC-15 | Moving into the county |
| Priority | Set by business value, risk and architectural significance, on one scale for the whole catalogue. | SSC-4 (M13, M21) | high |
| Status and format | Draft, reviewed or baselined; and the format, which for a service is the row alone, or the row with a use case model beneath it. | SSC-4 (M21), SSC-19 | reviewed; the row with a use case model beneath it |

### LIB-S02 · Borrow an item

| Field | What to record | Rule | Answer |
|---|---|---|---|
| Identifier | The stable reference by which the catalogue knows the row, allocated once and never reused. Its form is declared on the catalogue. | SSC-16 | LIB-S02 |
| Name | An active verb and an object, from the customer's viewpoint, in the sector's words. | SSC-6 | Borrow an item |
| Description | One line stating the outcome the name stands for. | SSC-4 (M13) | A member takes an item of the library home for a period and brings it back |
| Customer | The one role the service is delivered to, from the catalogue of actors. | SSC-5, SSC-7 | A member of a town library |
| Owning body | The one subject that owes and delivers the service. | SSC-3, SSC-7 | The town library that holds the item |
| Other parties | Every other party the service involves, each with its kind: supporting, offstage, or counterparty. | SSC-5 | none |
| Obligation | The identifiers of the register rows the service realises: of the obligations register, with the instrument and section, or of the observed-services register. | SSC-8, SSC-12 | OBL-05 — the County Libraries Act (fictitious), section 6 |
| Source mark | obligation, observed, derived or searched. | SSC-9 | obligation |
| Group | The one group of the organising structure the service realises; its area is the row's package. | SSC-10 | Lending |
| Registers read; registers changed | Two lists, by the names of the vocabulary. | SSC-13 | Read: the register of members; the catalogue of items. Changed: the register of loans |
| Evidence, output and channel | What the customer presents; what the service produces; the ways it is delivered. | SSC-7, SSC-19 | Evidence: the library card. Output: a loan with its due date. Channel: at the desk |
| State today | How the service is delivered today, from the catalogue's declared list of states; or not established, with the question that would settle it. | SSC-17 | at the desk, on a system |
| Realising system | The system that realises the service, by the identifier the sector's architecture gives it, or none. | SSC-16 | SYS-02, the lending desk application |
| Stage | The stage of the sector's roadmap in which the service is to be delivered digitally, or not placed. | SSC-18 | Stage 1 |
| Linked rules | The identifiers of the rows of the obligations register that govern the service. | SSC-14 | OBL-05; OBL-06 |
| Relationships | Include, extend or generalisation to another service, with the point named; usually none. | SSC-4 (M11) | none |
| Life events | The events under which the life-event view groups the service, where the catalogue keeps that view. | SSC-15 | none |
| Priority | Set by business value, risk and architectural significance, on one scale for the whole catalogue. | SSC-4 (M13, M21) | high |
| Status and format | Draft, reviewed or baselined; and the format, which for a service is the row alone, or the row with a use case model beneath it. | SSC-4 (M21), SSC-19 | reviewed; the row with a use case model beneath it |

### LIB-S03 · Accredit a town library

| Field | What to record | Rule | Answer |
|---|---|---|---|
| Identifier | The stable reference by which the catalogue knows the row, allocated once and never reused. Its form is declared on the catalogue. | SSC-16 | LIB-S03 |
| Name | An active verb and an object, from the customer's viewpoint, in the sector's words. | SSC-6 | Accredit a town library |
| Description | One line stating the outcome the name stands for. | SSC-4 (M13) | The county's board confirms that a town library meets the county's standard of service |
| Customer | The one role the service is delivered to, from the catalogue of actors. | SSC-5, SSC-7 | A town library |
| Owning body | The one subject that owes and delivers the service. | SSC-3, SSC-7 | The County Library Board |
| Other parties | Every other party the service involves, each with its kind: supporting, offstage, or counterparty. | SSC-5 | The County Library Service, supporting |
| Obligation | The identifiers of the register rows the service realises: of the obligations register, with the instrument and section, or of the observed-services register. | SSC-8, SSC-12 | OBL-09 — the County Libraries Act (fictitious), section 11 |
| Source mark | obligation, observed, derived or searched. | SSC-9 | obligation |
| Group | The one group of the organising structure the service realises; its area is the row's package. | SSC-10 | Quality |
| Registers read; registers changed | Two lists, by the names of the vocabulary. | SSC-13 | Read: the register of libraries. Changed: the register of accreditations |
| Evidence, output and channel | What the customer presents; what the service produces; the ways it is delivered. | SSC-7, SSC-19 | Evidence: the library's report of the year. Output: a certificate of accreditation. Channel: by post |
| State today | How the service is delivered today, from the catalogue's declared list of states; or not established, with the question that would settle it. | SSC-17 | not established — does the board still inspect every town library each year? |
| Realising system | The system that realises the service, by the identifier the sector's architecture gives it, or none. | SSC-16 | none |
| Stage | The stage of the sector's roadmap in which the service is to be delivered digitally, or not placed. | SSC-18 | not placed |
| Linked rules | The identifiers of the rows of the obligations register that govern the service. | SSC-14 | OBL-09 |
| Relationships | Include, extend or generalisation to another service, with the point named; usually none. | SSC-4 (M11) | none |
| Life events | The events under which the life-event view groups the service, where the catalogue keeps that view. | SSC-15 | none |
| Priority | Set by business value, risk and architectural significance, on one scale for the whole catalogue. | SSC-4 (M13, M21) | medium |
| Status and format | Draft, reviewed or baselined; and the format, which for a service is the row alone, or the row with a use case model beneath it. | SSC-4 (M21), SSC-19 | draft; the row alone |

### LIB-G01 · Lend an item between town libraries

| Field | What to record | Rule | Answer |
|---|---|---|---|
| Identifier | The stable reference by which the catalogue knows the row, allocated once and never reused. Its form is declared on the catalogue. | SSC-16 | LIB-G01 |
| Name | An active verb and an object, from the customer's viewpoint, in the sector's words. | SSC-6 | Lend an item between town libraries |
| Description | One line stating the outcome the name stands for. | SSC-4 (M13) | Searched: the County Libraries Act and the libraries' published guides; no obligation or practice found. Answers for closing the gap: the county's architect |
| Customer | The one role the service is delivered to, from the catalogue of actors. | SSC-5, SSC-7 | none |
| Owning body | The one subject that owes and delivers the service. | SSC-3, SSC-7 | none |
| Other parties | Every other party the service involves, each with its kind: supporting, offstage, or counterparty. | SSC-5 | none |
| Obligation | The identifiers of the register rows the service realises: of the obligations register, with the instrument and section, or of the observed-services register. | SSC-8, SSC-12 | none |
| Source mark | obligation, observed, derived or searched. | SSC-9 | searched |
| Group | The one group of the organising structure the service realises; its area is the row's package. | SSC-10 | Lending |
| Registers read; registers changed | Two lists, by the names of the vocabulary. | SSC-13 | none |
| Evidence, output and channel | What the customer presents; what the service produces; the ways it is delivered. | SSC-7, SSC-19 | none |
| State today | How the service is delivered today, from the catalogue's declared list of states; or not established, with the question that would settle it. | SSC-17 | not established |
| Realising system | The system that realises the service, by the identifier the sector's architecture gives it, or none. | SSC-16 | none |
| Stage | The stage of the sector's roadmap in which the service is to be delivered digitally, or not placed. | SSC-18 | not placed |
| Linked rules | The identifiers of the rows of the obligations register that govern the service. | SSC-14 | none |
| Relationships | Include, extend or generalisation to another service, with the point named; usually none. | SSC-4 (M11) | none |
| Life events | The events under which the life-event view groups the service, where the catalogue keeps that view. | SSC-15 | none |
| Priority | Set by business value, risk and architectural significance, on one scale for the whole catalogue. | SSC-4 (M13, M21) | none |
| Status and format | Draft, reviewed or baselined; and the format, which for a service is the row alone, or the row with a use case model beneath it. | SSC-4 (M21), SSC-19 | draft; the row alone |

The catalogue's declarations, stated once for the fixture. The sector is the public library services of the county of Eastbrook, which does not exist; inside its one boundary stand three bodies — the County Library Service, the County Library Board and the town libraries — and at the boundary stands the state's register of residents, a counterparty. One architect, the county's architect, answers for the catalogue. The structure it is organised by is the county's map of library capabilities, whose groups are Membership, Lending and Quality. The two registers are the obligations register (OBL-n) and the observed-services register (OBS-n), each a named list. The closed lists are the four source marks, the states today (at the desk, on paper; at the desk, on a system; online; not established), the stages (Stage 1, Stage 2, not placed) and the groups, each declared from the county's map.

> This header is the catalogue's record of the service. It is written once for each row and it is read by machine: the survey is generated from it, and the catalogue's checks run against it. A value that appears both here and in prose about the service will come to disagree with itself. State it here only.
