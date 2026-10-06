---
name: ux-enterprise-ruleset
description: >-
  Applies the enterprise standard for what a person sees, UX-01, and the ruleset an assistant
  generates screens under, UX-02, to any officer-facing screen work — generating or reviewing a
  form, a list, a menu, a wizard, a grid, a lookup, a worklist, a dashboard, a notice or a case or
  workflow screen, on Joget or any other back-office platform — by a procedure of four steps, and
  reads both documents from the one copy of each in the standards root at the moment of
  use. Use it whenever a task touches what a person will see or click — "create a form", "add a
  screen", "build the list", "wire the menu", "review this screen", "why is this field like this" —
  even when nobody mentions the user interface. It holds no rule of either document.
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
standard: UX-02
written_against: {edition: "1.4", sha256: "a9489ee036de8169a6317fab427f5aa8212de94cb7098bb6dcca620d43d10635"}
---

# ux-enterprise-ruleset

## What this skill is for

It makes an assistant apply two documents to every screen it generates or reviews, and it does so
by a procedure, not by knowing their rules. The documents are the enterprise standard for what a
person sees, `UX-01`, which carries the rules, the reasons for them, the catalogue of the ways
screens go wrong and the worked examples; and the ruleset an assistant generates screens under,
`UX-02`, which is the operational extract of `UX-01` written for an assistant. Each has one copy,
in the standards root. This skill names where they are, says in what order they are
applied, and holds no line of either: every rule is read from the document at the moment it is
applied.

## Where the two documents are

| The document | Its one copy |
|---|---|
| `UX-02`, the ruleset an assistant generates screens under | `standards/UX-02_Claude_Generation_Ruleset.md` |
| `UX-01`, the enterprise standard for what a person sees | `standards/UX-01_Enterprise_UX_Standard.md` |

This kit carries one copy of each, in its standards root. A second copy of either document found
anywhere else is not read, and is reported as a finding to the method's owner.

## Before the first step

1. **The staleness check.** In the kit's root,
   `kit/`, run
   `python3 tools/kit.py skills --check` and read this skill's line,
   `sdd-kit/ux-enterprise-ruleset`. Where it reads behind, or pinned to a document not in the
   root, the documents have moved since this skill was written: say so, read the documents as they
   now stand, and apply nothing this skill says about where a step is found without checking it
   against them. Where the program cannot be run, say that the check could not be run.
2. **Read `UX-02` in full**, from its copy above, at the start of any task that touches a screen,
   a form, a list, a menu or a case. Read `UX-01` at the sections a step below names, and wherever
   `UX-02` sends the reader to it for a reason or an example. Neither is worked from memory.
3. **The edition** is whatever the document's first lines state at that moment. This file records
   the edition its author read only in its pin, which is for the staleness check and nothing else.

## The procedure — four steps, in this order

The contract these four steps carry out is stated in `UX-01`, Annex B.2, its second point, and in
the note at the head of `UX-02`. It is cited here and not restated.

1. **Before any screen artefact: the derivation.** Open `UX-02` §2 and `UX-01` §5. Answer the
   existence test first, as both sections order it; where it fails, deliver what `UX-01` §5 names
   in place of a screen, and stop there for that screen. Otherwise produce the table `UX-02` §2
   gives, one for each screen, in its form and in its order, and include it in the output.
2. **Every field: its provenance.** In the table's field rows, give each field its provenance in
   the vocabulary `UX-02` §2 gives, with the further columns that section asks for, and then apply
   the test that section closes on. A reference field is decided by the table of `UX-02` §3.
3. **Every gap.** Where the specification is silent on something a screen needs, record it in the
   form `UX-02` §1 gives in its last point and `UX-01` §5 gives in the paragraph that follows its
   derivation questions, with its owner named.
4. **Before delivering: the review.** Run every point of the self-review of `UX-02` §5 over what
   is about to be delivered, and report what it finds in the form that section's closing
   paragraph gives. `UX-01` §6 holds the catalogue each point cites. The review also serves, on
   its own, as the audit of screens that already exist, as `UX-01` Annex B.2, its third point,
   says.

## Where the specification method meets this procedure

The method's skill for the screens of a use case, `use-case-screens` of this plugin, runs
the fourth step over a screen record at its check moment and writes each thing found as a finding
of the specification tree. The record's form is the method's own and carries none of this
procedure's vocabulary. The method records that its standard for the screens and `UX-01` each state
a derivation of a screen and neither names the other; that is a finding with an owner, recorded in
the register's row for the screens, and this skill does not settle it.

## On the spec-to-code platform

Where the work is the platform's, `UX-01` Annex B.1 says where each kind of its rules is carried:
in the pattern library of the generators, in the model's lint, and in the questions a screen's
specification must answer. The pattern library is at
`kit/patterns/ux/` and the model's
lint is the kit's `validate.py`, under its `tools/` folder. A generated screen is never corrected by
hand: a defect of what a person sees is corrected in the pattern or in the model, and the screen is
generated again. Where `UX-02` and an explicit module specification disagree, the closing note of
`UX-02` says which of the two prevails and what is done with the disagreement.

## What this skill never holds

- No words of any rule of `UX-01` or `UX-02`, and no line of either document's tables, lists or
  checklists. A rule is found by the section that carries it, and cited by that section.
- No edition of either document anywhere but the pin.
- No engagement: no engagement's name, path or terms.
- No count read from either document. It is read at run time.
