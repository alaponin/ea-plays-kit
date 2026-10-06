"""The house helpers the reader's edition is built with: paragraphs, headings, tables, figures."""
import json, re, sys
import signal
try:                       # piping a report into `head` must not truncate the run
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (AttributeError, ValueError):
    pass
sys.path.insert(0, '.')
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from sanitise import clean, scan

# the house palette, taken from the reference specification
INK    = RGBColor(0x1F, 0x29, 0x33)
NAVY   = RGBColor(0x1F, 0x38, 0x64)      # headings, table header fill
MIDBLU = RGBColor(0x2E, 0x75, 0xB6)      # sub-sub headings, subtitle, captions
GREY   = RGBColor(0x66, 0x66, 0x66)
RULE   = RGBColor(0xB4, 0xC6, 0xE7)
BLUE   = NAVY                             # kept for callers
CONTENT_W = Cm(15.9)

# The heading of the one page on which the rule identifiers of the standard may stand: the claim.
# verify.py reads the same constant, so the page it exempts is the page content.py draws.
CLAIM_HEADING = "Appendix A. How the model stands against its standard"


# ------------------------------------------------------------------ helpers
def shade(cell, hexfill):
    el = OxmlElement('w:shd'); el.set(qn('w:val'), 'clear')
    el.set(qn('w:color'), 'auto'); el.set(qn('w:fill'), hexfill)
    cell._tc.get_or_add_tcPr().append(el)


def cell_text(cell, text, bold=False, size=9, colour=INK, align=None):
    cell.text = ""
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2); p.paragraph_format.space_after = Pt(2)
    if align: p.alignment = align
    add_rich(p, text, size=size, bold_default=bold, colour=colour)
    return p


MD = re.compile(r'(\*\*.+?\*\*|«.+?»|\*.+?\*)')


def add_rich(p, text, size=10, bold_default=False, colour=INK, italic_default=False):
    """Render a subset of markdown emphasis into runs."""
    text = (text or "").replace('\u00a0', ' ').replace('`', '')
    for part in MD.split(text):
        if not part: continue
        b, i = bold_default, italic_default
        t = part
        if part.startswith('**') and part.endswith('**'): t, b = part[2:-2], True
        elif part.startswith('*') and part.endswith('*') and len(part) > 2: t, i = part[1:-1], True
        r = p.add_run(t)
        r.font.size = Pt(size); r.font.bold = b; r.font.italic = i
        r.font.color.rgb = colour
        r.font.name = 'Calibri'
    return p


def para(doc, text="", size=10, style=None, space_after=6, italic=False,
         align=None, colour=INK, space_before=0):
    p = doc.add_paragraph(style=style)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(space_before)
    if align: p.alignment = align
    if text: add_rich(p, text, size=size, colour=colour, italic_default=italic)
    return p


HSIZE = {1: 18, 2: 15, 3: 13}
HCOL = {1: NAVY, 2: NAVY, 3: MIDBLU}
HBEFORE = {1: 18, 2: 14, 3: 10}
HAFTER = {1: 10, 2: 7, 3: 6}


def heading(doc, text, level=1, page_break=False):
    if page_break:
        doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
    h = doc.add_heading(level=level)
    r = h.add_run(text)
    r.font.name = 'Calibri'
    r.font.color.rgb = HCOL[level]
    r.font.size = Pt(HSIZE[level])
    r.font.bold = True
    h.paragraph_format.space_before = Pt(HBEFORE[level])
    h.paragraph_format.space_after = Pt(HAFTER[level])
    h.paragraph_format.keep_with_next = True
    return h


def keep_with_next(p):
    kn = OxmlElement('w:keepNext'); kn.set(qn('w:val'), 'true')
    p._p.get_or_add_pPr().append(kn)


def table(doc, rows, widths, header=True, fs=9, band=True):
    # the paragraph that introduces a table must not be left behind by it
    if doc.paragraphs:
        keep_with_next(doc.paragraphs[-1])
    t = doc.add_table(rows=0, cols=len(widths))
    t.style = 'Table Grid'
    tblPr = t._tbl.tblPr
    lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); tblPr.append(lay)
    tw = OxmlElement('w:tblW'); tw.set(qn('w:w'), str(int(sum(w.cm for w in widths) * 567)))
    tw.set(qn('w:type'), 'dxa'); tblPr.append(tw)
    grid = t._tbl.find(qn('w:tblGrid'))
    if grid is None:
        grid = OxmlElement('w:tblGrid'); t._tbl.append(grid)
    for gc in list(grid): grid.remove(gc)
    for w in widths:
        gc = OxmlElement('w:gridCol'); gc.set(qn('w:w'), str(int(w.cm * 567))); grid.append(gc)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    for ri, row in enumerate(rows):
        cells = t.add_row().cells
        for ci, val in enumerate(row):
            cells[ci].width = widths[ci]
            is_h = header and ri == 0
            cell_text(cells[ci], val, bold=is_h, size=fs,
                      colour=RGBColor(0xFF, 0xFF, 0xFF) if is_h else INK)
            if is_h:
                shade(cells[ci], '1F3864')
            elif band and ri % 2 == 0:
                shade(cells[ci], 'F2F7FB')
            else:
                shade(cells[ci], 'FFFFFF')
    for row in t.rows:
        for ci, c in enumerate(row.cells):
            c.width = widths[ci]
    # no row may be split across a page break
    for row in t.rows:
        trPr = row._tr.get_or_add_trPr()
        cs = OxmlElement('w:cantSplit'); cs.set(qn('w:val'), 'true'); trPr.append(cs)
    if header:
        tr = t.rows[0]._tr
        trPr = tr.get_or_add_trPr()
        el = OxmlElement('w:tblHeader'); el.set(qn('w:val'), 'true'); trPr.append(el)
        # the header must never be the last thing on a page
        for c in t.rows[0].cells:
            for p in c.paragraphs:
                keep_with_next(p)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    return t


FIGN = [0]


MAX_FIG_H_CM = 21.0     # text height is 25.3cm; this leaves room for the caption


def figure(doc, path, caption, width_cm=15.9):
    """Place a figure at the column width, unless that would make it too tall to
    sit on a page with its caption — a package with fourteen use cases produces a
    figure nearly three times as tall as it is wide."""
    FIGN[0] += 1
    from PIL import Image
    w, h = Image.open(path).size
    if width_cm * h / w > MAX_FIG_H_CM:
        width_cm = MAX_FIG_H_CM * w / h
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(8); p.paragraph_format.space_after = Pt(3)
    # a caption stranded at the top of the next page reads as a defect: bind the
    # picture to the caption that names it, and keep the caption itself whole
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.keep_together = True
    p.add_run().add_picture(path, width=Cm(width_cm))
    c = doc.add_paragraph(); c.alignment = WD_ALIGN_PARAGRAPH.CENTER
    c.paragraph_format.space_after = Pt(12)
    c.paragraph_format.keep_together = True
    r = c.add_run(f"Figure {FIGN[0]}. {caption}")
    r.font.size = Pt(9); r.font.italic = True; r.font.color.rgb = MIDBLU
    r.font.name = 'Calibri'
    return FIGN[0]


def bullets(doc, items, size=10):
    for it in items:
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(3)
        add_rich(p, it, size=size)


def toc(doc):
    p = doc.add_paragraph()
    fld = OxmlElement('w:fldSimple')
    fld.set(qn('w:instr'), 'TOC \\o "1-2" \\h \\z \\u')
    inner = OxmlElement('w:r'); t = OxmlElement('w:t')
    t.text = "Right-click and choose “Update field” to build the table of contents."
    inner.append(t); fld.append(inner)
    p._p.append(fld)
