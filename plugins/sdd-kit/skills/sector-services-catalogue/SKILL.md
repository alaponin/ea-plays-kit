---
name: sector-services-catalogue
description: >-
  Helps a person write the catalogue of services of a sector under the standard SDD-10, The Sector
  Services Catalogue, which is a draft, and is written to the draft and says so: one boundary
  around a sector of several bodies, the customers outside it, every service the bodies owe or
  perform, what each rests on, and its state today. It prepares the catalogue from the template of
  the row header the standard's build produces, walks the person through the standard read from
  the document at the moment of use, writes the answers to the checklist's rules for kit conform,
  and builds the reader's edition the owner reviews. It enforces nothing on the draft's authority
  beyond what the draft says of itself. Use it when a sector's services are to be catalogued,
  checked or brought up to date before any service of it is specified. It holds no rule of the
  standard; it reads every rule where the standard states it.
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
standard: SDD-10
written_against: {edition: "0.1", sha256: "39d7a84bac89de782cc46b36b3783ad6d780e2ee4d88ebc6c60009b01233f06d"}
---

# sector-services-catalogue

**SDD-10 is a draft, and this skill is written to the draft.** It stood as a draft when the skill
was written against it (the pin above). At the start of every use the skill reads the standard's
standing from its first page and tells the person, in the standard's own words, and it enforces
nothing on the draft's authority beyond what the draft says of itself.

## What this skill is for

It helps a person write the catalogue of services of one sector: the statement of what the bodies
of the sector owe and do for the people and organisations they serve. The standard is `SDD-10`,
The Sector Services Catalogue, the document whose name begins `SDD-10_` in the standards root,
`standards/`. The design of the method's skills
names the register's row `S` for the thing; the register carries no such row yet. Everything the
skill needs to know about the thing it reads, at the moment it runs, from the standard and from
the kit's template and checklist; what it holds is only the steps that need a machine.

## Before the first moment

In the kit's root, `kit/` in this skill's folder:

    python3 tools/kit.py skills --check
    python3 tools/kit.py slot S

1. **The staleness check.** Read this skill's line, `sdd-kit/sector-services-catalogue`, in what
   `kit skills --check` prints. Where it reads behind, or pinned to a document not in the root,
   the skill stops and says so: `SDD-01` §14, rule 11. Where the program cannot be run, the skill
   says that the check could not be run and does not treat itself as current.
2. **The row.** Where `kit slot S` prints a row, the skill takes from it the document it was read
   out of, the standing, the section named as the form, the template, the checklist, the seams and
   the line saying who writes the thing. Where it prints that the register carries no such slot,
   the skill takes the standard as the document whose name begins `SDD-10_` in the standards root,
   the template as `<kit>/templates/spec/artefacts/S_sector_services_catalogue.md` and the
   checklist as `<kit>/templates/spec/checklists/SDD-10.md`, each of which names the standard's
   edition and checksum in its head; and it records the missing row as a finding whose owner is the
   owner of the kit's register (*Where this skill stops*, below).
3. **A draft says so.** The skill reads the line of the standard's first page that states its
   version and standing, and tells the person at the start in those words.

## Prepare

1. **Where the catalogue is kept.** A catalogue stands above the systems of a sector, not inside
   one system's specification tree. The person names the folder the sector's work is kept in,
   `<sector>`; where the standard says the catalogue is held, and beside what, is read from the
   standard.
2. Copy the template into that folder, keeping its name:

       cp <kit>/templates/spec/artefacts/S_sector_services_catalogue.md <sector>/

   The comment at the head of the copy names the edition and the checksum of the document the
   template was produced from. It stays as the record of what the catalogue is written to, and it
   is never edited.
3. **The material.** The standard says what the catalogue's architect has in front of them. The
   skill reads that from the standard's first section at the moment of use and confirms with the
   person that each thing stands in `<sector>`, or is named where it is held. Where one the
   standard requires is absent, the skill stops at this moment. The material is read and never
   written.

## Assist

1. Extract the standard's text, in the kit's root, from the document with the kit's own reader,
   the one `kit slot` reads an edition with. The text is read into the session and is not saved:

       python3 -B -c 'import sys, pathlib; sys.path.insert(0, "tools"); import slot; print(slot.Document(pathlib.Path(sys.argv[1])).text)' "<the document>"

2. Walk the person through the standard's sections in the order it gives them. What the standard
   says is stated once for the whole catalogue is written once, at the head of the catalogue, in
   the person's words; what it says is recorded on each row is written in the row header.
3. The template holds the row header as one table. The skill copies that table once for each row
   of the catalogue — each service, and each gap — under a heading of its own naming the row by its
   identifier and its name. It reads each line of the table from the template and the standard as
   it is reached, puts it to the person, and writes into the line's last column only what the
   person accepts. A line with nothing to record carries the word the standard gives for an
   absence, read from the standard, never an empty cell.
4. Where the standard reads the rules of another standard of the series, the skill opens that
   standard by its code in the standards root at that moment, and holds none of its rules.
5. Who proposes and who decides at this moment is read from the standard's first page, the line
   saying who writes the document it governs, and not from this file.

## Check

1. **The verdicts.** Read the rules from the table under `## Rules` in the checklist,
   `<kit>/templates/spec/checklists/SDD-10.md`. Put each rule to the person, by its identifier and
   the words the checklist gives it, and write the person's answer into
   `<sector>/_conformance/S_sector_services_catalogue.md_verdicts.yaml`, one entry for each rule, in
   the form `kit conform` reads (`python3 tools/kit.py conform --help`): the rule, then `met`,
   `not met` or `not applicable`; and, only where the checklist's `program` column names a program
   for that rule and that program was run, the program as the entry's `check`. The skill writes no
   verdict of its own.
2. **The claim.** In the kit's root:

       python3 tools/kit.py conform S <sector>/S_sector_services_catalogue.md

   Exit 0: it wrote the claim beside the catalogue, in its `_conformance/` folder, one line for each
   rule of the checklist. Exit 1: it refused and wrote nothing; what is corrected is the person's
   answer, never the program or the checklist. Exit 2: it could not run. While the register carries
   no row for the thing, the program says so and exits 2; the skill says that the claim could not
   be written, writes none by any other means, and points at the finding the first moment wrote.
   A check that cannot run is a failure and never a pass.
3. **The person's half.** The questions under the checklist's heading `Gate — the person's half`
   are put to the person one at a time, read from the checklist. An answer that shows something
   missing is a finding.
4. **The program's half.** The checklist's heading `Gate — the program's half` says what of the
   standard's gate a program performs. The skill runs only a program the checklist names and the
   kit holds, and reports no result of any check that does not exist.

## Render

The reader's edition is the Word document the owner reviews. It is a build (`SDD-01` §14,
rule 1), put to the owner as the ruling of 25 September 2026 on the owner's reading fixes; the
skill reads that ruling at `<standards>/rulings/2026-09-25-the-owner-reviews-a-polished-document.yaml`
and does not restate it.

1. Write the edition's source from the catalogue, in the register that ruling fixes, at
   `<sector>/_reader/S_sector_services_catalogue_reader.md`. The explanation of each term it uses is
   read from the standard's own section defining its words, at the moment of writing. The source is
   written again from the catalogue whenever the catalogue changes, and is never corrected in its
   own right.
2. Every view of the catalogue the standard asks for, and every figure, is produced by a program
   kept with the sector's work; this skill carries none. Where there is none, that is recorded as a
   finding with the catalogue's architect as its owner.
3. Build the Word document with pandoc, the document converter, found with `command -v pandoc`:

       pandoc <sector>/_reader/S_sector_services_catalogue_reader.md --from markdown --to docx --resource-path <sector>/_reader --output <sector>/_reviews/S_sector_services_catalogue.docx

   Where pandoc is not found, the build could not run, and the skill says so.
4. The Word document is never edited. A correction goes into the catalogue, the source is written
   again from it, and the edition is built again. The owner's acceptance is written into the
   catalogue, below the comment at its head, naming who accepted it and when, and the edition is
   built again from it.

## Where this skill stops

At the moment the standard, the template, the sector's material and the person's own material
together do not settle something the catalogue needs. `SDD-01` §14, rule 5 governs that moment; it
is cited here and not restated. The machine steps are these:

1. One file is written into `<sector>/_findings/`, naming what was missing, where the catalogue
   needed it, and who is to answer it.
2. Where the standard itself could not be followed, was ambiguous or was silent, the same is
   written into `<sector>/_amendments/`.
3. The skill carries on with the parts the gap does not touch, and stops the moment when none
   remain.

It also stops when the staleness check reads behind, and when a program it runs refuses
something: `SDD-01` §14, rule 11.

## What this skill never holds

- No words of any rule of any standard, and no line of any standard's form. A rule is named by its
  identifier and no more, and this file names none.
- No edition of its standard anywhere but the pin.
- No engagement: no engagement's name, path or terms.
- No figure read from a standard, such as a count of rules, fields or checks. It is read at run
  time.

## The fixture test

The fixture is `examples/fixture/S_sector_services_catalogue.md`: the template copied by the
prepare moment and filled for the public library services of the county of Eastbrook, which does
not exist and belongs to no engagement, with four rows — three services and one gap — and the
catalogue's declarations written after them. Beside it,
`examples/fixture/_conformance/S_sector_services_catalogue.md_verdicts.yaml` holds the answer to
each rule of the checklist. In the kit's root:

    python3 tools/kit.py conform S ../skills/sector-services-catalogue/examples/fixture/S_sector_services_catalogue.md
    python3 tools/kit.py skills --check

It passes when the first exits 0 and writes a claim naming every rule of the checklist with a
verdict, so that its count of rules equals the checklist's, and the second prints this skill as
current. **While the register carries no row for the thing, the first exits 2 and writes nothing,
so the fixture test does not pass and no claim stands beside the fixture**; the verdicts stand
ready for the day the row exists.

## Where the pieces live

| The piece | Where it is |
|---|---|
| the standards root, `<standards>` | `standards/`, in this skill's folder |
| the kit's root, `<kit>` | `kit/`, in this skill's folder |
| the standard | the document whose name begins `SDD-10_` in `<standards>` |
| the register's row | none yet; `kit slot S` says so |
| the template | `<kit>/templates/spec/artefacts/S_sector_services_catalogue.md` |
| the checklist | `<kit>/templates/spec/checklists/SDD-10.md` |
| the programs | `<kit>/tools/kit.py`, with the verbs `slot`, `conform` and `skills --check` |
| the ruling on the reader's edition | `<standards>/rulings/2026-09-25-the-owner-reviews-a-polished-document.yaml` |
| the sector's folder, `<sector>` | the folder the person names for the sector's work |
| the catalogue | `<sector>/S_sector_services_catalogue.md` |
| its verdicts, and its claim once one can be written | `<sector>/_conformance/` |
| the edition's source | `<sector>/_reader/` |
| findings and amendments | `<sector>/_findings/` and `<sector>/_amendments/` |
| the reader's edition | `<sector>/_reviews/S_sector_services_catalogue.docx` |
| the form this skill is written from | `references/SKILL-form.md` in this plugin |
| the fixture | `examples/fixture/` in this skill |
