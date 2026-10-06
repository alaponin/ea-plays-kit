---
name: use-case-description
description: >-
  Helps a person write one use case out in full under the standard SDD-06, One System Use Case.
  It writes the record header first, copied from the use case model and resolved against the entity
  model, the register of requirements, the register of business rules and the shared registers
  before any prose; walks the narrative through the standard's own template, read from the document
  at the moment of use; writes the claim of conformance rule by rule with kit conform; reads with the
  person where each thing the use case carries lands in the application model, from the table the
  standard itself carries; and builds the reader's edition the owner reviews. Use it for every goal
  the use case model decides to write out in full. It holds no rule of the standard; it reads every
  rule where the standard states it.
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
standard: SDD-06
written_against: {edition: "1.2", sha256: "b414e78337ac134cf51a3cbe6477e6653b2c7aabd585de0130bc9df703c6f50a"}
---

# use-case-description

## What this skill is for

It helps a person write one goal out in full: the story of the goal, every way it can be reached,
and every way it can fail, in one document read by one person in one sitting. The standard is
`SDD-06`, One System Use Case, the document whose name begins `SDD-06_` in the standards root,
`standards/`. The register's row for the thing is
`06`, and the row says it is written again for every goal, one folder for each. Everything the
skill needs to know about the thing it reads, at the moment it runs, from that row and from the
standard; what it holds is only the steps that need a machine.

## Before the first moment

In the kit's root, `kit/` in this skill's folder:

    python3 tools/kit.py skills --check
    python3 tools/kit.py slot 06

1. **The staleness check.** Read this skill's line, `sdd-kit/use-case-description`, in what
   `kit skills --check` prints. Where it reads behind, or pinned to a document not in the root,
   the skill stops and says so: `SDD-01` §14, rule 11. Where the program cannot be run, the skill
   says that the check could not be run and does not treat itself as current.
2. **The row.** From what `kit slot 06` prints, take the document it was read out of, the
   standing, the section named as the form, the template, the checklist, the seams, the line
   saying who writes the thing, and the notes.
3. **A draft says so.** Where the row gives the standing as a draft, the skill tells the person at
   the start, in the words of the standard's own first page read from the document, and enforces
   nothing on the draft's authority beyond what the draft says of itself.
4. **The goal, and its form.** The goal is one row of the use case model's survey, and its record
   is the file the use case model keeps for it in `<tree>/03_use_case_model/`. Read that record.
   Where it does not exist, or where it says that this use case takes a form other than written out
   in full, the skill stops: which goals are written, and in which form, is the model's to decide,
   as the standard's section on choosing the form says, and this skill writes only the full form.
5. **The departures the method declares.** The row's notes name the ways the method departs from
   this standard, cite the section of `SDD-01` that declares them, and say that a claim made here
   must name them. Read them from that section of `SDD-01`, the document whose name begins
   `SDD-01_` in the standards root, at this moment, and carry them to the check moment.

## Prepare — the header first

1. The specification tree, `<tree>`, is the folder `kit spec new` made for the system. The goal's
   folder in it is `<tree>/06_use_cases/<the use case's identifier>/`, one for each goal.
2. Copy the template the row names into that folder, keeping its name:

       cp <kit>/templates/spec/artefacts/06_use_case.md <tree>/06_use_cases/<the use case's identifier>/

   The comment at the head of the copy names the edition and the checksum of the document the
   template was produced from. It stays as the record of what the use case is written to, and it
   is never edited.
3. **The header, before any narrative field is touched.** The first part of the template is the
   record header. Fill each of its fields from the field of the model's record that carries the
   same thing, copied and not decided: the standard's first section names what the writer is
   given and may not decide, and a writer who finds themselves deciding one has found a gap in the
   model. Where the model's record carries nothing for a field, the field stays empty and the gap
   is raised against the model (*Where this skill stops*, below).
4. **Resolve every entry of the header before any prose is written.** `SDD-01` §7 gives the
   reason: every entry can then be checked against what was settled earlier, and an invention is
   caught at the start rather than at the end. Each skill of the method writes one `###` heading
   for each thing in a file, so each look-up is a listing of headings:

       grep -n '^### ' <tree>/01_requirements_register/01_requirements_register.md
       grep -n '^### ' <tree>/02_entity_model/02_entity_model.md
       grep -n '^### ' <tree>/02_entity_model/02_business_rules.md

   Every requirement the header names must be an entry of the register of requirements as it is
   published; every record it names, a record of the entity model; every business rule, an entry
   of the register of business rules; the primary actor, an actor of the use case model's
   catalogue of actors. Every identifier the header cites for something the shared registers
   publish is looked up in the set the register in `<tree>/05_shared_groundwork/` publishes, read
   in the shape that register's setting on its published set names. An entry that does not resolve
   is never reworded to fit: it is a gap, raised against the document that owns it.
5. **What the header is asked for and has no field for.** The method asks the header to name every
   record, every event, every setting and the set of screens that serve the goal before any prose
   (`SDD-01` §7). The template carries a field for the records and none for the rest, and the row's
   notes record that the standard has no line for a setting, an event or a computation. The skill
   adds no field to the template. It names each such thing the goal uses to the person at this
   moment and resolves it as in step 4; the use case then names it only where a field of the
   template reaches it — a setting through the business rule that reads it, an event or a
   computation at the step that raises or reads it.
6. Nothing is written into an upstream thing's folder, at this moment or at any other.

## Assist — the narrative

1. Extract the standard's text, in the kit's root, from the document `kit slot 06` was read out
   of, with the kit's own reader, the one `kit slot` reads the edition with. The text is read into
   the session and is not saved into the tree:

       python3 -B -c 'import sys, pathlib; sys.path.insert(0, "tools"); import slot; print(slot.Document(pathlib.Path(sys.argv[1])).text)' "<the document>"

2. Open, in that text, the section the row names as the form, and walk its second part, the
   narrative fields, in the order the template gives them. Read each field from the standard's text
   as it is reached: its name, what the standard says to write, and the rule it names. Put the
   field to the person. The skill may propose an answer from the material the person has given it;
   it writes into the field's last column only what the person accepts, in the person's words.
3. Where a field names a rule, open that rule in the text before the field is written, and read it
   with the person. The standard's sections on writing the flows and on what may and may not
   appear inside a use case are reached in this way, field by field; the skill carries no line of
   them.
4. A field too long for its cell — usually the main success scenario and the extensions — is set
   out below the table under a heading of its own, and the cell says where. The standard's own
   worked example lays them out the same way.
5. A word, a rule or a requirement the goal needs and the model does not carry is never supplied
   here: it is a gap, raised against the model (*Where this skill stops*, below).
6. Who proposes and who decides at this moment is the row's line on who writes the thing, read from
   `kit slot 06`, and not this file.
7. Nothing about screens is written here. The screens are a document of their own, written from
   this one.

## Check

1. **The verdicts.** Read the rules from the table under `## Rules` in the checklist the row names,
   `<kit>/templates/spec/checklists/SDD-06.md`. The standard's review names who answers them — read
   from the words before its first subsection, which the checklist's heading
   `Gate — the program's half` carries — and it is not the writer. Put each rule to them, by its
   identifier and the words the checklist gives it, and write their answers into
   `<tree>/06_use_cases/<the use case's identifier>/_conformance/06_use_case.md_verdicts.yaml`, one
   entry for each rule, in the form `kit conform` reads (`python3 tools/conform.py --help`): the
   rule, then `met`, `not met` or `not applicable`; and, only where the checklist's `program` column
   names a program for that rule and that program was run, the program as the entry's `check`. The
   skill writes no verdict of its own.
2. **What the claim must name and the claim file has no line for.** The standard's paragraph on
   claiming conformance asks a claim to name the model the use case belongs to and its version, and
   the row's notes ask it to name the departures of step 5 before the first moment. The claim
   `kit conform` writes carries a line for each rule and none for either. At the head of the
   verdicts file, as comment lines, the skill therefore writes the model and its version, the
   departures in the words of `SDD-01`, and the SHA-256 checksum of the use case file taken at the
   moment of answering (`shasum -a 256 <the file>`).
3. **The claim.** In the kit's root:

       python3 tools/kit.py conform 06 <tree>/06_use_cases/<the use case's identifier>/06_use_case.md

   Exit 0: it wrote the claim beside the use case, in its `_conformance/` folder, one line for each
   rule of the checklist. Exit 1: it refused and wrote nothing; each refusal names a rule, and what
   is corrected is the answer, never the program or the checklist. Exit 2: it could not run, which
   is said as such. The claim is made once for each use case and never for a set of them, as the
   standard's review says.
4. **The person's half.** The questions under the checklist's heading `Gate — the person's half`
   are put, one at a time, to those the review names, to be asked aloud at the review. The skill
   does not answer them. An answer that shows something missing is a finding.
5. **The program's half.** The skill runs only a program the checklist's `program` column names,
   and reports no result of any check the kit does not hold.
6. **What the use case gives the application model.** The row's outgoing seam to row `09` names
   the section of the standard that says where each thing a use case carries lands in the
   application model; `kit slot 06` prints it on that seam's line `declared at`. Open that section
   in the text. For each row of its first table, find the entries of this use case of the kind the
   row's first cell names, and read the row's other cells with the person: where the entry lands,
   whether the landing is mechanical or a judgement, and where it cannot land.
   - For an entry the row calls mechanical, confirm that it stands as step 4 of the prepare moment
     resolved it: a program will carry it as it is written.
   - For an entry the row calls a judgement, nothing is decided here. Whoever writes the
     application model decides it and writes it down, as that section says.
   - Where the person finds that an entry falls under the row's last cell, the skill says so. Where
     the use case itself is wrong, it is corrected here. Where the application model lacks what the
     entry needs, the entry stays as the goal needs it, and nothing is written here: the section
     says who writes that down.

   The skill writes nothing into `<tree>/09_application_model/`.
7. **What a change makes stale.** When the use case changes after anything downstream was made from
   it, `python3 tools/kit.py stale 06 <tree>/06_use_cases/<the use case's identifier>/06_use_case.md`
   in the kit's root lists what the change makes stale, from what each artifact made from this one
   records it was made from, and changes nothing.

## Render

The reader's edition is the Word document the owner reviews. It is a build (`SDD-01` §14,
rule 1), put to the owner as the ruling of 25 September 2026 on the owner's reading fixes; the
skill reads that ruling at `<standards>/rulings/2026-09-25-the-owner-reviews-a-polished-document.yaml`
and does not restate it.

1. Write the edition's source from the use case, in the register that ruling fixes, at
   `<tree>/06_use_cases/<the use case's identifier>/_reader/06_use_case_reader.md`. The explanation
   of each word the use case uses is read from the entity model and its glossary, which own those
   words, at the moment of writing. The source is written again from the use case whenever it
   changes, and is never corrected in its own right.
2. A figure is drawn by a program kept in `<tree>/_machinery/`, and the picture it draws is kept
   beside the source and referenced from it.
3. Build the Word document with pandoc, the document converter, found with `command -v pandoc`:

       pandoc <tree>/06_use_cases/<the use case's identifier>/_reader/06_use_case_reader.md --from markdown --to docx --resource-path <tree>/06_use_cases/<the use case's identifier>/_reader --output <tree>/_reviews/06_use_case_<the use case's identifier>.docx

   Where pandoc is not found, the build could not run, and the skill says so.
4. The Word document is never edited. A correction goes into the use case, the source is written
   again from it, and the document is built again. The owner's acceptance is written into the use
   case, below the comment at its head, naming who accepted it and when, and the edition is built
   again from it.

## Where this skill stops

At the moment the standard, the register, the upstream things and the person's own material
together do not settle something the use case needs. `SDD-01` §14, rule 5 governs that moment; it
is cited here and not restated. The machine steps are these:

1. One file is written into `<tree>/_findings/`, naming what was missing, where the use case needed
   it, and who is to answer it.
2. Where the standard itself could not be followed, was ambiguous or was silent, the same is
   written into `<tree>/_amendments/`.
3. The skill carries on with the parts the gap does not touch, and stops the moment when none
   remain.

It also stops before the first moment when the model holds no record for the goal, or gives it
another form; when the staleness check reads behind; and when a program it runs refuses
something: `SDD-01` §14, rule 11.

## What this skill never holds

- No words of any rule of any standard, and no line of any standard's template. A rule is named by
  its identifier and no more, and this file names none.
- No edition of its standard anywhere but the pin.
- No engagement: no engagement's name, path or terms. An engagement's own skill for its use cases
  stays the engagement's.
- No figure read from a standard, such as a count of rules, fields, steps or checks. It is read at
  run time.

## The fixture test

The fixture is `examples/fixture/06_use_case.md`: the template copied by the prepare moment and
filled for one goal, Renew a loan, of the loans module of a fictitious lending library, which
belongs to no engagement. Beside it, `examples/fixture/_conformance/06_use_case.md_verdicts.yaml`
holds the answer to each rule of the checklist, under a head naming the model and the declared
departures, and `examples/fixture/_conformance/06_use_case.md_conformance.md` is the claim
`kit conform` wrote over it. In the kit's root:

    python3 tools/kit.py conform 06 ../skills/use-case-description/examples/fixture/06_use_case.md
    python3 tools/kit.py skills --check

It passes when the first exits 0 and writes a claim naming every rule of the checklist with a
verdict, so that its count of rules equals the checklist's, and the second prints this skill as
current.

## Where the pieces live

| The piece | Where it is |
|---|---|
| the standards root, `<standards>` | `standards/`, in this skill's folder |
| the kit's root, `<kit>` | `kit/`, in this skill's folder |
| the standard | the document whose name begins `SDD-06_` in `<standards>`, as `kit slot 06` resolves it |
| the method's standard, for the header first and the declared departures | the document whose name begins `SDD-01_` in `<standards>` |
| the register's row | row `06` of `<kit>/templates/spec/slots.yaml`, read with `kit slot 06` |
| the template | `<kit>/templates/spec/artefacts/06_use_case.md` |
| the checklist | `<kit>/templates/spec/checklists/SDD-06.md` |
| the programs | `<kit>/tools/kit.py`, with the verbs `slot`, `conform`, `skills --check` and `stale` |
| the ruling on the reader's edition | `<standards>/rulings/2026-09-25-the-owner-reviews-a-polished-document.yaml` |
| the specification tree, `<tree>` | the folder `kit spec new` made for the system |
| the use case | `<tree>/06_use_cases/<the use case's identifier>/06_use_case.md` |
| its verdicts and its claim | `<tree>/06_use_cases/<the use case's identifier>/_conformance/` |
| the edition's source | `<tree>/06_use_cases/<the use case's identifier>/_reader/` |
| the upstream things | `<tree>/03_use_case_model/`, `<tree>/01_requirements_register/`, `<tree>/02_entity_model/`, `<tree>/05_shared_groundwork/` |
| the downstream thing it is read against, never written | `<tree>/09_application_model/` |
| findings and amendments | `<tree>/_findings/` and `<tree>/_amendments/` |
| the reader's edition | `<tree>/_reviews/06_use_case_<the use case's identifier>.docx` |
| the form this skill is written from | `references/SKILL-form.md` in this plugin |
| the fixture | `examples/fixture/` in this skill |
