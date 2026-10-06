---
name: interaction-design
description: >-
  Helps a person write the interaction design of an application under the standard SDD-11, The
  Interaction Design, which is a draft: how a person picks a coded value, finds one record among
  many, moves a record from one state to the next and acts on a record, settled once for the goals
  one writing of the application model carries, from their accepted screen records, and accepted
  by the owner before the model is written. It prepares the document from the kit's template and
  produces its four listings from the accepted screen records by a program, each compared as a
  set with a second reading of the records; walks the person through the standard's questions
  and decision tables read at the moment of use; checks the document with the kit's own reader
  and writes the claim of conformance rule by rule with kit conform; and builds the reader's
  edition the owner accepts. It holds no rule of the standard; it reads every rule where the
  standard states it.
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
standard: SDD-11
written_against: {edition: "0.1", sha256: "24ad9b91baaa5f5aa134a1b457107a4339ee12a2b312d0b6ccabf82e62bb7cd2"}
---

# interaction-design

**Written to a draft.** The standard this skill serves stood as a draft when the skill was
written against it (the pin above). At the start of every use the skill reads the standard's
standing from its first page and tells the person, in the standard's own words; it enforces
nothing on a draft's authority beyond what the draft says of itself.

## What this skill is for

It helps a person write the interaction design of an application: one document for the goals one
writing of its application model carries, read from the screen records the owner accepted, and
accepted by the owner before the model is written. The standard is `SDD-11`, The Interaction
Design, the document whose name begins `SDD-11_` in the standards root,
`standards/`. The register's row for the thing is
`08a`. Everything the skill needs to know about the thing it reads, at the moment it runs, from
that row, from the standard and from the kit's template of the document; what it holds is only
the steps that need a machine, and one program, `scripts/listings.py`, which produces the four
listings.

## Before the first moment

In the kit's root, `kit/` in this skill's folder:

    python3 tools/kit.py skills --check
    python3 tools/kit.py slot 08a

1. **The staleness check.** Read this skill's line, `sdd-kit/interaction-design`, in what
   `kit skills --check` prints. Where it reads behind, or pinned to a document not in the root,
   the skill stops and says so: `SDD-01` §14, rule 11. Where the program cannot be run, the skill
   says that the check could not be run and does not treat itself as current.
2. **The row.** From what `kit slot 08a` prints, take the document it was read out of, the
   standing, the sections named as the form, the template, the checklist, the seams, the line
   saying who writes the thing and who accepts it, the moment it is written, and the row's notes.
3. **A draft says so.** Where the row gives the standing as a draft, the skill reads the line of
   the standard's first page that states its version and standing, and tells the person at the
   start in those words. It enforces nothing on the draft's authority beyond what the draft says
   of itself.

## Prepare

1. The specification tree, `<tree>`, is the folder `kit spec new` made for the system. The thing's
   folder in it is `<tree>/08a_interaction_design/`, and the application's own programs are kept in
   `<tree>/_machinery/`.
2. **The goals.** The person names the goals the increment of the model carries. For each, its
   description and its screen record stand in the tree's folders the row's incoming seams name.
   What the standard requires of a goal before it enters the step is read from the standard and
   from the row's `when` line; the listing program refuses a screen record that does not stand
   accepted, and the skill says which record it refused.
3. **The upstream things.** For each other incoming seam the row prints (the lines beginning
   `<-`), confirm that the upstream thing stands in its folder of the tree. Where one does not,
   the skill stops at this moment. Nothing is written into an upstream thing's folder, at this
   moment or at any other.
4. **The document.** Copy the kit's template the row names, and remove from the copy the section
   the template marks as its own and asks to be deleted, keeping every heading below it as it
   stands:

       cp <kit>/templates/spec/INTERACTION_DESIGN.md.tmpl <tree>/08a_interaction_design/INTERACTION_DESIGN.md

   The removed section says what the kit's gate reads in each part of the document; it stays in
   the kit's template, and the skill reads it there whenever the assist moment needs it.
5. **The listing program, kept with the application's programs.** Copy this skill's program into
   the application's programs, once; an increment after the first uses the copy already there:

       cp <this skill>/scripts/listings.py <tree>/_machinery/listings.py

   Beside it the application keeps `<tree>/_machinery/screen_record_form.yaml`, which says how the
   application's screen records are written: the program reads the records only through that
   file. It is written once, with the person, from the records themselves; what each of its keys
   means is written at the head of the program (`python3 <tree>/_machinery/listings.py --help`),
   and `examples/fixture/screen_record_form.yaml` is a filled one.
6. **The four listings.** In the tree's root:

       python3 _machinery/listings.py --form _machinery/screen_record_form.yaml --appendix 08a_interaction_design/INTERACTION_DESIGN.md <the accepted screen record of each goal>

   It refuses, and writes nothing, when a record does not stand accepted. Otherwise it writes the
   four listings, and their comparison as sets with a second reading of the records, into the
   document's appendix, and names itself and the form file, by path and checksum, in the header's
   row for the program of the listings. It exits 1 when a comparison is not equal or a row could
   not be read; what it prints names each entry, and what is corrected is the form file or the
   record's own table, never the listing. A refusal is answered, not worked around: `SDD-01` §14,
   rule 11.

## Assist

1. Extract the standard's text, in the kit's root, from the document `kit slot 08a` was read out
   of, with the kit's own reader, the one `kit slot` reads the edition with. The text is read into
   the session and is not saved into the tree:

       python3 -B -c 'import sys, pathlib; sys.path.insert(0, "tools"); import slot; print(slot.Document(pathlib.Path(sys.argv[1])).text)' "<the document>"

2. Open, in that text, the sections the row names as the form and its questions, and walk the
   person through them in the order the standard gives them. The document's parts and the
   headings of its decision tables are those of the copied template, which the kit fixes for its
   gate; they are never retyped or renamed.
3. For each entry of each listing in the appendix, the person writes the row the standard asks
   for, in the decision table the template gives it. How a row names the construct of the
   application model it governs, and which words the gate reads in each column, are read from the
   template's own section in the kit at that moment.
4. Where the standard says an answer is read from an upstream document, the skill reads it there.
   Where that document is silent or disagrees, the skill records a finding (*Where this skill
   stops*, below).
5. What the document records where the goals are silent is read from the standard; the skill
   writes it in the part of the document the template gives for it, in the person's words.
6. Who proposes and who decides at this moment is the row's line on who writes the thing and who
   accepts it, read from `kit slot 08a`, and not this file.

## Check

1. **The listings again.** Run the listing program as the prepare moment ran it. It makes each
   listing by one reading of the records and compares it, as a set, with the same listing made by
   a second reading, which calls none of the program's functions that the first calls and reads
   the form's words in the records without regard to case, to backticks and asterisks, or to runs
   of white space. It exits 0 only when every listing equals the second reading's as a set, and
   exits 1 naming each entry the two do not share; how each reading reads is written at the head
   of the program (`python3 <tree>/_machinery/listings.py --help`).

   **What the comparison does not see.** Both readings take the application's form file as the
   only statement of what makes a value a coded value, a reference or a record's state, so a value
   whose cell says so in other words than the form's is left out of the listing by both, and the
   comparison is equal. For that reason the program prints, on every run, each value it placed in
   no listing. The person reads each of them against the four listings; where one belongs to a
   listing, the record's cell or the form file is corrected, never the listing, and the program is
   run again.
2. **The gate's reading.** In the kit's root, the kit's own reader of an interaction design prints
   what the kit's gate will read in the document — its status, who accepted it and when, the goals
   it covers, and each decision table with its rows — and every line it could not read:

       python3 -B tools/interaction_design.py <tree>/08a_interaction_design/INTERACTION_DESIGN.md

   A line it could not read is corrected in the document. The gate itself is the kit's, run on the
   application model when the model names this document; this skill does not run it.
3. **The verdicts.** Read the rules from the table under `## Rules` in the checklist the row names,
   `<kit>/templates/spec/checklists/SDD-11.md`. Put each rule to the person, by its identifier and
   the words the checklist gives it, and write the person's answer into
   `<tree>/08a_interaction_design/_conformance/INTERACTION_DESIGN.md_verdicts.yaml`, one entry for
   each rule, in the form `kit conform` reads (`python3 tools/kit.py conform --help`): the rule,
   then `met`, `not met` or `not applicable`; and, only where the checklist's `program` column names
   a program for that rule and that program was run, the program as the entry's `check`. The skill
   writes no verdict of its own.
4. **The claim.** In the kit's root:

       python3 tools/kit.py conform 08a <tree>/08a_interaction_design/INTERACTION_DESIGN.md

   Exit 0: it wrote the claim beside the document, in its `_conformance/` folder, one line for each
   rule of the checklist. Exit 1: it refused and wrote nothing; each refusal it prints names a rule,
   and what is corrected is the person's answer, never the program or the checklist. Exit 2: it
   could not run, which is said as such.
5. **The person's half.** The questions under the checklist's heading `Gate — the person's half`
   are put to the person one at a time, read from the checklist. An answer that shows something
   missing is a finding.
6. **What a change makes stale.** When the document changes after anything downstream was made
   from it, `python3 tools/kit.py stale 08a <tree>/08a_interaction_design/INTERACTION_DESIGN.md`
   in the kit's root lists what the change makes stale, and changes nothing. What follows a change
   to a document the owner has accepted is read from the standard.

## Render

The reader's edition is the Word document the owner accepts. It is a build (`SDD-01` §14,
rule 1), put to the owner as the ruling of 25 September 2026 on the owner's reading fixes; the
skill reads that ruling at `<standards>/rulings/2026-09-25-the-owner-reviews-a-polished-document.yaml`
and does not restate it. Which parts of the document the owner reads is read from the standard at
the moment of writing.

1. Write the edition's source from the document, in the register that ruling fixes, at
   `<tree>/08a_interaction_design/_reader/INTERACTION_DESIGN_reader.md`. The explanation of each
   term it uses is read from the standard's own section defining its words, at the moment of
   writing. The source is written again from the document whenever the document changes, and is
   never corrected in its own right.
2. The pages the document shows, and every figure, are produced by a program kept in
   `<tree>/_machinery/`; this skill carries none. Where the application has none, that is recorded
   as a finding with the application's analyst as its owner.
3. Build the Word document with pandoc, the document converter, found with `command -v pandoc`:

       pandoc <tree>/08a_interaction_design/_reader/INTERACTION_DESIGN_reader.md --from markdown --to docx --resource-path <tree>/08a_interaction_design/_reader --output <tree>/_reviews/INTERACTION_DESIGN.docx

   Where pandoc is not found, the build could not run, and the skill says so.
4. The Word document is never edited. A correction goes into the document, the source is written
   again from it, and the edition is built again. The owner's acceptance is written into the
   document's header, in the row for its version and status, naming who accepted it and when, in
   the words the kit's reader prints; and the edition is built again from it.

## Where this skill stops

At the moment the standard, the register, the template, the upstream things and the person's own
material together do not settle something the document needs. `SDD-01` §14, rule 5 governs that
moment; it is cited here and not restated. The machine steps are these:

1. One file is written into `<tree>/_findings/`, naming what was missing, where the document
   needed it, the document that owns the fact, and who is to answer it.
2. Where the standard itself could not be followed, was ambiguous or was silent, the same is
   written into `<tree>/_amendments/`.
3. The skill carries on with the parts the gap does not touch, and stops the moment when none
   remain.

It also stops when the staleness check reads behind, and when a program it runs refuses
something: `SDD-01` §14, rule 11.

## What this skill never holds

- No words of any rule of any standard, and no line of any standard's form. A rule is named by its
  identifier and no more, and this file names none.
- No edition of its standard anywhere but the pin.
- No engagement: no engagement's name, path or terms.
- No figure read from a standard, such as a count of rules, parts, tables or checks. It is read at
  run time.
- None of what every application is given without design: the kit and the house rules for what a
  person sees hold that, and the standard says where.

## The fixture test

The fixture is the interaction design of the lending desk application of the library of a town
called Eastbrook, which does not exist and belongs to no engagement. Its two accepted screen
records are `examples/fixture/screens/UC-LD-01.md` and `examples/fixture/screens/UC-LD-02.md`,
written in the form `examples/fixture/screen_record_form.yaml` declares;
`examples/fixture/listings_expected.yaml` holds the four listings written out by reading the
records by eye. The document is `examples/fixture/INTERACTION_DESIGN.md`, whose appendix and whose
header row for the program were written by `scripts/listings.py`; beside it,
`examples/fixture/_conformance/INTERACTION_DESIGN.md_verdicts.yaml` holds the answer to each rule
of the checklist, and `examples/fixture/_conformance/INTERACTION_DESIGN.md_conformance.md` is the
claim `kit conform` wrote over it.

In this skill's folder, the listings, each compared as a set with the second reading of the
records and with the listings written out by eye; it writes nothing:

    python3 scripts/listings.py --form examples/fixture/screen_record_form.yaml --expect examples/fixture/listings_expected.yaml examples/fixture/screens/UC-LD-01.md examples/fixture/screens/UC-LD-02.md

In the kit's root:

    python3 -B tools/interaction_design.py ../skills/interaction-design/examples/fixture/INTERACTION_DESIGN.md
    python3 tools/kit.py conform 08a ../skills/interaction-design/examples/fixture/INTERACTION_DESIGN.md
    python3 tools/kit.py skills --check

It passes when the listing program exits 0 with every comparison equal as sets, the kit's reader
reads the document's status, goals and decision tables and prints no line it could not read,
`kit conform` exits 0 and writes a claim naming every rule of the checklist with a verdict, so
that its count of rules equals the checklist's, and `kit skills --check` prints this skill as
current.

## Where the pieces live

| The piece | Where it is |
|---|---|
| the standards root, `<standards>` | `standards/`, in this skill's folder |
| the kit's root, `<kit>` | `kit/`, in this skill's folder |
| the standard | the document whose name begins `SDD-11_` in `<standards>`, as `kit slot 08a` resolves it |
| the register's row | row `08a` of `<kit>/templates/spec/slots.yaml`, read with `kit slot 08a` |
| the template | `<kit>/templates/spec/INTERACTION_DESIGN.md.tmpl` |
| the checklist | `<kit>/templates/spec/checklists/SDD-11.md` |
| the kit's reader of the document | `<kit>/tools/interaction_design.py` |
| the programs | `<kit>/tools/kit.py`, with the verbs `slot`, `conform`, `skills --check` and `stale` |
| the listing program | `scripts/listings.py` in this skill; its copy in `<tree>/_machinery/` |
| the application's form of its screen records | `<tree>/_machinery/screen_record_form.yaml` |
| the ruling on the reader's edition | `<standards>/rulings/2026-09-25-the-owner-reviews-a-polished-document.yaml` |
| the specification tree, `<tree>` | the folder `kit spec new` made for the system |
| the document | `<tree>/08a_interaction_design/INTERACTION_DESIGN.md` |
| its verdicts and its claim | `<tree>/08a_interaction_design/_conformance/` |
| the edition's source | `<tree>/08a_interaction_design/_reader/` |
| the upstream things | the folders of the tree the row's incoming seams name |
| findings and amendments | `<tree>/_findings/` and `<tree>/_amendments/` |
| the reader's edition | `<tree>/_reviews/INTERACTION_DESIGN.docx` |
| the form this skill is written from | `references/SKILL-form.md` in this plugin |
| the fixture | `examples/fixture/` in this skill |
