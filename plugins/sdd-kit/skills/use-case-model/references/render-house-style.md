# House style — the render step

The style below matched an organisation's existing requirements deliverables.
Yours may differ — **read the reference document first and take the values off
it** rather than assuming these. What matters is not these particular numbers but
that the document looks like it belongs on the same shelf as the ones around it.

## Reading a style off an existing .docx

Five minutes with `python-docx` answers most of it:

```python
from docx import Document
d = Document('reference.docx')
for p in d.paragraphs[:120]:
    if p.style.name.startswith('Heading') or p.runs:
        r = p.runs[0] if p.runs else None
        print(f"{p.style.name:16} {r.font.name if r else '':10} "
              f"{r.font.size.pt if r and r.font.size else '':>5} "
              f"{r.font.color.rgb if r and r.font.color and r.font.color.rgb else ''}")
s = d.sections[0]
print('margins', s.top_margin.cm, s.left_margin.cm)
for t in d.tables[:3]:
    print(t.style.name, len(t.columns), 'cols')
    print(t.rows[0].cells[0]._tc.xml[:400])   # header fill lives in w:shd
```

Look for: the heading font, sizes and colour; the body size and line spacing; the
table header fill and whether body rows alternate; where rules and dividers are
used; and how figures are captioned.

## Palette

| Role | Hex | Used for |
|---|---|---|
| Ink | `1F2933` | body text |
| Navy | `1F3864` | headings, table header fill |
| Mid blue | `2E75B6` | third-level headings, subtitle, figure captions |
| Grey | `666666` | the organisation line on the title page |
| Rule | `B4C6E7` | divider rules, table borders |
| Band | `F2F7FB` | the alternating table row |
| Label | `D6E4F0` | the label column of the metadata table |

Dark accent, very light fill, always. Text on a saturated fill cannot be read.

## Typography

| Element | Size | Weight | Colour |
|---|---|---|---|
| Title | 22 pt | bold | navy |
| Subtitle | 16 pt | regular | mid blue |
| Heading 1 | 18 pt | bold | navy |
| Heading 2 | 15 pt | bold | navy |
| Heading 3 | 13 pt | bold | mid blue |
| Body | 10.5 pt | regular | ink |
| Table body | 9 pt | regular | ink |
| Figure caption | 9 pt | italic | mid blue |

Calibri throughout, 1.14 line spacing, 6 pt after a paragraph. A4 with 2.54 cm
margins, giving a 15.9 cm text column — the number every table and figure width
is scaled to.

## Tables

- Header row: navy fill, white, bold, and **repeated on every page** it spans.
- Body rows alternate white and `F2F7FB`. Nothing else is shaded.
- Rows do not split across a page (`cantSplit`).
- Column widths are given as proportions and scaled to exactly 15.9 cm. Widths
  that do not sum to the column width are how a table ends up overhanging the
  margin in Word but not in the PDF render.
- A total row, when there is one, is bold and carries no fill.

## Title page

Organisation line in grey capitals, a rule, the title in navy, the subtitle in
mid blue, a second rule, then a metadata table with shaded labels: document,
purpose, status, scope, audience, contents. Six rows or fewer — a title page that
needs more is answering questions nobody asked.

The scope row states the size of the model, and it is **derived**: `words()`
spells the count from `model.json`. Never typed.

## Contents

Generated in two passes (build → render → locate headings → write page numbers →
build again). Not a Word TOC field: the field renders as its own placeholder text
until a reader presses F9, and no reader presses F9.

Level 1 entries bold, level 2 and 3 indented and regular, dot leaders, right-
aligned page numbers.

## Running header and footer

Header: the document's short name on the left, its status on the right, both in
small grey italics. Footer: the programme name on the left and a real `PAGE`
field on the right. A typed page number is wrong the moment anything moves.

## Figures

Centred, at the column width or scaled down to fit the page height, with the
caption immediately below in italic mid blue: `Figure N. <what it shows>`.

The picture paragraph carries `keep_with_next` so the caption can never be
stranded on the following page.

## Compatibility mode

Set `compatibilityMode` to 15 in `settings.xml` by **overwriting** the existing
value. Appending a second setting does nothing — Word reads the first one — and
the diff looks entirely reasonable, which is why it was shipped twice.
