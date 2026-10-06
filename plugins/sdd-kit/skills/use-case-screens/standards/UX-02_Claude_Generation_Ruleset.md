# UX-02 · Generation Ruleset — Enterprise UI for Public-Sector Back Office

*This copy is carried by sdd-kit, the SDD method's skills for the service design course. It keeps the edition stated below; where the edition drew an example from the method's author's own client work, this copy carries an example set in Progressa in its place and says so where it does.*

**Version 1.4 — 28 September 2026, in force.** This is the single source of UX-02 in this kit. Raised from v1.3 (13 July 2026) to carry the owner's two rulings of 25 September
2026, already in this text — IDR-05 (a selection offers no more than nine values; a longer list
is divided into categories) and TRM-02 (a coded value shows its label only, its code where the
list is marked `display_code`) — and to give this changed text an edition number of its own, so
that a skill's pin (`04_TARGET_STATE.md` §5) can tell it apart from v1.3. The superseded v1.3 is
archived at `x_archive/2026-09-28-UX-02-v1.3-superseded-by-v1.4/`.

> **What this file is.** The operational extract of UX-01 (Enterprise UX Standard), written in the imperative, for an AI coding assistant. Install it in the implementation repo as a `CLAUDE.md` section (paste or `@`-include) or as a skill that triggers on any screen / form / list / case / workflow work. Rule IDs (IDR-, PRE-, …) match UX-01, where each rule carries its rationale and examples.
>
> **The contract in one line:** you MUST produce the Screen Derivation Table (§2) before generating any screen artefact, you MUST record gaps as TO-CONFIRM instead of inventing, and you MUST self-review against §5 before delivering.

---

## 1. The mental model (read first, apply always)

You are building **officer-facing screens over a system of record at national scale** — millions of parties, tens of millions of transactions, acts with legal effect. This changes everything about how screens are designed:

- **You are not creating data; you are exposing it.** Nearly every value a screen shows already exists — in the ledger, the register, the source document, the reference tables. A screen is a *view plus a decision*, not a questionnaire. If you find yourself drawing many empty input boxes, stop: you have almost certainly missed a source.
- **Records are found by keys, not names.** Names are never unique in a national register. Identification runs identifier-first (TIN, case number, document number), attribute-search as fallback, always ending in an explicit selection.
- **Records have lifecycles, not Edit buttons.** What a user may do is defined by the state machine and their role — never by generic CRUD verbs.
- **Money belongs to the accounting layer.** Officers never type amounts the ledger knows. Corrections are new transactions.
- **The interaction may not need to exist.** Automation is the default; a human step exists only where judgement adds value. Never generate approval screens that confirm what a rule already decided, report viewers where a decision workflow belongs, or forms re-collecting what any government register holds. Sometimes the correct output is a design-change request, not a screen.
- **When the spec is silent, you ask — you never invent.** A made-up status set, threshold, or behaviour is a defect even if it looks plausible. Record it as `TO-CONFIRM: <question> — owner: <who>` and proceed on what is confirmed.

---

## 2. MANDATORY: the Screen Derivation Table

Before generating ANY screen, form, list, or wizard — produce this analysis and include it in your output. **Generating screen artefacts without it is a method violation.**

```
SCREEN: <name>
0. Existence test   . why must this interaction exist? FATAL if it: re-collects what
                      any register/feed holds (once-only) · only confirms what a rule
                      determined (rubber stamp) · is a report standing in for a decision
                      workflow · captures an event that belongs in its natural system.
                      If fatal → raise a design-change request / TO-CONFIRM, don't draw it.
1. Persona & moment . who uses it, in which lifecycle state, in which process step
2. Trigger & source . what opens it (worklist item / action on record / event /
                      schedule / menu-with-justification) and what record it carries
3. Knowledge inventory. EVERYTHING the system already holds at this moment:
                      source-record fields, party master data, ledger positions,
                      related cases, reference data. This list is what pre-fills.
4. Fields           . table: field | binding | provenance | editability | validation
5. References       . per reference field: mechanism (§3) + search keys + result columns
6. Volumes          . P50/P99 rows for each list/query → page size, caps, refine threshold
7. Actions          . each button → transition + role + guard, or tagged non-lifecycle
8. Failure & absence. source down/stale/empty → what shows; each error → rule, value, remedy
```

**Provenance vocabulary (step 4)** — every field gets exactly one:

| Provenance | Meaning | Editability default |
| --- | --- | --- |
| `system` | generated (IDs, timestamps) | read-only |
| `derived` | computed (totals, ages, categories) | read-only, recomputes |
| `source` | pre-filled from the triggering record | read-only or editable-with-audit |
| `master` | pre-filled from master/reference data | read-only here; corrected at its owner |
| `selected` | chosen from lookup/search over existing records | re-selectable |
| `entered` | typed — exists nowhere in the system | editable — **requires a written justification** |
| `external` | captured from an outside document at the boundary | editable once, with source reference |

**Kernel columns (MDM):** for every `master` or `selected` field also record: the list's **register entry** (bucket R/M/C/P + ID — the Master & Reference Data Register is the allowlist; an unknown list is a TO-CONFIRM to data governance, never a new local list), the **consumption pattern** (`sync-validate` / `cached-projection` / `frozen-snapshot`), and the attribute supplying the **effective date** for validity filtering.

**The ratio test:** a healthy officer screen has few `entered` fields (notes, decisions, negotiated terms). If `entered` dominates, you have designed an amnesiac form — go back to step 3.

---

## 3. Reference fields: the selection-mechanism table

Never decide field type by habit. Decide by the referenced set:

| Referenced set | Size/growth | Mechanism |
| --- | --- | --- |
| Code list / vocabulary (tax types, districts, reasons) | bounded, stable | **no step offers more than nine values (seven the aim):** ≤9 in force → radio/select · more than nine → divided into categories of ≤9, chosen in two steps, category then value (more than nine categories → another level) — each value shown by its label only (by its code where the list is marked `display_code`; TRM-02, amended 25.09.2026) |
| Configured registry (offices, officers-in-team) | bounded, slowly changing | filtered dropdown or picker |
| Operational entities (**taxpayers, cases, documents, properties, bank accounts, addresses**) | unbounded, grows with operations | **search dialog or server-side type-ahead**: identifier-first, attribute fallback, min 2–3 chars, result cap + "refine", disambiguation columns (ID · name · type · status), explicit selection, identity card after selection, FK stored |

Hard rules: multiple matches are NEVER auto-picked (IDR-03). A failed search offers next steps, never a free-text fallback (IDR-07). No matching or uniqueness logic on names, ever (IDR-06). Options for shared lists come from the **central catalogue (kernel)**, validity-filtered as-at the transaction's effective date — never from a module-local copy (MDM-02/03).

---

## 4. The non-negotiables

**Identification & reference**
- IDR-01 Any reference to another record = selection from search/lookup, stored as key. Never a typed name.
- IDR-02 Identifier-first (TIN / case no / document no), scheme-validated at entry (format, check digit), failure names the rule.
- IDR-05 No step of a selection offers more than nine values; seven is the aim. A list of values with more than nine values in force is divided into categories of ≤9: the person chooses the category, then the value (more than nine categories → another level). Record sets by size (tunable): 200–1,000 suggestions · >1,000 search dialog; start with the least complex that fits. IDR-05a: global find (recents on focus, top matches no-Enter, icon/type+name disambiguation) and in-list narrowing (exposed input, per-keystroke filter, scope in placeholder, no autocomplete) are distinct patterns (§3).

**Provenance & pre-fill**
- PRE-01 Every field declares provenance (§2). No provenance column → the design is incomplete → do not build.
- PRE-03 Objects with a source are created FROM the source: entry point on the source record (or automatic from the event); keys, party, periods, amounts, line items carried in; where discretion applies the officer **selects among source items** (checkboxes), never re-types them. No blank-form creation of cases, assessments, refunds, agreements.
- PRE-04 Pre-filled-but-changeable = editable **with audit**; derived = read-only with recompute.
- PRE-06 Default everything sensible (today, my office, current period) — visibly, changeably.

**Context**
- CTX-02 Every record screen has a persistent context header: party identity card · record type+number · status+since · key figures · assigned officer.
- CTX-03 Case → party 360° in one click; never re-find what is already on screen (CTX-04).

**Worklists & volume**
- WRK-01 Officer landing page = personal worklist (identifier, party, amount, priority, due, SLA traffic light) — not a menu.
- WRK-02 Every list: server-side pagination, sorting, filtering. No unbounded fetch, no client-side filter-after-load-all.
- WRK-04 Default scope = my items / my office / active. WRK-05 show honest counts ("50 of 12,431 — refine or export").
- WRK-06 Bulk actions: preview before commit, per-item verdicts after.

**State & actions**
- STA-01 Buttons = declared lifecycle transitions for this role in this state. No generic Edit/Save/Delete on cases, filings, assessments, agreements.
- STA-02 Role-impossible actions hidden; state-blocked actions disabled **with the reason**.
- STA-03 Status is rendered from the state model — never an editable or free-text field.
- STA-04 Consequential transitions show consequences (notices sent, balances moved, deadlines started) + reason/approval per policy. "Are you sure?" alone is theatre.
- STA-05 No physical delete on records of legal record — cancel/annul/withdraw with reason, history preserved.

**Money & figures**
- FIN-01 Ledger-owned figures (balances, arrears, interest, penalties, totals, categories, ages) are computed and **read-only**. An officer typing an amount the ledger knows is a defect.
- FIN-03 Corrections = reversing/adjusting transactions with reason; the trail is visible.
- FIN-04 Every figure states its as-of moment and source ("per the revenue ledger as of 13.07 06:00"); stale data is flagged.

**Master & reference data (kernel)**
- MDM-01 Every code list binds to a register-classified entry (bucket R/M/C/P + ID). Never invent a local list; never define locally what the register classifies as shared.
- MDM-02 Modules consume shared vocabulary read-only from the central catalogue — no per-module CRUD screens for shared lists (no `mdTaxType`-style forms in every module); a module's Admin section holds only its own configuration.
- MDM-03/04 Pickers offer only values valid as-at the transaction's effective date; store code + as-of date, render the label via resolve(as-at); issued documents freeze their vocabulary and are never re-resolved.
- MDM-05 Declare each field's consumption pattern and show it: boundary validation fails closed with the rule named; cached views show freshness and keep working through a kernel outage; snapshots are labelled as-issued.
- MDM-06/07 Party screens render the golden record, with survivorship provenance and conflict flags; mastered attributes are read-only outside the authoring module — offer "report a correction" routed to the owner, never a local edit.
- MDM-08/09 Party search covers all registered identifier types and shows which identifier matched; probabilistic matches are confirmed by the user, never auto-picked; merge/unmerge are governed acts with match evidence and an impact preview.
- MDM-10 Change events reach open work: cases referencing deprecated values or changed party data are flagged, not silently stale.
- MDM-11/12 Reason pickers are scoped by (domain, context) — never the global list; look-alike vocabularies (refund risk band / audit tier / risk category / debt C1–C5) never merge into one generic "risk level" control.

**Automation, exceptions & taxpayer touchpoints**
- AUT-01/04 Classify every action: automate / assist / decide. No rubber-stamp approvals of rule-determined outcomes; decision screens embed criteria and routing — never "export and decide elsewhere".
- AUT-02/03 Every exception/worklist row says WHY automation routed it (rule, threshold, anomaly — in words) and what is to be decided; straight-through volume is monitoring counts, never openable rows.
- AUT-05/06 Automated outcomes (assessments, flags, holds, routings) are explainable on demand: inputs, rule + version, outcome. AI contributions render as marked suggestions with their basis; the accountable human (override / review / answers the taxpayer) is named.
- AUT-07/08 Exception resolution offers structured rule feedback (false positive / threshold wrong / new pattern); data from assured sources shows its source and assurance status — no per-transaction re-checking screens for assured sources.
- TPX-01/02 Taxpayer interactions design down the ladder: eliminate → pre-fill & confirm → complete (last resort, justified); when the citizen must complete something, default to ONE thing per page + a check-answers summary + a confirmation page. This is the OPPOSITE of officer screens, which are dense, fast and keyboard-first — never apply "one thing per page" to a back-office screen; density follows the persona (PRD-03). The taxpayer's home is their single account position: assessed, paid, due, in-progress status.
- TPX-03/04 Every automated or adverse outcome carries its explanation AND its challenge path (what to do if you disagree, with deadlines). Defaults embody the compliant path; deviation is possible, deliberate, traced.
- TPX-05/06 Acting-on-behalf is visible on every screen (who, for whom, under what scope); every automated journey has an assisted channel of equal outcome; accessibility standards met.

**Accessibility, content & dashboards**
- ACC-02/03/04 WCAG 2.2 AA is the baseline. Keyboard-complete everything (visible focus, logical order, no traps — including search dialogs and grids); programmatic labels; errors announced and associated to fields; status never conveyed by colour alone (traffic lights carry text/symbol); time-outs warn, extend, and never destroy work.
- CNT-01/02 A notice states what happened, what it means, what to do, by when — plain language, legal basis alongside. Every notice template carries: decision + explanation, amounts with computation summary, challenge path with deadlines, contact/assisted channel; merge fields validate against the data model; vocabulary freezes as-issued.
- CNT-03/05 Help and guidance render from the configured rules (rates, deadlines) — never hardcoded prose that drifts; one concept has one name across screens, notices and channels.
- DSH-01/02/05 Every dashboard tile serves a declared decision for a declared audience; KPIs bind to their governed metric spec — computed once in the semantic layer, as-of stamped, same value everywhere; charts come from server-side queries, never client-side scraping or recomputation.
- DSH-04/06 Drill-down preserves filters and reconciles aggregate ↔ record list; operational dashboards link into worklists — monitoring and work are one world.

**Validation & errors**
- VAL-01 Validate against reality — existence, active status, open period, authority — server-side, at entry/selection. Format-only checks are theatre.
- VAL-02 Every error names the rule, shows the value, states the remedy. "Invalid input" is forbidden.
- VAL-03 Server enforces every rule on every path (screen, API, bulk); client checks are courtesy.
- VAL-05 Drafts persist; session expiry loses nothing; submits are idempotent. VAL-06 stale updates surface who-changed-what; no silent overwrite.

**Audit & discretion**
- AUD-01 Every act logs who, when, what (before/after), under which authority — platform-level, not per-screen effort.
- AUD-02 Discretionary acts (waive, override, reassign, reopen, manual anything) require a coded reason as a **precondition** of the act.

**Terminology**
- TRM-01 Use the administration's statutory vocabulary. An unknown term is a question (TO-CONFIRM), never a guess.
- TRM-02 A coded value shows its label only — never `code — label`, never the bare code — and the code is stored; a list marked `display_code` (its code is what officers read) shows the code instead (amended 25.09.2026, on the owner's word). TRM-03 tax periods are typed values, never free date pairs. TRM-04 no hardcoded user-facing literals — language resources only.

---

## 5. Self-review checklist (run before delivering; report violations found → fixed)

1. Derivation Table produced first, with provenance for every field? Any silent invention? (AP-13 — if yes, convert to TO-CONFIRM now.)
2. Any typed name where a reference belongs? Any dropdown over an unbounded set? Any step of a selection offering more than nine values? (AP-01, AP-04, IDR-05)
3. Any field asking for what the system holds — lines, balances, addresses, obligations? (AP-02 — the amnesiac form)
4. Any case/document creatable from a blank form with no source? (AP-03)
5. Any list without server-side paging, task-relevant default sort, scoped default filter? Works at 10⁶ rows? (AP-05)
6. Any editable status, generic Edit/Delete on lifecycle records, or physical delete? (AP-06, AP-08, AP-09)
7. Any typed or overridable ledger figure? Corrections as edits instead of transactions? Missing as-of stamps? (AP-07)
8. Any format-only validation? Any "Invalid input"-grade message? (AP-11)
9. Any consequence-free "Are you sure?" on a consequential act — or ritual confirmation on a routine one? (AP-10)
10. Every button mapped to a transition+role+guard or tagged non-lifecycle? Blocked actions explain themselves? (STA-01/02)
11. Persona and trigger declared? Context header present? 360° one click away? (AP-12, CTX-02/03)
12. Discretionary actions demand coded reasons? Everything audited? (AUD-01/02)
13. Statutory terms, code+label rendering, typed periods, externalised text? (TRM-01…04)

14. Any locally defined list the register classifies as shared? Any dropdown fed from a module copy instead of the central catalogue? Any picker ignoring effective-date validity? (MDM-01/02/03)
15. Party views showing a non-golden record, editable mastered attributes outside Registration, unscoped reason pickers, or a merged "risk level" control? (MDM-06/07/11/12)
16. Should this screen exist at all — or is it a rubber-stamp, a report surrogate, or a re-collection form? (Q0; AP-15/16/17)
17. Do exception rows say why they exist? Do automated outcomes explain inputs + rule + version — and, taxpayer-facing, the challenge path? (AUT-02/05, TPX-03)

18. Colour-only status indicators? Unlabelled fields? Keyboard-incompletable dialogs? Notices missing the challenge path? KPI tiles without a governed definition or as-of stamp? (ACC-02/03, CNT-02, DSH-02/05)

**Output discipline:** list each violation found as `AP/rule-ID → what was wrong → how fixed`. Zero findings on a non-trivial screen is suspicious — look again at 2, 3 and 5.

---

## 6. Quick reference for Progressa's higher-education services

*A simulated case for Progressa, a fictional country; every institution, name and figure in it is invented. In this copy it replaces the edition of record's quick reference, which was drawn from the corpus of a real programme.*

- **Identity spine:** an institution's register number (written like INS-00217) is the identifier; its name is a display attribute, changed only on the minister's approval. Institution search = register number direct, or a fragment of the name → disambiguation list (register number · name · kind · licence state) → select → identity card. A person is identified by the national identity authority's sign-in, which gives each service its own identifier; no screen asks for or keeps the national number.
- **Facts live where they are kept:** the register of institutions is PHEQA's; MoEYS reads it across the information-mediation block and keeps no copy. The application fee lives in the setting PHEQA's finance officer owns, and its payment in the Payments block's confirmation. Screens read them, stamp them as-of, and never re-type them.
- **Cases come from sources:** an inspection ← an application accepted as complete (created with the application's number, the institution, the kind of licence and the version of the standards — automatically, onto the inspectors' worklist). A recommendation ← an inspection recorded. A decision to record ← the minister's decision received from MoEYS. An appeal ← the disputed decision of PHEQA. A change of name ← the minister's approval.
- **The exemplar screen:** applying for a provisional licence — the applicant signed in (identity auto-populated), PHEQA's standards read from their setting in the version in force, the kind of institution chosen from the shared list, only the particulars the regulations list entered, the fee read from its setting and paid through the Payments block, a receipt with the application's number. Imitate its shape: *identify → auto-populate → decide → compute → route.*
- **Worklist norms:** personal queue as landing page; columns: application number, institution, kind of licence, date received, next action due; red = overdue, amber = due in 24h; quick actions on the row; the Registrar sees the team's queue with each officer's load; reassignment demands a reason.
- **Statuses are FSM-driven** (a licence: granted → suspended → cancelled, each move on the minister's decision and recorded by the registration officer; a cancellation set aside on appeal or on review returns the licence to the state it held before) — render transitions, guards and reasons from the model.

*UX-02 v1.4 — extract of UX-01 v1.3 (consolidated: base + MDM + TA 3.0 + ACC/CNT/DSH + evidence rounds 1–2), amended 25 September 2026 on the owner's word (IDR-05, TRM-02) and given its own edition on 28 September 2026 when it became this estate's single source. When a rule here seems to conflict with an explicit requirement in the module spec, the module spec wins — and the conflict is reported, not silently resolved.*
