# Reading an Estonian model law

Step 1 of this skill says: fetch the published model first. For the Estonian models, a
plain fetch fails, and it fails in silence. This file says how to read an Estonian
instrument correctly, and how to cite it. Read it before you adapt from an Estonian model.

**This needs a browser tool.** The portal of Estonian law, Riigi Teataja, builds each page
with JavaScript. A tool that runs the page's scripts can read it: a browser that the
assistant can drive. A plain web fetch cannot. If you have no browser tool, see
*When you cannot read the text*, at the end.

## The Estonian instruments that the decree plays adapt from

Read on 6 October 2026. The text in force changes several times a year. Check it again
each time, and quote no section number from this table. Quote it from the text that you
read today.

| Instrument | What the decree plays take from it | What was in force on 6 October 2026 |
| --- | --- | --- |
| **Public Information Act** — *Avaliku teabe seadus* (AvTS). Chapter 5¹ *Databases* (*Andmekogud*); § 43⁹ *Support systems to the state information system* | The mandatory connection. § 43⁹(1) clause 5 names the data exchange layer of information systems as a support system. § 43⁹(3) makes the support systems mandatory for all state and local government databases. § 43⁹(5) says that data is exchanged with, and between, the databases of the state information system through the data exchange layer. | Estonian text: in force from 01.10.2026 to 30.11.2026, published RT I, 30.06.2026, 9. English translation: of the text in force from 01.09.2025 to 15.03.2026, published 11.09.2025 — an older text. |
| **Government Regulation No. 105 of 23 September 2016**, *Infosüsteemide andmevahetuskiht* (*Data exchange layer of information systems*), the X-Road regulation | The operating authority's powers: § 3 the principles of managing X-tee, § 4 the tasks of the centre, § 5 joining X-tee and membership, § 6 refusal to admit, § 14 the end of membership. Its first line gives its legal basis — a model for the enacting formula of a Preamble. | Estonian text in force from 01.05.2026, published RT I, 28.04.2026, 13. A search of the English translations by title found none in force. |
| **Information Society Services Act** — *Infoühiskonna teenuse seadus* (InfoTS) | The interoperability play pages name this act for the structure of mandatory connection. Read it, but note that it governs the providers of information society services. The text read on 6 October 2026 does not mention a data exchange layer. The duty to use the exchange layer is in the Public Information Act, § 43⁹. Say which act you adapted from. | English translation: in force from 18.08.2026, published 27.07.2026. |

The first line of the regulation is a good example of the three traps together. It says
that the regulation is made under clause 5 of subsection 1 of § 43⁹ of the Public
Information Act. The line exists in Estonian only, the page needs a browser tool, and the
extracted text writes the section as "§ 439".

## The three traps

Each trap gives a citation that looks right and is wrong. Nothing shows an error.

### 1. A plain fetch returns a page with no law in it

On 6 October 2026, a plain fetch of an act's page returned only this line: *"You need
Javascript enabled to use this site."* There is no error code. Use the browser tool.

### 2. The English text can be an older text

Each act page starts with a block like this one, from the English translation of the
Public Information Act, read on 6 October 2026:

```
In force from:          01.09.2025
In force until:         15.03.2026
Translation published:  11.09.2025
```

**An "In force until" date in the past means that you read an older text.** On the same
day, the Estonian text in force ran from 01.10.2026. Read the block before you read the
law, and write its dates into the citation.

**The English text is not official. The Estonian text prevails.** For a point that the
decree depends on, read the provision in the Estonian text too. Most Government
regulations exist in Estonian only. Then translate the provision yourself, and say that
you did.

### 3. Superscript numbers break in extracted text

Estonian law inserts new parts with a superscript number: Chapter 5¹, § 43⁹, § 43¹⁰,
subsection (2¹). The page shows the superscript. The extracted text drops it.

| On the page | In extracted text | Write it as |
| --- | --- | --- |
| Chapter 5¹ | `Chapter 51` | Chapter 5¹ |
| § 43⁹ | `§ 439` | § 43⁹ |
| § 43¹⁰ | `§ 4310` | § 43¹⁰ |
| § 3¹ of the Information Society Services Act | `§ 31` | § 3¹ |
| subsection 4 of § 43³ | `subsection 4 of § 433` | § 43³(4) |

**How to see it.** A "§ 439" between § 43 and § 44 is § 43⁹. It is not section four
hundred and thirty-nine. A "Chapter 51" between Chapter 5 and Chapter 6 is Chapter 5¹.
When you are not sure, look at the heading on the page, or in the table of contents,
where the superscript stays. Or read the Estonian text.

This trap is the worst of the three. "§ 439" is a citation that a reader cannot find, and
cannot easily prove wrong.

## How to read an act, step by step

1. **Find the address with a search.** Do not guess an address. A web search for the
   act's English or Estonian name, with "riigiteataja", gives the address, even though a
   plain fetch of the page fails. The portal's own search works in the browser tool: one
   search for the Estonian texts, and one for the English translations.
2. **Open the page in the browser tool.** These address forms open the text in force:
   - English, the latest translation: `https://www.riigiteataja.ee/en/eli/<id>/consolide/current`
   - Estonian, the text in force: `https://www.riigiteataja.ee/akt/<id>?leiaKehtiv`

   Each consolidation has its own `<id>`. An `<id>` from an older consolidation can give
   *"Page not found"*. Then search again.
3. **Read the block of dates.** Write down *In force from*, *In force until* and, for a
   translation, *Translation published*.
4. **Find the heading.** Look for the section in the page's table of contents, where the
   superscript stays.
5. **Get the page text, and take the part that you need.** A long act is long. Take only
   the section that you adapt.
6. **Check for a repeal.** A repealed provision stays in the text with the mark
   `[Repealed – RT I, …]` in English, or `[Kehtetu – RT I, …]` in Estonian. Do not cite
   it.
7. **Write the citation**, as below. Then close the tab.

## Reading the structure

| Estonian | English | Shown as |
| --- | --- | --- |
| seadus | act | — |
| määrus | regulation | — |
| peatükk | chapter | `Chapter 5¹` |
| jagu | subchapter | `Subchapter 3` |
| **paragrahv (§)** | **section** | `§ 43⁹.` |
| **lõige** | **subsection** | `(5)` |
| punkt | clause | `5)` |

**A false friend.** An Estonian *paragrahv* is an English **section**. It is not a
paragraph. `§ 43⁹(1) clause 5` means section 43⁹, subsection 1, clause 5.

**Amendment notes** follow each amended provision, for example
`[RT I, 06.01.2016, 1 – entry into force 16.01.2016]`. RT I is part I of Riigi Teataja. The
note tells you when the wording that you quote came into force.

## Citing it

The first citation gives the reader all that they need to find the text:

> Public Information Act (*Avaliku teabe seadus*, AvTS) § 43⁹(5) — Estonian text in force
> from 01.10.2026 (RT I, 30.06.2026, 9), checked against the English translation of the
> text in force 01.09.2025–15.03.2026; riigiteataja.ee; read 6 October 2026.

After that, `AvTS § 43⁹(5)` is enough.

Two habits. **Name the consolidation that you read**, not only the act: a reader who
checks in six months may see another text. And **say when you quote an English
translation**, because it is not official.

## When you cannot read the text

If you have no browser tool, or the page does not open, do not fill the gap from memory.

- Say what you could not check. For example: *"The duty to use the exchange layer is in
  the Public Information Act, § 43⁹. I could not open the text in force today to confirm
  the subsection."*
- Mark the line ⚠ *unverified — learner to confirm*, and keep `[confirm]` for the section
  number.
- Never write a section number that you did not read. An invented number is worse than a
  gap, because it passes the review.
- If no published model can be read for an article, follow the one rule of
  `published-models.md`: the article is not drafted.
