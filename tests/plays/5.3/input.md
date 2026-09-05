# Play 5.3 — Map the method to a second sector · fixture input

**Consumes:** A28, BB status register — from [`tests/progressa.md`](../../progressa.md).
**Primary skill:** `ea-method-runner` · also runs: `bb-landscape-check`, `ea-institution-mapper`
**Produces:** A28 rev.2 — Second-sector map

## What the learner types

I have run, or plan to run, the EA method on [country X]'s [first sector]. I am considering [second sector]. Here are its main bodies [list them, one line each]. Produce a one-page map. (1) Classify each body (policy unit / regulatory agency / service-delivery authority / state registry / shared platform). (2) Name this sector's equivalent of the central duplicated record (the learner, the patient, the farmer, the beneficiary) and the flagship it is blocking. (3) Name the six deliverables for this sector. (4) List what this sector can REUSE from the first sector's work — the identity platform, the data-exchange backbone, the team, the framework, the governance — versus what is genuinely new. Output: a one-page map under those four headings.

## What the fixture supplies

Country: **Progressa** · Sector: **Education**. Substitute for every bracketed
placeholder above. The named input is A28, BB status register of `tests/progressa.md`; paste
those sections verbatim.

Where the play consumes an artefact from an earlier play (A1, A3, A22 …), run that
play on Progressa first — the chain is in
[`shared/workbook-chain.md`](../../../plugins/ea-plays/shared/workbook-chain.md).
