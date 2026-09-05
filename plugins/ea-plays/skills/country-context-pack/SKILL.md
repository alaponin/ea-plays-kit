---
name: country-context-pack
description: >-
  Build the A0 country context pack. This is the seven-section input that each play in this
  course uses. It comes from public records, not from memory. Run it one time for each
  country and sector, before any other play. It gives: a digital-landscape brief (feeds 1.1,
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

This skill makes **A0 — the country context pack**. A0 is the first artefact in the
workbook chain. The pack has the seven sections that the plays use.

Each play in the course starts when it asks the learner to paste context. The learner does
not have that context. This is the step that builds it.

The skill serves **Play 0**. Through A0 it serves each other play. The plays run bare in
any assistant. With this skill, their input has sources and dates. It does not come from
memory.

## Inputs

The skill needs the name of the country. It also needs the sector, if the learner has one:
education, health, social protection, agriculture, or tax. It needs nothing more.

If the learner gives no sector, build §1 to §5 and §7 for all of government. Then ask for
the sector before you build §6.

Ask a maximum of three questions, all at the same time. Record the answers in the pack.
See `references/output-contract.md` §4.

## Procedure

Build the sections in order. Each section is complete in itself. If a learner needs only
§4, you can give §4 alone with the provenance header.

1. **§1 Digital-landscape brief** — write four paragraphs: connectivity and affordability;
   the digital-government strategy in force and the body that owns it; the identity
   programme and any systems that cross agencies, such as data exchange, payments and civil
   registration; maturity and gaps against a published index. Sources: ITU DataHub and
   A4AI for connectivity (T1); the publications page of the ministry for the strategy (T1);
   UN EGDI and the World Bank GTMI for maturity (T1); ID4D and the site of the operator for
   identity (T1). Give the year with each institution, system and document.

2. **§2 Programme list** — list three to five programmes in the sector that are current or
   planned. Give the status, the year, the funder, the budget envelope and the lead body
   for each one. Also give which of these each programme needs: identity, payments, data
   exchange, registration and consent. Sources: the **national budget document** and the
   annual plan of the ministry (T1); **World Bank PADs and ICRs**, and AfDB and Global Fund
   project documents (T2). A PAD describes systems in unusual detail. A PAD gives the
   intent and an ICR gives the outcome. Say which one you use.

3. **§3 Ministry operating context** — give the institutional structure and the level of
   decentralisation. Give the policy framework and the sector plan. Give the legal,
   financial, technical, data and human-resource constraints. Include donor dependence and
   any PFM failure in the record. Give the political context. End with one paragraph on
   **what the public record does not contain**. That paragraph has a function: it stops the
   next play from inventing the part that is missing.

4. **§4 Institutional roles register** — record each role by post. Include the CDO or CTO
   or the political equivalent; the head of the civil service; the national ICT or
   e-government agency and its board; the CIOs of the sector ministries; any EA function or
   chief architect that exists; any governance board that crosses government; the
   procurement authority; the data-protection regulator; the budget authority; the
   government CISO; and the function for interoperability standards. Give the institution,
   a mandate of one line, and a status tag for each post. The status tags are **confirmed**
   if the post exists and a person holds it, **partial** if the post exists but is unclear
   or has no staff, and **gap** if the post does not exist. At the end, list the roles that
   an EA programme needs and the country does not have.

   Sources give you the names of the persons in the posts. **Remove these names when you
   write.** The August 2026 test runs put the names of real office-holders into this
   register, and then into the RACI. This rule prevents that failure.

5. **§5 Country characteristics one-liner** — write one paragraph for the comparator
   search. Give the population; the income classification; the type of governance and the
   level of sub-national autonomy; the region and its regional bodies; the digital-
   government maturity with the index rankings; the state of the national ID, the civil
   registration, the data exchange and the payments; the digital body that coordinates, and
   whether its mandate binds other bodies; the constraints of the budget cycle; the main
   donors; and whether an EA function or board exists.

6. **§6 Public bodies, systems and registries** — for the sector, list the ministry or
   ministries, the bodies for examinations or regulation, the registries, and the providers
   of the shared platforms. Give the mandate, the known systems and the known registries
   for each one. Mark each entry confirmed or inferred. **If a body that you expect does
   not exist, say so.** An absence is a finding. For a deeper register with legal mandates
   and a PAERA classification, use `ea-institution-mapper`.

7. **§7 Legal and policy list** — list the data-protection act, the procurement law and the
   e-procurement rules, the e-government or digital-transactions act or decree, the
   access-to-information act, the sector act, and the strategies in force. Give the title,
   the year, the status and the owning body for each one. Also give the one constraint that
   each one puts on a design for data sharing or a shared platform. For the full register
   with citations and the regulators that each law creates, use `ea-legal-context`.

8. **Run `cite-or-discard` on the full pack before you give it to the learner.** A0 is the
   input to each play. One invented URL here goes into thirty-seven artefacts.

9. **Put the date on it.** A0 goes stale. Say so in the output. Tell the learner to run it
   again before it is six months old, and to run §6 and §7 again sooner if a programme or a
   bill moves.

## Output contract

Write the provenance header first (`references/provenance-header.md`). Then write the
seven sections. Each heading gives the section number and the plays that the section
feeds:

```
## §4 Institutional roles register — feeds 1.6, 1.7
```

Write §2, §4, §6 and §7 as tables. Write §1, §3 and §5 as prose. Each claim carries its
URL, tier and access date **in the same row or the same sentence**. Do not use a
bibliography.

Write text in the chat. Do not make a file or a chart. **Posts, never names.** Write no
analysis before the header. See `references/output-contract.md`.

You can be unable to build a section, because there is no public budget document or no law
portal. Then give the section with its heading, the reason, and what the learner must ask
for inside the government. A section that you cannot build is not a reason to remove the
heading. The next play looks for the heading.

## Safeguard handed back

A0 is the public record. The public record is thin, it is not current, and sometimes it is
wrong. Do these steps before the pack goes into a briefing:

- **§2 budgets**: confirm the envelope with the budget department. Donor documents give
  the amounts that were approved, not the amounts that were paid.
- **§4 status tags**: a post on an organogram can have no person in it. Confirm each
  *partial* row and each *gap* row with a person inside the government.
- **§6 and §7**: confirm the mandate of each body against its establishing instrument.
  Confirm the status of each law against the gazette. A bill in the public record can have
  become law, or can have stopped, after the record was written.
- Each item that the pack marks ⚠ or "absent from the public record" is work for you. It
  is not a finding.

## References

- `references/api-guide.md` — the query patterns and indicator codes for the statistical
  APIs (World Bank, UNESCO UIS, UN SDG, ITU DataHub, UNICEF, Giga). Inherited; read it when
  §1 or §5 needs a figure.
- `references/source-selection.md` — which source answers which question. Inherited.
- `references/a0-sections.md` — the exact columns of the seven sections, and the play that
  each section feeds.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` — the shared contract.
