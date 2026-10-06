# -*- coding: utf-8 -*-
"""The release gate. Must print ALL CHECKS PASS before the document is delivered.

    python3 verify.py <doc.docx> [<doc.pdf>]

Ten checks, each of which exists because the defect it names once reached a reader
(references/render-failure-catalogue.md). The claim page — the appendix whose heading is
build_doc.CLAIM_HEADING — is the one page allowed to carry the standard's rule identifiers,
because it is the claim; every other check runs over it as over the rest.
"""
import sys
sys.dont_write_bytecode = True
import json, os, re
import signal
try:                       # piping a report into `head` must not truncate the run
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (AttributeError, ValueError):
    pass
sys.path.insert(0, '.')
from docx import Document
from docx.oxml.ns import qn
from sanitise import scan, residue, FORBIDDEN
from build_doc import CLAIM_HEADING
import counts as C

try:
    import project as P
except ImportError:
    class P:
        OUT = 'Use_Case_Model.docx'
        ABBREVIATIONS = {}
        COMMON_WORDS = set()
PATH = sys.argv[1] if len(sys.argv) > 1 else getattr(P, 'OUT', 'Use_Case_Model.docx')
doc = Document(PATH)
M = json.load(open('model.json', encoding='utf-8'))
PLAN = json.load(open('figplan.json', encoding='utf-8'))
fails = []


def add(name, problems):
    if problems:
        fails.append((name, problems))


# ---- gather all text in document order, blocks kept separate so a paragraph boundary is
#      not a sentence boundary; everything from the claim heading on is the claim page
BODY, CLAIM = [], []
in_claim = False
for el in doc.element.body.iterchildren():
    if el.tag == qn('w:p'):
        t = ''.join(x.text or '' for x in el.iter(qn('w:t')))
        sty = el.find(qn('w:pPr'))
        sty = sty.find(qn('w:pStyle')) if sty is not None else None
        if t.strip() == CLAIM_HEADING and sty is not None and (sty.get(qn('w:val')) or '').startswith('Heading'):
            in_claim = True
        if t.strip():
            (CLAIM if in_claim else BODY).append(t)
    elif el.tag == qn('w:tbl'):
        for p in el.iter(qn('w:p')):
            t = ''.join(x.text or '' for x in p.iter(qn('w:t')))
            if t.strip():
                (CLAIM if in_claim else BODY).append(t)
# the appendix after the claim page is not the claim
if CLAIM:
    cut = next((i for i, b in enumerate(CLAIM) if b.startswith('Appendix B.')), len(CLAIM))
    BODY += CLAIM[cut:]
    CLAIM = CLAIM[:cut]
blocks = BODY + CLAIM
ALL = "\n".join(blocks)
ALL_BODY = "\n".join(BODY)

# 1 ---------------------------------------------------------------- leaks
GATE_CODE = 'a quality-gate code'
leaks = scan(ALL_BODY)
claim_forbidden = [(p, w) for p, w in FORBIDDEN if w != GATE_CODE]
for b in CLAIM:
    for pat, what in claim_forbidden:
        for m in re.finditer(pat, b):
            leaks.append(f"{what}: {m.group(0)!r} on the claim page")
add("1. no internal or historical term survives", leaks)

# 2 ---------------------------------------------------------------- residue
add("2. no residue from a stripped reference", residue(ALL))

# 3 ---------------------------------------------------------------- sentence case
bad = []
for b in blocks:
    t = b.strip()
    if not t or t[0].isdigit() or not t[0].isalpha():
        continue
    if t[0].islower():
        bad.append(f"a block opens in lower case: {t[:70]!r}")
add("3. every block opens in upper case", bad)

# 4 ---------------------------------------------------------------- table pagination
bad = []
for ti, t in enumerate(doc.tables):
    for ri, row in enumerate(t.rows):
        trPr = row._tr.find(qn('w:trPr'))
        if trPr is None or trPr.find(qn('w:cantSplit')) is None:
            bad.append(f"table {ti + 1} row {ri + 1} may split across a page break")
    # a table with no navy header row (the title-page metadata block) has no
    # header to repeat and no introduction to keep with
    shd = t.rows[0].cells[0]._tc.tcPr
    fill = shd.find(qn('w:shd')).get(qn('w:fill')) if (shd is not None and shd.find(qn('w:shd')) is not None) else None
    if fill != '1F3864':
        continue
    hdr = t.rows[0]._tr.find(qn('w:trPr'))
    if hdr is None or hdr.find(qn('w:tblHeader')) is None:
        bad.append(f"table {ti + 1} header does not repeat")
    for c in t.rows[0].cells:
        for p in c.paragraphs:
            pPr = p._p.find(qn('w:pPr'))
            if pPr is None or pPr.find(qn('w:keepNext')) is None:
                bad.append(f"table {ti + 1} header row may be the last thing on a page")
                break
        else:
            continue
        break
add("4. tables cannot split, orphan a header, or lose their introduction", bad)

# 5 ---------------------------------------------------------------- totals derived
bad = []
w = C.words
for phrase in (f"{w(C.USE_CASES)} goals", f"{w(C.PACKAGES)} groups"):
    if phrase not in ALL.lower():
        bad.append(f"the derived phrase {phrase!r} is not in the document")
add("5. headline totals are spelled from the model", bad)

# 6 ---------------------------------------------------------------- table width
sec = doc.sections[0]
avail = sec.page_width - sec.left_margin - sec.right_margin
bad = []
for ti, t in enumerate(doc.tables):
    widths = [c.width for c in t.rows[0].cells if c.width is not None]
    if widths and sum(w_.emu for w_ in widths) > int(avail) + 20000:
        bad.append(f"table {ti + 1} is wider than the text column")
add("6. no table exceeds the text column", bad)

# 7 ---------------------------------------------------------------- figures
# The number of figures is the number the figure plan says were drawn, never a constant:
# a constant of fifteen once refused every model smaller than the one it was set on.
figs = len(doc.inline_shapes)
drawn = PLAN.get('written')
if drawn is None:
    drawn = 1 + sum(len(p['figs']) for p in PLAN['packages']) + bool(PLAN.get('coverage')) + bool(PLAN.get('entities'))
if figs != drawn:
    add("7. every figure is placed", [f"{figs} figures are embedded; the figure plan says {drawn} were drawn"])
bad = []
caps = [p.text for p in doc.paragraphs if p.text.startswith('Figure ')]
nums = [int(re.match(r'Figure (\d+)', c).group(1)) for c in caps]
if nums != list(range(1, len(nums) + 1)):
    bad.append(f"figure numbering is not consecutive: {nums}")
if len(caps) != figs:
    bad.append(f"{figs} images but {len(caps)} captions")
add("7. figures are numbered consecutively and each has a caption", bad)

# 8 ---------------------------------------------------------------- row coverage
ids = {u['id'] for u in M['use_cases'] if u['id']}
missing = sorted(i for i in ids if i not in ALL)
add("8. every use case appears in the document", [f"{i} is missing" for i in missing])

# 9 ---------------------------------------------------------------- consistency
bad = []
import sanitise
model_groups = {re.sub(r'\s+', ' ', sanitise.clean(p['name'])).strip() for p in M['packages'] if p['members']}
doc_groups = set()
for t in doc.tables:
    hdr = [c.text.strip() for c in t.rows[0].cells]
    if hdr[:2] == ['Group', 'Code']:
        for r in t.rows[1:]:
            n = r.cells[0].text.strip()
            if n and n != 'Total':
                doc_groups.add(n)
if doc_groups and doc_groups != model_groups:
    bad.append(f"the group table and the model disagree: only in the table {sorted(doc_groups - model_groups)}, "
               f"only in the model {sorted(model_groups - doc_groups)}")
# 9b. a group's code never stands alone in prose
CODES = [p['code'] for p in M['packages'] if p['members'] and p['code']]
for p in doc.paragraphs:
    t = p.text
    if not t.strip() or t.startswith('Figure '):
        continue
    for c in CODES:
        for m in re.finditer(rf'(?<![A-Za-z-]){re.escape(c)}(?![-A-Za-z0-9])', t):
            bad.append(f"the bare group code {c!r} appears in prose: …{t[max(0, m.start()-50):m.end()+50]}…")
# 9c. every figure a paragraph refers to exists
figs_present = set(range(1, figs + 1))
for p in doc.paragraphs:
    if p.text.startswith('Figure '):
        continue
    for m in re.finditer(r'\bFigure (\d+)\b', p.text):
        if int(m.group(1)) not in figs_present:
            bad.append(f"a cross-reference points at Figure {m.group(1)}, which does not exist")
# 9d. every abbreviation is expanded before or where it is first used. A run of capitals that
# is part of a reference (UC-01, FR-APP-001) is a reference, not an abbreviation.
ABBR = dict(getattr(P, 'ABBREVIATIONS', {}) or {})
COMMON_WORDS = {
    'and', 'the', 'for', 'a', 'an', 'of', 'to', 'in', 'on', 'by', 'is', 'are',
    'system', 'model', 'use', 'case', 'contents', 'figure', 'table', 'total', 'group',
} | {x.lower() for x in (getattr(P, 'COMMON_WORDS', set()) or set())}
KNOWN_OK = set(CODES) | set(ABBR)
# the organisation line of the title page is set in capitals by the house style; its words
# are words, not abbreviations
KNOWN_OK |= set(re.findall(r'[A-Z]{2,6}', (getattr(P, 'DOC', {}) or {}).get('organisation', '')))
for _a, _exp in ABBR.items():
    if not any(_exp in b for b in blocks):
        bad.append(f"the abbreviation {_a!r} is never expanded in the body")
first_use = {}
for i, b in enumerate(BODY):
    for m in re.finditer(r'(?<![-\w])([A-Z]{2,6})(?![-\w])', b):
        a = m.group(1)
        if a in KNOWN_OK:
            continue
        if a.lower() in COMMON_WORDS:
            continue
        first_use.setdefault(a, i)
for a, i in first_use.items():
    window = " ".join(BODY[max(0, i - 1):i + 1])
    if not re.search(rf'\(\s*{a}\s*\)', window):
        bad.append(f"the abbreviation {a!r} is used without being expanded")
add("9. the document is internally consistent", bad)

# 10 --------------------------------------------------------------- figures and captions
# A figure and the caption that names it must never be split by a page break.
bad = []
for p in doc.paragraphs:
    if not p._p.findall(qn('w:r') + '/' + qn('w:drawing')):
        continue
    if p.paragraph_format.keep_with_next is not True:
        bad.append("a picture paragraph is not bound to its caption")
PDF = sys.argv[2] if len(sys.argv) > 2 else None
if PDF and os.path.exists(PDF):
    import subprocess
    lst = subprocess.run(['pdfimages', '-list', PDF], capture_output=True, text=True).stdout
    img_pages = [int(l.split()[0]) for l in lst.split('\n')[2:]
                 if l.split() and l.split()[2] == 'image']
    txt = subprocess.run(['pdftotext', '-layout', PDF, '-'], capture_output=True, text=True).stdout
    cap_pages = {}
    for pageno, page in enumerate(txt.split('\f'), 1):
        for m in re.finditer(r'Figure (\d+)\.', page):
            cap_pages.setdefault(int(m.group(1)), pageno)
    if len(img_pages) != figs:
        bad.append(f"the rendering holds {len(img_pages)} pictures but the document declares {figs} figures")
    for k, ip in enumerate(img_pages, 1):
        cp = cap_pages.get(k)
        if cp is not None and cp != ip:
            bad.append(f"Figure {k} is drawn on page {ip} but its caption is on page {cp}")
add("10. no figure is separated from its caption", bad)

# ---------------------------------------------------------------- report
if fails:
    for name, problems in fails:
        print(f"FAIL — {name}")
        for p in problems[:12]:
            print("        ", p[:190])
        if len(problems) > 12:
            print(f"         … and {len(problems) - 12} more")
    sys.exit(1)
print("ALL CHECKS PASS")
print(f"  {figs} figures · {len(doc.tables)} tables · {len(doc.paragraphs)} paragraphs · "
      f"claim page {'present' if CLAIM else 'absent'}")
