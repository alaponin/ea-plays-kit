---
standard: SDD-02
title: The Requirements Catalogue
edition: "0.3"
document: SDD-02_The_Requirements_Catalogue_v0.3.md
sha256: e01379085ae69764c493da7decfabf2357e07f0ed463490d9ed606abe1cccfe4
produced_by: _working/2026-08-31_requirements_standard/reader_build/build_reader.js at 2026-09-29T09:30:51Z
converted_from: SDD-02_The_Requirements_Catalogue_v0.3.docx sha256 14e6f495bf3b98e429195bb95323db69ca8f1abff00a945fe2045cdeb287d30e (sdd-kit carries its text as Markdown)
---

# SDD-02 · The Requirements Catalogue — the checklist

*Produced from the document named above by `_working/2026-09-28_the_checklists/extract_checklist.py`, as the last step of its build, and never edited by hand. Every line below is the document's own words, read from it, except the lines in italics, which are this program's.*

*Rules counted in the document: 25. The document states "RQR-3 to RQR-29, twenty-five rules" (25).*

*The numbers of its range that carry no rule: RQR-18, RQR-26.*

## Gate — the program's half

### 8. Checking the work — the words before its first subsection

Checking has two halves, and they fail in different ways. One half can eventually be done by a computer program. The other half never can.

### 8.1 What a program will refuse, once such a program exists

> Please read this before the table. No program described below has been written. Nothing here runs today. The list is printed so that an analyst knows what will eventually be read mechanically, and so that whoever writes the program knows what to write. No result of any kind may be reported from this section, and nobody may claim that a register "passes the checks", until the program exists.

| The check | It refuses when |
|---|---|
| Required fields | A required line of section 6 is empty and has no written reason |
| Identifier uniqueness | The same identifier appears twice in one series |
| Identifier reuse | An identifier that once belonged to a withdrawn entry has been given to another |
| Reference resolution | A reference into the register does not resolve, or resolves without reporting the status |
| Group references | A reference names a group of entries rather than one entry |
| Source | A source names no document, or names one without saying where in it |
| Priority values | A priority is not a value of the register's scale |
| Priority attribution | A priority is set and no setter is recorded, or absent and not recorded as not set |
| Status values | A status is not one of the five |
| Setting aside | A set-aside entry has no signature, no date or no reason |
| Parameter names | A parameter name does not resolve in the parameter register. This check cannot be written at all until the parameter register exists |
| Publication | The register does not publish one list in one machine-readable form |
| Test of observation | The sentence is missing, or contains the word "shall" |
| Ordering | The register does not declare its ordering, or declares one with no outside source and no mark saying it was chosen |
| Counts | Nothing. This one reports the counts and never refuses |

## Gate — the person's half

### 8.2 What only a person can judge

No program will ever settle these. A review that skips them has confirmed that the boxes are full, not that the answers are right.

- Is the statement what the client meant, or what the analyst understood?
- Was the paraphrase necessary, or would the client's own sentence have served?
- Is the source the place the requirement really came from, or the nearest place that mentions it?
- Would anybody actually observe what the test of observation describes?
- Did the person who set the priority hold the authority to set it?
- Is the declared ordering the reason the register is arranged this way, or an explanation written afterwards?
- Are these two entries the same requirement? No mechanical method exists for this, and none is proposed here.
- Is the register complete against the client's material? See section 10.

## Form

### 6. The record sheet for one entry

| line | rule |
|---|---|
| Identifier | RQR-6, RQR-15 |
| Kind | RQR-4, RQR-7 |
| Subject | RQR-16 |
| Statement | RQR-8 |
| Paraphrased? | RQR-3 |
| Source | RQR-9 |
| Test of observation | RQR-10 |
| Priority | RQR-11, RQR-19 |
| Set by | RQR-11, RQR-20 |
| Status | RQR-12 |
| If set aside | RQR-21, RQR-22 |
| If amended | RQR-23 |
| Varies by installation? | RQR-13 |
| Recorded gaps | Section 4.4 |

### 7. The record sheet for the register as a whole

| line | rule |
|---|---|
| Ordering | RQR-5 |
| Priority scale | RQR-19 |
| Where variation is described | RQR-13 |
| Parameter register used | RQR-13 |
| Published as | RQR-27 |
| Version, date and status | — |
| Counts, stated and not judged | Section 4.4 |
| Columns never used | Section 4.4 |

## Rules

| rule | words | program |
|---|---|---|
| RQR-3 | Mark any wording that is not the client's | none |
| RQR-4 | Say which of the three kinds each entry | none |
| RQR-5 | Declare how the register is ordered, and where | none |
| RQR-6 | One identifier for each entry, allocated once and | none |
| RQR-7 | Each entry declares its kind | none |
| RQR-8 | Each entry carries the statement in a field | none |
| RQR-9 | Each entry names its source | none |
| RQR-10 | Each entry carries a test of observation | none |
| RQR-11 | Each entry carries a priority, and records who | none |
| RQR-12 | Each entry carries a status | none |
| RQR-13 | Declare where variation is described, and make every | none |
| RQR-14 | An entry contains no design | none |
| RQR-15 | The identifier names the kind and a number, | none |
| RQR-16 | The subject of an entry is a field, | none |
| RQR-17 | An identifier survives renaming, withdrawal and merging | none |
| RQR-19 | One priority scale for the whole register | none |
| RQR-20 | The priority is set by whoever holds the | none |
| RQR-21 | Setting something aside is a status, not a | none |
| RQR-22 | Setting aside is signed, dated and explained, and | none |
| RQR-23 | An entry is amended, never overwritten | none |
| RQR-24 | A withdrawn entry is never deleted, and its | none |
| RQR-25 | A version of the register is its entries | none |
| RQR-27 | Publish the entries as one named list, in | none |
| RQR-28 | Every identifier resolves without the document it appears | none |
| RQR-29 | Every entry can be referred to individually | none |
