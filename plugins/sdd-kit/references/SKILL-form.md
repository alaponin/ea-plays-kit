# The form of a skill of the method

This is the one form every skill of this plugin is written from. A skill of the method
helps a person write one thing the specification-driven development method has a person write,
under the standard that governs that thing. The form fixes what every such skill has in common:
the pin that records which edition of the standard its author read, the four moments it works in,
the point at which it stops, what it never holds, the fixture that tests it, and the shape of its
`SKILL.md`. It carries no rule of any standard. Where it needs one, it cites it by code, section
and number.

**Where the content comes from.** The accepted design of the target state of the method, a working
paper of 25 September 2026 in the method's estate that is not part of this kit,
sections 2 (what each skill reads, never holds and how its check runs), 3 (the routing), 5 (how a
skill stays correct when its standard changes) and 8.3 (where the knowledge of how to build a thing
lives); and the plan of the finish, a working paper of 28 September 2026, likewise not part of
this kit, section 3.1, which fixes the pin. **Where this form and those two documents disagree, they govern
and this form is corrected.**

## 1. What a skill holds, and what it reads

The knowledge of how to build a thing lives in its standard; the register holds where that
knowledge is; a skill holds only the steps that need a machine (the design of the target state, section 8.3).
Those steps are: which template to copy, which section of the standard to open, in what order the
parts of that section are filled, which program to run, and how the reader's edition is built.
Everything else is read at the moment the skill runs.

| What the skill needs | Where it reads it from |
|---|---|
| the thing's row: its standard, the section that is its form, its seams, its gate, its checklist, its template | the register, by `python3 tools/kit.py slot <row>` run in the kit's root |
| the standard itself | the document the register's row resolves in the standards root; its text extracted at the moment of use |
| the standard's rules and its gate | the checklist the standard's build produces, under the kit's `templates/spec/checklists/`, with the edition and checksum of the document in its head |
| the empty artifact | the template the standard's build produces, under the kit's `templates/spec/artefacts/` |
| the upstream things | the files the row's incoming seams name, in the specification tree; read, never written |
| the checks | the kit's programs: `slot`, `conform`, `skills --check` and `stale`, each run as `python3 tools/kit.py <verb>` in the kit's root |

**The two roots are written relative to the skill's own folder**, as the plugins of this kit's
author write their paths: the standards root, `../../standards/`, and the kit's root, `../../kit/`
(from this file, `../standards/` and `../kit/`). Every other path in a skill is written
relative to one of the two and says which. A path of the kit is never written relative on its own
(`templates/spec/...`), because the validator of the marketplace these skills were first published in reads a relative path that begins
with `templates/`, `scripts/`, `references/` or `examples/` as a file of the skill itself and
fails when the skill does not carry it.

## 2. The pin

Every skill of the method carries, in its frontmatter after `name` and `description`, the
standard it serves and the edition its author read:

```yaml
standard: SDD-05
written_against: {edition: "<edition>", sha256: "<64 hex>"}
```

- `standard` is the code of the one standard the skill serves.
- `edition` is the edition as `python3 tools/kit.py slot <row>` prints it on the line
  beginning `edition`, at the moment the author finished reading.
- `sha256` is the checksum of that edition's document in the standards root, taken at the same
  moment with `shasum -a 256 <the document>`.

The pin is the record of what the author read. It is not a fact the skill relies on: at run time
the skill opens whatever edition stands in the root. `kit skills --check` compares the pin with
the document in the root and with the head of the checklist, and prints the skill as current,
behind, or pinned to a document not in the root (the design of the target state, section 5, part 4). **The
edition appears in the pin and nowhere else in the skill** — not in the description, not in the
body, not in a file name the skill writes out.

**A skeleton carries `standard:` and no `written_against:`**, because nothing has yet been written
against any edition. The task that writes the skill adds the pin when it has read the standard.

## 3. Before the first moment

1. **The staleness check.** `python3 tools/kit.py skills --check` in the kit's root. If this
   skill's line reads behind, or pinned to a document not in the root, the skill stops and says
   so: SDD-01 §14, rule 11. If the program cannot be run, the skill says that the check could not
   be run and does not treat itself as current.
2. **The row.** `python3 tools/kit.py slot <row>` in the kit's root. The skill takes the
   standard's path, its standing and the section named as the form from what this prints.
3. **A draft says so.** Where the row gives the standard's standing as a draft, the skill tells the
   person at the start, in the words of the standard's own first page, and enforces nothing on the
   draft's authority beyond what the draft says of itself (the design of the target state, section 2, "What
   assist means").

## 4. The four moments

Every skill of the method works in the same four moments, in this order. What each moment does is
read from the standard and the register; the skill holds only how it is done.

**Prepare.** Copy the template the row's `preparation.template` cell names into the artifact's
folder in the specification tree. Fill the record header from the row. Confirm that every upstream
thing the row's incoming seams name exists, at the version the header cites. Write no upstream
thing.

**Assist.** Open, in the standard's text extracted at that moment, the section the row names as
the form. Walk the person through it part by part, in the order the standard gives, reading each
line from the text as it is reached. The skill carries the mechanics — how the text is extracted,
which section is opened, the order of the parts, and when to stop (section 5) — and never the
lines themselves.

**Check.** Run `python3 tools/kit.py conform <row> <artifact>` in the kit's root. The program
writes the conformance file into the tree's `_conformance/` folder, one line for each rule of the
checklist. The person's half of the standard's gate is put to the person as questions, read from
the checklist's section headed `Gate — the person's half`. The skill writes no verdict of its own.

**Render.** Build the reader's edition — the Word document the owner reviews — from the artifact,
by the program the skill names by path. The reader's edition is a build (SDD-01 §14, rule 1), put
to the owner as the ruling of 25 September 2026 fixes
(`rulings/2026-09-25-the-owner-reviews-a-polished-document.yaml` in the standards root). The owner's
acceptance is written into the artifact, and the edition is built again from it.

**Three skills have one step more**, because the target state gives them one (the design of the target state,
section 2): `use-case-model` consolidates several disagreeing sources before it prepares;
`application-model` compiles from the upstream things in place of preparing from a template; and
`use-case-screens` produces the walk-through with the kit's program as part of its render. A skill
adds no moment beyond these.

## 5. Where a skill stops

A skill stops at the moment the standard, the register, the upstream things and the person's own
material together do not settle something the artifact needs. It does not supply the missing
thing itself. SDD-01 §14, rule 5 governs that moment and is cited here, not restated.

The machine steps at that moment are these. The skill writes one file into the tree's `_findings/`
folder, naming what was missing, where the artifact needed it, and who is to answer it. Where the
standard itself could not be followed, was ambiguous or was silent, it writes the same into the
tree's `_amendments/` folder. It then carries on with the parts the gap does not touch, and stops
the moment when none remain.

A skill also stops when the staleness check of section 3 reads behind, and when a program it runs
refuses something; SDD-01 §14, rule 11 governs both.

## 6. What a skill never holds

- **No words of any rule** of any standard, and no line of any standard's form. A rule is cited by
  its identifier and no more (the design of the target state, section 4, first row).
- **No edition** of its standard anywhere but the pin.
- **No engagement**: no engagement's name, path or terms. A skill of the method serves every
  engagement.
- **No figure read from a standard** — a count of rules, parts or checks. It is read at run time.

**The test** is the target state's own measure, part (b) of test S3, as `inventory.py` in the
target state's folder counts it: a line of a skill that carries a rule identifier and six or more
words counts as a restating line, and a skill with three or more such lines is listed as
restating. A skill of this plugin is written so that the measure counts none of its lines: an
identifier is cited on its own, or in a line of fewer than six words.

## 7. The fixture test

Each skill carries, in `examples/fixture/` inside its own folder, one artifact produced from the
template by its prepare moment and filled for a fictitious subject that belongs to no engagement,
and, in `examples/fixture/_conformance/`, the file `kit conform` wrote over it. The fixture sits
under `examples/` so that the marketplace's `validate.py` proves that every fixture file the
`SKILL.md` names exists.

The test is run in the kit's root:

```
python3 tools/kit.py conform <row> <the skill's folder>/examples/fixture/<artifact>
python3 tools/kit.py skills --check
```

It passes when the first exits 0 and writes a conformance file naming every rule of the checklist
with a verdict, so that its count of rules equals the checklist's, and the second prints the skill
as current.

## 8. The shape of a written SKILL.md

In this order:

1. **Frontmatter**: `name`; `description`, beginning with what the skill does and naming the
   thing in words and the standard by code, under 1,024 characters, with no edition; `standard`;
   `written_against` (section 2).
2. **What this skill is for** — one paragraph: the thing in words, the standard by code and by its
   title, the register's row.
3. **Before the first moment** (section 3).
4. **Prepare**, **Assist**, **Check**, **Render** (section 4), each with the commands it runs and
   the paths it reads.
5. **Where this skill stops** (section 5).
6. **What this skill never holds** (section 6).
7. **The fixture test** (section 7).
8. **Where the pieces live** — one table: the two roots in full, then each path the skill reads,
   relative to its root.

## 9. The skeleton

A skeleton stands in the plugin for a skill that is not yet written, so that the catalogue lists
every skill of the method before any is written and each can be written on its own. Every skeleton
is produced from the block below by a program of the method's estate, not part of this kit,
which fills the fields in braces from its table of skills, from the
register and from the standards root. The task that writes a
skill replaces its skeleton whole, and the words "not yet written" leave the skill only then.

<!-- skeleton:begin -->
```markdown
---
name: {name}
description: >-
  Not yet written; do not use. The skeleton of the method's skill for {thing_lower},
  under the standard {code}, {title}. It carries no steps yet.{interim}
standard: {code}
---

# {name} — not yet written

**Not yet written.** This folder stands for the skill of the method that will help a person
write {thing_lower}.

It carries no steps yet, and no pin, because nothing has yet been written against any edition of
its standard.

| | |
|---|---|
| The standard | `{code}`, {title} — the document whose name begins `{code}_` in `../../standards/` |
| The register's row | {row} |
| Written from | the form of this plugin, `references/SKILL-form.md` |
| To be written by | the session `{task_session}` ({task_id} of the plan of the finish) |
```
<!-- skeleton:end -->

## 10. The driver

The plugin's eleventh skill, `sdd-specify`, routes rather than assists: it walks a specification
through the method's order and hands the person to the skill the register names for each thing. It
was moved into the method's plugin from another of the owner's plugins by the task that rewrote it, and it cannot stand here as a
skeleton before then, because `validate.py` refuses a skill name carried by two plugins. It keeps
its own four moments — locate, prepare, check and claim, stale — which the design of 14 September
2026 fixed and the target state does not reopen (the design of the target state, section 3). It follows
sections 1, 2, 5, 6, 7 and 8 of this form, and its pin names `SDD-01`, whose order and handovers it
walks.
