# What a bus log contains — and what is cargo

## The reference

The X-Road Operational Monitoring Protocol and the operational monitoring daemon
(NIIS, docs.x-road.global — the PR-OPMON and ARC-OPMOND documents) define the record a
Security Server keeps per message. Read the current version and cite it. The record is
about the *exchange*: who called what, when, with what outcome and size. It carries no
payload.

## Permitted fields — traffic

| Field (as the protocol names it, approximately) | What it is | Personal data? |
| --- | --- | --- |
| monitoringDataTs, requestInTs, requestOutTs, responseInTs, responseOutTs | timestamps | no |
| securityServerInternalIp, securityServerType | the server, client or producer side | no |
| clientXRoadInstance, clientMemberClass, clientMemberCode, clientSubsystemCode | the calling subsystem | no — an organisation |
| serviceXRoadInstance, serviceMemberClass, serviceMemberCode, serviceSubsystemCode, serviceCode, serviceVersion | the called service | no |
| restMethod, restPath (with path parameters, in some versions) | the operation | **path parameters can be a citizen's identifier** — see below |
| messageId, xRequestId | correlation ids | no |
| succeeded, faultCode, faultString | the outcome | no — unless the fault string echoes a payload |
| requestSize, responseSize, requestAttachmentCount, responseAttachmentCount | sizes | no |
| representedParty* | the party on whose behalf a call is made | **can be a person** — treat as cargo |

## Cargo — stop if present

- A national identification number, a name, a date of birth, an address, a phone number,
  an e-mail — in any field, including a path such as `/persons/{nin}` where the `{nin}` is a
  real value. A path template is traffic; a path with a value is cargo.
- A request or response body, or any fragment of one.
- A query string carrying a citizen's attribute.
- A `representedParty` or a user id that identifies a person.
- A fault string that quotes the payload.

When a field is cargo: name the field, not the value; stop; write the data-protection
section; produce no summary. Do not clean the logs yourself and continue — the learner
strips them at source and re-runs the play.

## What a log cannot tell you

- Whether the data returned was the right citizen's (B33 assertion 2 tests that; a log
  records that a call succeeded).
- Whether the exchange was lawful (the ACL and the decree say that; a log records that the
  ACL allowed it).
- What happened inside the provider system after the call.
- Anything about a period the logs do not cover, or a Security Server whose logs were not
  pasted.
