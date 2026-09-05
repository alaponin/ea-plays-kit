# Plan — consistency and simplification pass after 0.1.2

**Date** 2026-09-05 · **Status** proposed · **Target release** 0.1.3 (patch — reference
and documentation fixes; no skill contract changes) · **Follows**
`2026-09-05-fixture-separation.md`

## Problem

The 0.1.2 review found the fixture separation complete except for one file, plus a set of
small inconsistencies and some machinery that can be trimmed now the leak is closed.

1. **`bdat-assessor/references/change-impact-template.md` carries the marker but not the
   content.** Its filled example (l.109–169) is the pre-review fork: "Digital Government
   Authority"/"DGA" for PDGA; NLR ownership "contested between MoEYS and DGA" where §2 assigns
   it to MoEYS; "backbone not yet operational" where Linkup is live and the gap is MoEYS
   membership; "sixth version … the five that exist" where the fixture has three lists; and a
   legal-basis row that misses the Data Protection Act 2023, the one constraint §7 attaches.
   The checker passed it because DENY encodes the first review's four divergences, not these.
2. **`shared/workbook-chain.md` disagrees with itself.** The A6 row says *Feeds 1.7*, but the
   A21 row (3.7) and A30 row (5.5) both list A6 under *Consumed*. The header example copies
   the A6 row, so it inherits the error.
3. **Small drift** — a mis-count in the bdat traps section, one non-PAERA type name, a file
   listed twice in a SKILL.md, a README skill description that contradicts `play-map.json`,
   and an untracked `docs/` folder.
4. **Undocumented convention, over-specified checker.** The marker + `Fixture material`
   convention lives only in a CHANGELOG entry and checker comments; acceptance-criterion
   numbers are cited in prose but never listed; `EXEMPT` names two files that trip nothing;
   the Gambia rule claims more than it checks.

## Principles

- Same as the previous plan: one Progressa, tag files not skills, enforce don't request.
- **A convention lives in one place.** `tests/README.md` owns the fixture rules and the
  criteria list; the CHANGELOG points, the checker enforces.
- **Every exemption earns its line.** An entry in `EXEMPT` or `GAMBIA_OK` exists because a
  named file trips the regex for a stated reason.

## Work items

### WI-1 Rewrite the change-impact filled example

**File** `bdat-assessor/references/change-impact-template.md` l.109–169. Keep the six
section headings the template above it defines; replace the content from §1, §2, §3, §6, §7
of `tests/progressa.md`.

| Now | Becomes |
| --- | --- |
| Digital Government Authority / DGA | Progressa Digital Government Authority (PDGA) |
| Owner: contested between MoEYS and DGA | Owner: MoEYS — named in the Education Sector Plan 2023–2028 and in §2; **not yet a Linkup member and no data-standards function** (§6) |
| Trigger: donor-funded digital education programme | Trigger: World Bank human-capital programme, USD 6.5m over 3 years (§2, item 1) |
| Each ministry and examination authority holds its own partial list | Three lists: district EMIS, PNEA candidate list, Social Protection beneficiary register (sector-problem paragraph) |
| Backbone not yet operational | Linkup live in pilot with four members; MoEYS is not one — onboarding, not build, is the gap (§1) |
| "sixth version … the five that exist" | "a fourth list rather than replacing the three" |
| Legal basis: no law designates a registry | Two rows: (a) no instrument designates an authoritative learner registry; (b) **Data Protection Act 2023** requires a legal basis for sharing minors' data and parental consent for non-statutory uses — the Commission has 6 staff and no enforcement action yet (§7) |
| Person domain: PLR uses PNIA as anchor | PNIA issues IDs only at 16; for a primary-school child the anchor is the Civil Registration Department, paper-first, 71% birth registration (§1, §7). The Downward Trace must say so |
| Bespoke trap: clear | Bespoke trap: **present in the sector** — the 2016 beneficiary register under single-vendor maintenance is the counter-example already running (§1, §6) |
| Enabling conditions: 5 rows | 6 rows (add the DPA row); recount the "n of m absent or contested" sentence |
| Recurrent funding: Unknown | Recurrent funding: **annual budget cycle, no multi-year ICT envelopes** (§4, §5) |

**Done when** the file has no `DGA` token outside `PDGA`, and a side-by-side read against
§2 item 1 and §7 finds no disagreement.

### WI-2 Extend the deny-list for the divergences WI-1 removes

**File** `tests/check_fixtures.py`, `DENY`. Add:

```python
(r"\bDGA\b", "the body is PDGA — Progressa Digital Government Authority"),
(r"backbone not yet operational|no backbone exists",
 "Linkup is live in pilot; the gap is MoEYS membership (§1)"),
(r"contested between MoEYS", "the fixture assigns the NLR to MoEYS (§2)"),
```

Rename the comment above `DENY` from "the divergences the 2026-09-05 review found" to
"every divergence a review has found; add to it, never prune it". **Done when** the script
fails red on the current tree for this one file and passes after WI-1.

### WI-3 Fix the workbook chain and the header example

**Files** `shared/workbook-chain.md` l.42, `shared/provenance-header.md` example line 2,
then `sync-shared.sh`.

- A6 row *Feeds* → `1.7, 3.7, 5.5`.
- Header example → `**Feeds** 1.7, 3.7, 5.5`; bump `v0.1.2` → `v0.1.3` in the same line.
- **Optional, 20 lines:** add criterion 10 to the checker — parse the workbook-chain table
  and check that every artefact named in a *Consumed* cell appears with that play in the
  producing row's *Feeds* cell. This is exactly the class of error that just happened, and
  the table is regular enough to parse with one regex per row. Recommend doing it; skip if
  the table format proves irregular.

**Done when** `sync-shared.sh --check` passes and (if criterion 10 lands) it passes on the
corrected table and fails when l.42 is reverted.

### WI-4 Small drift

One commit, five edits:

1. `bdat-assessor/references/worked-example.md` Traps section: "five programmes across five
   ministries … Four more donor-funded systems" → "five programmes across four ministries,
   three donors" (§2: NLR and Scholarship are both MoEYS; §5: three donors).
2. Same file, two occurrences: `Shared Platform Provider` → `Shared Platform` (PAERA's term,
   as used by `bdat-assessor/SKILL.md` and `paera-a1-2.md`).
3. `bdat-assessor/SKILL.md` Reference Files: remove `change-impact-template.md` from the
   `Fixture material` list; in its main-list entry append *"(its filled example is fixture
   material and carries the marker)"*. One listing per file.
4. `plugins/ea-plays/README.md` l.45: `bdat-assessor` → *"The four-layer read of a body or
   sector, and the change-impact trace"*. The metamodel conformance check is 2.2 and
   belongs to `paera-reference-check`, whose row already says so.
5. `git add docs/` — commit the two plans. They are the *how*; the CHANGELOG is the *why*.

### WI-5 Give the convention and the criteria a home

**File** `tests/README.md`. Two new sections; then trim the CHANGELOG.

**"Fixture material inside skills"** — three sentences:

> Some skills carry Progressa material in `references/` so a single uploaded skill folder
> still has a worked example. Every such file opens with
> `<!-- fixture: Progressa (fictional) · canonical: tests/progressa.md · keep consistent with it -->`
> and its `SKILL.md` lists it under a `Fixture material` sub-heading. `check_fixtures.py`
> fails on an untagged fixture token and on every divergence a review has found; the
> authority for a Progressa fact is `progressa.md`, always.

**"Acceptance criteria"** — the nine (ten, with WI-3) in a table with a *Checked by*
column: `check_fixtures.py` / `sync-shared.sh --check` / `claude plugin validate` /
*manual*. Criterion 7 becomes a row (*manual — side-by-side against the private 30 Aug 2026
record*) and the existing "Acceptance criterion 7" section is deleted. Criteria 1, 4, 5, 6
need their text recovered from wherever the numbering originated (the original build
plan); if it is not to hand, write them from what the checker, sync script and validator
actually test and say so in a one-line note.

Then in `check_fixtures.py` shorten the docstring to *"Guards the machine-checkable
acceptance criteria; the list is in tests/README.md"* plus the run line, and in
`CHANGELOG.md` 0.1.1 → `### Added`, cut the two bullets to one: *"Fixture marker and
`Fixture material` convention, enforced by `check_fixtures.py` criterion 9 — see
`tests/README.md`."*

### WI-6 Honest checker exemptions

**File** `tests/check_fixtures.py`.

- `EXEMPT`: drop `workbook-chain.md` and `source-tiers.md` (neither contains a fixture
  token). Comment each remaining entry: `provenance-header.md`/`output-contract.md` — field
  rule, not fixture content; `SKILL.md` — declares fixture files under a sub-heading
  instead of carrying the marker.
- Gambia rule: rename `GAMBIA_OK` → `REAL_COUNTRY_AS_COMPARATOR_OK`, and change the
  failure message and the docstring line from "no real country leaks in" to *"the 30 Aug
  2026 test country does not come back except as one comparator among several"*. Same
  check, honest name.
- Final `ok —` line: *"…, one tagged Progressa, a consistent workbook chain"* if WI-3's
  criterion 10 lands.

### WI-7 Release 0.1.3

1. Bump both manifests `0.1.2` → `0.1.3`.
2. CHANGELOG `## [0.1.3] — <date>`: `### Fixed` (WI-1, WI-3 chain row, WI-4 items 1–4);
   `### Changed` (WI-5 README home, WI-6 exemptions); `### Added` (WI-2 deny entries;
   criterion 10 if built).
3. `bash plugins/ea-plays/scripts/package.sh` (runs sync, checker, both validators, the
   manifest-agreement check, then builds). Tag `v0.1.3`, attach `dist/*`.

## Order and effort

| # | Item | Depends on | Effort |
| --- | --- | --- | --- |
| 1 | WI-2 deny entries — written first, fails red | — | 10 min |
| 2 | WI-1 change-impact rewrite — goes green | WI-2 | 45 min |
| 3 | WI-3 chain row + header (+ criterion 10) | — | 15 min (+30 with criterion 10) |
| 4 | WI-4 small drift, one commit | — | 20 min |
| 5 | WI-5 README home + criteria table; trim docstring and CHANGELOG | — | 40 min |
| 6 | WI-6 exemptions | WI-5 (same file as the docstring cut) | 10 min |
| 7 | WI-7 release | all | 15 min |

Three commits: *"change-impact example against the fixture"* (1–2), *"workbook chain agrees
with itself"* (3), *"fixture rules in one place; honest exemptions"* (4–6). Then the release
commit. About 2.5–3 hours.

## Out of scope, decide later

- Whether `tests/progressa.md` should carry a short **"facts that files often get wrong"**
  list (PLR not started; PayPro at the Central Bank; child ID anchor is civil registration;
  Linkup live but MoEYS absent). It would help a human author; the checker already covers
  the machine side. Leaning: yes, five lines, next time the fixture is touched.
- Generating `DENY` from that list rather than hand-maintaining both. Not worth it at
  seven entries.
