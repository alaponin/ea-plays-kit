# -*- coding: utf-8 -*-
"""The reader's edition of a use case model: every section drawn from model.json.

    python3 content.py [<out.docx>]

Sections 2 and 3 are the model's own prose (its purpose, what is inside its boundary and
what is deliberately outside); every table is generated from the record headers and the
named sets; every total is spelled from counts.py. The framing sentences are generic and
hold for any model: to change what one document says about its own system, change the
model, not this file. A project that wants other framing sentences copies this file into
its build folder and edits the copy there.

Every string reaching the document passes through clean(). Never add text with a raw
doc.add_paragraph() — that is how internal identifiers leak into a reader's copy, and
the release gate exists because it happened. The one exception is the claim page, the
last appendix, which carries the standard's rule identifiers because it is the claim.
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
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from build_doc import (para, heading, table, figure, bullets, cell_text, shade, INK, GREY,
                       NAVY, MIDBLU, RULE, CLAIM_HEADING)
from sanitise import clean
import counts as C
import project as PJ

M = json.load(open('model.json', encoding='utf-8'))
PLAN = json.load(open('figplan.json', encoding='utf-8'))
OUT = sys.argv[1] if len(sys.argv) > 1 else PJ.OUT
W = C.words
CAP = C.cap
LEVELS = dict(getattr(PJ, 'READER_LEVELS', {}) or {})
BY_ID = {u['id']: u for u in M['use_cases']}
GROUPS = [p for p in M['packages'] if p['members']]

doc = Document()
s = doc.sections[0]
s.page_width, s.page_height = Cm(21.0), Cm(29.7)
s.left_margin = s.right_margin = Cm(2.54)
s.top_margin = s.bottom_margin = Cm(2.54)
st = doc.styles['Normal']
st.font.name = 'Calibri'; st.font.size = Pt(10.5); st.font.color.rgb = INK
st.paragraph_format.space_after = Pt(6)
st.paragraph_format.line_spacing = 1.14

FIGDIR = 'fig'
COLW = 15.9                      # the usable text column, in centimetres


def widths(*cm_values):
    """Scale a set of column widths to the text column exactly."""
    total = sum(cm_values)
    return [Cm(v * COLW / total) for v in cm_values]


def F(name):
    return os.path.join(FIGDIR, name)


HEADINGS = []


def H(text, level=1, page_break=False, raw=False):
    t = text if raw else clean(text)
    HEADINGS.append((level, t))
    return heading(doc, t, level, page_break=page_break)


def P(txt, **kw):
    return para(doc, clean(txt), **kw)


def level_word(u):
    return LEVELS.get(u['level'], u['level'])


def cap1(t):
    return t[0].upper() + t[1:] if t else t


# =================================================================== title page
def centred(text, size, bold=False, colour=INK, italic=False, before=0, after=6):
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after = Pt(after)
    r = p.add_run(text)
    r.font.size = Pt(size); r.font.bold = bold; r.font.italic = italic
    r.font.color.rgb = colour; r.font.name = 'Calibri'
    return p


RULE_LINE = "─" * 42

centred(PJ.DOC['organisation'], 14, bold=True, colour=GREY, before=110, after=4)
centred(RULE_LINE, 12, colour=RULE, after=10)
centred(PJ.DOC['title'], 22, bold=True, colour=NAVY, after=4)
centred(clean(M.get('system') or ''), 16, colour=MIDBLU, after=4)
centred(PJ.DOC['subtitle'], 13, colour=MIDBLU, after=10)
centred(RULE_LINE, 12, colour=RULE, after=26)

META = [(k, v(C) if callable(v) else v) for k, v in PJ.META]
mt = doc.add_table(rows=0, cols=2)
mt.style = 'Table Grid'
from docx.enum.table import WD_TABLE_ALIGNMENT as _TA
mt.alignment = _TA.CENTER
MW = widths(3.6, 12.3)
for k, v in META:
    cells = mt.add_row().cells
    cells[0].width = MW[0]; cells[1].width = MW[1]
    cell_text(cells[0], k, bold=True, size=10, align=WD_ALIGN_PARAGRAPH.RIGHT)
    shade(cells[0], 'D6E4F0')
    cell_text(cells[1], v, size=10)
from docx.oxml.ns import qn as _qn0
from docx.oxml import OxmlElement as _El0
for row in mt.rows:
    row.cells[0].width = MW[0]; row.cells[1].width = MW[1]
    _cs = _El0('w:cantSplit'); _cs.set(_qn0('w:val'), 'true')
    row._tr.get_or_add_trPr().append(_cs)

# =================================================================== contents
heading(doc, "Contents", 1, page_break=True)
TOCPAGES = {}
if os.path.exists('tocpages.json'):
    TOCPAGES = json.load(open('tocpages.json', encoding='utf-8'))
_toc_anchor = doc.add_paragraph()

# =================================================================== 1
H("1. What this document is, and how to read it", 1, page_break=True)
P("This document describes what the system is for: who uses it, what each of those people "
  "is trying to achieve, and what the system must therefore be able to do. It is written for "
  "the people who must agree that the description is right — the people whose work the system "
  "will carry, and the people who answer for the information it keeps. It assumes no technical "
  "knowledge, and every word that carries a particular meaning is explained where it is first "
  "used and again in Appendix B.")
P("It describes **goals, not screens**. Each entry says who wants something, what they want, "
  "and how you would know they had got it. It does not say which button anyone presses, how a "
  "screen is laid out, or how the system works inside. The goals are what you are asked to "
  "confirm, and they stay stable while the way a system presents them changes many times.")
P("**How the document is arranged.** Section 2 says what the system is for. Section 3 draws "
  "the edge of the system: what it does, and what it deliberately leaves to other systems and "
  "to people. Section 4 introduces everyone who deals with it. Section 5 explains how the goals "
  f"are grouped, and section 6 lists all {W(C.USE_CASES)} of them, group by group. Sections 7 "
  "to 10 cover the steps that several goals share, the records the goals read and change, the "
  "rules they follow and the settings they read. Section 11 sets out what we ask you to "
  "confirm. Appendix A shows how the model stands against the standard it is written to, and "
  "Appendix B explains the words the document uses.")

# =================================================================== 2
H("2. What the system is for", 1, page_break=True)
for t in M.get('purpose') or ["The model states no purpose yet."]:
    P(t)

# =================================================================== 3
H("3. Where the system's edge lies", 1, page_break=True)
P("Every system is defined as much by what it leaves alone as by what it does. This section "
  "draws that line. Figure 1 shows it in outline: the boundary is the system, everyone who "
  "deals with it stands outside, and every goal it serves sits inside.")
figure(doc, F('f01_overview.png'),
       f"The system, the {W(C.PACKAGES)} groups of goals it holds, and the roles that pursue "
       "them. The code and the count beside each group are the ones used throughout this "
       "document; section 5 lists them in full and section 4 introduces every role.")
H("3.1 What the system does", 2)
for t in M.get('inside') or ["The model does not yet say what is inside its boundary."]:
    P(t)
H("3.2 What the system deliberately leaves alone", 2)
for t in M.get('outside') or ["The model does not yet say what is outside its boundary."]:
    P(t)

# =================================================================== 4
H("4. The people and systems that deal with it", 1, page_break=True)
P(f"{CAP(C.ACTORS_NAMED)} roles and systems deal with the system directly, and "
  f"{W(C.ACTORS_OFFSTAGE)} further interests must be honoured by it without ever using it. A "
  "role is a set of responsibilities, not a job title: one person may hold several, and one "
  "role may be held by many people.")
n4 = 0
if C.PEOPLE:
    n4 += 1
    H(f"4.{n4} The people who use it", 2)
    rows = [["Role", "What they are trying to achieve"]]
    for a in C.PEOPLE:
        rows.append([clean(a['name']), clean(a['goal'])])
    table(doc, rows, widths(4.4, 11.6), fs=8.5)
if C.STARTERS:
    n4 += 1
    H(f"4.{n4} What starts work by itself", 2)
    P("Some of what the system does is started by no person: a clock, a device or another "
      "system starts it. Treating each as a user in its own right keeps those obligations "
      "visible instead of leaving them buried in the machinery.")
    rows = [["", "What it starts"]]
    for a in C.STARTERS:
        rows.append([clean(a['name']), clean(a['goal'])])
    table(doc, rows, widths(4.4, 11.6), fs=8.5)
if C.SUPPORTING:
    n4 += 1
    H(f"4.{n4} The systems it depends on", 2)
    P("These are named by what they do rather than by product, because every organisation "
      "has its own.")
    rows = [["System", "What the system needs from it"]]
    for a in C.SUPPORTING:
        rows.append([clean(a['name']), clean(a['goal'])])
    table(doc, rows, widths(4.6, 11.4), fs=8.5)
if C.OFFSTAGE:
    n4 += 1
    H(f"4.{n4} Interests that must be honoured", 2)
    P("These parties never use the system. It nonetheless owes them something, and naming them "
      "here is what stops that being forgotten.")
    rows = [["Party", "What the system owes them"]]
    for a in C.OFFSTAGE:
        rows.append([clean(a['name']), clean(a['goal'])])
    table(doc, rows, widths(4.6, 11.4), fs=8.5)

# =================================================================== 5
H("5. How the goals are grouped", 1, page_break=True)
P(f"The {W(C.USE_CASES)} goals are arranged into {W(C.PACKAGES)} groups. Each group is about "
  "one kind of work, and the groups are kept loosely connected, so that one can be built, "
  "changed or reviewed without disturbing the others.")
rows = [["Group", "Code", "What it is about", "Goals"]]
for p in GROUPS:
    rows.append([clean(p['name']), p['code'], clean(p['about']), str(len(p['members']))])
rows.append(["**Total**", "", "", f"**{C.USE_CASES}**"])
table(doc, rows, widths(3.9, 1.3, 8.8, 2.0), fs=8.5)
figure(doc, F(PLAN['coverage']),
       "Which roles pursue at least one goal in each group. The column headings are the group "
       "codes from the table above.")
if M.get('packages_prose'):
    P("**How the groups depend on one another.** " + " ".join(M['packages_prose']))

# =================================================================== 6
H("6. The goals, group by group", 1, page_break=True)
P("Each group below opens with what it is about, then shows its goals as a diagram, then lists "
  "them. For every goal the list gives a reference, the goal itself, the role that pursues it, "
  "its level, how far it is written out, how essential it is, the requirements it answers, and "
  "a short description of what it is for.")
P("**How to read the reference column.** Every goal has a short reference, such as UC-01. The "
  "references are labels for discussion and nothing more, but they are stable, so a comment "
  "made against one can be found again later. The same holds for the requirement references, "
  "which point into the register of requirements.", size=9.5)
FIG_FOR = {e['code']: e['figs'] for e in PLAN['packages']}
for p in GROUPS:
    H(clean(p['name']), 2, page_break=True)
    P(clean(p['about']))
    for fname, part in FIG_FOR.get(p['code'] or p['name'], []):
        if part:
            cap_ = (f"{clean(p['name'])} — the goals in this group, part {part[0]} of {part[1]}, "
                    f"with the roles that pursue them.")
        else:
            cap_ = f"{clean(p['name'])} — the goals in this group, with the roles that pursue them."
        figure(doc, F(fname), cap_)
    rows = [["Ref.", "The goal", "Who pursues it", "Level", "Written out", "Priority",
             "Answers", "What it is for"]]
    for i in p['members']:
        u = BY_ID.get(i)
        if not u:
            continue
        written = u['format'] or '—'
        if u['status']:
            written = f"{written}; {u['status']}"
        rows.append([u['id'], clean(u['name']), clean(u['actor']) or '—', cap1(level_word(u)),
                     cap1(written), cap1(clean(u['priority'])) or '—', ", ".join(u['requirements']) or '—',
                     cap1(clean(u['description']))])
    table(doc, rows, widths(1.3, 2.4, 1.9, 1.5, 1.7, 1.3, 2.2, 3.6), fs=7.5)

# =================================================================== 7
H("7. Steps that several goals share", 1, page_break=True)
P("A few pieces of behaviour appear inside more than one goal. Rather than describing them over "
  "and over, and risking a different description each time, they are written once and referred "
  "to. When one of them changes, it changes everywhere at once.")
why = {(r['included'], b): r['why'] for r in M['includes'] for b in r['bases']}
rows = [["The shared step", "Where it is used", "Why it is written once"]]
for u in M['use_cases']:
    for inc in u['relationships']['includes']:
        v = BY_ID.get(inc)
        rows.append([f"{inc} {clean(v['name']) if v else ''}".strip(), f"{u['id']} {clean(u['name'])}",
                     cap1(clean(why.get((inc, u['id']), ''))) or '—'])
if len(rows) > 1:
    table(doc, rows, widths(4.6, 4.6, 6.8), fs=8.0)
else:
    P("No goal of this model shares a step with another.")
ext_rows = [["The optional step", "Where it attaches", "When it applies"]]
for u in M['use_cases']:
    for e in u['relationships']['extends']:
        b = BY_ID.get(e['base'])
        when = " — ".join(x for x in (clean(e['point']), clean(e['when'])) if x)
        ext_rows.append([f"{u['id']} {clean(u['name'])}", f"{e['base']} {clean(b['name']) if b else ''}".strip(),
                         cap1(when) or '—'])
if len(ext_rows) > 1:
    H("7.1 Behaviour that only sometimes applies", 2)
    P("These steps run only when a stated condition holds. They are kept apart so that the "
      "ordinary path stays readable.")
    table(doc, ext_rows, widths(4.6, 4.6, 6.8), fs=8.0)

# =================================================================== 8
H("8. The records the goals read and change", 1, page_break=True)
ent = M['named'].get('entity_model') or {}
defs = ent.get('statements') or {}
P(f"The goals name {W(C.ENTITIES)} kinds of record. This is not a database design; it is the "
  "vocabulary the rest of the document uses, so that everyone means the same thing by the same "
  "word. Each word is defined once, in the entity model the use case model names, and the "
  "meaning shown here is read from it when this document is built.")
if PLAN.get('entities'):
    figure(doc, F(PLAN['entities']), "The records the goals read and change.")
rows = [["Record", "What it is", "Read by", "Changed by"]]
for e in C.ENTITY_NAMES:
    rd = [u['id'] for u in M['use_cases'] if e in u['entities'].get('reads', [])]
    ch = [u['id'] for u in M['use_cases'] if e in u['entities'].get('changes', [])]
    rows.append([clean(e), cap1(clean(defs.get(e, ''))) or '—', ", ".join(rd) or '—', ", ".join(ch) or '—'])
table(doc, rows, widths(3.2, 6.6, 3.1, 3.1), fs=8.0)

# =================================================================== 9
H("9. The rules the goals follow", 1, page_break=True)
reg = M['named'].get('business_rules') or {}
stm = reg.get('statements') or {}
P(f"{CAP(C.RULES)} rules run through the goals above. Each is written once, in the register of "
  "business rules the model names, and a goal refers to it rather than repeating it. The "
  "statement shown here is read from that register when this document is built.")
rows = [["#", "The rule", "Followed by"]]
for n, r in enumerate(C.RULE_IDS, 1):
    by = [u['id'] for u in M['use_cases'] if r in u['rules']]
    rows.append([str(n), cap1(clean(stm.get(r, ''))) or '—', ", ".join(by)])
table(doc, rows, widths(1.2, 11.2, 3.6), fs=8.0)
uncited = [r for r in (reg.get('entries') or []) if r not in C.RULE_IDS]
if uncited:
    P(f"{CAP(len(uncited))} further rules stand in the register and no goal follows them. A rule "
      "nothing follows is either no longer needed or a rule nobody is looking after:")
    bullets(doc, [cap1(clean(stm.get(r, ''))) or '—' for r in uncited], size=9)

# =================================================================== 10
H("10. The settings the goals read", 1, page_break=True)
sett = M['named'].get('settings') or {}
if sett.get('entries'):
    P(f"{CAP(C.SETTINGS)} settings shape how the system behaves. Each is something one "
      "organisation might reasonably set differently from another, and each is held outside the "
      "model with a named owner and a marked default. **This document gives no values.**")
    rows = [["#", "The setting", "What it governs"]]
    for n, x in enumerate(C.SETTING_NAMES, 1):
        rows.append([str(n), clean(x), cap1(clean((sett.get('statements') or {}).get(x, ''))) or '—'])
    table(doc, rows, widths(1.2, 5.8, 9.0), fs=8.0)
else:
    P(clean(sett.get('none') or sett.get('absent') or "The model names no catalogue of settings."))

# =================================================================== 11
H("11. What we are asking you to confirm", 1, page_break=True)
P("This document is issued to be checked by the people whose work it describes. It is not a "
  "request to approve a design, and nothing here commits anyone to a delivery date or a "
  "sequence. What we need is confirmation that the description is recognisably an account of "
  "your own work.")
P("**Three questions, asked of every entry that names your people.** They are short on purpose: "
  "they are the three ways a description of this kind is usually wrong.")
bullets(doc, [
    "**Is any goal here not really yours?** If an entry names your people but describes "
    "something another group does, say so and say whose it is.",
    "**Is any goal of yours missing?** If there is something your people must be able to do "
    "that no entry covers, describe it in your own words; it does not need to be written in the "
    "style used here.",
    "**Is anything described as something other than what you would call it?** If an entry is "
    "right in substance but uses a word your people do not use, tell us the word you use. A "
    "shared vocabulary is worth more than an elegant one.",
])
P("Comments are most useful against the reference in the first column of each table. Those "
  "references are stable, so a comment made against one of them can still be found when the "
  "description is revised.")

# =================================================================== appendix A — the claim
def rule_titles():
    """The rules' own titles, read from the standard's document at build time; the
    checklist's first words stand in when the document cannot be read."""
    import yaml
    out, order = {}, []
    try:
        t = open(PJ.CHECKLIST, encoding='utf-8').read()
    except OSError:
        return {}, [], {}
    head = {}
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    if m:
        head = yaml.safe_load(m.group(1)) or {}
    on = False
    for line in t.split('\n'):
        if line.startswith('## '):
            on = line.strip().lower() == '## rules'
            continue
        c = [x.strip() for x in line.split('|')]
        if on and len(c) >= 5 and re.match(r'^[A-Z]+\d+$', c[1]):
            order.append(c[1]); out[c[1]] = c[2] + ' …'
    # sdd-kit: the standards root, as a full path (SDD_STANDARDS_ROOT, sdd-kit's standards/ folder)
    root = getattr(PJ, 'STANDARDS_ROOT', os.environ.get('SDD_STANDARDS_ROOT', ''))
    try:
        doc = os.path.join(root, str(head.get('document', '')))
        if doc.lower().endswith('.md'):          # a standard bundled as Markdown
            paras = [re.sub(r'^[#*\s]+|\*\*', '', x) for x in open(doc, encoding='utf-8').read().splitlines()]
        else:
            paras = [p.text for p in Document(doc).paragraphs]
        for ptext in paras:
            mm = re.match(r'^([A-Z]+\d+)\s{2,}(.+)$', ptext.strip())
            if mm and mm.group(1) in out:
                out[mm.group(1)] = mm.group(2).strip()
    except Exception:
        pass
    return out, order, head


def claim_lines():
    rel = (M.get('front') or {}).get('claim')
    if not rel:
        return None, {}
    path = os.path.join(os.path.dirname(M['model_file']), rel)
    if not os.path.exists(path):
        return path, {}
    got = {}
    for line in open(path, encoding='utf-8'):
        c = [x.strip() for x in line.split(' · ')]
        if len(c) == 3 and re.match(r'^[A-Z]+\d+$', c[0]):
            got[c[0]] = (c[1], c[2])
    return path, got


H(CLAIM_HEADING, 1, page_break=True, raw=True)
titles, order, chead = rule_titles()
cpath, verdicts = claim_lines()
VERDICT_WORDS = {'met': 'Met', 'not met': 'Not met', 'not applicable': 'Does not apply'}
para(doc, f"The model is written to the standard {chead.get('standard', 'SDD-05')}, "
          f"{chead.get('title', 'The Use Case Model')}. The standard asks a model to claim "
          "conformance rule by rule: this page lists every rule of the standard, in the "
          "standard's own words, beside the verdict the model's claim records. A rule not met is "
          "a finding with a named owner; it does not defeat the claim, and an unrecorded failure "
          "would. The rule references on this page are the standard's, and this is the only page "
          "on which they appear.")
if verdicts:
    rows = [["Rule", "What the rule asks", "Verdict", "Decided by"]]
    for r in order:
        v, by = verdicts.get(r, ('—', '—'))
        rows.append([r, titles.get(r, ''), VERDICT_WORDS.get(v, v),
                     'A person' if by == 'no program' else by])
    table(doc, rows, widths(1.3, 10.1, 2.2, 2.4), fs=8.0)
else:
    para(doc, "The claim has not been written yet. It is written by the kit's conformance "
              "program once every rule has an answer, and this page is built again from it.")

# =================================================================== appendix B — the words
H("Appendix B. Words used in this document", 1, page_break=True)
P("Every word below carries a particular meaning in this document. The words about the system "
  "itself come from the glossary the model names; the others are the words the document uses "
  "for the way a model of goals is put together.")
gl = M['named'].get('glossary') or {}
words_rows = [["Word", "What it means here"]]
for t_ in gl.get('entries') or []:
    words_rows.append([clean(t_), cap1(clean((gl.get('statements') or {}).get(t_, ''))) or '—'])
words_rows += [
    ["Goal", "Something a person or a system wants the system to do for them, with a result they can see. Each goal is one entry in section 6."],
    ["Group", "A set of goals about one kind of work, reviewed and changed together."],
    ["Role", "A set of responsibilities one person, or many, may hold; not a job title."],
    [cap1(LEVELS.get('summary', 'a whole outcome')), "A goal that is reached over several sittings and gathers other goals under it."],
    [cap1(LEVELS.get('user goal', 'one sitting')), "A goal a person completes in one sitting, which is where most goals of a model sit."],
    [cap1(LEVELS.get('subfunction', 'a shared step')), "A step written once because several goals need it, and reached only through them."],
    ["Brief, outline, written out in full", "How far a goal is written down: a paragraph, a few paragraphs, or in full with every way it can succeed and fail."],
    ["Record", "A kind of thing the system keeps, defined once in the entity model."],
    ["Rule", "A constraint the goals follow, written once in the register of business rules."],
    ["Requirement", "A stated need the system must meet, written once in the register of requirements; the requirement references in section 6 point into it."],
    ["Setting", "A value an organisation decides for itself, held outside the model with a named owner."],
]
table(doc, words_rows, widths(4.2, 11.8), fs=8.0)

# =================================================================== contents, spliced in
def build_contents():
    """Create the contents entries at the end, then move them under the heading.
    Page numbers come from the render of the first pass; without them the entries
    are still listed, which is better than an empty page."""
    from docx.enum.text import WD_TAB_ALIGNMENT
    made = []
    for level, text in HEADINGS:
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.space_after = Pt(2)
        pf.left_indent = Cm(0.0 if level == 1 else 0.7)
        pf.tab_stops.add_tab_stop(Cm(16.0), WD_TAB_ALIGNMENT.RIGHT, 1)  # 1 = dot leader
        page = TOCPAGES.get(text)
        r = p.add_run(text)
        r.font.size = Pt(10.5 if level == 1 else 10)
        r.font.bold = (level == 1)
        r.font.name = 'Calibri'
        r.font.color.rgb = INK
        if page:
            r2 = p.add_run('\t' + str(page))
            r2.font.size = Pt(10.5 if level == 1 else 10)
            r2.font.name = 'Calibri'
            r2.font.color.rgb = INK
        made.append(p)
    anchor = _toc_anchor._p
    for p in made:
        el = p._p
        el.getparent().remove(el)
        anchor.addnext(el)
        anchor = el


build_contents()

# Word opens a python-docx file in Compatibility Mode unless it is told which
# version to behave as; overwrite the value, never append a second setting.
from docx.oxml.ns import qn as _qn
from docx.oxml import OxmlElement as _El
_settings = doc.settings.element
_compat = _settings.find(_qn('w:compat'))
if _compat is None:
    _compat = _El('w:compat')
    _settings.append(_compat)
_existing = None
for _cs in _compat.findall(_qn('w:compatSetting')):
    if _cs.get(_qn('w:name')) == 'compatibilityMode':
        _existing = _cs
        break
if _existing is None:
    _existing = _El('w:compatSetting')
    _existing.set(_qn('w:name'), 'compatibilityMode')
    _existing.set(_qn('w:uri'), 'http://schemas.microsoft.com/office/word')
    _compat.insert(0, _existing)
_existing.set(_qn('w:val'), '15')


# =================================================================== header & footer
def _field(p, instr):
    from docx.oxml.ns import qn as _q
    from docx.oxml import OxmlElement as _E
    r = p.add_run()
    fc = _E('w:fldChar'); fc.set(_q('w:fldCharType'), 'begin'); r._r.append(fc)
    it = _E('w:instrText'); it.set(_q('xml:space'), 'preserve'); it.text = instr
    r._r.append(it)
    fs_ = _E('w:fldChar'); fs_.set(_q('w:fldCharType'), 'separate'); r._r.append(fs_)
    t = _E('w:t'); t.text = "1"; r._r.append(t)
    fe = _E('w:fldChar'); fe.set(_q('w:fldCharType'), 'end'); r._r.append(fe)
    r.font.size = Pt(8); r.font.color.rgb = GREY; r.font.name = 'Calibri'


from docx.enum.text import WD_TAB_ALIGNMENT as _TAB
sec = doc.sections[0]
sec.different_first_page_header_footer = True
hp = sec.header.paragraphs[0]
hp.paragraph_format.tab_stops.add_tab_stop(Cm(16.0), _TAB.RIGHT)
hr_ = hp.add_run(f"{PJ.DOC['header_left']}\t{PJ.DOC['header_right']}")
hr_.font.size = Pt(8); hr_.font.italic = True; hr_.font.color.rgb = GREY
hr_.font.name = 'Calibri'
fp = sec.footer.paragraphs[0]
fp.paragraph_format.tab_stops.add_tab_stop(Cm(16.0), _TAB.RIGHT)
fr = fp.add_run(f"{PJ.DOC['footer_left']}\tPage ")
fr.font.size = Pt(8); fr.font.color.rgb = GREY; fr.font.name = 'Calibri'
_field(fp, ' PAGE ')

doc.save(OUT)
print(f"written {OUT}")
print(f"  {C.USE_CASES} use cases · {C.PACKAGES} groups · {C.ACTORS_NAMED} named actors "
      f"· {C.ENTITIES} records · {C.RULES} rules · {C.SETTINGS} settings · claim "
      f"{'read from ' + cpath if verdicts else 'not yet written'}")
