# The specifications to read

Read the specification, not a tutorial. Cite the version. Names of the publishing bodies
are here; find the current URL from the body's own site each time.

| Specification | Body | Governs | Pin |
| --- | --- | --- | --- |
| OpenAPI Specification 3.x | OpenAPI Initiative (Linux Foundation), spec.openapis.org | the structure of the contract: `openapi`, `info`, `servers`, `paths`, `components`, `securitySchemes` | the minor version B22 adopts (3.0.3 or 3.1.x); X-Road's OpenAPI 3 parser support is the constraint — check the NIIS documentation for the version it accepts |
| X-Road Message Protocol for REST (r1) | NIIS, docs.x-road.global | the path form `/r1/<instance>/<class>/<member>/<subsystem>/<service>/<path>`, the `X-Road-Client` header, error responses, the request id | the protocol version matching the X-Road release in B22 |
| X-Road Security Server user guide — REST services and OpenAPI 3 service descriptions | NIIS | how a Security Server parses an OpenAPI 3 description: `servers.url` as the forwarding target, one service per description, endpoint-level access rights | the X-Road release in B22 (7.x) |
| X-Road identifiers | NIIS release notes and terms | the permitted character set for member, subsystem and service codes (strict checking from 7.3.0) | 7.3.0 or later |
| OAuth 2.0 (RFC 6749), OAuth 2.1 draft, OpenID Connect Core 1.0 | IETF; OpenID Foundation | the security scheme at the application layer | as B22 adopts |
| GovStack Information Mediation Building Block | GovStack, govstack.gitbook.io | what the bus realises: a member joins the mediator once and reaches every declared exchange through it; the service registry and access control | the BB version B22 or the pattern register pins |
| GovStack Digital Registries Building Block | GovStack | a schema-driven registry read; a version per schema change; an audit entry per change — the pattern a lookup service takes | as pinned |

## What each governs, and what it does not

- **The OpenAPI contract** describes the provider's interface behind its Security Server.
  It does not describe the bus. The consumer never calls `servers.url`; it calls the r1
  path on its own Security Server.
- **The r1 protocol** describes how a call travels over the bus. It does not describe the
  payload; that is the contract's.
- **The security scheme** in the contract is the application-layer scheme between the
  Security Server and the provider system. Transport security between Security Servers
  is X-Road's mutual TLS and is not written in the contract. Say both, once.
- **Access rights** in X-Road are granted per service (and optionally per endpoint) to a
  subsystem. The contract's `securitySchemes` do not grant access; the ACL does.

## Rejected

A vendor's API gateway documentation as the source for X-Road behaviour; a blog post on
"X-Road in 10 minutes"; an OpenAPI example repository as the source for a field name.
