---
name: ea-open-learning-catalogue
description: >-
  Build a team capability-building plan from open learning materials, checking on the day it
  runs that every item actually resolves — each with a URL and a "checked on" date, and
  anything paywalled, moved or stale flagged. Serves play 5.5. Use when someone says "how do
  I build my team's capability", "what should my architects learn", "training plan for the
  EA team", "free EA and DPI learning resources", "onboard a new architect", "what courses
  exist for government enterprise architecture", "capability plan for the minister". Reads
  the PAERA site, GovStack specifications and learning material, the ITU Academy, the DPGA
  registry, the Knowledge Product video playlists and GitBook, and the World Bank Open
  Learning Campus. Returns a sequenced plan by role and starting point, what to fund, and
  how to retain the capability once it exists — because the real cost is the team's time,
  not the materials, and the real risk is the trained architect leaving.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
---

## What this skill does

Produces the learning sequence for 5.5, with every item **verified to exist on the day the
plan is written**. The play's safeguard is *confirm the specific materials exist and are
current*; link rot in open learning material is fast, and a plan whose first three links are
dead is not used twice.

## Inputs

Team size and the members' backgrounds — how many people, and where each is starting from
(a developer, a policy officer, a statistician, a project manager, a new graduate). If the
learner has A6, the RACI and role-gap list, read it: **the role gaps are what the plan has
to close**, and a plan that trains for roles the programme does not need is a plan nobody
funds.

If team size is unknown, ask once, alongside any other question — no more than three at
once, recorded in the output.

## Procedure

1. **Fetch every item before listing it.** Not a sample. Record the URL, the **checked on**
   date, and whether it resolved. This is the whole point of the skill.

2. **For each item record**: what it is, who it is for, roughly how long, whether it is
   free, whether registration is required, and whether it carries a credential. "Free but
   requires an institutional email" is a real barrier and belongs in the table.

3. **Flag four states**, per `references/learning-sources.md`:
   **current** · **stale** (exists, but its content refers to a superseded version) ·
   **paywalled** (or newly paywalled) · **moved or gone**. For anything moved or gone, spend
   one search on where it went, and say if you could not find it.

4. **Sequence by role and starting point**, not by topic. A policy officer and a developer
   do not start in the same place, and a sequence that ignores that is a reading list.
   Three tracks is usually right: architecture foundations, the specifications
   (PAERA, GovStack), and the method.

5. **Name the three layers**: what the team learns from **open materials**, what needs
   **taught instruction or mentoring**, and what only comes from **doing the work** with
   someone experienced. Most of an architect's capability is in the third layer, and a plan
   that pretends otherwise underestimates the time by a factor.

6. **Say what to fund.** Usually not the materials — they are free. What costs money:
   protected time; a mentor or an experienced architect for the first sector; the
   certification exam fees if a credential is required; and travel to the one workshop that
   is worth attending in person.

7. **Say how to retain the capability.** A trained architect is more employable and this is
   the fade mode 3.7 and 5.2 both name. Retention devices: the work itself being
   interesting, a career path that does not require leaving architecture to be promoted, and
   pairing so that capability sits in two heads rather than one.

8. **Run `cite-or-discard`** over the list. Here it is nearly the whole procedure — the
   verification *is* the deliverable.

## Output contract

Provenance header first (`references/provenance-header.md`), then:

**Learning sequence**

```
| # | Item | Source | For whom | Time | Free? | Registration? | Credential | Status | URL | Checked on |
```

Status: current / stale / paywalled / moved or gone.

**The three tracks** — foundations, specifications, method — with the items in order per
track and the starting point each assumes.

**The three layers** — open materials / taught instruction / learning by doing, with what
belongs in each and roughly what share of the capability each carries.

**What to fund** — a short list with the reason. Time first.

**How to retain it** — the fade mode, and the two or three devices against it.

**Could not verify** — every item that did not resolve, and where it appears to have gone.

Text in the chat. No file. No reasoning before the header. See
`references/output-contract.md`.

## Safeguard handed back

**The plan assumes the open materials cover your needs. Confirm they do before relying on
them, and budget honestly for the team's time — that is the real cost and the one most often
underestimated.**

- **Open one item per track yourself** before circulating the plan. A "checked on" date
  means the URL resolved, not that the content is good or current for your context.
- **Budget the time in days, not hours**, and protect it. Learning that competes with
  delivery loses every time — which is the first fade mode in the sustainment register.
- **Open materials teach the framework, not your country.** The judgement — which body owns
  which domain, which trade-off is politically survivable — comes from doing the work with
  someone who has done it before. Plan for that person.
- **Re-check the links** before the plan is reused. Six months is enough for a third of them
  to move.

## References

- `references/learning-sources.md` — the sources to check, what each offers, and the
  registration and currency traps in each.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` — the shared contract.
