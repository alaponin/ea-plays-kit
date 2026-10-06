# Trusted sources and the cite-or-discard loop

Each skill in this kit uses this file. Do not write this policy again in a SKILL.md.
Give the name of this file and apply it.

## The four tiers

| Tier | What counts | How to use it |
| --- | --- | --- |
| **1 — Primary / official** | Government gazettes and national law portals; the sites of ministries and agencies; national digital strategies as published; establishing acts; UN, World Bank, ITU, OECD, IMF, UNESCO, UNICEF datasets and reports; the PAERA and GovStack specifications; the Open Group and other standards bodies; peer-reviewed journals | Cite it. One Tier 1 source is enough to write a claim as a fact. |
| **2 — Reputable secondary** | DIAL / ADLI snapshots, ID4Africa, GSMA, Smart Africa, UNECA, the Digital Public Goods Alliance registry, MOSIP and X-Road (NIIS) deployment lists, established think tanks (CGD, ODI, Brookings, Carnegie), donor project documents (World Bank PADs and ICRs, EU and FCDO evaluations) | Cite it with the label *secondary*. Then find the primary source that it points to, and use the primary source. |
| **3 — Journalism** | National and international outlets that have a name and an editorial process | Use it for events: a system that started, a court ruling, or a project that stopped. Use it also for contested cases. Always add the primary source if one exists. |
| **Reject** | Document mirrors (docplayer, scribd), personal blogs and Medium posts, vendor marketing, Wikipedia as an end source, content farms, sites with AI-generated summaries | Never cite these sources. You can use Wikipedia to find a Tier 1 source. Do not use Wikipedia as the source. |

## The verification loop

Record these four items for each claim before you write the line:

1. the **URL**,
2. the **access date**, which is the day that you read the page,
3. the **tier**,
4. a **quotation of one line**, or a close paraphrase, of the passage that supports
   the claim.

Then read each URL again before you give anything to the learner. Make sure that the
passage is there. Give each claim one of these five states:

| State | Meaning | Action |
| --- | --- | --- |
| **supported** | The passage says what the claim says | Keep the claim. |
| **partly supported** | The source supports a weaker claim | Write the claim again. Make it agree with the source. |
| **not supported** | The source does not say it | Remove the claim. Do not remove only the citation. |
| **could not fetch** | The site refused, the request timed out, or the page is behind a paywall | Keep the claim. Mark it ⚠ *unverified — learner to confirm*. Tell the learner that the fetch failed. **Never make a claim weaker because a server refused you.** |
| **contested** | The sources do not agree | Keep both claims. Cite both sources. Tell which source says what. |

Never keep a *not supported* claim without a message to the learner. A claim that has
a ⚠ mark keeps that mark in the artefact. It also counts in the unverified count in
the provenance header.

## Contested cases

Some programmes are disputed. A court can rule that a national ID is unlawful, a
platform can stop, or a government can deny a cost overrun. The artefact must give
**both** sides, with one source for each side. If a comparator set contains no
contested case, you did not search enough.

## When a registry moves

This file gives the name of the **organisation**. It does not give the URL. The URLs
are in the `references/` folder of each skill. Thus a dataset that moves is a change
to one file. If you cannot find a named source, say so in the output. Do not put a
source with no name in its place.
