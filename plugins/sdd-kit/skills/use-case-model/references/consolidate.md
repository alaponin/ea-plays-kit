# The consolidate step: several sources into one model

The step before prepare, when more than one document claims to describe the same system and they
do not agree: "we have several versions of the model", "make an inventory of the inputs", "these
two specs contradict each other", "which source wins", "consolidate these into one", "resolve the
conflicts", "unify the requirements". It produces the register, the dispositions and the rulings
the single model is then prepared and written under.

*This is the text of the retired skill `ucm-consolidate`, kept as the consolidate step of this
skill. It names no standard and has not drifted; one paragraph is added under "What comes next",
the vocabulary of its checker is neutral, and the names of the two retired skills it handed to
are replaced by this skill's own moments.*

The situation: three, five, a dozen documents that overlap. Two of them are
versions of the same model that have diverged. One is authoritative and nobody
has said so out loud. Several contradict each other on things that matter, and
on many more things that do not.

The temptation is to start writing the unified model and resolve disagreements
as you meet them. Do not. You will resolve them inconsistently, you will resolve
some silently that were the owner's to decide, and nobody afterwards — including
you — will be able to say why the model says what it says.

Four stages, in order. Each produces an artefact the next one consumes.

---

## Stage 1 — the input register

**Every** source, before any of them is read for content. For each:

| Column | Why |
|---|---|
| Reference | a stable short id you will use in every later artefact |
| What it is | one line |
| Authority | who wrote it, under what mandate |
| Date and version | two renditions of one document with crossing section numbers is normal, and finding it out late is expensive |
| Status | current, superseded, draft, unknown |
| Overlap | which other inputs cover the same ground |
| **Absorption** | fully absorbed / partly absorbed / not absorbed / not applicable |

The absorption column is the one that earns the register. At the end you must be
able to say, of every input, what happened to it. "Not absorbed, and here is
why" is a perfectly good answer; silence is not.

Also record, separately:

- **Pointer rows** — where each input says something about a topic, so the
  consolidation can find the fragments of one subject scattered across five
  documents.
- **Obligations** — things a source imposes that are not about content: a
  format, a naming convention, a review step, a constraint on the work itself.
  They are easy to lose because they belong to no section.

> Check the physical documents, not their names. A guide that exists in two
> renditions with different section numbering will produce a citation that is
> wrong in a way nobody spots for months. Establish which rendition is being
> cited, and say so in the register.

## Stage 2 — the precedence order

**Before any conflict is disposed of, write down which source wins.**

State it as a short ordered list with the reason for each rank, and treat it as a
standing rule that everything afterwards is written under. Typically:

1. The methodology or standard the work must not contradict.
2. The domain-expert or advisory material, where the first is silent and does
   not contradict.
3. Everything else, carried only where neither of the above speaks.

Two consequences worth stating explicitly:

- A source ranked below another does not lose everything. It loses *where they
  conflict*. Where the higher source is silent, the lower one still speaks.
- Ranking is not quality. A lower-ranked source may be more detailed, more
  recent and better written. Rank is about authority, not merit, and saying so
  in the artefact prevents the argument.

## Stage 3 — dispose of every conflict

Enumerate the conflicts as a register — `CF-1`, `CF-2` — each with the topic,
what each source says, and a citation into each. Then give every one a **verdict
class**:

| Verdict | Meaning | Who decides |
|---|---|---|
| **Settled by the ranking source** | the top source speaks and the conflict evaporates | nobody — it is already decided |
| **Narrowed** | the ranking source constrains the answer without fixing it; the remaining choice is smaller and stated | you, within the constraint |
| **Settled by the second source** | the top source is silent and does not contradict | nobody |
| **Owner's to rule** | the sources genuinely differ on something only the owner can decide | the owner |
| **Third-party** | the answer belongs to someone outside this work | referred, with a named recipient |
| **Not a conflict** | on inspection the two sources are talking about different things | you, with the reasoning recorded |

Two rules about this table:

- **Every conflict gets a class.** A conflict left undisposed becomes a silent
  decision by whoever writes that paragraph.
- **"Not a conflict" needs its reasoning recorded**, because it is the class
  most often assigned in error, and the one nobody re-checks.

Then two more registers:

- **Divergences** — where the consolidated model will differ from a source that
  is not overruled. Each with its justification. This is the list a reviewer
  from that source's side will ask for.
- **Obligations** — carried forward from stage 1, each with its disposition.

## Stage 4 — the owner rules

Only the *owner's-to-rule* conflicts go to the owner, and they go as a
questionnaire, not as a chat message or a table in a report. Use the
**decision-questionnaire** skill where it is installed; that is precisely what it is for.

**Put a recommendation on every card.** An owner asked to choose between two
options with no view from the person who did the analysis is being asked to do
the analysis again. Give the recommendation and the reasoning; they can
overrule it in a sentence, which is much cheaper for them than deciding cold.

Expect two things back, and welcome both:

- **A card rejected as the wrong question.** "This has no relevance to a use
  case model" is a correct and useful answer — it means the question belonged to
  a different artefact, usually a configuration or an implementation concern.
  Withdraw the card and record why.
- **A ruling that corrects your framing.** The owner knows their domain. When
  the answer comes back with a note explaining that the roles do not work the
  way you assumed, that note is worth more than the ruling.

Record the answers as a **rulings record**: an identifier per ruling, what was
asked, what was ruled, the owner's own words where they added any, and where in
the model each ruling is applied. The record is what makes the model defensible
six months later, when someone asks why it says what it says.

Ship the rulings record with the standing rules at the top. It is the document
the model of record is written under.

---

## The gate

```bash
python3 scripts/check_registers.py --inventory inventory.md \
                                   --disposition disposition.md \
                                   --rulings rulings.md
```

Every argument is optional, so the checker is useful from the first artefact.
It enforces the arithmetic of the consolidation and nothing about its judgement:
every input carries an absorption verdict; every conflict the inventory raises
has a row in the disposition register; every conflict carries a verdict from the
closed vocabulary; every conflict sent to the owner has a ruling; every ruling
answers a conflict that exists; no identifier is duplicated or silently skipped.

**The two vocabularies default to the words of the two tables above**, and the
checker prints the vocabulary it used. Where a register uses words of its own,
pass them with `--verdicts`, `--owner-verdict` and `--absorption`: run with the
wrong vocabulary, the checker reports every healthy row as a hole — which is
exactly what it did the first time it was run, on a consolidation that was in
fact closed. `examples/consolidation/` beside this skill is a closed consolidation
of three fictitious sources to run it against first.

## What the finished consolidation looks like

Five artefacts, and the model is prepared from all five:

1. The input register, with absorption status for every input.
2. The precedence order, as a standing rule.
3. The conflict register, every conflict classed and disposed of.
4. The divergence and obligation registers.
5. The rulings record.

The test of the set is a question: **pick any sentence of the finished model and
ask why it says that.** The answer should be a source, a precedence rank, a
disposition or a ruling — reachable in one step. If the answer is "because that
seemed right", the consolidation has a hole in it.

## Errors this stage is prone to

**Stating a claim wider than the evidence behind it.** A command that lists the
sections of a source prints 45 of 55 and gets read as complete; the report says
the guide has 27 sections when it has 33. Before writing a count into an
artefact, count it a second way. The cost of the second count is seconds; the
cost of a wrong count in a register everything downstream cites is that every
later citation is suspect.

**Accusing a source of a defect on a naive parse.** Twenty-one stray `F-n`
references reported as an undocumented second findings series; they were
ordinary row citations in an existing section. Before reporting that a source is
inconsistent, read the passage. A withdrawn accusation costs more credibility
than the finding was worth.

**Mis-attributing a section to the wrong document** when several sources have
sections of the same number. Cite `<input reference> §n`, never bare `§n`. This
is the whole reason the input register assigns short references in stage 1.

**Resolving an owner's decision quietly.** The commonest and the most damaging.
If two sources differ on something that changes what people do, it is the
owner's, however obvious the answer looks from here.

## What comes next

- **The prepare moment of this skill** — the single model of record, written under the
  precedence order and the rulings.
- **decision-questionnaire**, where it is installed — the surface the owner answers on.
- **The render moment of this skill** — the reviewable document, once the model exists.

**In an estate run under the orchestrator's procedure**, the model is then prepared and written
to the standard for use case models by this skill, the rulings record is filed in the estate's
`rulings/` folder under its constants, and no question goes to the owner as a list: each
owner's-to-rule conflict is closed by one of the four routes of that procedure's section 5
(answered from a document in force, made a named setting, decided by taking the recommendation,
or recorded as a consequence for another document), and reaches the owner only as a short paper
when there is a finished document to look at.
