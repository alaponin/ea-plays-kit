---
name: gif-openapi-gen
description: >-
  Generate the service contract of a Government Interoperability Framework exchange and the
  X-Road wiring that publishes it: an OpenAPI 3.x contract whose paths, parameters, response
  schema, error responses and security scheme are taken from the semantic map and the
  standards portfolio (KP2 play 4.5, B24); and the X-Road service description derived from
  that contract — service code, version, the operations exposed, the provider's subsystem
  identity, the access-control entries naming which consumer subsystems may call it, and a
  test-call plan over the bus (4.7, B26). Use when someone says "OpenAPI contract",
  "generate the API spec for this service", "service contract for the bus", "X-Road service
  description", "REST service description X-Road", "wiring checklist", "access-control list
  for this service", "which subsystems may call", "test call over the bus", "r1 path",
  "Information Mediation building block", "gif-openapi-gen", or names KP2 play 4.5 or 4.7.
  It never invents a member, subsystem or service code.
allowed-tools: WebSearch, WebFetch, Read
disallowed-tools: Write, Edit, NotebookEdit
license: CC-BY-4.0
metadata:
  provider: FiscalAdmin OÜ
---

## What this skill does

This skill makes the contract of one service and the wiring that puts it on the bus. Play
4.5 makes **B24, the OpenAPI service contract**. Play 4.7 makes **B26, the X-Road service
description and wiring checklist**. Together they are the technical configuration of one
exchange — the thing a provider publishes and a consumer calls.

The bare play defends against the two failures — a field the provider does not expose, and
an invented identifier — with `[confirm]` placeholders. This skill adds the specification:
it **reads the OpenAPI 3.x specification and the X-Road REST message protocol as
published**, checks the contract's structure against them, cites the version, and takes
every field from the semantic map (B23) rather than from imagination. It keeps every
identifier as `[confirm]`, because no public source can say what a live X-Road registry
holds.

## Inputs

| Play | Makes | Needs |
| --- | --- | --- |
| 4.5 | B24 OpenAPI service contract | B23 the semantic map (the fields, types and identifier); B22 the standards portfolio (the OpenAPI, OAuth/OIDC and X-Road versions adopted); **the service brief** — what the service does, in one sentence |
| 4.7 | B26 X-Road service description and wiring checklist | B24; B6 the stakeholder tier map (who provides, who consumes); **the access policy** — which consumers may call which service; the member and subsystem codes, if the learner knows them |

Ask at most three questions, together: the service brief if it is missing; the provider
and consumer bodies if B6 does not settle them; whether the country's X-Road instance,
member class and any codes are known, and from which registry. Record the answers in the
artefact.

## Procedure

1. **Read the specifications** (T1). The OpenAPI specification at the version B22 adopts;
   the X-Road REST message protocol (r1) from the NIIS documentation; the X-Road
   service-description guidance for OpenAPI 3 services. Record the URL and the access
   date of each. `references/spec-anchors.md` names them. If the fetch fails, say so and
   mark the structural claims ⚠.

2. **Build the contract from the map, not around it.** Each response field is a B23 field
   with B23's type; the identifier is B23's identifier; the code lists are B23's. A field
   that is not in B23 does not enter the contract — say so and route it to 4.4. Release
   only the fields the purpose needs (B27, the decree): the contract is where purpose
   limitation becomes a `required` list.

3. **Write the six parts the play asks for.** The path(s) and operation(s); the request
   parameters, with the identifier's format as a pattern; the response schema with field
   names and types from B23; the error responses — at least 404 for *no record*, 403 for
   *not permitted*, 400 for *malformed identifier*; the security scheme (OAuth 2.x / OIDC
   as B22 adopts, and a note that on X-Road the transport security is the Security
   Server's mutual TLS — the two are not the same layer); `info.version` and
   `servers.url` as the forwarding target `[confirm]`.

4. **Mark every path, field name and type `[confirm: verify against what the provider
   system actually exposes]`.** Documentation drifts from the interface. The list of
   `[confirm]`s is part of the artefact.

5. **For 4.7, derive the service description from the contract.** The service code (from
   the contract's title or brief, in the X-Road identifier character set —
   `references/xroad-wiring.md`), the version, the operations exposed; the provider's
   subsystem identity `<INSTANCE>/<CLASS>/<MEMBER>/<SUBSYSTEM>`; the r1 path a consumer
   calls; the access-control entries — one per consumer subsystem per service, and *no
   wildcard*; the test-call plan — the exact request with the `X-Road-Client` header and
   the expected response, plus the negative call from a subsystem that holds no grant,
   expected to be denied by the provider-side ACL. Say where this realises the GovStack
   Information Mediation building block.

6. **Run `cite-or-discard`** on the specification citations. The contract's YAML is not a
   claim and is not verified; its `[confirm]`s are.

## Output contract

Write the provenance header first (`references/provenance-header.md`). Then:

For **4.5 (B24)**: the OpenAPI document as a fenced ```yaml block **in the chat** — text,
not a file; the `[confirm]` list; the X-Road service-description notes (which parts of the
contract X-Road reads: `servers.url` as the forwarding target, the paths as the operations,
the version).

For **4.7 (B26)**: the service-description table `| Service code | Version | Provider subsystem | Operations | Forwarding target | [confirm] |`; the access-control table `| Service | Consumer subsystem permitted | Basis (B5 exchange, B27) | [confirm] |`; the test-call plan — the positive call, the expected response, the negative call, the expected denial; the wiring checklist in order; the Information Mediation note.

Then the **Inputs supplied by the learner** block and the safeguard. Posts, not names.
Write no analysis before the header. See `references/output-contract.md`.

## Safeguard handed back

**A contract that names a field the provider does not expose fails at the first real
call. An identifier that is wrong does not fail — it silently routes nowhere or to the
wrong place.**

- Confirm every path and field against the provider system's real interface — call it,
  do not read its documentation — before the contract is published or the service
  description is derived.
- Confirm every member, subsystem and service code against the live X-Road registry before
  deployment. That is the single highest-stakes `[confirm]` in the framework.
- The access-control list is a legal instrument's technical shadow: each entry needs a
  catalogue exchange (B5) and a lawful basis (B27) behind it. An entry with neither is
  removed, not kept for convenience.
- The negative test is not optional. Run it; a bus where every member can call everything
  has no organisational layer.

## References

- `references/spec-anchors.md` — the OpenAPI, OAuth/OIDC, X-Road REST protocol and
  GovStack Information Mediation sources, what each governs, and the version to pin.
- `references/xroad-wiring.md` — the identifier shape, the character set, the r1 path
  form, the ACL rules, and the wiring checklist in order.

### Fixture material

- `references/progressa-contract.md` — the PNIA identity service contract and its wiring
  from the KP2 build pack, the worked example of 4.5 and 4.7 on Progressa. Progressa is the
  fictional demonstration country; `tests/progressa.md` and
  `tests/kp2/progressa-supplement.md` in the kit repo are canonical.

### The shared contract

- `references/source-tiers.md` · `references/provenance-header.md` ·
  `references/output-contract.md` · `references/workbook-chain.md` ·
  `references/workbook-chain-kp2.md`.
