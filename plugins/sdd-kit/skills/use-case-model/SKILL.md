---
name: use-case-model
description: >-
  Write a system's use case model under SDD-05, The Use Case Model: consolidate several
  disagreeing sources, prepare the model file and one record header for each goal from the
  kit's template, walk the person through the standard's text part by part, run the program's
  half of the standard's review and the kit's claim of conformance, and build the Word edition
  the owner reviews. Use whenever a use case model is written, extended, checked or rendered:
  "write the use case model", "what are the use cases for this system", "build the actor
  catalogue", "does this model meet the standard", "check the model", "consolidate these
  sources into one model", "make the use case model document". It reads the standard, its
  checklist and its template at the moment it runs, and holds no rule of any of them.
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
standard: SDD-05
written_against: {edition: "2.1", sha256: "122eb3aec02971a48996303325112c1c1a98069619335daea3c5d3ce30c0faee"}
---

# use-case-model

## What this skill is for

It helps a person write the use case model: the one statement, for the whole system, of its
boundary, the people and systems outside it, every goal they need, and how those goals group
together. The model is governed by `SDD-05`, The Use Case Model, the document whose name begins
`SDD-05_` in the standards root, `standards/`. It
is row `03` of the kit's register. The skill is written from the plugin's form,
`references/SKILL-form.md` at the root of this plugin, and has the form's four moments with the
one step more the target state gives it: it consolidates several disagreeing sources before it
prepares.

## Before the first moment

1. **The staleness check.** In the kit's root, run `python3 tools/kit.py skills --check`. If the
   line for `sdd-kit/use-case-model` reads behind, or pinned to a document not in the root, stop
   and say so: SDD-01 §14, rule 11 governs the refusal. If the program cannot be run, say that
   the check could not be run, and do not treat the skill as current.
2. **The row.** In the kit's root, run `python3 tools/kit.py slot 03`. Take from what it prints
   the standard's document and its standing, the section it names as the form, the template, the
   checklist, and the seams — what comes in from rows `01` and `02`, and what goes out to rows
   `06` and `04`.
3. **What is a draft.** The model names four things it does not hold: the published register of
   requirements (row `01`), the entity model with its glossary and its register of business
   rules (row `02`), and the catalogue of settings (row `05`). Run `kit slot` for each of those
   rows. Where one prints its standard as a draft, tell the person so, in the words of that
   standard's own first page, and enforce nothing on the draft's authority: the model names the
   thing and resolves identifiers in it, and judges nothing of the thing's own shape.

## Consolidate — only when several sources disagree

When more than one document claims to describe the system and they do not agree, consolidate
them before anything is prepared: `references/consolidate.md` is the step, in four stages — the
input register, the precedence order, every conflict disposed of by its class, and the owner's
rulings. Check the arithmetic of the consolidation with

```
python3 scripts/check_registers.py --inventory <inventory> --disposition <disposition> --rulings <rulings>
```

which prints the vocabulary it used; pass `--verdicts`, `--owner-verdict` and `--absorption`
when the registers use words of their own. `examples/consolidation/` is a closed consolidation
of three fictitious sources to run it against first. The model is then prepared under the
precedence order and the rulings.

## Prepare

1. **The folder.** The model lives in the specification tree's row folder,
   `<tree>/03_use_case_model/`. Its shape is `references/model-shape.md`: a model file, one file
   for each use case, a survey generated from them, and the tree's `_conformance/` beside them.
2. **The model file and the use case files.** Run

   ```
   python3 scripts/prepare.py <tree>/03_use_case_model --system "<the system's name>" --use-case UC-01 --use-case UC-02 ...
   ```

   It writes `use_case_model.md` from the skeleton in `references/model-shape.md`, with the
   edition and checksum the template's head gives, and one file for each identifier under
   `use_cases/`, each a copy of the template `kit slot 03` names,
   `kit/templates/spec/artefacts/03_use_case_model.md`,
   with its identifier filled. It never overwrites a file that exists. `--answers <file>` fills
   the header's answers from a YAML file keyed by the template's own field names;
   `examples/fixture/prepare_answers.yaml` is one.
3. **The upstream things.** Confirm that each thing the row's incoming seams name exists, and
   name it in the model file's head by its path, relative to the model file: the published
   register of requirements, the entity model, the glossary, the register of business rules and
   the catalogue of settings. Write none of them. One that does not exist yet is written in the
   head as absent, with the finding filed and its owner named (below, where this skill stops).

## Assist

Walk the person through the standard's text, part by part, in the order below, reading each
part from the document at the moment it is reached:

```
python3 scripts/standard_text.py <the standard's document, as kit slot 03 prints it> --section <n>
```

The whole system is covered first: every actor and every goal is named before any one goal is
written in depth (the standard's principle P7). Then, in this order:

| Part of the model | Open the standard's section | Where the answer goes |
|---|---|---|
| the system and its boundary | 4 | the model file's sections 1 and 2, and `boundary` and `treatment` in its head |
| the actors | 5, with 2.2 | the model file's table of actors |
| the goals, their names and their levels | 6, with 2.3 | one use case file each; the name and level in its header |
| the relationships | 7 | the headers' relationships; the model file's section 7 for the reasons and the conditions |
| the packages and the survey | 8.1 | the model file's table of packages |
| the binding to the requirements | 8.2 | the headers' linked requirements |
| the vocabulary | 8.3 | the headers' entities; the entity model and the glossary named in the head |
| the rules | 8.4 | the headers' business rules; the register named in the head |
| the record header of each goal | 9 | the rest of each header, as the template lays it out |
| what is written out, and in what order | 10 | the headers' format; the model file's section 9 for the order and its ground |

Which supporting actor each goal calls on is recorded in the model file's section 6, because no
field of the header carries it and the check reads it. When the parts are done, generate the
survey from the headers — it is never written by hand:

```
python3 scripts/extract.py <tree>/03_use_case_model/use_case_model.md --write-survey
```

## Check

1. **The program's half.** Run

   ```
   python3 scripts/check_model.py <tree>/03_use_case_model/use_case_model.md
   ```

   It reads the review's lines and their words from the standard's checklist,
   `kit/templates/spec/checklists/SDD-05.md`,
   and the header's fields and closed sets from the template, both at run time, and prints one
   line for each line of the review: `PASS`, `FINDING` or `OPEN`, with the facts it found, then
   this skill's own heuristics under `LOOK`. It exits 1 — the model refused — when any line
   carries a finding. Every finding is filed in the tree's `_findings/` with an owner before the
   claim is made. A format written in the word the standard for one use case uses for the middle
   form is read as the model standard's word, and the disagreement between the two standards is
   reported.
2. **The person's half.** Every line printed `OPEN` is answered by the model's owner with the
   architecture authority, reading the line as the checklist's section headed
   `Gate — the person's half` states it.
3. **The verdicts.** Write `_conformance/use_case_model.md_verdicts.yaml` beside the model file:
   one answer for each rule of the checklist, `met`, `not met` or `not applicable`. A rule whose
   line the program refused is answered `not met`. The checklist names no program for any rule
   of SDD-05, so every answer is recorded as a person's.
4. **The claim.** In the kit's root, run `python3 tools/kit.py conform 03 <the model file>`. It
   writes `_conformance/use_case_model.md_conformance.md` beside the model file, one line for
   each rule of the checklist, and refuses a claim that is not rule by rule.

The skill writes no verdict of its own. A model in the one-file shape of the retired plugin
for use case models is checked with `--legacy`, which reads it for checking only; it is refused, and it is
brought into the shape of this skill by the prepare moment.

## Render

The reader's edition is the Word document the owner reviews. It is a build and never a source
(SDD-01 §14, rule 1), and it is put to the owner as the ruling of 25 September 2026 fixes,
`rulings/2026-09-25-the-owner-reviews-a-polished-document.yaml` in the standards root.

1. **The build folder.** Copy `scripts/render/` and `scripts/extract.py` into one folder outside
   the specification tree: the document is derived, and does not belong beside its source.
   Because that folder stands outside this skill's folder, set `SDD_KIT_ROOT` and
   `SDD_STANDARDS_ROOT` to the full paths of the `kit/` and `standards/` folders in this
   skill's folder before the build.
2. **The project.** Fill `project.py` there: `SRC`, the model file; `OUT`, the document's name;
   `DOC`, the title page. Anything a reader must not see goes into it twice, as a strip rule and
   as a forbidden term: the strip rule removes it, and the forbidden term makes the release gate
   fail if it survives.
3. **The build.** Run `./build.sh --figs` there, and `--publish <folder>` to copy the gated
   document into the folder people open. The build reads the model, draws the diagrams under
   their geometry guards, builds, renders and paginates twice, and ends with the release gate,
   which must print `ALL CHECKS PASS`. The claim page, its last appendix but one, is read from
   the conformance file and from the standard's own document at build time.
4. **Look at it.** `pdftoppm -f 1 -l 8 -r 100 -png <the document>.pdf page`, and sweep the title
   page, the contents, every figure and the first page of each section. A defect the eye sees
   and the gate does not is a missing check, added to `verify.py` in the same sitting.

The render step's scripts are `scripts/render/build.sh`, `build_doc.py`, `content.py`,
`counts.py`, `diag.py`, `figs.py`, `project.py`, `sanitise.py`, `tocgen.py` and `verify.py`; how
they draw is in `references/render-house-style.md`, `references/render-diagram-convention.md`
and `references/render-failure-catalogue.md`. The owner's acceptance is written into the model
file, and the edition is built again from it.

## Where this skill stops

At the moment the standard, the register, the upstream things and the person's own material
together do not settle something the model needs, the skill stops and does not supply it; SDD-01
§14, rule 5 governs that moment. It writes one file into the tree's `_findings/` naming what was
missing, where the model needed it and who is to answer it; where the standard could not be
followed, was ambiguous or was silent, it writes the same into the tree's `_amendments/`. It then
carries on with the parts the gap does not touch. It also stops when the staleness check reads
behind, and when a program it runs refuses: SDD-01 §14, rule 11.

## What this skill never holds

- No words of any rule of SDD-05 or of any other standard, no line of the standard's review, no
  line of its form, and no part of its worked model: each is read from the checklist, the
  template or the standard's document when it is needed, and a rule is cited by its identifier
  alone.
- No edition of the standard anywhere but the pin.
- No engagement: no engagement's name, path or terms. The fixtures are fictitious.
- No figure read from a standard.

## The fixture test

`examples/fixture/` is a model of a fictitious allotment registry, prepared from the template
with `examples/fixture/prepare_answers.yaml` and checked; `examples/fixture/_conformance/` holds
its verdicts and the claim `kit conform` wrote over it. `examples/refused/use_case_model_one_file.md`
is the same subject in the one-file shape of the retired plugin, which that plugin's gate passed.
In the kit's root:

```
python3 tools/kit.py conform 03 <this skill>/examples/fixture/use_case_model.md
python3 tools/kit.py skills --check
```

The first exits 0 and writes a claim naming every rule of the checklist; the second prints this
skill as current. Then, in this skill's folder:

```
python3 scripts/check_model_selftest.py
```

It checks the fixture, which must pass the program's half; makes fifteen faults in copies of it,
one at a time, each of which must be refused on its own line and on no other; and checks the
one-file fixture, which must be refused on the four lines of the review the report of
24 September 2026 named for a model of that shape. It exits 0 when every case is as expected.
The render step is proved by building the fixture's edition in a build folder outside the tree.

## Where the pieces live

| Piece | Where |
|---|---|
| the standards root | `standards/`, in this skill's folder |
| the kit's root | `kit/`, in this skill's folder |
| the standard | the standards root, the document whose name begins `SDD-05_` |
| the rulings | the standards root, `rulings/` |
| the register's row | the kit's root, `python3 tools/kit.py slot 03` |
| the checklist | `kit/templates/spec/checklists/SDD-05.md` |
| the template | `kit/templates/spec/artefacts/03_use_case_model.md` |
| the claim program | the kit's root, `python3 tools/kit.py conform 03 <the model file>` |
| the staleness check | the kit's root, `python3 tools/kit.py skills --check` |
| the consolidate step | this skill, `references/consolidate.md` and `scripts/check_registers.py` |
| the shape of the model | this skill, `references/model-shape.md` |
| prepare, read, check | this skill, `scripts/prepare.py`, `scripts/extract.py`, `scripts/check_model.py` |
| the standard's text | this skill, `scripts/standard_text.py` |
| the render step | this skill, `scripts/render/` |
| the fixtures | this skill, `examples/fixture/`, `examples/refused/`, `examples/consolidation/` |
| the check's self-test | this skill, `scripts/check_model_selftest.py` |
