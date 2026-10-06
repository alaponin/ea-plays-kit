---
name: sdd-specify
description: >-
  Start and drive a specification written to the standards of the specification-driven development
  method, SDD-01 and the standards it places, for any system: scaffolds the specification tree with
  kit spec new, and then, at each of its four moments — locate and say what is next, prepare, check
  and claim, list what a change made stale — reads the register's row for the thing in hand and
  hands the person to the skill the row's skill cell names, or says that the cell is absent and who
  owns it. Use WHENEVER a system is about to be specified or a run is resumed: 'specify X to the
  standards', 'start a new specification', 'scaffold the SDD tree', 'which slot are we in', 'what is
  written next', 'which skill helps with the entity model', 'claim conformance rule by rule', 'the
  use case changed, what is stale'. It knows the order of the method only by reading it from the
  register, and it holds no rule of any standard.
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
standard: SDD-01
written_against: {edition: "3.5", sha256: "b14cf9b6ba88c725a664e25a5ff080bd21c0b8554abe2e49d27d2bb230391a5b"}
---

# sdd-specify

## What this skill is for

It routes a specification through the method: it knows where a run stands, which thing is written
next, and which skill helps a person write it. The standard whose order and handovers it walks is
`SDD-01`, Specification-Driven Development, the document whose name begins `SDD-01_` in the estate's
root, `standards/`. It does not describe any of the
things the method has a person write. For each of them it reads the thing's row in the delivery
kit's register and hands the person to the skill that row names; the skill reads its own standard.

A run produces two things, and the second is the one that gets dropped: the specification, and the
tree's `_amendments/` folder, holding every place a standard could not be followed, was ambiguous,
cost more than it was worth or was silent, each recorded at the moment it happened. A run that
produces the first and not the second has failed, however good the specification is.

**No domain literal.** This skill, the register and the scaffolder carry no system name, no sector
word and no project.

## Before the first moment

In the kit's root, `kit/` in this skill's folder:

    python3 tools/kit.py skills --check
    python3 tools/kit.py slot --check

1. **The staleness check.** Read this skill's line, `sdd-kit/sdd-specify`, in what
   `kit skills --check` prints. Where it reads behind, or pinned to a document not in the root, the
   skill stops and says so: `SDD-01` §14, rule 11. Where the program cannot be run, the skill says
   that the check could not be run and does not treat itself as current. Every other skill's line is that skill's own to act on when it is reached.
2. **The register.** `kit slot --check` resolves every row and every handover of the register
   against the standards in the root and the kit. Every cell it reports as not resolving is said
   to the person, and is said again in whatever the moment produces — a finding, a claim, a list —
   and is never worked around. The moment goes on with what does resolve.

## Starting a run

1. **Scaffold the tree.** In the kit's root:

       python3 tools/kit.py spec new <systemId> --name "<the system's name>" --out <tree> [--carry SLOT=PATH ...] [--prior <an earlier attempt's folder>]

   It writes one folder for each thing the register names, every folder's readme rendered from the
   register, and the planning commission. Carry a generated document together with the folder of
   its source (`--carry 03=./model/`), never alone: a generated document carried alone can be
   corrected only by hand, which the method forbids (`SDD-01` §14, rule 1). The command warns when a
   single Word, PDF, slide or spreadsheet file is carried without a folder; the warning is answered,
   not passed over. Every carried file is checksummed on both sides and the command refuses a copy
   that differs.
2. **Hand the commission to a new session.** The planning commission the scaffolder writes at
   `<tree>/_sessions/SPEC_PLAN_SESSION_PROMPT.md` designs the run and writes no specification. What
   comes back is opened and checked on disk, not taken on its word: each deliverable it names
   exists, its counts match its working files, and what it says ran did run.

## The four moments

Every moment is about one thing of the method, the row `<n>` of the register, and begins the same
way: in the kit's root, `python3 tools/kit.py slot <n>` prints the row; in this skill's folder,

    python3 scripts/skill_for.py <n>

prints what the row's `skill` cell says, in one of three forms: the skill it names, with the path of
its `SKILL.md`; `none`, where no standard of the method governs the thing and the method gives it no
skill; or `absent`, with the owner and the reason the cell gives. The program's help says how each
form is read (`python3 scripts/skill_for.py --help`).

- **Where it names a skill**, the person is handed to that skill for the moment, by its name
  (`<plugin>:<skill>`), and the skill's own moments do the work: its prepare (or its compile, or its
  consolidate), its check, its render. This skill does none of them itself.
- **Where it reads `none`**, the moment is the register's row alone. What the row says of the thing
  — who writes it and when, and whether it is ever edited — is read from `kit slot <n>` and said to
  the person.
- **Where it reads `absent`**, the skill says so, with the cell's owner, and carries out the moment
  from the row: the standard at the section the row names as the form, the template the row names,
  the checklist and the programs the row names. The absence is recorded, not filled: nothing is
  written into the register here.

**Locate, and say what is next** — at any time. In the kit's root, `python3 tools/kit.py spec map`
draws the order of the things and the handovers from the register, and `python3 tools/kit.py spec
route` prints, for each crossing, the section of the standard that states how it is made. Which
thing the run is at is read from the tree, never remembered. The thing written next is the one the
map puts next whose upstream things all stand in the tree; any thing may be entered again, but only
from above it, and a measure written after the thing it measures is not a measure.

**Before a thing is written — prepare.** Read the row, and the skill cell as above. Where the row's
incoming seams name an upstream thing that does not stand in its folder of the tree, the moment
stops and records a finding with an owner in `<tree>/_findings/`: a goal may not invent what the
groundwork does not hold. Otherwise, hand the person to the skill.

**After a thing is written — check and claim.** Read the row, and the skill cell as above. The
named skill runs the thing's check and writes the claim of conformance with `kit conform`, rule by
rule. Where the cell is absent, in the kit's root,
`python3 tools/kit.py conform <n> <the artifact>` writes the claim from the checklist the row names,
from the verdicts the person and the programs gave. A claim that is not rule by rule is not a
claim. Every departure of the method from a standard that `SDD-01` §9 declares is named as part of
the claim.

**After a thing has changed — list what is stale.** In the kit's root,
`python3 tools/kit.py stale <n> <the artifact>` lists every thing of the tree made from the changed
one at a version that is no longer current, and changes nothing. The list is written into the
amendment that made the change; nothing on it is reviewed, agreed or built from until it has been
made again, by the skill each of its rows names.

## Where this skill stops

At the moment the register, the standards, the tree and the person's own material together do not
settle what the run needs. `SDD-01` §14, rule 5 governs that moment; it is cited here and not
restated. One file is written into `<tree>/_findings/`, naming what was missing and who is to answer
it; where a standard could not be followed, was ambiguous or was silent, the same goes into
`<tree>/_amendments/`. The run goes on with what the gap does not touch.

It also stops when the staleness check reads behind, and when a program it runs refuses something:
`SDD-01` §14, rule 11. And it stops, and says so, whenever the run is found to have broken a rule of
`SDD-01` §14, read from the standard at that moment — among them rules 1, 5, 7, 13, 18 and 19 —
and whenever it finds that:

- the amendment folder is empty after a thing was closed: either nothing was learned, which is not
  credible, or it was not recorded;
- a thing was written out of the order the map draws;
- the customer's own documents were touched, which the register's row 00 says are never edited.

## What this skill never holds

- No words of any rule of any standard, and no line of any standard's form. A rule is named by its
  identifier and no more.
- No order of the things and no list of the handovers: they are read from the register, through
  `kit spec map` and `kit spec route`, at the moment of use.
- No description of any thing of the method: the skill the register names holds that, and reads it
  from its own standard.
- No edition of its standard anywhere but the pin.
- No engagement: no engagement's name, path or terms.
- No figure read from a standard. It is read at run time.

## The fixture test

This skill writes no artifact of its own, so its fixture is what it reads:
`examples/fixture/slots.yaml`, four rows of the register with the cells `skill_for.py` reads, the
skill cells of rows 01 and 09 filled as the register's own round is to fill them and rows 00 and 06
as the register carries them. `examples/fixture/expected.txt` holds what the program is to print.

In this skill's folder:

    python3 scripts/skill_for.py --slots examples/fixture/slots.yaml 00 01 09
    python3 scripts/skill_for.py --slots examples/fixture/slots.yaml 06
    python3 scripts/skill_for.py 00 01 09

In the kit's root:

    python3 tools/kit.py skills --check

It passes when the first prints the lines of `examples/fixture/expected.txt` for rows 00, 01 and 09
— none, and the two skills named, each at its path — and exits 0; the second prints row 06 as
absent with its owner and exits 1; the third prints, for each of the three rows, what the register
standing in the kit says of it now; and `kit skills --check` prints this skill as current.

## Where the pieces live

| The piece | Where it is |
|---|---|
| the standards root, `<standards>` | `standards/`, in this skill's folder |
| the kit's root, `<kit>` | `kit/`, in this skill's folder |
| the marketplace | this skill's folder, where the kit looks for each skill a row names beside it, at `../<skill>/SKILL.md` |
| the standard | the document whose name begins `SDD-01_` in `<standards>` |
| the register | `<kit>/templates/spec/slots.yaml`, read with `kit slot`, `kit spec map` and `kit spec route` |
| the checklist of the standard | `<kit>/templates/spec/checklists/SDD-01.md` |
| the scaffolder | `<kit>/tools/scaffold_spec.py`, reached as `kit spec new` |
| the programs | `<kit>/tools/kit.py`, with the verbs `spec`, `slot`, `conform`, `skills --check` and `stale` |
| the program that reads a row's skill cell | `scripts/skill_for.py` in this skill |
| the specification tree, `<tree>` | the folder `kit spec new` made for the system |
| findings and amendments | `<tree>/_findings/` and `<tree>/_amendments/` |
| the form this skill is written from | `references/SKILL-form.md` in this plugin, its section on the driver |
| the fixture | `examples/fixture/` in this skill |
