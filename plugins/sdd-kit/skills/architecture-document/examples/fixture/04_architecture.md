<!--
standard: SDD-08
title: The Software Architecture Document
edition: "0.1"
document: SDD-08_The_Software_Architecture_Document_v0.1.docx
sha256: a36ad686ee22ea0c1007518fd9f7ebf67aa486e453689b4767e13d9cf656c2f7
produced_by: _working/2026-08-31_architecture_standard/docx_build/build_ar01.js at 2026-09-15T12:19:43Z
-->

# The software architecture specification

*Written to SDD-08, The Software Architecture Document, edition 0.1. Produced from the standard by `_working/2026-09-28_the_checklists/extract_checklist.py`, as the last step of its build; a copy of it is filled, and this file is never edited by hand. The quoted lines are the standard's own words.*

## 7. The form the architect fills

> Six parts. Part 1 is filled once for the application; parts 2 to 5 once for each item of that kind; part 6 once at the end. Every line names the rule that requires it, because a form line whose origin nobody can state is how a form grows until people stop filling it in.

### 7.1 Part 1 — the application, once

#### The lending desk application of the Eastbrook town library

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Application | The name of the one thing this specification covers | ARC-1 | The lending desk application of the Eastbrook town library: members, items and loans at the one desk of the library |
| Version, date, finished | The version, the date, and finished or draft | ARC-2 | Version 1 · 24 September 2026 · finished |
| Platform version | The exact value | ARC-6 | 9.0.7 |
| Edition | The exact value | ARC-6 | enterprise |
| Database | The exact value | ARC-6 | MySQL 8.0 |
| What the edition forbids | Each capability the design would have used and the edition does not allow, with what will be used instead | ARC-7 | Nothing the design would have used: every component named in part 2 is available in the enterprise edition |
| Conventions | Naming, dates, numbering, language — stated once for the whole application | ARC-8 | Dates shown day first as DD/MM/YYYY; identifiers of members as the card number printed on the card; English only; money in euro to two places |
| Documents read | The requirement register, the use case model and the record model this specification was written from, each with its version | ARC-3 | The register of requirements, version 1; the use case model, version 1; the record model, version 1 — all of the Eastbrook town library |

### 7.2 Part 2 — once for each component

#### The search control

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Component and version | Which one, at which version | ARC-9 | The platform's record search control, the version shipped with 9.0.7 |
| Switched on to do | One sentence naming the requirement or use case it serves | ARC-9 | To find one member among the library's members by card number or a fragment of the name, for the use case Lend an item to a member |
| Configured | Once for the whole application, or separately at each place it is used | ARC-10 | Once for the whole application |
| Configuration | The settings, checked against what the component accepts | ARC-12 | Search over the member records; keys: card number, then name; result columns: card number, name, category — each a setting the control accepts |

#### The scheduled job runner

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Component and version | Which one, at which version | ARC-9 | The platform's scheduler, the version shipped with 9.0.7 |
| Switched on to do | One sentence naming the requirement or use case it serves | ARC-9 | To mark each loan overdue on the morning after its due date, for the requirement that overdue loans are shown to the desk |
| Configured | Once for the whole application, or separately at each place it is used | ARC-10 | Separately at each place it is used; there is one |
| Configuration | The settings, checked against what the component accepts | ARC-12 | One job, daily at 06:00 local time, over the loans standing on loan; a setting the scheduler accepts |

The negative list. The platform's payment component is available and deliberately not used: the library takes no payments through the application, and fines are paid at the town hall.

> And once at the end of part 2, the negative list. Each component that was available and is deliberately not used, with the reason in one line. (ARC-11.)

### 7.3 Part 3 — once for each process

#### Lending and return

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Process | Which business process this is | ARC-13 | Lending an item and receiving it back |
| Machinery | Which machinery runs it | ARC-13 | The platform's workflow engine |
| What the machinery decides | The routing and timing choices that belong to the machinery | ARC-14 | The order in which the desk's screens are offered and when the overdue job runs |
| What it does not decide | The business choices that are specified elsewhere and are only carried here | ARC-14 | Who may lend, the loan period and the fine; each is specified in the use case model and the register of business rules and is only carried here |
| States used | Each state the process moves a record through, and confirmation that the record model already has it — or a finding | ARC-15 | on loan, overdue, returned — each already stands in the record model's states of the loan |
| Who changes each state | For each change: a person in a named role, a scheduled job, or an incoming instruction | ARC-16 | on loan: a person, the desk librarian; overdue: the scheduled job; returned: a person, the desk librarian |

### 7.4 Part 4 — once for each crossing

> The longest part of the form, and the one that repays the most care. Figure 3 in section 6 shows the same thing as a picture.

#### The town's register of residents, out

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Direction | In or out | ARC-17 | Out |
| Far side | Which system, organisation or team is on the other end | ARC-17 | The town's register of residents, kept by the town hall of Eastbrook |
| What crosses | Every field, listed individually | ARC-17 | The member's resident number, and back: the resident's name and whether the resident still lives in the town |
| Meaning | What each field means, in words, independent of how it travels | ARC-21 | The resident number identifies one resident of the town; the answer says whether that person may hold a library card |
| Format | The format the fields travel in, written beside the meaning and not merged with it | ARC-21 | A request and a reply in JSON over HTTPS, as the town hall publishes it |
| Issuer | For each borrowed field, who creates and owns it | ARC-18 | The town hall of Eastbrook issues and owns the resident number |
| Name space | Which set of names the value belongs to, so that two identical strings from different sources are not confused | ARC-18 | The town's resident numbers, never the library's card numbers |
| Validity | How long the value stays valid, on the issuer's terms | ARC-18 | A resident number stays valid for the life of the resident; the answer on residence is valid on the day it is given |
| How it is checked | The rule that tells a correct value from an incorrect one | ARC-18 | Nine digits with the town's check digit |
| Freshness shown | How the reader can tell how old the information is | ARC-19 | The date of the last answer is shown beside the member's residence |
| If the value is missing | What the application does. Absence returned as absence is an answer; a substituted default is not, unless the specification says so and says why | ARC-19 | The member is shown as not confirmed, and no default is put in its place |
| If the value is out of date | What the application does. Carrying an old value forward silently is the failure this line exists to prevent | ARC-19 | An answer older than a year is shown as out of date, and the desk asks again |
| If the far side cannot be reached | What the application does, and what the user sees | ARC-19 | The loan goes ahead; the member is shown as not confirmed today, and the desk is told so |
| Must not be stored | What this application may never keep, and how long it may keep anything it is permitted to hold | ARC-20 | The resident's address; only the answer and its date are kept, for one year |
| How both sides check it | What is published, what a test would read, and what a passing result would mean | ARC-22 | The town hall publishes the reply's schema; a test reads a known resident's reply and passes when the name and the answer match |
| Authentication | How the caller is identified, and where the credential is kept — never the credential itself | ARC-23 | A key the town hall issues, kept in the platform's credential store under the name eastbrook-residents; never the key itself |
| If an incoming instruction cannot be carried out | What the application does, what it records, and what fails so that somebody notices | ARC-24 | Not applicable: the crossing is outgoing and carries no instruction in |

### 7.5 Part 5 — once for each bespoke component

#### The fine calculator

| Line | What to write | Rule | Answer |
|---|---|---|---|
| What it is | The component, and what kind of thing it is | ARC-26 | A small program run when an item is returned, which works out the fine due |
| What was tried first | The parts of the model and the catalogue components that were examined, and why each could not express the requirement | ARC-25 | The record model's computed field and the platform's calculation component; neither can read the library's table of fines by category and period |
| Forced by | The requirement, cited, that makes this necessary | ARC-26 | The requirement that the fine is shown to the member at the desk when the item is returned |
| Reads / writes | Which records it reads and which it writes | ARC-27 | Reads the loan, the member's category and the table of fines; writes the fine on the return |
| Wanted elsewhere | Whether another application needs the same thing | ARC-28 | No other application is known to need it |

### 7.6 Part 6 — decisions and findings, once at the end

#### Decisions and findings

| Line | What to write | Rule | Answer |
|---|---|---|---|
| Each decision | What was decided, by whom, on what date, and what would make it wrong | ARC-5, ARC-29, ARC-30 | The search control rather than a drop-down for members, decided by the architect on 24 September 2026; wrong if the library ever has fewer than a hundred members |
| Each finding | The question, a named owner, a date, and what the application does in the meantime | ARC-4 | Whether the town hall's reply may be cached for a day: owner, the town hall's data officer; by 30 September 2026; meanwhile the desk asks once per loan |
| Each withdrawal | What was withdrawn, when, why, and what replaced it | ARC-31 | None withdrawn |
| Counts, stated and not judged | How many crossings; how many carry a freshness answer; how many bespoke entries; how many findings are open. No target is set on any of these and none should be inferred | — | One crossing; one carries a freshness answer; one bespoke entry; one finding open |
