# Twelve defects that reached a reviewer — the render step

Every one of these got through to a person who had to point it out. Each entry
names what they saw, what actually caused it, and the check that now catches it.
The pattern worth noticing: nearly all of them are a claim made wider than the
evidence behind it.

---

## 1. The overview figure invented a taxonomy

**Seen:** Figure 1 showed a five-part structure. Section 5 listed eleven groups.
They had nothing to do with each other.

**Cause:** the figure was drawn by hand from a mental model of the system; the
section was generated from `model.json`. Two sources, one document.

**Fix:** the figure is built from `model.json` — the real groups, their real
codes, their real counts, and real actor names from the actor catalogue.

**Check 9a:** the groups named anywhere in the document are exactly the groups in
the model, and the gate fails naming the difference in both directions.

> A figure drawn by hand beside generated prose will drift. Not might — will.
> If the document generates a section, generate the figure that summarises it
> from the same data.

---

## 2. Diagram fonts rendered at 4.3 pt

**Seen:** "Font on the diagram is way too small, not possible to read even with
160% increase."

**Cause:** the figures were drawn on a 25-inch canvas and placed in a 16 cm
column. The scale factor was 0.25, so 17 pt source text arrived as 4.3 pt. The
formula was in the diagram standard; it simply was not applied.

**Fix:** canvas 7.2 inches, so the scale factor is near 0.87.

**Guard:** `check_readable()` computes the size every font will have in the
document and raises before the file is written if the smallest falls below
7.5 pt.

---

## 3. The diagrams were not use case diagrams

**Seen:** "your wrong-form diagrams" beside properly organised ones from another
deliverable.

**Cause:** coloured boxes in a grid. Readable, informative, and not a use case
diagram — no boundary, no actors, no associations.

**Fix:** the house convention: titled system boundary, ovals with reference and
name, stick actors outside on both sides, association lines. See
`render-diagram-convention.md`.

> Ask for the reference document before drawing. "Like the ones in X" is a
> five-minute conversation that saves a rebuild.

---

## 4. The table of contents was empty

**Seen:** no contents where the contents should be.

**Cause:** a Word TOC field was inserted. Word renders it as "Right-click to
update field" until someone presses F9. Nobody presses F9.

**Fix:** a generated contents — build, render to PDF, locate the headings in the
rendered text, write the page numbers, build again.

**Check 7:** every heading appears in the contents and every contents entry
carries a page number.

---

## 5. Compatibility Mode in the title bar

**Seen:** Word opened the document in Compatibility Mode.

**Cause:** a second `compatSetting` element was appended to `settings.xml`. Word
reads the first one, which still said 12.

**Fix:** overwrite the existing value to 15. Appending to XML that already holds
the key is a null operation with an innocent-looking diff.

**Check 8:** exactly one `compatibilityMode` setting exists and its value is 15.

---

## 6. Internal identifiers leaked into a table

**Seen:** `BR-14` and an internal authority's name in the rules table of a
document that was supposed to carry neither.

**Cause:** the rules table was filled by a loop that inserted cell text
directly, bypassing `clean()`.

**Fix:** rules renumbered 1..n for the reader; every cell routed through
`clean()`.

**Check 2:** `scan()` runs over the finished .docx and fails on any forbidden
term, wherever it came from.

> Every string. A single raw insertion undoes the whole sanitisation pipeline,
> and it will be in a table, because tables are where loops are.

---

## 7. Association lines crossed actor names

**Seen:** caught by the geometry guard, not by a person.

**Cause:** lines routed straight from actor to oval passed through the text of
other actors.

**Fix:** orthogonal routing through a gutter clear of the labels.

**Guard:** `check_lines_clear_of_text()`.

---

## 8. Ovals overran the system boundary

**Seen:** also caught by a guard, after the guard was extended.

**Cause:** the overlap check exempted frames — a use case *should* sit inside its
boundary — and the exemption also hid ovals crossing the boundary edge.

**Fix:** an explicit containment assertion: every oval's bounding box is inside
its boundary, with margin.

> An exemption in a check is a hole in the check. When you add one, add the
> narrower assertion that covers what the exemption gave up.

---

## 9. Fourteen captions were separated from their figures

**Seen:** the figure at the foot of one page, "Figure 1." alone at the top of
the next.

**Cause:** nothing bound them.

**Fix:** `keep_with_next` on the picture paragraph.

**Check 10:** pair the page of each embedded image (from `pdfimages -list`) with
the page of its caption (from `pdftotext`) in the rendered PDF, and fail on any
that differ.

---

## 10. Codes were used nine pages before they were defined

**Seen:** a figure whose column headings were two-letter group codes, sitting in
section 4; the table defining those codes in section 5.

**Cause:** the figure was placed where it was drawn, not where it could be read.

**Fix:** the figure moved to sit immediately after the table that defines its
headings, with a caption that says so.

**Check 9b and 9d:** a bare group code never stands alone in prose, and no
abbreviation is used before it is expanded.

---

## 11. A section count was stated from a truncated listing

**Seen:** a report claiming a source guide had 27 sections. It has 33.

**Cause:** the command that listed the headings printed 45 of 55 and the output
was read as complete.

**Fix:** none available in code — this is a discipline defect.

> State a claim no wider than the command that produced it. If the output may
> have been truncated, count it a second way before writing the number down.

---

## 12. A parse produced an accusation that was wrong

**Seen:** twice. First, twenty-one stray `F-n` references reported as an
undocumented second findings series — they were ordinary row citations. Second,
fourteen "orphaned captions" reported by a new check — the diagrams are raster
images, so the caption is simply the first extractable text on the page, and the
figures were fine.

**Cause:** in both cases a naive parse, and a conclusion drawn before the parse
was tested against a case known to be good.

**Fix:** for the captions, compare image pages to caption pages instead of
guessing from text order.

> Before reporting what a new check found, run it against something you know is
> correct. A check that fires on a good document is not evidence, it is noise —
> and reporting it as a defect costs the reader's trust in every check beside it.
