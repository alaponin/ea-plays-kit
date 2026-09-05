# What each status requires

The status is a claim about the world. This rubric is what has to be true before you may
write it. When the evidence you have supports two statuses, write the lower one.

| Status | Required evidence | Not sufficient |
| --- | --- | --- |
| **live** | The operator's own statement, a regulator's or audit report, or a donor completion report, saying the system is in production — **plus** a named operator, **plus** at least one of: a coverage or volume figure, a published member list, a documented onboarding procedure. | A strategy naming it. A launch press release with no later trace. A vendor case study. A conference slide. A deployment map entry with no date. |
| **pilot** | Same evidence as live, but the source itself says pilot / phase 1 / limited members, or the member list is a handful of founding bodies. | A programme that intends to pilot. |
| **planned** | A funded, dated commitment in a strategy, budget line, or approved donor project. | An aspiration in a speech. A sector plan calling for something with no funder. |
| **none** | Searched all the sources in `block-sources.md` for this block and found nothing beyond aspiration. State which sources you searched. | Not having looked. |
| **unclear** | Sources conflict, or the most recent statement is more than two years old, or the operator cannot be identified. | — use this rather than guessing. |

## The trap this rubric exists to close

A World Bank appraisal document (a PAD) describes what a project **will** build. Its
completion report (an ICR) describes what it **did** build. Reading a PAD as evidence of a
live system is the most common way a *planned* block gets recorded as *live*, and it is the
error that puts a phantom platform into a target architecture.

The same trap, in three other clothes:

- A national strategy listing a data-exchange layer among its pillars.
- A GovStack or DPI map entry recording a country's *engagement*, not its deployment.
- A ministry's "digital services" page describing the service it intends to offer.

## Availability is a separate judgement

A block can be **live** and still not **available to a new sector**. Record these
separately. A block is available when all four hold:

1. There is a documented onboarding procedure a new member can follow.
2. There is a legal basis covering a new member's data flows — not only the founding
   members'.
3. The cost is known and a ministry could pay it.
4. The operator is currently accepting members (not "paused pending phase 2").

Where any of the four is unknown, the answer in the column is *unknown*, and the gate
decision that depends on it is not ready to be taken.
