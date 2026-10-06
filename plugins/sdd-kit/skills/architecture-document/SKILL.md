---
name: architecture-document
description: >-
  Helps a person write the software architecture specification of one application under the
  standard SDD-08, The Software Architecture Document: what the application is
  built on — the platform it is bound to, the components it switches on, the machinery that runs
  its processes, everything that crosses its boundary, and the code written specially. It
  prepares the specification from the template the standard's build produces, walks the person
  through the standard's own form read from the document at the moment of use, writes the claim
  of conformance rule by rule with kit conform, and builds the reader's edition the owner reviews.
  Use it when an application's architecture is to be specified, checked or brought up to date
  before its application model is written. It holds no rule of the standard; it reads every rule
  where the standard states it.
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
standard: SDD-08
written_against: {edition: "1.0", sha256: "762846a7ae4bcc3d041cc04194a987c8cab1845c2e51e9aa08f57775ea6aba5f"}
---

# architecture-document

## What this skill is for

It helps a person write the software architecture specification of one application: what the
application is built on, stated so that whoever writes the application model, and the software
that generates the application from it, can use it. The standard is `SDD-08`, The Software
Architecture Document, the document whose name begins `SDD-08_` in the standards root,
`standards/`. The register's row for the thing
is `04`. Everything the skill needs to know about the thing it reads, at the moment it runs, from
that row and from the standard; what it holds is only the steps that need a machine.

## Before the first moment

In the kit's root, `kit/` in this skill's folder:

    python3 tools/kit.py skills --check
    python3 tools/kit.py slot 04

1. **The staleness check.** Read this skill's line, `sdd-kit/architecture-document`, in what
   `kit skills --check` prints. Where it reads behind, or pinned to a document not in the root,
   the skill stops and says so: `SDD-01` §14, rule 11. Where the program cannot be run, the skill
   says that the check could not be run and does not treat itself as current.
2. **The row.** From what `kit slot 04` prints, take the document it was read out of, the
   standing, the section named as the form, the template, the checklist, the seams, the line
   saying who writes the thing, and the row's notes.
3. **A draft says so.** Where the row gives the standing as a draft, the skill reads the line of
   the standard's first page that states its version and standing, and tells the person at the
   start in those words. It enforces nothing on the draft's authority beyond what the draft says
   of itself.
4. **What must be settled first.** Where the row's notes say that something is a decision for the
   owner before the thing is begun, the skill puts it to the person before preparing, and stops
   if it is not settled (*Where this skill stops*, below).

## Prepare

1. The specification tree, `<tree>`, is the folder `kit spec new` made for the system. The thing's
   folder in it is `<tree>/04_architecture/`.
2. Copy the template the row names into that folder, keeping its name:

       cp <kit>/templates/spec/artefacts/04_architecture.md <tree>/04_architecture/

   The comment at the head of the copy names the edition and the checksum of the document the
   template was produced from. It stays as the record of what the specification is written to,
   and it is never edited.
3. For each incoming seam the row prints (the lines beginning `<-`), confirm that the upstream
   thing stands in its folder of the tree, and read its version from its own header; the
   specification records each version it read, in the line of the form the seam's `declared at`
   names. Where an upstream thing does not stand there, the skill stops at this moment.
4. Nothing is written into an upstream thing's folder, at this moment or at any other.

## Assist

1. Extract the standard's text, in the kit's root, from the document `kit slot 04` was read out
   of, with the kit's own reader, the one `kit slot` reads the edition with. The text is read
   into the session and is not saved into the tree:

       python3 -B -c 'import sys, pathlib; sys.path.insert(0, "tools"); import slot; print(slot.Document(pathlib.Path(sys.argv[1])).text)' "<the document>"

2. Open, in that text, the section the row names as the form, and walk the person through its
   parts in the order the standard gives them. Each part's heading says whether its table is
   filled once, or once for each thing of its kind; the skill copies the part's table in the
   artifact once for each such thing, each copy under a heading of its own naming the thing.
   Where the form asks for something once beside a table rather than in it, the skill writes it
   where the form says.
3. Read each line from the standard's text as it is reached: its name, what the standard says to
   write, and the rule it names. Put the line to the person. The skill may propose an answer from
   the upstream things and the person's own material; it writes into the line's last column only
   what the person accepts, in the person's words. A line with nothing to record carries the
   written reason, never an empty cell.
4. The things the form is filled once for each of — components, processes, crossings, bespoke
   entries — are listed with the person from the upstream things and their own material. Where
   the standard or the row says that no document publishes such a list, the skill records that
   as a finding and carries on with the list the person gives.
5. Who proposes and who decides at this moment is the row's line on who writes the thing, read
   from `kit slot 04`, and not this file.
6. No credential is ever written into the artifact; where one is needed, the place it is kept is
   named and nothing else.

## Check

1. **The verdicts.** Read the rules from the table under `## Rules` in the checklist the row names,
   `<kit>/templates/spec/checklists/SDD-08.md`. Put each rule to the person, by its identifier and
   the words the checklist gives it, and write the person's answer into
   `<tree>/04_architecture/_conformance/04_architecture.md_verdicts.yaml`, one entry for each rule,
   in the form `kit conform` reads (`python3 tools/kit.py conform --help`): the rule, then `met`,
   `not met` or `not applicable`; and, only where the checklist's `program` column names a program
   for that rule and that program was run, the program as the entry's `check`. The skill writes
   no verdict of its own.
2. **The claim.** In the kit's root:

       python3 tools/kit.py conform 04 <tree>/04_architecture/04_architecture.md

   Exit 0: it wrote the claim beside the artifact, in its `_conformance/` folder, one line for each
   rule of the checklist. Exit 1: it refused and wrote nothing; each refusal it prints names a
   rule, and what is corrected is the person's answer, never the program or the checklist. Exit 2:
   it could not run, which is said as such.
3. **The person's half.** The questions under the checklist's heading `Gate — the person's half`
   are put to the person one at a time, read from the checklist. An answer that shows something
   missing is a finding (*Where this skill stops*, below).
4. **The program's half.** The checklist's heading `Gate — the program's half` says which checks a
   program performs and whether any has been built. The skill runs only a program the checklist's
   `program` column names and the kit holds, and reports no result of any check that does not
   exist.
5. **What a change makes stale.** When the specification changes after anything downstream was
   made from it, `python3 tools/kit.py stale 04 <tree>/04_architecture/04_architecture.md` in the
   kit's root lists what the change makes stale, and changes nothing.

## Render

The reader's edition is the Word document the owner reviews. It is a build (`SDD-01` §14,
rule 1), put to the owner as the ruling of 25 September 2026 on the owner's reading fixes; the
skill reads that ruling at `<standards>/rulings/2026-09-25-the-owner-reviews-a-polished-document.yaml`
and does not restate it.

1. Write the edition's source from the artifact, in the register that ruling fixes, at
   `<tree>/04_architecture/_reader/04_architecture_reader.md`. The explanation of each term it
   uses is read from the standard's own section defining its words, at the moment of writing. The
   source is written again from the artifact whenever the artifact changes, and is never corrected
   in its own right.
2. A figure is drawn by a program kept in `<tree>/_machinery/`, and the picture it draws is kept
   beside the source and referenced from it.
3. Build the Word document with pandoc, the document converter, found with `command -v pandoc`:

       pandoc <tree>/04_architecture/_reader/04_architecture_reader.md --from markdown --to docx --resource-path <tree>/04_architecture/_reader --output <tree>/_reviews/04_architecture.docx

   Where pandoc is not found, the build could not run, and the skill says so.
4. The Word document is never edited. A correction goes into the artifact, the source is written
   again from it, and the document is built again. The owner's acceptance is written into the
   artifact, below the comment at its head, naming who accepted it and when, and the edition is
   built again from it.

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

It also stops when the staleness check reads behind, and when a program it runs refuses
something: `SDD-01` §14, rule 11.

## What this skill never holds

- No words of any rule of any standard, and no line of any standard's form. A rule is named by its
  identifier and no more, and this file names none.
- No edition of its standard anywhere but the pin.
- No engagement: no engagement's name, path or terms.
- No figure read from a standard, such as a count of rules, parts or checks. It is read at run
  time.

## The fixture test

The fixture is `examples/fixture/04_architecture.md`: the template copied by the prepare moment and
filled for the lending desk application of the library of a town called Eastbrook, which does not
exist and belongs to no engagement. Beside it,
`examples/fixture/_conformance/04_architecture.md_verdicts.yaml` holds the answer to each rule of
the checklist, and `examples/fixture/_conformance/04_architecture.md_conformance.md` is the claim
`kit conform` wrote over it. In the kit's root:

    python3 tools/kit.py conform 04 ../skills/architecture-document/examples/fixture/04_architecture.md
    python3 tools/kit.py skills --check

It passes when the first exits 0 and writes a claim naming every rule of the checklist with a
verdict, so that its count of rules equals the checklist's, and the second prints this skill as
current.

## Where the pieces live

| The piece | Where it is |
|---|---|
| the standards root, `<standards>` | `standards/`, in this skill's folder |
| the kit's root, `<kit>` | `kit/`, in this skill's folder |
| the standard | the document whose name begins `SDD-08_` in `<standards>`, as `kit slot 04` resolves it |
| the register's row | row `04` of `<kit>/templates/spec/slots.yaml`, read with `kit slot 04` |
| the template | `<kit>/templates/spec/artefacts/04_architecture.md` |
| the checklist | `<kit>/templates/spec/checklists/SDD-08.md` |
| the programs | `<kit>/tools/kit.py`, with the verbs `slot`, `conform`, `skills --check` and `stale` |
| the ruling on the reader's edition | `<standards>/rulings/2026-09-25-the-owner-reviews-a-polished-document.yaml` |
| the specification tree, `<tree>` | the folder `kit spec new` made for the system |
| the artifact | `<tree>/04_architecture/04_architecture.md` |
| its verdicts and its claim | `<tree>/04_architecture/_conformance/` |
| the edition's source | `<tree>/04_architecture/_reader/` |
| the upstream things | the folders of the tree the row's incoming seams name |
| findings and amendments | `<tree>/_findings/` and `<tree>/_amendments/` |
| the reader's edition | `<tree>/_reviews/04_architecture.docx` |
| the form this skill is written from | `references/SKILL-form.md` in this plugin |
| the fixture | `examples/fixture/` in this skill |
