<!-- fixture: Progressa (fictional) · canonical: tests/progressa.md, and page 3.6 of the service design course with its worked example · keep consistent with them -->
# Worked example — the open lines of a review, turned into cards for the Registrar

Progressa is fictional. Every body, date and figure here is invented. The example comes
from page 3.6 of the service design course, *The review: three people, every open line
given a name*, and from its worked example for Progressa.

## What the learner pastes

PHEQA, the Progressa Higher Education Quality Authority, held the review of the screens for
a provisional licence. Three people sat at the review: the supplier's analyst, who owns the
screens; the supplier's builder; and the head of the registration desk. The Registrar of
PHEQA convened it and accepts its record. She does not take one of the three seats.

The record holds five open lines:

| Line | What is open | Owner | Date |
| --- | --- | --- | --- |
| 1 | Show the fee due on S2, beside the standards, as well as on S4 | The supplier's analyst | 26 November 2026 |
| 2 | Is a name held by an institution whose licence was cancelled still held, for the check on S3? | The Registrar of PHEQA | 3 December 2026 |
| 3 | S3 asks for the governing board as one block of text; the desk asks for each member's name and role on its own line | The supplier's analyst, after the head of the registration desk confirms the list of roles | 26 November 2026 |
| 4 | The failure "PNIA does not answer at sign-in" tells the applicant nothing about when to try again. What may the screen say? | The head of the ICT unit of PHEQA, after asking PNIA for its published service hours | 3 December 2026 |
| 5 | The builder cannot tell from S5 whether the confirmation can be printed. Is a printed confirmation asked for anywhere? | The Registrar of PHEQA, against the register of requirements | 26 November 2026 |

The learner asks: *"Make the page for the Registrar."*

## The inputs the skill asks for

- **Who rules:** the Registrar of PHEQA, on lines 2 and 5, and on whether she accepts the
  screens. The owners rule on lines 1, 3 and 4.
- **By when:** 3 December 2026.

## The cards, as the numbered list in the chat

**Decisions**

1. **A name after a cancelled licence**
   *Background.* The screen for a new application checks that no other institution holds
   the name that the applicant wants. The record does not say what happens to the name of
   an institution whose licence was cancelled.
   *Question.* When a licence is cancelled, does the institution's name stay held?
   a. **It stays held** — a new applicant cannot take the name; the check refuses it, and
      students do not confuse the new institution with the old one.
   b. **It is free at once** — a new applicant can take the name on the day of the
      cancellation; the check lets it through.
   c. **It stays held for a period that you set** — type the period in the note; the check
      refuses the name until the period ends.
   d. **Establish the fact first** — read the rules of PHEQA on names before you choose;
      if they settle it, the screen follows them.
   *Note: d is recommended. If the rules of PHEQA say nothing, a, b or c is a policy
   choice, and it is yours.*
   *Who rules:* the Registrar of PHEQA. *Touches:* line 2 · the answer goes into the
   shared groundwork of the service.

2. **Accept the screens now?**
   *Background.* The screens are accepted when every open line is closed, or when each
   line that stays open has an owner and a date.
   *Question.* Do you accept the screens now, while three lines stay open with their
   owners — the fee on the second screen, the members of the board, and the message when
   the identity service does not answer — or after every line is closed?
   a. **Accept now, with owned lines open** — the work goes on to the next document; the
      three open lines travel with their owners and dates.
   b. **Accept when every line is closed** — the work waits until the last line closes, on
      3 December 2026 at the latest.
   *Note: rule card 3 first. If a printed confirmation is asked for, the screens change,
   and a may be too early.*
   *Who rules:* the Registrar of PHEQA. *Touches:* lines 1, 3 and 4 · the record of the
   review.

**Quick answers**

3. **A printed confirmation**
   *Background.* The last screen confirms the application. The builder cannot tell
   whether the applicant must be able to print it.
   *Question.* Must the applicant be able to print the confirmation?
   a. **Establish the fact first** — read the register of requirements; the screen follows
      what it says.
   b. **No** — the screen offers no printed confirmation.
   c. **Yes** — add the need to the register of requirements first; then the screen
      changes.
   *Note: a is recommended. This is a fact in a document, not a preference.*
   *Who rules:* the Registrar of PHEQA. *Touches:* line 5 · the register of requirements.

**Not yours to rule**

- **The fee on the second screen** (line 1) — the supplier's analyst changes the screen;
  it was agreed at the review. Closes by 26 November 2026.
- **The members of the board, one to a line** (line 3) — the analyst changes the screen
  after the head of the registration desk confirms the list of roles. Closes by
  26 November 2026.
- **The message when the identity service does not answer** (line 4) — the head of the
  ICT unit of PHEQA decides, after PNIA gives its published service hours. The answer goes
  into the architecture. Closes by 3 December 2026.

## The page

`decisions-for-the-registrar.html` — *Open the page, click an answer on each card, press
Copy answers, and paste the block back here.*

## What the skill does with the answers

The Registrar's block comes back, for example *"1 → Establish the fact first · 2 → Accept
when every line is closed · 3 → Establish the fact first"*. The skill writes each answer
against its line, and names the document where it goes. Lines 2 and 5 stay open until the
Registrar has read the rules and the register and ruled again. The skill does not close
them.

## The safeguard, as the Registrar reads it

The Registrar rules. The page only records her answers. Each answer goes into the document
that owns the fact: the shared groundwork for line 2, the architecture for line 4, the
register of requirements for line 5.
