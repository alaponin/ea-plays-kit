# The acceptance check — its shape

One once-only exchange proves all four EIF layers in one call. The script has a GIVEN, a
WHEN, a THEN of five assertions, a negative check and an observability check. Each
assertion names the layer it proves. A script that proves only the happy path is half a
check.

## GIVEN

The federation deployed (B32 run to the end); the members registered (B31); the service
published from its contract (B24, B26); the demonstration data seeded, with one citizen
record that exists in every provider register the exchange reads — that record's
identifier is the test key.

## WHEN

The consumer's system makes each provider call **through the consumer's own Security
Server**, on the r1 path, with the `X-Road-Client` header naming the consumer subsystem.
Write the exact calls. A call made straight to a provider's application is not a test of
the bus.

## THEN — the five assertions

| # | Assertion | Layer | What it rules out |
| --- | --- | --- | --- |
| 1 | Happy path — each call returns 200 **cross-server** (consumer SS → provider SS), not through any direct connection | technical | a demonstration that bypasses the bus |
| 2 | Right citizen — every returned field equals the seeded record for that identifier, field by field | semantic | "data returned" that is somebody else's |
| 3 | Asked once — the assembled form holds the citizen-provided field(s) plus only pre-filled bus fields; the two sets are disjoint and together cover the form; no field a register holds is re-entered | organisational + legal | a form that quietly asks again |
| 4 | Negative — a member that is on the bus, is a provider in its own right, and holds no grant on this service is **denied by the provider-side ACL** with the X-Road access-denied fault — not a transport error, not the consumer SS rejecting a client it does not host | organisational | "on the bus means granted everything" |
| 5 | Field conformance — each response carries exactly the fields its own contract declares: nothing the contract withholds is returned, nothing it requires is missing | legal (purpose limitation) | a register that returns a field the contract withholds — the field purpose limitation exists to keep off the wire, which assertion 2 cannot see |

## The observability check

A citizen seeded in one provider register and deliberately absent from another returns
the present record and a **clean 404** from the absent one. Errors are observable, not
silent.

## The artefact a passing run produces

The assembled application for the test citizen, with per-field provenance: the one
citizen-provided field, and every bus-pre-filled field with the service it came from. It is
the tangible *asked-once* object — the thing a minister can be shown — and the seam a
later form (KP4) replaces. Optional further evidence: the exchange visible in the provider
Security Server's message log.

## Mapping to the run

Number the assertions in the script as the run numbers them, so that a failing line names
the assertion. Record the run's date, the X-Road release, and whether the run was against a
cold redeploy (the reproducibility proof) or a warm stack.
