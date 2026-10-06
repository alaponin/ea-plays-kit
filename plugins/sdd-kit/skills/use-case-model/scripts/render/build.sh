#!/usr/bin/env bash
# The whole pipeline, in the only order that produces correct page numbers.
#
#   ./build.sh                     build, paginate, gate
#   ./build.sh --figs              redraw the figures too (after a change to the model)
#   ./build.sh --publish <dir>     and, once the gate passes, copy the document into <dir>
#
# Run it from the build folder — a copy of the skill's scripts/render/ with
# scripts/extract.py beside them and project.py filled in, outside the specification
# tree. It never edits a generated file: every correction goes into the model or into a
# script, and you run this again.
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1

FIGS=0
PUBLISH=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --figs) FIGS=1; shift ;;
    --publish) PUBLISH="${2:?--publish needs a folder}"; shift 2 ;;
    *) echo "unknown argument: $1"; exit 2 ;;
  esac
done

DOC=$(python3 -c "import project; print(project.OUT)")
PDF="${DOC%.docx}.pdf"
SRC=$(python3 -c "import project; print(project.SRC)")
LEGACY=$(python3 -c "import project; print('--legacy' if getattr(project, 'LEGACY', False) else '')")

step() { printf '\n\033[1m== %s\033[0m\n' "$1"; }

step "1. read the model"
python3 extract.py "$SRC" --out model.json $LEGACY

if [[ "$FIGS" == 1 ]]; then
  step "2. draw the figures (geometry guards refuse a figure that fails)"
  rm -rf fig && mkdir -p fig
  python3 figs.py
else
  step "2. figures unchanged (pass --figs to redraw)"
  [[ -d fig ]] || { echo "no fig/ directory — run with --figs first"; exit 1; }
fi

step "3. build, render, derive the page numbers, build again"
python3 content.py "$DOC"
rm -f "$PDF"; soffice --headless --convert-to pdf "$DOC" >/dev/null 2>&1
python3 tocgen.py "$DOC" "$PDF" tocpages.json
python3 content.py "$DOC"

step "4. confirm pagination has settled"
rm -f "$PDF"; soffice --headless --convert-to pdf "$DOC" >/dev/null 2>&1
cp tocpages.json .tocpages.prev
python3 tocgen.py "$DOC" "$PDF" tocpages.json
if ! diff -q .tocpages.prev tocpages.json >/dev/null; then
  echo "pagination moved on the second pass — building once more"
  python3 content.py "$DOC"
  rm -f "$PDF"; soffice --headless --convert-to pdf "$DOC" >/dev/null 2>&1
  cp tocpages.json .tocpages.prev
  python3 tocgen.py "$DOC" "$PDF" tocpages.json
  diff -q .tocpages.prev tocpages.json >/dev/null \
    || { echo "FAIL: the contents page numbers will not settle"; exit 1; }
fi
rm -f .tocpages.prev
echo "pagination is stable"

step "5. the release gate"
python3 verify.py "$DOC" "$PDF"

if [[ -n "$PUBLISH" ]]; then
  step "6. publish the gated document to the folder people open"
  # Without this the build leaves the document here and somebody copies it up by
  # hand. That is how a delivered file came to be four hours older than its own
  # generator: a copy nobody had to update. Nothing is published that has not
  # passed the gate above.
  mkdir -p "$PUBLISH"
  cp "$DOC" "$PUBLISH/"
  echo "published $(cd "$PUBLISH" && pwd)/$(basename "$DOC")"
fi

cat <<EOF

Built $DOC. Before it goes to anyone, look at the rendered pages — the gate checks
what can be checked mechanically, not whether the document reads well:

  pdftoppm -f 1 -l 8 -r 100 -png "$PDF" page

Sweep the title page, the contents, every figure, and the first page of each
section. A defect you can see and the gate cannot is a missing check — add it.
EOF
