"""Derive the contents page numbers from the render, so the reader opens a
document whose contents are already filled in."""
import json, re, subprocess, sys
import signal
try:                       # piping a report into `head` must not truncate the run
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (AttributeError, ValueError):
    pass
from docx import Document

DOCX, PDF, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
txt = subprocess.run(['pdftotext', '-layout', PDF, '-'],
                     capture_output=True, text=True).stdout
pages = txt.split('\f')

doc = Document(DOCX)
heads = [p.text.strip() for p in doc.paragraphs
         if p.style.name.startswith('Heading') and p.text.strip()
         and p.text.strip() != 'Contents']

def norm(s):
    return re.sub(r'\s+', ' ', s).strip().lower()

# The contents page lists every heading, so it would match all of them. Any page
# carrying five or more headings is a contents page and is skipped.
norm_heads = [re.sub(r'\s+', ' ', h).strip().lower() for h in heads]
def dense(i):
    n = re.sub(r'\s+', ' ', pages[i]).strip().lower()
    return sum(1 for h in norm_heads if h in n) >= 5

start = next((i for i, pg in enumerate(pages)
              if re.search(r'^\s*Contents\s*$', pg, re.M)), None)
skip = set()
if start is not None:
    j = start
    while j < len(pages) and (j == start or dense(j)):
        skip.add(j)
        j += 1

found, missing, cursor = {}, [], 0
for h in heads:
    n = norm(h)
    for i in range(cursor, len(pages)):
        if i in skip:
            continue
        if n in norm(pages[i]):
            found[h] = i + 1
            cursor = i
            break
    else:
        missing.append(h)

if missing:
    print("FAIL — these headings were not located in the render:")
    for m in missing:
        print("   ", m)
    sys.exit(1)

json.dump(found, open(OUT, 'w'), indent=1, ensure_ascii=False)
print(f"located all {len(found)} headings; contents pages skipped: {sorted(x + 1 for x in skip)}; body pages {min(found.values())}–{max(found.values())}")
