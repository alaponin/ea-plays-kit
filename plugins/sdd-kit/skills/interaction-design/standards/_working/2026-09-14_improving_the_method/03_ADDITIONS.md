---
artefact: 03_ADDITIONS
commission: _prompts/PROMPT_IMPROVE_the_method_2026-09-14.md (METHOD-2026-09-14-03, provisional)
upstream: part six of The_Method_Today_2026-09-12.docx, whose six additions are stated as decisions
  taken and are placed here, not reopened; 00_DECISIONS.md D5 to D9 of this round; item 8 of
  03_RECOMMENDATION.md of 12 September for the placements tested in D7
serves: the SDD method project — the six additions the analysis of 12 September decided, each
  given a place by path, a border, a prerequisite and a test
standing: a design. The four clauses of the third addition are drafted here as text and are written
  into no standard by this round; a listing in the report shows the nine standards unchanged. Every
  placement lands on a standard that already borders its subject or in a written procedure, under the
  owner's standing instruction of 1 September, and no tenth standard is proposed
written: 14 September 2026, by a working session at Fable. _standards/ stands for
  the method's standards estate (in sdd-kit, standards/), kit/ for the delivery kit (in sdd-kit, kit/), and the travelling layer for
  the orchestrator skill of the owner's project-operations plugin, which is not part of sdd-kit
---

# The six additions, placed

Each section below is one addition, in the analysis's own order, and carries the six things the
instruction asks for: what it is, in one paragraph; where it lands, by path, with the standard or
the procedure that borders its subject; what changes for somebody doing the work; what becomes
impossible once it exists; what must exist before it; and how anybody would know it had been done,
written so that a stranger could run the test. The rounds that build each are in `04_PLAN.md`, and
where an addition is the other programme's work, decision D9 says so and it is cited rather than
planned twice.

---

## One · The checks inside each standard, brought out as material anybody can read

**What it is.** Eight of the nine standards carry their own checklist inside them — checkpoint lines
a reader answers one by one, the lines of the form that fix what is written, the rule table, and in
one case a quality check that is also the gate of the review — and they are unreachable because a
person has to open a large document and find the right section. The addition brings each standard's
checklist out as one file beside it: the gate's lines in their two halves, the form's lines with the
rule each serves, the rule table by identifier, and the name of the program that reads the standard's
lines where one exists. It is not written separately. It is produced by a program from the document
of record itself, at the end of every build of that standard and on demand over the root, and it
names the document, the edition and the digest it was produced from, so that a checklist for a
superseded edition says so on its face.

**Where it lands.** Nine files, `kit/templates/spec/checklists/SDD-0n.md`, one per standard, in the
delivery kit, where the register's `check.checklist` cell points at them and `kit conform` reads
them. The extractor is one program, `_standards/_working/<date>_checklists/extract_checklist.py`,
the build source of this piece of work in the place the constants file gives to build sources; it
reads the built document and not the build script, which is what lets it produce a checklist for the
edition of record of the entity model standard, whose build source does not exist (finding F-2). The
border is each standard's own gate and form — the entity model standard's parts 5, 6 and 11 and their
counterparts in the other eight — and the estate's rule in its readme that every document is
generated and never edited by hand; the checklist is one more output of the same act. One consequence
is recorded for the scaffold: the recommendation of 12 September says the slot READMEs already point
at `checklists/`, and a count over the four scaffold templates at 18:10 UTC finds the word in none of
them (`_evidence/listings.txt`), so `slot_README.md.tmpl` gains one line naming the slot's checklist,
in round M0.

**What changes for somebody doing the work.** A person checking a description against its standard
opens one short file instead of a fifty-page document, answers its lines in order, and finds the
name of the program that answers the lines a program can read. The next person does the same.

**What becomes impossible.** A checklist that disagrees with the standard it came from, because the
two are produced from one document and compared on every rebuild; a second checking program written
for a standard that already names one, because the first is named where anybody looking for it will
find it; and a claim of conformance that cites a rule the standard does not carry, because the file
the claim is written from carries the standard's rules and no others.

**What must exist before it.** The register with its `check.checklist` cell, round M0, so that the
file has a cell to be named in; nothing else. It does not wait on the four clauses and does not wait on
the entity model standard's build source being restored.

**How anybody would know.** Run `python3 extract_checklist.py _standards/SDD-03_The_Entity_Model_v0_5.docx`
twice and compare the two outputs byte for byte: identical. Open the output and count: forty-three
lines in its first half, C1 to C43; seventeen lines in its second half; twenty-two gate lines; and
EM-1 to EM-56 in its rule table — the four counts `_evidence/count_out.txt` gives from the same
document by another route. Rebuild the method standard in its own build folder, run the extractor
over the rebuilt document, and compare with the file in the kit: identical. Nine files exist under
`kit/templates/spec/checklists/`, `ls` shows nine, and `kit slot --check` exits 0 with every
`check.checklist` cell resolving.

---

## Two · One instrument that applies all of those checks

**What it is.** The one procedure of `01_PROCEDURE.md`: a skill of its own, `sdd-slot`, with two
programs beneath it, that reads the register for the artefact in hand and does the one act the moment
calls for — prepare, check and claim rule by rule, list what a change made stale, or say what is
next. It is one instrument rather than nine because between one standard and the next only the
standard's name and the location of its checking program change, and both are cells of the register.
Decision D1 gives its shape and the ground; this section places it.

**Where it lands.** The skill `sdd-slot` of the owner's spec-to-code plugin, which is not part of sdd-kit,
its only source; the two programs at `kit/tools/slot.py` and `kit/tools/conform.py`, reached as
`kit slot` and `kit conform` through the kit's facade `kit/tools/kit.py`, beside the sixty-six
programs already there; and one change to the run-driver, `kit/skills/sdd-specify/SKILL.md`, whose
steps 3 and 4 become a citation of the skill. The border is the run-driver itself, which is the one
written procedure that already runs the method and whose steps 3 and 4 describe the same moments in
prose; the instrument extends what that procedure does per slot and does not stand beside it as a
second description. The plugin's manifest is raised one version.

**What changes for somebody doing the work.** At the moment an artefact is about to be written,
has been written, or has changed, one skill answers what governs it, what to open, what it must take
from its neighbours, and what to run; and the check step ends in a file naming every rule of the
governing standard with a verdict against each — the first claim of its kind the method has
produced.

**What becomes impossible.** Nine near-identical procedures beside the one that runs the method; a
second checking program built in an engagement because the first could not be found; a conformance
claim that is an opinion; and a claim citing the result of a check no program performs.

**What must exist before it.** The register, round M0, which it reads; the checklists, round M1,
which `kit conform` writes from; for a project that was never scaffolded, the project's constants
file with its map of places, which the orchestrator layer's round R3 writes and which is the
per-project half of the lookup.

**How anybody would know.** The seven tests of `01_PROCEDURE.md` §7: a fresh session given only the
skill's path and the kit answers *what governs the entity model* with row 02 resolved; `kit slot
--check` exits 0; `kit conform 06` on one description of the second slice writes a file in
`_conformance/` naming U1 to U21 with a verdict against each; `kit stale 06` on a scratch copy lists
exactly the screen set and the walk-through; the kit copy of the run-driver no longer carries steps
3 and 4 as prose (`grep` for "Step 3" returns the citation line and nothing else); and the plugin
lists `sdd-slot`.

---

## Three · Four clauses, closing the four incomplete handovers

**What it is.** At three of the four broken handovers the thing that crosses already exists and has a
settled form, and what is missing is a name: one sentence on each side citing the other's document,
after which the program that checks that citations resolve keeps the two naming each other without
anybody's attention. At the fourth there is no form at all, and the repair is to declare that the form
is a setting with a name and an owner and no value in the standard. Decision D7 tested the analysis's
placements and amended one; this section drafts the text of each clause and says which section it
joins and what the citation program resolves afterwards. **None of the four is written into any
standard by this round.**

**Where they land, by path.** Five standards are opened, in their build sources under `_standards/_working/`
by the house method — built, compared, the superseded edition archived, the change announced in the
record of what is running — and the clauses land in the built editions as follows. Two of the five,
the standard for the use case model and the standard for the screens, are in force; opening each
produces a new edition, versions 2.1 and 1.1, and a claim of conformance made against the edition
superseded stays a claim against that edition.

**Clause 3a — `_standards/SDD-02_The_Requirements_Catalogue`, the rules on what the register
publishes, RQR-27 to RQR-29, as a sentence following RQR-27.**

> The published list is read by the use case model, which the standard for the use case model
> (SDD-05) governs: its rule M16 binds every goal to entries of this list by identifier, in both
> directions, and no other document is the measure of the goals' completeness.

**Clause 3b — `_standards/SDD-05_The_Use_Case_Model`, rule M16, the requirement binding, as its
second sentence.**

> The list a goal binds to is the register of requirements as published under the standard for the
> requirements catalogue (SDD-02), rule RQR-27 — one named list, in one place, in a form a program
> reads — and the binding names entries by their identifiers in that list and by nothing else.

*Resolves afterwards:* SDD-02 → SDD-05 and SDD-05 → SDD-02, both zero in the chain's citation
matrix today. The check the chain names at handover 3 — every request realised by a goal and every
goal realising a request — can then be told which file is the list.

**Clause 4 — `_standards/SDD-04_The_Shared_Registers`, the rules that govern what a register
publishes, IOS-15 to IOS-18, as a sentence following IOS-15; and the open question the standard
records about its own largest hole, numbered OQ-12 in the recommendation of 12 September, closed by
it.**

> The form in which a register of this standard publishes its set — what a program reading it finds,
> field by field — is a setting, `registers.published_set_shape`, whose owner is the module's
> architect and which carries no value in this standard; each module's catalogue of settings carries
> its value. Every check of part 6 that reads a published set reads the shape the setting names, and
> none of them waits on this document to declare one.

*Resolves afterwards:* no new citation between documents; the citation program resolves the setting's
name against the module's catalogue of settings, which is the standard's own rule for a setting —
named, owned, and carrying no value in the rule that reads it. Route 2 of the four, inside D7.

**Clause 7a — `_standards/SDD-07_The_Screens_of_a_Use_Case`, §13, replacing the sentence that says
a screen set is on none of the links and nothing states where.**

> A set of screens stands on the chain of traceability between the goal it serves and what is built
> from it: the set names the goal's identifier and version, the application model (SDD-09) names the
> set it was compiled from by identifier and version, and the use case model's trace (SDD-05) names
> the link from the goal to its set. A set that no link names is a finding.

**Clause 7b — `_standards/SDD-05_The_Use_Case_Model`, the rule that carries the trace, which the
recommendation of 12 September names as M15 and this round, which did not open that standard, records
as the recommendation's numbering — as a sentence added to that rule.**

> The trace runs from a business goal to its use case, from the use case to the set of screens that
> serves it, governed by the standard for the screens (SDD-07), from that set to the increment that
> builds it, and from the increment to its acceptance tests and to what is built.

*Resolves afterwards:* SDD-07 → SDD-05, SDD-07 → SDD-09, and SDD-05 → SDD-07, all zero today. The
three documents a counterpart is asked to see agreeing — the goal, its screens and the walk-through —
can then be followed by something that traces.

**Clause 11a — `_standards/SDD-09_The_Application_Model`, the section that names what the model is
compiled from, §1 to §2, as the sentence that names the inputs.** This is the amended placement of D7:
the subject is this specification's own, and a sentence in the method standard would leave both sides
naming nothing.

> The model is compiled from the goals written out in full under the standard for one use case
> (SDD-06) and their sets of screens under the standard for the screens (SDD-07), together with the
> entity model (SDD-03) and the architecture specification (SDD-08), each named by identifier and
> version. In the vocabulary of the platform reference (S2C-01) those are the decision inventory, the
> use-case model and the domain model; the two vocabularies name the same documents, and this
> specification cites them by the codes above.

**Clause 11b** is clause 7a: its second clause names the application model as what is built from the
set, so that the giving side names its reader. No further sentence is written into the screens
standard, and none into the standard for one use case, whose §7 already names the set of screens that
serves the goal as the description's downstream.

*Resolves afterwards:* SDD-09 → SDD-06, SDD-09 → SDD-07 and SDD-09 → SDD-03, all zero today, and
SDD-07 → SDD-09 through 7a. The person compiling the model can tell from the standard that governs
it which documents are its input, and the chain, drawn again by the same citation count, shows both
sides of handover 11 naming the same thing.

**What changes for somebody doing the work.** At each of the four they can find, from the standard in
front of them, the document they are supposed to be reading or writing, without asking anybody which
file is meant; and at handover 4 the checks of the shared registers standard stop waiting.

**What becomes impossible.** A use case model measured against a list that no standard names; a set
of screens on no link of the chain of traceability; an application model whose input is named in words
no earlier standard uses; and a standard whose own checks wait on a question it never answers.

**What must exist before it.** The register, round M0, whose resolving program verifies each rebuilt
edition's row afterwards; the text above, as the review of this round leaves it; and, for clause
11a, the owner's answer on the customer copy of the application model specification, because opening
it produces a version 1.2 of a document a customer holds at 1.1 and what a customer is told is his
under section 4 of the constants — the instruction of round M3 carries that question as its decision
paper.

**How anybody would know.** `check_standards.py` of the consistency pass, whose rule R3 checks that
citations resolve — five lines of it name R3, by count at 18:10 UTC — run over the five rebuilt
documents, resolves the new citations and refuses none; the citation matrix of the chain, recomputed
by the inception round's `citations.py`, shows a non-zero cell in each of the eight positions named
above; the chain drawn again from the rebuilt standards shows fourteen handovers with both sides
naming the same thing and no state reading broken; and `kit slot --check` exits 0 with the five rows'
editions raised to 0.2, 0.4, 2.1, 1.1 and 1.2.

---

## Four · A defined starting point for a new piece of work

**What it is.** Two things do part of this today and neither is complete: a note written by hand at
the start of a working day, restating the whole state of an engagement beside the things that change
daily; and a scaffold that renders a folder for each of the eleven things and has never been run. The
addition separates the starting point in two — the constants of a project written once and amended
only by a ruling, and the state never written but produced from the records — and brings the scaffold
level with the standards and runs it on a new piece of work's first day, so that every one of the
eleven things has a place before anything is written into any of them.

**Where it lands.** Three places, two of them the other programme's. The constants: the form
`references/CONSTANTS-template.md` in the travelling layer, written in round R1 of 14 September, and
one instance per project — `_standards/CONSTANTS.md` for this estate, written by the inception round,
and the engagement's, which the orchestrator layer's round R3 writes with its map of places and its
slot map. The state: the register of instructions of round R2b, the record of what is running, and
the refreshed statement of where a project stands that the `project-status` procedure produces. The
scaffold: the register `kit/templates/spec/slots.yaml` brought current and extended in round M0 of
this plan, and `kit spec new` run as the first act of the next new specification. The border for the
scaffold is the method standard's §4 and §5, which the scaffold declares itself sourced from, and the
orchestrator procedure's §8.2, which says the structure is created before work begins from a single
description of what a specification is made of. The scaffold's two changes the orchestrator plan's
R5 names — a place for each of the three kinds of document, and the emitted commission closing
decisions by the four routes — are carried inside M0 by citation, because one body of work opens one
file (D9).

**What changes for somebody doing the work.** A day begins from the constants and from the state as
a command prints it, not from prose; and a new piece of work begins with a rendered tree in which each
slot's README names, from the register, what governs it, what it takes, and where its check is.

**What becomes impossible.** A starting note that restates what has not changed; somebody beginning a
day from prose about the state of a system instead of from the state itself; a new piece of work whose
documents land wherever the first day happened to put them; and a scaffold rendering rules two
editions old.

**What must exist before it.** For the constants and the state, rounds R1, R2b and R3 of the
orchestrator plan, which exist or are planned there and are not planned here. For the scaffold, round
M0 alone.

**How anybody would know.** `kit spec new probe --name Probe --out /tmp/probe` renders eleven slot
folders whose READMEs name EM-1 to EM-56 for slot 02 and IOS-1 to IOS-47 for slot 05, and three
support folders named for the three kinds of document; `grep -r "governed by nothing" /tmp/probe`
returns nothing; the engagement's next initiation note is under a fifth of the last in bytes, which
is R3's own test and is cited.

---

## Five · A clear separation between what is in production and what is being changed

**What it is.** A change to a document of record is described in a place of its own — what is
proposed, the difference line by line, the work it takes, and the report of the work — and touches
the document at one moment only, when the review accepts it; at that moment the difference is folded
in, the edition it replaces is kept where it stood, and everything made from what changed is marked as
no longer current. In this estate three of those four parts already exist under other names —
`_proposals/` holds what is proposed and binds nothing, `rulings/` holds what was decided, and the
house build folds a change in and archives the superseded edition under `x_archive/` — and the
part that does not exist is the fourth: the marking of what became stale, which is obligations 2 and
3 of decision D8.

**Where it lands.** The rule lands in one sentence in `_standards/SDD-01_Specification_Driven_Development`,
in the section that already states that a fault is corrected in the document that owns the fact and
everything below it is produced again — §5, the order of work, which the run-driver calls the
ratchet — as the sentence that says what *produced again* obliges of the document that changed. That
is the only opening of the method standard this design makes, and it is the one the analysis's
seventh part names as travelling with the fourth step. The mechanism lands in the one procedure's
change step, `kit/tools/stale.py`, reached as `kit stale`, which reads the register's `seams.gives`
cells, lists every artefact of the tree made from the changed one with the version each was made
from, marks each one as no longer current, and writes the list into the amendment. The convention
for an engagement's estate — one folder per amendment holding the proposal, the difference, the
tasks and the report, applied on acceptance — is the recommendation of 12 September's item 10 and is
that estate's to adopt; it is a consequence recorded for the engagement and not a round of this plan.
The check that refuses an instruction naming a document of record among its outputs without a change
folder is a consequence for the travelling layer's placement check, round R2a.

**What changes for somebody doing the work.** An amendment is written where amendments are written and
not into the document; the before-and-after snapshot stops being necessary because the difference is
in front of them; and the list of what the amendment made stale is produced for them and attached to
it.

**What becomes impossible.** An amendment applied to a document of record before it has been accepted;
a document out of date only in somebody's memory, because the mark is on the document; a change whose
consequences nobody listed; and the snapshot taken before a change.

**What must exist before it.** The register with its `seams` field, round M0; the skill, round M2,
whose change step calls the program; and for the sentence in the method standard, nothing but the
house build of that standard, whose source exists and is byte-identical to the document in the root.

**How anybody would know.** In a scratch copy of a specification tree, raise the version line of one
description and run `kit stale 06 <that description>`: the output names exactly its set of screens and
its walk-through, each with the version it was made from, and nothing else; each named file now carries
the mark; a rebuilt method standard carries the sentence in §5 and `check_standards.py` reports no new
finding against it; the next amendment in the estate leaves a description of itself and no
`_before_` snapshot.

---

## Six · A small number of mechanical refusals, in place of the seven

**What it is.** Five of the seven obligations of the analysis's part four can be refused by a program
without any judgement, and two can only be made visible to the person who signs. The five: the two
declarations at a handover are compared before a single result is read, and a disagreement stops the
reading; the acceptance of an amendment runs every check that reads anything made from what it
changed and prints the list of what is now stale; a piece of work may not be closed without a record of
where it stands; the standing list of the ways work fails lives in the written procedure, and the
procedure is refused when its forms no longer match the work; and, beneath them all, one field on
every report saying which party answered it. The two visible steps: a line on the report naming the
handovers of the schema the round crossed, and a line per lesson on the review naming what the lesson
became. Decision D8 places each once.

**Where it lands.** Five in the travelling layer, the orchestrator skill of the owner's project-operations plugin, which is not part of sdd-kit:
the field, in `references/REPORT-template.md` since round R1; the comparison of declarations, in
`scripts/trace_check.py`, round R2a; the running-record refusal, in `scripts/placement_check.py`,
round R2a; the forms-match-the-work refusal, in the same program as one further comparison, a
consequence for R2a; and the two visible lines, one on `references/REPORT-template.md` and one on
`references/REVIEW-template.md`, consequences for those forms. One in this programme: the stale list,
`kit stale`, the fifth addition's mechanism, round M4. The border for the five is the orchestrator
procedure itself, whose §2.3, §2.5.2 and §11 already name the trace check and the placement check and
say none of them stops a round; the border for the one is the run-driver's own rule that a fault is
corrected above and everything below is produced again.

**What changes for somebody doing the work.** A report that answers a neighbouring instruction is
sent back before its results are read; an amendment comes back with the list of what it made stale;
a round cannot be closed while its row stands open; and an instruction not written from the form is
reported as such.

**What becomes impossible.** A report read as though it answered the instruction it did not answer; a
change to a document of record whose consequences nobody listed; a piece of work closed with no record
of where it stood; and a written procedure that has quietly stopped describing the practice it governs.

**What must exist before it.** Rounds R1 (done), R2a and R3 of the orchestrator plan, which own five
of the six places; rounds M0 and M2 of this plan for the sixth.

**How anybody would know.** The orchestrator plan's own tests for R2a, cited: each self-test fails on
its defective case and passes on its sound case; the trace check fed a report with one character of
its declaration changed exits 1; the placement check fed an instruction with no running-record line
reports it. For the sixth, the test of the fifth addition. And for the whole: the refusals, fed the
work of a week already finished, refuse exactly those pieces that broke the rule and nothing else,
which is the analysis's own test for its first step.
