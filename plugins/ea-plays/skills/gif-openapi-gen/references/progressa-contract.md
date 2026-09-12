<!-- fixture: Progressa (fictional) · canonical: tests/progressa.md · keep consistent with it -->
# The Progressa identity service — contract and wiring

The worked example of plays 4.5 and 4.7 on Progressa, as the KP2 build pack publishes it.
The country facts come from `tests/progressa.md` and `tests/kp2/progressa-supplement.md`;
the identifiers are the frozen ones of the build pack. Progressa is fictional; the
exchange is the target state that the National Learner Registry programme delivers — in
the baseline the Progressa Learner Registry (PLR) is planned and not started.

## B24 — the contract (4.5)

Service brief: *return a person's identity, purpose-limited to credential issuance, given
a NIN.* Provider: the Progressa National ID Authority (PNIA). Fields from the person
entity of the semantic map; the six fields are the release set the purpose needs, and no
more.

```yaml
openapi: 3.0.3
info:
  title: Progressa National ID Authority — identity API
  version: "1.0"
  description: Purpose-limited person lookup for credential issuance. Returns only the fields the credential purpose needs.
servers:
  - url: http://app-pnia:8000/v1        # [confirm: set per the actual environment]
paths:
  /persons/{nin}:
    get:
      operationId: getPerson
      summary: Fetch a person's identity by NIN
      parameters:
        - name: nin
          in: path
          required: true
          schema: {type: string, pattern: '^[0-9]{11}$'}   # [confirm: NIN format]
      responses:
        "200":
          description: The person record (purpose-limited fields only)
          content:
            application/json:
              schema:
                type: object
                required: [nin, given_name, family_name, date_of_birth, sex, region]
                properties:
                  nin: {type: string}
                  given_name: {type: string}
                  family_name: {type: string}
                  date_of_birth: {type: string, format: date}
                  sex: {type: string, enum: [F, M]}
                  region: {type: string}
        "404":
          description: No person with this NIN
```

The `[confirm]` list for a real country: `servers.url`; the NIN pattern; each of the six
field names and types against the register's real interface; the `sex` enumeration.

## B26 — the service description and wiring (4.7)

| Item | Value |
| --- | --- |
| Instance · class | `PROGRESSA` · `GOV` |
| Provider subsystem | `PROGRESSA/GOV/PNIA/IDENTITY` |
| Service | `PROGRESSA/GOV/PNIA/IDENTITY/identity-api`, version 1.0, one operation `GET /persons/{nin}` |
| Forwarding target | `servers.url` of the contract |
| Consumer permitted | `PROGRESSA/GOV/PNEA/EXAMS` — and no other |
| Basis | B5: PNEA pre-fills identity for the certificate application; lawful basis stated on the service (purpose-limited person lookup for credential issuance — illustrative wording in the fixture, not a real statute) |
| r1 path a consumer calls | `https://ss-pnea/r1/PROGRESSA/GOV/PNIA/IDENTITY/identity-api/persons/{nin}` with `X-Road-Client: PROGRESSA/GOV/PNEA/EXAMS` |
| Negative check | the same call with `X-Road-Client: PROGRESSA/GOV/PLR/ENROLMENT`, routed through PLR's own Security Server — PLR is on the bus and is a provider, and holds no grant on `identity-api` — is denied by the provider-side ACL with an X-Road access-denied fault |

The second service of the exchange, `PROGRESSA/GOV/PLR/ENROLMENT/enrolment-api` with
`GET /enrolments/{nin}`, follows the same shape from the enrolment entity (nin, school,
level, enrolment_year, status) and grants `PNEA:EXAMS` only.

## What a real country's run adds

The X-Road release and the OpenAPI version read on the day, cited; every identifier as
`[confirm]` until the registry confirms it; a lawful basis that cites a real article of the
decree.
