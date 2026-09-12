---
name: gif-semantic-map
description: >-
  Generate the semantic layer of a Government Interoperability Framework for one exchange:
  the semantic map that aligns two agencies' field lists for a shared entity to a published
  vocabulary — OneRoster (1EdTech), CEDS, ISO/IEC 11179, JSON-LD, W3C Verifiable
  Credentials, the GovStack Identity OIDC claims — with the term-to-term mapping, the
  code-list reconciliation and the linking identifier (KP2 play 4.4, B23); and the
  bronze/silver/gold plan that takes a real sector data source through ingestion, validation
  against the map and publication onto the bus (4.6, B25). Use when someone says "semantic
  map", "align these two field lists", "map agency A's fields to agency B's", "which
  vocabulary should we use", "code-list reconciliation", "what identifier links these
  records", "bronze silver gold", "medallion pipeline for the bus", "put this dataset on the
  bus", "de-duplication key", "gif-semantic-map", or names KP2 play 4.4 or 4.6. It never
  invents an identifier, because a wrong identifier silently merges two citizens' records.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
---

## What this skill does

This skill makes the semantic configuration of one exchange. Play 4.4 makes **B23, the
semantic map**: the shared entity, its fields aligned to a published vocabulary, the mapping
from each agency's term to the shared definition, the reconciliation of code lists, and the
identifier that links the same record across the two agencies. Play 4.6 makes **B25, the
bronze/silver/gold source map**: how a real dataset is ingested as-is, cleaned and validated
against the map, published as the authoritative dataset, and put onto the bus.

The bare play defends against the one dangerous error — a wrong identifier or code value
that merges two people's records — with `[confirm]` placeholders. This skill adds the
source: it **fetches the published vocabulary** and checks each element name, type and
definition against the specification as published, so that the shared definitions are the
vocabulary's and not the model's recollection of it. It cites the version. And it keeps
every identifier and every code value as `[confirm]`, because no public source can confirm
what a live registry holds.

## Inputs

| Play | Makes | Needs |
| --- | --- | --- |
| 4.4 | B23 Semantic map | B5 (the exchange and its entity); B22 (the semantic standards the portfolio adopts); **agency A's field list and code lists; agency B's; the vocabulary to align to** |
| 4.6 | B25 Bronze/silver/gold source map | B23; **a description of the source dataset** — its schema or fields if known, its owner, its refresh |

If the learner has no B22, ask which vocabulary to align to; if they do not know, propose
one from `references/vocabularies.md` for the entity and say why, and mark the choice
*inputs supplied by the learner* once they accept it. If the learner has no field lists,
stop: a semantic map with invented source fields maps nothing.

Ask at most three questions, together: the vocabulary; the identifier each agency uses
today for the entity; for 4.6, where the source is refreshed from and how often.

## Procedure

1. **Fetch the vocabulary** (T1 — the standards body's own publication; see
   `references/vocabularies.md`). Record the version and the URL. For each shared field,
   find the element in the vocabulary: its name, its definition, its type and, where the
   vocabulary gives one, its code list. Quote the definition. If the vocabulary has no
   element for a field, say so — the field is then *local*, defined in the map, and flagged
   for the Semantics Working Group (B18).

2. **Map term to term.** One row per shared field: agency A's term · agency B's term · the
   shared element (vocabulary, element, version) · the transformation, if any. Where A and B
   mean different things by the same word, split the row; where they mean the same thing by
   different words, say so and cite the definition that unites them.

3. **Reconcile code lists.** Where A's allowed values differ from B's, write the translation
   table, value by value. Where the vocabulary has its own code list, map both to it. Every
   value is `[confirm: check against the live registry]` — a code list in a document is not
   the code list in the database.

4. **Choose the identifier — and say what breaks if it is not unique.** The identifier is
   the field that links the same record across both agencies. State: what it is; who issues
   it; its coverage (from A0 §1, §6 — a national ID that reaches most adults but issues to
   a child only at 16 does not identify a learner of 9; take the real figure from A0, never
   from this instruction); what the fallback is for a record with no
   identifier; and the risk — a non-unique key merges records for different people, a
   missing key drops them. Never propose a composite of name and date of birth as the
   linking key without saying that it merges twins and namesakes.

5. **For 4.6, plan the three stages against the map.** Bronze: what is ingested as-is,
   with provenance and retention for audit. Silver: the cleaning rules, the validation
   against B23 (types, code lists, required fields), how a bad or duplicate record is
   flagged and not dropped, and the de-duplication key — which is the identifier of step 4,
   `[confirm: verify uniqueness]`. Gold: the published authoritative dataset, its owner, its
   refresh, and the service it backs. Onto the bus: the OpenAPI contract (`gif-openapi-gen`
   makes it), the X-Road service description, the trust-zone security (B21) and the
   data-protection basis (B27) — name each as a pointer, do not draft it here.

6. **Run `cite-or-discard`** on every vocabulary citation before you give the output. A
   field attributed to a vocabulary that does not define it is *not supported*: mark the
   field local.

## Output contract

Write the provenance header first (`references/provenance-header.md`). Then:

For **4.4 (B23)**: the entity block — entity · vocabulary · version · URL · access date;
the map table `| Shared field | Vocabulary element (definition quoted) | Agency A term | Agency B term | Type | Transformation | [confirm] |`; the code-list reconciliation tables; the identifier section — identifier · issuer · coverage · fallback · risk if not unique; the list of every `[confirm]`.

For **4.6 (B25)**: the four stage sections BRONZE, SILVER, GOLD, ONTO THE BUS, each with its rules as a list; the de-duplication key and its risk; the go-live checklist of what must be confirmed against the real source.

Then the **Inputs supplied by the learner** block and the safeguard. Text in the chat,
never a file; the map is a markdown table, not a spreadsheet. Posts, not names. Write no
analysis before the header. See `references/output-contract.md`.

## Safeguard handed back

**Identifier and code-list errors are the most dangerous defects in the whole framework. A
wrong identifier silently merges two citizens' records, and nothing in this output can
see the live registry.**

- Resolve every `[confirm]` against the live registries with the data owners before the
  map is published to the semantic registry (B19).
- Have the Semantics Working Group (B18) agree the map. A map two agencies did not agree is
  a proposal.
- The de-duplication key in the silver stage is the highest-risk decision in 4.6. Test it
  on the real data for collisions before the first load.
- The vocabulary version in the header is the one read on that date. Pin it in B22.

## References

- `references/vocabularies.md` — the published vocabularies by entity, where each is
  published, what it defines and does not, and the version to pin.
- `references/identifier-rules.md` — how to choose and describe the linking identifier,
  the fallbacks, and the failure modes.

### Fixture material

- `references/progressa-semantic-map.md` — the semantic map of the Progressa once-only
  exchange (person, enrolment) as the KP2 build pack publishes it. Progressa is the
  fictional demonstration country; the canonical description is `tests/progressa.md` and
  `tests/kp2/progressa-supplement.md` in the kit repo.

### The shared contract

- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` ·
  `references/workbook-chain-kp2.md`.
