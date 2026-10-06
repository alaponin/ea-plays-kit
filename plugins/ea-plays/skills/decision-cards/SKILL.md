---
name: decision-cards
description: >-
  Turn a list of open questions into one page of decision cards that the person who must
  rule can answer by clicking, each card complete on its own, and read the answers back:
  the open lines of a review, the assumptions and losses of a model, the proposed
  decisions of a response matrix, the asks that a learner takes to a minister. Serves the
  four asks of EA play 1.7, the response matrix of the education DPI roadmap course
  (6.7), and the review record (3.6) and the model review (4.5) of the service design
  course. It is the one skill of this kit that makes a file, and it always gives the same
  cards as a numbered list in the chat. Use when someone says "make decision cards", "what
  must my minister decide", "turn these open lines into questions", "one page of
  decisions", "a questionnaire for the director", "yes-or-no questions for the owner",
  "put the four asks on one page", "read back the answers", "record the rulings".
allowed-tools: Read, Write
disallowed-tools: Edit, NotebookEdit
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
---

## What this skill does

A decision often waits because the person who must rule cannot find the question. The
question is inside a long record, a table or a model. This skill takes each open question
out and puts it on a card. The card says what is open, why it matters, and what follows
from each answer. The person reads the card once and answers it.

**The named person rules. The page only records.** The page never decides. It never
pre-selects an answer, and it never closes an open line by itself. An answer counts as a
ruling only when the person whose post the card names gives it.

**This skill makes a file.** It is the one skill of this kit that does. The other skills
follow rule 1 of `references/output-contract.md`: text in, text out. This skill keeps that
rule for its record. It writes the same cards as a numbered list in the chat, and that list
is what the next play reads. The file is for the person who rules: one HTML page that opens
in any browser, with no internet connection and nothing to install.

If the assistant cannot write a file, the numbered list is the whole output. See *When no
file can be made*.

## Inputs

Any list of open questions, in any form. For example:

| Course and page | What the learner pastes | Who rules |
| --- | --- | --- |
| EA course 1.7 | The four asks, and the open points of the draft ToR (A7) | the minister |
| Education DPI roadmap course 6.7 | The draft response matrix, with a proposed decision for each comment | the post that the team names to decide each row |
| Service design course 3.6 | The record of a review: the open lines, their owners and their dates | the convener who accepts the record, and the owner of each line |
| Service design course 4.5 | The list of assumptions and losses of the application model | the owner of the service |

Ask at most three questions, together, before you start: who rules (by post); whether that
post rules on all the cards or on some of them; and the date by which the answers are
needed. Record the answers in an *Inputs supplied by the learner* block.

If the input names no one who rules, ask. Do not choose the person yourself.

## Procedure

1. **Read the list from what the learner pasted.** Do not work from memory of an earlier
   conversation. Keep each line's own words. Note the identifier of each line, if it has
   one, for example `CM-05` or "line 4 of the record".

2. **Group the lines into decisions.** Two lines that ask the same question in two places
   are one decision, and one card. Two different questions are never one card. If the
   course page says one card for each line, follow the page. The model review of the
   service design course says one question for each loss.

3. **Sort the cards into three groups, and label the groups on the page.**
   - **Decisions** — the answer changes the design, the plan or a document. Put these
     first.
   - **Quick answers** — a yes or a no, a date, a number, a signature.
   - **Not yours to rule** — a fact to establish, a line that another post owns, or a line
     that waits for another body. Show these in grey. Give one line that says why no answer
     on this page can close them, and who or what closes them. Never drop them. A person
     who finds an omission stops trusting the page.

4. **Write each card.** Each part except the last line is in plain words.
   - A **title** of five words or less.
   - **The background**, in one or two sentences, so that the card stands on its own.
   - **The line's own words**, in quotation marks, where the course asks for them.
   - **The question**, in one sentence. It states a choice.
   - **Two to four options.** Each option says what follows if the person chooses it:
     what changes, what it costs, what it closes off. An option that gives only its name
     is not finished. The options do not overlap, and together they cover the choice.
   - **The note**, in italics: the trade-off, the link to another card, or your
     recommendation. Do not pre-select the recommendation.
   - **Who rules**: the post. Never the name of a person.
   - **The last line, `Touches`**: the identifiers of the lines that the answer closes,
     and the document where the answer is written. This is the only place for
     identifiers, codes and section numbers.

5. **Keep these rules on every card.**
   - **Nothing internal in the words of the card.** No identifier, no file name, no code,
     no section number, no name of a tool. If an internal thing must be named, name it in
     ordinary words, and put the identifier in `Touches`.
   - **A card does not send the reader to another document.** "See the report" means that
     the card is not finished. Put the fact in the card.
   - **Never invent a number.** If no source gives a figure, the option says "a period
     that you set — type it in the note".
   - **Offer "establish the fact first"** when a document can settle the answer, and
     recommend it. Do not ask a person to choose by preference what a document can answer.
   - **Say when two cards must be ruled together.** The person cannot see a link that you
     do not write down.
   - **Posts, not names.** A card names the post that rules. The person can type their
     own name on the page when they answer. The skill never fills it in.

6. **Write the numbered list in the chat.** The shape is in *Output contract*.

7. **Build the page** from `references/card-page-template.html`. Keep it one file, with the
   style and the script inside it. Do not load anything from the internet. Do not use the
   browser's storage. Keep the light and the dark colours. Each option is a real click
   target, the selection shows, and the tally moves. *Copy answers* gives a text block.
   Fill in one card block for each card, in the order of the list. Give the file a plain
   name, for example `decisions-for-the-registrar.html`.

8. **Check the page before you give it.** Read each card as the person who must answer it.
   Then confirm, card by card:

   | Check | Done |
   | --- | --- |
   | No identifier, code, file name or section number outside `Touches` | ☐ |
   | The background needed to answer is inside the card | ☐ |
   | The question is one sentence and states a choice | ☐ |
   | Each option says what follows from it | ☐ |
   | Nothing sends the reader to another document | ☐ |
   | The card names the post that rules | ☐ |
   | No option is pre-selected | ☐ |

   A card that fails one of the first two checks is worse than no card. It costs the
   person the time that it was made to save.

9. **Say how to answer, in one line.** For example: *Open the page, click an answer on each
   card, press Copy answers, and paste the block back here.*

10. **Read the answers back.** The page cannot send anything. The copied block is the
    channel. When the block comes back, write each answer against each line that its card
    touches. Name the document where the answer goes: the document that owns the fact. A
    line stays open until the post that the card names has ruled on it. Never mark a line
    as ruled on any other ground.

## When no file can be made

Some assistants, and some settings, do not let a skill write a file. Then give the
numbered list alone, with the options of each card as a., b., c. Ask the person to answer
with the number and the letter, for example *"2 b, 5 a"*. Read the answers back as in step
10. Nothing else changes: the same cards, the same rules, the same person who rules.

## Output contract

Write the provenance header first (`references/provenance-header.md`). The decision page
is not a numbered workbook artefact, so the **Artefact** field gives its name, for example
`Decision page — the four asks`. **Consumed** names the artefact that the lines came from,
for example `A7`, or `—`. **Feeds** is `—`. Then write:

- **Inputs supplied by the learner** — who rules, and by when.
- **The cards, as a numbered list** — one item for each card: the title; the background;
  the question; the options as a., b., c., each with what follows from it; who rules;
  `Touches`. Under the heading *Not yours to rule*, the lines that no answer on the page can
  close, each with what closes it.
- **The page** — the name of the HTML file, and the one line on how to answer.
- **The safeguard** — below.

Posts, not names. No analysis before the header. See `references/output-contract.md`, and
the one exception that this skill makes to its rule 1.

## Safeguard handed back

- **The named person rules. The page only records.** A click is not a ruling until the
  post that the card names has given it. If you answer a card yourself to test the page,
  clear it before you send the page.
- **Each answer goes into the document that owns the fact.** An answer that stays in the
  page or in the chat is lost. Write it into that document, and run again the play that
  checks the document.
- **A card in other words can draw a "yes" that was not meant.** Before you send the page,
  read each card against the line that it came from. Where the course asks for the line's
  own words, keep them.

## Fixture material

- `references/worked-example.md` — the review of the provisional-licence screens at
  PHEQA, from page 3.6 of the service design course: five open lines, turned into cards for
  the Registrar. Progressa is fictional.

## References

- `references/card-page-template.html` — the page: one file, with the cards, the tally and
  the *Copy answers* block.
- `references/worked-example.md` — the Progressa example above.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` ·
  `references/workbook-chain-gif.md` — the shared contract.
