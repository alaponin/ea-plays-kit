# The attributes, where to check them, and how they get obscured

Score only what a register or the vendor's own documentation states. Everything else is
"not documented", which is itself a finding.

| Attribute | Where the fact lives | How it gets obscured |
| --- | --- | --- |
| **Licence** | **opensource.org**'s approved-licence list, checked against the exact licence name in the tool's repository or licence file | "Open" covering open-core (the useful half is proprietary), a free tier, or a source-available licence that forbids the use you need. Record the **licence name**, then check that name against the OSI list. |
| **ArchiMate certification** | **The Open Group's tool certification register** | Certification against an older ArchiMate version presented as current. Record the version certified. |
| **Export formats** | The vendor's **documentation** — the manual, not the feature grid | A format listed on a marketing page and absent from the manual. A format that exists but is lossy: relationships, layout or custom attributes dropped. The manual usually says so, in a note. |
| **Metamodel extensibility** | The vendor's documentation on custom entity or relationship types | "Customisable" meaning colours and views, not the metamodel. Look for whether a *new entity type* can be defined, not a new attribute. |
| **Pricing** | The **published pricing page** | No public price ("contact us") — record it as a finding, not a blank. Export or API access gated behind an enterprise tier, which converts an open format into a lock-in mechanism. Per-user pricing that becomes untenable when the sector CIOs need read access. |
| **DPGA status** | The **Digital Public Goods Alliance registry** | Nothing much — this one is a straightforward register. |
| **Repository and activity** | The public repository, for open tools: last release, open issues, number of contributors | A tool with one contributor is a dependency on a person. |

## Three questions that decide lock-in

Answer these three from the facts above, not from an impression:

1. **Is there a documented export** of the full model, in the manual?
2. **Is it an open format** — ArchiMate Exchange Format, CSV, or plain files that another
   tool reads?
3. **Is that export available at the tier you can afford?**

Three yeses is low lock-in. Any no is the answer, whatever the rest of the table says.

## When the answer is "no tool"

Under a few hundred entities, a spreadsheet or wiki carrying the A16 schema — capabilities,
data domains with one named owner each, applications mapped to both, technology, and a
decision log — outperforms a tool the practice cannot maintain. The failure mode of a
dedicated EA tool in a small practice is not cost; it is that one person learns it and then
leaves.

Recommend it plainly where it is right. The play asks for a scored comparison; a comparison
that concludes "not yet" is a valid outcome and it is the honest one more often than the
market suggests.

## Citing a vendor page

A vendor's page is Tier "reject" as evidence that a tool is *good*. It is Tier 1 as evidence
of *what the vendor documents* — and that is what this skill scores, because a documented
claim is one you can hold them to. Cite it for the second, and say which you are doing.
