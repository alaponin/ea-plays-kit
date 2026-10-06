# SDD-09 · The Application Model

*This copy is carried by sdd-kit, the SDD method's skills for the service design course. It keeps the edition stated below; where the edition drew an example from the method's author's own client work, this copy carries an example set in Progressa in its place and says so where it does.*

*The point at which the specification stops being written for people and becomes something a program reads and builds from, field by field*

*AN INTERNAL SPECIFICATION  ·  VERSION 1.2  ·  29 SEPTEMBER 2026  ·  IN FORCE*

*One application, one document. A guided reference to every section and every field of the model, and the checks the model has to pass.*

Field | Value
--- | ---
Document | SDD-09 · The Application Model. The single document from which a complete working application is generated, validated and deployed, specified section by section and field by field. It carried the code S2C-02 until this edition.
Version and standing | Version 1.2 · 29 September 2026 · in force. It comes into force by the owner's ruling of 29 September 2026, rulings/2026-09-29-four-draft-standards-in-force.yaml, which accepts it as version 1.1 stated it. It supersedes version 1.1 of 11 August 2026, a draft for customer review, which is kept in x_archive/. What changed: it came into force by the owner's ruling of 29 September 2026, and no rule changed; and the line of this page on who writes the model now says that a person reviews it and approves it or asks for adjustments, by the owner's ruling of the same day, rulings/2026-09-29-what-an-assistant-writes-a-person-approves.yaml. It specifies schema 0.1.6. Version 1.0 was of 14 July 2026. An internal standard of FiscalAdmin OÜ, owned and approved by Aare Lapõnin, for the work of FiscalAdmin OÜ.
Who writes the document it governs | An assistant writes it, under the discipline that a gap is recorded and never invented, and a person reviews it and approves it or asks for adjustments. One model for each application.
Who reads it | The software that turns the model into a working application, and the person who reviews the model before it does.
When it is written | Last of the documents a person edits, and only after the software architecture document is finished.
Rules | None of its own. It states the shape of the model and the checks the model must pass, in section 24.
What it does not cover | What the application is for, and what it is built on. Those are settled in SDD-01 to SDD-08, cited here and never restated.
Author | FiscalAdmin OÜ · Aare Lapõnin

---

*One application — one YAML document. This volume specifies, section by section and field by field, the single canonical model from which a complete Joget DX application is generated, validated, deployed and tested: entities and their lifecycles, processes, forms, lists, navigation, dashboards, reports, interfaces, seed data, acceptance scenarios and the bespoke-plugin budget.*

Contents

1.  Purpose and how to read this specification	3
2.  The application model on one page	3
3.  Conventions used throughout the model	4
3.1  Identifier grammars	4

3.2  Extension points and open decisions	4

3.3  Notation in this volume	5

4.  Document identity — the model section	5
5.  Application binding — the app section	5
6.  Traceability — requirements and features	6
7.  Roles	7
8.  Vocabularies	7
9.  The component catalog	8
10.  Named queries	8
11.  Entities — the domain model	9
11.1  Entity kinds	9

11.2  Entity fields	9

11.3  Attributes and the type system	10

11.4  Structured validations	11

12.  Lifecycles — the behavioural heart	11
13.  Processes — orchestration	13
14.  Forms	14
14.1  Sections and fields	15

14.2  Controls	16

15.  Lists (datalists)	17
16.  Navigation — the userview	18
17.  Dashboards	19
18.  Composite views (360° record consoles)	19
19.  Reports	20
20.  Interfaces — the external surface	20
21.  Seed data	21
22.  Acceptance — scenarios in the model	22
23.  The bespoke-plugin budget	23
24.  Validation — what a model must pass	23
24.1  The sixteen cross-reference rules	24

25.  Versioning, provenance and drift	24
Appendix A.  The complete reference model — Facility Permit	25

Appendix B.  Glossary	33

## 1.  Purpose and how to read this specification

This volume is the complete, guided specification of the application model — the single YAML document (`<app>.app.yaml`) from which a whole Joget DX application is generated: its data model, record lifecycles, processes, screens, lists, navigation, dashboards, reports, APIs, master data, and acceptance tests. It is the customer-facing companion to the platform architecture volume S2C-01; where S2C-01 explains why the platform is built this way, this volume specifies exactly what an application model may and must contain.

The normative source is the machine-readable schema `application-model.schema.yaml` (JSON Schema 2020-12, version 0.1.6), which validates every model document automatically. This volume restates that schema in guided form — each section of the model is presented as a short explanation of intent, a field-by-field reference table, and a worked example — so it can be read end-to-end and discussed in a review meeting without a schema validator at hand. If this text and the schema ever disagree, the schema wins, and the disagreement is a defect in this document.

All examples are drawn from the platform’s reference application, Facility Permit — a deliberately small but complete service (online application, back-office review, approval, issuance) that exercises every section of the model and is regenerated and regression-tested continuously. Its full model appears in Appendix A.

Reading paths. A business reviewer can read sections 2–3, then the opening prose of each section, skipping the reference tables. A technical reviewer should read everything, including the validation annex (§24), which lists every automatic check a model must pass before anything is generated from it.

## 2.  The application model on one page

One application — one YAML document. The model is the only artefact a human edits. Everything downstream — form definitions, datalists, the userview, workflow packages, lifecycle configuration, seed loads, API definitions, dashboards, reports, test suites, the traceability matrix — is generated from it by deterministic tooling, stamped with the model version that produced it, and never edited by hand. A defect in a generated artefact is fixed in the model (or in the generator), and the artefact is regenerated.

The model is compiled from an upstream design ledger (Layer 0 in S2C-01 terms): the decision inventory, use-case model and domain model that analysts produce and gate before anything is built. The compile step from ledger to model is an authored, review-gated activity: an analyst (with tool assistance where available) writes the model against this specification, and it is admitted only through the validator and the platform gate. No upstream generation tooling is presumed by this volume. For the programme this volume was first written for, the ledger is concrete: the decision log and its rulings, the gated use-case descriptions, and the foundation data-model views. This volume specifies the compiled result — Layer 1 — the single source of truth for generation.

A model document has up to 23 top-level sections. Three are mandatory (`model`, `app`, `entities`); the rest are present when the application needs them. They group naturally as follows:

| Group | Sections | What they carry |
|---|---|---|
| Identity & binding | `model`, `app` | Versioning of the document itself; application id and the exact platform (DX version, edition, database) generation targets. |
| Traceability | `requirements`, `features` | The functional-requirement register and the feature decomposition every other object is tagged with; feeds the generated traceability matrix. |
| Actors & meaning | `roles`, `vocabularies` | Logical roles (mapped to Joget groups/permissions) and governed code lists with their seed rows. |
| Reusable machinery | `catalog`, `queries` | The runtime components the app switches on (lifecycle engine, approval service, prefill…) and named SQL reused by lists, dashboards and reports. |
| Domain & behaviour | `entities` (with `lifecycle`), `processes` | The data model, its state machines (the behavioural heart), and the orchestration over them. |
| User interface | `forms`, `lists`, `navigation`, `dashboards`, `views`, `reports` | Screens, grids, menus, KPI/chart surfaces, composite 360° record views, and typeset reports. |
| Integration | `interfaces` | APIs the application exposes; external systems it consumes, always through a catalogued adapter component. |
| Data & assurance | `seed`, `acceptance` | Ordered master-data loads; given/when/then scenarios emitted into the regression harness. |
| Governance | `bespoke_plugins` | The budget of custom Java outside the catalog — every entry justified by a named requirement. |

Before anything is generated, the model passes a four-level validation gate: structural schema validation, sixteen cross-reference lint rules (L001–L016), platform-specific delta rules keyed on the declared DX version, and config-contract validation of every component configuration against that component’s published contract. Section 24 lists them all.

## 3.  Conventions used throughout the model

### 3.1  Identifier grammars

Every identifier in the model belongs to one of five grammars. They are deliberately strict: identifiers flow into physical table names, Joget object ids and generated code, where the platform imposes hard limits.

| Grammar | Pattern | Used for |
|---|---|---|
| `snakeId` | `^[a-z][a-z0-9_]{0,39}$` | Most model ids: entities, roles, vocabularies, queries, states, transitions, sections, processes… |
| `kebabId` | `^[a-z][a-z0-9-]{0,39}$` | Catalog component and bespoke-plugin ids (e.g. status-framework, form-prefill). |
| `freeId` | `^[A-Za-z0-9][A-Za-z0-9_.-]{0,39}$` | Requirement, feature and scenario ids (FR-001, F01, t01_submit…). |
| `attrId` | `^[a-z][a-zA-Z0-9_]{0,38}$` | Attribute / column logical ids. camelCase is tolerated for continuity with existing Joget field ids; the physical column gets a c_ prefix. |
| `semver` | `^\d+\.\d+\.\d+(-…)?$` | Version numbers (spec_version, catalog versions). |

Two platform caps are enforced at the schema level rather than discovered at deployment: a form id is at most 24 characters (a hard Joget DX limit) and a physical table name at most 40 (so the platform-prefixed `app_fd_` name stays inside MySQL/PostgreSQL identifier limits with headroom).

### 3.2  Extension points and open decisions

Unknown keys beginning `x-` are allowed everywhere and ignored by validation — they are annotation extension points for working notes, upstream references and projector hints that have not yet been promoted into the schema. Keys marked `x-decision` in the schema flag design decisions that are closed by an Architecture Decision Record (ADR) before 1.0 of the construct concerned.

### 3.3  Notation in this volume

In the reference tables, Req. marks fields that are mandatory within their object (●) or conditionally mandatory (◐, condition given in the Meaning column); blank means optional. Defaults are stated in the Meaning column. Field names, literal values and YAML fragments appear in `fixed font`. Enumerated values are given as a \| separated list.

## 4.  Document identity — the model section

The `model` section describes the specification document itself, not the application. Its two version numbers carry the platform’s provenance discipline: `schema_version` is const-pinned — a document copied to an environment with a different schema fails validation instantly — and `spec_version` is bumped on every edit, however small, because it is written into the provenance stamp of every generated artefact and drives drift detection.

| Field | Type / allowed values | Req. | Meaning |
|---|---|---|---|
| `schema_version` | `"0.1.6"` (const) | ● | The schema this document targets. Fixed by the schema itself; any other value fails validation. |
| `spec_version` | semver | ● | Version of this application spec. Bump on every change; consumed by provenance stamps and drift comparison. |
| `status` | `draft \| review \| approved` |  | Editorial status of the document. |
| `authors` | array of string |  | Document authors. |

| `model:`<br>`schema_version: "0.1.6"`<br>`spec_version: "0.1.6"`<br>`status: draft`<br>`authors: ["FiscalAdmin OU"]` |
|---|

*Facility Permit — document identity.*

## 5.  Application binding — the app section

The `app` section names the application and binds it to an exact platform. The binding is not documentation: generators and the platform-delta lint rules key on it. Declaring `edition: community`, for example, makes any Enterprise-only construct (form grids, wizards, SQL charts, Jasper reports, dashboards) a validation error rather than a deployment surprise.

| Field | Type / allowed values | Req. | Meaning |
|---|---|---|---|
| `id` | `^[a-zA-Z][a-zA-Z0-9_]{1,19}$` | ● | Joget application id (APP_ID). Short; used in package assembly and push tooling. |
| `name` | string | ● | Display name. |
| `description` | string |  | One-line description of the service. |
| `platform.dx` | `"8.0" \| "8.1" \| "9.0"` | ● | Target DX version. Platform-delta rules and generator conventions are keyed on this. |
| `platform.edition` | `enterprise \| community` | ● | Edition gate for Enterprise-only realizations. |
| `platform.db` | `mysql \| postgres` | ● | Target database. |
| `conventions` | object |  | App-wide naming conventions the projector applies (e.g. numbered form-name prefixes). |

| `app:`<br>`id: facilityPermit`<br>`name: Facility Permit`<br>`description: Online application, back-office review, and issuance of facility operating permits.`<br>`platform: { dx: "9.0", edition: enterprise, db: postgres }`<br>`conventions:`<br>`form_name_prefix: numbered   # "01.01 - ..." style applied by the projector` |
|---|

*Facility Permit — application binding.*

## 6.  Traceability — requirements and features

Traceability is generated, never maintained by hand. The `requirements` section is the functional-requirement register (or a set of references into an upstream catalogue); the `features` section decomposes delivery into vertical, dependency-ordered slices. Every major object elsewhere in the model — entities, forms, lists, processes, scenarios, plugins — carries a `feature` tag. From these three ingredients the toolchain emits the TRACE matrix (requirement → feature → realising objects → proving tests → produced artefacts) as a build output, so it can never go stale.

#### 6.1  requirements[]

| Field | Type / allowed values | Req. | Meaning |
|---|---|---|---|
| `id` | freeId | ● | Requirement id, e.g. FR-001. |
| `text` | string | ● | The requirement statement. |
| `source` | string |  | Upstream document / section reference — the citation column. |

#### 6.2  features[]

| Field | Type / allowed values | Req. | Meaning |
|---|---|---|---|
| `id` | freeId | ● | Feature id; convention <BB>-Fnn-<slug> or Fnn. |
| `name` | string | ● | Feature name. |
| `requirements` | array of freeId |  | Requirements this feature realises. |
| `depends_on` | array of freeId |  | Features that must be delivered first. |

| `requirements:`<br>`- { id: FR-001, text: "An applicant can submit a facility permit application online.", source: "ModuleSpec §2.1" }`<br>`- { id: FR-004, text: "A rejection must carry a rejection reason.", source: "ModuleSpec §2.3" }`<br>`features:`<br>`- { id: F01, name: "Application intake",  requirements: [FR-001, FR-002, FR-005] }`<br>`- { id: F02, name: "Review and decision", requirements: [FR-003, FR-004, FR-006], depends_on: [F01] }` |
|---|

*Facility Permit — requirement register and feature slices (abridged).*

## 7.  Roles

Roles are logical: the model says who in business terms, and the projector maps each role to Joget groups, userview permissions and form/list permission classes. Every role reference anywhere in the model — lifecycle transitions, menu visibility, list actions, process participants, scenario actors — must resolve to a declared role (lint rule L006).

| Field | Type / allowed values | Req. | Meaning |
|---|---|---|---|
| `id` | snakeId | ● | Role id, referenced everywhere. |
| `name` | string | ● | Display name. |
| `description` | string |  | What the role does. |
| `directory_hint` | string |  | Optional mapping hint to an external directory group. |

| `roles:`<br>`- { id: applicant,  name: Applicant }`<br>`- { id: officer,    name: Permit Officer }`<br>`- { id: supervisor, name: Supervisor }` |
|---|

*Facility Permit — roles.*

## 8.  Vocabularies

Vocabularies are the simple, governed code lists of the application — code and label, optionally cascading from a parent vocabulary (the district → centre pattern). For each vocabulary the projector generates the master-data lookup form, its datalist and the seed load, so a code list is declared once and never re-keyed. Rich, multi-attribute master data is not a vocabulary: it is modelled as an entity of kind `md_lookup` (§11).

| Field | Type / allowed values | Req. | Meaning |
|---|---|---|---|
| `id` | snakeId | ● | Vocabulary id; referenced by attributes of type enum. |
| `name` | string | ● | Display name. |
| `parent` | snakeId |  | Parent vocabulary for cascading lookups; rows then carry parent_code. |
| `rows` | array | ◐ | Inline seed rows `{code, name[, parent_code]}`. Either rows or file supplies the seed. |
| `file` | string | ◐ | Relative path to a CSV seed (code,name[,parent_code]) as the alternative to inline rows. |

| `vocabularies:`<br>`- id: rejection_reason`<br>`name: Rejection Reason`<br>`rows:`<br>`- { code: incomplete,  name: "Incomplete documentation" }`<br>`- { code: failed_insp, name: "Failed inspection" }`<br>`- { code: ineligible,  name: "Applicant not eligible" }` |
|---|

*Facility Permit — one of four vocabularies.*

## 9.  The component catalog

The `catalog` section lists the reusable runtime components this application switches on — the lifecycle engine (status-framework), the approval service, form prefill, identity adapters and so on. The platform is catalog-first: behaviour is configuration over proven components wherever possible, and custom Java is a budgeted exception (§23). Every `component:` reference elsewhere in the model must resolve to an entry here (lint rule L007), and each component publishes its own configuration contract — a JSON Schema of exactly which settings it accepts — against which local `config` blocks are validated during lint.

| Field | Type / allowed values | Req. | Meaning |
|---|---|---|---|
| `component` | kebabId | ● | Component id from the platform registry (e.g. status-framework, approval-service, form-prefill). |
| `version` | string | ● | Semver or range; pinned at generation time. |
| `scope` | `global \| per_use` (default per_use) |  | Whether one global configuration applies, or each use site configures its own. |
| `config` | object |  | Global configuration when scope is global; validated against the component’s config contract. |

| `catalog:`<br>`- { component: status-framework, version: "2.x", scope: global }`<br>`- { component: approval-service, version: "1.x" }`<br>`- { component: form-prefill,     version: "1.x" }`<br>`- { component: identity-adapter, version: "0.x" }` |
|---|

*Facility Permit — the components in use.*

## 10.  Named queries

Every non-trivial number and listing in the application — JDBC-bound datalists, dashboard tiles, report datasources — reads a named query declared once here. One definition, many consumers: when the meaning of “pending applications” changes, it changes in exactly one place. Parameters are typed; a report or filter that references a parameter its query does not declare fails lint (L011).

| Field | Type / allowed values | Req. | Meaning |
|---|---|---|---|
| `id` | snakeId | ● | Query id, referenced by lists, dashboards and reports. |
| `description` | string |  | What the query answers. |
| `sql` | string | ● | The SQL statement (platform-prefixed physical names, e.g. app_fd_…, c_…). |
| `params[]` | `{id, type}`; type: `string \| integer \| decimal \| date \| datetime \| boolean` |  | Typed parameters, referenced as $P{…} (Jasper) or #requestParam.…# (JDBC lists). |

| `queries:`<br>`- id: q_apps_by_status`<br>`description: Pipeline distribution for the dashboard chart.`<br>`sql: >-`<br>`SELECT c_status AS status, COUNT(\*) AS n`<br>`FROM app_fd_permit_application GROUP BY c_status`<br>`- id: q_certificate`<br>`description: Certificate datasource for the Jasper report.`<br>`sql: >-`<br>`SELECT c_application_no, c_applicant_name, c_facility_type, c_district, c_decided_at`<br>`FROM app_fd_permit_application WHERE c_application_no = $P{application_no}`<br>`params:`<br>`- { id: application_no, type: string }` |
|---|

*Facility Permit — named queries (abridged).*

## 11.  Entities — the domain model

Entities are the heart of the model: the records the application keeps, at national scale, with legal effect. Each entity declares its classification (`kind`), its physical table, its attributes, its indexes and audit level — and, for case-bearing entities, its lifecycle (§12). Entity design answers the grain question explicitly: what one record represents and what makes two records duplicates.

### 11.1  Entity kinds

| Kind | Meaning and generation consequence |
|---|---|
| `main` | A primary case or registry record. Maps to a primary form and table; usually carries the lifecycle. |
| `child` | A one-to-many detail of a parent entity (inspections of an application). Requires parent; realised as a grid sub-form. |
| `junction` | A many-to-many link record. Requires parent. |
| `md_lookup` | Rich master data (multi-attribute reference records) — the big sibling of a vocabulary. |
| `config` | Operational configuration data (fee matrices, thresholds) — seeded, governed, never hard-coded. |
| `log_event` | Append-only audit/event records; typically generated rather than user-entered. |

### 11.2  Entity fields

| Field | Type / allowed values | Req. | Meaning |
|---|---|---|---|
| `id` | snakeId | ● | Entity id, referenced by forms, lists, processes, seeds, fixtures, interfaces. |
| `name` | string | ● | Display name. |
| `kind` | `main \| child \| junction \| md_lookup \| config \| log_event` | ● | Classification (see 11.1). |
| `table` | `^[a-z][a-z0-9_]{1,39}$` | ● | Physical table name. The platform prefixes app_fd_ (columns c_); the 40-char cap keeps prefixed names inside database identifier limits. Must be unique across entities (L012). |
| `scale` | `bounded \| operational` |  | Referenced-set scale. operational = unbounded, grows with operations — editable references to it render as a search-select popup, never a dropdown. Defaults: operational when the entity has a lifecycle, bounded otherwise. |
| `feature` | freeId |  | Feature tag for traceability and incremental generation. |
| `canonical_ref` | object |  | Mapping to a canonical/reference model (TA-RDM, GovStack RegBB, sector model): model, path, and a list of declared divergences {what, reason}. |
| `pk` | object |  | Primary-key strategy: `strategy: uuid \| id_generator \| natural` (default uuid); `format` (e.g. PA-??????) and `attr` for business keys. |
| `attributes[]` | array (min 1) | ● | The attribute list — see 11.3. |
| `lifecycle` | object |  | The entity’s state machine — see §12. Only for case-bearing entities; declared here, before any process. |
| `audit` | `none \| status \| full` (default none) |  | status = the lifecycle engine’s transition log; full = a log_event entity generated per change. |
| `indexes[]` | `{attrs[], unique}` |  | Secondary indexes; unique defaults to false. |
| `validations[]` | array |  | Structured cross-field conditional requirements — see 11.4. |
| `parent` | `{entity, fk_attr}` | ◐ | Required for kind child / junction: the owning entity and the FK attribute. |
| `effective_dating` | `{from[, to]}` |  | Marks the entity as effective-dated (a validity interval, not just date fields); the projector realises as-at semantics — a currently-effective view — so temporal validity is expressed, not flattened. (Schema 0.2 construct.) |

### 11.3  Attributes and the type system

Attributes are typed once, on the entity, and everything else inherits: a form field bound to an attribute inherits its type, control and validation; a list column inherits its formatting hooks; the generated table gets the right column. Two attribute types carry conditional requirements enforced by the schema itself: `enum` requires a `vocabulary`, and `ref` requires a `ref` block naming the target entity.

| Field | Type / allowed values | Req. | Meaning |
|---|---|---|---|
| `id` | attrId | ● | Logical id; physical column is c_<id>. |
| `name` | string |  | Display name (defaults derived from id). |
| `type` | `string \| text \| integer \| decimal \| boolean \| date \| datetime \| enum \| ref \| file \| json \| computed` | ● | The logical type. enum → coded value from a vocabulary; ref → FK to another entity; computed → derived, with formula. |
| `required` | boolean (default false) |  | Mandatory at entry. |
| `unique` | boolean (default false) |  | Uniqueness constraint. |
| `length` | integer |  | For string. |
| `precision / scale` | integer |  | For decimal. |
| `vocabulary` | snakeId | ◐ | Required when type = enum — the vocabulary supplying codes. |
| `ref` | `{entity[, display]}` | ◐ | Required when type = ref: target entity and the attribute shown via the lookup pattern. |
| `formula` | string |  | For type computed (calculation / concatenation realizations). |
| `default` | any |  | Default value. |
| `pattern` | string |  | Regex constraint (e.g. national-id shape). |
| `description` | string |  | Meaning of the attribute — carried into generated artefacts. |
| `govstack` | `{path[, type_path, type_value, transform]}` |  | Attribute-level canonical GovStack mapping — the authored semantic residue of the RegBB integration seam. Attributes without it default to extension.<id> in the emitted channel contract. |

### 11.4  Structured validations

Conditional requirements of the form “if X then these fields / this grid are required” are declared as data, not prose: each rule names its trigger (`when: {field, equals}`), what becomes required (`require_fields`, `require_grids`, `min_entries`) and the user-facing `message`. They are realised as guard or form-quality rules, and emitted verbatim into the RegBB validation-rules contract where the entity participates in a registration channel.

| `entities:`<br>`- id: permit_application`<br>`name: Permit Application`<br>`kind: main`<br>`table: permit_application`<br>`feature: F01`<br>`canonical_ref:`<br>`model: GovStack-RegBB`<br>`path: registration.application`<br>`divergences:`<br>`- { what: "issued state added beyond RegBB approve/reject", reason: "permit issuance is a distinct legal act" }`<br>`pk: { strategy: id_generator, format: "PA-??????", attr: application_no }`<br>`audit: status`<br>`attributes:`<br>`- { id: application_no,   type: string, unique: true, length: 12, description: "Business key, generated." }`<br>`- { id: applicant_name,   type: string, required: true, length: 120 }`<br>`- { id: national_id,      type: string, required: true, pattern: "^[0-9]{11}$" }`<br>`- { id: facility_type,    type: enum, vocabulary: facility_type, required: true }`<br>`- { id: status,           type: string, length: 20, description: "Lifecycle status attr." }`<br>`- { id: rejection_reason, type: enum, vocabulary: rejection_reason }`<br>`- { id: decided_at,       type: datetime }` |
|---|

*Facility Permit — the main entity (attributes abridged; lifecycle shown in §12).*

## 12.  Lifecycles — the behavioural heart

A lifecycle is the complete life story of a long-lived record: its states, the allowed moves between them, who may make each move, under what condition, and with what side effects. It is declared on the entity, before any process — processes reference lifecycle transitions and may never invent a state change the lifecycle does not define. By default the status-framework catalog component executes the lifecycle at runtime: legal transitions apply and are audited; illegal ones are refused by the engine, not by screen discipline.

| Field | Type / allowed values | Req. | Meaning |
|---|---|---|---|
| `status_attr` | attrId | ● | The entity attribute that carries the current state. |
| `engine` | `status_framework \| native` (default status_framework) |  | status_framework = the catalog component provides transition execution and the audit trail; native = plain field updates. |
| `states[]` | array (min 2) | ● | See below. |
| `transitions[]` | array (min 1) | ● | See below. |

#### 12.1  states[]

| Field | Type / allowed values | Req. | Meaning |
|---|---|---|---|
| `id` | snakeId | ● | State id. |
| `name` | string |  | Display name. |
| `initial` | boolean (default false) |  | Exactly one state must be initial (L005). |
| `terminal` | boolean (default false) |  | Terminal states have no outgoing transitions (L005). |
| `tone` | `grey \| blue \| green \| amber \| red` |  | Status-badge colour; absent → grey (initial) / amber (intermediate) / green (terminal). |

#### 12.2  transitions[]

| Field | Type / allowed values | Req. | Meaning |
|---|---|---|---|
| `id` | snakeId | ● | Transition id — referenced by process outcomes, list actions and scenarios. |
| `from / to` | snakeId | ● | Declared states (L005). |
| `trigger` | `user \| system \| timer \| process` (default user) |  | What fires the transition. |
| `roles` | array of snakeId |  | The authority matrix row: who may execute. Empty for system/timer triggers. |
| `guard` | string |  | The human-readable rule that must hold (its realization — route condition or validator — is a design-stage decision). |
| `guard_expr` | `<attr> eq\|ne\|gt\|lt\|ge\|le <value>` |  | The machine-checkable companion: a predicate the runtime engine evaluates against the record before the transition applies (e.g. total_amount eq 0). Word operators, because > and \| are configuration separators. |
| `effects[]` | array of effect |  | Side effects executed on transition — see 12.3. |

#### 12.3  Effects

| Effect type | Meaning and companion fields |
|---|---|
| `audit` | Write the transition to the audit trail (the default discipline on every meaningful move). |
| `set_attr` | Set an attribute: `attr`, `value` (e.g. `${now}`). |
| `notify` | Send a notification: `template` and `to` (`role:<id>` or `attr:<id>` as the address source). |
| `component` | Invoke a catalog component with `config` (contract-validated). |
| `emit_event` | Emit a domain event for downstream consumers. |

| `lifecycle:`<br>`status_attr: status`<br>`engine: status_framework`<br>`states:`<br>`- { id: draft,        name: Draft, initial: true, tone: grey }`<br>`- { id: submitted,    name: Submitted, tone: amber }`<br>`- { id: under_review, name: Under review, tone: blue }`<br>`- { id: approved,     name: Approved, tone: green }`<br>`- { id: rejected,     name: Rejected, terminal: true, tone: red }`<br>`- { id: issued,       name: Issued, terminal: true, tone: green }`<br>`transitions:`<br>`- id: submit`<br>`from: draft`<br>`to: submitted`<br>`roles: [applicant]`<br>`effects:`<br>`- { type: audit }`<br>`- { type: set_attr, attr: submitted_at, value: "${now}" }`<br>`- id: approve`<br>`from: under_review`<br>`to: approved`<br>`roles: [officer]`<br>`guard: "no inspection with result = fail"`<br>`effects:`<br>`- { type: audit }`<br>`- { type: set_attr, attr: decided_at, value: "${now}" }`<br>`- { type: notify, template: permit_decision, to: "attr:email" }` |
|---|

*Facility Permit — lifecycle of the permit application (abridged: 6 states, 5 transitions).*

| Rule — Lifecycle integrity is machine-checked (L005): exactly one initial state, every transition between declared states, no exits from terminal states. Every role named on a transition must be declared (L006). |
|---|

## 13.  Processes — orchestration

Processes orchestrate work over a case-bearing entity: who does what, in which order, with which deadlines. Two realizations exist. `xpdl` generates a Joget workflow package (participants, activities, routing); `approval_service` configures the Decision & Approval Service catalog component (sequential/parallel steps, quorum, segregation of duties, delegation). Both drive the same entity lifecycle: a human outcome maps to a declared transition, and validation refuses a process that tries to invent a state change (L010).

| Field | Type / allowed values | Req. | Meaning |
|---|---|---|---|
| `id` | snakeId | ● | Process id. |
| `name` | string | ● | Display name. |
| `entity` | snakeId | ● | The case entity this process drives. |
| `realization` | `xpdl \| approval_service` | ● | Which machinery realises it. |
| `feature` | freeId |  | Feature tag. |
| `participants[]` | `{id, map}` |  | Work assignment: map is `role:<roleId>`, `hash:<#var#>` or `plugin:<mapper>` — mirroring XPDL participant mapping. |
| `activities[]` | array of activity |  | The steps — see 13.1. |
| `routing[]` | `{after, when, goto}` |  | Route conditions over outcomes/variables; empty when = the default route. |
| `deadlines[]` | `{on, after, escalate_to, effects}` |  | ISO-8601 durations (e.g. P3D) on an activity, with escalation to a role and optional effects. |
| `approval` | object |  | approval_service realization config (bands, chains, quorum, SoD, delegation) — validated against the DAS config contract. |

#### 13.1  Activities and outcomes

An activity is `human` (requires a `participant` and a `form`) or `tool` (requires a catalog `component`). Human activities declare their decision `outcomes`, and each outcome names the lifecycle `transition` it executes — the single rule that keeps screens, workflow and the state machine telling one story.

| `processes:`<br>`- id: permit_review`<br>`name: Permit Review`<br>`entity: permit_application`<br>`realization: approval_service`<br>`participants:`<br>`- { id: reviewer,   map: "role:officer" }`<br>`- { id: escalation, map: "role:supervisor" }`<br>`activities:`<br>`- id: review`<br>`kind: human`<br>`participant: reviewer`<br>`form: frmPermitReview`<br>`outcomes:`<br>`- { id: approve, label: Approve, transition: approve }`<br>`- { id: reject,  label: Reject,  transition: reject }`<br>`deadlines:`<br>`- { "on": review, after: P3D, escalate_to: "role:supervisor" }`<br>`approval:`<br>`mode: single`<br>`sod: { initiator_cannot_review: true }` |
|---|

*Facility Permit — the review process (approval-service realization).*

## 14.  Forms

Forms are declared logically: sections of fields, each field either bound to an entity attribute (`attr`) — inheriting its type, control and validation — or form-local (`id` + `control`). The projector turns this into Joget form-definition JSON, applying the enterprise UX standard: identify by identifier, create from source, act by lifecycle transition, never re-type what the ledger already knows.

| Field | Type / allowed values | Req. | Meaning |
|---|---|---|---|
| `id` | `^[a-zA-Z][a-zA-Z0-9_]{0,23}$` | ● | Joget form id — hard 24-character platform cap, enforced here rather than at deployment. |
| `name` | string | ● | Display name; numbered prefix convention applied via app.conventions. |
| `entity` | snakeId | ● | The entity the form reads/writes. |
| `purpose` | `create \| edit \| view \| review \| wizard_step \| wizard` | ● | The moment in the case the form serves; drives generation defaults. |
| `layout` | `detail_360` |  | Optional record-console layout: sections render as tabs (enterprise multi-page form), sections marked header:true stay pinned as the context header, and a user-triggered lifecycle adds an Actions tab. |
| `wizard` | `{steps[], partial_store}` | ◐ | For purpose wizard: ordered wizard_step form ids (min 2); Enterprise realization. |
| `sections[]` | array (min 1) | ● | See 14.1. |
| `validation[]` | `{rule, message, realization}` |  | Form-level (cross-field) rules; realization: validator_plugin \| form_quality \| beanshell. |
| `permissions` | `{roles[], note}` |  | Who may use the form. |
| `prefill` | object | ◐ | Form-level prefill configuration realised by the form-prefill catalog component; requires component, body validated against its contract and passed through verbatim. |
| `post_actions[]` | `{on, component\|process, config}` |  | Actions after save (on: create \| edit \| both) — start a process or run a component. |
| `feature` | freeId |  | Feature tag. |

#### 14.1  Sections and fields

| Field | Type / allowed values | Req. | Meaning |
|---|---|---|---|
| `sections[].id` | snakeId | ● | Section id. |
| `sections[].label` | string |  | Section heading. |
| `sections[].columns` | 1–4 (default 2) |  | Layout columns. |
| `sections[].readonly` | boolean |  | Render the whole section read-only (review/summary panels). |
| `sections[].header` | boolean |  | detail_360 layout only: pin this section above the tabs as the context header. |
| `fields[].attr` | attrId | ◐ | Bound field: the entity attribute. Either attr, or id + control (unbound). |
| `fields[].id + control` | attrId + enum | ◐ | Unbound (form-local) field; control is then mandatory. |
| `fields[].control` | see 14.2 |  | Bound fields derive a default control from the attribute type; set only to override. |
| `fields[].label` | string |  | Field label override. |
| `fields[].readonly` | boolean |  | Read-only field. |
| `fields[].required` | boolean |  | Override; bound fields inherit from the attribute. |
| `fields[].child` | `{entity, form, columns[]}` | ◐ | Required when control = grid: the one-to-many child entity, its row form, and grid columns. |
| `fields[].deletable` | boolean (default false) |  | Grid only: rows may be removed. Editable grids allow add/edit; this adds remove. |
| `fields[].validator / config` | object |  | Element-specific extras passed through to the projector. |

#### 14.2  Controls

| Control | Notes |
|---|---|
| `text · textarea · number · date · datetime · select · radio · checkbox` | The plain entry set; usually derived from the attribute type rather than declared. |
| `hidden · id_generator · calculation · concat` | System-carried values: hidden context, generated business keys, computed fields. |
| `lookup · smart_search` | Reference pickers over another entity or vocabulary; references to operational-scale entities render as search-select popups, never dropdowns. |
| `grid · embedded_list` | One-to-many child records (requires child); embedded read-only listings. |
| `file · gis_polygon · custom_html · custom` | Attachments, spatial capture, presentation HTML, and escape-hatch custom elements (custom requires class_name). |

| `forms:`<br>`- id: frmPermitReview`<br>`name: Permit Review`<br>`entity: permit_application`<br>`purpose: review`<br>`feature: F02`<br>`sections:`<br>`- id: sec_summary`<br>`label: Application`<br>`readonly: true`<br>`fields:`<br>`- { attr: application_no }`<br>`- { attr: applicant_name }`<br>`- { attr: facility_type }`<br>`- { attr: district }`<br>`- id: sec_inspections`<br>`label: Inspections`<br>`columns: 1`<br>`fields:`<br>`- id: inspections`<br>`control: grid`<br>`label: Inspections`<br>`child: { entity: inspection, form: frmInspectionRow, columns: [inspected_at, result] }`<br>`- id: sec_decision`<br>`label: Decision`<br>`columns: 1`<br>`fields:`<br>`- { attr: rejection_reason, label: "Rejection reason (required when rejecting)" }`<br>`validation:`<br>`- rule: "outcome == reject implies rejection_reason is not empty"`<br>`message: "Rejection reason is mandatory when rejecting."`<br>`realization: validator_plugin`<br>`permissions: { roles: [officer] }` |
|---|

*Facility Permit — the officer’s review form: summary panel, inspections grid, decision section.*

## 15.  Lists (datalists)

Lists are the working grids of the application — registers, worklists, “my applications”. A list reads either an entity (the form-data binder path; `source.form` disambiguates when an entity has several forms) or a named query (the JDBC path, for joins and aggregates). Columns can format themselves from what the model already knows: an enum column renders its vocabulary label, a lifecycle status renders as a coloured badge, dates format consistently.

| Field | Type / allowed values | Req. | Meaning |
|---|---|---|---|
| `id` | `^[a-zA-Z][a-zA-Z0-9_]{0,29}$` | ● | Datalist id. |
| `name` | string | ● | Display name. |
| `source` | `{entity[, form][, extra_condition]} \| {query}` | ● | Exactly one of entity or query. |
| `columns[]` | array (min 1) | ● | Each column: `attr` (entity path) or `expr` (query alias), `label`, `format`: `none \| date \| datetime \| currency \| options \| status_badge \| link`, `width`. |
| `filters[]` | array |  | Filter types: `text \| select \| cascading_select \| date_range \| status`. Select filters auto-derive options from vocabularies and lifecycle states; query-source filters name their `param` or explicit `options`. |
| `actions[]` | array |  | Row/list actions: `open_form \| launch_process \| execute_transition \| link \| delete`, with role gating and row-link parameters (`href_column`, `href_param`). |
| `sort` | `{by, dir}` (dir default desc) |  | Default sort. |
| `page_size` | integer (default 20) |  | Page size. |
| `permissions` | `{roles[], note}` |  | Who sees the list. |
| `feature` | freeId |  | Feature tag. |

| `lists:`<br>`- id: dlPermitRegister`<br>`name: Permit Register`<br>`feature: F02`<br>`source: { entity: permit_application, form: frmPermitApply }`<br>`columns:`<br>`- { attr: application_no, label: "No." }`<br>`- { attr: applicant_name, label: Applicant }`<br>`- { attr: facility_type,  label: Type }`<br>`- { attr: status,         label: Status, format: status_badge }`<br>`- { attr: submitted_at,   label: Submitted, format: datetime }`<br>`filters:`<br>`- { attr: facility_type, type: select }`<br>`- { attr: status,        type: select }`<br>`- { attr: submitted_at,  type: date_range, label: "Submitted between" }`<br>`sort: { by: submitted_at, dir: desc }`<br>`permissions: { roles: [officer, supervisor] }` |
|---|

*Facility Permit — the back-office register.*

## 16.  Navigation — the userview

Navigation declares the portal: personas → categories → menus. Categories are role-gated (an empty `roles` list means visible to all authenticated users), and each menu entry names its target by type. The `crud` type is the workhorse: it exposes an entity’s form-and-list pair as a full maintain screen, with `add: false` to suppress the New button (records that only enter by an engine or audited path) and `delete: false` where records are never deleted (history retention on cases).

| Field | Type / allowed values | Req. | Meaning |
|---|---|---|---|
| `userview_id` | `^[a-zA-Z][a-zA-Z0-9_]{0,29}$` | ● | Userview id. |
| `name` | string |  | Portal name. |
| `theme` | object |  | Theme configuration (name is DX-version-dependent). |
| `categories[]` | array (min 1) | ● | Each: `id`, `label`, optional `roles[]`, and `menus[]` (min 1). |
| `menus[].type` | `form \| list \| crud \| dashboard \| report \| html \| api \| external_link \| inbox` | ● | Menu kind; L009 checks the target field matches the type and exists. |
| `menus[].label` | string | ● | Menu label. |
| `menus[].form / list / entity / dashboard / report / html / href` | per type | ◐ | The target: crud names the entity plus its form and list; inbox needs no target. |
| `menus[].add / delete` | boolean |  | crud only: suppress New / row delete. |
| `menus[].roles` | array of snakeId |  | Menu-level role gate. |

| `navigation:`<br>`userview_id: uvPermit`<br>`name: Facility Permits`<br>`categories:`<br>`- id: cat_apply`<br>`label: Apply`<br>`roles: [applicant]`<br>`menus:`<br>`- { type: form, label: "New permit application", form: frmPermitApply }`<br>`- { type: crud, label: "My applications", entity: permit_application,`<br>`form: frmPermitApply, list: dlMyApplications, delete: false }`<br>`- id: cat_office`<br>`label: Back office`<br>`roles: [officer, supervisor]`<br>`menus:`<br>`- { type: crud, label: "Permit register", entity: permit_application,`<br>`form: frmPermitReview, list: dlPermitRegister, delete: false }`<br>`- { type: inbox,     label: "My tasks" }`<br>`- { type: dashboard, label: "Review pipeline", dashboard: dash_office }`<br>`- { type: report,    label: "Permit certificate", report: rpt_certificate }` |
|---|

*Facility Permit — two personas, two categories.*

## 17.  Dashboards

Dashboards are KPI tiles and charts over named queries — realised natively (Enterprise SQL-chart and dashboard menus), reading server-side SQL, never scraping rendered screens. A `chart` tile names its query and the column aliases for the category and value axes; a `kpi` tile carries RAG thresholds.

| Field | Type / allowed values | Req. | Meaning |
|---|---|---|---|
| `id` | snakeId | ● | Dashboard id, referenced from navigation. |
| `name` | string |  | Display name. |
| `tiles[]` | array (min 1) | ● | The tiles. |
| `tiles[].kind` | `kpi \| chart` | ● | Tile kind. |
| `tiles[].query` | snakeId |  | The named query feeding the tile (L011). |
| `tiles[].chart_type` | `bar \| line \| pie \| area \| table` |  | Chart tiles. |
| `tiles[].key / value` | string |  | Chart tiles: query column aliases for the category/x axis and the numeric/y axis. |
| `tiles[].thresholds` | `{green, amber, red}` |  | KPI tiles: RAG thresholds. |

| `dashboards:`<br>`- id: dash_office`<br>`name: Review Pipeline`<br>`feature: F02`<br>`tiles:`<br>`- kind: chart`<br>`chart_type: bar`<br>`label: Applications by status`<br>`query: q_apps_by_status`<br>`key: status`<br>`value: n` |
|---|

*Facility Permit — the office dashboard.*

## 18.  Composite views (360° record consoles)

A composite `detail` view presents a main entity together with its child records as one surface — the case-360 console — instead of disconnected forms. The projector emits the composite (userview surface plus embedded child grids). Together with the `detail_360` form layout (§14), this is the model’s answer to the officer’s daily question: everything about this case, on one screen, without re-querying. These are schema 0.2 constructs, available in 0.1.6 documents.

| Field | Type / allowed values | Req. | Meaning |
|---|---|---|---|
| `id` | snakeId | ● | View id. |
| `name` | string |  | Display name. |
| `kind` | `detail` | ● | Composite kind (detail = the 360 record view). |
| `entity` | snakeId | ● | The main entity. |
| `sections[]` | `{form \| child, as: grid \| form, label}` |  | Ordered panels: a form over the main record, or a child entity rendered as a grid. |

## 19.  Reports

Reports are typeset, pixel-laid-out documents — certificates, statements, financial reports — realised by JasperReports (Enterprise). A report names its datasource query, its parameters (which must exist on that query — L011) and its output formats. Grids are not reports; anything that must print, sign or export goes here.

| Field | Type / allowed values | Req. | Meaning |
|---|---|---|---|
| `id` | snakeId | ● | Report id, referenced from navigation. |
| `name` | string | ● | Display name. |
| `engine` | `jasper` | ● | Realization engine. |
| `query` | snakeId | ● | The named datasource query. |
| `params` | array of snakeId |  | Parameters, resolved against the query’s declared params. |
| `output` | `[pdf \| xlsx \| docx]` (default [pdf]) |  | Output formats. |
| `feature` | freeId |  | Feature tag. |

| `reports:`<br>`- id: rpt_certificate`<br>`name: Permit Certificate`<br>`engine: jasper`<br>`query: q_certificate`<br>`params: [application_no]`<br>`output: [pdf]` |
|---|

*Facility Permit — the issued certificate.*

## 20.  Interfaces — the external surface

The `interfaces` section declares everything that crosses the application boundary. Inbound entries are APIs this application exposes (generated as API Builder definitions, authenticated by api_id/api_key — not basic auth). Outbound entries are external systems it consumes — always through a catalogued adapter component, never ad-hoc HTTP in code, so failure behaviour, retries and configuration stay governed.

#### 20.1  inbound[]

| Field | Type / allowed values | Req. | Meaning |
|---|---|---|---|
| `id` | snakeId | ● | API id. |
| `style` | `rest` | ● | API style. |
| `resource` | string | ● | Path template, e.g. /permits/{id}/status. |
| `operations` | `[get \| post \| put \| delete]` (min 1) | ● | HTTP operations exposed. |
| `auth` | `api_builder \| none` (default api_builder) |  | Authentication scheme. |
| `exposes` | `{entity, attrs[]}` |  | The entity and exact attributes exposed — nothing leaves the boundary undeclared. |

#### 20.2  outbound[]

| Field | Type / allowed values | Req. | Meaning |
|---|---|---|---|
| `id` | snakeId | ● | Adapter use id. |
| `component` | kebabId | ● | The catalog adapter component (L007). |
| `config` | object |  | Contract-validated component configuration. |
| `used_by` | array of string |  | Informative back-references, e.g. form:frmX.field:y. |

| Standing rule — Secrets are never literal. Any secret-bearing configuration value must be an `${env:NAME}` reference (L013) — a model document is always safe to commit, copy and send for review. |
|---|

| `interfaces:`<br>`inbound:`<br>`- id: api_permit_status`<br>`style: rest`<br>`resource: "/permits/{applicationNo}/status"`<br>`operations: [get]`<br>`auth: api_builder`<br>`exposes: { entity: permit_application, attrs: [application_no, status, decided_at] }`<br>`outbound:`<br>`- id: identity_check`<br>`component: identity-adapter`<br>`config:`<br>`endpoint: "${env:IDENTITY_BB_URL}"`<br>`api_key: "${env:IDENTITY_BB_KEY}"`<br>`lookup_key: national_id`<br>`used_by: ["form:frmPermitApply.field:applicant_name"]` |
|---|

*Facility Permit — one API exposed, one identity lookup consumed.*

## 21.  Seed data

Seed declares the master-data rows for `md_lookup` and `config` entities (vocabularies seed through their own `rows`/`file`). Loads are ordered (`order`, default 100) and executed cache-coherently, so a fresh instance comes up with its reference data complete and consistent.

| Field | Type / allowed values | Req. | Meaning |
|---|---|---|---|
| `entity` | snakeId | ● | The seeded entity. |
| `order` | integer (default 100) |  | Load order across seed sets. |
| `rows` | array of object | ◐ | Inline rows (attribute id → value); either rows or file. |
| `file` | string | ◐ | CSV alternative. |

| `seed:`<br>`- entity: permit_fee`<br>`order: 10`<br>`rows:`<br>`- { facility_type: clinic,   fee_amount: 150.00 }`<br>`- { facility_type: pharmacy, fee_amount: 100.00 }`<br>`- { facility_type: lab,      fee_amount: 200.00 }` |
|---|

*Facility Permit — the fee configuration.*

## 22.  Acceptance — scenarios in the model

Acceptance criteria live in the model, in the same given/when/then language the business signed off — and are emitted into the platform’s regression harness as cold-start, order-independent test suites. A scenario is not prose: its fixtures, actions and assertions reference declared entities, states, transitions, forms and processes, and lint (L014) refuses a scenario that references anything the model does not define.

#### 22.1  fixtures[]

| Field | Type / allowed values | Req. | Meaning |
|---|---|---|---|
| `id` | snakeId | ● | Fixture id. |
| `seed` | boolean (default true) |  | Load all vocabularies and seed sets first. |
| `records[]` | `{entity, alias, values, state}` |  | Prepared records: the entity, a scenario-local alias, attribute values, and the lifecycle state the record starts in. |

#### 22.2  scenarios[]

| Field | Type / allowed values | Req. | Meaning |
|---|---|---|---|
| `id` | freeId | ● | Scenario id. |
| `name` | string |  | What the scenario proves. |
| `feature` | freeId |  | Feature tag — links the scenario into TRACE. |
| `given` | `{fixture, actor}` | ● | Starting fixture and the acting role (role:<id>). |
| `when[]` | array (min 1) | ● | Actions: `submit_form \| save_draft \| execute_transition \| complete_activity \| call_api \| run_component \| custom`, each naming its target (form, transition, entity, the fixture alias via `on`) and values. |
| `then[]` | array (min 1) | ● | Assertions: `entity_state \| record_count \| field_value \| validation_error \| api_response \| custom_sql`, with the companion fields each needs (state, attr, equals, where, sql). |

| `acceptance:`<br>`scenarios:`<br>`- id: t03_reject_requires_reason`<br>`name: Rejection without a reason is blocked`<br>`feature: F02`<br>`given: { fixture: fx_submitted, actor: "role:officer" }`<br>`when:`<br>`- { action: execute_transition, entity: permit_application, "on": app1, transition: start_review }`<br>`- { action: complete_activity, process: permit_review, activity: review, "on": app1,`<br>`outcome: reject, values: { rejection_reason: "" } }`<br>`then:`<br>`- { assert: validation_error, form: frmPermitReview, message_contains: "Rejection reason" }`<br>`- { assert: entity_state, entity: permit_application, "on": app1, state: under_review }` |
|---|

*Facility Permit — the guard scenario for FR-004.*

## 23.  The bespoke-plugin budget

Custom Java outside the catalog is allowed — and budgeted. Every entry must name the requirement that forces it and the reason no catalog component or model construct can express it. Growth in this section during specification is a signal, not a convenience: it returns the feature to architecture. The coverage metric — behaviour expressed in model + catalog versus entries here — is the platform’s honest measure of how declarative the delivery really is.

| Field | Type / allowed values | Req. | Meaning |
|---|---|---|---|
| `id` | kebabId | ● | Plugin id. |
| `type` | `ApplicationPlugin \| FormLoadBinder \| FormStoreBinder \| FormValidator \| FormOptionsBinder \| DataListBinder \| ProcessTool \| ParticipantMapper \| FormElement \| ApiPlugin \| Scheduler \| Other` | ● | Joget plugin type. |
| `justification` | `{requirement, reason}` | ● | The forcing requirement (must resolve — L016) and why it cannot be catalog/config. |
| `reads / writes` | arrays of snakeId |  | Entities touched (must resolve — L016). |
| `complexity` | `S \| M \| L` |  | Sizing. |
| `feature` | freeId |  | Feature tag. |

| `bespoke_plugins:`<br>`- id: nid-checksum-validator`<br>`type: FormValidator`<br>`justification:`<br>`requirement: FR-002`<br>`reason: "National-ID checksum is algorithmic validation not expressible in DefaultValidator or form-quality rules."`<br>`reads: [permit_application]`<br>`complexity: S`<br>`feature: F01` |
|---|

*Facility Permit — a one-entry budget.*

## 24.  Validation — what a model must pass

A model is validated at four levels before anything is generated from it; the toolchain (`kit validate`) exits 0 only when all four pass. The intent is to fail at authoring time, not on a deployed instance.

| Level | What it checks |
|---|---|
| 1 · Schema | Structure, types, patterns, enumerations, conditional requirements — this volume’s tables, enforced by JSON Schema 2020-12. |
| 2 · Cross-reference lint | The sixteen L-rules below: every reference in the document resolves, and structural integrity holds. |
| 3 · Platform deltas | D-rules — mechanised quirks of the declared DX version/edition (eleven live, each with a fixture pair proving it fires and passes correctly). Keyed on app.platform. |
| 4 · Config contracts | Every component config block validates against that component’s published contract (strict schemas where published; structural checks and key allow-lists at their honest ceiling elsewhere). |

### 24.1  The sixteen cross-reference rules

| Rule | Guards |
|---|---|
| `L001` | Unique ids within every collection. |
| `L002` | Every entity reference resolves (forms, lists, processes, parents, seeds, fixtures, interfaces). |
| `L003` | Every attribute reference binds to its entity (fields, columns, filters, status_attr, pk, effects, grid columns, exposed attrs). |
| `L004` | Vocabulary references and cascading parents resolve. |
| `L005` | Lifecycle integrity: exactly one initial state; transitions between declared states; terminal states have no exits. |
| `L006` | Every role reference (transitions, permissions, menus, actions, participants, escalations, scenario actors) is declared. |
| `L007` | Every component reference resolves to a versioned catalog entry; engine choices imply their component. |
| `L008` | Feature tags resolve; feature→requirement and dependency links hold. |
| `L009` | Navigation menu targets exist and match the menu type. |
| `L010` | Process integrity: participants declared; activity forms exist; outcomes map only to declared transitions; routing/deadlines reference real activities. |
| `L011` | Named-query references resolve; report params exist on their query. |
| `L012` | Physical table names unique across entities. |
| `L013` | Secret-bearing outbound config values are ${env:NAME} references, never literals. |
| `L014` | Acceptance integrity: fixtures resolve; aliases exist; transitions/states/activities/outcomes referenced by scenarios are real. |
| `L015` | Grid child form exists and is bound to the child entity. |
| `L016` | Bespoke-plugin justifications cite real requirements; reads/writes reference real entities. |

Beyond these, a U-series of user-experience rules (from the embedded Enterprise UX Standard) lints screen constructs against the UX ruleset, and the validator’s exit codes are scripted into CI: 0 valid · 1 schema failure · 2 lint failure.

## 25.  Versioning, provenance and drift

Three version numbers govern a model’s life. `schema_version` moves when the schema changes and is const-pinned in every document. `spec_version` moves on every model edit and is written — with a content fingerprint (sha256) and tool versions — into the provenance stamp of every generated file. The kit release the project pins moves on any shipped change to schema, validator, projectors or rules; upgrades are deliberate acts.

Provenance makes the standing rule enforceable: because every generated artefact says which model produced it, drift detection can mechanically compare the model, the build outputs and what a server actually runs. The four verdicts — clean · stale generated · hand-edited deployed · unprovenanced — turn “never hand-edit” from a discipline into a measurement. For the customer this means: the documented state of the system and its real state can always be reconciled, on demand, by tooling.

## Appendix A.  The complete reference model — Facility Permit

The full, machine-validated model of the reference application, exactly as maintained in the platform repository (`examples/facility-permit.app.yaml`, 500 lines). It exercises every top-level section of this specification and regenerates and regresses green in the platform’s CI. It is reproduced in full so this volume is self-contained in review.

| `# =============================================================================`<br>`# Worked example — Facility Permit application`<br>`# Sector-neutral instance of the Joget Application Model (schema 0.1.6).`<br>`# Exercises every top-level section once; deliberately small.`<br>`# Archetype: register -> review -> approve -> issue.`<br>`# =============================================================================`<br>`model:`<br>`schema_version: "0.1.6"`<br>`spec_version: "0.1.6"`<br>`status: draft`<br>`authors: ["FiscalAdmin OU"]`<br>`app:`<br>`id: facilityPermit`<br>`name: Facility Permit`<br>`description: Online application, back-office review, and issuance of facility operating permits.`<br>`platform:`<br>`dx: "9.0"          # x-decision: DX 8.x vs 9.0 pending platform reconciliation`<br>`edition: enterprise`<br>`db: postgres`<br>`conventions:`<br>`form_name_prefix: numbered   # "01.01 - ..." style applied by the projector`<br>`# ---------------------------------------------------------------- traceability`<br>`requirements:`<br>`- { id: FR-001, text: "An applicant can submit a facility permit application online.", source: "ModuleSpec §2.1" }`<br>`- { id: FR-002, text: "The national ID is checksum-validated and identity data is prefilled from the identity provider.", source: "ModuleSpec §2.2" }`<br>`- { id: FR-003, text: "An officer reviews the application with recorded inspections and approves or rejects it.", source: "ModuleSpec §2.3" }`<br>`- { id: FR-004, text: "A rejection must carry a rejection reason.", source: "ModuleSpec §2.3" }`<br>`- { id: FR-005, text: "Application status is queryable by application number via API.", source: "ModuleSpec §2.5" }`<br>`- { id: FR-006, text: "Management sees the review pipeline on a dashboard.", source: "ModuleSpec §2.6" }`<br>`features:`<br>`- { id: F01, name: "Application intake",  requirements: [FR-001, FR-002, FR-005] }`<br>`- { id: F02, name: "Review and decision", requirements: [FR-003, FR-004, FR-006], depends_on: [F01] }`<br>`# ----------------------------------------------------------------------- roles`<br>`roles:`<br>`- { id: applicant,  name: Applicant }`<br>`- { id: officer,    name: Permit Officer }`<br>`- { id: supervisor, name: Supervisor }`<br>`# ---------------------------------------------------------------- vocabularies`<br>`vocabularies:`<br>`- id: facility_type`<br>`name: Facility Type`<br>`rows:`<br>`- { code: clinic,   name: "Health clinic" }`<br>`- { code: pharmacy, name: "Pharmacy" }`<br>`- { code: lab,      name: "Laboratory" }`<br>`- id: district`<br>`name: District`<br>`rows:`<br>`- { code: north,   name: "Northern District" }`<br>`- { code: central, name: "Central District" }`<br>`- { code: south,   name: "Southern District" }`<br>`- id: rejection_reason`<br>`name: Rejection Reason`<br>`rows:`<br>`- { code: incomplete, name: "Incomplete documentation" }`<br>`- { code: failed_insp, name: "Failed inspection" }`<br>`- { code: ineligible,  name: "Applicant not eligible" }`<br>`- id: inspection_result`<br>`name: Inspection Result`<br>`rows:`<br>`- { code: pass, name: "Pass" }`<br>`- { code: fail, name: "Fail" }`<br>`# --------------------------------------------------------------------- catalog`<br>`catalog:`<br>`- { component: status-framework, version: "2.x", scope: global }`<br>`- { component: approval-service, version: "1.x" }`<br>`- { component: form-prefill,     version: "1.x" }`<br>`- { component: identity-adapter, version: "0.x" }`<br>`# --------------------------------------------------------------------- queries`<br>`queries:`<br>`- id: q_pending_count`<br>`description: Applications awaiting action.`<br>`sql: >-`<br>`SELECT COUNT(\*) FROM app_fd_permit_application`<br>`WHERE c_status IN ('submitted','under_review')`<br>`- id: q_apps_by_status`<br>`description: Pipeline distribution for the dashboard chart.`<br>`sql: >-`<br>`SELECT c_status AS status, COUNT(\*) AS n`<br>`FROM app_fd_permit_application GROUP BY c_status`<br>`- id: q_certificate`<br>`description: Certificate datasource for the Jasper report.`<br>`sql: >-`<br>`SELECT c_application_no, c_applicant_name, c_facility_type, c_district, c_decided_at`<br>`FROM app_fd_permit_application WHERE c_application_no = $P{application_no}`<br>`params:`<br>`- { id: application_no, type: string }`<br>`# -------------------------------------------------------------------- entities`<br>`entities:`<br>`- id: permit_application`<br>`name: Permit Application`<br>`kind: main`<br>`table: permit_application`<br>`feature: F01`<br>`canonical_ref:`<br>`model: GovStack-RegBB`<br>`path: registration.application`<br>`divergences:`<br>`- { what: "issued state added beyond RegBB approve/reject", reason: "permit issuance is a distinct legal act" }`<br>`pk: { strategy: id_generator, format: "PA-??????", attr: application_no }`<br>`audit: status`<br>`attributes:`<br>`- { id: application_no, type: string, unique: true, length: 12, description: "Business key, generated." }`<br>`- { id: applicant_name, type: string, required: true, length: 120 }`<br>`- { id: national_id,    type: string, required: true, pattern: "^[0-9]{11}$" }`<br>`- { id: email,          type: string, required: true, length: 120 }`<br>`- { id: facility_type,  type: enum, vocabulary: facility_type, required: true }`<br>`- { id: district,       type: enum, vocabulary: district, required: true }`<br>`- { id: address,        type: text }`<br>`- { id: status,         type: string, length: 20, description: "Lifecycle status attr." }`<br>`- { id: submitted_at,   type: datetime }`<br>`- { id: rejection_reason, type: enum, vocabulary: rejection_reason }`<br>`- { id: decided_at,     type: datetime }`<br>`lifecycle:`<br>`status_attr: status`<br>`engine: status_framework`<br>`states:`<br>`- { id: draft,        name: Draft, initial: true, tone: grey }`<br>`- { id: submitted,    name: Submitted, tone: amber }`<br>`- { id: under_review, name: Under review, tone: blue }`<br>`- { id: approved,     name: Approved, tone: green }`<br>`- { id: rejected,     name: Rejected, terminal: true, tone: red }`<br>`- { id: issued,       name: Issued, terminal: true, tone: green }`<br>`transitions:`<br>`- id: submit`<br>`from: draft`<br>`to: submitted`<br>`trigger: user`<br>`roles: [applicant]`<br>`effects:`<br>`- { type: audit }`<br>`- { type: set_attr, attr: submitted_at, value: "${now}" }`<br>`- id: start_review`<br>`from: submitted`<br>`to: under_review`<br>`trigger: user`<br>`roles: [officer]`<br>`effects: [ { type: audit } ]`<br>`- id: approve`<br>`from: under_review`<br>`to: approved`<br>`trigger: user`<br>`roles: [officer]`<br>`guard: "no inspection with result = fail"`<br>`effects:`<br>`- { type: audit }`<br>`- { type: set_attr, attr: decided_at, value: "${now}" }`<br>`- { type: notify, template: permit_decision, to: "attr:email" }`<br>`- id: reject`<br>`from: under_review`<br>`to: rejected`<br>`trigger: user`<br>`roles: [officer]`<br>`guard: "rejection_reason is present"`<br>`effects:`<br>`- { type: audit }`<br>`- { type: set_attr, attr: decided_at, value: "${now}" }`<br>`- { type: notify, template: permit_decision, to: "attr:email" }`<br>`- id: issue`<br>`from: approved`<br>`to: issued`<br>`trigger: user`<br>`roles: [officer]`<br>`effects:`<br>`- { type: audit }`<br>`- { type: notify, template: permit_issued, to: "attr:email" }`<br>`- id: inspection`<br>`name: Inspection`<br>`kind: child`<br>`table: permit_inspection`<br>`feature: F02`<br>`parent: { entity: permit_application, fk_attr: application_id }`<br>`attributes:`<br>`- { id: application_id, type: ref, ref: { entity: permit_application, display: application_no } }`<br>`- { id: inspected_at,   type: date, required: true }`<br>`- { id: result,         type: enum, vocabulary: inspection_result, required: true }`<br>`- { id: notes,          type: text }`<br>`- id: permit_fee`<br>`name: Permit Fee Configuration`<br>`kind: config`<br>`table: permit_fee_config`<br>`feature: F01`<br>`attributes:`<br>`- { id: facility_type, type: enum, vocabulary: facility_type, required: true }`<br>`- { id: fee_amount,    type: decimal, precision: 10, scale: 2, required: true }`<br>`# ------------------------------------------------------------------- processes`<br>`processes:`<br>`- id: permit_review`<br>`name: Permit Review`<br>`feature: F02`<br>`entity: permit_application`<br>`realization: approval_service`<br>`participants:`<br>`- { id: reviewer,   map: "role:officer" }`<br>`- { id: escalation, map: "role:supervisor" }`<br>`activities:`<br>`- id: review`<br>`kind: human`<br>`participant: reviewer`<br>`form: frmPermitReview`<br>`outcomes:`<br>`- { id: approve, label: Approve, transition: approve }`<br>`- { id: reject,  label: Reject,  transition: reject }`<br>`deadlines:`<br>`- { "on": review, after: P3D, escalate_to: "role:supervisor" }`<br>`approval:`<br>`mode: single`<br>`sod: { initiator_cannot_review: true }`<br>`# ----------------------------------------------------------------------- forms`<br>`forms:`<br>`- id: frmPermitApply`<br>`name: Permit Application`<br>`entity: permit_application`<br>`purpose: create`<br>`feature: F01`<br>`# Form-level prefill (D-10 PASSTHROUGH), realized by the form-prefill component:`<br>`# returning-applicant autofill — on entry of a national_id, name/email are prefilled`<br>`# from that applicant's most recent prior application. Body is the form-prefill`<br>`# config vocabulary; the forms projector copies it verbatim into loadBinder:prefill.`<br>`# (FR-002 identity-provider validation itself is the identity-adapter's job —`<br>`# interfaces.outbound.identity_check + the nid-checksum-validator bespoke plugin.)`<br>`prefill:`<br>`component: form-prefill`<br>`keySources:`<br>`- { source: currentField, name: national_id }`<br>`formId: frmPermitApply`<br>`matchField: national_id`<br>`orderBy: submitted_at`<br>`mappings:`<br>`- { from: applicant_name, to: applicant_name }`<br>`- { from: email,          to: email }`<br>`sections:`<br>`- id: sec_applicant`<br>`label: Applicant`<br>`columns: 2`<br>`fields:`<br>`- { attr: application_no, control: id_generator, readonly: true }`<br>`- { attr: national_id }`<br>`- { attr: applicant_name }`<br>`- { attr: email }`<br>`- id: sec_facility`<br>`label: Facility`<br>`columns: 2`<br>`fields:`<br>`- { attr: facility_type }`<br>`- { attr: district }`<br>`- { attr: address, control: textarea }`<br>`permissions: { roles: [applicant] }`<br>`- id: frmPermitReview`<br>`name: Permit Review`<br>`entity: permit_application`<br>`purpose: review`<br>`feature: F02`<br>`sections:`<br>`- id: sec_summary`<br>`label: Application`<br>`columns: 2`<br>`readonly: true`<br>`fields:`<br>`- { attr: application_no }`<br>`- { attr: applicant_name }`<br>`- { attr: facility_type }`<br>`- { attr: district }`<br>`- id: sec_inspections`<br>`label: Inspections`<br>`columns: 1`<br>`fields:`<br>`- id: inspections`<br>`control: grid`<br>`label: Inspections`<br>`child:`<br>`entity: inspection`<br>`form: frmInspectionRow`<br>`columns: [inspected_at, result]`<br>`- id: sec_decision`<br>`label: Decision`<br>`columns: 1`<br>`fields:`<br>`- { attr: rejection_reason, label: "Rejection reason (required when rejecting)" }`<br>`validation:`<br>`- rule: "outcome == reject implies rejection_reason is not empty"`<br>`message: "Rejection reason is mandatory when rejecting."`<br>`realization: validator_plugin`<br>`permissions: { roles: [officer] }`<br>`- id: frmInspectionRow`<br>`name: Inspection`<br>`entity: inspection`<br>`purpose: edit`<br>`feature: F02`<br>`sections:`<br>`- id: sec_row`<br>`label: Inspection`<br>`columns: 2`<br>`fields:`<br>`- { attr: inspected_at }`<br>`- { attr: result }`<br>`- { attr: notes, control: textarea }`<br>`permissions: { roles: [officer] }`<br>`# ----------------------------------------------------------------------- lists`<br>`lists:`<br>`- id: dlPermitRegister`<br>`name: Permit Register`<br>`feature: F02`<br>`# 2 forms bound to permit_application -> source.form disambiguates the binder table (E-probe F-1)`<br>`source: { entity: permit_application, form: frmPermitApply }`<br>`columns:`<br>`- { attr: application_no, label: "No." }`<br>`- { attr: applicant_name, label: Applicant }`<br>`- { attr: facility_type,  label: Type }`<br>`- { attr: district,       label: District }`<br>`- { attr: status,         label: Status, format: status_badge }`<br>`- { attr: submitted_at,   label: Submitted, format: datetime }`<br>`filters:`<br>`# both select filters auto-derive their options: facility_type from its vocabulary,`<br>`# status from the entity's lifecycle states (E-probe backlog #4, now realized).`<br>`- { attr: facility_type, type: select }`<br>`- { attr: status,        type: select }`<br>`- { attr: submitted_at,  type: date_range, label: "Submitted between" }   # E-probe #5`<br>`sort: { by: submitted_at, dir: desc }`<br>`permissions: { roles: [officer, supervisor] }`<br>`# NOTE (E-probe backlog): a \`link\` column format is the last unrealized list construct — a`<br>`# hyperlink is available today via a row action (\`actions: [{type: link, href}]\`); tracked in`<br>`# docs/E-PROBE-FINDINGS.md (#3).`<br>`- id: dlMyApplications`<br>`name: My Applications`<br>`feature: F01`<br>`source: { entity: permit_application, form: frmPermitApply }`<br>`x-row-scope: current_user            # projector concern: scope rows to creator`<br>`columns:`<br>`- { attr: application_no, label: "No." }`<br>`- { attr: status,         label: Status }`<br>`- { attr: submitted_at,   label: Submitted, format: datetime }`<br>`permissions: { roles: [applicant] }`<br>`# ------------------------------------------------------------------ navigation`<br>`navigation:`<br>`userview_id: uvPermit`<br>`name: Facility Permits`<br>`categories:`<br>`- id: cat_apply`<br>`label: Apply`<br>`roles: [applicant]`<br>`menus:`<br>`- { type: form, label: "New permit application", form: frmPermitApply }`<br>`# crud gives the applicant row View/Edit of their own applications (list + add + edit + view)`<br>`- { type: crud, label: "My applications", entity: permit_application, form: frmPermitApply, list: dlMyApplications, delete: false }`<br>`- id: cat_office`<br>`label: Back office`<br>`roles: [officer, supervisor]`<br>`menus:`<br>`# crud lets an officer open each application to review it (row View/Edit on the register)`<br>`- { type: crud, label: "Permit register", entity: permit_application, form: frmPermitReview, list: dlPermitRegister, delete: false }`<br>`- { type: inbox,     label: "My tasks" }`<br>`- { type: dashboard, label: "Review pipeline", dashboard: dash_office }`<br>`- { type: report,    label: "Permit certificate", report: rpt_certificate }`<br>`# ------------------------------------------------------------------ dashboards`<br>`dashboards:`<br>`- id: dash_office`<br>`name: Review Pipeline`<br>`feature: F02`<br>`tiles:`<br>`# NOTE (E-probe backlog): a kpi/RAG card (kind: kpi, thresholds) is a separate CustomHTML`<br>`# surface not yet realized (DB-02); only chart tiles project. See docs/E-PROBE-FINDINGS.md.`<br>`- kind: chart`<br>`chart_type: bar`<br>`label: Applications by status`<br>`query: q_apps_by_status`<br>`key: status`<br>`value: n`<br>`# --------------------------------------------------------------------- reports`<br>`reports:`<br>`- id: rpt_certificate`<br>`name: Permit Certificate`<br>`engine: jasper`<br>`feature: F02`<br>`query: q_certificate`<br>`params: [application_no]`<br>`output: [pdf]`<br>`# ------------------------------------------------------------------ interfaces`<br>`interfaces:`<br>`inbound:`<br>`- id: api_permit_status`<br>`style: rest`<br>`resource: "/permits/{applicationNo}/status"`<br>`operations: [get]`<br>`auth: api_builder`<br>`exposes:`<br>`entity: permit_application`<br>`attrs: [application_no, status, decided_at]`<br>`feature: F01`<br>`outbound:`<br>`- id: identity_check`<br>`component: identity-adapter`<br>`config:`<br>`endpoint: "${env:IDENTITY_BB_URL}"`<br>`api_key: "${env:IDENTITY_BB_KEY}"`<br>`lookup_key: national_id`<br>`used_by: ["form:frmPermitApply.field:applicant_name"]`<br>`feature: F01`<br>`# ------------------------------------------------------------------------ seed`<br>`seed:`<br>`- entity: permit_fee`<br>`order: 10`<br>`rows:`<br>`- { facility_type: clinic,   fee_amount: 150.00 }`<br>`- { facility_type: pharmacy, fee_amount: 100.00 }`<br>`- { facility_type: lab,      fee_amount: 200.00 }`<br>`# ------------------------------------------------------------------ acceptance`<br>`acceptance:`<br>`fixtures:`<br>`- id: fx_base`<br>`seed: true`<br>`records:`<br>`- entity: permit_application`<br>`alias: app1`<br>`state: draft`<br>`values:`<br>`applicant_name: "Test Applicant"`<br>`national_id: "38001010001"`<br>`email: "applicant@example.org"`<br>`facility_type: clinic`<br>`district: north`<br>`- id: fx_submitted`<br>`seed: true`<br>`records:`<br>`- entity: permit_application`<br>`alias: app1`<br>`state: submitted`<br>`values:`<br>`applicant_name: "Test Applicant"`<br>`national_id: "38001010001"`<br>`email: "applicant@example.org"`<br>`facility_type: clinic`<br>`district: north`<br>`scenarios:`<br>`- id: t01_submit_application`<br>`name: Applicant submits a draft application`<br>`feature: F01`<br>`given: { fixture: fx_base, actor: "role:applicant" }`<br>`when:`<br>`- { action: execute_transition, entity: permit_application, "on": app1, transition: submit }`<br>`then:`<br>`- { assert: entity_state, entity: permit_application, "on": app1, state: submitted }`<br>`- assert: custom_sql`<br>`sql: "SELECT COUNT(\*) FROM app_fd_permit_application WHERE c_submitted_at IS NOT NULL AND c_national_id = '38001010001'"`<br>`equals: 1`<br>`- id: t02_approve_path`<br>`name: Officer reviews and approves`<br>`feature: F02`<br>`given: { fixture: fx_submitted, actor: "role:officer" }`<br>`when:`<br>`- { action: execute_transition, entity: permit_application, "on": app1, transition: start_review }`<br>`- { action: complete_activity, process: permit_review, activity: review, "on": app1, outcome: approve }`<br>`then:`<br>`- { assert: entity_state, entity: permit_application, "on": app1, state: approved }`<br>`- id: t03_reject_requires_reason`<br>`name: Rejection without a reason is blocked`<br>`feature: F02`<br>`given: { fixture: fx_submitted, actor: "role:officer" }`<br>`when:`<br>`- { action: execute_transition, entity: permit_application, "on": app1, transition: start_review }`<br>`- { action: complete_activity, process: permit_review, activity: review, "on": app1, outcome: reject, values: { rejection_reason: "" } }`<br>`then:`<br>`- { assert: validation_error, form: frmPermitReview, message_contains: "Rejection reason" }`<br>`- { assert: entity_state, entity: permit_application, "on": app1, state: under_review }`<br>`# ------------------------------------------------------------- plugin budget`<br>`bespoke_plugins:`<br>`- id: nid-checksum-validator`<br>`type: FormValidator`<br>`justification:`<br>`requirement: FR-002`<br>`reason: "National-ID checksum is algorithmic validation not expressible in DefaultValidator or form-quality rules."`<br>`reads: [permit_application]`<br>`complexity: S`<br>`feature: F01` |
|---|

*facility-permit.app.yaml — complete listing (schema 0.1.6).*

## Appendix B.  Glossary

| Term | Meaning |
|---|---|
| Application model | The one structured YAML document that fully describes an application — data, statuses, screens, rules, tests. The only artefact a human edits. |
| Projector / generator | A projector derives from the model the exact slice a proven generator needs; the generator turns it into a deployable Joget artefact. Neither is ever hand-edited. |
| Direct emitter | A projector-like converter that writes its output straight from the model (lifecycle config, seeds, API definitions, test suites, TRACE). |
| Catalog component | A reusable, versioned runtime part (lifecycle engine, approval service, form prefill…) switched on through configuration rather than code. |
| Config contract | The machine-checkable statement (JSON Schema) of exactly which settings a catalog component accepts. |
| Lifecycle | The declared state machine of a long-lived record: states, transitions, authority, guards, effects — enforced at runtime by the lifecycle engine. |
| Vocabulary | A governed simple code list (code/label, optionally cascading) with its seed rows. |
| Provenance stamp | The header in every generated file naming the model version, schema version, tool version and content fingerprint that produced it. |
| Drift | Any disagreement between the model, the generated files, and what a server runs — detected mechanically from provenance stamps. |
| L-rules / D-rules | The cross-reference lint rules (L001–L016) and the platform-delta rules (mechanised version-specific quirks) applied at validation. |
| TRACE | The generated traceability matrix: requirement → feature → realising objects → proving tests → produced artefacts. |
| Bespoke-plugin budget | The governed list of custom Java outside the catalog, each entry justified by a named requirement. |
| Seed data | Master-data rows loaded into a fresh instance in a defined, cache-coherent order. |
| Given / when / then | The standard phrasing of behaviour tests: a starting situation, an action, an outcome that must hold. |
