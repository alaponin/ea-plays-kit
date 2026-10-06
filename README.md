# ea-plays-kit

Two Claude plugins for learners on four Knowledge Product courses about digital government:

- **Government Enterprise Architecture** (the EA course): how a government plans its bodies,
  systems and data as one whole.
- **Government Interoperability Framework** (the interoperability course): the legal,
  organisational and technical rules that let public bodies exchange data.
- **The education DPI roadmap** course: how a ministry plans its digital public
  infrastructure, step by step.
- **The service design** course: how a public service is specified and built on shared
  building blocks.

| Plugin | What it is |
| --- | --- |
| [`ea-plays`](plugins/ea-plays/README.md) | Four skills that sharpen the plays and the AI usage tips of the four courses |
| [`sdd-kit`](plugins/sdd-kit/README.md) | The service design course's method: twelve skills that help a team write its documents, with the standards and the programs they use |

Each course is made of **plays**. A play is a prompt that the learner runs in an AI
assistant during a lesson. Each play makes one **artefact** for the learner's own country,
for example a gap analysis, a RACI or a draft decree. The artefacts feed into each other and
build up a country workbook.

The plays are published on the course GitBook, and they work in any assistant without this
kit. The kit adds the step a bare prompt skips. It finds the public sources before it
writes, checks each claim against them afterwards, and marks what it could not verify.

## Install

In Claude Code:

```
/plugin marketplace add alaponin/ea-plays-kit
/plugin install ea-plays@ea-plays-kit
/plugin install sdd-kit@ea-plays-kit
```

In any agent that reads skill files, through the skills CLI. The skills are published through
the ITU Skills Marketplace from this repository; every skill folder is self-contained.

```
npx skills add alaponin/ea-plays-kit                         # every skill
npx skills add alaponin/ea-plays-kit --skill decision-cards  # one skill
```

Each plugin's README has the other ways to install it, the list of its skills, and which
play or subtopic each skill serves.

## Terms

| Term | Meaning |
| --- | --- |
| Play | One prompt from a course, identified by module and number, for example `2.4` |
| Artefact | What a play makes. EA course artefacts are A-numbered (`A7`); interoperability course artefacts are B-numbered (`B11`). The two courses reuse play ids, so the letter tells them apart |
| A0 | The country context pack. Play 0 makes it, and every later play reads from it |
| Workbook chain | Which play makes each artefact and which plays consume it. One file per course, in `plugins/ea-plays/shared/` |
| Provenance header | The three lines at the top of every output: country, date, sources by tier, and unverified lines |
| Progressa | A fictional country. The tests and worked examples run on it, so they do not depend on a real country |

## Layout

```
.claude-plugin/marketplace.json   the marketplace
plugins/ea-plays/                 the first plugin
  .claude-plugin/plugin.json      the manifest (the only file in this folder)
  shared/                         rules every skill follows: source tiers, provenance header,
                                  output contract, and the two workbook chains
                                  (workbook-chain.md for EA, workbook-chain-gif.md for interoperability)
  skills/<name>/SKILL.md          four skills, each one self-contained
  scripts/sync-shared.sh          copies shared/*.md into the references/ folder of each skill
  scripts/package.sh              builds the Cowork .plugin
plugins/sdd-kit/                  the second plugin: the service design course's method
  standards/, kit/                the standards the skills read and the programs they run
  skills/<name>/                  twelve skills; each carries a copy of kit/ and of the
                                  standards' text, so each is self-contained
  scripts/sync-skills.sh          makes those copies
tests/
  progressa.md                    the Progressa country pack (A0)
  play-map.json                   every EA course play, its artefact, inputs and skill (37)
  plays/                          one fixture folder per EA play whose skill ships
  gif/                            the interoperability supplement to Progressa, its play map
                                  (38) and one fixture folder per play whose skill ships
  dpi-roadmap/, service-design/   the fixtures of decision-cards for those two courses
  check_fixtures.py               the automated check
```

`shared/` is edited in one place only. `sync-shared.sh` **copies** it into each skill's
`references/` folder, so a learner can upload a single skill folder to the Claude app, where
there is no plugin root. No `SKILL.md` depends on a plugin root.

`plugins/sdd-kit/standards/` and `plugins/sdd-kit/kit/` are edited in one place only, the same
way: `sync-skills.sh` copies them into each sdd-kit skill. The standards' figures stay at the
plugin root.

## Working on it

```bash
bash plugins/ea-plays/scripts/sync-shared.sh    # run it after you edit a file in shared/
bash plugins/sdd-kit/scripts/sync-skills.sh     # run it after you edit sdd-kit's kit/ or standards/
python3 tests/check_fixtures.py                 # fixtures, README tables, workbook chains,
                                                # the marketplace checks on every skill
claude plugin validate plugins/ea-plays --strict
claude plugin validate plugins/sdd-kit --strict
claude --plugin-dir plugins/ea-plays            # load a plugin for one session; install nothing
```

CI runs these checks with `--check` on the two sync scripts, sdd-kit's own checks (at the
plugin root and in one skill on its own), and `claude plugin validate . --strict` on the
marketplace, on every push and pull request.

To make a release:

1. Increase the version of the plugin in its `plugin.json` **and** in `marketplace.json`.
2. Add the entry to `CHANGELOG.md`.
3. Run `bash plugins/ea-plays/scripts/package.sh`.
4. Tag the commit.
5. Attach `dist/*` to the GitHub release. Do not commit build output.

## Licence

The content uses CC BY 4.0. `LICENSE` at the root of the repository carries the full text.
`plugins/ea-plays/LICENSE-CONTENT` says which files the licence covers, and it travels inside
the packaged plugin.

The scripts use MIT. See `plugins/ea-plays/LICENSE-CODE`. sdd-kit carries the same two
licence files.

Each `SKILL.md` declares `license: CC-BY-4.0` and `metadata.provider` in its frontmatter, as
the ITU Skills Marketplace requires.
