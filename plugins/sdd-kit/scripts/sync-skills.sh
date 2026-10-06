#!/usr/bin/env bash
# Copy kit/ and the text of standards/ into every skill's folder, so a skill installed on its
# own (the Claude app, `npx skills add`, the ITU Skills Marketplace) carries what it reads and
# runs. kit/ and standards/ at the plugin root are the one place to edit; the copies are built.
# The standards' figures stay at the root: a skill reads the text, not the pictures.
#
#   sync-skills.sh          copy, then verify every copy matches
#   sync-skills.sh --check  verify only; do not write. Non-zero if anything drifted.
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
check_only=0
[[ "${1:-}" == "--check" ]] && check_only=1
skip=(--exclude=figures --exclude=__pycache__ --exclude=.DS_Store)

drift=0
for skill in "$root"/skills/*/; do
  name="$(basename "$skill")"
  for part in kit standards; do
    if (( check_only )); then
      out="$(rsync -rcn --delete --out-format='%n' "${skip[@]}" "$root/$part/" "$skill$part/" 2>&1)" || true
      [[ -z "$out" ]] || { echo "drift: $name/$part: $(echo "$out" | head -3 | tr '\n' ' ')" >&2; drift=1; }
    else
      rsync -rc --delete "${skip[@]}" "$root/$part/" "$skill$part/"
    fi
  done
done

if (( drift )); then
  (( check_only )) && echo "Skill copies have drifted. Edit kit/ or standards/, then run sync-skills.sh." >&2
  exit 1
fi
(( check_only )) && echo "kit and standards in sync in every skill" \
  || echo "synced kit/ and standards/ into $(ls -d "$root"/skills/*/ | wc -l | tr -d ' ') skills"
