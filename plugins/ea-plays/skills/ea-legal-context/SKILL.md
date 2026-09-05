---
name: ea-legal-context
description: >-
  Assemble the national legal register an EA programme touches — data-protection act,
  e-government or e-transactions law, public procurement act, statistics act, civil
  registration and identity acts, the act establishing the ICT agency or digital ministry,
  any e-government decree or cabinet directive, and the access-to-information act — each
  with its citation, status, the regulator it creates, and the one line of it that matters
  for architecture. Serves the Governance Board ToR whose binding-decision scope must cite
  real statutes (1.7, 3.4), the principle card that dies if it cites the wrong statute
  (2.3), the body classification (2.4), the joint business-IT agenda's constraints (1.4)
  and the Discovery brief's legal collection area (4.2). Use when someone says "which laws
  apply", "what is the legal basis for sharing this data", "does the country have a data
  protection act", "cite the statute for this principle", "legal constraints on a shared
  platform", "can we share learner data", "what does the procurement law allow". Reads the
  national gazette and law portal first, then UNCTAD's Cyberlaw Tracker, DLA Piper's Data
  Protection Laws of the World, World Bank ID4D diagnostics and OGP action plans. It never
  drafts legal text and every output ends with the legal-counsel flag.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
---

## What this skill does

Builds the **legal register**: the instruments an EA programme actually touches, each with
its citation, its status, the regulator it creates, and the single line of it that
constrains an architecture.

It exists because of one sentence in 2.3 — *a principle card that cites the wrong statute
will not survive its first challenge* — and because a Governance Board ToR whose
binding-decision scope is invented does more damage than one that was never written.

**This skill does not give legal advice and does not draft legal text.** It finds
instruments, states what they say, and hands the interpretation to counsel.

## Inputs

The country. Optionally a sector, which adds the sector act and any sector-specific data
rules, and a question ("can we share learner data with the social register?") which the
register is then built to answer.

If the learner has A0 §7, deepen it rather than rebuilding: §7 is the first pass; this adds
the citation, the regulator, the amendment history and the architecture line.

## Procedure

1. **Search the national gazette or law portal first** (T1). The gazette is the authority;
   a ministry's PDF may be an earlier version. Where no portal exists, try the parliament's
   bill tracker, then the ministry of justice, then FAOLEX (which carries far more than
   agriculture), then a regional body's legal repository.

2. **Then the trackers**, to find what you missed and to cross-check status (T2):
   the UNCTAD Global Cyberlaw Tracker for data protection, e-transactions, cybercrime and
   consumer law; DLA Piper's *Data Protection Laws of the World*; World Bank ID4D country
   diagnostics for identity and civil-registration law; OGP action plans for
   access-to-information and open-data commitments.

   A tracker tells you an act **exists**. It does not tell you the current text. Chase every
   tracker entry to the instrument.

3. **For each instrument record**: title · year · citation as it should be cited ·
   **status** (in force / amended / bill / draft / repealed / enacted-but-not-commenced) ·
   the body that owns it · the **regulator it creates**, if any, and whether that regulator
   is operative · **the one line that matters for EA**.

   *Enacted but not commenced* is a real and common state — an act passed with commencement
   left to a minister's order that never came. Treat it as its own status, never as *in
   force*.

4. **Establish currency.** Search the title plus "amendment" and plus "repeal"; check the
   gazette index for the years since; see whether the body's own site cites something later.
   Where currency cannot be established, mark ⚠ *currency not established* — never present
   an unconfirmed clause as in force.

5. **Write the architecture line.** One sentence, in an architect's language, on what the
   instrument does to a design. Not a summary of the act — the constraint.

   > *Data Protection Act 2023 §14: a legal basis is required for processing a minor's data;
   > parental consent is not sufficient for a statutory register, and is required for
   > anything beyond it. Consequence: a learner registry needs a statutory basis, not a
   > consent flow.*

6. **Record the regulator's capability separately from the law's existence.** An act in
   force with a regulator that has six staff and has taken no enforcement action is two
   facts, and a design depends on both. Say so.

7. **Run `cite-or-discard`** before returning. A fabricated section number in a Board ToR is
   the single most damaging output this kit can produce.

## Output contract

Provenance header first (`references/provenance-header.md`), then:

```
| Instrument | Citation | Year | Status | Owning body | Regulator created (operative?) | The one line that matters for EA | Source | Tier | Checked |
```

Then, in order:

- **Answering the question asked**, where the learner asked one — the instruments that
  bear on it, what each permits and forbids, and what remains unresolved on the public
  record.
- **Gaps** — the instruments an EA programme would expect and that do not appear to exist.
  Name them: no e-transactions act, no data-sharing regulation, no statistics act. An
  absence is a design constraint.
- **⚠ Currency not established** — every instrument whose amendment history you could not
  confirm.
- **The legal-counsel flag** (below). Always. Every output, without exception.

Text in the chat. No file. Posts, not names — cite the *office* that owns an instrument,
never the minister who signed it. No reasoning before the header. See
`references/output-contract.md`.

## Safeguard handed back

**This register is a finding aid, not legal advice, and nothing in it has been read by a
lawyer.**

Before any of it reaches a Terms of Reference, a principle card, a consent design or a
data-sharing agreement:

- **National counsel must confirm every citation and every status.** Search results
  systematically favour original acts over their amendments, and a repealed section reads
  exactly like a live one.
- **Ask counsel the question, not the answer.** "Does §14 permit this flow?" — not "we
  believe §14 permits this flow".
- Anything marked ⚠, *inferred*, or *currency not established* is not usable until
  confirmed.
- Where the register says an instrument does not exist, that is the absence of a *public
  record* of it, which is not the same as its absence.

## References

- `references/instrument-checklist.md` — the instruments to look for, why each one bears on
  an architecture, and what its absence implies.
- `references/law-sources.md` — where national law is published, the trackers and what each
  can and cannot prove, and how to establish currency.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` — the shared contract.
