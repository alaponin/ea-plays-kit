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

## Acceptance criterion 7

Criterion 7 (at least as specific as the real-country run of 30 August 2026) is a manual
side-by-side read against the private synthesis record, which is not in this repo. It is
not machine-checked.
