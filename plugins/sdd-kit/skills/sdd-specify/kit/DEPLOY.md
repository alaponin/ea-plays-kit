# DEPLOY — the one build-and-deploy path (C3/C4)

There is exactly **one** path from a validated Layer-1 model to a running app. It has two
commands: **build** (pinned) and **deploy** (single). No ad-hoc fork paths, no second
importer.

```
  the interaction design the owner accepted  (SDD-11; slot 08a)
        │  named in the model's entry model.interaction_design, by path and SHA-256
        ▼
  <app>.app.yaml
        │  kit gen  (L021 first; then the projectors, L1 → L2 specs; in-kit, neutral)
        ▼
  Layer-2 specs ──┐
        │  build_app.py --model  (L021 first; every spec projected from that model;
        ▼                 resolves the PINNED generator set from .kit.yaml, version-checked;
                          L2 → Joget JSON → <app>.jwa, and <app>.admission.yaml beside it)
   <app>.jwa + <app>.admission.yaml
        │  deploy_dx9.py  (the admission record, then L021 again; the single DX9 deploy;
        ▼                 encodes rules/JOGET-DEPLOY-DELTAS.md)
   running app on a registered instance
```

## 0. Admission — the interaction design gate (rule L021)

Since 25 September 2026 (METHOD-2026-09-25-12; SDD-11 section 8; the kit's decision record
ADR-105), **a model is admitted to generation, to the build and to the deploy only when it names
the interaction design its owner accepted, and agrees with it.** The model names the document in
one required entry:

```yaml
model:
  schema_version: "0.1.6"
  spec_version: "0.1.6"
  interaction_design:
    path: <the document, relative to this model>.md
    sha256: <its SHA-256 checksum>          # shasum -a 256 <the document>
```

The document is written to the kit's template of its form,
`templates/spec/INTERACTION_DESIGN.md.tmpl`: each row of its five decision tables names the
construct of the model it governs by the model's identifier between backticks (`` `facility_type` ``,
`` `frmPermitApply.national_id` ``, `` `approve` ``), or reads *not in the model*. The kit's worked
reference has one, `examples/facility-permit.interaction-design.md`.

`kit validate`, `kit gen`, `tools/build_app.py`, `kit deploy` and `tools/deploy_dx9.py` run the
same function first (`validate.admit_or_refuse`) and refuse the model, doing nothing else, when:

| Check | The model is refused when |
|---|---|
| 1 | it names no interaction design, or still carries the question `kit new` wrote |
| 2 | the file it names is not there, beside the model at the relative path given |
| 3 | the file's SHA-256 is not the checksum named: a document changed after its acceptance is accepted again and named again |
| 4 | the document's header row *Version and status* does not read `baselined`, *accepted by* a name *on* a date (`25 September 2026` or `2026-09-25`) |
| 5 | a form or list names in its `use_case` a goal the document's table of goals does not list |
| 6 | a list the Lists table names is fixed or maintained, maintained by a role, shows its code, or is divided into categories otherwise than the table decides; or it counts more than nine members in force and carries no `groups` |
| 7 | a place where the References table finds the record *by a search* is placed as a drop-down, radio buttons or check-boxes, or the choice fills or locks other values than the table says |
| 8 | a move the Moves table gives a button is offered by another label or to other roles, or the model offers a button for a move the table lists as no person's |
| 9 | an act the Acts table names carries another record, or a form the table keeps off the menus stands on a visible menu (a CRUD menu shows its list from the menu, and its form only through its New button: an `edit_form`, and a `form` with `add: false`, open from the list's rows and stand on no menu; METHOD-2026-09-26-02, point 18) |

The refusal reads, before anything else a verb prints:

```
INTERACTION DESIGN: refused — 1 error(s) (L021, SDD-11 section 8; an error in every custody mode, and nothing turns it off)
  - [L021] vocabularies/facility_type: check 6 — the list Facility Type (facility_type) shows its code in the model (display_code true), and the Lists table's row 'Facility type (`facility_type`)' (line 45) decides its label is shown
kit gen: REFUSED by the interaction design gate — nothing was done. The model facility-permit.app.yaml is admitted only when it names the interaction design the owner accepted and agrees with it (SDD-11, section 8).
```

(the worked reference with `display_code: true` set on `facility_type`, which its document
decides against).

An admitted model prints `INTERACTION DESIGN: admitted — <path>, baselined, accepted by
<name> on <date>; SHA-256 …; N goal(s) covered, M row(s) … agree with the model`.

**A loss on a gap of the kit** (METHOD-2026-09-26-02, point 19 (b), and its version 3, gap 1).
Where the document decides what the kit cannot yet state or build, the model records the loss in
one place, and the gate admits that disagreement — and no other — while the estate's round that
removes the gap is open:

```yaml
model:
  interaction_design:
    path: ...
    sha256: ...
    losses:
      - { id: LOSS-1, gap: G3, rows: [212], x-note: the fixed list the design divides }
```

`gap` names an entry of the kit's register of its own gaps, `templates/spec/kit-gaps.yaml` (G1 to
G5); `rows` the lines of the document's decision rows it covers. Each entry names the kind of
disagreement it admits, and the gate admits a disagreement on a covered row only when it is of that
kind:

| Entry | The one kind of disagreement it admits |
|---|---|
| G1 | an act the model lacks, where the Acts table's act stands on a list, or opens the very form it stands on (another record of it) |
| G2 | an Acts row that stands on an element that is no form, list or category of the model |
| G3 | a list the model maintains where the Lists table fixes it, and the list is divided into categories (the model's list names `groups`) |
| G4 | an act the model lacks, where the Acts table's act stands on a list |
| G5 | a choice that fills, or locks, some of the values its References row names and not all of them — not a choice that fills nothing, and not a value the form does not place |

Each disagreement admitted is printed under the verdict as a warning, `~ [L021] … — admitted as the
recorded loss LOSS-1, on the kit's gap G3, which the estate's round names open: …`, and the
admission line counts them. A loss covering a row whose disagreement is of another kind is refused
in words that name the kind the disagreement is and the kind the entry admits, and the
disagreement stands:

```
  - [L021] model/interaction_design/losses/LOSS-1: the recorded losses — the loss LOSS-1 covers the document's line 45, where the disagreement is: the list shows its code as its label in one of the two and its label in the other (check 6, code-shown). Its entry G3 (checks 6) admits only: the list is maintained in the application in one of the two and fixed in the other, and the model maintains the list and the row fixes it, and the model's list is divided into categories (it names `groups`) (check 6, maintained-or-fixed: maintained-in-the-model-fixed-in-the-row, divided-into-categories). A loss admits only the kind of disagreement its entry names, and this one stands
```

(the worked reference with `display_code: true` on `facility_type`, recorded as a loss on G3). A
loss naming no entry, an entry the register does not hold, or a row on which no disagreement
arises, is refused too; a disagreement that arises from no row is never admitted. The
engagement's own kinds — the design's words, the model's source, its starting data — are never
admitted, whichever entry a loss over them names. When the round that removes a gap removes its
entry, every model still recording a loss on it is refused.

L021 is an error in `stamp` and in `required` custody alike: it reads no `.kit.yaml`, no key of the
model but its entry `interaction_design`, no flag and no environment variable. The gate cannot know that the owner accepted these very bytes;
it knows that the document the model names says so, and that the model agrees with it.

## 1. Build — `tools/build_app.py` (pinned)

The build uses the generator set **pinned in `.kit.yaml`** (`generators.registry_version`),
resolved from `$JOGET_PLUGINS_HOME` (the `joget-platform-plugins` library). It **refuses** to
run if the library's `registry_version` does not match the pin, or if the library is not
found — so a build can never silently reach into an untracked fork copy (the C2 risk).

```bash
export JOGET_PLUGINS_HOME=/path/to/joget-platform-plugins
python3 tools/build_app.py \
    --model <app>.app.yaml \
    --app <appId> --name "<App Name>" --out build/out \
    --forms <specdir> [<specdir> …] \
    --datalists <specdir> [<specdir> …] \
    --userview <uv.yml> [--dashboard <dash.yml>] [--workflow <wf.yml>] \
    --kit-yaml .kit.yaml
# -> build/out/<appId>.jwa and build/out/<appId>.admission.yaml
```

Prerequisites: `pip install pyyaml`; `$JOGET_PLUGINS_HOME` set; a `.kit.yaml` whose
`generators.registry_version` matches that library.

**The admission (METHOD-2026-09-25-12).** `--model` is required: the build runs the interaction
design gate on it first (section 0) and stops, having built nothing, when it refuses. It then
refuses any spec it is given that was not projected from that model: each `*.spec.yml` of the
`--forms`, `--datalists` and `--reports` directories, and the userview, dashboard and workflow
files, must carry the provenance line `# source_sha256:` that `kit gen` writes, equal to the
model's own SHA-256. A spec written by hand, or projected from another model or an earlier
version of this one, is named and refused:

```
[build] FAIL: 1 of the 1 spec(s) given were not projected from the admitted model <app>.app.yaml (SHA-256 …) — refusing. …
    …/F-handwritten.spec.yml: no provenance line
```

After the archive is built, the build writes beside it `<appId>.admission.yaml`: the rule, the
time, the application, the archive and its SHA-256, the model and its SHA-256, the interaction
design and its checksum, and how many specs were checked. It is written by the build only; the
deploy reads it.

### What every generated application carries: the administration of its lists of values

Since 25 September 2026 (METHOD-2026-09-25-02, `tools/lov.py`), every application the kit
generates carries, with no design in its model, the administration of its lists of values.

Each vocabulary in the model is a list the application maintains, unless the model marks it
`fixed: true`. For each such list, `kit gen` writes into the feature folder `_lov/`: its own
table (the application's id, then `lv_`, then the list's id, cut to 24 characters with a short
digest when longer), a form to add a value and a form to change one, a list, and its first values
from the model's `rows` or `file` (in `_seed/`, loaded like every other seed). An entity of kind
`md_lookup` is treated the same way where the model gives it no form, list or menu of its own.

The userview gains the administration's categories, visible only to the role that maintains the
lists — the list's `maintained_by`, else the application's administrator role (the one role whose
id is `administrator`, `admin`, `system_administrator` or ends in `_administrator` or `_admin`).
Since METHOD-2026-09-25-04 (item 7) they are grouped by the record that uses each list: *Lists of
values — Debt case* holds the lists only the debt case uses, *Lists of values — shared lists*
those used by several records or by none, and no category holds more than nine entries (a larger
one is divided into even parts, *(1 of 2)*, *(2 of 2)*, in the order of the labels). This replaces the
single alphabetical category of the lists-of-values round. Since METHOD-2026-09-26-02 (points 10
and 11) a category that would hold one list is joined with the smallest other of its role, named
after both (*Lists of values — Inspection and shared lists*), and the model may choose one category
instead: `navigation.lists_of_values: {grouping: one_category, category: Admin}`. There a value
can be added, its label changed, its order changed and it can be retired. Nothing is deleted: the entry offers no delete, and the change
form does not let a code change, because records hold the code.

Every drop-down that binds such a list draws its options from it and shows the label only. It
offers only the values in force, in the list's order; a record that already holds a retired
value still shows it and keeps it on save. A cascading list (a vocabulary with a `parent`) offers
only the values of the parent value chosen on the same form. A `fixed` list keeps its values
inline, label only, and cascades through the platform's own control field. Lint rule L017 refuses
a vocabulary the model binds that has no rows and no file, because it would deploy as an empty
drop-down.

For the build, pass the `_lov` folders with the others, and deploy with `--seed` pointed at the
generated `_seed/` folder so that the first values load:

```bash
python3 tools/build_app.py --model <app>.app.yaml ... --forms <gen>/<feature>/forms ... <gen>/_lov/forms \
    --datalists <gen>/<feature>/datalists ... <gen>/_lov/datalists ...
python3 tools/deploy_dx9.py --instance <jdxN> --app <appId> --jwa <out>/<appId>.jwa --seed <gen>/_seed
```

### What every generated application carries: the interaction patterns

Since 25 September 2026 (METHOD-2026-09-25-04; the analysis `INTERACTION_PATTERNS.md`, table 7.3),
the projectors realise the house rules for what a person sees, for every application:

- **A value shown as it is read.** A read-only coded value, reference or directory user is a
  labelled value, not a disabled drop-down; a read-only yes-or-no reads *Yes* or *No*, an editable
  one is a checkbox; a vocabulary with `display_code: true` shows its code. Every date control
  shows the date day first, in `app.conventions.date_format` (default `dd/mm/yy`, DD/MM/YYYY; the
  schema admits only day-first forms).
- **The state as a badge.** The status attribute is a read-only labelled value coloured by its
  state's `tone`, never a drop-down (STA-03).
- **A move made by a button.** A form's `acts[]` (or, when it declares none, the user moves of its
  roles) are buttons on the record's screen, offered only in the states their move leaves from,
  and shown disabled, with the guard's words, where the guard's fact does not hold. Each set of
  roles has a bar of its own, which the platform shows only to those roles (a GroupPermission on
  the element; METHOD-2026-09-25-01, item 20), so nobody is offered a move he may not make. The
  single *Action* drop-down is gone. Each user move has its own trigger form (`act<Entity><Move>`, table
  `<entity table>_act`), created as a new record and post-processed by `joget-transition-guard`,
  the path on which delta D-015 says the post-processor runs. **Deploy
  `joget-transition-guard` 1.2.0 or later**: the trigger forms name the record by `targetField`
  and check the actor's roles (`checkRoles`), which 1.1.0 does not read. Each user move gets a
  hidden userview category, *Moves — <role>*, visible to the move's roles, from which its buttons
  open the trigger forms.
- **A record carried to the form its act opens.** A `prefill` naming `form-prefill` is realised by
  `joget-form-prefill` (1.0.0), and any other component is refused (RL-44). The field that refers
  to the carried record is read-only, and the form's root guard (`joget-require-guard`) refuses a
  save without it or with one that names no row of the record's table.
- **Hidden categories.** A navigation category with `hidden: true` is projected with `hide`
  set, and the lint (U025) refuses a form whose trigger is `record_action` on a visible menu. The
  pinned generator (registry 0.11.0) writes the category's `hide` as the platform's own value, so
  the category is left out of the built application's menu and nothing is done by hand after the
  import. `kit totality` still names a category the specification hides and the build shows
  (T112), which catches a build made with a generator older than 0.11.0.
- **Lists that fit their record.** A field's `options_query` (one of the model's `queries[]`, with
  the carried record's key as its one parameter) is realised by the Enterprise
  `JdbcOptionsBinder`, the parameter written `'#requestParam.<name>?sql#'`. A list's
  `default_scope` may name `#currentUser.username#` and `#requestParam.<name>#`; both are quoted
  and escaped for SQL (L020 refuses any other hash variable).
- **A search that fills.** The fields a smart search's `populate` fills are locked on the page by
  a script the form carries (`kit_locked_fields`) and are not the platform's read-only, which
  would store them blank (delta D-069).
- **References seeded under the key their look-up reads.** `project_seed` writes a seeded
  reference under the target's business key (`pk.attr`) when the model names the row by its seeded
  identifier; L019 refuses a seeded reference that names no seeded row.
- **A long list chosen by category.** A vocabulary of more than nine values in force names its
  `groups` (another vocabulary, its categories); each row names its `group`. A drop-down over it
  is chosen in two steps — the category, a drop-down of the page only that is never stored, then
  the values of that category in force — its options read with their categories by the Enterprise
  `JdbcOptionsBinder`. The administration's form for a value of such a list requires its category.
  U026 refuses a bound list of more than nine values with no `groups`, a category of more than
  nine and a list of more than nine categories.

U001, U007, L018, L019, L020, U025 and U026 are errors in every custody mode, `stamp` included.

### Since 27 September 2026: a move made, a label said, a list read (METHOD-2026-09-26-02)

What one application needed of the kit so that it can be worked
(`tests/test_repair_dm_application.py`, one test for each point):

- **A move made by its button takes effect** (point 1). The button carries the record's key under
  the name of the move form's field that shows it (`record_key`), so that the save, which reads a
  read-only field again from its request (delta D-069), stores it and the guard finds the record.
  Every form opened with a record carried reads the key under the name of the field that shows it.
  A move refused because the record is not in the state it leaves from, or because a guard over a
  word the record holds fails, is refused by the form's root guard in words at the head of the
  form, before anything is saved.
- **The design's words** (point 3). A move's form is headed with the label the model's `acts` give
  the move, and its button says it (FormMenu's *submit button label*); a move two acts label
  differently has a form headed with each. A form whose purpose is `view` is opened read-only and
  offers no Save: from a CRUD menu, edit read-only with no Edit button; from a form menu, read-only
  as the platform reads it (`Yes`).
- **A list's filter reads its list** (point 4). A filter over a list the application maintains
  carries the drop-down's own options binder: the values in force, in the list's order, read when
  the list is shown. Over a divided list the filter is chosen in two steps, category then value,
  when the record holds the category; a record that does not is refused, never offered one step of
  every value.
- **A date and time shown day first** (point 5). A `datetime` attribute is the platform's date
  picker in its date-and-time mode, `DD/MM/YYYY HH:mm`, stored `yyyy-MM-dd HH:mm`; a list shows it
  with the same pattern.
- **The code of an added value is made on saving** (point 9). The form that adds a value asks for
  its label; the code is the platform's ID generator in its distributed mode, a number no two values
  are given, whatever the list, version or deploy. A list whose code is its label (`display_code`)
  asks for the label once, and it is the code; the uniqueness guard says *This label is already in
  the list.* A first value in the shape of a made code (fifteen or more digits) is refused.
- **The administration's grouping is a setting** (point 10): `navigation.lists_of_values`,
  `grouping: by_record` (the default) or `grouping: one_category` with the `category` it is named
  (one application's model: `Admin`). The limit of nine stays with drop-downs and the steps of a
  choice, not with this menu.
- **No menu entry stands alone** (point 11). The lint's A009 refuses a generated menu whose visible
  category holds one entry, naming it; the administration joins a category of one list with the
  smallest other of its role, named after both, and divides a large one into even parts.

The library changes this needs are in the pinned generators (`gen_userview`: the button's label and
the reading forms; `gen_datalists`: a column's labels given inline), registry 0.11.0.

## 2. Deploy — `tools/deploy_dx9.py` (single)

```bash
python3 tools/deploy_dx9.py --instance <jdxN> --app <appId> --jwa build/out/<appId>.jwa
python3 tools/deploy_dx9.py --instance <jdxN> --app <appId> --jwa build/out/<appId>.jwa --dry-run
```

`deploy_dx9.py` is the **only** DX9 deploy. Before it reads the instance registry or touches a
server it **admits the archive** (METHOD-2026-09-25-12): it reads `<appId>.admission.yaml` beside
the archive and refuses, deploying nothing, when there is no record (the archive was not built by
`build_app.py` from an admitted model), when the record names another application, when the
archive's SHA-256 is not the one recorded, when the model the record names is not there or has
changed since the build, when the interaction design gate, run again on that model, refuses it
(section 0), or when a `--seed` spec was not projected from that model. `--dry-run` runs the
admission and stops there, reading no instance; it is how a refusal by the deploy is shown
without a server:

```
[  FAIL   ] no admission record beside the archive (<appId>.admission.yaml is not in build/out): the archive was not built by build_app.py from a model the interaction design gate admitted, and nothing is deployed from it (METHOD-2026-09-25-12; SDD-11 section 8)
```

`kit deploy <app>.app.yaml --instance <jdxN>` runs the gate on the model first too, before its
pre-deploy match.

Once the archive is admitted, it reads `~/.joget/instances.yaml` for the URL,
install path, DB and admin credentials (secrets from the env vars the registry names), and
performs, each step mapped to a delta in `rules/JOGET-DEPLOY-DELTAS.md`:

- resolve instance, ensure `/jw` context (DD-001)
- check that every plugin the archive binds is installed on the instance, before anything is
  imported (G4; described below)
- login + import via the CSRF protocol (DD-002/003)
- publish the imported version (DD-004)
- grant admin visibility — blank category role-permissions (DD-006)
- isolated Tomcat restart to clear the definition cache (DD-005)
- smoke-test that the userview(s) render — the gate (exit 0 only if it passes)

Flags: `--no-grant-admin`, `--no-restart`, `--no-dep-check`, `--instances <path>`, `--seed <dir>`,
`--db-import`, `--dry-run`. None of them skips the admission.

### The plugin check (G4)

Before it imports anything, the deploy reads every class the archive binds (each `className` in
its `appDefinition.xml`) and sets aside those that ship with Joget: every class under
`org.joget.`, the Enterprise plugins included, except the families of Joget's own marketplace
plugins, which a server installs one by one (`NOT_SHIPPED_WITH_JOGET` in `tools/deploy_dx9.py`;
today one family, the API Builder's `org.joget.api.`). Every class left must be found as a class
file in one of the jars in the instance's `wflow/app_plugins` folder, under the `installation_path`
that `~/.joget/instances.yaml` gives the instance. If any is missing, the deploy stops before the
import and names each missing class, and for a class of a Joget marketplace family the plugin that
carries it. When the instance has no installation path on this machine the check cannot be made:
the deploy says how many classes it could not verify and proceeds. `--no-dep-check` skips the
check. The check reads class files only: it does not tell which version of a plugin holds a
class, and it does not follow a plugin's own dependencies.

The plugins an application the kit builds needs, and what in the model calls for each:

| Plugin | Needed when | The class the archive binds |
|---|---|---|
| Joget's API Builder, the marketplace plugin `apibuilder_plugins`, installed through the console's plugin upload | always: every archive carries the data interface `API-<appId>-data`, through which the starting data loads and the acceptance runner acts | `org.joget.api.lib.AppFormAPI` |
| `joget-transition-guard` 1.2.0 or later, with the two library bundles it imports, `joget-status-manager` and `joget-event-chain` (2.0.0) | an entity with a lifecycle: its engine-events form, and the trigger form of each move a person makes | `com.fiscaladmin.joget.transitionguard.TransitionGuard` |
| `joget-unique-guard` | a maintained list of values (the administration's forms keep each code unique), and an entity uniqueness constraint enforced by a guard | `com.fiscaladmin.joget.uniqueguard.UniqueGuard` |
| `joget-require-guard` | an entity's `validations`, a reference that must name an existing record, and a record carried to the form an act opens | `com.fiscaladmin.joget.requireguard.RequireGuard` |
| `joget-form-prefill` 1.0.0 | a form whose `prefill` names `form-prefill` | `com.fiscaladmin.joget.formprefill.FormPrefillLoadBinder` |
| `joget-lookup-field` | a look-up that shows a record's name beside the key typed | `global.govstack.lookupfield.element.LookupFieldElement` |
| `joget-smart-search` | an editable reference to a register that is searched rather than chosen from a list | `global.govstack.smartsearch.element.SmartSearchElement` |

The API Builder is the one a server most often lacks: without it every call to the data interface
answers 500. The check has named it since 24 September 2026 (METHOD-2026-09-24-03); before that it
passed every `org.joget.` class as shipping with Joget.

**`--db-import` (credential-free, DD-009).** When the console admin secret isn't held but the
registry Postgres creds are, `--db-import` imports at the **definition level** instead of over
HTTP: it parses `appDefinition.xml`, UPSERTs `app_app` (published) + rewrites the
`app_form/datalist/userview/builder` rows + creates the `app_fd_<table>` tables, then runs the
same grant-admin → restart → `--seed` → smoke steps (the smoke is an unauthenticated GET). Use it
to run the **entire** path with one command where only DB access is available:

```bash
python3 tools/deploy_dx9.py --instance jdx7 --app facilityPermit \
    --jwa build/out/facilityPermit.jwa --db-import --seed build/gen/_seed
```

**Deprecated:** any earlier toolkit DX9 import path. Use `deploy_dx9.py` only; it is the sole
home of the DX9 deploy deltas.

## Worked example — a registration app → your instance

```bash
export JOGET_PLUGINS_HOME=$PWD/../joget-platform-plugins
python3 tools/build_app.py --model <your-project>/<its model>.app.yaml \
    --app registrationApp --name "Registration" --out build/out \
    --forms   <your-project>/build/F0*/forms \
    --datalists <your-project>/build/F0*/datalists \
    --userview  <your-project>/build/<its userview>.uv.yml \
    --dashboard <your-project>/build/<its dashboard>.dash.yml \
    --workflow  <your-project>/build/<its workflow>.spec.yml \
    --kit-yaml .kit.yaml
python3 tools/deploy_dx9.py --instance <your-instance> --app registrationApp --jwa build/out/registrationApp.jwa
```

> Note: the build needs `--model`, that model must name an accepted interaction design, and each
> spec given must carry that model's provenance line; the build refuses the example unless all
> three hold. The paths are placeholders, so the example is a shape, not a command known to run.
