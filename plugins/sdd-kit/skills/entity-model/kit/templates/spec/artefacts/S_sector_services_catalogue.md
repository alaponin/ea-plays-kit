<!--
standard: SDD-10
title: The Sector Services Catalogue
edition: "0.1"
document: SDD-10_The_Sector_Services_Catalogue_v0.1.md
sha256: 39d7a84bac89de782cc46b36b3783ad6d780e2ee4d88ebc6c60009b01233f06d
produced_by: _working/2026-08-31_house_rebuild/build_house.js at 2026-09-25T07:55:07Z
converted_from: SDD-10_The_Sector_Services_Catalogue_v0.1.docx sha256 2def397fff4d5128b1cab9753a8731394fbf2f752c18edbaeec310c27a262051 (sdd-kit carries its text as Markdown)
-->

# The sector's catalogue of services

*Written to SDD-10, The Sector Services Catalogue, edition 0.1. Produced from the standard by `_working/2026-09-28_the_checklists/extract_checklist.py`, as the last step of its build; a copy of it is filled, and this file is never edited by hand. The quoted lines are the standard's own words.*

## 9.1 The row header

> These are the fields every row carries. The survey is generated from them, and the catalogue's completeness and traceability checks run against them. A gap row carries its identifier; a name for what is missing; in its description, what was searched, or which standard or comparison expects the service, and the person who answers for closing the gap; its group; and its source mark. Its other fields read none.

| Field | What to record | Rule | Answer |
|---|---|---|---|
| Identifier | The stable reference by which the catalogue knows the row, allocated once and never reused. Its form is declared on the catalogue. | SSC-16 |  |
| Name | An active verb and an object, from the customer's viewpoint, in the sector's words. | SSC-6 |  |
| Description | One line stating the outcome the name stands for. | SSC-4 (M13) |  |
| Customer | The one role the service is delivered to, from the catalogue of actors. | SSC-5, SSC-7 |  |
| Owning body | The one subject that owes and delivers the service. | SSC-3, SSC-7 |  |
| Other parties | Every other party the service involves, each with its kind: supporting, offstage, or counterparty. | SSC-5 |  |
| Obligation | The identifiers of the register rows the service realises: of the obligations register, with the instrument and section, or of the observed-services register. | SSC-8, SSC-12 |  |
| Source mark | obligation, observed, derived or searched. | SSC-9 |  |
| Group | The one group of the organising structure the service realises; its area is the row's package. | SSC-10 |  |
| Registers read; registers changed | Two lists, by the names of the vocabulary. | SSC-13 |  |
| Evidence, output and channel | What the customer presents; what the service produces; the ways it is delivered. | SSC-7, SSC-19 |  |
| State today | How the service is delivered today, from the catalogue's declared list of states; or not established, with the question that would settle it. | SSC-17 |  |
| Realising system | The system that realises the service, by the identifier the sector's architecture gives it, or none. | SSC-16 |  |
| Stage | The stage of the sector's roadmap in which the service is to be delivered digitally, or not placed. | SSC-18 |  |
| Linked rules | The identifiers of the rows of the obligations register that govern the service. | SSC-14 |  |
| Relationships | Include, extend or generalisation to another service, with the point named; usually none. | SSC-4 (M11) |  |
| Life events | The events under which the life-event view groups the service, where the catalogue keeps that view. | SSC-15 |  |
| Priority | Set by business value, risk and architectural significance, on one scale for the whole catalogue. | SSC-4 (M13, M21) |  |
| Status and format | Draft, reviewed or baselined; and the format, which for a service is the row alone, or the row with a use case model beneath it. | SSC-4 (M21), SSC-19 |  |

> This header is the catalogue's record of the service. It is written once for each row and it is read by machine: the survey is generated from it, and the catalogue's checks run against it. A value that appears both here and in prose about the service will come to disagree with itself. State it here only.
