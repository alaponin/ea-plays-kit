# kit — the programs the skills run

This is the part of the method's delivery kit that the twelve skills reach. Run every command in
this folder, as `python3 tools/kit.py <verb>`. It needs Python 3.10 or later with `pyyaml` and
`jsonschema`.

The kit finds the standards at `../standards/` and the skills at `../skills/`, beside it in the
plugin; nothing is configured.

## The verbs this copy carries

| Verb | What it does | Used by |
|---|---|---|
| `slot <n>`, `slot --check` | Prints one row of the register of the twelve documents, or checks every row and handover against the standards | every skill |
| `spec new`, `spec map`, `spec route` | Scaffolds the specification tree; draws the order of the documents; prints how each handover is made | `sdd-specify` |
| `skills --check` | Compares every skill's pin with the standard it was written against | every skill |
| `conform <n> <document>` | Writes the claim of conformance, rule by rule, from the person's verdicts | every skill |
| `stale <n> <document>` | Lists what a change to one document makes stale | every skill |
| `screens walk <record>` | Produces the clickable walk-through from a screen record | `use-case-screens` |
| `new`, `validate`, `compile` | Starts, validates and admits the application model | `application-model` |
| `gen`, `deploy`, `seed`, `test` | Generates the application from the model and deploys it to a Joget DX installation (`GETTING-STARTED.md`, `DEPLOY.md`) | module 5 of the course |

The other verbs the facade lists in its help (`kit.py --help`) belong to the full delivery kit and
are not carried in this copy; they report that their program is missing.
