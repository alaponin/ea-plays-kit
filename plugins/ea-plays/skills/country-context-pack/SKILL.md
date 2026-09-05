---
name: country-context-pack
description: >-
  Build the A0 country context pack — the seven-section input every play in this course
  consumes, sourced from public records rather than pasted from memory. Run it once per
  country and sector, before any other play. Returns: a digital-landscape brief (feeds 1.1,
  1.2); a programme list with budget envelopes and building-block needs (1.3, 1.5); the
  ministry operating context and constraints (1.4); an institutional roles register by post
  with confirmed/partial/gap tags (1.6, 1.7); a country-characteristics one-liner (1.8, 5.1);
  the public bodies, systems and registries table (2.1, 2.4, 2.5, 4.1); and the legal and
  policy list (2.3, 1.7). Use when someone says "build my country context", "run Play 0",
  "I need the input for play 1.1", "what do I paste into this prompt", "research [country]
  for an EA assessment", "country brief for digital government", or asks any play's question
  without having the context to hand. Reads World Bank, ITU DataHub, UN EGDI, national budget
  documents and donor project documents; every claim carries a URL, tier and date; posts, never
  names. Plays run bare in any assistant; this makes their input real.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
---

## What this skill does

Produces **A0 — the country context pack**, the artefact at the head of the workbook
chain, in the seven sections the plays consume. Every play in the course opens by asking
the learner to paste context they do not have; this is the step that builds it.

It serves **Play 0**, and through A0 it serves every other play. Plays run bare in any
assistant — with this skill their input is sourced and dated instead of remembered.

## Inputs

The country name, and the sector if the learner has one (education, health, social
protection, agriculture, tax…). Nothing else. If no sector is given, build §1–§5 and §7
whole-of-government and ask which sector before building §6.

Ask at most three clarifying questions, all at once, and record the answers in the pack —
see `references/output-contract.md` §4.

## Procedure

Build the sections in order. Each is self-contained: a learner who needs only §4 can be
given §4 alone, with the provenance header.

1. **§1 Digital-landscape brief** — four paragraphs: connectivity and affordability; the
   digital-government strategy in force and the body that owns it; the identity programme
   and any cross-agency systems (data exchange, payments, civil registration); maturity and
   gaps against a published index. Sources: ITU DataHub and A4AI (connectivity, T1); the
   ministry's own publications page (strategy, T1); UN EGDI and the World Bank GTMI
   (maturity, T1); ID4D and the operator's own site (identity, T1). Name institutions,
   systems and documents with the year of each.

2. **§2 Programme list** — three to five current or planned programmes in the sector, each
   with status, year, funder and budget envelope, lead body, and which of identity,
   payments, data exchange, registration and consent it needs. Sources: the **national
   budget document** and the ministry's annual plan (T1); **World Bank PADs and ICRs**,
   AfDB and Global Fund project documents (T2) — a PAD describes systems in unusual detail.
   Read a PAD as intent and an ICR as outcome; say which you are using.

3. **§3 Ministry operating context** — institutional structure and degree of
   decentralisation; policy framework and sector plan; legal, financial (including donor
   dependence and any documented PFM failure), technical, data and human-resource
   constraints; political context. End with one paragraph on **what is absent from the
   public record**. That paragraph is not padding — it is what stops the next play
   inventing the missing part.

4. **§4 Institutional roles register** — by post. The CDO/CTO or political equivalent; the
   head of the civil service; the national ICT or e-government agency and its board; sector
   ministry CIOs; any existing EA function or chief architect; any cross-government
   governance board; the procurement authority; the data-protection regulator; the budget
   authority; the government CISO; the interoperability-standards function. Each with
   institution, one-line mandate, and a status tag — **confirmed** (exists, post filled),
   **partial** (exists but unclear or unstaffed), **gap** (does not exist). End with the
   roles an EA programme needs that are missing.

   Sources will hand you the names of current holders. **Drop them at the point of
   writing.** The August 2026 test runs put real office-holders into this register and into
   the RACI downstream; that is the failure this rule exists to prevent.

5. **§5 Country characteristics one-liner** — one paragraph, for comparator search:
   population; income classification; governance type and sub-national autonomy; region and
   regional bodies; digital-government maturity with the index rankings; state of national
   ID, civil registration, data exchange and payments; the coordinating digital body and
   whether its mandate is binding; budget-cycle constraints; main donors; whether an EA
   function or board exists.

6. **§6 Public bodies, systems and registries** — for the sector: ministry or ministries,
   examinations or regulatory bodies, registries, and the shared-platform providers. Each
   with mandate, known systems, known registries, and confirmed/inferred. **Where a body
   you would expect does not appear to exist, say so** — an absence is a finding.
   For a deeper register with legal mandates and a PAERA classification, hand off to
   `ea-institution-mapper`.

7. **§7 Legal and policy list** — data-protection act, procurement law and e-procurement
   rules, e-government or digital-transactions act or decree, access-to-information act,
   the sector act, and the strategies in force. Each with title, year, status, owning body,
   and the one constraint it places on a data-sharing or shared-platform design. For the
   full register with citations and the regulators created, hand off to `ea-legal-context`.

8. **Run `cite-or-discard` on the whole pack** before returning it. A0 is the input to
   every play; a fabricated URL here propagates into thirty-seven artefacts.

9. **Date-stamp it.** A0 goes stale. Say so in the output: re-run before it is six months
   old, and re-run §6 and §7 sooner if a programme or a bill is moving.

## Output contract

Provenance header first (`references/provenance-header.md`), then the seven sections,
each under a heading that names the section number and the plays it feeds:

```
## §4 Institutional roles register — feeds 1.6, 1.7
```

§2, §4, §6 and §7 are tables. §1, §3 and §5 are prose. Every claim carries its URL, tier
and access date **inline in the row or the sentence**, not in a bibliography.

Text in the chat. No file, no chart. **Posts, never names.** No reasoning before the
header. See `references/output-contract.md`.

Where a section cannot be built — no public budget document, no law portal — return the
section with the heading, the reason, and what the learner should ask for internally.
A missing section is not a reason to omit the heading; the next play looks for it.

## Safeguard handed back

A0 is the public record, and the public record is thin, dated and sometimes wrong.
Before the pack carries a play into a briefing:

- **§2 budgets**: confirm the envelope with the budget department. Donor documents state
  approved amounts, not disbursed ones.
- **§4 status tags**: a post that exists on an organogram may be vacant. Confirm the
  *partial* and *gap* rows with someone inside.
- **§6 and §7**: confirm each body's mandate against its establishing instrument, and each
  law's status against the gazette — a bill in the public record may have been enacted or
  dropped since.
- Anything the pack marks ⚠ or "absent from the public record" is your homework, not a
  finding.

## References

- `references/api-guide.md` — query patterns and indicator codes for the statistical APIs
  (World Bank, UNESCO UIS, UN SDG, ITU DataHub, UNICEF, Giga). Inherited from
  `country-context-data`; load it when §1 or §5 needs a figure.
- `references/source-selection.md` — which source answers which question. Inherited.
- `references/a0-sections.md` — the seven sections' exact columns and the play each feeds.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` — the shared contract.
