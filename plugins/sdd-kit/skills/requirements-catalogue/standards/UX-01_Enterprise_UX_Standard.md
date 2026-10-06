# UX-01 · Enterprise UX Standard for Public-Sector Back-Office Systems

*This copy is carried by sdd-kit, the SDD method's skills for the service design course. It keeps the edition stated below; where the edition drew an example from the method's author's own client work, this copy carries an example set in Progressa in its place and says so where it does.*

| **Volume** | UX-01 · UI/UX principles and binding rules for enterprise public-sector systems |
| --- | --- |
| **Status** | **v1.3 — consolidated + evidence rounds 1–2.** Absorbs Amendment A1 (MDM implications) and Amendment A2 (TA 3.0 implications) into the base standard, and adds three families closing the declared gaps: ACC (accessibility), CNT (content & notices), DSH (dashboards & analytical views). v1.2 folded in the Round-1 vendor deltas (selection-control ladder, list hardenings, search distinction); v1.3 folds in the Round-2 government-source deltas (UX-03 §7): persona-specific density, the audit Timeline precedent, and five openly-licensed Annex-D patterns. Component-level patterns are routed to Annex D, not the rules. 99 rules in 16 families. Rules marked ⚑ are provisional on the MDM ADD §10 open decisions (D-1…D-5) and register FLAGs. |
| **Author** | FiscalAdmin OÜ · Aare Lapõnin |
| **Date** | 13 July 2026 |
| **Companion** | UX-02 v1.3 · the condensed generation ruleset for AI-assisted implementation (CLAUDE.md section or skill) |
| **Sources** | S2C-01 Platform Architecture v0.9 · the module requirement specifications of the programme it was first written for · that programme's master-data architecture design and master-data register · TA30 Digital Transformation Principles (OECD TA 3.0 derivation) · a tax-administration white paper · UX-03 Public-Source Catalogue (verified evidence rounds 1–2: SAP Fiori / SLDS 2 / Pega / ServiceNow; GOV.UK / MoJ / Home Office / DWP / USWDS). Government-source text adapted under OGL v3.0 / CC0 — see Annex D. Round 3 deprioritised per Annex C. |
| **Relationship** | Supplies the platform-invariant rules for what a person sees. Binds to the screen specification of the use case description (S2C-04 §7.3) and to the screen set of WF-01 (W8, W10, W14, W15). Rule identifiers are citable from screen records, use case descriptions, CADs, FISs and application models. *Restated 31 August 2026: the previous wording bound this standard to the nine interrogation dimensions of S2C-01 §5, which S2C-04 re-grained on 13 August 2026 from a filing system into a disposition list; the binding pointed at a section that no longer said what it used to.* |

**In one sentence:** an officer-facing screen is a governed view over data the system already holds, at national scale, with legal effect — every field, lookup, list and action on it must be *derivable* from that premise; the interaction itself must first *earn its existence* against automation; and where automation acts, the screen must explain it and make it contestable.

**Change log**

| Version | Change |
| --- | --- |
| v1.0 (13.07.2026) | Initial standard: 5 premises, principles P1–P10, 51 rules in 10 families, Screen Design Protocol Q1–Q8, anti-patterns AP-01–14, TA annex, adoption & U001–U010 |
| v1.1 (13.07.2026) | Consolidates A1 (MDM family, 15 rules; 10 amendments) and A2 (AUT 8 + TPX 7 rules; Q0 existence gate; AP-15–19; 10 amendments); adds premise 6, principles P11–P12; adds ACC (6), CNT (6), DSH (6); U-series extended to U024; Annex C source lineage. Amendments A1/A2 remain in project knowledge as decision records; this text supersedes them. |
| v1.2 (13.07.2026) | Evidence round 1 (UX-03): IDR-05 gains the numeric selection-control ladder (tunable defaults) and the global-vs-in-context search note (IDR-05a); WRK-04/05 gain the never-open-empty and filter-summary-integrity hardenings. Component-level vendor patterns (Fiori message-control catalogue, SLDS search numerics, Pega case anatomy) routed to new Annex D as pattern-library inputs, not rules; corroboration and the confirmed public-source gaps recorded there. No rule renumbering; family/rule count unchanged. |
| v1.3 (13.07.2026) | Evidence round 2 (UX-03 §7, government sources): PRD-03 + TPX-01 sharpened to make screen density persona-specific (dense expert officer UX vs citizen one-thing-per-page), cited to DWP/MoJ; AUD-03 gains the MoJ Timeline precedent (display side), with the audit *control* side (AUD-02) recorded as UX-01-original. Five openly-licensed component patterns added to Annex D (D.5–D.9); OGL v3.0 attribution recorded there. Round 3 deprioritised. No rule renumbering; family/rule count unchanged. |
| v1.3, amended 25.09.2026 | IDR-05 amended on the owner's word of 25 September 2026 (ruling `long-lists-are-chosen-by-category`; METHOD-2026-09-25-04, item 7): no step of a selection offers more than nine values, and seven is the aim; a list of values with more than nine values in force is divided into categories of no more than nine, chosen category first, then the value; more than nine categories add another level. For a list of values this replaces the ladder's two lowest bands; the bands for record sets that grow with operations stand. Annex B.1 gains U025 and U026, the kit's lints for CTX-01 and for the amended IDR-05. No rule renumbering; family/rule count unchanged. |
| v1.3, amended 25.09.2026 (TRM-02) | TRM-02 amended on the owner's word of 25 September 2026 (the lists-of-values round, METHOD-2026-09-25-02; recorded by METHOD-2026-09-25-01, item 13): a coded value shows its label only, unless its list is marked `display_code`, where it shows its code; the rule had rendered "code — label". The code is stored as before. No rule renumbering; family/rule count unchanged. |

---

## 1. Purpose and how to use this standard

**The failure mode this standard removes.** AI-assisted (and junior-developer) screen generation defaults to the *consumer web-form archetype*: blank questionnaires that ask the user to type what the system knows, free-text where selection is required, ten-row demo lists, generic Edit/Save/Delete verbs on records that have lifecycles, approval clicks on decisions a rule already took. Two measured examples from the build of a case-management module: a case screen expecting the taxpayer to be entered **by name** (in a register of millions, where names are never unique), and a debt case whose debt lines were **typed in by the officer** although every line already exists in taxpayer accounting and the module's requirements ask for cases created *from* those balances.

All such failures are instances of **one root error: designing the screen as if it were the origin of the data and the decision, when it is a view over data that already exists and automation that already ran.** Everything in this standard is a consequence of correcting that premise. Generic UX advice does not correct it; concrete, testable rules wired into the design and generation workflow do.

**Three uses.**

1. **Design input.** During specification, the rules act as forced questions and defaults — the platform-invariant half of Dimension 7 (S2C-01 §5). The Screen Design Protocol (§5) is run for every screen before it is specified, starting with the existence test (Q0).
2. **Generation constraint.** During implementation, an AI assistant or generator must satisfy the rules. UX-02 is the condensed, imperative extract for exactly this purpose.
3. **Review instrument.** A generated or hand-built screen is graded against the rule index (Appendix) and the anti-pattern catalogue (§6); findings cite rule IDs.

**Enforcement classes.** Following the mechanization gate of S2C-01 §12.3, every rule carries one of three classes — a rule that cannot fail a build is merely advice:

| Class | Meaning | Where it lands |
| --- | --- | --- |
| **[LINT]** | Mechanizable as a validation rule over the spec/model — can fail authoring | U-series candidates, Annex B.1 |
| **[GEN]** | A generator / pattern-library obligation — fixed once in the pattern, inherited by every screen | UX pattern library, Annex B.1 |
| **[REV]** | Judgement call — review-checklist item for humans or an AI self-review pass | UX-02 checklist, Annex B.2 |

---

## 2. The operating premises

Six facts distinguish public-sector back-office systems from consumer web applications and from CRUD demos. Every rule follows from at least one of them; when in doubt about a design choice, return here.

**Premise 1 — Scale is national.** Registers hold 10⁵–10⁷ parties, ledgers hold 10⁷–10⁹ transactions, and both only grow. Any design gesture that assumes the record set fits in a dropdown, a page, or a human memory is wrong from the first day, even if the DEV database has forty rows. Design for the millionth record.

**Premise 2 — The data mostly exists, across the whole of government.** A tax administration's facts are born in registers, ledgers, filings, third-party feeds and interfaces — registration data comes from primary registers "without any intervention of taxpayers" (TA white paper §6.2), and the once-only principle (TA 3.0) extends the boundary: a fact held by *any connected government register or feed* counts as known. Officer screens rarely *create* primary data; they **view, select, decide and annotate**. A screen dominated by empty input boxes is almost always a specification failure.

**Premise 3 — Users are professionals inside a workflow.** Officers use these screens hundreds of times a day, trained, under caseload and SLA. Efficiency, consistency and keyboard speed dominate; first-visit discoverability is secondary. Work *arrives* through queues and events; officers do not browse for it.

**Premise 4 — Acts have legal effect.** A status change, an assessment, a write-off is an administrative act: attributable to a person, dated, reasoned, and reversible only by a further act — never by editing history. The UI must *enforce* this, not merely record it.

**Premise 5 — The organisation outlives the software.** Terminology, codes, periods and formats come from law and national registries and will be read by auditors years later, possibly in another language. Labels, vocabularies and retention are governed data, not developer choices.

**Premise 6 — Automation is the default; humans handle exceptions.** In the target operating model (TA 3.0), rule-expressible steps run without human interruption; officers see the minority of cases where judgement genuinely adds value. Screens therefore serve exceptions, decisions and assurance — a human step that merely confirms what a rule determined is a defect of the process, and its screen a defect of the design.

---

## 3. The twelve principles

**P1 — The system already knows.** Never ask a user for anything the system — or any connected government register or feed — holds or can derive. Every screen is a view over an existing data model; input is the exception, reserved for facts that genuinely enter the organisation at this moment, through this person.

**P2 — Identify by identifier; display by name.** Humans have names; records have keys. A record is *found* by its identifier or by attribute search, *chosen* from a result list, *shown* with its human-readable identity, and *stored* as a key. Typing a name into a reference field is transcription, and transcription is how wrong parties get enforced against.

**P3 — Design for the millionth record.** Every list paginates server-side, every search is bounded and indexed, every dropdown is finite by construction. If a control's content scales with the register, the control is wrong.

**P4 — Work arrives in queues.** The officer's day starts at a worklist scoped to them, ordered by what the administration wants done first. Navigation exists for the exceptions; the queue is the norm.

**P5 — Context is loaded, not reassembled.** Opening a case loads the party, the figures, the history, the related records — the officer never re-assembles context the record already implies, and never re-searches what is already on screen.

**P6 — The lifecycle is the interface.** What a user can do to a record is exactly the set of declared transitions allowed for their role in the record's current state. Buttons are transitions; there is no generic Edit on a record of legal effect.

**P7 — Money is computed, never typed.** Balances, arrears, interest, penalties, totals and ages originate in the accounting and computation layer and render read-only. A typed amount is confined to the boundary where an external fact first enters the system — and corrections are new transactions, never edits.

**P8 — Every act has an author and a reason.** Who, when, what, under which authority — always; and any discretionary act carries a reason code. Discretion without a reason is arbitrariness; the UI makes the reason a precondition, not an afterthought.

**P9 — Errors explain and unblock.** A validation message names the rule, shows the offending value, and states the remedy. The system never discards work, never fails silently, and never leaves the officer with "Invalid input" and a cleared form.

**P10 — The law writes the labels.** Field names, action names, codes, periods and formats come from statutory and administrative vocabulary — resolved from the reference kernel as-at the relevant date, rendered consistently and multilingually. Developers (and AI assistants) do not invent domain terminology.

**P11 — The interaction must earn its existence.** The best screen is often no screen. An interaction that re-collects what government already holds, confirms what a rule already determined, or presents a report where a decision workflow belongs, should not be designed — it should be designed *away*. (Logically this principle precedes all others; it is numbered here to preserve citation stability.)

**P12 — Automation explains itself.** Every automated determination a person meets — assessment, flag, hold, routing — must be able to say what it decided, on which data, under which rule version, and how it can be challenged. Explanation and contestability are part of the outcome, not documentation about it.

---

## 4. The binding rules

Ninety-nine rules in sixteen families. Each rule: identifier, enforcement class, statement, and — where load-bearing — a wrong/right pair. Rules use MUST / NEVER deliberately. Text integrating former Amendments A1/A2 is not separately marked; the change log and the retained amendment documents carry the lineage.

### 4.1 IDR — Identification, search and reference

**IDR-01 [GEN] Reference is selection, never transcription.** Any field whose value refers to another record — a party, a case, a document, an employer, a property — MUST be captured by selecting from a search or lookup result and stored as the internal key. Free-text entry of a name or description *as the reference* is forbidden.

> ✗ `Taxpayer name: [___________]` on a case form
> ✓ `Taxpayer: [🔍 search]` → result list → selection → identity card (TIN · name · type · status), FK stored

**IDR-02 [GEN] Identifier-first, across all registered identifiers.** The primary search path is the unique identifier — TIN, case number, document number, or any identifier registered in the party cross-reference (national ID, VAT number, EORI, per the identifier-type reference R-18) — validated at entry against its scheme (length, format, check digit) with the scheme rule named on failure. Results show which identifier matched. Deterministic exact matches MAY auto-select; any probabilistic match (per `resolve_party` confidence) ALWAYS presents candidates for explicit confirmation.

**IDR-03 [GEN] Attribute search is the fallback, and it is smart.** Where no identifier is at hand, the user searches by combinable partial attributes (name fragment, date of birth, region, status, address fragment), executed server-side, returning a disambiguation list whose columns distinguish homonyms (identifier, full name, type, status, distinguishing attribute). The user selects; with multiple matches the system NEVER auto-picks.

**IDR-04 [GEN] The identity card is the golden record.** A selected party renders as a compact identity block — identifier, name, type, status, key flags — sourced from the reconciled golden record, carrying a visible flag when the party has open master-data conflicts. Never text sitting in an input box; a wrong selection is corrected by re-searching, never by editing the displayed text.

**IDR-05 [LINT] Bounded sets in dropdowns; unbounded sets in search.** Dropdowns, radio groups and checklists are reserved for reference data of bounded, stable size. The selection-control ladder sets the mechanism by cardinality — **tunable defaults, not physics** (these are the SAP/Salesforce settings confirmed by UX-03; adjust per deployment): **≤ ~12 → radio group or select · ~13–200 → combo box with type-to-filter and validation · ~200–1,000 → input with server-side suggestions · > ~1,000, or multi-attribute / conditional search → a full search (value-help) dialog.** Always start with the least complex control that fits. **A list of values is chosen in steps of no more than nine** (amended 25 September 2026 on the owner's word; ruling `long-lists-are-chosen-by-category`): no step of a selection offers more than nine values, and seven is the aim. A list of values with more than nine values in force is divided into categories of no more than nine; the person chooses the category first, then the value within it; with more than nine categories, another level is added. The categories are themselves a list of values, maintained like any other, and each value names its category. For a list of values this replaces the ladder's two lowest bands (≤ ~12 and ~13–200); the bands for record sets that grow with operations stand as written. Any entity set that grows with operations — parties, cases, documents, addresses, properties, bank accounts — is by definition in the top band and MUST use a search dialog or server-side type-ahead with a minimum character threshold, a result cap, and a "refine your search" message.

*Note — two searches, two patterns (IDR-05a [REV]).* Searching *for a record* (global find; navigates away) and searching *within an on-screen list* (narrowing what is already shown) are different patterns and MUST NOT be built the same. Global find: recent items on focus, top matches as you type without Enter, disambiguation by icon/type + name + a distinguishing attribute. In-list narrowing: the search input is exposed (never behind an icon), filters on every keystroke, declares its scope in the placeholder ("Search this list…"), and shows no autocomplete dropdown — the user is refining, not navigating. (UX-03: Fiori list report vs worklist; SLDS global vs in-context search.)

**IDR-06 [REV] Names are attributes, never keys.** No joining, matching, de-duplication or uniqueness logic on names anywhere in the design. Homonyms are normal data, not edge cases.

**IDR-07 [GEN] No-hit is not a dead end.** A failed search offers the legitimate next steps — widen the criteria, verify the source document, initiate registration through the proper flow if authorised, or escalate — but never "just type it in anyway".

### 4.2 PRE — Field provenance and pre-fill

**PRE-01 [LINT] The provenance law.** Every field on every screen MUST declare exactly one provenance:

| Provenance | Meaning |
| --- | --- |
| `system` | generated by the system (IDs, timestamps, sequence numbers) |
| `derived` | computed from other data (totals, ages, categories, statuses) |
| `source` | pre-filled from the triggering / related record (the return, the ledger position, the application) |
| `master` | pre-filled from master or reference data — the golden record / kernel catalogue via the sanctioned access path |
| `selected` | chosen by the user from a lookup or search over existing records |
| `entered` | typed by the user — a fact that exists nowhere in the system |
| `external` | captured from an outside document at the boundary (paper payment, court order), with source reference |

Every `master`- or `selected`-provenance field additionally declares its **consumption pattern** (sync-validate / cached-projection / frozen-snapshot, MDM-05). A screen specification without a provenance column is incomplete and MUST NOT be built.

**PRE-02 [REV] `entered` is the exception, and it justifies itself against the whole of government.** Every `entered` field carries a one-line justification answering: *why can this value not be pre-filled, derived or selected — from this system, any connected government register, or a third-party feed?* "Our module doesn't have it" is not sufficient (once-only). An officer screen dominated by `entered` fields is a red flag for a missed source, not a data-entry requirement.

**PRE-03 [GEN] Create from source.** A business object that exists *in response to* something — a debt case to arrears, an assessment to a return, a refund to a credit position, an audit case to a risk hit, an appeal to a disputed decision — MUST be created *from* its source: the creation entry point lives on or near the source record; keys, party, periods, amounts and line items carry over automatically; where discretion applies, the officer **selects among source items** (e.g., which open ledger items a case covers) rather than typing them; the officer adds only genuinely new facts. Blank-form creation of such objects is forbidden.

> ✗ "New debt case" menu item opening an empty form with typed debt lines
> ✓ "Create debt case" action on the taxpayer account view / arrears worklist → case pre-filled with taxpayer, open items (checkbox-selectable), computed totals and ages; officer adds strategy and notes

**PRE-04 [GEN] Editable-with-audit vs read-only.** A pre-filled value the user may legitimately change is editable **with audit** — original value and change recorded, the modification visibly marked. A `derived` value is read-only, with recomputation when its inputs move. Mastered attributes follow MDM-07: corrected at their owner, never edited in a consuming module.

**PRE-05 [REV] Nothing is re-keyed.** Data moving between records inside the system moves by reference or copy-on-create — never by an officer re-typing it from one screen into another.

**PRE-06 [GEN] Defaults everywhere, shown not hidden — and defaults embody the compliant path.** Dates default to today or the statutory deadline; office to the user's office; period to the current period. The default choice is the compliant one; deviation remains possible, deliberate and traced. Defaults are visible and changeable (with audit where material), never silently assumed.

### 4.3 CTX — Context and creation

**CTX-01 [REV] Every screen declares its trigger.** Worklist item, action on a source record, inbound event, scheduled process, or — exceptionally — a menu. "Opened from the menu with no context" is a design smell that MUST be justified; most legitimate menu entries are searches and registers, not creation forms.

**CTX-02 [GEN] The standing header.** Every record screen carries a persistent context header answering, without scrolling: **who** (the golden-record identity card, IDR-04), **what** (record type + number), **where** (status + since when), **how much** (the key figures for this record type), **whose** (assigned officer — and, for automated processes, the human-in-the-loop frame: who overrides, who answers the taxpayer). It never scrolls away and is identical in structure across modules.

**CTX-03 [GEN] 360° adjacency.** From any case, the party's full picture — account balances, filings, other cases, contact history — is one click away; from any party view, each domain detail is one click away. Cross-module context is read-only unless the officer holds authority there.

**CTX-04 [REV] Never re-find what is on screen.** Acting on a record never requires searching again for that record or for details the record implies: line items, balances, prior actions and documents load with the record.

### 4.4 WRK — Worklists, lists and volume

**WRK-01 [GEN] Queue-first — and the queue is an exception queue.** An officer's landing page is their worklist: assigned items with identifier, party, key amount, priority, next-action due date and SLA state — not a menu tree, not an everything-dashboard. Every row exists because a rule, threshold or anomaly routed it there, and displays why (AUT-02); straight-through-processed volume is monitoring, not work (AUT-03). Supervisors land on the team queue with per-officer load.

**WRK-02 [LINT] Every list is server-side.** Pagination, sorting and filtering execute in the query layer. No unbounded fetch; no "load all rows, then filter in the browser"; no list without a page size.

**WRK-03 [REV] Task-relevant defaults.** Default sort serves the task (due date, priority, age, amount — never insertion order); columns are chosen per persona and task, each earning its place; the record identifier and the party are always among them.

**WRK-04 [GEN] Scoped by default; never open empty.** Default filters are *my items / my office / active*, applied on first paint so the list always opens showing the user's relevant slice — a worklist or register MUST NOT load empty and wait to be queried (an empty first screen over a national register is both a dead end for the user and a performance trap). Widening to all records is an explicit act — and an authorisation question, not just a filter.

**WRK-05 [GEN] Honest counts; the filter summary matches the list.** Totals and truncation are always visible — "showing 50 of 12,431 — refine or export". The active filters on display MUST describe exactly the rows in the list — no hidden default filter silently narrowing the set, no stale filter chip left after the query changed. Exports respect authority and are logged.

**WRK-06 [GEN] Bulk with preview and per-item verdicts.** Mass operations (bulk reassignment, bulk notices, bulk write-off) show what will be affected before commit, and report per-item outcomes after — *n* succeeded, *m* failed, each failure with its reason.

### 4.5 STA — State, lifecycle and actions

**STA-01 [LINT] Actions are transitions.** The actions offered on a lifecycle-bearing record are exactly the declared transitions permitted for this role in this state — rendered from the state model. Generic Edit / Save / Delete verbs on cases, filings, assessments and agreements are forbidden.

**STA-02 [GEN] Unavailable is explained.** An action the role can never perform is hidden. An action blocked by state or guard is shown disabled *with the reason*: "Cannot close — enforcement action pending."

**STA-03 [LINT] Status is rendered, never edited.** Status displays with its label, since-when, and set-by-whom where relevant — driven by the state model. A status is NEVER an editable field, a free-text value, or a dropdown the user simply re-picks.

**STA-04 [GEN] Consequential actions show consequences.** Irreversible or high-impact transitions (write-off, enforcement, closure, publication on a debtors list, party merge, vocabulary publication) present what will happen — notices sent, balances moved, deadlines started, records re-pointed, live cases re-categorised — and require reason and/or approval routing per policy. For automated or mass actions the preview includes affected-party counts and the rights notice that will accompany them. A bare "Are you sure?" is not a safeguard.

**STA-05 [LINT] No deletion of records of legal record.** Records that acquired legal existence are cancelled / annulled / withdrawn with a reason, retained and visible in history. Physical delete exists only for drafts that never acquired legal effect.

### 4.6 FIN — Financial and legal data integrity

**FIN-01 [LINT] System figures are computed.** Balances, arrears, interest, penalties, totals, debt categories and ages originate in the accounting/computation layer and render **read-only**. An officer typing an amount that exists in the ledger is a defect, not a convenience.

**FIN-02 [REV] External amounts are captured once, at the boundary.** A genuinely external amount (a paper payment, a court award, a customs valuation from a document) is entered where it first enters the organisation, by the role that owns that boundary, with a source-document reference — and from that moment on it is a system figure like any other.

**FIN-03 [GEN] Corrections are transactions.** Reversal or adjustment with reason — never an in-place edit of a financial figure. Screens show the adjustment trail (original → reversal → replacement).

**FIN-04 [GEN] As-of honesty, with lineage on demand.** Every displayed figure — and every cached view of kernel data — states its as-of moment and its source: "Outstanding €4,213.50 · per the revenue ledger as of 13.07.2026 06:00". On demand, lineage: which feed, which form version, which rule version produced this figure. Staleness beyond a configured threshold is flagged on screen, and dependent actions warn or block per policy.

**FIN-05 [GEN] Reconciliation is visible; history renders as-at.** Parts sum to wholes on screen — lines to header, components to balance — and a discrepancy displays *as* a discrepancy, never silently absorbed. Historical documents render with the rates, labels and addresses of their date (codes stored with as-at dates; resolved per MDM-04).

### 4.7 VAL — Validation and error behaviour

**VAL-01 [GEN] Validate against reality, not just format.** Existence, active status, temporal validity, open period, jurisdiction, authority — checked server-side at entry or selection time, not only at final submit. For coded values this is the kernel `validate(domain, code, country, as_of)` at the boundary, failing closed. Format-only checking is theatre.

**VAL-02 [GEN] Errors — and outcomes — name the rule, the value, and the remedy.** "TIN 12345678 fails the check-digit rule — verify against the source document." "Period 2026-Q3 is not yet open for VAT — earliest filing 01.10.2026." Statutory rules cite their identifier; automated outcomes explain per AUT-05. "Invalid input" is forbidden vocabulary.

**VAL-03 [LINT] The server enforces; the client assists.** Every rule is enforced server-side regardless of path — screen, API, bulk file. Client-side checks are a courtesy copy, never the enforcement point.

**VAL-04 [GEN] Block vs warn, distinguished.** Illegality blocks. Anomaly (unusual amount, atypical date, out-of-pattern combination) warns and proceeds only on confirmation with reason — and the override is audited (AUD-02).

**VAL-05 [GEN] No work is ever lost.** Long forms persist drafts (explicit save-and-resume or autosave); session expiry does not destroy input; double-submission is idempotent (one click, one act — a retry never books twice).

**VAL-06 [GEN] Concurrency is surfaced.** A stale update is detected and reported — who changed what since you loaded — and the officer re-decides on current data. Silent last-write-wins is forbidden.

### 4.8 AUD — Audit and accountability

**AUD-01 [GEN] Everything attributable.** Every create, change, transition and decision records who, when, what (before/after), through which action, under which authority — automatically, as a property of the platform, not per-screen effort.

**AUD-02 [LINT] Discretion carries reasons.** Waive, override, reassign, reopen, manual anything — requires a reason: a code from a controlled list plus optional free text, captured as a precondition of the act. Overrides of automated determinations are a named discretionary class, and feed the rule-feedback loop (AUT-07).

**AUD-03 [GEN] History is a screen, not a table dump.** Any record's timeline — acts, status changes, documents generated, communications, accesses where relevant — is readable chronologically by authorised users, in human language, from the record itself. Each entry states **who or what made the update** (person or system), when, and a short description with an optional detail link. Realised by the timeline / case-history pattern (Annex D.5) — the one part of the audit family with a government precedent (MoJ). The *control* side (AUD-02: reason-for-change capture, four-eyes) has no public precedent and is UX-01-original.

**AUD-04 [REV] Reading is also an act.** Access to sensitive records is scoped by role, office and jurisdiction; where policy requires (VIP files, investigations), *viewing* is logged and reviewable. Masked values render visibly as masked — a value that exists but is withheld never looks like absence.

### 4.9 PRD — Officer productivity

**PRD-01 [REV] The frequent path is short — and measured.** The top tasks per persona are identified and measured: target ≤ 3 interactions from worklist to acting; keyboard-completable end-to-end; no decorative confirmations on routine acts. Outcome metrics accompany the interaction metrics: straight-through-processing rate, time-to-certainty, taxpayer effort.

**PRD-02 [GEN] No dead ends.** Completing an action offers the natural continuation — next item in the queue, back to the worklist, the follow-on action — never an orphan success page.

**PRD-03 [REV] Progressive disclosure, with limits; density is persona-specific.** Exceptional detail may collapse; identity, status and money are never hidden. The default view carries what the 80% task needs. Expert officer screens are deliberately **dense, fast and keyboard-first** — the citizen-facing "one thing per page" rule (TPX-01) is *wrong* for high-volume professional work, a distinction authoritative government practice now makes explicitly (DWP internal-systems research; MoJ "beyond the GOV.UK Design System for professional users"). Match density to the persona, not to a house style.

**PRD-04 [GEN] The system waits, not the officer.** Long operations — bulk generation, recalculation, external calls — run asynchronously with progress and notification. A frozen screen is a defect. Unavailable dependencies degrade gracefully per their declared behaviour: cached data with a staleness flag (FIN-04, MDM-05), never a blank error page.

### 4.10 TRM — Terminology, language and format

**TRM-01 [REV] Statutory vocabulary.** Labels and action names use the administration's legal and operational terms from the domain glossary — "Assessment", not "Invoice"; "Write-off", not "Delete debt". Developers and AI assistants NEVER invent domain terminology; an unknown term is a question, not a guess.

**TRM-02 [GEN] A coded value shows its label only, stores its code — resolved as-at.** "VAT, standard rate" — never "20 — VAT, standard rate", and never the code alone. The one exception is a list whose code is itself what officers read (a debt category "C4", a tax type "VAT"): it is marked `display_code` in the application model, and its values show the code instead of the label. The label resolves via the kernel `resolve` as-at the transaction date; the code is stored with its as-of date where the vocabulary is effective-dated. *Amended 25 September 2026 on the owner's word (METHOD-2026-09-25-01, item 13): the rule said codes render "code — label".*

**TRM-03 [GEN] Structured periods and legal formats.** Tax periods are typed values (period type + period), never free date pairs. Dates, numbers and money follow the administration's locale and statutory conventions, uniformly on every screen, list, notice and export.

**TRM-04 [LINT] Externalised text, multilingual-ready.** No user-facing literal is hardcoded in a layout or a script; all labels and messages live in language resources with fallback. (Public-sector deployments are routinely bi- or trilingual.)

### 4.11 MDM — Master & reference data on screen

Grounded in the master-data architecture design (ADD) of the programme this standard was first written for (kernel contracts `resolve` / `validate` / `subscribe` / `map` + `resolve_party`; four-bucket classification; temporal semantics; consumption patterns; golden record; stewardship-as-a-case) and its master-data register (the 43-entry register as allowlist). ⚑ = gated on that design's open decisions (its §10).

**MDM-01 [LINT] Every code list on a screen names its register entry.** Any dropdown, picker, radio set or type-ahead over a code list MUST bind to a list classified in the Master & Reference Data Register (bucket + ID, e.g. R-05 payment method). A screen MUST NOT introduce a list the register does not know, and MUST NOT locally define one the register classifies as shared (R or M) — the register is the allowlist (ADD §6.2). An unknown list is a TO-CONFIRM to the Data Governance Office, never a silently invented local vocabulary.

**MDM-02 [GEN] Shared vocabulary is consumed, never authored, in modules.** Module screens render bucket-R lists read-only, sourced through the sanctioned catalogue access path (ADD §8.2) — never from a module-local copy or a direct kernel-table read. Module Admin sections contain only the module's own bucket-C configuration. The most a module screen offers on a shared value is *request a change*, routed to stewardship.

> ✗ A generated "Master Data" menu in the Payments module with CRUD forms for currencies and payment methods
> ✓ Payments screens consume R-04/R-05 from the catalogue; the steward console is where those lists are maintained

**MDM-03 [GEN] Pickers offer only values valid as-at the effective date.** Code selection filters by temporal validity against the *transaction's* effective date — not today's, where the two differ. Superseded values are never selectable but always renderable in history; future-effective values become selectable only when the effective date qualifies. Where validity drives the choice, the effective date is explicit on the screen.

**MDM-04 [GEN] Store the code, render the resolution.** Fields bound to reference values store code + as-of date; screens render labels via `resolve(domain, code, country, as_of)`. Historical records display the label, hierarchy and attributes as they stood on the record's date; relabelling and translation change presentation, never history.

**MDM-05 [GEN] Declare the consumption pattern; make it visible.** Every screen interaction over kernel data declares one of the three sanctioned patterns (ADD §5.6), and the pattern shows in behaviour: **sync-validate** at the boundary fails closed with a named rule; **cached-projection** views carry data freshness ("reference data as of 13.07 06:10") and keep working through a kernel outage; **frozen-snapshot** documents state their as-issued vocabulary and are never re-resolved.

**MDM-06 [GEN] Party screens show the golden record — with survivorship on demand.** Identity views render the reconciled golden record. Each mastered attribute can disclose its provenance: contributing sources, the survivorship rule / source-trust tier that decided, and when. Unresolved conflicts display as flags on the affected attributes — never hidden, and never resolvable by an officer editing the value in place.

**MDM-07 [GEN] One fact, one writer — on screen.** A mastered attribute is editable only in its authoring module (party identity: Registration). Everywhere else it is read-only with a *report-a-correction* affordance that routes to the owner or steward. A consuming module NEVER edits its local projection.

**MDM-08 [GEN] Search the identifiers, not just the TIN.** Party lookup searches the identifier cross-reference (M-02) across all registered identifier types (R-18). Results show the primary identifier *plus which identifier matched* ("matched on VAT no MT2231…"). `resolve_party` confidence governs behaviour: deterministic matches may auto-select; probabilistic matches are ALWAYS presented as candidates for explicit confirmation.

**MDM-09 [GEN] Match, merge and unmerge are governed screens.** Duplicate-candidate queues show the match evidence (matched attributes, rule or score, source trust). Merge preview enumerates the impact before commit — the cases, agreements, balances and documents that will re-point. Merge and unmerge are effective-dated, reasoned, audited acts flowing through the conflict-resolution workflow — never a data fix.

**MDM-10 [GEN] Change events reach open work.** Where a module holds cached projections, the change feed (`subscribe`) drives the screens: open cases referencing a deprecated/superseded value or a changed golden record flag it ("party identity updated 12.07 — review before enforcement"); worklists can filter by *affected by reference change*. No officer decides on silently stale meaning.

**MDM-11 [REV] ⚑ Scoped catalogues render scoped pickers.** Partitioned catalogues — reason codes above all (R-14: one mechanism, many scopes) — surface only the (domain, context) slice the screen belongs to: the appeals refusal picker shows appeal refusal reasons only. The UI never offers the global partition list. (Gated on the R-14 pattern being ratified; feeds AUD-02.)

**MDM-12 [REV] ⚑ Look-alike vocabularies never merge on screen.** Refund risk band, audit risk tier, compliance risk category and debt category C1–C5 are four vocabularies sharing a word (a flag of the master-data register). Each renders under its proper name; no screen offers a generic "risk level" control; views showing several display them side by side, named. (The naming prohibition holds regardless of how that flag resolves.)

**MDM-13 [GEN] Vocabulary change is a case.** The steward console realises proposal → review → approval → effective-dating → publication as a case type of the platform's case-management building block (ADD §7.1), inheriting the WRK/STA/AUD families wholesale (steward worklists, transition-driven actions, proposer ≠ approver, reasons). Publication of a consequential change additionally presents an **impact preview** — which modules, screens and live records consume the value, and what a change would re-categorise.

**MDM-14 [GEN] Quality gates are steward-facing screens.** The promoted quality rules (orphaned records, duplicate active names, missing translations, transactions referencing inactive values — ADD §7.4) surface as steward dashboards and worklists with drill-down to the offending rows, each defect class carrying its resolution action — counts alone are not a screen.

**MDM-15 [GEN] Crosswalks are governed screens, not spreadsheets.** Where information is exchanged externally, screens show the internal code *and* its mapped external code with the mapping version (`map` contract); unmapped codes surface as steward work items; officers never hand-type an external code where a governed mapping exists.

### 4.12 AUT — Automation, exceptions and explanation

Grounded in the TA 3.0 principles (P4, P7–P11, P25, P28–P33, P41, P48, P50 of the transformation-principles document).

**AUT-01 [REV] Classify every human action: automate / assist / decide.** Each action on an officer screen is one of: rule-expressible (→ automated, no screen), analytics-assisted human decision, or genuine judgement/discretion. An action that merely confirms what a rule already determined is deleted, not designed. Approval steps exist only where judgement or legally required accountability demands a human.

> ✗ "Approve refund" button on a screen showing a refund the rules already fully determined, below every threshold
> ✓ The refund executes; the officer's screen exists only for the flagged minority, and says why each item was flagged

**AUT-02 [GEN] Exceptions explain themselves.** Every worklist item that exists because automation stopped carries, on the item: **why** (the rule, threshold or anomaly that fired, in words), **what is to be decided** (with the criteria), and the full data context attached. The officer never re-derives why they are seeing a case.

**AUT-03 [GEN] The green lane is visible, not workable.** Straight-through-processed volume appears as monitoring — counts, STP rate, trend — never as list rows an officer can open "just to check". Random assurance samples arrive as explicitly labelled sample items, distinct from risk-flagged ones.

**AUT-04 [GEN] Decisions, not reports.** A screen that presents data for a decision embeds the decision: criteria displayed, threshold state, the routing/outcome actions attached. "Export it and decide elsewhere" is forbidden as a designed flow; a request for "a report" is answered at design time with *what decision does it serve?* Genuine reports (statutory, analytical) remain — as reports, not as decision surrogates.

**AUT-05 [GEN] Automated outcomes are explainable on screen.** Every automated determination — assessment, risk flag, penalty, refund hold, case routing — renders its explanation on demand: the input data used, the rule(s) and rule **version** applied, the outcome; reproducible on request. Extends VAL-02 from errors to outcomes; the explanation vocabulary is the statutory one (TRM-01).

**AUT-06 [GEN] Assistance is marked; accountability is named.** AI/analytics contributions render as *suggestions with their basis* (score, drivers), visually and semantically distinct from facts and from rule determinations; they never silently auto-act where accountability requires a human. Per process, the human-in-the-loop frame is visible on the case: who may override, who reviews, who answers the taxpayer.

**AUT-07 [GEN] Resolution feeds the rules.** Exception-handling screens offer a structured feedback outcome — false positive · threshold miscalibrated · new pattern — routed to rule governance. This is the S2C-01 §12.3 conversion ritual given a button: every exception handled is a chance to need fewer exceptions.

**AUT-08 [GEN] Source assurance is displayed.** Where data originates from an assured external system (certified payroll software, e-invoicing platform, fiscal device, trusted intermediary), screens show the source and its assurance status; when the source is assured, per-transaction re-verification screens are not built — effort aims at the system. Upstream feed changes and outages surface per the declared degradation behaviour.

### 4.13 TPX — Taxpayer touchpoints (the minimal set)

Scope note: UX-01 covers the officer back office; TPX is the *minimal* taxpayer-facing set the platform cannot ship without, because the same platform generates portal screens. A full taxpayer-experience standard (journeys, service standards, content depth) remains future work and will draw on the public-sources research.

**TPX-01 [REV] The filing ladder; one thing per page.** Every taxpayer interaction is designed down the ladder — **eliminate** (nothing to do; the system already knows) → **pre-fill and confirm** → **complete** (last resort) — and the specification justifies the rung chosen. This is the PRE family pointed outward. Where the taxpayer must complete something, default to **one thing (one question) per page**, a review-before-submit summary, and a confirmation page (Annex D.6 / D.9) — the researched GOV.UK default for citizen services. This density rule is the *opposite* of the officer default (PRD-03); the persona decides, not a single house style.

**TPX-02 [GEN] The account is the home.** The taxpayer's landing view is their single position across all taxes and duties: assessed, paid, due, refunds, obligations and deadlines, with drill-down — and the live status of anything in progress, without asking. (The taxpayer-side mirror of WRK-01 and the accounting L1/L2/L3 view.)

**TPX-03 [GEN] Every automated or adverse outcome carries its explanation and its challenge path.** What was decided, on which data, under which rule (version), and what to do if you disagree — review, objection, appeal, with deadlines. The rights affordance is part of the decision display, not a leaflet. (Mirror of AUT-05.)

**TPX-04 [GEN] Compliant by default.** Defaults, prompts and flow order make the compliant choice the easiest one; deviation remains possible but is deliberate, visible and traced. Never dark patterns — the deviation path is honest, just not the default.

**TPX-05 [GEN] Acting-for is first-class.** Representation — agent, accountant, payroll bureau, employee-for-company — is visible on every screen: who is acting, on whose behalf, under which authorisation scope; switching context is an explicit act; everything done under delegation is attributed to both parties.

**TPX-06 [REV] Assisted-channel parity and accessibility.** Every automated journey has a defined assisted channel achieving the *same outcome* (office, phone, intermediary); interfaces meet the ACC family; digital exclusion never produces worse treatment.

**TPX-07 [GEN] Friction is instrumented.** Touchpoints record where users stall, abandon, err and seek help; effort is the design metric and it is measured, feeding friction out of the design rather than staffing it.

### 4.14 ACC — Accessibility

Adopted by reference: **WCAG 2.2 level AA** (and EN 301 549 where the deployment is EU-bound) is the conformance baseline; the rules below are the screen-level obligations this standard enforces on top of, not instead of, that baseline.

**ACC-01 [LINT] The conformance target is declared and gated.** Every deployment declares its accessibility standard (WCAG 2.2 AA / EN 301 549 / national equivalent) as a platform attribute; conformance checking is part of acceptance, not an aspiration in a policy document.

**ACC-02 [GEN] Keyboard-complete.** Every task is completable keyboard-only: visible focus, logical focus order, no traps, shortcuts on the frequent paths (PRD-01). Search-and-select dialogs, grids and wizards — the workhorses of this standard — are explicitly keyboard-operable.

**ACC-03 [GEN] Semantics for assistive technology.** Form fields are programmatically labelled; tables carry headers; validation errors and status changes are announced (live regions); identity, status and money are never conveyed by colour alone — SLA traffic lights and RAG tiles always carry text or symbol equivalents.

**ACC-04 [GEN] Accessible error and time-out behaviour.** Errors are identified in text, associated to their field, with the remedy stated (VAL-02 is written to be WCAG-conformant by construction); session time-outs warn, are extendable, and never destroy work (VAL-05).

**ACC-05 [REV] Contrast, zoom and density.** Minimum contrast ratios hold in all component states; dense officer grids remain readable and operable at 200% zoom / user font scaling — density is a setting, not a fixed aesthetic.

**ACC-06 [REV] Assistive parity is tested.** Acceptance for each persona's top tasks includes a keyboard-only pass and a screen-reader smoke pass; a task that cannot be completed that way fails acceptance, not merely a checklist.

### 4.15 CNT — Content, notices and language

The letter *is* the product for most taxpayers; content is design, not decoration.

**CNT-01 [REV] Plain language for people; statutory precision alongside.** Taxpayer-facing content states what happened, what it means, what to do, and by when — in plain language at a defined reading level — with the legal basis cited *alongside* (not instead). Officer-facing content may be terse; it is never jargon that contradicts the glossary.

**CNT-02 [GEN] The notice is a designed product.** Every outbound notice/letter template carries, structurally: the party identity and subject reference; the decision and its explanation (AUT-05/TPX-03 content); amounts with a computation summary; the challenge path with deadlines; the contact/assisted channel. Merge fields are validated against the data model (the template registry's versioning and merge-field validation machinery); the notice freezes its vocabulary as-issued (MDM-05).

**CNT-03 [GEN] Instructional text is data-aware.** In-context help, hints and guidance reflect the actually configured rules — rates, thresholds, deadlines — rendered from the rule repository, never hardcoded prose that drifts from configuration.

**CNT-04 [REV] Every question carries its why.** Taxpayer-facing forms ask in task order, group related fields, and justify each request — "we ask because…" with the legal basis — consistent with data minimisation. A question that cannot state its why is removed (and PRE-02/Q0 asked again).

**CNT-05 [GEN] One thing, one name, everywhere.** A concept has exactly one name across screens, lists, notices and channels (TRM-01 glossary); a status shown in the portal is the same word the officer sees and the letter prints. Channels never rename each other's states.

**CNT-06 [REV] Translation parity.** All-language versions carry legal equivalence review; terminology in every language comes from the same glossary; a language fallback never silently changes meaning (TRM-04).

### 4.16 DSH — Dashboards, KPIs and analytical views

For the three dashboard levels the module specs already prescribe (strategic / departmental / operational) and the governed KPI catalogue.

**DSH-01 [REV] Every dashboard declares its decision and its audience.** A tile that informs no decision for its declared audience is removed — AUT-04 applied to dashboards. Strategic, departmental and operational views are distinct designs, not one screen with more filters.

**DSH-02 [GEN] KPIs carry their definition.** Every KPI tile links to its governed metric specification (formula, period, source, owner — the governed KPI catalogue) and states its as-of moment. No unexplained numbers; the same KPI shows the same value everywhere, computed once in the semantic layer, never re-derived per dashboard.

**DSH-03 [GEN] Thresholds and RAG states come from configuration.** Traffic-light thresholds are configured values (two-zone model), rendered with text/symbol as well as colour (ACC-03), consistent across every screen that shows the measure.

**DSH-04 [GEN] Drill-down preserves context and reconciles.** From aggregate → filtered list → record without losing filters; every aggregate is reconcilable to the record list beneath it (FIN-05 applied to analytics). A number that cannot be drilled is marked as external/summary-only.

**DSH-05 [GEN] Charts are server-computed.** Chart data comes from governed server-side queries — never client-side scraping of rendered artefacts, never client recomputation of catalogued KPIs (a lesson of one delivered dashboard). Every chart states its as-of (FIN-04).

**DSH-06 [REV] Operational dashboards connect to work.** An operational dashboard answers "what needs doing now" and links into the corresponding worklists (WRK-01) — monitoring and work are one world, not parallel ones. Green-lane/STP monitoring per AUT-03 lives here.

---

## 5. The Screen Design Protocol (mandatory)

The rules of §4 judge a finished design. This protocol *produces* a correct one: it forces the derivation that naive generation skips. **No screen is specified, generated or built before the protocol's output — the Screen Derivation Table — exists.** For an AI assistant this is a hard contract: producing screen artefacts without it is a method violation.

**Q0 — The existence test (before everything else).** Why must this interaction exist? Four checks, each fatal:

1. Does it re-collect what any government register or feed already holds? (once-only)
2. Does it only confirm what a rule already determined? (the rubber stamp)
3. Is it a report standing where a decision workflow belongs?
4. Could the event be captured in its natural system of origin instead?

If any answer is yes, the correct deliverable is a **design-change request** (or a TO-CONFIRM to the process owner), not a screen. Only past Q0 does the derivation begin.

**The eight derivation questions:**

1. **Persona & moment.** Who uses this screen, in which state of which lifecycle, at which step of which process? (One screen per moment beats one screen for everything.)
2. **Trigger & source.** What opens this screen — worklist item, action on a record, event, schedule, menu? What record does it carry in?
3. **The knowledge inventory.** List everything the system already holds at this moment: the source record's fields, the party's master data, ledger positions, prior and related cases, reference data, computed values — each classified by register bucket + ID (R/M/C/P). *This list is what pre-fills.* If it is empty, prove it — that is rare.
4. **Field provenance table.** Every field: label, entity.attribute binding, provenance (PRE-01), editability, validation. `entered` rows carry their whole-of-government justification (PRE-02); `master`/`selected` rows carry register ID, consumption pattern and effective-date source.
5. **Reference resolution.** For every record-reference field: the selection mechanism per IDR-05, the search keys, the disambiguation columns — and for code lists, the register entry, home, consumption pattern and validity basis.
6. **Volumes.** Expected P50 / P99 result sizes for every list and query, and the consequences drawn (page size, caps, indexes, refine thresholds).
7. **Actions ↔ transitions.** Every button mapped to a lifecycle transition + role + guard (STA-01), or explicitly declared non-lifecycle — and every human action classified automate / assist / decide (AUT-01), with no rubber-stamps surviving.
8. **Failure, absence & explanation.** What shows when the source is unavailable, stale or empty (per declared consumption pattern); what each validation failure says (VAL-02); what happens to work in progress (VAL-05); the explanation content for automated outcomes and — taxpayer-facing — the challenge path (AUT-05, TPX-03).

Unanswerable questions are recorded as **TO-CONFIRM with a named owner — never resolved by a silent default** (chain of custody, S2C-01 invariant 10, applied to UX).

**Worked micro-example — "Create instalment agreement" (mirrors one specified instalment-agreement screen):**

| Field | Binding | Provenance | Edit | Validation / note |
| --- | --- | --- | --- | --- |
| Taxpayer | agreement.tin | `selected` — identifier lookup (IDR-02), golden-record identity card | re-select | TIN exists, active, has open debt |
| Name, contact | party master | `master` (cached-projection) — auto from register | read-only | corrections route to Registration (MDM-07) |
| Debt summary (lines) | ledger open items | `source` — auto from the revenue ledger, per tax type & period | select which items are covered | as-of stamp shown (FIN-04) |
| Total amount | computed | `derived` | read-only | Σ(selected items) + projected interest |
| Instalments, frequency, start | agreement terms | `entered` — genuine negotiation outcome | editable | count/frequency within policy bounds |
| Per-instalment amount | computed | `derived` | read-only | recalculates on any term change |
| Approval route | derived from thresholds | `derived` | read-only | within parameters → auto-approve (AUT-01); else supervisor (the threshold rule) |

Note the shape: **one** family of genuinely `entered` fields — everything else the system already knew. That ratio is what a correct back-office screen looks like.

---

## 6. The anti-pattern catalogue

Named, recognisable failures. An AI assistant self-reviews against this list before delivering any screen (UX-02); a human reviewer cites AP numbers in findings.

| # | Anti-pattern | Symptom | Killed by |
| --- | --- | --- | --- |
| AP-01 | **Name as key** | A reference captured by typing a name; matching or uniqueness logic on names | IDR-01/02/03/06 |
| AP-02 | **The amnesiac form** | The screen asks for data the system holds (debt lines, balances, addresses, obligations) | PRE-01/02/03/05, P1 |
| AP-03 | **The blank-form case** | A case/document created from an empty form, unlinked to any source record | PRE-03, CTX-01 |
| AP-04 | **The infinite dropdown** | A dropdown over parties, cases, or any operational entity set | IDR-05, P3 |
| AP-05 | **Demo-scale design** | Unpaginated lists, client-side filtering, "select all" over the register | WRK-02/05, P3 |
| AP-06 | **Editable status** | Status as a free dropdown or text field the user re-picks | STA-01/03 |
| AP-07 | **The editable ledger** | Typed or overridable balances, interest, totals | FIN-01/03, P7 |
| AP-08 | **Generic CRUD on casework** | Edit/Save/Delete buttons on cases, filings, assessments | STA-01/05, P6 |
| AP-09 | **Delete as an option** | Physical delete offered on records of legal record | STA-05, AUD-01 |
| AP-10 | **Are-you-sure theatre** | Consequence-free confirm dialogs on consequential acts (and on routine ones) | STA-04, PRD-01 |
| AP-11 | **Validation theatre** | Format-only checks — accepts a well-formed TIN that doesn't exist, a date in a closed period | VAL-01/03 |
| AP-12 | **The orphan screen** | A screen with no persona, no trigger, no workflow home | CTX-01, WRK-01, Q1–Q2 |
| AP-13 | **Silent defaults** | Invented business behaviour — a made-up status set, an assumed rounding, a guessed threshold | protocol TO-CONFIRM rule; S2C-01 inv. 10 |
| AP-14 | **One-screen-fits-all** | The same screen for intake clerk, case officer and approving supervisor | Q1, WRK-03, PRD-03 |
| AP-15 | **The rubber-stamp screen** | An approval click that confirms what the rule already determined | AUT-01, Q0 |
| AP-16 | **The report surrogate** | A list/dashboard where a decision workflow belongs; "export and decide elsewhere" | AUT-04, DSH-01, Q0 |
| AP-17 | **The re-collection form** | Asks for what a government register or feed holds (AP-02 at whole-of-government scope) | PRE-02, Q0 |
| AP-18 | **The unexplained verdict** | An automated outcome with no inputs, rule version, or challenge path | AUT-05, TPX-03, P12 |
| AP-19 | **The anonymous exception** | A worklist row that doesn't say why automation routed it to a human | AUT-02, WRK-01 |

---

## Annex A — A binding to Progressa's higher-education services

*A simulated case for Progressa, a fictional country; every institution, name, date and figure in it is invented. In this copy of the standard it replaces the edition of record's binding, which was drawn from the corpus of a real programme, so that every rule has a native example in the setting of the courses this kit is published with.*

The core rules are domain-neutral. This annex binds them to one setting — the services Progressa's quality authority for higher education, PHEQA, and its ministry of education, MoEYS, owe to private institutions — so that every rule has a native example, and each example shows the rules already implied by what the services must do.

### A.1 The identity spine: register number first

Every institution PHEQA has registered has one identifier, its register number, written like INS-00217; its name, its kind and its address are data *about* the institution, and its name changes only when the minister approves a change. Search accepts **the register number, or a fragment of the name**; several matches return a **disambiguation list (register number, name, kind, state of the licence)**; the officer **selects**; the selected institution renders as the standing header. That is IDR-01…04 verbatim. A person is identified by the national identity authority's sign-in, which gives each service its own identifier for the person: no screen asks for, shows or keeps the national number (MDM-08 applied to a person).

### A.2 Worked example — an inspection created from its application (the failure, corrected)

**Wrong (as generated):** a "New inspection" form with `Institution name: [____]` and a grid where the inspector types the particulars of the application she is to inspect.

**Right (as the services already require):**

- *Automatic path (the norm):* when the registration officer accepts an application as complete, the system creates the inspection carrying **the application's number, the institution, the kind of licence asked for, and the version of PHEQA's standards the application was made under**, assigned to the inspectors' worklist. No screen at all: the inspector first meets the inspection in her queue (WRK-01, AUT-02 — the row says which event created it).
- *Manual path (the exception):* creation from context — the application's workspace exposes **Record an inspection visit** on an application already identified and showing its particulars. The form arrives with the application and the institution bound (identity card), the standards in their version **read from the setting** that holds them, and the date of the visit proposed from the inspector's calendar. The inspector contributes: what she found, the outcome, and her notes.
- The fee remains the Payments block's throughout: the application *references* the payment confirmation, it never *re-states* the amount (FIN-01).

Rules exercised: PRE-01/03, IDR-01/04, CTX-01/02, FIN-01/04, STA-01, WRK-01, AUT-02.

### A.3 Worked example — institution lookup

Identifier-first (the register number direct — IDR-02); attribute fallback = a fragment of the name, searched on the server, disambiguation columns register number · name · kind · licence state (IDR-03); selection → the institution's standing header with drill-down to its licence and its decisions (CTX-02/03); access logged with user, register number, timestamp (AUD-01/04). Add: format validation of the register number at entry, result caps with refine messaging, recently-worked shortcuts (PRD-01).

### A.4 The compliant exemplar — applying for a provisional licence

The screens of the provisional-licence application are the pattern to imitate: the applicant is **identified by sign-in**, PHEQA's standards are **read from their setting** in the version in force, the kind of institution is **chosen** from the shared list, only the particulars the regulations list are **entered**, the fee is **read** from the setting its owner keeps and **paid** through the Payments block, and the receipt gives the application's number. Its shape generalises: **identify → auto-populate the substance from what is already held → capture only what nobody else holds → compute the rest → route by rule.**

### A.5 Rule manifestations across the services

How PRE-03 (create from source) lands in each service:

| Service | Object | Created from | Pre-filled substance |
| --- | --- | --- | --- |
| Register an institution | entry in the register of institutions | a licence granted | name, kind and address — from the application the licence was granted on |
| License an institution | application, then licence | the applicant's request through PHEQA's self-service | the applicant's identity from the sign-in; the standards in force; the fee due |
| Recommend a decision to the minister | recommendation | an inspection recorded | the application, the institution and the inspection's outcome |
| Record a decision on a licence | the licence's new state | the minister's decision received from MoEYS | the licence, the decision and its date |
| Hear an institution's appeal | appeal | the disputed decision of PHEQA | decision reference, institution, dates |
| Approve a change of an institution's name | request for approval | the institution's request | the institution from the register; the proposed name |
| Publish the list of registered institutions | the list for the Gazette | the register of institutions, read across the information-mediation block | every registered institution, its kind and its licence state |
| Review a decision of PHEQA | request for review | the aggrieved person's request | the decision reviewed, read from PHEQA |

The same exercise applies per family: IDR as register-number and application-number lookups everywhere; WRK as the officers' worklists (the inspector's queue of applications awaiting a visit, the registration officer's queue of decisions received); STA as the licence's moves, each on a decision someone is entitled to make; AUD as the mandatory reason on reassignment; MDM as the shared code lists of the groundwork (the kinds of institution); AUT as the automatic creation of an inspection from an accepted application; DSH as the Registrar's view of the applications in hand and their age.

## Annex B — Adoption and enforcement

### B.1 In the spec-to-code platform (S2C-01)

**Home.** This standard *is* the platform-invariant half of Dimension 7 (S2C-01 §5): the [GEN] rules become the UX pattern library baked into the generators — the worklist pattern, the identity-card widget, the standing context header, the search-select control, the action-bar-from-transitions, the explanation panel, the notice template structure. Fixed once in a pattern, inherited by every screen. The per-application half (which columns, which filters, which volumes) stays elicited via the question slots.

**Question slots.** Q0 plus the eight protocol questions become Dimension-7 template slots, so a screen specification *cannot be silent* about existence, trigger, provenance, selection mechanisms, volumes, actions or failure behaviour.

**Candidate model-lint rules (U-series)**, in the L-rule style of `tools/validate.py`, each requiring a fixture pair per §12.4 discipline:

| ID | Rule (model predicate) | Enforces |
| --- | --- | --- |
| U001 | every form field bound to a reference-kind attribute declares its selection mechanism; `dropdown` only against a vocabulary or bounded entity | IDR-01/05 |
| U002 | every form field declares `provenance` (enum per PRE-01); `entered` requires a `justification` | PRE-01/02 |
| U003 | a creation form for a case-kind entity declares `created_from`; menu-triggered creation requires an explicit waiver | PRE-03, CTX-01 |
| U004 | fields bound to attributes owned by another module/system are read-only outside the owner | FIN-01, PRE-04 |
| U005 | every list declares pagination, default sort, and a default scope filter | WRK-02/03/04 |
| U006 | lifecycle-bearing entities expose no generic edit/delete; every screen action maps to a declared transition or is tagged non-lifecycle | STA-01/05 |
| U007 | status attributes render via the lifecycle component, never a plain input | STA-03 |
| U008 | every form/screen object declares `persona` and `trigger` | CTX-01, Q1–Q2 |
| U009 | transitions tagged discretionary declare reason capture (vocabulary-backed) | AUD-02 |
| U010 | no user-facing literal outside language resources | TRM-04 |
| U011 | every options/lookup binding names a register entry ID; R/M-classified lists must target the kernel catalogue component, never a module-local table | MDM-01/02 |
| U012 | no module userview/navigation exposes CRUD screens for R/M-classified lists | MDM-02 |
| U013 | every code-bound field declares consumption pattern ∈ {sync_validate, cached_projection, frozen_snapshot}; document-generation bindings must be frozen_snapshot | MDM-05 |
| U014 | fields bound to mastered attributes outside the authoring module are read-only and declare a correction route | MDM-07 |
| U015 | every picker over an effective-dated vocabulary names the attribute supplying its effective date | MDM-03 |
| U016 | reason-code pickers declare their (domain, context) scope | MDM-11 |
| U017 | every human process activity declares its value class (`assist` \| `decide`); class `confirm` fails | AUT-01 |
| U018 | entities carrying automated determinations declare an explanation binding (rule id + version + inputs reference) | AUT-05 |
| U019 | taxpayer-visible adverse outcomes declare their challenge-path content | TPX-03 |
| U020 | a form field whose canonical mapping marks a register-held attribute cannot carry provenance `entered` | PRE-02 (once-only) |
| U021 | lists bound to exception queues declare a reason-display binding | AUT-02 |
| U022 | the deployment declares its accessibility conformance target; acceptance includes keyboard-only and screen-reader scenarios for top persona tasks | ACC-01/06 |
| U023 | notice templates declare the structural blocks (decision · explanation · amounts · challenge path · contact) and their merge fields resolve against the data model | CNT-02 |
| U024 | dashboard tiles bind to governed metric-spec IDs (no inline recomputation of a catalogued KPI); thresholds reference configuration | DSH-02/03 |
| U025 | a form that belongs to a record (its trigger a record's act) stands on no visible menu: it is opened from the record, which it carries (kit lint U025, 25.09.2026) | CTX-01 |
| U026 | a list of values bound to a field with more than nine values in force is divided into categories (`groups`) of no more than nine; no category holds more than nine values and no list of categories more than nine (kit lint U026, 25.09.2026) | IDR-05 |

**The compounding loop applies.** Every naive-UI incident found on an instance follows the §12.3 ritual: register entry → mechanizable? → U-rule with fixture pair, or review-checklist entry. This document is the register's UX seed, not its ceiling.

### B.2 In AI-assisted sessions (the immediate fix)

1. **Install UX-02 v1.3** in the implementation repo — as a `CLAUDE.md` section, or as a skill triggered by any screen/form/list/case/dashboard/notice work.
2. **The contract:** the assistant MUST run Q0, MUST produce the Screen Derivation Table before any screen artefact, MUST record gaps as TO-CONFIRM instead of inventing, and MUST self-review against the anti-pattern catalogue, listing and fixing violations before delivery.
3. **Review prompts:** for existing screens, UX-02's checklist doubles as an audit prompt — "grade these screens against UX-01 §4/§6, cite rule IDs".

### B.3 Governance

This standard is versioned; rules are citable (family-ID); FISs, CADs and application models cite rule IDs the way they cite FRs. Additions follow the platform-delta discipline: incident → candidate rule → mechanization verdict → this document + (where [LINT]) a U-rule with fixtures. Waivers are explicit and signed — a screen that must violate a rule says so, says why, and names who accepted it. ⚑ rules track the MDM ADD §10 decisions and move in step with them.

---

## Annex C — Source lineage, boundaries and the standing intake

**Analysed to date:**

| Source | Contributed |
| --- | --- |
| S2C-01 Platform Architecture v0.9 | Enforcement philosophy (mechanization gate, invariants, chain of custody); Dimension-7/8/9 hooks; the pattern-library home |
| The module specifications of the programme it was first written for, and a tax-administration white paper | Native examples and terminology (A.1–A.5); confirmation that the rules were already implied by the corpus |
| That programme's master-data architecture design and master-data register | Family 4.11 (MDM); consumption patterns; golden record; register-as-allowlist; ⚑ gates D-1…D-5 |
| TA30 Digital Transformation Principles (OECD TA 3.0) | Premise 6, P11–P12, Q0, families 4.12 (AUT) and 4.13 (TPX); ten rule amendments |
| UX-03 Public-Source Catalogue (evidence round 1) | v1.2 deltas: IDR-05 ladder, IDR-05a search dichotomy, WRK-04/05 hardenings; Annex D component-pattern inputs; confirmation that provenance / audit-UI / financial-integrity / terminology have no public counterpart (the families where UX-01 leads) |
| UX-03 §7 — government sources (evidence round 2) | v1.3 deltas: persona-specific density (PRD-03 / TPX-01), AUD-03 Timeline precedent, Annex D.5–D.9 (OGL v3.0 / CC0, adaptable); re-tested and reconfirmed that PRE / FIN / TRM and the audit *control* side have no government precedent |

**Standing intake — the public-sources cross-check.** Round 1 (enterprise vendors) and Round 2 (government / public-sector: GOV.UK, MoJ, Home Office, DWP, USWDS) are complete and verified — see UX-03 §§2–7; their deltas are folded into v1.2 and v1.3 above. **Round 3 is deprioritised**: the remaining unswept systems (Canada.ca, EU ECL, Estonia Veera, Singapore SGDS, German KERN, Australia) and the formal standards (ISO 9241-110, WCAG 2.2 / EN 301 549, NN/g) offer low expected marginal yield for the officer core; the one open prize is terminology / localisation (TRM) content from the bilingual / multilingual systems (Canada.ca, EU ECL), to be run as a narrow pass only if the TRM gap ever bites. Any further round enters as a vX delta under the same discipline.

**What this standard is deliberately not:**

- **A visual design system.** Layout grids, typography, spacing, component visual specifications, theming and iconography belong to the UX pattern library / platform theme, which this standard constrains behaviourally but does not draw. The pending research's design-system findings feed that library, not this document.
- **An NFR catalogue.** Response-time budgets, availability, capacity live in the module NFRs; this standard states only behavioural consequences (async over frozen screens, staleness flags).
- **A target operating model.** Which processes exist, who staffs them, how the transformation is governed — TOM and S2C-01 Layer-0 territory. This standard takes only what lands on a screen.
- **Usability evidence.** The rules encode expert judgement and the corpus, not yet observation. Dimension-7 playback (confirming work-and-workspace decisions against previews with real officers) is the mechanism that validates — and falsifies — them; findings flow back through B.3.

---

## Annex D — Pattern-library inputs from verified public sources

These are **component-level** patterns from the verified public sources (UX-03, rounds 1–2). They are deliberately **not rules** — they specify *how* a control looks and behaves, the province of the UX pattern library / platform theme (see Annex C, "what this standard is deliberately not"), not the principle layer. They are the reference set the generators' [GEN] patterns should implement, re-expressed in our own words. Two licence regimes apply: the **Round-1 vendor sources** (Fiori, SLDS, Pega — D.1–D.4) are proprietary, so nothing is copied — cite version-pinned URLs in the library; the **Round-2 government sources** (GOV.UK, MoJ, Home Office — D.5–D.9) are under the **Open Government Licence v3.0** (or CC0 for USWDS), which permits adaptation, so their text may be reused directly provided any deployment carries the OGL attribution: *"Contains public sector information licensed under the Open Government Licence v3.0."*

**D.1 The message-control catalogue (behind VAL-02/04).** A five-type message model with a scenario-to-control mapping: *error* (blocks further processing) · *warning* (may proceed, may fail later) · *success* · *information* · *confirmation*. Controls: a dialog / message-box for a decision or a non-field message; an inline field state (semantic colour + click-to-reveal in-place message) for field validation, aggregated into a message popover; a transient toast as the standard success signal; an in-page strip for persistent page-level status. (Source: SAP Fiori Message Handling.)

**D.2 Search result behaviours (behind IDR-02/03 and IDR-05a).** On focus, offer recent items (~5). As the user types, return top matches live (~5, no Enter). Disambiguate with object icon/type + record name + a distinguishing attribute. Offer pre-scoping (an object-type selector on the input) and pre-filtering (an advanced popover whose active-filter count persists as a chip). Matching should tolerate stemming, configured synonyms and spelling slips. (Source: Salesforce SLDS 2 global / in-context search.)

**D.3 Case-page anatomy (behind CTX-02/03).** A three-region record page: a **summary panel** (type icon, label, unique ID, primary actions, highlighted fields, tabs); a **work area** carrying the lifecycle as visible stages plus the current assignments/actions; a **utilities panel** (attachments, followers, related cases, stakeholders). (Source: Pega case pattern — near-identical to CTX-02/03, i.e. independent corroboration.)

**D.4 Recorded corroboration and confirmed gaps (no action — evidence, not change).** Verified findings that *confirm* existing rules, logged so the alignment is citable: Fiori's find-vs-worklist-vs-record floorplan separation ↔ our IDR / WRK / CTX split; Fiori's *hide unauthorised actions* ↔ STA-02 — but we keep **disable-with-reason** for *state-blocked* actions, a deliberate divergence from Fiori's *hide*, because accountability requires the officer to see what exists but is currently blocked and why; Pega's smart-default pre-fill and *placeholder ≠ pre-filled value* ↔ PRE-06 / PRE-01; Pega's "a form is a UI of last resort" and 5–7-step wizard cap ↔ P11 / PRD; and DWP's internal-systems research ↔ Premise 3 / PRD-03 (it names back-office "agent interfaces" as an unsolved design problem — external validation of this standard's reason for existing). On the gap re-test across both rounds: field-provenance display (PRE), financial-integrity display (FIN) and terminology / localisation (TRM) have **no** public counterpart, vendor or government, and remain UX-01-original; audit / accountability now splits — its **display** side gains a government precedent (MoJ Timeline, D.5) while its **control** side (reason-for-change, four-eyes — AUD-02) remains original.

**D.5 Timeline / case-history (behind AUD-03).** A record of case / application events in date order; each entry captures **who or what** made the update (person or system), the date/time, a short title / description, and an optional link to detail. The display realisation of the audit-history rule. (Source: MoJ Design System "Timeline", OGL v3.0.)

**D.6 Check answers / review-before-commit (behind TPX-01; adjacent to STA-04, WRK-06).** Immediately before submission, show a summary of everything entered, grouped by section, each row with a "Change" link that returns to that question and back to the summary. The same shape serves an officer's consequence-preview before a consequential act. (Source: GOV.UK "Check answers", OGL v3.0.)

**D.7 Error summary + inline message (behind VAL-02, ACC-04).** On a validation failure, show a summary block at the top of the page listing every error as links to the offending fields, *and* the inline per-field message at each field — the accessibility-conformant realisation of "name the rule, the value, the remedy". (Source: GOV.UK "Error summary" / "Recover from validation errors", OGL v3.0.)

**D.8 Caseworker task patterns (behind IDR / WRK / PRD).** The officer-facing verbs, as named library entries: *search for something*, *choose from a long list*, *filter a list*, *compare information*, *add to a list*, *get more details*. They corroborate IDR-05 / IDR-05a and the WRK family and give the pattern library its back-office vocabulary. (Sources: Home Office Design System; MoJ Design System — OGL v3.0.)

**D.9 Confirmation & task-list pages (behind TPX-01, PRD-02).** After a completed submission, a confirmation page stating what happened and the next step (no dead end); for multi-step journeys, a task-list page showing each task and its status. (Source: GOV.UK "Confirmation pages" / "Complete multiple tasks", OGL v3.0.)

---

## Appendix — Rule index

| ID | Class | Rule in one line |
| --- | --- | --- |
| IDR-01 | GEN | References are captured by selection and stored as keys — never typed names |
| IDR-02 | GEN | Identifier-first across all registered identifiers; scheme-validated; probabilistic matches always confirmed |
| IDR-03 | GEN | Attribute search → server-side disambiguation list → user selects; never auto-pick on multiple |
| IDR-04 | GEN | Selected party renders as the golden-record identity card, with conflict flag; corrected by re-search |
| IDR-05 | LINT | A list of values: no step offers more than nine values, seven the aim — more than nine in force are divided into categories of ≤9, chosen category then value (amended 25.09.2026); record sets: selection-control ladder by cardinality (200–1,000 suggest · >1,000 search dialog, tunable); 05a: global vs in-list search are distinct patterns |
| IDR-06 | REV | No matching, joining or uniqueness logic on names |
| IDR-07 | GEN | Failed search offers legitimate next steps, never free-text fallback |
| PRE-01 | LINT | Every field declares provenance; master/selected fields also declare consumption pattern |
| PRE-02 | REV | `entered` justifies itself against the whole of government (once-only) |
| PRE-03 | GEN | Objects with a source are created from the source; items selected, not typed |
| PRE-04 | GEN | Pre-filled-but-changeable → editable-with-audit; derived → read-only; mastered → corrected at owner |
| PRE-05 | REV | Nothing is re-keyed between records |
| PRE-06 | GEN | Defaults everywhere sensible — visible, changeable, audited; defaults embody the compliant path |
| CTX-01 | REV | Every screen declares its trigger; context-free menu creation is a justified exception |
| CTX-02 | GEN | Persistent header: who (golden record), what, where, how much, whose (incl. human-in-the-loop) |
| CTX-03 | GEN | 360° adjacency: case ↔ party full picture in one click |
| CTX-04 | REV | Never re-find what is already on screen |
| WRK-01 | GEN | Landing page = scoped exception queue; every row says why it was routed; STP volume is monitoring |
| WRK-02 | LINT | All lists server-side paginated, sorted, filtered |
| WRK-03 | REV | Task-relevant default sort and columns; identifier and party always present |
| WRK-04 | GEN | Default scope = mine / my office / active on first paint; never open empty; widening is explicit |
| WRK-05 | GEN | Honest counts and truncation; filter summary matches the list exactly; logged, authority-bound export |
| WRK-06 | GEN | Bulk operations: preview before, per-item verdicts after |
| STA-01 | LINT | Actions = declared transitions for this role in this state; no generic CRUD verbs |
| STA-02 | GEN | Never-available actions hidden; state-blocked actions disabled with reason |
| STA-03 | LINT | Status rendered from the state model; never editable or free-text |
| STA-04 | GEN | Consequential transitions show consequences (incl. affected counts, rights notices) + reason/approval |
| STA-05 | LINT | No physical delete on records of legal record; cancel/annul with reason |
| FIN-01 | LINT | System-originated figures are computed and read-only |
| FIN-02 | REV | External amounts entered once, at the boundary, with source reference |
| FIN-03 | GEN | Corrections are reversing/adjusting transactions, trail visible |
| FIN-04 | GEN | Every figure states as-of + source; lineage on demand; staleness flagged |
| FIN-05 | GEN | Reconciliation visible; history renders as-at its date |
| VAL-01 | GEN | Validate against reality — existence, temporal validity, period, authority — server-side, at entry; kernel validate for codes |
| VAL-02 | GEN | Errors and outcomes name the rule, the value, and the remedy |
| VAL-03 | LINT | Server enforces every rule on every path; client checks are courtesy |
| VAL-04 | GEN | Illegality blocks; anomaly warns and proceeds only with audited reason |
| VAL-05 | GEN | Drafts persist; sessions don't destroy work; submits are idempotent |
| VAL-06 | GEN | Stale updates surfaced with who-changed-what; no silent overwrite |
| AUD-01 | GEN | Who, when, what, before/after, under which authority — on everything |
| AUD-02 | LINT | Discretion requires a coded reason as precondition; automated-override is a named class feeding AUT-07 |
| AUD-03 | GEN | History is a readable chronological screen; each entry says who/what + when (Timeline, D.5); control side (AUD-02) is original |
| AUD-04 | REV | Sensitive access scoped and view-logged where required; masked values visibly masked |
| PRD-01 | REV | Top tasks ≤ 3 interactions, keyboard-completable; STP rate, time-to-certainty, effort measured |
| PRD-02 | GEN | Every completion offers the natural next step |
| PRD-03 | REV | Collapse detail, never identity/status/money; density is persona-specific — dense expert officer UX ≠ citizen one-thing-per-page |
| PRD-04 | GEN | Long work runs async; degraded dependencies degrade gracefully per declaration |
| TRM-01 | REV | Statutory vocabulary only; unknown terms are questions, not guesses |
| TRM-02 | GEN | A coded value shows its label only (its code, where the list is marked `display_code`), stores its code; resolve as-at via the kernel (amended 25.09.2026) |
| TRM-03 | GEN | Typed tax periods; uniform legal formats for dates, numbers, money |
| TRM-04 | LINT | All user-facing text externalised, multilingual-ready |
| MDM-01 | LINT | Every code list names its register entry; the register is the allowlist |
| MDM-02 | GEN | Shared vocabulary consumed read-only via the catalogue; module Admin = own config only |
| MDM-03 | GEN | Pickers filter by validity as-at the transaction's effective date |
| MDM-04 | GEN | Store code + as-of date; render via resolve; history never re-labelled |
| MDM-05 | GEN | Consumption pattern declared and visible: fail-closed / freshness-stamped cache / frozen snapshot |
| MDM-06 | GEN | Party screens show the golden record; survivorship on demand; conflicts flagged |
| MDM-07 | GEN | One fact, one writer — mastered attributes read-only outside the owner, with correction route |
| MDM-08 | GEN | Search all identifiers; show which matched; probabilistic matches always confirmed |
| MDM-09 | GEN | Match/merge/unmerge are governed screens with evidence and impact preview |
| MDM-10 | GEN | Change events flag open work referencing changed values or parties |
| MDM-11 | REV | ⚑ Scoped catalogues render scoped pickers (reason codes by domain+context) |
| MDM-12 | REV | ⚑ Look-alike vocabularies never merge on screen (no generic "risk level") |
| MDM-13 | GEN | Vocabulary change is a case: steward console with four-eyes and impact preview |
| MDM-14 | GEN | Quality gates surface as steward worklists with drill-down and resolution actions |
| MDM-15 | GEN | Crosswalks are governed screens; internal + mapped external code with version |
| AUT-01 | REV | Every human action classified automate / assist / decide; rubber-stamps deleted |
| AUT-02 | GEN | Exception items carry why-flagged, what-to-decide, criteria and context |
| AUT-03 | GEN | Green-lane volume is monitoring, never workable rows; samples labelled |
| AUT-04 | GEN | Decisions, not reports: criteria and routing embedded; no export-to-decide |
| AUT-05 | GEN | Automated outcomes explainable: inputs, rule + version, outcome — reproducible |
| AUT-06 | GEN | AI renders as marked suggestions with basis; accountable human named |
| AUT-07 | GEN | Exception resolution offers structured rule feedback to governance |
| AUT-08 | GEN | Source assurance displayed; no per-transaction re-checking of assured sources |
| TPX-01 | REV | The filing ladder: eliminate → pre-fill → complete (justified); citizen default = one thing per page + check-answers (opposite of PRD-03) |
| TPX-02 | GEN | The taxpayer's home is the single account position with live status |
| TPX-03 | GEN | Every automated/adverse outcome carries explanation + challenge path with deadlines |
| TPX-04 | GEN | Compliant by default; deviation deliberate, honest, traced |
| TPX-05 | GEN | Acting-for visible: who, for whom, under what scope; dual attribution |
| TPX-06 | REV | Assisted channel of equal outcome; ACC family met |
| TPX-07 | GEN | Friction instrumented; effort measured and designed out |
| ACC-01 | LINT | Conformance target (WCAG 2.2 AA / EN 301 549) declared and gated at acceptance |
| ACC-02 | GEN | Keyboard-complete: focus visible, order logical, no traps, shortcuts on frequent paths |
| ACC-03 | GEN | Programmatic labels, table headers, announced status; never colour alone |
| ACC-04 | GEN | Accessible errors (text, associated, remedied); warn-and-extend time-outs |
| ACC-05 | REV | Contrast in all states; readable and operable at 200% zoom; density is a setting |
| ACC-06 | REV | Keyboard-only and screen-reader passes in acceptance for top tasks |
| CNT-01 | REV | Plain language for people, legal basis alongside; defined reading level |
| CNT-02 | GEN | Notices carry decision, explanation, amounts, challenge path, contact; merge fields validated; vocabulary frozen |
| CNT-03 | GEN | Help and guidance render from configured rules, never hardcoded prose |
| CNT-04 | REV | Every question states its why (legal basis); unjustifiable questions removed |
| CNT-05 | GEN | One concept, one name — across screens, notices and channels |
| CNT-06 | REV | Translation parity with legal-equivalence review from one glossary |
| DSH-01 | REV | Every dashboard declares its decision and audience; decision-less tiles removed |
| DSH-02 | GEN | KPIs link to their governed metric spec; computed once, same value everywhere |
| DSH-03 | GEN | Thresholds/RAG from configuration; text + colour; consistent everywhere |
| DSH-04 | GEN | Drill-down preserves context; aggregates reconcile to their record lists |
| DSH-05 | GEN | Charts server-computed from governed queries; as-of stamped |
| DSH-06 | REV | Operational dashboards link into worklists; monitoring and work are one world |

*UX-01 · v1.3 · 13 July 2026 — companion: UX-02 v1.3. Amendments A1/A2 absorbed; evidence rounds 1–2 (UX-03) folded in; Round 3 deprioritised per Annex C; additions follow Annex B.3.*
