# -*- coding: utf-8 -*-
"""Everything about ONE document. The scripts beside this file are generic; this
file is the only one you edit per document.

Copy the render step's scripts into a build folder outside the specification tree,
fill this in, and leave the rest alone. A setting left as it is here falls back to a
default that holds for any model, so start small and add only what the document needs.
"""
import os

# --------------------------------------------------------------- the artefact
OUT = 'Use_Case_Model.docx'
SRC = 'use_case_model.md'            # the model file, absolute or relative to the build folder
LEGACY = False                       # True reads the one-file shape of the retired plugin

# The standard's checklist, read at build time for the claim page. Its rules are
# never copied into this file.
# The kit's root, as a full path: the build folder stands outside the plugin, so it is given
# by SDD_KIT_ROOT (sdd-kit's kit/ folder) or written here.
KIT_ROOT = os.environ.get('SDD_KIT_ROOT', '')
CHECKLIST = os.path.join(KIT_ROOT, 'templates', 'spec', 'checklists', 'SDD-05.md')

# What appears on the title page. The organisation line sits above the rule in
# grey small caps; the title is the document, the subtitle its one-line purpose.
DOC = {
    'organisation': 'THE ORGANISATION OR PROGRAMME',
    'title':        'Use Case Model',
    'subtitle':     'What the system is for, who uses it, and what it must do',
    'header_left':  'Use Case Model',          # running header, left
    'header_right': 'For review and confirmation',
    'footer_left':  'The organisation or programme',
}

# The metadata table under the title. Keep it to six rows or fewer. A value may
# be a callable taking the counts module, for a total that must never be typed.
META = [
    ('Document', lambda C: DOC['title']),
    ('Purpose',  'To establish the goals the system must serve, for confirmation '
                 'by the people whose work it describes'),
    ('Status',   'For review and confirmation'),
    ('Scope',    lambda C: f"{C.cap(C.USE_CASES)} goals in {C.words(C.PACKAGES)} groups"),
    ('Audience', 'The people whose work the system will carry'),
    ('Contents', 'Goals, the people and systems around them, the groups they fall into, '
                 'the steps they share, the records and rules they name. No screen designs '
                 'and no step-by-step specifications'),
]

# The name drawn on the system's boundary in the overview figure; the model's own
# `system` is used when this is None.
SYSTEM_LABEL = None

# ------------------------------------------------------------------- packages
# The name a reader sees for each package code. Left empty, the model's own names are
# used; set them only to override. Order is the model's.
GROUP_NAMES = {}

# Accent and wash for each group. The accent carries the text and the border;
# the wash is the fill. Never a saturated fill — text on it must stay readable.
PALETTE = {
    # 'AP': ('#1F6FB2', '#E8F2FB'),
}
DEFAULT_COLOUR = ('#1F3864', '#EEF3FA')

# --------------------------------------------------------------- the reader's words
# The words the reader's edition uses for the standard's levels of goal. The model
# keeps the standard's words; the document explains each of these in its glossary.
READER_LEVELS = {
    'summary': 'a whole outcome',
    'user goal': 'one sitting',
    'subfunction': 'a shared step',
}
SUBFUNCTION_WORD = 'shared step'

# --------------------------------------------------------------- sanitisation
# Strip rules particular to this document: internal source names, a jurisdiction
# a generic model must not name, house vocabulary a reader has no use for.
# (pattern, replacement) applied in order, before the generic rules.
EXTRA_STRIP = [
    # (r'\bInternalCodename\b', ''),
]

# Terms that must never survive into the finished document. The release gate
# fails on any of them, with the reason shown here.
EXTRA_FORBIDDEN = [
    # (r'\bInternalCodename\b', 'an internal source name'),
]

# Abbreviations the document may use before expanding them, because the cover
# and the running header carry them ahead of any sentence. Each still has to be
# expanded somewhere in the body — name the expansion here and the gate checks it.
ABBREVIATIONS = {
    # 'ABC': 'a better case (ABC)',
}

# Words in capitals the release gate should not read as abbreviations — the
# document's own words written in capitals for emphasis.
COMMON_WORDS = set()
