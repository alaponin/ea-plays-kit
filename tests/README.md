# Fixtures

There is one folder for each play, under `plays/`. There is also the canonical Progressa page.

| File | What it is |
| --- | --- |
| `progressa.md` | The fixture country, as an A0 pack in the seven sections of Play 0. Each `input.md` names the sections that it uses. |
| `play-map.json` | The single source of truth. For each play id it gives the primary skill, the skills that also run, the artefact, and the inputs. The table in the plugin README and `check_fixtures.py` both read this file. |
| `plays/<id>/input.md` | The prompt of the play, with Progressa in the place of the country. It also says which section of `progressa.md` to paste. |
| `plays/<id>/expected.md` | The **shape** of an output that passes: the headings, the columns, the nine provenance fields, and the safeguard. It never gives the wording. |
| `check_fixtures.py` | The check that you can run. CI runs it. Run it before each commit that changes a skill or the README. |

## Running it

```bash
python3 tests/check_fixtures.py
bash plugins/ea-plays/scripts/sync-shared.sh --check
claude plugin validate plugins/ea-plays --strict
```

To run one play, load the plugin without an installation, and paste the fixture:

```bash
claude --plugin-dir plugins/ea-plays
```

## Fixture material inside skills

Some skills carry Progressa material in their `references/` folder. Therefore one skill
folder that a learner uploads still has a worked example. Each of these files starts with
this line:
`<!-- fixture: Progressa (fictional) · canonical: tests/progressa.md · keep consistent with it -->`
Its `SKILL.md` also lists the file under the sub-heading `Fixture material`.
`check_fixtures.py` fails when it finds a fixture token with no marker. It also fails on each
difference from the fixture that a review found. The authority for a fact about Progressa is
always `progressa.md`.

## Acceptance criteria

| # | Criterion | Checked by |
| --- | --- | --- |
| 1 | Both manifests pass the strict validation, and their versions are the same | `claude plugin validate --strict` · `package.sh` |
| 2 | Each play in `play-map.json` has a fixture folder and a row in the README, and one primary skill that the plugin ships | `check_fixtures.py` |
| 3 | Each `expected.md` declares the nine provenance fields, and the shared example gives the version that the plugin ships | `check_fixtures.py` |
| 4 | Each `expected.md` carries the safeguards of the output contract: posts and not names, and text only | `check_fixtures.py` |
| 5 | Each skill folder is self-contained. No file depends on `${CLAUDE_PLUGIN_ROOT}` | `package.sh` |
| 6 | The fixture tree covers each play in `play-map.json`, and no other folder | `check_fixtures.py` |
| 7 | A run is as specific as the run for a real country on 30 August 2026, or more specific | **manual** — compare it with the private record of 30 Aug 2026, which is not in this repo |
| 8 | The shared references are the same in all fourteen skills | `sync-shared.sh --check` |
| 9 | In the plugin, Progressa appears only as fixture material that carries the marker and agrees with the fixture. The test country of 30 Aug 2026 appears only as one comparator among several | `check_fixtures.py` |
| 10 | The workbook chain agrees with itself. When a play consumes an artefact, the *Feeds* cell of that artefact names the play | `check_fixtures.py` |

Criteria 1, 4, 5 and 6 are written here from what the tools test. The build plan that gave
them their numbers is not in this repo.
