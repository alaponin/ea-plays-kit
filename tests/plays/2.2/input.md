# Play 2.2 — Check a draft architecture against the PAERA metamodel · fixture input

**Consumes:** a draft model, or the initiatives list — from [`tests/progressa.md`](../../progressa.md).
**Primary skill:** `paera-reference-check`
**Produces:** A10 — Metamodel conformance report

## What the learner types

Below is a draft architecture for [name the body or system] [paste the model: the elements and how they relate, in whatever form you have — a list, a table, a description]. Check it against the PAERA metamodel, whose entity types are Capability, Service, Application, Data Domain, Technology Component and Organisation, with the relationships: Capability delivered-by Service, Capability supported-by Application, Application uses Data Domain, everything runs-on Technology Component, Organisation owns each. For each element in my draft, map it to a PAERA entity type. Flag any element that does not map cleanly (a candidate private-language term or a missing entity). List every relationship in the metamodel that my draft is missing — for example a Data Domain with no named owning Organisation, or an Application with no Capability above it. Output: a mapping table (my element / PAERA entity / note), then a list of non-conforming elements, then a list of missing relationships, then 3 suggested corrections.

## What the fixture supplies

Country: **Progressa** · Sector: **Education**. Put these two values in the place of each
placeholder in brackets above. The named input is a draft model, or the initiatives list of `tests/progressa.md`. Paste
those sections without a change.

If this play consumes an artefact from an earlier play, such as A1, A3 or A22, run that play
on Progressa first. The chain is in
[`shared/workbook-chain.md`](../../../plugins/ea-plays/shared/workbook-chain.md).
