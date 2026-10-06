<!--
standard: SDD-08
title: The Software Architecture Document
edition: "1.0"
document: SDD-08_The_Software_Architecture_Document_v1.0.md
sha256: 762846a7ae4bcc3d041cc04194a987c8cab1845c2e51e9aa08f57775ea6aba5f
produced_by: _working/2026-08-31_architecture_standard/docx_build/build_ar01.js at 2026-09-29T20:23:07Z
converted_from: SDD-08_The_Software_Architecture_Document_v1.0.docx sha256 e54fd381fb4da70eda91833310ec36eea5ff4d17edabec1b25f547a7452f4b48 (sdd-kit carries its text as Markdown)
-->

# The software architecture specification

*Written to SDD-08, The Software Architecture Document, edition 1.0. Produced from the standard by `_working/2026-09-28_the_checklists/extract_checklist.py`, as the last step of its build; a copy of it is filled, and this file is never edited by hand. The quoted lines are the standard's own words.*

## 7. The form the architect fills

> Six parts. Part 1 is filled once for the application; parts 2 to 5 once for each item of that kind; part 6 once at the end. Every line names the rule that requires it, because a form line whose origin nobody can state is how a form grows until people stop filling it in.

### 7.1 Part 1 — the application, once

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Application | The name of the one thing this specification covers | ARC-1 |  |
| Version, date, finished | The version, the date, and finished or draft | ARC-2 |  |
| Platform version | The exact value | ARC-6 |  |
| Edition | The exact value | ARC-6 |  |
| Database | The exact value | ARC-6 |  |
| What the edition forbids | Each capability the design would have used and the edition does not allow, with what will be used instead | ARC-7 |  |
| Conventions | Naming, dates, numbering, language — stated once for the whole application | ARC-8 |  |
| Documents read | The requirement register, the use case model and the record model this specification was written from, each with its version | ARC-3 |  |

### 7.2 Part 2 — once for each component

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Component and version | Which one, at which version | ARC-9 |  |
| Switched on to do | One sentence naming the requirement or use case it serves | ARC-9 |  |
| Configured | Once for the whole application, or separately at each place it is used | ARC-10 |  |
| Configuration | The settings, checked against what the component accepts | ARC-12 |  |

> And once at the end of part 2, the negative list. Each component that was available and is deliberately not used, with the reason in one line. (ARC-11.)

### 7.3 Part 3 — once for each process

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Process | Which business process this is | ARC-13 |  |
| Machinery | Which machinery runs it | ARC-13 |  |
| What the machinery decides | The routing and timing choices that belong to the machinery | ARC-14 |  |
| What it does not decide | The business choices that are specified elsewhere and are only carried here | ARC-14 |  |
| States used | Each state the process moves a record through, and confirmation that the record model already has it — or a finding | ARC-15 |  |
| Who changes each state | For each change: a person in a named role, a scheduled job, or an incoming instruction | ARC-16 |  |

### 7.4 Part 4 — once for each crossing

> The longest part of the form, and the one that repays the most care. Figure 3 in section 6 shows the same thing as a picture.

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Direction | In or out | ARC-17 |  |
| Far side | Which system, organisation or team is on the other end | ARC-17 |  |
| What crosses | Every field, listed individually | ARC-17 |  |
| Meaning | What each field means, in words, independent of how it travels | ARC-21 |  |
| Format | The format the fields travel in, written beside the meaning and not merged with it | ARC-21 |  |
| Issuer | For each borrowed field, who creates and owns it | ARC-18 |  |
| Name space | Which set of names the value belongs to, so that two identical strings from different sources are not confused | ARC-18 |  |
| Validity | How long the value stays valid, on the issuer's terms | ARC-18 |  |
| How it is checked | The rule that tells a correct value from an incorrect one | ARC-18 |  |
| Freshness shown | How the reader can tell how old the information is | ARC-19 |  |
| If the value is missing | What the application does. Absence returned as absence is an answer; a substituted default is not, unless the specification says so and says why | ARC-19 |  |
| If the value is out of date | What the application does. Carrying an old value forward silently is the failure this line exists to prevent | ARC-19 |  |
| If the far side cannot be reached | What the application does, and what the user sees | ARC-19 |  |
| Must not be stored | What this application may never keep, and how long it may keep anything it is permitted to hold | ARC-20 |  |
| How both sides check it | What is published, what a test would read, and what a passing result would mean | ARC-22 |  |
| Authentication | How the caller is identified, and where the credential is kept — never the credential itself | ARC-23 |  |
| If an incoming instruction cannot be carried out | What the application does, what it records, and what fails so that somebody notices | ARC-24 |  |

### 7.5 Part 5 — once for each bespoke component

| Line | What to write | Rule | Answer |
|---|---|---|---|
| What it is | The component, and what kind of thing it is | ARC-26 |  |
| What was tried first | The parts of the model and the catalogue components that were examined, and why each could not express the requirement | ARC-25 |  |
| Forced by | The requirement, cited, that makes this necessary | ARC-26 |  |
| Reads / writes | Which records it reads and which it writes | ARC-27 |  |
| Wanted elsewhere | Whether another application needs the same thing | ARC-28 |  |

### 7.6 Part 6 — decisions and findings, once at the end

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Each decision | What was decided, by whom, on what date, and what would make it wrong | ARC-5, ARC-29, ARC-30 |  |
| Each finding | The question, a named owner, a date, and what the application does in the meantime | ARC-4 |  |
| Each withdrawal | What was withdrawn, when, why, and what replaced it | ARC-31 |  |
| Counts, stated and not judged | How many crossings; how many carry a freshness answer; how many bespoke entries; how many findings are open. No target is set on any of these and none should be inferred | — |  |
