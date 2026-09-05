---
name: cite-or-discard
description: >-
  Verify every claim in a draft against its source before the draft is used, and drop the
  ones that do not survive. Run it on comparator-country cards (1.8, 5.1), a business case
  or ministerial one-pager (1.3, 5.4, 5.7), a foundation map (1.5), a tool comparison (3.2),
  a learning plan (5.5), or any output carrying URLs. Its audit mode runs the other way —
  given an input pack, it says which lines are sourced and which are the learner's or the
  model's assertion, which is how the Discovery brief's source column (4.2) gets populated
  instead of promised. Use whenever someone says "check these sources", "verify this
  citation", "is this claim real", "did you make this up", "which of these URLs are
  primary", "fact-check this table", "is docplayer a source", or before anything goes to a
  minister. Fetches every URL, grades it against the four source tiers, and returns keep /
  downgrade / drop per claim. Plays run bare in any assistant; this makes the safeguard real.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
---

## What this skill does

Takes any output that carries claims and URLs and returns a verification table saying,
for each claim, whether the source actually supports it — then rewrites, marks or drops
the claims that failed. It operationalises the safeguard that nearly every play in the
course ends with: *verify against a named source before you use this*.

The plays run bare in any assistant. With this skill they run better, because the check
happens rather than being left as the learner's homework.

## Inputs

**Verify mode (default).** A draft carrying claims and URLs — a comparator card set, a
cost case, a foundation map, a tool comparison, a legal register. Paste it whole.

**Audit mode.** An input pack the learner assembled — A0 sections, interview notes, a
Discovery brief in progress. Say "audit this pack" or ask for the source column.

If the draft has no URLs at all, do not refuse: run audit mode instead and tell the
learner every line is unsourced, which is the finding.

## Procedure

1. **Split into atomic claims.** One row per checkable assertion. "Rwanda published a
   GEA framework in 2022 and it is mandatory for ministries" is two claims, not one.
   Rhetoric, recommendations and the learner's own judgements are not claims — list
   them separately as *assertion, not claim* rather than trying to verify them.

2. **Grade each URL against `references/source-tiers.md`** before fetching. A docplayer
   or scribd link is a **mirror**: record it, then search for the document on the issuing
   body's own site and use that. A Medium post or personal blog is **rejected**: search
   for what it was summarising. Wikipedia is a finding aid, never the source.

3. **Fetch every URL.** Not a sample — every one. Extract the passage that bears on the
   claim and quote it in one line. Where a page is long, quote the sentence, not the
   section.

4. **Resolve to one of five states**, per `references/source-tiers.md`:
   *supported · partly supported · not supported · could not fetch · contested.*

   **`could not fetch` is not `not supported`.** Government portals block automated
   fetches routinely. A refused, timed-out or paywalled fetch keeps the claim, marks it
   ⚠ and hands the learner a manual check. Never downgrade a claim because a server said
   no — that is the single most damaging error this skill can make.

5. **Chase the primary.** For every Tier 2 or Tier 3 source, spend one search on the
   Tier 1 document behind it. If you find it, cite that and demote the secondary to a
   *found via* note. If you do not, say so — "no primary located" is a result.

6. **Look for the contested case.** Where a claim concerns a programme that has been
   litigated, cancelled, overrun or disputed, search once for the other side. A set of
   claims with no dissent in it has been searched credulously, not thoroughly.

7. **Return the table, then the rewritten draft.** Not the table alone — the learner
   wants the clean version. Claims that scored *partly supported* come back rewritten
   down to what the source says; *not supported* claims are gone from the rewrite and
   listed under *dropped*; ⚠ claims stay, marked.

## Output contract

Provenance header first (`references/provenance-header.md`), then:

```
| # | Claim | URL | Tier | Verdict | Supporting passage | Action |
```

*Verdict* is one of the five states. *Action* is **keep**, **rewrite** (with the
rewritten wording), **drop**, or **⚠ unverified — learner to confirm**.

Then, in order:

- **Dropped** — one line per discarded claim, naming what the source actually said.
- **Downgraded sources** — every mirror, blog or vendor page found, and whether the
  primary was located.
- **Contested** — both sides, both cited, where any claim is disputed.
- **The rewritten draft** — the original with the table applied.

Text in the chat. No file. Posts, not names. No reasoning before the header — see
`references/output-contract.md`.

**Audit mode** returns instead: `| Line | Claim | Sourced? | Source or "learner's
assertion" | Tier |`, then a count — *n of m lines carry a source*.

## Safeguard handed back

This skill checks that a source says what a claim says. It does not check that the
source is *right*, that it is current, or that the body that published it is neutral.
Before the artefact is shown to anyone with authority:

- open the two or three claims the decision turns on yourself;
- confirm the date on each — a live status from 2023 may be false now;
- and for any contested case, read both sides before you repeat either.

A claim marked ⚠ is unverified, not verified-as-true. Do not let it pass into a
cabinet briefing on the strength of having appeared in this table.

## References

- `references/source-tiers.md` — the four tiers, the five verdict states, and the rule
  for a fetch that fails. Load before grading anything.
- `references/provenance-header.md` — the nine header fields.
- `references/output-contract.md` — text in / text out, posts not names, strip reasoning.
- `references/workbook-chain.md` — to fill **Consumed** and **Feeds**.
- `references/known-mirrors.md` — the domains that are mirrors or rejected outright, and
  where the primary usually lives instead.
