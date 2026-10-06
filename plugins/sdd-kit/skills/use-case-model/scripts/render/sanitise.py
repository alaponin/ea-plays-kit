"""Strip everything internal or historical, then close the holes stripping leaves.

Every string that reaches the document passes through clean(); the finished .docx is
scanned by scan() for anything that survived. Raw insertion is how leaks get in.
"""
import json, os, re

try:
    import project as P
except ImportError:                      # the generic rules still work alone
    class P:
        EXTRA_STRIP = []
        EXTRA_FORBIDDEN = []
        GROUP_NAMES = {}

# The reader's word for the lowest level of goal. The standard's own word is what the model
# carries; the reader's edition says this instead, unless the project names another.
SUB_WORD = getattr(P, 'SUBFUNCTION_WORD', 'shared step') or 'shared step'

# ---------------------------------------------------------------- strip rules
# Order matters: parentheticals first, then bare references, then residue.
STRIP = list(getattr(P, 'EXTRA_STRIP', []) or []) + [
    # --- history and version chatter: never reaches a reader
    (r'\*\*New at v[\d.]+\.?\*\*\s*', ''),
    (r'\bNew at v[\d.]+\.?\s*', ''),
    (r'\bAdded at v[\d.]+\.?\s*', ''),
    (r'\bIntroduced at v[\d.]+\.?\s*', ''),
    (r'\b(?:since|from|at|in) v[\d.]+\b', ''),
    (r'\bv[01]\.\d\b', ''),

    # --- modelling machinery
    (r'\s*\((?:M|U)\d{1,2}(?:[,–-]\s*(?:M|U)?\d{1,2})*\)', ''),
    (r'\b(?:M|U)\d{1,2}\b(?=[\s,.;)])', ''),
    (r'\s*\((?:ruled by )?R-\d+(?:\s*,\s*R-\d+)*\)', ''),
    (r'\s*—?\s*ruled by R-\d+', ''),
    (r'\bR-\d+\b', ''),
    (r'\s*\((?:see )?`?BR-\d+`?(?:\s*,\s*`?BR-\d+`?)*\)', ''),
    (r'`?\bBR-\d+`?', 'a registered rule'),
    (r'\s*\(`?P-\d+`?(?:\s*(?:and|,)\s*`?P-\d+`?)*\)', ''),
    (r'`?\bP-\d+`?', 'a governed setting'),
    (r'\b(?:EN|AF|CF|HR)-\d+\b', ''),

    # --- source names an internal reader uses and a reader must not see
    # (project-specific rules live in project.py: EXTRA_STRIP)
    (r'\s*\(?\bthe [Gg]uide\b\s*§\s?\d+(?:\.\d+)?\)?', ''),
    (r'§\s?\d+(?:\.\d+)?', ''),

    # --- standard vocabulary a reader has no use for
    (r'\bDPO\b', 'data protection officer'),
    (r'\bsubfunctions\b', SUB_WORD + 's'),
    (r'\bsubfunction\b', SUB_WORD),
    (r'\b[Kk]ite[- ]level\b', 'whole-outcome'),
    (r'\bKite[- ]level\b', 'Whole-outcome'),
    (r'\bsea level\b', 'the working level'),
    (r'«include»', 'included'),
    (r'«extend»', 'optional'),
]

# American spellings and idiom the house style does not use
BRITISH = [
    (r'\b(analy|organi|recogni|prioriti|categori|summari|normali|minimi|maximi|utili|reali|emphasi)z(e|es|ed|ing|ation|ations)\b',
     lambda m: m.group(1) + 's' + m.group(2)),
    (r'\bcolor(s|ed|ing)?\b', lambda m: 'colour' + (m.group(1) or '')),
    (r'\bbehavior(s|al|ally)?\b', lambda m: 'behaviour' + (m.group(1) or '')),
    (r'\bfulfill(s|ed|ing|ment)?\b', lambda m: 'fulfil' + (m.group(1) or '')),
    (r'\bprograms?\b', 'programme'),
    (r'\bleverage[sd]?\b', 'use'),
    (r'\bgotten\b', 'got'),
    (r'\bmoving forward\b', 'from here on'),
    (r'\bgoing forward\b', 'from here on'),
    (r'\bat the end of the day\b', 'in the end'),
    (r'\bballpark\b', 'approximate'),
    (r'\bacross the board\b', 'in every case'),
    (r'\bdeep dive\b', 'close examination'),
    (r'\blow[- ]hanging fruit\b', 'the easiest gains'),
    (r'\bmove the needle\b', 'make a difference'),
    (r'\bcircle back\b', 'return to it'),
    (r'\bbang for the buck\b', 'value for the effort'),
]

# residue left behind where a reference was removed
TIDY = [
    (r'\(\s*\)', ''),
    (r'\[\s*\]', ''),
    (r'\s+,', ','),
    (r',\s*,+', ','),
    (r',\s*([.;:])', r'\1'),
    (r'\s*—\s*—\s*', ' — '),
    (r'\s*—\s*([.,;:])', r'\1'),
    (r'\(\s*([,;])\s*', '('),
    # A preposition stranded before its punctuation. The whitespace before the
    # punctuation is what distinguishes a strip from a clause that legitimately
    # ends in one; without it this rule mangles good prose.
    (r'\b(of|in|to|at|by|for|from|with|under|against|per|on)\s+([.,;:])', r'\2'),
    (r'\.\s*\.+', '.'),
    (r'\s{2,}', ' '),
    (r'\s+([.,;:)])', r'\1'),
    (r'\(\s+', '('),
    (r'^\s*[—,;:]\s*', ''),
    # an elliptical possessive reads as an unfinished sentence to a plain-English
    # reader: "is the Committee's" means "is the Committee's to decide"
    (r"\b(is|are|remains|stays) (the [A-Z][\w '’-]*?'s)\s*$", r'\1 \2 to decide'),
]

# a group's two-letter code must never stand alone in prose; the reader meets the
# codes only in the group table and in the reference column. The negative lookahead
# is what preserves a real reference (MG-01) while expanding a bare code (MG).
GROUP_NAMES = dict(getattr(P, 'GROUP_NAMES', {}) or {})
if not GROUP_NAMES and os.path.exists('model.json'):      # the codes and names the model itself gives
    try:
        GROUP_NAMES = {p['code']: p['name'] for p in json.load(open('model.json', encoding='utf-8'))['packages']
                       if p.get('code') and p.get('members')}
    except (ValueError, KeyError):
        GROUP_NAMES = {}
for _c, _n in GROUP_NAMES.items():
    STRIP.append((rf'(?<![A-Za-z-]){_c}(?![-A-Za-z0-9])', _n))

FORBIDDEN = list(getattr(P, 'EXTRA_FORBIDDEN', []) or []) + [
    (r'\bR-\d+\b', 'a ruling identifier'),
    (r'\bBR-\d+\b', 'a rule identifier'),
    (r'\bP-\d+\b', 'a parameter identifier'),
    (r'\b(?:CF|AF|HR|EN)-\d+\b', 'an internal identifier'),
    (r'\bfirst authority\b|\bsecond authority\b', 'an internal source name'),
    (r'§\s?\d+', 'a source section reference'),
    (r'\bv0\.\d\b|\bNew at v\b', 'version history'),
    (r'\bsubfunctions?\b', 'modelling vocabulary'),
    (r'\b[Kk]ite\b', 'modelling vocabulary'),
    (r'\bDPO\b', 'an unexplained abbreviation'),
    (r'\b(?:M|U)\d{1,2}\b(?=[\s,.;)])', 'a quality-gate code'),
    (r'\borganiz|\bbehavior\b|\bcolor\b|\bleverage\b|\butiliz', 'an American spelling or idiom'),
]


def clean(s):
    if not s:
        return s
    t = s
    for pat, rep in STRIP:
        t = re.sub(pat, rep, t)
    for pat, rep in BRITISH:
        t = re.sub(pat, rep, t, flags=re.I)
    for pat, rep in TIDY:
        t = re.sub(pat, rep, t)
    t = t.strip()
    # a sentence that now opens in lower case because it opened on an identifier
    if t and t[0].islower() and not t.startswith(('e.g', 'i.e')):
        t = t[0].upper() + t[1:]
    return t


def scan(text):
    """Every forbidden term that survived, with what it is."""
    out = []
    for pat, what in FORBIDDEN:
        for m in re.finditer(pat, text):
            ctx = text[max(0, m.start() - 45):m.end() + 45].replace('\n', ' ')
            out.append(f"{what}: {m.group(0)!r} in …{ctx}…")
    return out


def residue(text):
    """Holes a strip can leave, checked on the finished text."""
    out = []
    checks = [
        (r'\(\s*\)', 'empty parentheses'),
        (r',\s*,', 'a doubled comma'),
        (r'\s,', 'a space before a comma'),
        (r'\b(?:of|in|to|at|by|for|from|with|under|against|per)\s+[.,;]', 'a stranded preposition'),
        (r'—\s*[.,;]', 'a dash left before punctuation'),
        (r'\.\s*\.', 'a doubled full stop'),
    ]
    for pat, what in checks:
        for m in re.finditer(pat, text):
            ctx = text[max(0, m.start() - 45):m.end() + 45].replace('\n', ' ')
            out.append(f"{what}: …{ctx}…")
    return out
