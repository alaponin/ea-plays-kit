# Fixtures

One folder per play under `plays/`, plus the canonical Progressa page.

| File | What it is |
| --- | --- |
| `progressa.md` | The fixture country as an A0 pack in the seven Play 0 sections. Every `input.md` names the sections it consumes. |
| `play-map.json` | Single source of truth: play id → primary skill, also-runs skills, artefact, inputs consumed. The plugin README table and `check_fixtures.py` both read it. |
| `plays/<id>/input.md` | The play's prompt with Progressa substituted, and which section of `progressa.md` to paste. |
| `plays/<id>/expected.md` | The **shape** of a passing output — headings, columns, the provenance field set, the safeguard. Never the wording. |
| `check_fixtures.py` | The runnable check. CI runs it; run it before every commit that touches a skill or the README. |

## Running it

```bash
python3 tests/check_fixtures.py
bash plugins/ea-plays/scripts/sync-shared.sh --check
claude plugin validate plugins/ea-plays --strict
```

For a live run of one play, load the plugin without installing it and paste the
fixture:

```bash
claude --plugin-dir plugins/ea-plays
```

## Fixture material inside skills

Some skills carry Progressa material in `references/` so a single uploaded skill folder
still has a worked example. Every such file opens with
`<!-- fixture: Progressa (fictional) · canonical: tests/progressa.md · keep consistent with it -->`
and its `SKILL.md` lists it under a `Fixture material` sub-heading. `check_fixtures.py`
fails on an untagged fixture token and on every divergence a review has found; the
authority for a Progressa fact is `progressa.md`, always.

## Acceptance criteria

| # | Criterion | Checked by |
| --- | --- | --- |
| 1 | Both manifests validate strict, and their versions agree | `claude plugin validate --strict` · `package.sh` |
| 2 | Every play in `play-map.json` has a fixture folder and a README row, with one primary skill that ships in the plugin | `check_fixtures.py` |
| 3 | Every `expected.md` declares the nine provenance fields | `check_fixtures.py` |
| 4 | Every `expected.md` carries the output-contract safeguards — posts not names, text only | `check_fixtures.py` |
| 5 | Every skill folder is self-contained; nothing depends on `${CLAUDE_PLUGIN_ROOT}` | `package.sh` |
| 6 | The fixture tree covers every play in `play-map.json` and nothing else | `check_fixtures.py` |
| 7 | A run is at least as specific as the real-country run of 30 August 2026 | **manual** — side-by-side against the private 30 Aug 2026 record, which is not in this repo |
| 8 | The shared references are in sync across all fourteen skills | `sync-shared.sh --check` |
| 9 | Progressa appears in the plugin only as tagged, consistent fixture material, and the 30 Aug 2026 test country does not come back except as one comparator among several | `check_fixtures.py` |
| 10 | The workbook chain agrees with itself — what a play consumes, its producer feeds | `check_fixtures.py` |

Criteria 1, 4, 5 and 6 are written here from what the tooling actually tests: the build
plan that originally numbered them is not in this repo.
