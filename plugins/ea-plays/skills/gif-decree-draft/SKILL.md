---
name: gif-decree-draft
description: >-
  Draft the components of a Government Interoperability Framework decree — the Decree
  Drafting Kit of KP2 Module 2 — against named, published legal models, and never from
  imagination: the five-component outline (2.2, B9), the Explanatory Memorandum and the
  Preamble scaffold (2.3, B10), one operative article adapted from a published model — the
  mandatory-connection, once-only, data-protection, principles, operating-authority or
  sanctions article (2.4, B11) — and the Cover Note with the Two-Track Regulatory Memo that
  coordinates the decree with the data-protection law (2.5, B12). Use when someone says
  "draft the interoperability decree", "outline the decree", "explanatory memorandum",
  "preamble", "draft the once-only article", "mandatory connection article", "cover note to
  the Ministry of Justice", "two-track memo", "coordinate the decree with the
  data-protection law", "decree drafting kit", "gif-decree-draft", or names a KP2 Module 2
  play. It never invents a citation, a section number or an obligation.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
---

## What this skill does

This skill drafts the parts of an interoperability decree. It makes four of the six
artefacts of KP2 Module 2: B9 the outline, B10 the Memorandum and Preamble, B11 one
operative article, B12 the Cover Note and the Two-Track Regulatory Memo. B8 comes from
`ea-legal-context`, and B13 from `gif-consistency-check`.

It exists because of one sentence in play 2.4: *invented legal text is the single most
dangerous output in this whole knowledge product — it reads convincingly and is worthless
or harmful.* The bare play defends against that with `[confirm]` placeholders. This skill
adds two things. It fetches the **published model** and adapts it, so the structure and the
force of each article come from a real instrument. And it reads the **legal register** of
the country, so that a placeholder the register can fill — the data-protection act, the
section on public-sector sharing, the act that establishes the digital agency — is filled
with a cited instrument, and the rest stay `[confirm]`.

**This skill does not give legal advice. It does not make law.** What it produces is a
Decree Drafting Kit: structured, sourced drafts that a qualified lawyer in the jurisdiction
turns into an instrument with legal force. The kit speeds the lawyer. It does not replace
them.

## Inputs

Each play names its inputs in `references/workbook-chain-kp2.md`. Ask for the missing
artefact by number and stop; do not build it.

| Play | Makes | Needs | Also useful |
| --- | --- | --- | --- |
| 2.2 | B9 outline | B4 Strategic Foundation Document, B8 legal-readiness assessment | A0 §7, A0 §10 |
| 2.3 | B10 Memorandum and Preamble | B4, B9 | the legal register |
| 2.4 | B11 one article | B9, B5 Use-Case Catalogue, **which article**, **which published model** | the legal register, B8 |
| 2.5 | B12 Cover Note and Two-Track Memo | B10, B11, **the status of the data-protection law** | A0 §10, the legal register |

If the learner has no legal register, run `ea-legal-context` first, or say that you
work from A0 §7 and §10 alone and that every citation is then `[confirm]`.

Ask at most three questions, together, before you start. For 2.4: which article, and
which published model (if the learner names none, propose one from
`references/published-models.md` and say why). For 2.5: whether the data-protection law is
in force, in parliament, in draft, or absent. Record the answers in an *Inputs supplied by
the learner* block in the artefact.

## Procedure

1. **Fetch the published model first** (T1). For each component or article, open the
   instrument in `references/published-models.md` — the consolidated text on the official
   portal, never a summary. Quote the passage you adapt from, with its URL and access date.
   If the fetch fails, say so, mark the model ⚠ *unverified — learner to confirm*, and
   adapt from the structure that `references/published-models.md` gives. Never adapt from
   memory alone without saying so.

2. **Read the legal register.** For each placeholder that the bare play would leave as
   `[confirm]`, look for the instrument in the register: the constitution's article on
   subordinate legislation, the act that establishes the digital agency, the
   data-protection act and its public-sector section, the procurement act, the sector act.
   Where the register gives the instrument with a citation and a status, write the citation
   and mark it *(register, <date>)*. Where the register does not, write
   `[confirm: <what is needed>]`. Where the register gives the instrument but its currency is
   not established, write the citation **and** keep the `[confirm]` — both.

3. **Adapt, do not invent.** Stay close to the structure and the force of the model. Where
   the model names an institution, a law or a value of its own country, replace it with the
   country's equivalent from the register, or with `[confirm]`. Add no obligation that is
   not in the model or clearly required by the framework's principles; if you add one, say
   which principle requires it. Flag every term that has a specific legal meaning —
   *controller*, *processor*, *public body*, *authoritative source*, *administrative act* —
   for local-counsel review.

4. **Keep the decree and the catalogue aligned.** For 2.4, read B5. The mandatory-connection
   article must cover the first-wave bodies in B5 and no more; the once-only article must
   cover the exchanges in B5 and no more. Write the coverage as a short table after the
   article: catalogue exchange → the clause that authorises it. `gif-consistency-check`
   repeats this check in 2.6; do the first pass here.

5. **For 2.5, coordinate the two instruments from the real text.** The Two-Track Memo is
   the decree ↔ data-protection-law coordination. Open the data-protection act from the
   register. For each point of intersection — definitions, lawful basis, consent and
   data-subject rights, cross-border transfer, the data-protection officer, sanctions — say
   whether the decree defers, fills a gap, or could conflict, and cite the section of the
   act that you read. If the act is in draft or in parliament, say which version you read
   and mark every reference to it ⚠. If it is absent, the memo says so and lists what the
   decree must then carry itself.

6. **Run `cite-or-discard`** on every citation before you give the output. A citation to
   a section that the fetched text does not contain is *not supported*: remove the section
   number and restore the `[confirm]`.

## Output contract

Write the provenance header first (`references/provenance-header.md`). Then write the
artefact as the play's prompt asks — the shape for each component is in
`references/component-templates.md`. Then, in this order:

- **Inputs supplied by the learner** — the answers to your questions.
- **The models adapted from** — a table: component or article · published model · the
  passage adapted · URL · tier · access date.
- **Every `[confirm]`** — one line each: the placeholder, what is needed, and who resolves
  it (counsel, the Ministry of Justice, the data-protection authority, the sponsor).
- **Every flagged term** — the term, where it appears, and why it needs counsel.
- **The legal-counsel flag** — below. Write it in each output. There is no exception.

Text in the chat, never a file. Posts, not names: the *Minister of Justice*, never the
minister's name; the *Data Protection Commissioner*, never the person. A court ruling or a
signed instrument is cited as the document. Write no analysis before the header. See
`references/output-contract.md`.

## Safeguard handed back

**This is a drafting kit. It is not a decree, and no lawyer has read it.**

- **A `[confirm]` placeholder must never reach the Ministry of Justice as if it were a
  citation.** Resolve each one with counsel before transmission, or transmit the list of
  placeholders as an open-items annex.
- **Every clause adapted from a foreign model is a proposal.** The model's force may not
  transfer: a regulation that binds member states directly has no counterpart in a
  unitary state's executive decree. Ask counsel whether the route is a decree or primary
  legislation; the Cover Note asks that question and does not answer it.
- **The register can be wrong or stale.** A section that is repealed looks like a section
  that is live. Counsel confirms each citation and each status before the article carries
  it.
- **The memo coordinates with the law as read on the date in the header.** If the
  data-protection law changes during drafting, run 2.5 again.

## References

- `references/published-models.md` — the instruments to adapt from, component by
  component: where each is published, which provision does what, and what does not
  transfer across legal systems.
- `references/component-templates.md` — the shape of each of the five components and of
  the six operative articles, with the enforcement ladder.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` ·
  `references/workbook-chain-kp2.md` — the shared contract.
