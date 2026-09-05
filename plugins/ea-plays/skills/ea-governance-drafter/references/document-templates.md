# The seven documents

Structures taken from the KP1 Module 1, 3 and 5 scripts and the decision-log convention.
Draft from these, not from what a governance document generally looks like.

---

## 1. EA Governance Board — Terms of Reference (1.7, 3.4)

| § | Section | What goes in it |
| --- | --- | --- |
| 1 | **Purpose** | Why the Board exists and what it governs. Two paragraphs. |
| 2 | **Binding decision scope** | Five to eight *specific decision types* — new digital projects above a stated threshold; cross-domain integration approvals; technology selections creating vendor dependency; exceptions to the architecture; data-domain ownership disputes. **Each one cites the instrument that gives the Board authority over it.** |
| 3 | **Membership** | Chair (the CDO/CTO or political equivalent), permanent members (sector CIOs, major registry owners, the data-protection regulator), optional external advisor. **By post.** Carry the roles register's status tag: a member post tagged *gap* is named as a required appointment. |
| 4 | **Cadence** | Quarterly main meetings plus a fast ad-hoc path with its own trigger and quorum. |
| 5 | **Reporting line** | To whom the Board reports up, and what it reports. |
| 6 | **Escalation** | How a decision the Board cannot resolve is escalated, to whom, and within what period. |
| 7 | **Mandate review** | How often the ToR itself is reviewed, and by whom. |

**Where authority comes from.** §2 is the document. Quote the instrument and section behind
each decision type. Where the coordinating body's mandate is *coordinating* rather than
*binding*, say so plainly and draft the alternative: a spending gate, a procurement
condition, a cabinet directive. A ToR that asserts authority no instrument grants is worse
than no ToR — it will be tested once and then ignored.

**Characteristic failure:** no quorum, no escalation path, and a decision scope written as
areas of interest ("digital transformation") rather than decision types ("approval of any
ICT procurement above X"). Areas of interest bind nobody.

**Close with the four asks** — what the learner needs from the minister — where this is 1.7.

---

## 2. Phase RACI and role-gap list (1.6)

Five rows, one per lifecycle phase (Discover, Assess, Adapt, Plan, Execute & Govern), with
R / A / C / I columns filled **by post** from the roles register.

Then, the part that matters more than the matrix:

```
| Role gap | Phase it blocks | Why it blocks | Resolution options (2-3) |
```

The August 2026 run produced six gaps where the template expected five, each with
"blocking from phase N" and resolution options. Reproduce that: a gap without a named
blocked phase and options is a complaint, not a finding.

**One Accountable per phase.** Two Accountables is the characteristic failure, and it means
nobody is.

**Characteristic failure:** assigning R or A to a post tagged *gap* in the roles register
without flagging it. The matrix then looks complete and is fiction.

---

## 3. EA repository structure (3.1)

Section-by-section schema. Minimum sections: **Capabilities · Data Domains · Applications ·
Technology · Decision Log.**

For each section: the fields it captures. Across sections: the relationships to record,
**using PAERA metamodel entity names** — check them with `paera-reference-check` rather than
inventing labels.

Two rules the schema must encode:

- **One named owner per data domain.** Not a body — a post. A domain with no owner is the
  duplicate registry that has not happened yet.
- **Applications map to capabilities and to data domains.** An application that maps to
  neither is an orphan, and finding orphans is half of what the repository is for.

Then **single-source rules**: who may edit, how a change is recorded, and how second copies
are prevented. The third is the hard one and it is a rule about people, not the tool: name
what happens when someone circulates a spreadsheet extract.

**Characteristic failure:** an inventory rather than a portfolio — every system listed, no
relationships recorded, nothing decidable from it.

---

## 4. Repository update policy (3.3)

One page, four headings:

1. **The single owner accountable for currency.** One post. Not a committee.
2. **Trigger events, and what each updates.** Systems going live; systems retired;
   reorganisations; Board decisions; new registries. Each trigger names the exact fields.
3. **The light conformance check** applied to every change: shared-entity use, one owner per
   data domain, decisions logged with reasons.
4. **How updates are captured at the project-review gate**, so governance and update are one
   motion rather than two jobs.

**Characteristic failure:** a policy with no trigger — "the repository shall be kept
current". Currency is an event-driven obligation or it is nothing.

---

## 5. Architecture review gate checklist (3.5)

Four parts:

1. **Project-intake questions.** At minimum: does a shared block exist for this (from the BB
   status register); which data domains does it touch, and does it consume the owner's copy;
   does it meet each adopted principle; is the sourcing choice deliberate; can it export to
   an open format.
2. **What a pass looks like** for each question. A question with no pass criterion is a
   conversation, not a gate.
3. **The exception form** — reason, the block it bypasses, a **sunset date**, who approved.
   An exception with no sunset date is a permanent decision taken quietly.
4. **The decision-log fields** recorded in the repository, so the gate feeds §4 above.

**A gate can only point at blocks that exist.** Build the intake questions against the BB
status register, not against the strategy.

**Characteristic failure:** no fail condition. If nothing can fail the gate, the gate is a
form.

---

## 6. EA health scorecard (3.6)

One page, quarterly. **Four metrics**, each with a one-line definition and how to compute it
from the data the practice actually has:

| Metric | Definition |
| --- | --- |
| **Coverage** | How much of the estate the repository describes |
| **Re-use rate** | Projects consuming a shared block, against projects that could have |
| **Open exceptions** | Count **and age** — age is the real signal |
| **Decisions** | Count and **time-to-decision** |

Each gets a red/amber/green threshold, **set honestly** — a threshold nobody can fail
measures nothing.

Then a **"what's not working"** section that names gaps rather than hiding them, and the
**one-line story for the minister**.

**No vanity metrics.** Pages, diagrams, models, meetings held, attendance. They rise
without anything improving, and a scorecard changes behaviour — measure re-use, and re-use
is what people will pursue.

**Characteristic failure:** measuring activity instead of re-use.

---

## 7. Sustainment risk register (3.7 practice, 5.2 programme)

The four fade-modes. For 3.7 (the practice): the team pulled onto urgent delivery; the
repository going stale; the Board drifting to advisory; the sponsor changing. For 5.2 (the
programme): the team pulled onto delivery; the sponsor changing; governance drifting to
advisory; funding becoming an annual favour.

```
| Fade mode | Likelihood (in this context) | Impact | Counter-move | Owner of the counter | Early-warning signal |
```

Then the **early-warning signals** as their own list, because they are the operational
output — the thing someone checks monthly:

- months since the last Board meeting;
- weeks since the last repository update;
- overrides or exceptions granted this quarter;
- weeks since the team last did architecture rather than delivery work;
- whether funding is still a multi-year envelope or has become an annual line.

Likelihood and impact are **in this context**, not in general. "The sponsor changing" is
near-certain within an electoral cycle and the register should say so.

**Characteristic failure:** no owner per risk, and signals that cannot be observed. Every
signal above is a number someone can look up in five minutes; that is the test.
