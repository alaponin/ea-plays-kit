---
name: application-model
description: >-
  Helps a person, with an assistant, write the application model of a system under the standard
  SDD-09, The Application Model: the one description of the application a program
  reads, compiled from the use cases written out in full, their screen records and the interaction
  design the owner accepted, by the landing tables the standards for one use case (SDD-06) and for
  its screens (SDD-07) carry. It starts the model from the kit's skeleton, names the accepted
  interaction design by path and checksum, lands each thing where its row says and records every
  judgement as an assumption and every thing that cannot land as a loss; checks the model with kit
  validate (the interaction design's gate, then the levels the standard names), the landing ledger
  with its own program, and writes the claim of conformance rule by rule with kit conform; and
  builds the reader's edition of the assumptions and losses. It holds no rule of any standard and reads the landing
  tables at the moment of use.
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
standard: SDD-09
written_against: {edition: "1.2", sha256: "039b22acac1ac4fe5f2501daa633673e26e369e747810ac1826e26613cc8bab8"}
---

# application-model

## What this skill is for

It helps a person write the application model: the description of the application that the delivery
kit's programs read and generate the application from, written goal by goal from the documents
people wrote before it. The standard is `SDD-09`, The Application Model, the document whose name
begins `SDD-09_` in the standards root, `standards/`.
The register's row for the thing is `09`. The model's form is the kit's schema of the model, which
the row names as its template. The standard says who writes the model: an assistant writes it,
under the discipline that a gap is recorded and never invented, and a person reviews it and
approves it or asks for adjustments.

This skill takes the place of `s2c-compile-to-l1`, which built the model from the stage names of an
earlier pipeline. It compiles instead from the method's own things, by the landing tables the
standard for one use case and the standard for its screens now carry, and it holds only the steps
that need a machine and one program, `scripts/landing.py`, which reads those tables at the moment of
use and checks the record of where each thing landed.

## Before the first moment

In the kit's root, `kit/` in this skill's folder:

    python3 tools/kit.py skills --check
    python3 tools/kit.py slot 09

1. **The staleness check.** Read this skill's line, `sdd-kit/application-model`, in what
   `kit skills --check` prints. Where it reads behind, or pinned to a document not in the root, the
   skill stops and says so: `SDD-01` §14, rule 11. Where the program cannot be run, the skill says
   that the check could not be run and does not treat itself as current.
2. **The row.** From what `kit slot 09` prints, take the document it was read out of, the standing,
   the sections named as the form, the template, the checklist, the program of the check, every
   incoming seam with the section that states how it is crossed, the line saying who writes the
   thing, the moment it is written, and the row's notes.
3. **A draft says so.** Where the row gives the standing as a draft, the skill reads the line of the
   standard's first page that states its version and standing, and tells the person at the start in
   those words.

## Compile

This moment takes the place of the prepare moment of the plugin's form: the model is not filled
from an empty template but compiled from the things upstream of it.

1. **The tree.** The specification tree, `<tree>`, is the folder `kit spec new` made for the system.
   The model's folder in it is `<tree>/09_application_model/`.
2. **The accepted interaction design.** The model is written only from an interaction design the
   owner has accepted: `SDD-01` §14, rule 19, and the row's `when` line. In the kit's root, the kit's own reader prints
   the document's status, who accepted it and when:

       python3 -B tools/interaction_design.py <tree>/08a_interaction_design/INTERACTION_DESIGN.md

   Where it prints any status but baselined with a name and a date, the skill stops at this moment
   and says so; nothing of the model is written.
3. **The upstream things.** For each incoming seam the row prints (the lines beginning `<-`),
   confirm that the upstream thing stands in its folder of the tree at the version the documents
   downstream of it cite: the use cases written out in full for the goals the interaction design
   covers, their screen records, the entity model, the shared registers, the architecture
   specification and the register of requirements. Where one does not, the skill stops at this
   moment. Nothing is written into an upstream thing's folder, at this moment or at any other.
4. **The skeleton.** In the kit's root:

       python3 tools/kit.py new <appId> --name "<the application's name>" --out <tree>/09_application_model/<appId>.app.yaml

   The skeleton asks one question first, in its entry `model.interaction_design`. Answer it with
   the accepted document's path relative to the model and its checksum, taken with
   `shasum -a 256 <tree>/08a_interaction_design/INTERACTION_DESIGN.md`. Replace every placeholder
   the skeleton carries as the landing reaches it.
5. **The landing tables, read now.** In this skill's folder:

       python3 scripts/landing.py tables

   It reads the register's crossing from the use case into the model, opens the sections of the
   standards that crossing names, and prints every row of their tables: the thing, where it
   lands, whether the landing is mechanical or a judgement, and where it cannot land. The ledger
   uses a row's first cell in exactly the words printed.
6. **The landing.** Walk each upstream document with the person, thing by thing, in the order the
   document gives. For each thing, find its row, write the thing into the model where the row lands
   it, and write one entry for it into `<tree>/09_application_model/landing.yaml`, in the form the
   program's own help gives (`python3 scripts/landing.py --help`):
   - a thing its row lands in the model goes under `items`, with the place it landed as `ref`;
   - where the row reads a judgement, the entry carries the decision in one sentence as
     `assumption` and its ground by identifier and section as `ground`; where the row reads both,
     or offers more than one place, it carries either those two or `why_mechanical`, one sentence
     saying why no judgement arose;
   - a thing that cannot land, in whole or in part, is written into
     `<tree>/09_application_model/loss-report.yaml`, one entry with `id`, `what`, `landed_as` and
     `feeds` (the fields the kit's refusal of an unnamed loss reads), and its ledger entry names
     the loss;
   - a thing its row lands nowhere and carries in its own document goes under `carried`.

   What the words mechanical, judgement, assumption and loss mean is read from the section of the
   standard for one use case that the tables stand in, at the moment of use, and not from this file.
7. **The interaction design's decisions.** Each row of its tables of lists, references, moves and
   acts is carried into the construct of the model that realises it, as a transcription, and is
   decided again by nobody. How a row names its construct is read from the kit's template of the
   document, `<kit>/templates/spec/INTERACTION_DESIGN.md.tmpl`. The ledger does not repeat these
   rows: the kit's gate compares the model with them, row by row, at the check.
8. **Two limits of the landing tables, and how this skill meets them.** The review that accepted
   the tables named two places where they fall short of their own definitions, to stand until a
   later edition corrects them.
   - *An actor other than the primary actor.* The tables give a row to the goal's primary actor
     only. A second actor a use case calls on, in a step or a variation, lands among the model's
     roles wherever the model names it as acting, because the model's check refuses a role it
     names and does not declare. The entry goes under the ledger's `outside` list, with the place it
     landed, the assumption, its ground and the path of an amendment; the amendment, written into
     `<tree>/_amendments/`, records that the table is silent, names the section of the standard for
     one use case that holds the tables, and names that standard's owner as the one to answer.
   - *A whole-record screen.* Its row reads mechanical and offers two places. The skill treats the
     landing as a judgement: the person chooses between the two places the row names, and the
     ledger entry carries the assumption and its ground. `landing.py check` reports such an entry
     that carries neither an assumption nor `why_mechanical`. The disagreement between the row and
     the tables' own definition of mechanical is written into `<tree>/_amendments/`, naming the
     section of the standard for the screens that holds the row and that standard's owner.

## Assist

1. Extract the standard's text, in the kit's root, from the document `kit slot 09` was read out of,
   with the kit's own reader, the one `kit slot` reads the edition with. The text is read into the
   session and is not saved into the tree:

       python3 -B -c 'import sys, pathlib; sys.path.insert(0, "tools"); import slot; print(slot.Document(pathlib.Path(sys.argv[1])).text)' "<the document>"

2. Open, in that text, the sections the row names as the form, and walk the person through the
   model section by section in the order the standard gives them. The fields of each construct,
   their types and which are required are read from the kit's schema of the model, the row's
   template, `<kit>/application-model.schema.yaml`, at that moment; they are never retyped here.
3. Where the standard or the schema says a value is read from an upstream document, the skill reads
   it there. Where that document is silent or disagrees with another, the skill records a finding
   (*Where this skill stops*, below) and does not choose a value.
4. The row's notes name the sections of the model that no upstream thing feeds. Where the model
   needs one of them, what is written is a finding with an owner, never a local invention.
5. A fault found in the model goes back into the document that asserted it, as the row's notes
   say, and never into the model alone.

## Check

1. **The model.** In the kit's root:

       python3 tools/kit.py validate <tree>/09_application_model/<appId>.app.yaml

   The interaction design's gate runs first, then the levels the standard's gate section names.
   Exit 0: both passed. Any other exit: what it prints names each refusal; what is corrected is
   the model, or the document upstream that the refusal traces to, and never the
   program. A refusal is answered, not worked around: `SDD-01` §14, rule 11.
2. **The landing.** In this skill's folder:

       python3 scripts/landing.py check <tree>/09_application_model/landing.yaml

   It reads the tables again at that moment and reports, for every ledger entry, a row the tables
   do not carry, a judgement without its assumption, a place in the model that does not resolve, a
   loss the loss report does not hold or a loss no entry names, an entry in the wrong list, and
   every entry of the loss report that the kit's own refusal of an unnamed loss refuses. Exit 0:
   nothing to report. Exit 1: each line names the entry. Exit 2: it could not run, which is said as
   such. It reads the ledger and not the upstream documents, so whether every thing they carry has
   an entry is the person's walk at the landing, and the skill says so.
3. **The verdicts.** Read the rules from the table under `## Rules` in the checklist the row names,
   `<kit>/templates/spec/checklists/SDD-09.md`. For each rule whose `program` column names a
   program that was run at step 1, the verdict is that program's answer: `met` where it passed the
   model, `not met` where it refused the model on that rule. Write one entry for each rule into
   `<tree>/09_application_model/_conformance/<appId>.app.yaml_verdicts.yaml`, in the form
   `kit conform` reads (`python3 tools/kit.py conform --help`), naming the program as the entry's
   `check`. A rule no program checks is put to the person, and the answer is theirs. The skill
   writes no verdict of its own.
4. **The claim.** In the kit's root:

       python3 tools/kit.py conform 09 <tree>/09_application_model/<appId>.app.yaml

   Exit 0: it wrote the claim beside the model, in its `_conformance/` folder, one line for each
   rule of the checklist. Exit 1: it refused and wrote nothing; each refusal it prints names a rule,
   and what is corrected is the verdicts file. Exit 2: it could not run, which is said as such.
5. **The person's half.** The questions under the checklist's heading `Gate — the person's half`
   are put to the person one at a time, read from the checklist, where it states any.
6. **What a change makes stale.** When the model changes after anything was generated from it,
   `python3 tools/kit.py stale 09 <tree>/09_application_model/<appId>.app.yaml` in the kit's root
   lists what the change makes stale, and changes nothing.

## Render

The reader's edition puts to the owner what only a person can settle about the model: every
assumption the ledger records and every loss the loss report holds. It is a build (`SDD-01` §14,
rule 1), put to the owner as the ruling of 25 September 2026 on the owner's reading fixes; the
skill reads that ruling at `<standards>/rulings/2026-09-25-the-owner-reviews-a-polished-document.yaml`
and does not restate it.

1. Write the edition's source from the ledger, the loss report and the model, at
   `<tree>/09_application_model/_reader/APPLICATION_MODEL_reader.md`. Each assumption and each loss
   becomes one card saying, in plain words, what the application will do because of it, with the
   document and section it rests on. How such a card is written — what the application will do,
   never what the model's text says; facts shown, only genuine choices asked — is the method's
   step for any review, carried by a skill this kit does not include; the card is written to the three
   points just named.
2. Build the Word document with pandoc, the document converter, found with `command -v pandoc`:

       pandoc <tree>/09_application_model/_reader/APPLICATION_MODEL_reader.md --from markdown --to docx --output <tree>/_reviews/APPLICATION_MODEL.docx

   Where pandoc is not found, the build could not run, and the skill says so.
3. The Word document is never edited. The owner's answer on an assumption goes back into the
   document upstream that the assumption rests on, as a finding, never into the model alone; the
   model is compiled again from it, and the edition is built again.

## Where this skill stops

At the moment the standard, the register, the landing tables, the upstream things and the person's
own material together do not settle something the model needs. `SDD-01` §14, rule 5 governs that
moment; it is cited here and not restated. The machine steps are these:

1. One file is written into `<tree>/_findings/`, naming what was missing, where the model needed
   it, the document that owns the fact, and who is to answer it.
2. Where the standard itself, or one of the landing tables, could not be followed, was ambiguous or
   was silent, the same is written into `<tree>/_amendments/`.
3. The skill carries on with the parts the gap does not touch, and stops the moment when none
   remain.

It also stops when the staleness check reads behind, when the interaction design does not stand
accepted, and when a program it runs refuses something: `SDD-01` §14, rule 11.

## What this skill never holds

- No words of any rule of any standard, and no line of any standard's form or of any landing table.
  A rule is named by its identifier and no more.
- No construct of the kit's schema of the model: its fields are read from the schema at run time.
- No edition of its standard anywhere but the pin.
- No engagement: no engagement's name, path, terms or model.
- No figure read from a standard, such as a count of rules, rows, sections or levels. It is read at
  run time.

## The fixture test

The fixture is the application model of the lending desk of the library of a town called
Eastbrook, which does not exist and belongs to no engagement: the same application whose
interaction design is the fixture of the plugin's skill `interaction-design`. Its folders stand as a
specification tree would hold them:

- `examples/fixture/06_use_cases/UC-LD-01.md` and `examples/fixture/06_use_cases/UC-LD-02.md`, the
  two use cases written out in full, filled from the kit's template of the use case;
- `examples/fixture/07_screens/UC-LD-01.md` and `examples/fixture/07_screens/UC-LD-02.md`, and
  `examples/fixture/08a_interaction_design/INTERACTION_DESIGN.md`, byte for byte the screen records
  and the accepted interaction design of that skill's fixture;
- `examples/fixture/02_05_04_settled_once/EXTRACT.md`, an extract standing in for the entity model,
  the shared registers and the architecture specification, which claims conformance to none;
- `examples/fixture/09_application_model/lending_desk.app.yaml`, the model, written from the kit's
  skeleton; beside it `examples/fixture/09_application_model/landing.yaml`, the ledger, and
  `examples/fixture/09_application_model/loss-report.yaml`, the losses;
- `examples/fixture/09_application_model/_conformance/lending_desk.app.yaml_verdicts.yaml`, the
  answer to each rule of the checklist, and
  `examples/fixture/09_application_model/_conformance/lending_desk.app.yaml_conformance.md`, the
  claim `kit conform` wrote over the model;
- `examples/fixture/_findings/F-LD-01.md` and `examples/fixture/_findings/F-LD-02.md`, the two
  findings the compile raised, and `examples/fixture/_amendments/A-LD-01.md`, the amendment for the
  second actor the landing table does not cover.

The fixture's ledger exercises the first limit of the landing tables: the head librarian, called
on in a variation, lands under `outside` with its amendment. Its screens carry no whole-record
screen, so the second limit is not exercised by the fixture. No reader's edition is built for the
fixture: it tests the skill's compile and check, and says so here rather than leaving the part out.

In this skill's folder:

    python3 scripts/landing.py tables
    python3 scripts/landing.py check examples/fixture/09_application_model/landing.yaml

In the kit's root:

    python3 tools/kit.py validate ../skills/application-model/examples/fixture/09_application_model/lending_desk.app.yaml
    python3 tools/kit.py conform 09 ../skills/application-model/examples/fixture/09_application_model/lending_desk.app.yaml
    python3 tools/kit.py skills --check

It passes when `landing.py tables` prints the rows it read and exits 0, `landing.py check` exits 0
with nothing to report, `kit validate` admits the interaction design and passes every level with
exit 0, `kit conform` exits 0 and writes a claim naming every rule of the checklist with a verdict, so that its count of rules equals the checklist's, and `kit skills --check` prints this
skill as current.

## Where the pieces live

| The piece | Where it is |
|---|---|
| the standards root, `<standards>` | `standards/`, in this skill's folder |
| the kit's root, `<kit>` | `kit/`, in this skill's folder |
| the standard | the document whose name begins `SDD-09_` in `<standards>`, as `kit slot 09` resolves it |
| the register's row | row `09` of `<kit>/templates/spec/slots.yaml`, read with `kit slot 09` |
| the landing tables | the sections of the standards for one use case and for its screens that the register's crossing from row 06 into row 09 names, read by `scripts/landing.py` |
| the template: the kit's schema of the model | `<kit>/application-model.schema.yaml` |
| the skeleton | `kit new`, `<kit>/tools/kit.py` |
| the checklist | `<kit>/templates/spec/checklists/SDD-09.md` |
| the model's check, with the interaction design's gate | `<kit>/tools/validate.py`, reached as `kit validate` |
| the kit's reader of an interaction design, and its template | `<kit>/tools/interaction_design.py`; `<kit>/templates/spec/INTERACTION_DESIGN.md.tmpl` |
| the kit's refusal of an unnamed loss | `<kit>/tools/compile_l1.py`, called by `scripts/landing.py` |
| the programs | `<kit>/tools/kit.py`, with the verbs `slot`, `new`, `validate`, `conform`, `skills --check` and `stale` |
| the landing program | `scripts/landing.py` in this skill |
| the ruling on the reader's edition | `<standards>/rulings/2026-09-25-the-owner-reviews-a-polished-document.yaml` |
| the specification tree, `<tree>` | the folder `kit spec new` made for the system |
| the model, its ledger and its losses | `<tree>/09_application_model/` |
| its verdicts and its claim | `<tree>/09_application_model/_conformance/` |
| the edition's source | `<tree>/09_application_model/_reader/` |
| the upstream things | the folders of the tree the row's incoming seams name |
| findings and amendments | `<tree>/_findings/` and `<tree>/_amendments/` |
| the reader's edition | `<tree>/_reviews/APPLICATION_MODEL.docx` |
| the form this skill is written from | `references/SKILL-form.md` in this plugin |
| the fixture | `examples/fixture/` in this skill |
