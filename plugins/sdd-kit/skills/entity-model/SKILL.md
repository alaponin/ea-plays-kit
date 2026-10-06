---
name: entity-model
description: >-
  Helps a person write the entity model of one module, with the glossary and the register of
  business rules kept beside it, under the standard SDD-03, The Entity Model. It opens the crossing
  from the module's written descriptions into the model as the standard's form states it, answers
  the form in its first pass and then its second, writes one claim of conformance over the model,
  the glossary and the register together with kit conform, and builds the reader's edition the
  owner reviews. Use it when a module's entity model, glossary or register of business rules is to
  be written, checked or brought up to date. It holds no rule of the standard; it reads every rule
  where the standard states it.
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
standard: SDD-03
written_against: {edition: "1.0", sha256: "7f128a3e0c2e599651a6e37164dbe6e7c472a8d72853abfef75feb1156a72fdc"}
---

# entity-model

## What this skill is for

It helps a person write the entity model of one module: which records the system keeps, what one
record of each kind means, what identifies it, how the records relate, and what the system depends
on whoever keeps it. Beside the model stand its glossary, which carries the words the model does
not, and its register of business rules, which carries the constraints the model cannot express.
The standard is `SDD-03`, The Entity Model, the document whose name begins `SDD-03_` in the
standards root, `standards/`. The register's row
for the thing is `02`. The three are written by one person in one piece of work, and the
standard's part on conformance makes them one claim, so this skill treats them as one artifact
kept in three files. Everything the skill needs to know about them it reads, at the moment it
runs, from that row and from the standard; what it holds is only the steps that need a machine.

## Before the first moment

In the kit's root, `kit/` in this skill's folder:

    python3 tools/kit.py skills --check
    python3 tools/kit.py slot 02

1. **The staleness check.** Read this skill's line, `sdd-kit/entity-model`, in what
   `kit skills --check` prints. Where it reads behind, or pinned to a document not in the root,
   the skill stops and says so: `SDD-01` §14, rule 11. Where the program cannot be run, the skill
   says that the check could not be run and does not treat itself as current.
2. **The row.** From what `kit slot 02` prints, take the document it was read out of, the
   standing, the section named as the form, the template and the two files named beside it, the
   checklist, the seams, the line saying who writes the thing, and the line saying when it is
   written.
3. **A draft says so.** Where the row gives the standing as a draft, the skill tells the person at
   the start, in the words of the standard's own first page read from the document, and enforces
   nothing on the draft's authority beyond what the draft says of itself.
4. **Which pass this is.** The row's line on when the thing is written, and the standard's form,
   say that the form is answered in passes and which of its lines belong to the first. Settle with
   the person, at the start, which pass this sitting is: while `<tree>/03_use_case_model/` holds no
   use case, it is the first; once a goal has been named there, it is the second. Every moment below
   reads the answer.

## Prepare

1. The specification tree, `<tree>`, is the folder `kit spec new` made for the system. The
   thing's folder in it is `<tree>/02_entity_model/`.
2. **In the first pass**, copy the template the row names and the two templates it names beside
   it into that folder, keeping their names:

       cp <kit>/templates/spec/artefacts/02_entity_model.md <tree>/02_entity_model/
       cp <kit>/templates/spec/artefacts/02_glossary.md <tree>/02_entity_model/
       cp <kit>/templates/spec/artefacts/02_business_rules.md <tree>/02_entity_model/

   The comment at the head of each copy names the edition and the checksum of the document the
   template was produced from. It stays as the record of what the file is written to, and it is
   never edited. **In the second pass** nothing is copied: the three files the first pass wrote are
   the ones written into, and a copy is never laid over what a file already holds.
3. **The heading of each file.** Under the title of each copy, the skill writes the file's heading
   in one paragraph: the module the model is of, and the version and date of the file. The model's
   heading also names the glossary and the register beside it, by their file names, because the
   standard's rules for the glossary and for the register ask the model's own heading to name them
   and the template carries no line for it. The heading of the glossary and of the register names
   the model by its file name.
4. For each incoming seam the row prints, confirm that the upstream thing stands in the tree. The
   module's written descriptions stand in `<tree>/00_customer_documents/`; where they do not, the
   skill stops at this moment (*Where this skill stops*, below). The catalogue of settings, in
   `<tree>/05_shared_groundwork/`, is usually written after the first pass: where a business rule
   needs the name of a setting and the catalogue does not yet carry it, that line is a gap, and the
   rest of the work goes on.
5. Nothing is written into an upstream thing's folder, at this moment or at any other.

## Assist

1. Extract the standard's text, in the kit's root, from the document `kit slot 02` was read out
   of, with the kit's own reader, the one `kit slot` reads the edition with. The text is read into
   the session and is not saved into the tree:

       python3 -B -c 'import sys, pathlib; sys.path.insert(0, "tools"); import slot; print(slot.Document(pathlib.Path(sys.argv[1])).text)' "<the document>"

2. **The crossing, first.** Open, in that text, the section the row names as the form, and read
   the sentence at its head that says how the records are found in the module's written
   descriptions; the seam from row `00`, in what `kit slot 02` prints, points at the same sentence.
   Do what it says, one sentence of the descriptions at a time: for each thing a sentence says the
   business deals with, put to the person the tests that sentence names, each read from the rule it
   cites; write the thing where the sentence sends it — a copy of the record table in the model, an
   attribute or a relationship there, or an entry of the glossary or of the register of business
   rules; and write the words of the descriptions that named it as its source line, in the form the
   rule the sentence cites asks for. The skill proposes where each thing goes; the person decides,
   in the person's words.
3. **The passes.** Read, from the same section, the paragraph that says which lines belong to the
   first pass. In the first pass, put only those lines to the person and leave every other line of
   the form empty for the second. In the second pass, put the remaining lines. A line the first pass
   answered is not changed at this moment: the row's notes say that changing it is a different act,
   which travels as a correction.
4. **The parts.** Walk the parts of the form in the order the standard gives them. Each part's
   heading says what one copy of its table stands for — a record, a relationship, the model as a
   whole, a glossary entry, a business rule. Copy the part's table once for each such thing the
   module has, each copy under a heading of its own naming the thing. The parts for glossary
   entries and for business rules are filled in `02_glossary.md` and `02_business_rules.md`, and
   every other part in `02_entity_model.md`. The table of governed lists is filled once, in the
   model, one row for each list, in the columns the standard lays out after its part for the model
   as a whole.
5. Read each line from the standard's text as it is reached: its name, what the standard says to
   write, and the rule it names. Put the line to the person. The skill may propose an answer from
   the material the person has given it; it writes into the line's last column only what the person
   accepts, in the person's words. A line with no answer carries the written reason it has none.
6. **The read-back of a relationship.** Where a line asks for a relationship to be read back to a
   business reader, read the form of the sentence from the rule the line names, and put both
   readings to the business reader the person names, as questions. Write each answer with who gave
   it and when. The skill never answers for the business reader.
7. Who proposes and who decides at this moment is the row's line on who writes the thing, read from
   `kit slot 02`, and not this file.
8. At the end of a pass, answer the model's line that says which pass the model is reported
   finished for. It is read from the form like every other line.

## Check

1. **The verdicts, over the three files.** Read the rules from the table under `## Rules` in the
   checklist the row names, `<kit>/templates/spec/checklists/SDD-03.md`. Put each rule to the
   person, by its identifier and the words the checklist gives it. The rules the standard sets out
   under its parts for the glossary and for the register of business rules — which rules those are
   is read from the standard's own headings, at the moment — are answered by reading
   `02_glossary.md` and `02_business_rules.md`; every other rule is answered by reading
   `02_entity_model.md`. Write the person's answers into
   `<tree>/02_entity_model/_conformance/02_entity_model.md_verdicts.yaml`, one entry for each rule,
   in the form `kit conform` reads (`python3 tools/conform.py --help`): the rule, then `met`,
   `not met` or `not applicable`; and, only where the checklist's `program` column names a program
   for that rule and that program was run, the program as the entry's `check`. At the head of the
   file, as comment lines, name the three files, each with its SHA-256 checksum taken at the moment
   of answering (`shasum -a 256 <the file>`), so that the claim records every part it was made over.
   The skill writes no verdict of its own.
2. **The claim.** In the kit's root:

       python3 tools/kit.py conform 02 <tree>/02_entity_model/02_entity_model.md

   Exit 0: it wrote the one claim, beside the model, in its `_conformance/` folder, one line for
   each rule of the checklist — over the model, the glossary and the register together, as the
   standard's part on conformance makes them one claim. Exit 1: it refused and wrote nothing; each
   refusal names a rule, and what is corrected is the person's answer, never the program or the
   checklist. Exit 2: it could not run, which is said as such.
3. **At the end of each pass.** The claim is written again at the end of each pass. At the end of
   the first, the person answers each rule over what the first pass holds; a rule not met only
   because its lines belong to the second pass is recorded as a finding that names the second pass
   as the moment it is answered.
4. **The person's half.** The questions under the checklist's heading `Gate — the person's half`
   are put to the person one at a time, read from the checklist. An answer that shows something
   missing is a finding (*Where this skill stops*, below).
5. **The program's half.** The standard's own gate says which of its checks a program performs and
   whether they are built; the checklist's `program` column names what the kit holds. The skill
   runs only a program that column names, and reports no result of any check the kit does not hold.
6. **What a change makes stale.** When the model changes after anything downstream was made from
   it, `python3 tools/kit.py stale 02 <tree>/02_entity_model/02_entity_model.md` in the kit's root
   lists what the change makes stale, from what each artifact made from this one records it was
   made from, and changes nothing.

## Render

The reader's edition is the Word document the owner reviews. It is a build (`SDD-01` §14,
rule 1), put to the owner as the ruling of 25 September 2026 on the owner's reading fixes; the
skill reads that ruling at `<standards>/rulings/2026-09-25-the-owner-reviews-a-polished-document.yaml`
and does not restate it.

1. Write one source for the three files, because they are one piece of work, at
   `<tree>/02_entity_model/_reader/02_entity_model_reader.md`, in the register that ruling fixes.
   The explanation of each of the standard's terms it uses is read from the standard's own section
   defining its words, at the moment of writing; the words of the module are explained from the
   module's own glossary. The source is written again from the three files whenever one of them
   changes, and is never corrected in its own right.
2. The picture of the model is drawn by a program kept in `<tree>/_machinery/`, from
   `02_entity_model.md`, in the notation and to the layout convention the model itself states, and
   the picture it draws is kept beside the source and referenced from it. The kit holds no such
   program. Where none has been written for the tree, the edition says that the picture is not
   drawn yet, as the model's own line on its pictures must say too.
3. Build the Word document with pandoc, the document converter, found with `command -v pandoc`:

       pandoc <tree>/02_entity_model/_reader/02_entity_model_reader.md --from markdown --to docx --resource-path <tree>/02_entity_model/_reader --output <tree>/_reviews/02_entity_model.docx

   Where pandoc is not found, the build could not run, and the skill says so.
4. The Word document is never edited. A correction goes into the file it concerns, the source is
   written again, and the document is built again. The owner's acceptance is written into the
   model, below the comment at its head, naming who accepted it, when, and for which pass, and the
   edition is built again from it.

## Where this skill stops

At the moment the standard, the register, the upstream things and the person's own material
together do not settle something the artifact needs. `SDD-01` §14, rule 5 governs that moment; it
is cited here and not restated. The machine steps are these:

1. One file is written into `<tree>/_findings/`, naming what was missing, where the artifact needed
   it, and who is to answer it.
2. Where the standard itself could not be followed, was ambiguous or was silent, the same is
   written into `<tree>/_amendments/`.
3. The skill carries on with the parts the gap does not touch, and stops the moment when none
   remain.

It also stops at the end of the first pass: the second pass is written from the goals, and it
begins only once a goal has been named. And it stops when the staleness check reads behind, and
when a program it runs refuses something: `SDD-01` §14, rule 11.

## What this skill never holds

- No words of any rule of any standard, and no line of any standard's form. A rule is named by its
  identifier and no more, and this file names none.
- No edition of its standard anywhere but the pin.
- No engagement: no engagement's name, path or terms.
- No figure read from a standard, such as a count of rules, parts, lines or checks. It is read at
  run time.

## The fixture test

The fixture is the model of the loans module of a fictitious lending library, which belongs to no
engagement, in its three files: `examples/fixture/02_entity_model.md`,
`examples/fixture/02_glossary.md` and `examples/fixture/02_business_rules.md`, each the template
copied by the prepare moment and filled. Beside them,
`examples/fixture/_conformance/02_entity_model.md_verdicts.yaml` holds the answer to each rule of
the checklist, under a head naming the three files with their checksums, and
`examples/fixture/_conformance/02_entity_model.md_conformance.md` is the one claim `kit conform`
wrote over them. In the kit's root:

    python3 tools/kit.py conform 02 ../skills/entity-model/examples/fixture/02_entity_model.md
    python3 tools/kit.py skills --check

It passes when the first exits 0 and writes one claim naming every rule of the checklist with a
verdict, so that its count of rules equals the checklist's, and the second prints this skill as
current.

## Where the pieces live

| The piece | Where it is |
|---|---|
| the standards root, `<standards>` | `standards/`, in this skill's folder |
| the kit's root, `<kit>` | `kit/`, in this skill's folder |
| the standard | the document whose name begins `SDD-03_` in `<standards>`, as `kit slot 02` resolves it |
| the register's row | row `02` of `<kit>/templates/spec/slots.yaml`, read with `kit slot 02` |
| the templates | `<kit>/templates/spec/artefacts/02_entity_model.md`, with `02_glossary.md` and `02_business_rules.md` beside it |
| the checklist | `<kit>/templates/spec/checklists/SDD-03.md` |
| the programs | `<kit>/tools/kit.py`, with the verbs `slot`, `conform`, `skills --check` and `stale` |
| the ruling on the reader's edition | `<standards>/rulings/2026-09-25-the-owner-reviews-a-polished-document.yaml` |
| the specification tree, `<tree>` | the folder `kit spec new` made for the system |
| the artifact, in three files | `<tree>/02_entity_model/02_entity_model.md`, `02_glossary.md` and `02_business_rules.md` |
| its verdicts and its one claim | `<tree>/02_entity_model/_conformance/` |
| the edition's source | `<tree>/02_entity_model/_reader/` |
| the program that draws the picture | `<tree>/_machinery/`, written for the tree |
| the upstream things | `<tree>/00_customer_documents/`; `<tree>/05_shared_groundwork/` for the names of settings |
| findings and amendments | `<tree>/_findings/` and `<tree>/_amendments/` |
| the reader's edition | `<tree>/_reviews/02_entity_model.docx` |
| the form this skill is written from | `references/SKILL-form.md` in this plugin |
| the fixture | `examples/fixture/` in this skill |
