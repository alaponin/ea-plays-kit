# ea-plays-kit

This is the learner kit for the Knowledge Product AI plays on government enterprise
architecture. It is one Claude Code plugin, `ea-plays`, with fourteen skills.

```
/plugin marketplace add alaponin/ea-plays-kit
/plugin install ea-plays@ea-plays-kit
```

**The plays run bare in any assistant.** They are the product. They are neutral about the
tool. They are published on the GitBook. This kit is an optional layer. It adds the sources
and the verification, which is the step that a learner does not do.

**[`plugins/ea-plays/README.md`](plugins/ea-plays/README.md)** gives what the kit does, the
table from a play to a skill, and the other two ways to install it. Those two ways are
Cowork, and one skill at a time in the Claude app.

## Layout

```
.claude-plugin/marketplace.json   the marketplace
plugins/ea-plays/                 the plugin
  .claude-plugin/plugin.json      the manifest — no other file is here
  shared/                         source tiers · provenance header · workbook chain · output contract
  skills/<name>/SKILL.md          fourteen skills, each one self-contained
  scripts/sync-shared.sh          copies shared/*.md into the references/ of each skill
  scripts/package.sh              builds the Cowork .plugin
tests/                            the Progressa fixture, 38 play folders, the checker
```

The `shared/` folder exists one time. `sync-shared.sh` **copies** it into the `references/`
folder of each skill. Therefore a learner can upload one skill folder to the Claude app,
where there is no plugin root. No `SKILL.md` depends on a plugin root.

## Working on it

```bash
bash plugins/ea-plays/scripts/sync-shared.sh    # run it after you edit a file in shared/
python3 tests/check_fixtures.py                 # the check that you can run
claude plugin validate plugins/ea-plays --strict
claude --plugin-dir plugins/ea-plays            # load the plugin for one session; install nothing
```

CI runs the first three, plus `claude plugin validate . --strict` on the marketplace,
on every push and pull request.

To make a release, do these five steps. Increase the version in **both** manifests. Add the
entry to the CHANGELOG. Run `bash plugins/ea-plays/scripts/package.sh`. Tag the commit. Then
attach `dist/*` to the release on GitHub. Do not commit a build product.

## Licence

The content uses CC BY 4.0. `LICENSE` at the root of the repository carries the full text.
`plugins/ea-plays/LICENSE-CONTENT` says which files the licence covers, and it travels inside
the packaged plugin.

The scripts use MIT. See `plugins/ea-plays/LICENSE-CODE`.

Each `SKILL.md` declares `license: CC-BY-4.0` and `metadata.provider` in its frontmatter, as
the Giga Skills Marketplace needs.
