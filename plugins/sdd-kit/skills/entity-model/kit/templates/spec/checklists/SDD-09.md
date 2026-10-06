---
standard: SDD-09
title: The Application Model
edition: "1.2"
document: SDD-09_The_Application_Model_v1.2.md
sha256: 039b22acac1ac4fe5f2501daa633673e26e369e747810ac1826e26613cc8bab8
produced_by: _working/2026-08-31_house_rebuild/build_house.js at 2026-09-29T20:23:06Z
converted_from: SDD-09_The_Application_Model_v1.2.docx sha256 cc907f738314b9754fb79b832ee49f0cfafd8d3453d5ca82b5def55c768cc3fd (sdd-kit carries its text as Markdown)
---

# SDD-09 · The Application Model — the checklist

*Produced from the document named above by `_working/2026-09-28_the_checklists/extract_checklist.py`, as the last step of its build, and never edited by hand. Every line below is the document's own words, read from it, except the lines in italics, which are this program's.*

*Rules counted in the document: 16. The document states "The sixteen cross-reference rules" (16).*

## Gate — the program's half

### 24. Validation — what a model must pass

A model is validated at four levels before anything is generated from it; the toolchain (kit validate) exits 0 only when all four pass. The intent is to fail at authoring time, not on a deployed instance.

| Level | What it checks |
|---|---|
| 1 · Schema | Structure, types, patterns, enumerations, conditional requirements — this volume’s tables, enforced by JSON Schema 2020-12. |
| 2 · Cross-reference lint | The sixteen L-rules below: every reference in the document resolves, and structural integrity holds. |
| 3 · Platform deltas | D-rules — mechanised quirks of the declared DX version/edition (eleven live, each with a fixture pair proving it fires and passes correctly). Keyed on app.platform. |
| 4 · Config contracts | Every component config block validates against that component’s published contract (strict schemas where published; structural checks and key allow-lists at their honest ceiling elsewhere). |

#### 24.1 The sixteen cross-reference rules

| Rule | Guards |
|---|---|
| L001 | Unique ids within every collection. |
| L002 | Every entity reference resolves (forms, lists, processes, parents, seeds, fixtures, interfaces). |
| L003 | Every attribute reference binds to its entity (fields, columns, filters, status_attr, pk, effects, grid columns, exposed attrs). |
| L004 | Vocabulary references and cascading parents resolve. |
| L005 | Lifecycle integrity: exactly one initial state; transitions between declared states; terminal states have no exits. |
| L006 | Every role reference (transitions, permissions, menus, actions, participants, escalations, scenario actors) is declared. |
| L007 | Every component reference resolves to a versioned catalog entry; engine choices imply their component. |
| L008 | Feature tags resolve; feature→requirement and dependency links hold. |
| L009 | Navigation menu targets exist and match the menu type. |
| L010 | Process integrity: participants declared; activity forms exist; outcomes map only to declared transitions; routing/deadlines reference real activities. |
| L011 | Named-query references resolve; report params exist on their query. |
| L012 | Physical table names unique across entities. |
| L013 | Secret-bearing outbound config values are ${env:NAME} references, never literals. |
| L014 | Acceptance integrity: fixtures resolve; aliases exist; transitions/states/activities/outcomes referenced by scenarios are real. |
| L015 | Grid child form exists and is bound to the child entity. |
| L016 | Bespoke-plugin justifications cite real requirements; reads/writes reference real entities. |

Beyond these, a U-series of user-experience rules (from the embedded Enterprise UX Standard) lints screen constructs against the UX ruleset, and the validator’s exit codes are scripted into CI: 0 valid · 1 schema failure · 2 lint failure.

## Gate — the person's half

*The document states no part of its gate for a person to answer.*

## Form

*The form of this document is the schema of the application model, `application-model.schema.yaml`, which the register names as its template; its parts are the sections below.*

| line | rule |
|---|---|
| 4. Document identity — the model section | *none of its own; section 24 states the checks* |
| 5. Application binding — the app section | *none of its own; section 24 states the checks* |
| 6. Traceability — requirements and features | *none of its own; section 24 states the checks* |
| 7. Roles | *none of its own; section 24 states the checks* |
| 8. Vocabularies | *none of its own; section 24 states the checks* |
| 9. The component catalog | *none of its own; section 24 states the checks* |
| 10. Named queries | *none of its own; section 24 states the checks* |
| 11. Entities — the domain model | *none of its own; section 24 states the checks* |
| 12. Lifecycles — the behavioural heart | *none of its own; section 24 states the checks* |
| 13. Processes — orchestration | *none of its own; section 24 states the checks* |
| 14. Forms | *none of its own; section 24 states the checks* |
| 15. Lists (datalists) | *none of its own; section 24 states the checks* |
| 16. Navigation — the userview | *none of its own; section 24 states the checks* |
| 17. Dashboards | *none of its own; section 24 states the checks* |
| 18. Composite views (360° record consoles) | *none of its own; section 24 states the checks* |
| 19. Reports | *none of its own; section 24 states the checks* |
| 20. Interfaces — the external surface | *none of its own; section 24 states the checks* |
| 21. Seed data | *none of its own; section 24 states the checks* |
| 22. Acceptance — scenarios in the model | *none of its own; section 24 states the checks* |
| 23. The bespoke-plugin budget | *none of its own; section 24 states the checks* |

## Rules

| rule | words | program |
|---|---|---|
| L001 | Unique ids within every collection. | tools/validate.py |
| L002 | Every entity reference resolves (forms, lists, processes, parents, | tools/validate.py |
| L003 | Every attribute reference binds to its entity (fields, | tools/validate.py |
| L004 | Vocabulary references and cascading parents resolve. | tools/validate.py |
| L005 | Lifecycle integrity: exactly one initial state; transitions between | tools/validate.py |
| L006 | Every role reference (transitions, permissions, menus, actions, participants, | tools/validate.py |
| L007 | Every component reference resolves to a versioned catalog | tools/validate.py |
| L008 | Feature tags resolve; feature→requirement and dependency links hold. | tools/validate.py |
| L009 | Navigation menu targets exist and match the menu | tools/validate.py |
| L010 | Process integrity: participants declared; activity forms exist; outcomes | tools/validate.py |
| L011 | Named-query references resolve; report params exist on their | tools/validate.py |
| L012 | Physical table names unique across entities. | tools/validate.py |
| L013 | Secret-bearing outbound config values are ${env:NAME} references, never | tools/validate.py |
| L014 | Acceptance integrity: fixtures resolve; aliases exist; transitions/states/activities/outcomes referenced | tools/validate.py |
| L015 | Grid child form exists and is bound to | tools/validate.py |
| L016 | Bespoke-plugin justifications cite real requirements; reads/writes reference real | tools/validate.py |
