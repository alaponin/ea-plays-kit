---
name: ea-comparator-evidence
description: >-
  Find comparator countries that actually resemble yours and document what each one really
  built, from its published EA framework or digital-government coordination instrument —
  three to five cards, a Tier 1 source per claim, one transferable mechanism each, and at
  least one contested or mixed case with both sides cited. Serves the comparator signposts
  play (1.8) and the evidence play (5.1), and feeds the proof section of the ministerial
  business case (5.4) and the closing case (5.7). Use when someone says "which countries are
  like mine", "find comparator countries", "has anyone actually done this", "is this proven
  or just theory", "what did Rwanda/Ghana/Estonia actually build", "give me evidence for the
  minister", "show me a country that failed at this", "signpost countries for my context".
  Selects by World Bank income classification, population band, governance type and region,
  with priority to African and developing-country examples; reads published national EA
  frameworks, the UN EGDI, the World Bank GovTech Maturity Index and the OECD Digital
  Government Index. Runs cite-or-discard on itself before returning — the 1.8 test run
  produced comparators sourced to document mirrors and blog posts, and this is the fix.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
---

## What this skill does

Selects comparator countries on stated criteria and documents what each actually built,
with a primary source per claim and one mechanism the learner's country could transfer.

The August 2026 run of 1.8 produced five comparators with URLs — a real improvement on the
video's four unsourced signposts — but some of those URLs were document mirrors and Medium
posts. This skill exists to make the sourcing survive a check, and to stop the set being
a list of successes.

## Inputs

**A0 §5, the country-characteristics one-liner.** That is the whole input. If the learner
does not have it, build it (or hand off to `country-context-pack`) — comparators selected
without it are selected on the model's impression of the country, which is how Estonia ends
up as a comparator for a country of 200 million.

If the learner has A8 from an earlier run, extend and re-verify it rather than starting again.

## Procedure

1. **State the selection criteria before selecting.** Write them out: income classification,
   population band, governance type (unitary / federal, and the degree of sub-national
   autonomy), region, and the maturity signal. Then say which countries meet them. A
   comparator set whose criteria are not stated cannot be argued with, and it will be
   argued with.

2. **Give priority to African and developing-country examples.** A minister who is shown
   Estonia and Singapore is being shown countries with a different fiscal and institutional
   reality, and knows it. Estonia earns a place for a specific transferable mechanism
   (X-Road governance, the once-only obligation in law), not as a general model.

3. **Use the maturity indices as the comparability signal, not as the finding**: the UN
   E-Government Survey EGDI, the World Bank GovTech Maturity Index, the OECD Digital
   Government Index. They say a country is comparable. They do not say what it built.

4. **For each comparator, find what it actually built** — from its **published EA
   framework** or its digital-government coordination instrument (T1). Kenya's GEA, Ghana's
   GEA, South Africa's GWEA, Rwanda's RISA framework, India's IndEA, Estonia's X-Road
   governance are known starting points; search for others rather than reusing this list.
   Peer-reviewed case studies are T1. Donor evaluations are T2.

   The card records **the instrument**, not the intention: the framework as published, the
   act or directive that made it binding, and what is documented as having happened since.

5. **Find the transferable mechanism.** One per card: the specific device this country used
   that the learner's could adopt. The 2026 test run surfaced Liberia's "Technical
   Clearance" and a spending-gate authority — that is exactly the level of specificity
   wanted. "They had political commitment" is not a mechanism.

6. **Include at least one contested or mixed case, with both sides cited.** This is
   mandatory, not a nice-to-have. A national ID ruled unlawful, a platform abandoned, a
   framework published and never applied, a cost overrun the government disputes. Cite the
   court judgment or audit report **and** the government's response. Named journalism (T3)
   is appropriate here and must be paired with the primary.

   A set of five successes is not evidence; it is a brochure, and a minister's advisor will
   find the counter-example you omitted.

7. **Synthesise the recurring elements** — what appears in three or more cards. That
   synthesis, not the individual cards, is what carries into 5.4 and 5.7.

8. **Run `cite-or-discard` on your own output** before returning it. Every URL fetched,
   every mirror chased to its primary, every claim graded. This step is not optional and it
   is named in the output.

## Output contract

Provenance header first (`references/provenance-header.md`), then:

**Selection criteria** — the five criteria with the learner's country's values, and the
countries that met them.

**Comparator cards**, three to five, each:

```
### <Country> — <one-line why it is comparable>
| | |
| --- | --- |
| **Comparable because** | income · population · governance · region · maturity index and rank |
| **What it built** | the framework or instrument, with its year |
| **Made binding by** | the act, directive or spending gate — or "not binding" |
| **Documented since** | what the record says happened, with dates |
| **Transferable mechanism** | the one device this country could adopt |
| **Sources** | URL · tier · checked on — one row per claim above |
```

**Contested case** — its own card, both sides, both cited, and one line on what the dispute
means for the learner's country.

**Recurring elements** — what appears in three or more cards, and what appears in none.

**Verification summary** — the `cite-or-discard` result: how many claims kept, rewritten,
dropped, ⚠; which sources were mirrors and whether the primary was found.

Text in the chat, tables not charts. Posts, not names. No reasoning before the header.
See `references/output-contract.md`.

## Safeguard handed back

Comparators persuade, which is exactly why they are dangerous.

- **Open the two or three sources the argument rests on** before this goes to a minister.
  A framework published is not a framework applied, and the gap between them is where every
  comparator argument fails under questioning.
- **Check the dates.** A country's framework from 2019 may have been superseded, and its
  agency may have been restructured twice since.
- **Be ready for the counter-example.** You included one contested case; the room may know
  another. Better to have searched for it.
- **A mechanism transfers only with its preconditions.** Liberia's technical clearance
  works because something gives it teeth. Name what that is in your country, or say it is
  missing — that absence is the real finding.
- Anything marked ⚠ is unverified, not verified-as-true.

## References

- `references/comparator-selection.md` — the five criteria, how to band them, and the
  failure modes of each.
- `references/known-frameworks.md` — published national EA frameworks and coordination
  instruments known at the time of writing, with what each one is and is not, and the
  contested cases worth knowing about. A starting point for search, never a substitute.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` — the shared contract.
