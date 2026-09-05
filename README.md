# ea-plays-kit

The learner kit for the Knowledge Product AI plays on government enterprise architecture.
One Claude Code plugin, `ea-plays`, with fourteen skills.

```
/plugin marketplace add alaponin/ea-plays-kit
/plugin install ea-plays@ea-plays-kit
```

**The plays run bare in any assistant.** They are the product, they are tool-neutral, and
they are published on the GitBook. This kit is the optional layer that adds the sources and
the verification — the step learners skip.

Everything the kit does, the play → skill table, and the other two install routes (Cowork,
and single skills in the Claude app) are in **[`plugins/ea-plays/README.md`](plugins/ea-plays/README.md)**.

## Layout

```
.claude-plugin/marketplace.json   the marketplace
plugins/ea-plays/                 the plugin
  .claude-plugin/plugin.json      the manifest — nothing else lives here
  shared/                         source tiers · provenance header · workbook chain · output contract
  skills/<name>/SKILL.md          fourteen skills, each self-contained
  scripts/sync-shared.sh          shared/*.md -> every skill's references/
  scripts/package.sh              the .plugin and the standalone zip
tests/                            the Progressa fixture, 38 play folders, the checker
```

`shared/` exists once and is **copied** into every skill's `references/` by
`sync-shared.sh`. That is what lets a learner upload one skill folder to the Claude app,
where there is no plugin root; nothing in a `SKILL.md` depends on one.

## Working on it

```bash
bash plugins/ea-plays/scripts/sync-shared.sh    # after editing anything in shared/
python3 tests/check_fixtures.py                 # the runnable check
claude plugin validate plugins/ea-plays --strict
claude --plugin-dir plugins/ea-plays            # load it for one session, install nothing
```

CI runs all four on every push and pull request.

To release: bump the version in **both** manifests, add the CHANGELOG entry, run
`bash plugins/ea-plays/scripts/package.sh`, tag, and attach `dist/*` to the GitHub release.
Build products are not committed.

## Licence

Content — CC BY 4.0 (`plugins/ea-plays/LICENSE-CONTENT`).
Scripts — MIT (`plugins/ea-plays/LICENSE-CODE`).
