# Fixtures

One folder per play under `plays/`, plus the canonical Progressa page.

| File | What it is |
| --- | --- |
| `progressa.md` | The fixture country as an A0 pack in the seven Play 0 sections. Every `input.md` names the sections it consumes. |
| `play-map.json` | Single source of truth: play id → primary skill, also-runs skills, artefact, inputs consumed. The plugin README table and `check_fixtures.py` both read it. |
| `plays/<id>/input.md` | The play's prompt with Progressa substituted, and which section of `progressa.md` to paste. |
| `plays/<id>/expected.md` | The **shape** of a passing output — headings, columns, the provenance field set, the safeguard. Never the wording. |
| `plays/<id>/gambia.md` | The 30 August 2026 real-country baseline, where one exists. |
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

## Why only Module 1 has a `gambia.md`

The four raw test documents from the 30 August 2026 Gambia runs are in no repo. The
only surviving record is `KP1_Play_Tests_Synthesis_2026-08-30.md`, whose per-play
table covers Module 1 only. Those eight baselines are excerpted here; 2.1–2.7, 3.2
and 4.1–4.8 were run on that day but their outputs were not preserved.

**To close the gap:** re-run those plays on The Gambia with the kit loaded, strip
office-holders' names, and add the excerpt as `gambia.md`. Until then acceptance
criterion 7 is verifiable for Module 1 and for the Progressa shape everywhere.
