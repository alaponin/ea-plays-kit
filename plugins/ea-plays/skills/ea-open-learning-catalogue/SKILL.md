---
name: ea-open-learning-catalogue
description: >-
  Build a plan to develop the capability of a team, from open learning materials. On the day
  that the plan is written, check that each item resolves. Give each item a URL and a
  "checked on" date, and flag each item that is behind a paywall, that moved, or that is
  stale. Serves play 5.5. Use when someone says "how do I build my team's capability", "what
  should my architects learn", "training plan for the EA team", "free EA and DPI learning
  resources", "onboard a new architect", "what courses exist for government enterprise
  architecture", "capability plan for the minister". Reads the PAERA site, the GovStack
  specifications and learning material, the ITU Academy, the DPGA registry, the Knowledge
  Product video playlists and GitBook, and the World Bank Open Learning Campus. Returns a
  plan in sequence by role and by starting point, what to fund, and how to keep the
  capability after the team has it. The true cost is the time of the team, not the
  materials, and the true risk is that the architect you trained leaves.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
---

## What this skill does

This skill makes the learning sequence for play 5.5. It **verifies that each item exists on
the day that it writes the plan**.

The safeguard of the play says: *confirm the specific materials exist and are current*.
Links to open learning material break quickly. Nobody uses a plan a second time when its
first three links are dead.

## Inputs

The skill needs the size of the team and the background of each member. Give the number of
people, and the starting point of each one: a developer, a policy officer, a statistician, a
project manager, or a new graduate.

If the learner has A6, the RACI and role-gap list, read it. **The plan must close the role
gaps.** Nobody funds a plan that trains people for roles that the programme does not need.

If you do not know the size of the team, ask one time. Ask it with your other questions. Ask
a maximum of three questions at the same time, and record the answers in the output.

## Procedure

1. **Read every item before you list it.** Read all of them, not a sample. Record the URL,
   the **checked on** date, and whether the page opened. This step is the purpose of the
   skill.

2. **Record these items for each entry**: what it is, who it is for, how long it takes,
   whether it is free, whether the learner must register, and whether it gives a credential.
   "Free but requires an institutional email" is a true barrier. Put it in the table.

3. **Give each item one of four states**, as `references/learning-sources.md` defines them:
   **current** · **stale**, which means that it exists but its content is about a version
   that is superseded · **paywalled**, which includes items that a publisher moved behind a
   paywall recently · **moved or gone**. For each item that moved or is gone, do one search
   for its new location. If you do not find it, say so.

4. **Put the items in sequence by role and by starting point. Do not sequence them by
   topic.** A policy officer and a developer do not start at the same place. A sequence that
   ignores this is a reading list. Three tracks are usually correct: the foundations of
   architecture, the specifications, which are PAERA and GovStack, and the method.

5. **Name the three layers.** Say what the team learns from **open materials**, what needs
   **instruction or a mentor**, and what comes only from **doing the work** with a person
   who has experience. Most of the capability of an architect is in the third layer. A plan
   that says something different makes the time much too short.

6. **Say what to fund.** Usually this is not the materials, because they are free. These
   items cost money: time that nobody can take away; a mentor or an architect with
   experience for the first sector; the fees for a certification exam, if the team needs a
   credential; and travel to the one workshop that is worth a journey.

7. **Say how to keep the capability.** A trained architect can find another job more easily.
   Plays 3.7 and 5.2 both name this fade mode. These devices help: work that is interesting;
   a career path that lets a person get a promotion and stay in architecture; and pair work,
   so that the capability is in two heads and not one.

8. **Run `cite-or-discard` on the list.** Here it is almost the full procedure, because the
   verification is the deliverable.

## Output contract

Write the provenance header first (`references/provenance-header.md`). Then write these six
sections.

**Learning sequence**

```
| # | Item | Source | For whom | Time | Free? | Registration? | Credential | Status | URL | Checked on |
```

The status is current, stale, paywalled, or moved or gone.

**The three tracks** — foundations, specifications and method. Give the items of each track
in order, and the starting point that each track assumes.

**The three layers** — open materials, instruction, and learning by doing. Give what belongs
in each layer, and how much of the capability each layer gives.

**What to fund** — a short list with a reason for each item. Put time first.

**How to keep it** — the fade mode, and the two or three devices against it.

**Could not verify** — each item that did not open, and where it appears to have moved.

Write text in the chat. Do not make a file. Write no analysis before the header. See
`references/output-contract.md`.

## Safeguard handed back

**This plan assumes that the open materials cover what you need. Confirm that they do before
you use them. Budget the time of the team honestly. That time is the true cost, and people
make it too small more than any other item.**

- **Open one item in each track yourself** before you send the plan to other people. A
  "checked on" date says that the URL opened. It does not say that the content is good, or
  that it is current for your context.
- **Budget the time in days, not in hours**, and protect it. Learning that competes with
  delivery loses each time. This is the first fade mode in the sustainment register.
- **Open materials teach the framework. They do not teach your country.** The judgement
  comes from doing the work with a person who has done it before. That judgement includes
  which body owns which domain, and which trade-off can survive politically. Plan for that
  person.
- **Check the links again before you use the plan a second time.** In six months, a third of
  them move.

## References

- `references/learning-sources.md` — the sources to check, what each one gives, and the
  traps for registration and currency in each one.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` — the shared contract.
