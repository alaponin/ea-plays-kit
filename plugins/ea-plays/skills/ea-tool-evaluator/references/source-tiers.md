# Trusted sources and the cite-or-discard loop

Shared by every skill in this kit. Do not restate this policy inside a SKILL.md —
name this file and apply it.

## The four tiers

| Tier | What counts | How to treat it |
| --- | --- | --- |
| **1 — Primary / official** | Government gazettes and national law portals; ministries' and agencies' own sites; national digital strategies as published; establishing acts; UN, World Bank, ITU, OECD, IMF, UNESCO, UNICEF datasets and reports; the PAERA and GovStack specifications; the Open Group and other standards bodies; peer-reviewed journals | Cite freely. One Tier 1 source is enough to state a claim as fact. |
| **2 — Reputable secondary** | DIAL / ADLI snapshots, ID4Africa, GSMA, Smart Africa, UNECA, the Digital Public Goods Alliance registry, MOSIP and X-Road (NIIS) deployment lists, established think tanks (CGD, ODI, Brookings, Carnegie), donor project documents (World Bank PADs and ICRs, EU and FCDO evaluations) | Cite, labelled *secondary*. Chase the primary it points to and prefer that. |
| **3 — Journalism** | Named national and international outlets with an editorial process | Use for **events** (a system launched, a court ruling, a project cancelled) and for contested cases. Always pair with the primary if one exists. |
| **Reject** | Document mirrors (docplayer, scribd), personal blogs and Medium posts, vendor marketing, Wikipedia as an end source, content farms, AI-generated summary sites | Never cite. Wikipedia may be used to *find* a Tier 1 source, never as the source. |

## The verification loop

For every claim you emit, record four things before you write the line:

1. the **URL**,
2. the **access date** (the day you fetched it),
3. the **tier**,
4. a **one-line quotation or close paraphrase** of the passage that supports the claim.

Then, before returning anything to the learner, fetch each URL and confirm the
passage is there. Resolve each claim to one of five states:

| State | Meaning | Action |
| --- | --- | --- |
| **supported** | The passage says what the claim says | Keep. |
| **partly supported** | The source supports a weaker version | Rewrite the claim down to what the source says. |
| **not supported** | The source does not say it | Drop the claim, not just the citation. |
| **could not fetch** | The site refused, timed out, or is paywalled | Keep the claim, mark it ⚠ *unverified — learner to confirm*, and say the fetch failed. **Never downgrade a claim because a server refused you.** |
| **contested** | Sources disagree | Keep both, cite both, say which is which. |

A claim that survives as *not supported* is never kept silently. A claim marked
⚠ carries that mark all the way into the artefact and into the provenance header's
unverified count.

## Contested cases

Where a programme is disputed — a national ID ruled unlawful, a platform
abandoned, a cost overrun denied — the artefact must carry **both** sides with a
source each. A comparator set with no contested case in it has not been searched
hard enough.

## When a registry moves

This file names the **organisation**, never the URL. URLs live in each skill's
`references/` so a moved dataset is a one-file fix. If a named source cannot be
found at all, say so in the output rather than substituting an unnamed one.
