#!/usr/bin/env bash
# Build the release artefact from one source tree.
#
#   package.sh            build into dist/
#   package.sh --check    validate only; build nothing
#
# Output (never committed — attached to the GitHub release):
#   dist/ea-plays-v<version>.plugin   Cowork: a stored zip of the plugin folder
#
# The Claude app's one-skill-at-a-time route uploads a folder straight from the source
# tree, so it needs no artefact of its own.
set -euo pipefail

plugin="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
repo="$(cd "$plugin/../.." && pwd)"
dist="$repo/dist"
version="$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1]))["version"])' \
           "$plugin/.claude-plugin/plugin.json")"

echo "==> sync shared references"
bash "$plugin/scripts/sync-shared.sh"

echo "==> fixtures and provenance headers"
python3 "$repo/tests/check_fixtures.py"

echo "==> validate"
claude plugin validate "$plugin" --strict
claude plugin validate "$repo"   --strict

# The two manifests must agree, or the marketplace serves a version that does not exist.
mversion="$(python3 - "$repo/.claude-plugin/marketplace.json" <<'PY'
import json,sys
print(next(p["version"] for p in json.load(open(sys.argv[1]))["plugins"] if p["name"]=="ea-plays"))
PY
)"
[[ "$version" == "$mversion" ]] || { echo "version mismatch: plugin.json $version, marketplace.json $mversion" >&2; exit 1; }
echo "==> version $version (both manifests agree)"

[[ "${1:-}" == "--check" ]] && { echo "check only — nothing built"; exit 0; }

rm -rf "$dist"; mkdir -p "$dist"

# Cowork .plugin — a stored (uncompressed) zip of the plugin folder, as the existing kits are.
echo "==> dist/ea-plays-v$version.plugin"
( cd "$plugin" && zip -q -r -0 "$dist/ea-plays-v$version.plugin" \
    .claude-plugin skills shared scripts README.md LICENSE-CODE LICENSE-CONTENT \
    -x '*.DS_Store' )

# Every skill folder must stay self-contained — sync-shared.sh copied shared/*.md into
# each references/, and a folder that still points at ${CLAUDE_PLUGIN_ROOT} would break
# when a learner uploads it to the Claude app on its own.
if grep -rl 'CLAUDE_PLUGIN_ROOT' "$plugin/skills" >/dev/null 2>&1; then
  echo "skills reference \${CLAUDE_PLUGIN_ROOT}; they must be self-contained" >&2
  exit 1
fi

ls -lh "$dist"
echo "==> done. Attach it to the GitHub release; it is not committed."
