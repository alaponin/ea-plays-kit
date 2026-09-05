---
name: cite-or-discard
description: >-
  Verify each claim in a draft against its source before you use the draft, and drop the
  claims that fail. Run it on comparator-country cards (1.8, 5.1), a business case or a
  ministerial one-pager (1.3, 5.4, 5.7), a foundation map (1.5), a tool comparison (3.2),
  a learning plan (5.5), or any output that has URLs. The audit mode does the opposite:
  for an input pack, it tells which lines have a source, and which lines are an assertion
  by the learner or the model. This is how the source column of the Discovery brief (4.2)
  gets its content. Use whenever someone says "check these sources", "verify this
  citation", "is this claim real", "did you make this up", "which of these URLs are
  primary", "fact-check this table", "is docplayer a source", or before anything goes to a
  minister. Reads every URL, grades it against the four source tiers, and gives keep /
  downgrade / drop for each claim. Plays run bare in any assistant; this makes the
  safeguard real.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
---

## What this skill does

This skill reads an output that has claims and URLs. It gives a verification table. The
table tells, for each claim, if the source supports the claim. The skill then writes the
claim again, marks it, or drops it.

Almost every play in the course ends with the same safeguard: *verify against a named
source before you use this*. This skill does that work.

The plays run bare in any assistant. With this skill they run better, because the check
occurs. It does not stay as homework for the learner.

## Inputs

**Verify mode is the default.** The input is a draft that has claims and URLs: a set of
comparator cards, a cost case, a foundation map, a tool comparison, or a legal register.
Paste the full draft.

**Audit mode.** The input is a pack that the learner assembled: A0 sections, interview
notes, or a Discovery brief that is not complete. Say "audit this pack", or ask for the
source column.

If the draft has no URLs, do not refuse. Run audit mode. Then tell the learner that no
line has a source. This is the finding.

## Procedure

1. **Divide the draft into single claims.** Write one row for each assertion that you
   can check. "Rwanda published a GEA framework in 2022 and it is mandatory for
   ministries" is two claims, not one. Rhetoric, recommendations and the judgements of
   the learner are not claims. Put them in a different list with the label *assertion,
   not claim*. Do not try to verify them.

2. **Grade each URL against `references/source-tiers.md` before you read it.** A
   docplayer or scribd link is a **mirror**. Record it. Then search for the document on
   the site of the body that issued it, and use that site. A Medium post or a personal
   blog is **rejected**. Search for the material that it summarised. Wikipedia helps you
   to find a source. It is never the source.

3. **Read every URL.** Read all of them, not a sample. Find the passage that applies to
   the claim, and quote it in one line. If a page is long, quote the sentence. Do not
   quote the section.

4. **Give each claim one of five states**, as `references/source-tiers.md` defines them:
   *supported · partly supported · not supported · could not fetch · contested.*

   **`could not fetch` is not the same as `not supported`.** Government portals block
   automatic fetches frequently. If a fetch is refused, times out, or hits a paywall,
   keep the claim, mark it ⚠, and give the learner a manual check to do. Never make a
   claim weaker because a server refused you. This is the most damaging error that this
   skill can make.

5. **Find the primary source.** For each Tier 2 or Tier 3 source, do one search for the
   Tier 1 document behind it. If you find the document, cite it. Then make the secondary
   source a *found via* note. If you do not find it, say so. "No primary located" is a
   result.

6. **Look for the contested case.** A claim can be about a programme that went to court,
   stopped, had a cost overrun, or is disputed. Then do one search for the other side. A
   set of claims with no disagreement in it is a set that you searched with too much
   trust.

7. **Give the table first, then the draft that you wrote again.** Do not give the table
   alone. The learner needs the clean version. Write each *partly supported* claim again,
   to agree with the source. Remove each *not supported* claim from the new draft, and
   put it in the *dropped* list. Keep the ⚠ claims, with their marks.

## Output contract

Write the provenance header first (`references/provenance-header.md`). Then write this
table:

```
| # | Claim | URL | Tier | Verdict | Supporting passage | Action |
```

*Verdict* is one of the five states. *Action* is **keep**, **rewrite** with the new
words, **drop**, or **⚠ unverified — learner to confirm**.

Then write these four sections in this order:

- **Dropped** — one line for each claim that you removed, with what the source says.
- **Downgraded sources** — each mirror, blog or vendor page that you found, and whether
  you found the primary source.
- **Contested** — both sides, with a citation for each, for each claim that is disputed.
- **The rewritten draft** — the first draft with the table applied to it.

Write text in the chat. Do not make a file. Posts, not names. Write no analysis before
the header. See `references/output-contract.md`.

**Audit mode** gives a different table: `| Line | Claim | Sourced? | Source or "learner's
assertion" | Tier |`. Then it gives a count: *n of m lines carry a source*.

## Safeguard handed back

This skill checks that a source says what a claim says. It does not check that the source
is correct. It does not check that the source is current. It does not check that the body
that published the source is neutral. Do these three steps before you show the artefact
to a person with authority:

- read the two or three claims that the decision depends on;
- confirm the date of each claim, because a live status from 2023 can be false now;
- for each contested case, read both sides before you repeat one of them.

A claim with a ⚠ mark is unverified. It is not verified as true. Do not let it go into a
cabinet briefing because it is in this table.

## References

- `references/known-mirrors.md` — the domains that are mirrors or that you must reject,
  and where the primary source usually is.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` — the shared contract.
  Read `source-tiers.md` before you grade a source.
