# The output contract

Every skill in this kit obeys all six rules. They exist because the August 2026
play tests broke each one at least once, and each break severed the workbook chain.

## 1. Text in, text out

The output is markdown **in the chat**: tables, headed sections, lists. Never a
file, never a `.docx`, never a chart, never an image, never a screenshot. A table
inside a picture cannot be pasted into the next play; a `.docx` cannot be read by
the assistant that runs 1.7 after 1.6.

This is why every skill declares `disallowed-tools: Write`. If the learner asks
for a file, produce the text and say they can save it themselves — the chain needs
the text.

## 2. Posts, not names

Refer to **the post**: *the PDGA Director-General*, *the MoEYS ICT Director*, *the
head of the civil service*. Never the name of the current holder, even where the
name is public and easy to find. Sources will hand you names; drop them at the
point of writing, not at the point of review.

If a source is only comprehensible with the name (a court ruling, a signed
instrument), cite the document, not the person.

## 3. Strip your own reasoning

"The search confirms… let me now produce the table" is the model talking to
itself. The learner will paste this output into the next play. Cut every word of
it. The provenance header is the first thing in the output and the artefact is the
second.

## 4. Record the clarifying answers

Some skills must ask before they can answer — repository size, budget posture,
which sector. Ask at most **three** questions, ask them all at once, and when the
answers come back, write them into the artefact as an *Inputs supplied by the
learner* block. They are part of the artefact, not a conversation that evaporates.

## 5. Every claim carries its source

Inline, in the row it belongs to: URL, tier, access date. Not a bibliography at
the end — a learner checking one row should not have to match it to a footnote.
Apply `source-tiers.md`; mark anything unverified with ⚠.

## 6. Hand the safeguard back

Every play in the course ends with a safeguard — the specific way *this* output
can mislead. A skill that does the verification still ends by naming what remains
the learner's judgement: what to confirm with a person, what counsel must approve,
what only a costing exercise can settle. Restate it as the learner's **next
action**, not as a disclaimer.

## What this contract is not

It is not a licence to be terse. Sourced, complete and long beats clean and thin.
The rules govern the *form* of the output, never its ambition.
