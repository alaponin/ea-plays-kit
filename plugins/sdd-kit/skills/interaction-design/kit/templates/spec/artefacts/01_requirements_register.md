<!--
standard: SDD-02
title: The Requirements Catalogue
edition: "0.3"
document: SDD-02_The_Requirements_Catalogue_v0.3.md
sha256: e01379085ae69764c493da7decfabf2357e07f0ed463490d9ed606abe1cccfe4
produced_by: _working/2026-08-31_requirements_standard/reader_build/build_reader.js at 2026-09-29T09:30:51Z
converted_from: SDD-02_The_Requirements_Catalogue_v0.3.docx sha256 14e6f495bf3b98e429195bb95323db69ca8f1abff00a945fe2045cdeb287d30e (sdd-kit carries its text as Markdown)
-->

# The register of requirements

*Written to SDD-02, The Requirements Catalogue, edition 0.3. Produced from the standard by `_working/2026-09-28_the_checklists/extract_checklist.py`, as the last step of its build; a copy of it is filled, and this file is never edited by hand. The quoted lines are the standard's own words.*

## 6. The record sheet for one entry

> Fill this in once for each entry. Every line names the rule that requires it. Where a line has no answer, write the reason there is no answer. An entry is finished when every line has either an answer or a written reason.

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Identifier | The kind, and a number from this register's series for that kind | RQR-6, RQR-15 |  |
| Kind | Function · quality · constraint | RQR-4, RQR-7 |  |
| Subject | The business area or module. As a field, never inside the identifier | RQR-16 |  |
| Statement | The sentence saying what was asked for, in the client's words | RQR-8 |  |
| Paraphrased? | No; or yes, together with the client's own words | RQR-3 |  |
| Source | The client's document · the place in it · the words | RQR-9 |  |
| Test of observation | One sentence, in the language of observation, without "shall" | RQR-10 |  |
| Priority | A value of this register's scale; or not set | RQR-11, RQR-19 |  |
| Set by | The person or role, and the date; or nobody — not set | RQR-11, RQR-20 |  |
| Status | Proposed · in force · amended · withdrawn · set aside | RQR-12 |  |
| If set aside | Who signed it · the date · the reason | RQR-21, RQR-22 |  |
| If amended | What changed · against which version | RQR-23 |  |
| Varies by installation? | No; or the parameter names it depends on, each resolving to one parameter register entry | RQR-13 |  |
| Recorded gaps | Anything unresolved, with a named person and a date | Section 4.4 |  |

## 7. The record sheet for the register as a whole

> Fill this in once for the register.

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Ordering | What the register is ordered on, and the thing outside it the ordering came from; or chosen by the analyst, marked as such | RQR-5 |  |
| Priority scale | The fixed set of values, defined once | RQR-19 |  |
| Where variation is described | A separate variation model, or markers on entries — and where it is kept | RQR-13 |  |
| Parameter register used | Its name and version; or a recorded gap, with a named person, stating that none exists | RQR-13 |  |
| Published as | The name of the list · where it is kept · the form a program reads | RQR-27 |  |
| Version, date and status | As required of every document in this organisation | — |  |
| Counts, stated and not judged | How many entries; how many with no source; how many with no priority setter; how many with a parameter name that does not resolve; how many set aside. State the file each count was made on and when. Set no target for any of them, and do not let anyone infer one | Section 4.4 |  |
| Columns never used | List them. Each is a recorded gap with a named person | Section 4.4 |  |
