# The shape the model is held in

This is the skill's own shape: how the use case model is laid out as files so that
`scripts/extract.py` can read it, `scripts/check_model.py` can check it and the render step can
draw the reader's edition from it. It carries no rule of the standard. Where a part of the shape
exists because the standard asks for something, the rule is cited by its identifier and the
reader opens the standard to read it.

## The folder

```
<the model's folder>/                 the row's folder in the specification tree
  use_case_model.md                   the model file: the artifact the claim is made for
  use_cases/<identifier>.md           one file for each use case (M19)
  survey.md                           generated from the use case files; never written by hand
  _conformance/                       the verdicts and the claim, written by `kit conform`
```

## The model file

A YAML head, then nine sections whose headings carry the words below; `extract.py` finds a
section by those words, not by its number.

| Head key | What it holds |
|---|---|
| `system` | the name of the system under discussion |
| `standard`, `written_to` | the standard's code, and the edition and checksum the template's head gave when the model was prepared |
| `version` | the model's own version |
| `owner` | the person accountable for the model |
| `boundary` | `organisation` or `software` |
| `treatment` | `black-box` or `white-box` |
| `use_cases` | the folder of use case files, relative to the model file |
| `survey` | the survey file, relative to the model file |
| `named` | the five things the model names and does not hold — `requirements`, `entity_model`, `glossary`, `business_rules`, `settings` — each as a path relative to the model file, or as `{absent: <what is missing>, owner: <who writes it>}` with a finding filed, or, for a thing the model has no use for, `{none: <the sentence saying why>}` |
| `claim` | where `kit conform` writes the claim |

| Heading carries | What the section holds |
|---|---|
| Purpose | what the system is for, in prose |
| system under discussion | the treatment in prose, with two sub-sections whose headings carry **Inside** and **Outside** |
| actors | one table: `Actor`, `Kind` (`primary`, `supporting` or `offstage`), `Is it a person?` (`yes` or `no`), `The goal it brings, or the service it gives` |
| packages | one table: `Package`, `Code`, `What it is about`, `Its use cases` (identifiers); then a sub-section whose heading carries **depend**, in prose |
| survey | one sentence naming the survey file |
| supporting actor | one table: `Use case`, `Supporting actors it calls on` — the record of which supporting actor each goal calls on, which no field of the header carries |
| relationships | sub-sections whose headings carry **Included** (`Included`, `Base use cases`, `Why it is written once`), **Optional** (`Extension`, `Base`, `At the point`, `When`), **Generalisation**, and **not draw** (the relationships the model deliberately leaves out, in prose) |
| diagrams | one sentence: the diagrams are drawn from the headers by the render step, and the model keeps no picture |
| written out | the format decision and the order it sets, with its ground (M21) |

The relationship tables carry only what the headers cannot: the reason a step is written once,
and the point and condition of an optional step. The relationship itself is stated in the use
case files' headers, and the check reports a table row whose pair no header states.

## A use case file

A copy of the kit's template of row 03, made by `scripts/prepare.py`, with the `Answer` column
of its header table filled and nothing else in the template changed; then one heading,
`## One-line description`, and one line beneath it saying what the goal is for. The header is
the only place a value of the use case is stated.

Four conventions make an answer readable by a program:

- **Status and priority** — the status, then the priority, separated by `·`.
- **Linked requirements**, **Business rules** — identifiers, separated by commas.
- **Entities** — `reads: A, B; changes: C`, names only.
- **Relationships** — clauses separated by `;`: `includes UC-06, UC-07`, `included by UC-02`,
  `extends UC-02 at <the point> when <the condition>`, `extended by UC-04`, `generalises UC-x`,
  `specialises UC-x`; or `—` for none.

## The survey

`python3 scripts/extract.py <model file> --write-survey` writes it: one row for each use case,
every field of its header in the order the header carries them, then its package and its
one-line description. The check generates it again and compares the two byte for byte, so a
survey edited by hand is found (M13, M19).

## The named sets

The model reads each named set and never writes one. A set in markdown is read from the first
cell of every table row (an identifier, or an entity's or a term's name) and the second cell (its
statement or its definition); a set in YAML or JSON from its keys, or from the `id` or `name` of
its entries; a delimited file from its first column. The published register of requirements,
the entity model with its glossary and its register of business rules, and the catalogue of
settings are each written in their own row of the specification tree, by their own standard.

## The skeleton

`scripts/prepare.py` writes a new model file from this block, filling the three names in braces.

<!-- skeleton:begin -->
```markdown
---
system: {system}
standard: SDD-05
written_to: {edition: "{edition}", sha256: "{sha256}"}
version: "0.1"
owner:
boundary:
treatment:
use_cases: use_cases
survey: survey.md
named:
  requirements: {absent: "the published register of requirements", owner: }
  entity_model: {absent: "the entity model's first pass", owner: }
  glossary: {absent: "the glossary beside the entity model", owner: }
  business_rules: {absent: "the register of business rules", owner: }
  settings: {absent: "the catalogue of settings", owner: }
claim: _conformance/use_case_model.md_conformance.md
---

# The use case model — {system}

## 1. Purpose

## 2. The system under discussion

### Inside the boundary

### Deliberately outside the boundary

## 3. The actors

| Actor | Kind | Is it a person? | The goal it brings, or the service it gives |
|---|---|---|---|

## 4. The packages

| Package | Code | What it is about | Its use cases |
|---|---|---|---|

### How the packages depend on one another

## 5. The survey

The survey is `survey.md`, generated from the record headers by `extract.py --write-survey`, and never written by hand.

## 6. Which supporting actor each use case calls on

| Use case | Supporting actors it calls on |
|---|---|

## 7. The relationships

### Included steps

| Included | Base use cases | Why it is written once |
|---|---|---|

### Optional steps

| Extension | Base | At the point | When |
|---|---|---|---|

### Generalisations

### The relationships the model deliberately does not draw

## 8. The diagrams

The diagrams are drawn from the record headers by the render step; the model keeps no picture.

## 9. Which use cases are written out, and in what order
```
<!-- skeleton:end -->

## Two habits worth the trouble

**Record what a role may not do**, beside the actor, when two roles must be held by different
people: a constraint recorded on the actor can be checked, and the same constraint mentioned in
one use case is invisible everywhere else.

**Ask who is not here.** The offstage actors — the party the system decides about, an oversight
body — are where missed requirements live, and naming one that never interacts, with the
reason, answers the question a reviewer asks first.
