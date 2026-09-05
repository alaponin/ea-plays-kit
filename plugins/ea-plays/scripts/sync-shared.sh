#!/usr/bin/env bash
# Copy shared/*.md into every skill's references/, so a single skill folder
# uploaded to the Claude app is self-contained.
#
#   sync-shared.sh          copy, then verify every copy matches
#   sync-shared.sh --check  verify only; do not write. Non-zero if anything drifted.
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
check_only=0
[[ "${1:-}" == "--check" ]] && check_only=1

drift=0
for skill in "$root"/skills/*/; do
  name="$(basename "$skill")"
  for src in "$root"/shared/*.md; do
    dst="$skill/references/$(basename "$src")"
    if (( check_only )); then
      if ! cmp -s "$src" "$dst"; then
        echo "drift: $name/references/$(basename "$src")" >&2
        drift=1
      fi
    else
      mkdir -p "$skill/references"
      cp "$src" "$dst"
      # A copy that differs after copying means something is writing it back.
      cmp -s "$src" "$dst" || { echo "copy failed: $dst" >&2; drift=1; }
    fi
  done
done

if (( drift )); then
  (( check_only )) && echo "Shared references have drifted. Edit shared/, then run sync-shared.sh." >&2
  exit 1
fi
(( check_only )) && echo "shared references in sync" || echo "synced shared/*.md into $(ls -d "$root"/skills/*/ | wc -l | tr -d ' ') skills"
