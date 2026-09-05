# The seven documents

These structures come from the scripts of KP1 Modules 1, 3 and 5, and from the convention
for a decision log. Draft from these structures. Do not draft from your knowledge of
governance documents.

---

## 1. EA Governance Board — Terms of Reference (1.7, 3.4)

| § | Section | What goes in it |
| --- | --- | --- |
| 1 | **Purpose** | Why the Board exists, and what it governs. Write two paragraphs. |
| 2 | **Binding decision scope** | Five to eight *specific types of decision*: a new digital project above a stated threshold; approval of an integration that crosses domains; a technology selection that creates a dependency on a vendor; an exception to the architecture; a dispute about the ownership of a data domain. **Each type cites the instrument that gives the Board its authority over that type.** |
| 3 | **Membership** | The chair, who is the CDO or CTO or the political equivalent; the permanent members, who are the sector CIOs, the owners of the main registries, and the data-protection regulator; and an external advisor, if the Board wants one. Write each member **by post**. Carry the status tag from the roles register. If the post of a member has the tag *gap*, name it as an appointment that the government must make. |
| 4 | **Cadence** | A main meeting each quarter, and a fast path for an urgent decision, with its own trigger and its own quorum. |
| 5 | **Reporting line** | The body that the Board reports to, and what the Board reports. |
| 6 | **Escalation** | How the Board escalates a decision that it cannot make, to whom, and in what period. |
| 7 | **Mandate review** | How frequently a body reviews the ToR, and which body does it. |

**Where the authority comes from.** Section 2 is the document. Quote the instrument and the
section behind each type of decision. If the mandate of the coordinating body is
*coordinating* and not *binding*, say so plainly, and draft the alternative: a spending gate,
a condition in a procurement, or a cabinet directive. A ToR that claims an authority that no
instrument gives is worse than no ToR. A person tests it one time, and then people ignore it.

**The characteristic failure:** there is no quorum and no path for escalation, and the scope
of the decisions is a list of areas of interest, such as "digital transformation", and not a
list of types of decision, such as "approval of any ICT procurement above X". An area of
interest binds nobody.

**End with the four asks**, which are what the learner needs from the minister, when the
document is for play 1.7.

---

## 2. Phase RACI and role-gap list (1.6)

Write five rows, one for each phase of the lifecycle: Discover, Assess, Adapt, Plan, and
Execute and Govern. Fill the R, A, C and I columns **by post**, from the roles register.

Then write the part that matters more than the matrix:

```
| Role gap | Phase it blocks | Why it blocks | Resolution options (2-3) |
```

The August 2026 run found six gaps where the template expected five. Each gap had the phase
that it blocked and the options to resolve it. Do the same. A gap with no named phase and no
options is a complaint. It is not a finding.

**Write one Accountable post for each phase.** Two Accountable posts is the characteristic
failure. It means that nobody is accountable.

**The characteristic failure:** you give R or A to a post that the roles register tags as
*gap*, and you do not flag it. The matrix then looks complete, and it is a fiction.

---

## 3. EA repository structure (3.1)

Write a schema, section by section. The minimum sections are **Capabilities · Data Domains ·
Applications · Technology · Decision Log**.

For each section, give the fields that it holds. Across the sections, give the relationships
to record. **Use the entity names of the PAERA metamodel.** Check the names with
`paera-reference-check`. Do not invent a label.

The schema must contain these two rules:

- **One named owner for each data domain.** The owner is a post, not a body. A domain with no
  owner is the duplicate registry that has not happened yet.
- **Each application maps to a capability and to a data domain.** An application that maps to
  neither is an orphan. To find the orphans is half of the purpose of the repository.

Then write the **rules for a single source**: who can edit, how the repository records a
change, and how it stops a second copy. The third rule is the difficult one, and it is a rule
about people and not about the tool. Say what happens when a person sends an extract in a
spreadsheet to other people.

**The characteristic failure:** the repository is an inventory and not a portfolio. It lists
each system, it records no relationship, and nobody can decide anything from it.

---

## 4. Repository update policy (3.3)

Write one page with four headings:

1. **The single owner who is accountable that the repository is current.** One post. Not a
   committee.
2. **The events that trigger an update, and what each event updates.** The events are: a
   system goes live; a body retires a system; a government reorganises; the Board takes a
   decision; a body creates a registry. Each trigger names the exact fields to update.
3. **The light conformance check for each change**: the change uses the shared entities, each
   data domain has one owner, and the log records each decision with its reason.
4. **How the gate for a project review captures the updates**, so that governance and update
   are one action and not two jobs.

**The characteristic failure:** a policy with no trigger, that says "the repository shall be
kept current". Currency is an obligation that an event drives, or it is nothing.

---

## 5. Architecture review gate checklist (3.5)

Write four parts:

1. **The questions at intake.** As a minimum: does a shared block exist for this, from the BB
   status register; which data domains does the project touch, and does it use the copy of
   the owner; does it meet each principle that the country adopted; is the sourcing choice
   deliberate; can the system export to an open format.
2. **What a pass looks like** for each question. A question with no criterion for a pass is a
   conversation. It is not a gate.
3. **The form for an exception** — the reason, the block that the project does not use, a
   **sunset date**, and who approved it. An exception with no sunset date is a permanent
   decision that somebody took quietly.
4. **The fields for the decision log** that the repository records, so that the gate feeds
   part 4 above.

**A gate can point only at blocks that exist.** Build the questions at intake from the BB
status register. Do not build them from the strategy.

**The characteristic failure:** there is no condition that fails. If nothing can fail the
gate, the gate is a form.

---

## 6. EA health scorecard (3.6)

Write one page each quarter. Give **four metrics**. Give a definition of one line for each
metric, and say how to calculate it from the data that the practice has.

| Metric | Definition |
| --- | --- |
| **Coverage** | How much of the estate the repository describes |
| **Re-use rate** | The projects that use a shared block, against the projects that could use one |
| **Open exceptions** | The count **and the age**. The age is the true signal |
| **Decisions** | The count, and the **time to a decision** |

Give a red, amber and green threshold for each metric. **Set the thresholds honestly.** A
threshold that nobody can fail measures nothing.

Then write a section with the title **"what is not working"**, which names the gaps and does
not hide them. Then write the **story of one line for the minister**.

**Use no vanity metrics.** These are vanity metrics: pages, diagrams, models, meetings held,
and attendance. They increase when nothing improves. A scorecard changes behaviour. Measure
re-use, and people will pursue re-use.

**The characteristic failure:** the scorecard measures activity instead of re-use.

---

## 7. Sustainment risk register (3.7 for the practice, 5.2 for the programme)

Give the four fade modes. For play 3.7, which is about the practice, the fade modes are:
somebody moves the team onto urgent delivery; the repository becomes stale; the Board becomes
advisory; the sponsor changes. For play 5.2, which is about the programme, the fade modes
are: somebody moves the team onto delivery; the sponsor changes; the governance becomes
advisory; the funding becomes a favour that a body grants each year.

```
| Fade mode | Likelihood (in this context) | Impact | Counter-move | Owner of the counter | Early-warning signal |
```

Then write the **early-warning signals** as their own list. They are the operational output,
and a person checks them each month:

- the number of months since the last meeting of the Board;
- the number of weeks since the last update of the repository;
- the number of overrides or exceptions in this quarter;
- the number of weeks since the team last did architecture work and not delivery work;
- whether the funding is still an envelope for several years, or has become a line for one
  year.

Give the likelihood and the impact **in this context**, not in general. A change of sponsor
is almost certain inside an electoral cycle, and the register must say so.

**The characteristic failure:** no risk has an owner, and nobody can observe the signals.
Each signal above is a number that a person can find in five minutes. That is the test.
