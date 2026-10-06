# Fixtures

There is one folder for each play whose primary skill ships, under `plays/`. There is also the
canonical Progressa page.

| File | What it is |
| --- | --- |
| `progressa.md` | The fixture country, as an A0 pack in the seven sections of Play 0. Each `input.md` names the sections that it uses. |
| `play-map.json` | The single source of truth. For each play id of the whole course it gives the primary skill, the skills that also run, the artefact, and the inputs; the course GitBook reads the artefacts and inputs from it. A play whose primary skill does not ship in this release has no fixture. |
| `plays/<id>/input.md` | The prompt of the play, with Progressa in the place of the country. It also says which section of `progressa.md` to paste. |
| `plays/<id>/expected.md` | The **shape** of an output that passes: the headings, the columns, the nine provenance fields, and the safeguard. It never gives the wording. |
| `dpi-roadmap/plays/<id>/`, `service-design/plays/<id>/` | Fixtures for the education DPI roadmap and service design courses. Their plays run bare, so there is no play map: each `input.md` says which skill the fixture tests, and `check_fixtures.py` reads every folder there. |
| `check_fixtures.py` | The check that you can run. CI runs it. Run it before each commit that changes a skill or the README. |

## Running it

```bash
python3 tests/check_fixtures.py
bash plugins/ea-plays/scripts/sync-shared.sh --check
bash plugins/sdd-kit/scripts/sync-skills.sh --check
claude plugin validate plugins/ea-plays --strict
claude plugin validate plugins/sdd-kit --strict
```

sdd-kit's skills are checked by its own programs, in `plugins/sdd-kit/kit/` (Python 3.10 or
later, with `pyyaml` and `jsonschema`): `python3 tools/kit.py skills --check` and
`python3 tools/kit.py slot --check`. CI also runs the first in one skill's folder on its own.

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
| 2 | Each play in `play-map.json` whose primary skill ships has a fixture folder and a row in the README; no fixture tests a skill that does not ship | `check_fixtures.py` |
| 3 | Each `expected.md` declares the nine provenance fields, and the shared example gives the version that the plugin ships | `check_fixtures.py` |
| 4 | Each `expected.md` carries the safeguards of the output contract: posts and not names, and text only | `check_fixtures.py` |
| 5 | Each skill folder is self-contained. No file depends on `${CLAUDE_PLUGIN_ROOT}` | `package.sh` |
| 6 | The fixture tree covers each play in `play-map.json` whose skill ships, and no other folder | `check_fixtures.py` |
| 7 | A run is as specific as the run for a real country on 30 August 2026, or more specific | **manual** — compare it with the private record of 30 Aug 2026, which is not in this repo |
| 8 | The shared references are the same in every ea-plays skill | `sync-shared.sh --check` |
| 9 | In the plugin, Progressa appears only as fixture material that carries the marker and agrees with the fixture. The test country of 30 Aug 2026 appears only as one comparator among several | `check_fixtures.py` |
| 10 | The workbook chain agrees with itself. When a play consumes an artefact, the *Feeds* cell of that artefact names the play | `check_fixtures.py` |
| 11 | Each fixture of the DPI roadmap and service design courses has its two files and nothing else, the nine provenance fields, the posts and text-only rules, and a header that names the skill its `input.md` tests, which the plugin ships | `check_fixtures.py` |
| 12 | Every skill in the repository passes the ITU Skills Marketplace's automated checks: a valid slug as its name, a description, a licence, a provider under `metadata.provider`, at least 80 characters of instructions; and no `SKILL.md` stands where the marketplace would list it as a skill by mistake | `check_fixtures.py` |
| 13 | Each sdd-kit skill carries an exact copy of the plugin's `kit/` and of its standards' text, so it works installed on its own | `sync-skills.sh --check` · `check_fixtures.py` |

Criteria 1, 4, 5 and 6 are written here from what the tools test. The build plan that gave
them their numbers is not in this repo.
