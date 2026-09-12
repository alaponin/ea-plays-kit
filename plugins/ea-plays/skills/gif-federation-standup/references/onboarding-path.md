# The member onboarding path

The order the method gives. A registration (B31) closes with this checklist; each step has
an approval from the governance RACI (B16) and a piece of evidence. A self-assessed *met*
is a claim, not proof — the evidence column is what the Operating Authority reads.

| # | Step | Approval (B16 — post, not name) | Evidence | `[confirm]` |
| --- | --- | --- | --- | --- |
| 0 | Prerequisite: the ecosystem-level conventions are published — identifier character set, member-code scheme, subsystem-code scheme, host naming | the Operating Authority, once, before member #1 | the published conventions page | — |
| 1 | Application and signed obligations — the member agreement (B17) signed by the post that can bind the agency | the Steering Committee or the Operating Authority as the RACI says | the signed agreement | which post can bind |
| 2 | Member Requirements met (B29) — the checklist with its evidence column filled, spot-checked on the high-risk rows (clean data, lawful basis) | the Operating Authority | the completed B29 | — |
| 3 | Member and subsystem codes assigned per the conventions; entered in the Central Server registry | the Operating Authority | the registry entry | every code |
| 4 | Certificate issuance — authentication certificate for the Security Server, signing certificate for the member, from the ecosystem's CA | the CA's registration authority | the certificates' serials | the CA in use (a Test CA is demonstration-only) |
| 5 | Security Server deployment — the member's own, or hosted on an existing server on a single-host demonstration | the member's technical contact; the Operating Authority for a hosted server | the server registered and visible in the Central Server | server code, address |
| 6 | **Conformance test against the standards portfolio (B22)** — state the approach: self-assessment, third-party, or a test suite | the Technical Working Group named in B18 | the test record | the approach the governance chose |
| 7 | First service registration — the service from its OpenAPI description (B24), the ACL from B26 | the Operating Authority | the service in the catalogue | service code, ACL subjects |
| 8 | Production go-live — the acceptance script (B33) green, both go-live approvals recorded | the two posts the RACI names for go-live | the acceptance record; the approvals | — |

## The conformance-test approaches

| Approach | What it proves | When it is enough |
| --- | --- | --- |
| self-assessment | the member says it conforms | a pilot member in a demonstration; never for production |
| third-party | an assessor the Operating Authority names checked it | a production member where no test suite exists |
| test suite | the member's service passed the suite the Technical Working Group maintains against B22 | the target; the field-conformance check of B33 is one such test |

## The conventions a registration assumes

Published once, before the first member; enforced at registration. A convention
retrofitted after fifty members is not retrofitted at all, because certificates, DNS,
firewall rules and monitoring all key off the names.

- **Identifier character set** — X-Road's own allowlist, from 7.3.0: `a-zA-Z0-9'()+,-.=?`.
- **Member code** — typically the national organisation-registry code; stable across
  renaming and merger; reused, not assigned.
- **Subsystem code** — one per system, not per service.
- **Host naming** — encodes owner, role, environment and sequence, so that a name alone
  says whose, what for, which environment, which one.
