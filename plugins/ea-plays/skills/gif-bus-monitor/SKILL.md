---
name: gif-bus-monitor
description: >-
  Summarise the health of a Government Interoperability Framework bus from its operational
  logs and flag anomalies as questions for a human — the KP2 play 5.8 that produces the
  bus-health summary and anomaly list (B35). Reads exchange METADATA only — timestamp,
  calling subsystem, called service, outcome, latency — and refuses to proceed if the logs
  carry citizen personal data. Use when someone says "summarise the bus logs", "bus health",
  "X-Road operational monitoring", "which services are failing", "anomalies in the exchange
  logs", "a caller that never called this before", "off-hours surge", "quarterly compliance
  note for the Steering Committee", "conformance re-check", "monitor the bus", or names KP2
  play 5.8.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
---

## What this skill does

This skill reads the operational logs of the bus and writes **B35, the bus-health summary
and anomaly list**. It monitors the traffic. It never reads the cargo.

Play 5.8 is the one play in KP2 where the learner pastes operational data rather than a
document. The bare play defends the citizen with one instruction: metadata only, and stop
if personal data appears. This skill makes that instruction a **gate that runs first**,
before any analysis, and it adds the published reference for what an X-Road operational
monitoring record contains — so that a field the learner pastes that is not in that record
is recognised as cargo, not traffic. It also gives the summary a shape the Operating
Authority can act on: a question per anomaly, three things for the week, one paragraph for
the quarter.

## Inputs

| Play | Makes | Needs |
| --- | --- | --- |
| 5.8 | B35 Bus-health summary and anomaly list | **the metadata logs** — timestamp, calling subsystem, called service, success or failure, latency; B33 (which services and callers are expected); the period the logs cover |

Ask at most three questions, together: the period; whether the logs are from the
Security Servers' operational monitoring or from an application; which callers and
services are expected (if B33 is not to hand). Record the answers in the artefact.

## Procedure

1. **Run the personal-data gate before anything else.** Read the field names and a sample
   of values. The permitted set is in `references/log-fields.md`: identifiers of
   *subsystems* and *services*, timestamps, outcomes, sizes, latencies, request ids. If
   any field or value is, or could be, a person's identifier, name, date of birth, address,
   or a payload — a national number in a path, a query string with a citizen's attribute, a
   response body — **stop**. Write the provenance header, then one section: *Data-protection
   issue — the logs contain personal data*, naming the field (not the value), and the next
   action (strip the field at source, involve the data-protection officer). Produce no
   summary. Do not paraphrase the values.

2. **Establish the baseline from B33 and the catalogue.** Which subsystems are expected to
   call which services (the ACL grants). A caller-service pair not in that set is a finding
   even at one call.

3. **Compute, in a table, per service**: calls, successes, failures, failure rate, median
   and p95 latency where the logs allow, and the same for the previous comparable period if
   the logs cover it. Say what the logs do not allow (no latency field → no latency row).
   Do arithmetic on what is pasted; never estimate a rate.

4. **Flag anomalies as questions.** Rising failure rate; rising latency; a spike in volume;
   a caller that has not called this service before; an off-hours surge; a run of
   access-denied faults from one caller; a service silent in a period it was busy before.
   For each: the observation with its numbers, the period, and the **question** for a
   person — *"Did PNEA's exams window open on the 3rd, or is this a retry loop?"* — never a
   conclusion. `references/anomaly-rubric.md` gives the patterns and the question shapes.

5. **Do not infer anything about a citizen.** No row of the output concerns an individual.
   A pattern that could only be explained by one person's activity is reported as *a
   pattern the Operating Authority should examine at source*, and no further.

6. **Write the week and the quarter.** The top three things the Operating Authority
   should look at this week, ranked by citizen impact then by member obligation. One
   paragraph for the quarterly Steering Committee report: which members show sustained
   failure or unusual behaviour that warrants a conformance re-check (B29, B22) — by
   subsystem, with the numbers, and with the SLA target (B30) beside them where the learner
   supplied one.

7. **Run `cite-or-discard`** on the operational monitoring protocol citation before you
   give the output. A claim about what the record can or cannot contain that the fetched
   protocol does not carry is *not supported*: drop it, and say the field set is
   unverified. The logs themselves are input, not a source, and are not cited.

## Output contract

Write the provenance header first (`references/provenance-header.md`). The Sources line
counts the operational monitoring protocol citation; the logs are input, not a source.
Then:

- **Gate result** — one line: *no personal data found in the fields pasted* or the
  data-protection issue section (and nothing after it).
- **Volume and outcomes by service** — the table of step 3.
- **Trends** — services with rising failure or latency, with the numbers.
- **Anomalies — questions for a human** — `| # | Observation (numbers, period) | Pattern | Question | Who answers (post) |`, ranked.
- **This week** — the top three.
- **Quarterly compliance note** — one paragraph.
- **What these logs cannot show** — the fields absent, the period's gaps.
- **Inputs supplied by the learner**, then the safeguard.

Text in the chat, never a file and never a chart — a table of numbers is the chart. Posts,
not names; subsystems, not people. Write no analysis before the header. See
`references/output-contract.md`.

## Safeguard handed back

**This play monitors the traffic, never the cargo. Confirm the logs are stripped of
citizen personal data before they go into the prompt — and if this output says they were
not, act on that first.**

- Every anomaly is a question. The answer comes from the member's technical contact, the
  Operating Authority's own monitoring, or the message log examined at source under its
  legal basis — not from this summary.
- A conformance re-check is a governance decision (B16, B19). This note recommends it; the
  Technical Working Group orders it.
- Rates computed on a partial period, or on logs from one Security Server, describe that
  server and that period. Say so when you carry them into the quarterly report.

## References

- `references/log-fields.md` — what an X-Road operational monitoring record contains, the
  permitted field set, and what is cargo.
- `references/anomaly-rubric.md` — the anomaly patterns, the numbers that evidence each,
  and the question shape for each.
- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` ·
  `references/workbook-chain-kp2.md` — the shared contract.
