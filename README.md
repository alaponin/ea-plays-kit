# ea-plays-kit

A Claude plugin for learners on two Knowledge Product courses about digital government:

- **Government Enterprise Architecture** (the EA course): how a government plans its bodies,
  systems and data as one whole.
- **Government Interoperability Framework** (the interoperability course): the legal,
  organisational and technical rules that let public bodies exchange data.

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
```

**[`plugins/ea-plays/README.md`](plugins/ea-plays/README.md)** has the other two ways to
install it (Cowork, or one skill at a time in the Claude app), the list of skills, and a
table that shows which skill each play uses.

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
plugins/ea-plays/                 the plugin
  .claude-plugin/plugin.json      the manifest (the only file in this folder)
  shared/                         rules every skill follows: source tiers, provenance header,
                                  output contract, and the two workbook chains
                                  (workbook-chain.md for EA, workbook-chain-gif.md for interoperability)
  skills/<name>/SKILL.md          twenty-two skills, each one self-contained
  scripts/sync-shared.sh          copies shared/*.md into the references/ folder of each skill
  scripts/package.sh              builds the Cowork .plugin
tests/
  progressa.md                    the Progressa country pack (A0)
  plays/                          one fixture folder per EA course play (37)
  gif/                            the interoperability supplement to Progressa, and one
                                  fixture folder per interoperability course play (38)
  check_fixtures.py               the automated check
```

`shared/` is edited in one place only. `sync-shared.sh` **copies** it into each skill's
`references/` folder, so a learner can upload a single skill folder to the Claude app, where
there is no plugin root. No `SKILL.md` depends on a plugin root.

Skills whose names start with `gif-` exist for the interoperability course. The other skills
serve the EA course, and many of them also serve the interoperability course.

## Working on it

```bash
bash plugins/ea-plays/scripts/sync-shared.sh    # run it after you edit a file in shared/
python3 tests/check_fixtures.py                 # fixtures, README tables, workbook chains
claude plugin validate plugins/ea-plays --strict
claude --plugin-dir plugins/ea-plays            # load the plugin for one session; install nothing
```

CI runs the first three, plus `claude plugin validate . --strict` on the marketplace,
on every push and pull request.

To make a release:

1. Increase the version in **both** manifests.
2. Add the entry to `CHANGELOG.md`.
3. Run `bash plugins/ea-plays/scripts/package.sh`.
4. Tag the commit.
5. Attach `dist/*` to the GitHub release. Do not commit build output.

## Licence

The content uses CC BY 4.0. `LICENSE` at the root of the repository carries the full text.
`plugins/ea-plays/LICENSE-CONTENT` says which files the licence covers, and it travels inside
the packaged plugin.

The scripts use MIT. See `plugins/ea-plays/LICENSE-CODE`.

Each `SKILL.md` declares `license: CC-BY-4.0` and `metadata.provider` in its frontmatter, as
the Giga Skills Marketplace requires.
