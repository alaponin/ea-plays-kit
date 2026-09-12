# X-Road wiring — identifiers, paths, access rights, and the checklist

## The identifier shape

| Identifier | Form | Example shape | Rule |
| --- | --- | --- | --- |
| instance | one code per federation | `<INSTANCE>` | set once by the owner; never invented by a member |
| member | `<INSTANCE>/<CLASS>/<MEMBER>` | `INSTANCE/GOV/AGENCY` | the member code is typically the national organisation-registry code, stable across renaming — reused, not assigned |
| subsystem | `<INSTANCE>/<CLASS>/<MEMBER>/<SUBSYSTEM>` | `INSTANCE/GOV/AGENCY/SYSTEM` | **one per system, not per service** — a system with five services is one subsystem with five service codes |
| service | `<INSTANCE>/<CLASS>/<MEMBER>/<SUBSYSTEM>/<SERVICE>[/<VERSION>]` | `.../SYSTEM/identity-api` | the service code names the API, not the operation |
| `X-Road-Client` header | the calling subsystem | `INSTANCE/GOV/CONSUMER/SYSTEM` | the consumer's subsystem, never its member alone |

Character set: from X-Road 7.3.0, identifiers permit only `a-zA-Z0-9'()+,-.=?`, and
strict checking is on by default for a fresh installation. A code outside this set fails
registration. Write the set in the checklist; do not assume a hyphen or an underscore is
safe — the underscore is not in the set.

**Every value above is `[confirm: verify against the live X-Road registry]` for a real
country.** The skill proposes a shape; the registry holds the truth.

## The r1 path

```
https://<consumer security server>/r1/<INSTANCE>/<CLASS>/<PROVIDER>/<SUBSYSTEM>/<SERVICE>/<path from the contract>
```

with the header `X-Road-Client: <INSTANCE>/<CLASS>/<CONSUMER>/<SUBSYSTEM>`. The consumer
calls **its own** Security Server; the Security Server routes to the provider's. A test call
made directly to the provider's application proves nothing about the bus.

## Access rights

- Grant per service to a consumer **subsystem**. Never to a member, never to a group unless
  the governance (B16) has decided that global groups exist, and never with a wildcard.
- Each entry needs two things behind it: a row in the Use-Case Catalogue (B5) and a lawful
  basis (B27 or the decree article). Write both in the ACL table's *Basis* column.
- The **negative check** is part of the wiring, not a later test: name a subsystem that is
  on the bus, is a provider in its own right, and holds no grant on this service — its call
  must be denied by the provider-side ACL with an X-Road access-denied fault, not by a
  transport error. *On the bus does not mean granted this service.*

## The service description X-Road reads

From an OpenAPI 3 document a Security Server takes: `servers.url` as the forwarding target
to the provider system (`[confirm: set per the actual environment]`); the paths as the
operations for endpoint-level access rights; `info.version` as the service version. It
does not read `securitySchemes` as a grant. One service code per OpenAPI document.

## The wiring checklist, in order

1. The provider's member and subsystem exist in the Central Server registry `[confirm]`.
2. The provider's Security Server holds a registered authentication certificate and a
   signing key for the member `[confirm]`.
3. The subsystem is registered as a client of that Security Server.
4. The OpenAPI document is reachable from the Security Server at the URL the description
   names, and parses at the X-Road release in use.
5. The service is added from the description, enabled, and the forwarding target answers
   from the Security Server's network.
6. Access rights are granted per the ACL table — each consumer subsystem, per service.
7. The consumer's subsystem exists and is registered on its own Security Server `[confirm]`.
8. The positive test call from the consumer's Security Server returns the contract's
   response with exactly the declared fields.
9. The negative test call is denied by the provider-side ACL.
10. The service is entered in the service catalogue (B19's register) with its contract,
    its semantic entity, its lawful basis and its ACL subjects.

Steps 1, 2 and 7 are the registrations that play 5.4 (B31) produces; this checklist assumes
them and says so.
