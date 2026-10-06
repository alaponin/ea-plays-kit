# Getting started with the spec kit

A practical, standing guide: what the kit is, how the pieces fit, and how to drive it from
an empty folder to validated, generated, evidence-backed Joget artefacts.

> **One sentence.** You author an application **once** as a single validated model; the kit
> deterministically projects that one source into the input specs for every Joget artefact
> type (forms, datalists, userview, dashboards, workflow) plus integration contracts, tests,
> traceability and coverage — and nothing downstream is ever hand-maintained in parallel.

---

## 1. Mental model

```
  YOU WRITE ONE FILE                    THE KIT                         THE PLATFORM
 ┌───────────────────┐   validate   ┌───────────────────┐   run the   ┌──────────────┐
 │  <app>.app.yaml   │ ───────────▶ │  four-layer check │             │   shipped    │
 │  (Layer 1 model)  │              │  schema · lint ·  │             │  generators  │
 │  entities, forms, │   project    │  delta · contract │   feed L2   │  (gen_forms, │   deploy   ┌────────┐
 │  lists, nav,      │ ───────────▶ │  projectors →     │ ──────────▶ │  gen_*, …)   │ ─────────▶ │ Joget  │
 │  dashboards,      │              │  Layer-2 specs    │   specs     │  → JSON/XPDL │            │instance│
 │  processes, …     │   emit       │  emitters →       │             └──────────────┘            └────────┘
 └───────────────────┘ ───────────▶ │  trace/suite/     │
                                     │  regbb/coverage   │
                                     └───────────────────┘
```

**Before the model: the interaction design.** Since METHOD-2026-09-25-12 (ADR-105) the model is
written from the interaction design its owner accepted (SDD-11; slot `08a` of the method), and it
names that document in its required entry `model.interaction_design`, by its path relative to the
model and its SHA-256 checksum. The kit reads the document and refuses, at every step from
`kit validate` to the deploy, a model that names none or disagrees with it (rule L021; section 6).

Two layers matter:

- **Layer 1** — the model *you* write (`<app>.app.yaml`). The single source of truth.
- **Layer 2** — the generator-input specs the kit **projects** from Layer 1 (one per artefact
  type). These are consumed by the *shipped Joget generators* to produce the actual JSON/XPDL.

The kit owns **Layer 1 → Layer 2** (validated, deterministic, provenance-stamped) and *proves*
that projection matches the real generators by round-trip. It does **not** re-implement the
generators or the deploy — those are the shipped engines it orchestrates.

---

## 2. Prerequisites

- **Python 3.10+** with `pyyaml` and `jsonschema`:
  ```bash
  pip install --user pyyaml jsonschema        # add pytest to run the test suite
  ```
- The kit is invoked as `python3 tools/kit.py <verb> …`. A convenience alias helps:
  ```bash
  alias kit='python3 <the path of sdd-kit>/kit/tools/kit.py'
  ```
- Optional environment wiring (only needed for the steps that touch external engines):

  | Env var | Points to | Used by |
  |---|---|---|
  | `GEN_SCRIPTS_DIR` | the delivery scripts dir (`gen_datalists.py`, `gen_workflow.py`) | turning Layer-2 specs into JSON; datalists/workflow round-trip tests |
  | `NEUTRAL_GEN_DIR` | project-neutral reference generators (default: sibling `joget-platform-plugins/reference-app/generators/`) | the forms round-trip's JSON leg (the plugin library's `gen_forms.py`, which `build_app.py` builds with and the golden JSON was made with, since 24 September 2026); userview/dashboards generation + round-trip tests |
  | `JOGET_INSTANCES` | `instances.yaml` (default `~/.joget/instances.yaml`) | `kit match` / `kit deploy` |
  | `KIT_DEPLOY_CMD` / `KIT_SEED_CMD` / `KIT_TEST_CMD` | the delivery deploy/seed/test commands | `kit deploy` / `seed` / `test` |
  | `JOGET_PLUGINS_REGISTRY` | canonical `registry.yaml` (default: sibling plugin lib) | contract-mirror integrity test |

  If an env var is unset, the affected step **skips gracefully** or tells you what to set — the
  in-kit verbs (`validate`, `gen`, `trace`, `suite`, `coverage`, `diff`, `drift`, `checklist`,
  `regbb`, `new`) need none of it.

---

## 3. Five-minute quickstart

```bash
# 1. Scaffold a minimal model; its interaction design is written as a question to answer
kit new demoApp --out demoApp.app.yaml
kit validate demoApp.app.yaml
#    INTERACTION DESIGN: refused — … check 1 — the entry model.interaction_design is still the
#    question `kit new` wrote, and it is not answered …

# 2. Write the interaction design from templates/spec/INTERACTION_DESIGN.md.tmpl, have the owner
#    accept it (its header reads "baselined · accepted by <name> on <date>"), and name it:
#      model:
#        interaction_design: {path: demoApp.interaction-design.md,
#                             sha256: <shasum -a 256 demoApp.interaction-design.md>}
kit validate demoApp.app.yaml
#    INTERACTION DESIGN: admitted — … / SCHEMA: ok / LINT: ok / DELTA: ok / CONTRACT: ok / MODEL: …

# 3. Project every artefact type into Layer-2 specs
kit gen all demoApp.app.yaml --out build/
#    writes build/<feature>/forms/F-*.spec.yml, …/datalists/DL-*.spec.yml,
#    build/<userviewId>.uv.yml, etc. — each provenance-stamped.

# 4. See the evidence
kit trace    demoApp.app.yaml     # requirements → artefacts → acceptance coverage matrix
kit coverage demoApp.app.yaml     # % declarative vs bespoke-Java budget
```

That's the whole authoring loop: **design → write → validate → gen → inspect**. Everything else is
either turning those Layer-2 specs into JSON (the shipped generators) or evidence/deploy tooling.

---

## 4. The Layer-1 model

One YAML document per application, validated against `application-model.schema.yaml`
(schema `0.1.6`). The worked, sector-neutral reference is `examples/facility-permit.app.yaml`
— read it end to end; it exercises every section once. The top-level sections:

| Section | What it holds | Projected/consumed by |
|---|---|---|
| `model` | doc metadata (`schema_version`, `spec_version`) and, required, `interaction_design`: the accepted interaction design, by `path` and `sha256` | rule L021, first, in `kit validate`, `kit gen`, the build and the deploy |
| `app` | id, name, **`platform`** (`dx` / `edition` / `db`) | delta rules key on `platform` |
| `requirements`, `features` | FR register + feature tags | `kit trace`, coverage |
| `roles` | who does what | forms/lists/nav permissions |
| `vocabularies` | simple code lists | forms (static options), seed |
| `catalog` | reusable platform components (versioned) | contract validation |
| `entities` (+ `attributes`, `lifecycle`, `pk`, `parent`) | the domain model | forms, datalists, workflow, regbb |
| `forms` | logical forms (sections + fields, `prefill`) | forms projector |
| `lists` | datalists (entity- or query-sourced) | datalists projector |
| `navigation` | userview categories → menus | userview projector |
| `dashboards` | KPI/chart tiles over `queries` | dashboards projector |
| `processes` | participants, activities, routing (`realization: xpdl` / `approval_service`) | workflow projector |
| `queries` | named SQL | datalists, dashboards, reports |
| `interfaces` | inbound APIs, outbound adapters (incl. `regbb` channel) | regbb emitter |
| `seed`, `acceptance` | seed rows + given/when/then scenarios | seed loader, `kit suite` |
| `bespoke_plugins` | the Java escape-hatch **budget** (FR-justified) | `kit coverage` |

The rule of thumb: if a behaviour can be *declared*, it belongs in a structured section; if it
truly needs custom Java, it goes in `bespoke_plugins` with a requirement justification, so the
escape hatch stays visible and countable (that's what `kit coverage` measures).

---

## 5. Command reference

Run any verb with `--help` for its flags. Exit codes are meaningful (0 ok · non-zero =
errors/drift), so every verb composes into CI.

### Author & check
| Command | Does |
|---|---|
| `kit new <appId> [--out F]` | scaffold a minimal model valid through all four layers, whose `model.interaction_design` is a question to answer: refused by L021 until it names an accepted interaction design |
| `kit validate <app>` | **interaction design (L021) → schema → lint (L-rules) → delta (D-rules, platform-keyed) → contract** |
| `kit diff <old> <new>` | structural id-level diff of two model versions (exit 1 on drift) |

### Generate (Layer-1 → Layer-2 specs)
| Command | Does |
|---|---|
| `kit gen forms\|datalists\|userview\|dashboards\|workflow\|all <app> --out DIR` | run L021 first, writing nothing when it refuses; then project the model into each generator's input spec, provenance-stamped |
| `kit regbb <app> [--out F]` | emit the GovStack RegBB channel contract **pair** (`{serviceId}.yml` + `validation-rules.yaml`) |

`kit gen` stops at the Layer-2 spec. To produce actual Joget JSON, run the shipped generator on
those specs (e.g. `gen_forms.py build/F01/forms build/json`) — the kit guarantees, by round-trip
test, that this yields the right output.

### Evidence & coverage
| Command | Does |
|---|---|
| `kit trace <app> [--out F]` | requirement → feature → artefacts → acceptance matrix + gap list |
| `kit coverage <app> [--out F]` | declarative-vs-bespoke %, with the FR-justified bespoke budget |
| `kit suite <app> [--out F]` | compile `acceptance` into a regression-suite manifest (carries the cold-start/order-independent discipline) |
| `kit drift <app> <generated_dir>` | provenance readback: **IN_SYNC / STALE / HAND_EDITED / ORPHAN / MISSING** (exit 1 on drift) |
| `kit checklist <app> [--out F]` | platform-delta review checklist scoped to your platform (the non-mechanizable gotchas) |

### Deploy (gated)
| Command | Does |
|---|---|
| `kit match <app> --instance jdxN [--instances P]` | model `platform` (dx/db) vs the target instance in `instances.yaml` |
| `kit deploy <app> --instance jdxN` | run L021, then `match`; on success hand off to `$KIT_DEPLOY_CMD` |
| `kit seed <app>` / `kit test <app>` | run `$KIT_SEED_CMD` / `$KIT_TEST_CMD` (the delivery seed/regression engines) |

The build (`tools/build_app.py --model <app>`) and the deploy (`tools/deploy_dx9.py`, with
`--dry-run` to stop after the admission) run the same gate; the build takes only specs projected
from the admitted model and writes `<appId>.admission.yaml`, which the deploy requires
(`DEPLOY.md`, sections 0 to 2).

---

## 6. The four validation layers (why `kit validate` is the point)

`kit validate` fails a mistake **at authoring time** instead of at a broken deploy:

0. **The interaction design gate (L021)**, before the four layers — the model names the
   interaction design its owner accepted, the file is there with the checksum named, its header
   reads baselined with a name and a date, it covers every goal the model's forms and lists name
   in `use_case`, and the model's lists, references, moves and acts agree with its four decision
   tables (the nine checks: `DEPLOY.md` section 0). It prints `INTERACTION DESIGN: refused` or
   `admitted` first, and validation goes on so that every other finding shows too; the exit is not
   0 while it refuses. It is an error in every custody mode, and nothing turns it off.
1. **Schema** (JSON Schema 2020-12) — types, required fields, id patterns, hard platform caps
   (e.g. the 24-char form-id limit), co-requirements (enum⇒vocabulary, ref⇒entity, grid⇒child).
2. **Lint (L-rules)** — cross-references JSON Schema can't see: every entity/attribute/role/
   feature/query/component/menu target resolves; lifecycle integrity; process↔lifecycle mapping.
3. **Delta rules (D-series)** — platform "gotchas" that differ from the docs, **keyed on your
   `platform`** so one rule set serves DX8/DX9 and both editions. Blocking `error` vs advisory
   `warn`. e.g. Enterprise-only controls on `community`, Postgres camelCase folding, wizard
   partial-store. The full catalogue is `rules/JOGET-PLATFORM-DELTAS.md` (D-001..065).
4. **Contract** — each `config`/`prefill` block is validated against the catalog component's
   published contract (mirrored from `joget-platform-plugins/registry.yaml`). `form-prefill` gets
   a rich source-grounded schema; the rest are config-key allow-lists.

The gotchas that *can't* be a rule (judgement calls) surface via `kit checklist`.

---

## 7. Generation flow in detail

```
kit gen forms  ──▶ build/<feature>/forms/F-<id>.spec.yml   ──▶ gen_forms.py     ──▶ <form>.json
kit gen datalists ─▶ …/datalists/DL-<id>.spec.yml           ──▶ gen_datalists.py ─▶ <list>.json
kit gen userview ─▶ <userviewId>.uv.yml                     ──▶ gen_userview.py  ──▶ <uv>.json   (neutral gen)
kit gen dashboards ▶ <dashId>.dash.yml                      ──▶ gen_dashboards.py▶ SqlChartMenu  (neutral gen)
kit gen workflow ─▶ WF-<id>.spec.yml                        ──▶ gen_workflow.py  ──▶ package.xpdl + maps
kit regbb        ─▶ {serviceId}.yml + validation-rules.yaml (emitted directly; the channel contract)
```

- **datalists / workflow** round-trip against the *delivery* generators (`GEN_SCRIPTS_DIR`)
  — those are already project-neutral.
- **forms** round-trip against the plugin library's `gen_forms.py` — the generator `build_app.py`
  builds with and the golden JSON was made with — found like the reference generators below
  (`NEUTRAL_GEN_DIR`, else the sibling `joget-platform-plugins`). Until 24 September 2026 it was
  looked for in `GEN_SCRIPTS_DIR`, whose older `gen_forms.py` the golden does not match.
- **userview / dashboards** round-trip against **project-neutral reference generators** in
  `joget-platform-plugins/reference-app/generators/` (`NEUTRAL_GEN_DIR`) — the delivery ones bake
  in project policy, so the kit uses clean reference implementations to keep the proof independent
  (see `docs/adr/ADR-023`).

Every projected file carries a provenance header (`source_sha256`, `spec_version`, projector
version). That stamp is what `kit drift` reads back.

---

## 8. Conventions you must keep

- **Never hand-edit generated artefacts.** Change the model and regenerate. `kit drift` turns
  this into a checkable verdict — a hand edit shows as `HAND_EDITED` (distinct from a merely
  `STALE` file that just needs regenerating).
- **Every load-bearing decision is an ADR** in `docs/adr/` (ADR-001..026). Read these to
  understand *why* something is the way it is.
- **Every platform lesson is a delta-register entry.** Mechanizable ones become D-rules; the rest
  become checklist items. A validation rule without a register reference doesn't ship.
- **Bump `spec_version` on every model change** — it flows into generated-artefact provenance.

The full, consolidated working rules — source-first, git-on-the-Mac-via-Desktop-Commander,
the one build/deploy path, zero-domain-content, testbeds-keep-results-not-input, instance
hygiene — live in **`rules/session-conventions.md`**. Read it before working on the platform.
The upstream design method (evidence → procedure catalogue → use-case model → domain model →
realism gate → compile) is scaffolded in **`skills/`**.

---

## 9. What's proven vs. deferred

**Proven & tested** (round-tripped against real generators/oracles; the suite is green): the
four-layer validator, all **five projectors** (forms, datalists, userview, dashboards, workflow),
the RegBB emitter pair, the config-contract mirror over every registered component, and the whole
evidence surface (`trace`/`suite`/`coverage`/`drift`/`match`/`checklist`).

**Deferred depth** (breadth within a type, not missing capability — all logged in
`docs/PROJECTION-DECISIONS.md`): tool-activity/deadline/approval-service workflow steps, KPI &
DashboardMenu tiles, dashboard/report/inbox userview menus, entity-source datalist gating, and
getting the reference app's own richer nav/lists/dashboard/process into CI.

**Honest scope.** This is a validated, evidence-backed *front half* — a research/reference
platform — not a one-click "build my app" button. Actual JSON generation and deployment still run
the shipped Joget engines against your instance; the kit is what makes that reliable and auditable.

---

## 10. Running the tests / CI

```bash
python3 -m pytest tests/ -q                       # hermetic: full-round-trip legs skip gracefully
GEN_SCRIPTS_DIR=/path/to/delivery/scripts \
  python3 -m pytest tests/ -q                      # full: runs the generator round-trips too
```

CI (`.github/workflows/conformance.yml`) runs `kit validate` on the reference app + the whole
suite on every change to the schema, tools, tests, or examples. Legs that need an external
generator skip in hermetic CI; the projector-stability checks always run.

---

## 11. Troubleshooting

- **`kit gen dashboards` refuses a KPI tile / `kit gen workflow` refuses a tool activity** — by
  design (deferred constructs, `PROJECTION-DECISIONS.md`). Model only the realized constructs, or
  extend the generator + projector following the ADR-023/024 pattern.
- **A round-trip test skips** — the external generator/oracle isn't reachable; set `GEN_SCRIPTS_DIR`
  (or `NEUTRAL_GEN_DIR`). This is expected in a clean checkout.
- **`kit deploy` says "not configured"** — set `KIT_DEPLOY_CMD` to your delivery deploy command;
  the kit orchestrates it, it doesn't embed it.
- **`INTERACTION DESIGN: refused`** — each line names its check (1 to 9) and, for checks 4 to 9,
  the row of the document it disagrees with, by its line. Change the model to the decision, or,
  where the decision is what should change, have the owner accept the document again and name it
  again with its new checksum. There is no flag or setting that skips it.
- **`kit validate` fails on `DELTA`** — read the cited D-id in `rules/JOGET-PLATFORM-DELTAS.md`; it's
  a real platform gotcha for your declared `dx`/`edition`/`db`.

---

## 12. Repo map

| Path | What |
|---|---|
| `README.md` | the map + the `kit` verb list |
| `application-model.schema.yaml` | the Layer-1 schema |
| `examples/facility-permit.app.yaml` | the worked reference model |
| `examples/facility-permit.interaction-design.md` | the worked reference's interaction design, which its model names |
| `templates/spec/INTERACTION_DESIGN.md.tmpl` | the form of an interaction design the gate reads |
| `tools/kit.py` | the CLI facade |
| `tools/validate.py` | the interaction design gate (L021) + schema + lint + delta + contract |
| `tools/interaction_design.py` | the reading of an interaction design's tables |
| `tools/project_*.py` | the five projectors |
| `tools/emit_*.py` | trace / suite / coverage emitters |
| `tools/MAPPING-*.md` | exactly how each artefact type maps |
| `rules/JOGET-PLATFORM-DELTAS.md` | the delta register (D-001..065) |
| `contracts/registry-mirror.yaml` | mirrored component config contracts |
| `docs/adr/` | every decision (ADR-001..026) |
| `docs/PROJECTION-DECISIONS.md` | per-projector dispositions (what's promoted/deferred) |
| `docs/SESSION-RESUME.md` | fast re-entry / current state |
| `TRACKER.md` | the build roadmap and its evidence |
| `tests/` | the round-trip + hermetic test suite |
