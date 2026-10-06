# Use case diagrams for a Word document — the render step

Two independent things have to be right: the diagram must be a use case diagram,
and it must be legible after Word scales it down. Both are enforced by the
scripts; this page explains what they enforce and why.

> This supersedes the generic advice in the `docx-diagram-style` skill for use
> case diagrams specifically. That skill recommends a 10-inch canvas; for a
> figure this dense, 10 inches is still too wide. The reasoning is identical —
> only the number changes.

## The form

A use case diagram is not a picture of boxes. It has four elements and it needs
all four:

```
        ┌──────────────────────────────────────┐
        │              Allocation              │   ← the package's frame,
   ○    │                                      │     named at the top
  /|\ ──┼───  (      UC-03  Allocate      )    │
  / \   │     (          a plot          )    │   ← the goal, as an oval
        │                                      │     carrying reference and name
 Garden │     (  UC-05  Place an applicant )──┼──  ○
 officer│     (    on the waiting list     )   │   /|\
        │                                      │   / \
        └──────────────────────────────────────┘   Resident
   ↑                                                 ↑
   an actor, outside the frame,                      actors are split left
   as a stick figure                                 and right of the frame
```

**The frame** is drawn once per figure, titled with the package it holds: a
package is drawn as a titled frame (M12), and the system's one boundary (M1) is the
overview figure, drawn once for the whole model. Nothing that is not a use case goes
inside a frame; no actor goes inside one, ever.

**The ovals** carry two lines: the use case reference and its name, read from
the record headers through `model.json` and never typed here (M8).

**The actors** are stick figures outside the frame, named as the catalogue names
them (M4), split left and right so association lines stay short. Clocks and other
systems are drawn the same way (M6).

**The associations** are plain lines from an actor to the use case that serves
its goal. Not arrows — a use case association has no direction. Include and
extend relationships are a different notation and are shown in the relationships
section of the document rather than crowded onto every group figure (M11).

**Six use cases per figure, at most.** A package with sixteen goals becomes three
figures captioned "part 1 of 3" and so on. Cramming a group onto one page is how
the fonts got unreadable in the first place.

## The arithmetic

Word scales an image to the column width. Every font in it scales by the same
factor.

```
scale_factor    = display_width / canvas_width
font_in_document = source_font_pt × scale_factor
```

The text column of an A4 page with 2.54 cm margins is 15.9 cm — 6.26 inches.

| Canvas | Scale | 10.5 pt source → | Verdict |
|---|---|---|---|
| 25 in | 0.25 | 2.6 pt | invisible |
| 18 in | 0.35 | 3.6 pt | this is what shipped, once |
| 10 in | 0.63 | 6.6 pt | still below the floor |
| **7.2 in** | **0.87** | **9.1 pt** | **the working value** |

A tall figure is scaled by its *height* instead, when the height would otherwise
overrun the page — the effective width becomes `MAX_H × w / h`, and the fonts
shrink further. `check_readable()` accounts for this; do not compute it by hand.

**The floor is 7.5 pt in the document.** Below that a reader zooms, and a reader
who has to zoom says the diagram is broken.

Source sizes that work on a 7.2-inch canvas:

| Element | Source pt | In the document |
|---|---|---|
| Figure title | 15.0 | 13.0 |
| Boundary name | 12.0 | 10.4 |
| Use case reference | 11.5 | 10.0 |
| Use case name | 10.5 | 9.1 |
| Actor name | 10.5 | 9.1 |

## The font

The document's body is Calibri; **Carlito** is its metric-compatible clone and
is what a Linux build normally has. Naming a font that is not installed does
not fail — matplotlib silently substitutes its default, whose wider glyphs push
every label past the shape that holds it, and the geometry guard then reports a
dozen defects that are really one missing font.

So the family is resolved once, in `diag.pick_font()`, against what is actually
installed, and the build says which one it used. `UCM_FONT` overrides the
preference order. A substituted font is not fatal, because every label is
wrapped by **measurement** rather than by a guessed character count:
`fit_text()` and `fit_top_text()` try successively tighter wraps and keep the
widest one that measurably fits.

That combination is what makes the figures portable. A wrap width in characters
is a guess about glyph widths, and the guess is wrong the moment the build moves
to another machine.

## The guards

`diag.py` registers every shape and every text as it is drawn, then checks the
finished axes. `save()` raises rather than writing a figure that fails, so a bad
figure cannot reach the document.

| Guard | What it catches |
|---|---|
| `check_overlaps` | two shapes occupying the same space |
| `check_text_fits` | a label wider or taller than the shape that owns it |
| `check_lines_clear_of_text` | an association line crossing a name |
| containment assertion | an oval crossing the boundary that should hold it |
| `check_readable` | any text below the legibility floor once scaled |

A shape may own more than one label — an oval owns its reference and its name —
so `_register()` takes both, and the containment check treats them together.

When a guard fires, fix the layout. Widening a tolerance to get the figure out
means the next figure fails silently instead of loudly.

## Colour

A dark accent with a very light wash, one pair per group. The accent carries the
border and the text; the wash is the fill. Never a saturated fill: text on it is
unreadable in print and at a glance on screen.

Colour must not be the only carrier of meaning. Every group is identified by its
name and its code as well as its colour, so the figure still works in greyscale
and for a reader who cannot distinguish the hues.
