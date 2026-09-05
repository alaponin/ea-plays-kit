# Plan — one fixture country, explicitly tagged

**Date** 2026-09-05 · **Status** proposed · **Target release** 0.1.1 (patch — reference
fixes only; no skill contract changes)

## Problem

The review of 2026-09-05 found two things.

1. **Progressa has forked.** The canonical fixture is `tests/progressa.md`. Two skills carry
   their own Progressa in `references/` and it disagrees with the canonical page:
   - `bdat-assessor/references/worked-example.md` — "Youth and *Sport*" (fixture: *Skills*);
     PDGA "runs payments infrastructure" (fixture: Central Bank runs PayPro); PLR modelled as
     an operating body with an enrolment system (fixture: *planned, not started* — the
     absence of PLR *is* the sector problem).
   - `ea-institution-mapper/references/paera-a1-2.md` — cites an "Establishment Decree
     2019 §3" for PDGA that the fixture does not contain.
   A learner running 2.5 with the fixture pasted and the worked example loaded gets two
   Progressas at once. Nothing tags the material as fixture content and nothing checks it.

2. **The Gambia leaks into the plugin.** The 30 Aug 2026 test runs were on The Gambia and
   the real country has ended up in three places it should not be:
   - `shared/provenance-header.md` — the canonical example header says `**Country** The
     Gambia`, two lines above the rule "`Progressa` for fixture runs". `sync-shared.sh` has
     copied it into all fourteen skills.
   - `bb-sourcing-researcher/references/worked-example.md` — a full real-country worked
     example, while `bdat-assessor`'s is Progressa. Two example-country conventions.
   - `tests/plays/1.1–1.8/gambia.md` — eight baselines the checker never reads, covering 8
     of 38 plays, excerpted from a synthesis document that is in no repo. Documentation of
     a manual acceptance step, not a fixture; real-country material in a public CC BY kit.

   Legitimate Gambia mentions that **stay**: `ea-comparator-evidence/references/known-
   frameworks.md` (one comparator among several) and `country-context-pack/references/
   api-guide.md` (a source list).

## Principles

- **One Progressa.** `tests/progressa.md` is the only source of Progressa facts. Anything
  in `plugins/` that names Progressa or its bodies derives from it and must agree with it.
- **Tag files, not skills.** A skill is not "a Progressa skill"; a *file* contains fixture
  material. Worked examples stay inside skills because the standalone-upload route has no
  `tests/`, so each such file declares itself.
- **Enforce, don't request.** "Do not diverge" becomes a failing check in
  `check_fixtures.py`, run by CI.
- **The fixture tree is one-country.** `tests/plays/*` contains Progressa only.

## Work items

### WI-1 Fix the shared example header

**Files** `plugins/ea-plays/shared/provenance-header.md`, then `sync-shared.sh`.

Change the example to Progressa, consistent with `tests/plays/1.6/expected.md`:

```
> **Artefact** A6 — Phase RACI and role-gap list · **Country** Progressa · **Sector** Education · **Built** 2026-09-05
> **Skill** ea-governance-drafter v0.1.1 · **Consumed** A0 §4, A4, A5 · **Feeds** 1.7, 3.7
```

(A6 is `ea-governance-drafter`'s artefact per `play-map.json`, not
`ea-institution-mapper`'s — the current example is also wrong about the skill. Check
`workbook-chain.md` for the Feeds list before committing.) Run `sync-shared.sh`.

**Done when** `grep -ri gambia plugins/ea-plays/shared` is empty and `sync-shared.sh
--check` passes.

### WI-2 Fixture-material marker

**Convention.** Every file under `plugins/` that contains Progressa material opens with
exactly this line, before the H1:

```
<!-- fixture: Progressa (fictional) · canonical: tests/progressa.md · keep consistent with it -->
```

and the owning `SKILL.md` lists the file under a `Fixture material` sub-heading in its
"Reference Files" section, with the sentence *"Progressa is the fictional demonstration
country shared by every play; the canonical description is `tests/progressa.md` in the kit
repo."*

**Files to mark now** `bdat-assessor/references/worked-example.md`,
`ea-institution-mapper/references/paera-a1-2.md`, and (after WI-4)
`bb-sourcing-researcher/references/worked-example.md`. The shared `provenance-header.md`
and `output-contract.md` are **exempt** — they mention Progressa only as a field rule, not
as fixture content; the checker exempts them by path.

### WI-3 Extend `check_fixtures.py` — acceptance criterion 9

Add a section after criterion 8:

```python
# --- 9: Progressa appears in the plugin only as tagged, consistent fixture material
FIXTURE_TOKENS = r"\b(Progressa|PDGA|PNIA|PNEA|MoEYS|PLR|Linkup|PayPro)\b"
MARKER = "<!-- fixture: Progressa (fictional)"
EXEMPT = {"provenance-header.md", "output-contract.md", "workbook-chain.md", "source-tiers.md"}
CANON = {  # name → the exact string tests/progressa.md uses
    "MoEYS": "Ministry of Education, Youth and Skills",
    "PLR status": "not started",
    "PayPro operator": "Central Bank of Progressa",
}
```

Rules, each a `check(...)`:

1. Any `plugins/**/*.md` matching `FIXTURE_TOKENS` and not in `EXEMPT` must have `MARKER`
   on line 1.
2. Any marked file must not contain a known divergence: the strings
   `Youth and Sport`, `PDGA … payments`, `Establishment Decree`, and any row that gives
   PLR a running system. Implement as a short deny-list plus the `CANON` names — a
   regex per entry, not a parser. Keep the list in the script, next to the fixture it
   guards.
3. `plugins/**` (excluding the two legitimate files named above, by path) must not match
   `\bGambia\b` — the real-country leak must not come back.
4. `tests/plays/*/` must contain only `input.md` and `expected.md`.

Update the docstring header (criteria list) and the final `ok —` line. **Done when** the
script fails on the current tree for exactly the files named in this plan, and passes
after WI-1, 4, 5, 6.

### WI-4 Convert the bb-sourcing worked example to Progressa

**File** `bb-sourcing-researcher/references/worked-example.md`; two lines in `SKILL.md`
(l.86, l.218) that say "Gambia education context".

The eighteen product columns are country-independent and stay verbatim. Replace only the
country-specific frame:

| Now (Gambia) | Becomes (Progressa, from `tests/progressa.md`) |
| --- | --- |
| low-income | lower-middle-income |
| DHIS2 SEMIS | district EMIS with its own learner numbering (§1, §6) |
| iLearn Gambia, SMS attendance | drop; no fixture equivalent |
| national digital ID effort | PNIA National ID, 78 % adult coverage, e-KYC live (§1) |
| — | Linkup, X-Road 7.x in pilot, MoEYS not a member (§1) |
| — | PayPro fast-payment system; scholarships still paid by cheque (§1, §2) |

Then re-read blocks 1 (Identity), 6 (Messaging), 9 (Data exchange), 10 (Payments) and 15
(Analytics) and change the *Posture* where the frame changed it — e.g. Identity is
"Reuse existing (PNIA)" not "Reuse-OSS", Data exchange is "Reuse existing (Linkup) —
onboard MoEYS", Analytics loses the "extend existing DHIS2" argument. Rewrite the
"Worked reasoning" paragraph for the block you keep as the walkthrough, and the
"Cross-cutting findings" list. Add the WI-2 marker and title it *Worked Example: Progressa
Education Sector — 18-Block Sourcing Analysis*.

**Done when** the file has no Gambia token, the marker is present, and the postures in
the roll-up table sum correctly to the new bespoke-footprint percentage.

### WI-5 Rewrite the bdat worked example against the fixture

**File** `bdat-assessor/references/worked-example.md`. Keep the section structure (Bodies →
Business → Data → Application → Technology → Trace → Gaps → Traps); replace the content
with what §6 and the sector-problem paragraph of `tests/progressa.md` actually say.

Corrections that must land:

- MoEYS = Ministry of Education, Youth and **Skills**.
- PLR row: classification *State Registry*, status **planned — called for in the Education
  Sector Plan 2023–2028, not started**. No "Enrolment system". The Application layer shows
  learner data held **three times** (district EMIS, PNEA candidate list, Social Protection
  beneficiary register) — the duplicate-registry finding becomes **Confirmed**, not "Risk".
- PDGA runs Linkup only. Payments belong to the **Central Bank of Progressa (PayPro)**; add
  that row.
- Add **Civil Registration Department** (paper-first, 71 % birth registration) — it is the
  legal identity anchor for children (§7) and the reason PNIA cannot be the learner key
  below age 16.
- Technology layer: Linkup is a *live pilot with four members and MoEYS is not one* — the
  point-to-point finding is **Confirmed** (tax↔business-register direct DB link, 2022;
  MoEYS↔Health by spreadsheet).
- Traps: the bespoke trap is **present**, not hypothetical — the Social Register (2016,
  single-vendor maintenance) is the fixture's vendor-lock-in case.
- Add a source line under the H1: *"All facts from `tests/progressa.md` §1, §6, §7 and the
  sector-problem paragraph. Progressa is fictional; the example carries no sources."*

Also fix `ea-institution-mapper/references/paera-a1-2.md` l.56–58: replace the invented
decree with the fixture's stated basis — *coordinating but not binding mandate; unit under
the Ministry of ICT (§1, §4)* — and confidence `confirmed` → `confirmed (A0 §1)`. Hybrid
note: the 2021 Interoperability Framework gives PDGA a standards role that is *published,
not applied* (§7).

**Done when** WI-3 rule 2 passes and a side-by-side read of the Bodies table against §6
finds no disagreement.

### WI-6 Remove the Gambia baselines

- Delete `tests/plays/1.1–1.8/gambia.md` (eight files).
- `tests/README.md`: remove the `gambia.md` row and the whole section *"Why only Module 1
  has a `gambia.md`"*. Replace with a short *"Acceptance criterion 7"* section: *"Criterion 7
  (at least as specific as the real-country run of 30 Aug 2026) is a manual side-by-side
  read against the private synthesis record, which is not in this repo. It is not
  machine-checked."*
- `CHANGELOG.md`: under `[Unreleased]` → `### Changed`, note the removal and the reason
  (one country in the fixture tree; real-country material out of the public kit).
- Root `README.md` l.28 stays ("the Progressa fixture, 38 play folders, the checker") —
  it is already accurate once the baselines go.

**Done when** `grep -rli gambia tests` is empty.

### WI-7 Release

1. Bump `0.1.0` → `0.1.1` in both manifests; `provenance-header.md` example follows.
2. `CHANGELOG.md` — move the `[Unreleased]` notes to `## [0.1.1] — <date>` under
   `### Fixed` (WI-1, WI-5, paera-a1-2), `### Changed` (WI-4, WI-6), `### Added`
   (WI-2 marker convention, WI-3 criterion 9).
3. `bash plugins/ea-plays/scripts/sync-shared.sh && python3 tests/check_fixtures.py &&
   claude plugin validate plugins/ea-plays --strict`.
4. `bash plugins/ea-plays/scripts/package.sh`; tag `v0.1.1`; attach `dist/*`.

## Order and effort

| # | Item | Depends on | Effort |
| --- | --- | --- | --- |
| 1 | WI-1 header | — | 10 min |
| 2 | WI-3 checker (written first so it fails red, then goes green) | — | 45 min |
| 3 | WI-6 remove baselines | — | 15 min |
| 4 | WI-2 marker + SKILL.md sub-headings | — | 15 min |
| 5 | WI-5 bdat + paera-a1-2 rewrite | WI-2 | 1.5 h |
| 6 | WI-4 bb-sourcing conversion | WI-2 | 1 h |
| 7 | WI-7 release | all | 15 min |

Items 1–4 can be one commit ("fixture hygiene: tag, check, one country"); 5 and 6 one
commit each so the content rewrites are reviewable on their own.

## Out of scope, decide later

- Whether the other twelve skills should get a Progressa `worked-example.md` under the same
  marker, or whether `tests/plays/*/expected.md` is their worked example. Leaning: no new
  worked examples until a learner asks; the fixture `expected.md` is the contract.
- Generating the bdat worked example from `tests/progressa.md` §6 by script. At this size a
  hand-written file guarded by criterion 9 is enough.
- Re-running Modules 2–4 on a real country to rebuild criterion 7 coverage. Do it outside
  this repo and keep the record private.
