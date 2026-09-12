# X-Road sources

The Nordic Institute for Interoperability Solutions (NIIS) publishes X-Road and its
documentation at docs.x-road.global and on GitHub (nordic-institute/X-Road). Read the
guide at the release in use — the portfolio (B22) names it. A step from a 6.x guide can be
wrong on 7.x, and a 7.x step can be wrong on 8. Cite the document code and the section.

| Document | What it proves | Used by |
| --- | --- | --- |
| Central Server Installation Guide (IG-CS) | install; initialise the instance and the owner; the admin user | 5.5 |
| Central Server User Guide (UG-CS) | member classes; members and subsystems; certification, OCSP and timestamping services; the configuration anchor; management requests and their approval | 5.4, 5.5 |
| Security Server Installation Guide (IG-SS) | install; the initialisation with anchor, owner member and server code | 5.5 |
| Security Server User Guide (UG-SS) | keys and certificates; clients and subsystems; services from an OpenAPI 3 description; access rights; the message log | 5.4, 5.5, 5.6 |
| Security Server Sidecar guide | the containerised Security Server and its limits | 5.5 (demonstration) |
| Test CA notes (in the X-Road repository's development/ or ansible/ material) | a trust anchor for a demonstration only | 5.5 |
| X-Road Message Protocol for REST (PR-REST, r1) | the call shape, the `X-Road-Client` header, the fault responses — `Server.ServerProxy.AccessDenied` is the denial the negative check expects | 5.6 |
| X-Road Terms and Abbreviations | member, subsystem, service, client, global configuration | all |
| Release notes 7.3.0 (XRDDEV-1960) | the identifier character set and strict checking | 5.4 |
| Operational Monitoring and Environmental Monitoring protocols | what the bus logs about an exchange, and what it does not | 5.6, and `gif-bus-monitor` |

## Beside the guides

| Source | Tier | Use |
| --- | --- | --- |
| NIIS X-Road World Map and the published member ecosystems (Estonia, Finland, Iceland and others) | T2 | how a production ecosystem names hosts and codes; a comparator, never a template |
| Estonia — the X-tee regulation and the RIA operator pages | T1 | what a production operator publishes: onboarding, member obligations, the catalogue |
| Finland — the Suomi.fi Data Exchange Layer service description and its naming convention | T1 | host naming that encodes owner, role, environment and sequence |
| GovStack Information Mediation BB | T1 | what the federation realises |

## What no source can give you

The instance identifier, the member codes, the subsystem codes, the server codes and the
addresses of a real country. Those come from the country's Central Server registry and its
environment, and they are `[confirm]` until the operator confirms them.
