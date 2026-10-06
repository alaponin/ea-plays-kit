---
name: shared-registers
description: >-
  Helps a person write the shared registers of one module under the standard SDD-04, The Shared
  Registers: what makes two rows the same thing, who writes each fact, the states a record moves
  through, and the catalogues of events, computations, shared code lists and settings beside them.
  It prepares the register from the template the standard's build produces, walks the person
  through the standard's own form read from the document at the moment of use, writes the claim of
  conformance rule by rule with kit conform, and builds the reader's edition the owner reviews. Use
  it when a module's shared registers are to be written, checked or brought up to date. It holds no
  rule of the standard; it reads every rule where the standard states it.
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
standard: SDD-04
written_against: {edition: "1.0", sha256: "d167b5047937ff382d59d5297ed8c2b158e4e61e132c8b7cd9092862ee3592ef"}
---

# shared-registers

## What this skill is for

It helps a person write the rest of the shared groundwork of one module: the register that says
what makes two rows the same thing, who writes each fact and the states a record moves through,
with the catalogues of events, computations, shared code lists and settings beside it. The
standard is `SDD-04`, The Shared Registers, the document whose name begins `SDD-04_` in the
standards root, `standards/`. The register's row
for the thing is `05`. Everything the skill needs to know about the thing it reads, at the moment
it runs, from that row and from the standard; what it holds is only the steps that need a machine.

## Before the first moment

In the kit's root, `kit/` in this skill's folder:

    python3 tools/kit.py skills --check
    python3 tools/kit.py slot 05

1. **The staleness check.** Read this skill's line, `sdd-kit/shared-registers`, in what
   `kit skills --check` prints. Where it reads behind, or pinned to a document not in the root,
   the skill stops and says so: `SDD-01` §14, rule 11. Where the program cannot be run, the skill
   says that the check could not be run and does not treat itself as current.
2. **The row.** From what `kit slot 05` prints, take the document it was read out of, the
   standing, the section named as the form, the template, the checklist, the seams, and the line
   saying who writes the thing.
3. **A draft says so.** Where the row gives the standing as a draft, the skill tells the person at
   the start, in the words of the standard's own first page read from the document, and enforces
   nothing on the draft's authority beyond what the draft says of itself.

## Prepare

1. The specification tree, `<tree>`, is the folder `kit spec new` made for the system. The thing's
   folder in it is `<tree>/05_shared_groundwork/`.
2. Copy the template the row names into that folder, keeping its name:

       cp <kit>/templates/spec/artefacts/05_shared_registers.md <tree>/05_shared_groundwork/

   The comment at the head of the copy names the edition and the checksum of the document the
   template was produced from. It stays as the record of what the register is written to, and it
   is never edited.
3. For each incoming seam the row prints, confirm that the upstream thing stands in its folder of
   the tree, at the version the register will cite for it. For this row that is the entity model,
   in `<tree>/02_entity_model/`. Where it does not stand there, the skill stops at this moment
   (*Where this skill stops*, below).
4. Nothing is written into an upstream thing's folder, at this moment or at any other.

## Assist

1. Extract the standard's text, in the kit's root, from the document `kit slot 05` was read out
   of, with the kit's own reader, the one `kit slot` reads the edition with. The text is read
   into the session and is not saved into the tree:

       python3 -B -c 'import sys, pathlib; sys.path.insert(0, "tools"); import slot; print(slot.Document(pathlib.Path(sys.argv[1])).text)' "<the document>"

2. Open, in that text, the section the row names as the form, and walk the person through its
   parts in the order the standard gives them. Each part's heading says what one copy of its table
   stands for. The skill copies the part's table in the artifact once for each such thing the
   module has, each copy under a heading of its own naming the thing.
3. Read each line from the standard's text as it is reached: its name, what the standard says to
   write, and the rule it names. Put the line to the person. The skill may propose an answer from
   the material the person has given it; it writes into the line's last column only what the
   person accepts, in the person's words.
4. Who proposes and who decides at this moment is the row's line on who writes the thing, read
   from `kit slot 05`, and not this file.
5. Where a line asks for something another thing of the specification holds, such as a row of the
   entity model or an actor of the use case model, the skill reads it from its folder in the tree
   and cites it by its place there.

## Check

1. **The verdicts.** Read the rules from the table under `## Rules` in the checklist the row names,
   `<kit>/templates/spec/checklists/SDD-04.md`. Put each rule to the person, by its identifier and
   the words the checklist gives it, and write the person's answer into
   `<tree>/05_shared_groundwork/_conformance/05_shared_registers.md_verdicts.yaml`, one entry for
   each rule, in the form `kit conform` reads (`python3 tools/conform.py --help`): the rule,
   then `met`, `not met` or `not applicable`; and, only where the checklist's `program` column
   names a program for that rule and that program was run, the program as the entry's `check`. The
   skill writes no verdict of its own.
2. **The claim.** In the kit's root:

       python3 tools/kit.py conform 05 <tree>/05_shared_groundwork/05_shared_registers.md

   Exit 0: it wrote the claim beside the artifact, in its `_conformance/` folder, one line for
   each rule of the checklist. Exit 1: it refused and wrote nothing; each refusal it prints names a
   rule, and what is corrected is the person's answer, never the program or the checklist. Exit 2:
   it could not run, which is said as such.
3. **The person's half.** The questions under the checklist's heading `Gate — the person's half`
   are put to the person one at a time, read from the checklist. An answer that shows something
   missing is a finding (*Where this skill stops*, below).
4. **The program's half.** The skill runs only a program the checklist's `program` column names,
   and reports no result of any check the kit does not hold.
5. **What a change makes stale.** When the register changes after anything downstream was made
   from it, `python3 tools/kit.py stale 05 <tree>/05_shared_groundwork/05_shared_registers.md` in
   the kit's root lists what the change makes stale, from what each artifact made from this one
   records it was made from, and changes nothing.

## Render

The reader's edition is the Word document the owner reviews. It is a build (`SDD-01` §14,
rule 1), put to the owner as the ruling of 25 September 2026 on the owner's reading fixes; the
skill reads that ruling at `<standards>/rulings/2026-09-25-the-owner-reviews-a-polished-document.yaml`
and does not restate it.

1. Write the edition's source from the artifact, in the register that ruling fixes, at
   `<tree>/05_shared_groundwork/_reader/05_shared_registers_reader.md`. The explanation of each
   term it uses is read from the standard's own section defining its words, at the moment of
   writing. The source is written again from the artifact whenever the artifact changes, and is
   never corrected in its own right.
2. A figure is drawn by a program kept in `<tree>/_machinery/`, and the picture it draws is kept
   beside the source and referenced from it.
3. Build the Word document with pandoc, the document converter, found with `command -v pandoc`:

       pandoc <tree>/05_shared_groundwork/_reader/05_shared_registers_reader.md --from markdown --to docx --resource-path <tree>/05_shared_groundwork/_reader --output <tree>/_reviews/05_shared_registers.docx

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

The fixture is `examples/fixture/05_shared_registers.md`: the template copied by the prepare
moment and filled for the loans module of a fictitious lending library, which belongs to no
engagement. Beside it, `examples/fixture/_conformance/05_shared_registers.md_verdicts.yaml` holds
the answer to each rule of the checklist, and
`examples/fixture/_conformance/05_shared_registers.md_conformance.md` is the claim `kit conform`
wrote over it. In the kit's root:

    python3 tools/kit.py conform 05 ../skills/shared-registers/examples/fixture/05_shared_registers.md
    python3 tools/kit.py skills --check

It passes when the first exits 0 and writes a claim naming every rule of the checklist with a
verdict, so that its count of rules equals the checklist's, and the second prints this skill as
current.

## Where the pieces live

| The piece | Where it is |
|---|---|
| the standards root, `<standards>` | `standards/`, in this skill's folder |
| the kit's root, `<kit>` | `kit/`, in this skill's folder |
| the standard | the document whose name begins `SDD-04_` in `<standards>`, as `kit slot 05` resolves it |
| the register's row | row `05` of `<kit>/templates/spec/slots.yaml`, read with `kit slot 05` |
| the template | `<kit>/templates/spec/artefacts/05_shared_registers.md` |
| the checklist | `<kit>/templates/spec/checklists/SDD-04.md` |
| the programs | `<kit>/tools/kit.py`, with the verbs `slot`, `conform`, `skills --check` and `stale` |
| the ruling on the reader's edition | `<standards>/rulings/2026-09-25-the-owner-reviews-a-polished-document.yaml` |
| the specification tree, `<tree>` | the folder `kit spec new` made for the system |
| the artifact | `<tree>/05_shared_groundwork/05_shared_registers.md` |
| its verdicts and its claim | `<tree>/05_shared_groundwork/_conformance/` |
| the edition's source | `<tree>/05_shared_groundwork/_reader/` |
| the upstream thing | `<tree>/02_entity_model/` |
| findings and amendments | `<tree>/_findings/` and `<tree>/_amendments/` |
| the reader's edition | `<tree>/_reviews/05_shared_registers.docx` |
| the form this skill is written from | `references/SKILL-form.md` in this plugin |
| the fixture | `examples/fixture/` in this skill |
