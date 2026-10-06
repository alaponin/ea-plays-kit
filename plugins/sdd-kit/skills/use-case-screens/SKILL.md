---
name: use-case-screens
description: >-
  Helps a person write the screens of one use case under the standard SDD-07, The Screens of a Use
  Case, and produces from them the walk-through a person clicks through. It prepares the record of
  the set from the kit's template and from the use case's four lists before any screen is drawn;
  walks the record's form with the person, read from the standard at the moment of use; sets the
  screens beside the use case's steps, variations, entities and requirements by a program; reviews
  the set against the enterprise standard for what a person sees, UX-01, through the skill
  ux-enterprise-ruleset; writes the claim of conformance rule by rule with kit conform; produces the
  walk-through with kit screens walk; and builds the reader's edition the owner reviews. Use it for
  every use case a person completes in one sitting, once the goal's use case has been written out in
  full. It holds no rule of any standard; it reads every rule where the standard states it.
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
standard: SDD-07
written_against: {edition: "1.3", sha256: "f3602240be8516e29266fe0a86cca91448d4c14305f67379a10e1fc8ea3ae6be"}
---

# use-case-screens

## What this skill is for

It helps a person write the screens of one goal — the screens a person meets while reaching it,
the step or variation of the use case each one serves, and what each shows and lets them do —
and it produces from that written record the walk-through a counterpart clicks through. The standard is `SDD-07`, The Screens of a Use Case, the document whose
name begins `SDD-07_` in the standards root, `standards/`.
The register has two rows for it: `07`, the screens, written again for every goal, one folder for
each; and `08`, the walk-through, which nobody writes. What a screen may show, and how, is governed
by the enterprise standard for what a person sees, `UX-01`, in the same root; this skill reaches it
through the skill `ux-enterprise-ruleset` of this plugin and reads none of it itself.
Everything else the skill needs to know about the thing it reads, at the moment it runs, from the two
rows and from the standard; what it holds is only the steps that need a machine.

## Before the first moment

In the kit's root, `kit/` in this skill's folder:

    python3 tools/kit.py skills --check
    python3 tools/kit.py slot 07
    python3 tools/kit.py slot 08

1. **The staleness check.** Read this skill's line, `sdd-kit/use-case-screens`, in what
   `kit skills --check` prints. Where it reads behind, or pinned to a document not in the root, the
   skill stops and says so: `SDD-01` §14, rule 11. Where the program cannot be run, the skill says
   that the check could not be run and does not treat itself as current. Read the line of `sdd-kit/ux-enterprise-ruleset` as well: where it reads
   behind, the review under that skill at the check moment is not run, and the skill says why.
2. **The rows.** From what `kit slot 07` prints, take the document it was read out of, the
   standing, the section named as the form and the sections beside it, the template, the checklist,
   the seams, the line saying who writes the thing, and the notes. From what `kit slot 08` prints,
   take the section that names the program producing the walk-through, and the notes.
3. **A draft says so.** Where the rows give the standing as a draft, the skill tells the person at
   the start, in the words of the standard's own first page read from the document, and enforces
   nothing on the draft's authority beyond what the draft says of itself.
4. **The use case, and whether it has a set.** The use case is the goal's file in
   `<tree>/06_use_cases/<the use case's identifier>/06_use_case.md`, where `<tree>` is the folder
   `kit spec new` made for the system. Where it does not exist, or is not yet written out in full,
   the skill stops: the row's `when` line says when the screens are written. Read with the person
   the part of the standard's §4 that says which use cases have a set of their own, and stop where
   this one has none.
5. **The notes.** Row 07's notes name what the method records about this thing, among them a
   finding on how this standard and `UX-01` each derive a screen. Carry each note that bears on this
   set to the check moment; the skill settles none of them.

## Prepare — the four lists first

1. The goal's folder in the tree is `<tree>/07_screens/<the use case's identifier>/`, one for each
   goal: the register's row 07 gives the folder's name.
2. Copy the template the row names into that folder, named after the use case:

       cp <kit>/templates/spec/artefacts/07_screen_record.md <tree>/07_screens/<the use case's identifier>/<the use case's identifier>_screens.md

   The name is not the template's, because the kit's program that produces the walk-through takes
   the set's identifier from the record's file name and prints it on every page
   (`python3 tools/kit.py screens walk --help` in the kit's root). The comment at the head of the
   copy names the edition and the checksum of the document the template was produced from; it stays
   as the record of what the set is written to, and it is never edited.
3. **The four lists, before any screen is drawn.** Read from the use case, with the person, its
   four lists: its numbered steps, its variations with their kinds and
   endings, the entities it reads and those it changes, and the requirements it realises. The
   fields they are read from are the ones the four-list program reads, named in its own
   documentation: `python3 scripts/four_lists.py --help` in this skill's folder. Nothing is added to
   the four lists here. A list that is missing something the screens will need is a gap in the use
   case (*Where this skill stops*, below).
4. **The use case's version.** The standard asks each screen, and the set once, to name the use
   case with its version. Where the use case's record header carries no version, name the file the
   set is worked out from by its checksum, taken with `shasum -a 256 <the use case>`, and write the
   want of a version into `<tree>/_amendments/` once for the tree.
5. **The four things beside it.** The standard's §1 names what the writer needs beside the use
   case. Confirm that each exists in the tree, as a listing of its headings, since each skill of
   the method writes one `###` heading for each thing in a file:

       grep -n '^### ' <tree>/02_entity_model/02_entity_model.md
       grep -n '^### ' <tree>/02_entity_model/02_business_rules.md
       grep -n '^### ' <tree>/01_requirements_register/01_requirements_register.md

   Every entity, rule and requirement a screen will name is looked up there and in the use case,
   and never reworded to fit.
6. Nothing is written into an upstream thing's folder, at this moment or at any other.

## Assist — the screens, then the set

1. Extract the standard's text, in the kit's root, from the document `kit slot 07` was read out
   of, with the kit's own reader, the one `kit slot` reads the edition with. The text is read into
   the session and is not saved into the tree:

       python3 -B -c 'import sys, pathlib; sys.path.insert(0, "tools"); import slot; print(slot.Document(pathlib.Path(sys.argv[1])).text)' "<the document>"

2. **Which screens there are.** Open §4 of that text and walk it with the person over the four
   lists: the main path first, then each variation, then any screen another use case shares. Where
   the standard says a person decides, the person decides and the skill proposes at most.
3. **Each screen.** Copy the record header's table and the table of `For each screen` once for
   each screen, in the same order under both headings, and walk them line by line: the header as
   §5 of the text gives it, then the lines of §11 for each screen. At the line on every value, open
   §6 and ask its questions of each value in turn, reading each from the text as it is reached.
4. **The set.** Walk the lines of §11 for the set as a whole, once. Where a step, a variation, an
   entity or a requirement of the four lists is reached by no screen, the reason is written in the
   line the template gives that list, in the form the four-list program reads (its documentation,
   step 3 of *Prepare*).
5. **How an answer is written.** Identifiers stand between backticks, several entries in one cell
   are separated by `<br>`, and the acts, the variations and the values are written in the grammar
   the walk-through program documents (`python3 tools/kit.py screens walk --help`). The template's
   headings and the first columns of its tables are never changed; only the Answer cells are
   written. The kit's program refuses any other departure, which is why the grammar is kept.
6. Where a line names a rule, open the rule in §10 of the text before the line is written, and read
   it with the person; the skill carries no line of it. The person proposes and accepts; the skill
   writes into an Answer cell only what the person accepts, in the person's words.
7. A word, an entity, a rule or a requirement a screen needs and the use case does not declare is
   never supplied here: it is a gap, raised against the use case (*Where this skill stops*, below).
   §5 of the text says where such a gap belongs; it is read there, not here.
8. Who proposes and who decides at this moment is the row's line on who writes the thing, read from
   `kit slot 07`, and not this file.

## Check

1. **The four lists.** Set the screens beside the use case's four lists by the skill's program:

       python3 <skill>/scripts/four_lists.py <tree>/07_screens/<the use case's identifier>/<the use case's identifier>_screens.md <tree>/06_use_cases/<the use case's identifier>/06_use_case.md

   `<skill>` is this skill's folder (*Where the pieces live*, below). The program reads the
   record with the kit's own reader of it, prints each item of each list as reached,
   carried by a written reason, or unmatched, and then everything the screens name that the four
   lists do not hold. It prints no figure. Exit 0: nothing is unmatched. Exit 1: each unmatched item
   is printed, and whichever is wrong, the record or the use case, is corrected; the use case is
   corrected through its own skill, and never by this one. Exit 2: it could not run, which is said
   as such. The reading against the stakeholders' interests is not the program's; the person makes
   it and records it in the set's line, with who read it and when.
2. **The walk-through, before the verdicts.** Produce it now, as the render moment's first step
   says, because the rules about the walk-through and the review's questions about it are answered
   by opening it and following it through, and because the kit's program refuses a record that
   leaves a person with no way on.
3. **What a person sees, under UX-01.** Run the fourth step of the skill
   `ux-enterprise-ruleset` of this plugin — its review before delivery — over the set,
   reading the two documents it names from the standards root. Each thing it finds is written into
   `<tree>/_findings/` as one file, and the record is corrected where the correction is the
   record's. Nothing of that skill's vocabulary is written into the record, whose form is this
   standard's. Where it and this standard ask the same question in two ways, that is the finding
   row 07's notes already record, and the skill settles nothing between them.
4. **The verdicts.** Read the rules from the table under `## Rules` in the checklist the row
   names, `<kit>/templates/spec/checklists/SDD-07.md`. The standard's review names who answers
   them; it is read from the opening words the checklist carries under `Gate — the person's half`.
   Put each rule to them, by its number and the words the checklist gives it, and write their
   answers into `_conformance/<the use case's identifier>_screens.md_verdicts.yaml` beside the
   record, one entry for each rule, in the form `kit conform` reads (`python3 tools/conform.py --help`):
   the rule's number as a quoted key, then `met`, `not met` or `not applicable`; and, only
   where the checklist's `program` column names a program for that rule and that program was run,
   the program as the entry's `check`. The skill writes no verdict of its own. The output of the
   four-list program and of the walk-through program is what the person reads to answer; neither is
   cited as a `check` unless the checklist names it.
5. **What the claim must name and the claim file has no line for.** The standard's paragraph on
   claiming conformance, in its §1, asks a claim to name the use cases the set belongs to and the
   version of each. The claim `kit conform` writes carries a line for each rule and none for that.
   At the head of the verdicts file, as comment lines, the skill therefore writes the use case and
   its version, the SHA-256 of the record taken at the moment of answering, what each program
   printed, and, for every rule not met, the finding and its owner.
6. **The claim.** In the kit's root:

       python3 tools/kit.py conform 07 <tree>/07_screens/<the use case's identifier>/<the use case's identifier>_screens.md

   Exit 0: it wrote the claim beside the record, in its `_conformance/` folder, one line for each
   rule of the checklist. Exit 1: it refused and wrote nothing; each refusal names a rule, and what
   is corrected is the answer, never the program or the checklist. Exit 2: it could not run, which
   is said as such.
7. **The person's half.** The questions under the checklist's heading `Gate — the person's half`
   are put, one at a time, to those the review names, at the review, with the walk-through open.
   The skill answers none of them. An answer that shows something missing is a finding.
8. **The program's half.** The skill runs only a program the checklist's `program` column names,
   and reports no result of any check the kit does not hold.
9. **What the set gives the application model.** Row 07's seam to row `09` names the section of
   the standard that says where each thing a set's record carries lands in the application model;
   `kit slot 07` prints it on that seam's line `declared at`. Open that section in the text. For
   each row of its tables, find the entries of this record of the kind the row's first cell names,
   and read the row's other cells with the person: where the entry lands, which kind of landing
   the row gives it, and where it cannot land. Nothing is decided here that the section
   leaves to whoever writes the application model, and nothing is written into
   `<tree>/09_application_model/`.
10. **What a change makes stale.** When the record changes after anything was made from it,
    `python3 tools/kit.py stale 07 <the record>` in the kit's root lists what the change makes
    stale, and changes nothing. The program reads the version an artifact records at its head;
    where it says it could not run, the skill says so and does not treat the check as passed.
    Whatever the program says, the walk-through is produced again whenever the record changes.

## Render

The render moment has two builds: the walk-through a counterpart clicks through, and the reader's
edition the owner reviews. Both are builds (`SDD-01` §14, rule 1), and neither is ever edited.

1. **The walk-through.** In the kit's root:

       python3 tools/kit.py screens walk <tree>/07_screens/<the use case's identifier>/<the use case's identifier>_screens.md --out <tree>/08_walkthrough/<the use case's identifier>/

   The folder is the one the register's row 08 gives the tree, which holds the record under the
   same version control, as the standard's §8 asks of where a walk-through is held. Exit 0: the
   pages are written, and the program prints what it wrote. Exit 1: the record is refused and
   nothing is written; the record is corrected, never a page. Exit 2: it could not run, which is
   said as such. Exit 3: a defect of the kit's program, found by its own check before any page was
   written; it is reported to the kit's owner as a finding and worked around by nobody. The pages
   are produced again whenever the record changes, and the set's line saying how, by whom and when
   the walk-through was last produced is kept true.
2. **The reader's edition.** It is put to the owner as the ruling of 25 September 2026 on the
   owner's reading fixes; the skill reads that ruling at
   `<standards>/rulings/2026-09-25-the-owner-reviews-a-polished-document.yaml` and does not restate
   it. Write the edition's source from the record, in the register that ruling fixes, at
   `<tree>/07_screens/<the use case's identifier>/_reader/<the use case's identifier>_screens_reader.md`.
   The explanation of each word the set uses is read from the entity model and its glossary, which
   own those words, at the moment of writing; where the walk-through stands, and how to open it, is
   said in the edition. The source is written again from the record whenever the record changes,
   and is never corrected in its own right.
3. A figure is drawn by a program kept in `<tree>/_machinery/`, and the picture it draws is kept
   beside the source and referenced from it.
4. Build the Word document with pandoc, the document converter, found with `command -v pandoc`:

       pandoc <tree>/07_screens/<the use case's identifier>/_reader/<the use case's identifier>_screens_reader.md --from markdown --to docx --resource-path <tree>/07_screens/<the use case's identifier>/_reader --output <tree>/_reviews/07_screens_<the use case's identifier>.docx

   Where pandoc is not found, the build could not run, and the skill says so.
5. A correction goes into the record; the walk-through is produced again and the edition built
   again from it. The owner's acceptance is written into the record, as a line below its title
   naming who accepted it and when, and both builds are made again from it.

## Where this skill stops

At the moment the standard, the register, the use case, the things beside it and the person's own
material together do not settle something the set needs. `SDD-01` §14, rule 5 governs that moment;
it is cited here and not restated. The machine steps are these:

1. One file is written into `<tree>/_findings/`, naming what was missing, where the set needed it,
   and who is to answer it.
2. Where the standard itself could not be followed, was ambiguous or was silent, the same is
   written into `<tree>/_amendments/`.
3. The skill carries on with the parts the gap does not touch, and stops the moment when none
   remain.

It also stops before the first moment when the use case is not written out in full, or is one the
standard gives no set; when the staleness check reads behind; and when a program it runs refuses
something: `SDD-01` §14, rule 11.

## What this skill never holds

- No words of any rule of any standard — of `SDD-07`, of `UX-01` or of `UX-02` — and no line of
  any standard's template. A rule is named by its number or its identifier and no more.
- No edition of its standard anywhere but the pin.
- No engagement: no engagement's name, path or terms.
- No figure read from a standard, such as a count of rules, lines, questions or checks. It is read
  at run time.

## The fixture test

The fixture is `examples/fixture/UC-LN-02_screens.md`: the template copied by the prepare moment
and filled for one goal, Renew a loan, of the loans module of a fictitious lending library, which
belongs to no engagement. Beside it stand `examples/fixture/06_use_case.md`, the use case the set
was worked out from — a copy of the fixture of the skill `use-case-description`, so that this
fixture stands on its own — and `examples/fixture/_conformance/`, holding the answer to each rule
under a head naming the use case, its version and what the two programs printed
(`UC-LN-02_screens.md_verdicts.yaml`), and the claim `kit conform` wrote over it
(`UC-LN-02_screens.md_conformance.md`). `examples/unmatched/UC-LN-02_screens.md` is the same record
with four defects planted in it: step 6 and variation 6a served by no screen, the entity Renewal
changed on no screen, and a requirement named that the use case does not declare.

In the kit's root, with `<skill>` for this skill's folder (*Where the pieces live*, below):

    python3 tools/kit.py conform 07 <skill>/examples/fixture/UC-LN-02_screens.md
    python3 tools/kit.py skills --check
    python3 tools/kit.py screens walk <skill>/examples/fixture/UC-LN-02_screens.md --out <a new folder outside the skill>
    python3 <skill>/scripts/four_lists.py <skill>/examples/fixture/UC-LN-02_screens.md <skill>/examples/fixture/06_use_case.md
    python3 <skill>/scripts/four_lists.py <skill>/examples/unmatched/UC-LN-02_screens.md <skill>/examples/fixture/06_use_case.md

It passes when the first exits 0 and writes a claim naming every rule of the checklist with a
verdict, so that its count of rules equals the checklist's; the second prints this skill as
current; the third exits 0; the fourth exits 0 and prints no unmatched item; and the fifth exits 1
and prints as unmatched exactly the four planted defects.

## Where the pieces live

| The piece | Where it is |
|---|---|
| the standards root, `<standards>` | `standards/`, in this skill's folder |
| the kit's root, `<kit>` | `kit/`, in this skill's folder |
| this skill's folder, `<skill>` | `../skills/use-case-screens/` from the kit's root, where the commands that name it are run |
| the standard | the document whose name begins `SDD-07_` in `<standards>`, as `kit slot 07` resolves it |
| the enterprise standard for what a person sees | `<standards>/UX-01_Enterprise_UX_Standard.md`, reached through `sdd-kit:ux-enterprise-ruleset` |
| the method's standard, for the moments of stopping | the document whose name begins `SDD-01_` in `<standards>` |
| the register's rows | rows `07` and `08` of `<kit>/templates/spec/slots.yaml`, read with `kit slot 07` and `kit slot 08` |
| the template | `<kit>/templates/spec/artefacts/07_screen_record.md` |
| the checklist | `<kit>/templates/spec/checklists/SDD-07.md` |
| the programs of the kit | `<kit>/tools/kit.py`, with the verbs `slot`, `conform`, `skills --check`, `stale` and `screens walk` |
| the four-list program | `scripts/four_lists.py` in this skill |
| the ruling on the reader's edition | `<standards>/rulings/2026-09-25-the-owner-reviews-a-polished-document.yaml` |
| the specification tree, `<tree>` | the folder `kit spec new` made for the system |
| the record of the set | `<tree>/07_screens/<the use case's identifier>/<the use case's identifier>_screens.md` |
| its verdicts and its claim | `<tree>/07_screens/<the use case's identifier>/_conformance/` |
| the walk-through | `<tree>/08_walkthrough/<the use case's identifier>/` |
| the edition's source | `<tree>/07_screens/<the use case's identifier>/_reader/` |
| the upstream things | `<tree>/06_use_cases/`, `<tree>/02_entity_model/`, `<tree>/01_requirements_register/` |
| the downstream thing it is read against, never written | `<tree>/09_application_model/` |
| findings and amendments | `<tree>/_findings/` and `<tree>/_amendments/` |
| the reader's edition | `<tree>/_reviews/07_screens_<the use case's identifier>.docx` |
| the form this skill is written from | `references/SKILL-form.md` in this plugin |
| the fixture | `examples/fixture/` and `examples/unmatched/` in this skill |
