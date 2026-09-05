#!/usr/bin/env bash
# Build the three release artefacts from one source tree (plan §3.7).
#
#   package.sh            build into dist/
#   package.sh --check    validate only; build nothing
#
# Outputs (never committed — attached to the GitHub release):
#   dist/ea-plays-v<version>.plugin         Cowork: a stored zip of the plugin folder
#   dist/skills-standalone-v<version>.zip   the Claude app: 14 self-contained skill folders
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

# Standalone skills — each folder self-contained, because sync-shared.sh already copied
# shared/*.md into every references/. A learner uploads one folder; no plugin root needed.
echo "==> dist/skills-standalone-v$version.zip"
( cd "$plugin" && zip -q -r "$dist/skills-standalone-v$version.zip" skills -x '*.DS_Store' )

# A skill folder that still points at ${CLAUDE_PLUGIN_ROOT} would break on upload.
if grep -rl 'CLAUDE_PLUGIN_ROOT' "$plugin/skills" >/dev/null 2>&1; then
  echo "skills reference \${CLAUDE_PLUGIN_ROOT}; they must be self-contained" >&2
  exit 1
fi

ls -lh "$dist"
echo "==> done. Attach both to the GitHub release; neither is committed."
