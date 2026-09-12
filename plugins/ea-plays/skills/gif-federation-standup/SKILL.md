---
name: gif-federation-standup
description: >-
  Stand up and prove an X-Road federation for a Government Interoperability Framework — the
  three KP2 Module 5 plays that turn configuration into a running slice: the member
  registration, with its subsystem, service codes, access-control list and the onboarding
  checklist in the method's order (5.4, B31); the federation stand-up run book for the
  Central Server, the Test CA and one Security Server per member, each step marked where it
  differs from production (5.5, B32); and the once-only acceptance script in given / when /
  then with the negative check (5.6, B33). Use when someone says "register a member on
  X-Road", "subsystem and ACL", "onboarding checklist", "stand up the federation", "run book
  for the Central Server", "Security Server deployment steps", "Test CA", "acceptance
  check", "once-only proof", "given when then for the exchange", "prove the exchange runs",
  "Linkup", "build pack", or names KP2 play 5.4, 5.5 or 5.6. It never invents an identifier
  or an address.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
---

## What this skill does

This skill makes the three artefacts that stand a federation up and prove it. Play 5.4
makes **B31, the X-Road member registration**: the subsystem, its service codes, the
access-control list, and the onboarding checklist that ends in the conformance test. Play
5.5 makes **B32, the federation stand-up run book**: the ordered, reproducible steps for
the Central Server, the Test CA and each Security Server, with a *differs in production*
note per step. Play 5.6 makes **B33, the once-only acceptance script**: given / when /
then, the negative check, and each assertion mapped to the layer it exercises.

The bare plays defend against invented identifiers and addresses with `[confirm]`. This
skill adds the **published procedure**: it reads the NIIS X-Road installation and
administration guides at the release the portfolio adopts, so that each step of the run
book is the guide's step, cited, and not a recollection. It also carries the shape of the
KP2 build pack's own acceptance check, so that a learner's script proves what the
pack proves: cross-server routing, the right record, asked once, denied when not granted,
and field conformance.

**This skill writes text.** It does not deploy anything and it does not run a container.
The run book is executed by a person, in a sandbox, before it is trusted.

## Inputs

| Play | Makes | Needs |
| --- | --- | --- |
| 5.4 | B31 Member registration | B26 the service description and wiring (the provider's services and ACL); B29 the Member Requirements checklist; **the member's details** — organisation, member class, any known codes; **the access policy** |
| 5.5 | B32 Stand-up run book | B31 (the members to register); **the topology** — Central Server, the Security Servers, the Test CA; **the X-Road release** |
| 5.6 | B33 Acceptance script | B32; B27 the data-protection envelope (which fields the exchange may carry); **the scenario** — the consumer, the providers, the citizen-provided field |

Also useful: B22, the standards portfolio, where the X-Road release is pinned — ask the
learner for the release if they do not have B22.

Ask at most three questions, together: the X-Road release; whether the run is a
single-host demonstration (containers, a Test CA) or a production install; whether the
member codes come from a registry the learner can name. Record the answers in the
artefact.

## Procedure

1. **Read the guides at the release in use** (T1, `references/xroad-sources.md`): the
   Central Server installation and user guides, the Security Server installation and user
   guides, the Test CA notes, the REST message protocol. Cite the section for each step you
   write. If a guide cannot be fetched, mark those steps ⚠ and say so.

2. **For 5.4, write the registration from B26 — never from scratch.** The subsystem
   `<INSTANCE>/<CLASS>/<MEMBER>/<SUBSYSTEM>` (one per system), the service codes from
   B26, the ACL rows from B26 with their basis. Every member, subsystem and service code
   is `[confirm: verify against the live X-Road registry]`. Then the onboarding checklist in
   the method's order — `references/onboarding-path.md` — with the conformance test
   named by approach (self-assessment, third-party, test suite) and the approval per the
   governance RACI (B16) beside each step.

3. **For 5.5, order the steps as the guides order them.** Central Server: install,
   initialise the instance and the owner member, add the member class, register the
   certification service, OCSP responder and timestamping service, generate the
   configuration anchor. Test CA: bring up, register as the trust anchor. Each Security
   Server: install, import the anchor, initialise with owner member and server code,
   generate the authentication key and the signing key, submit the certificate requests to
   the CA, import the certificates, register the authentication certificate with the
   Central Server, approve the request, add the subsystem as a client, register it,
   approve. Verification: all members and subsystems present in the Central Server
   registry; a test call resolves cross-server. Mark each step **demonstration-only** where
   it is: the Test CA as trust anchor, fixed admin credentials, a single host, explicit
   approval over the admin API. Every address and identifier is `[confirm: set per the
   actual environment]`.

4. **For 5.6, write the five assertions.** The build pack's acceptance check proves five
   things and each is mapped to a layer (`references/acceptance-shape.md`): the happy path
   returns cross-server (technical); the returned fields equal the seeded record for that
   citizen — the *right* person, not merely data (semantic); the assembled form holds the
   one citizen-provided field plus only pre-filled bus fields, disjoint and covering the
   form (organisational + legal); a member on the bus with no grant is denied by the
   provider-side ACL, not by a transport failure (organisational); each response carries
   exactly the fields its contract declares — nothing withheld is returned (legal, purpose
   limitation). Add the error-observability check: a citizen present in one register and
   absent from the other returns a clean 404, not silence.

5. **Keep the seams visible.** Where a step depends on a production choice the
   demonstration does not make — a real CA, a member's own Security Server, a pairwise
   pseudonymous identifier instead of the raw national number, message-log retention —
   say so in the *differs in production* note and point to 5.7 (B34).

6. **Run `cite-or-discard`** on the guide citations before you give the output.

## Output contract

Write the provenance header first (`references/provenance-header.md`). Then:

For **5.4 (B31)**: the subsystem registration block; the ACL table `| Service | Consumer subsystem | Basis | [confirm] |`; the onboarding checklist as an ordered list, each step with its approval and evidence; the `[confirm]` list.

For **5.5 (B32)**: the run book as an ordered list under the headings Central Server · Test CA · Security Server (one per member) · Verification, each step with its guide citation and a *differs in production* note; the topology table; the `[confirm]` list.

For **5.6 (B33)**: GIVEN · WHEN (the exact calls, with headers and r1 paths) · THEN (the five assertions, each with the layer it proves) · the negative check · the observability check; the `[confirm]` list.

Then the **Inputs supplied by the learner** block and the safeguard. Text in the chat,
never a file or a script to download; commands appear as fenced blocks in the text. Posts,
not names. Write no analysis before the header. See `references/output-contract.md`.

## Safeguard handed back

**A run book is reproducible only once it has been run. An acceptance check that proves the
happy path is half a check. And every X-Road identifier is the single highest-stakes
`[confirm]` in the framework — a wrong code can route one citizen's data to a service
that asked about another.**

- Execute the run book end to end in the sandbox and confirm every member registers,
  before it becomes the build pack's run book.
- Confirm every identifier against the live registry before deployment. Then confirm it
  again after a rebuild.
- Run the negative check and the field-conformance check, not only the happy path.
  Confirm the data returned is the right citizen's.
- Nothing here is a production hardening. The *differs in production* notes are the
  input to 5.7; the security review is independent and is done, not listed.

## References

- `references/xroad-sources.md` — the NIIS guides and protocols by release, and what each
  proves.
- `references/onboarding-path.md` — the member onboarding path in order, with the
  approval and the evidence per step, and the conformance-test approaches.
- `references/acceptance-shape.md` — the five layer-mapped assertions, the negative and
  observability checks, and the artefact a passing run produces.

### Fixture material

- `references/progressa-federation.md` — the Progressa federation: topology, frozen
  identifiers, the once-only scenario and its acceptance, as the KP2 build pack stands it
  up. Progressa is the fictional demonstration country; `tests/progressa.md` and
  `tests/kp2/progressa-supplement.md` in the kit repo are canonical.

### The shared contract

- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` ·
  `references/workbook-chain-kp2.md`.
