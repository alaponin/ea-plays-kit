#!/usr/bin/env python3
"""gate_report.py — the computed custody artefact (CH-01 WP-A, ADR-069).

Assemble / check / sign design/gate-report.yaml and resolve the custody verdict that
kit gen / build_app / kit deploy key on. NEVER hand-authored: each constituent block is
written from a gate's actual exit, keyed by the sha256 of every input that gate read;
`check` recomputes those shas against the working tree.

  gate_report.py assemble <app.yaml>          run constituent gates -> design/gate-report.yaml
  gate_report.py check    <app.yaml>          recompute freshness; print verdict; 0 GREEN else 1
  gate_report.py sign     <app.yaml> --as ID  record {signer,date} (signer-on-record v1)
  gate_report.py resolve  <app.yaml>          print GATED:<sha> | UNGATED  (what gen/deploy stamp)

Custody:  GREEN + fresh + signed -> GATED:<report-sha>   else  UNGATED.
Signer-on-record v1 (owner ruling 2026-07-18): signer in authors is WARNED, not blocked,
until a second signing identity exists (ADR-074; signers registry T1).
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import pathlib
import subprocess
import sys

try:
    import yaml
except ImportError:
    sys.exit("gate_report.py needs pyyaml (pip install pyyaml)")

from observation import NOTHING as OBSERVED_NOTHING

HERE = pathlib.Path(__file__).resolve().parent
PY = sys.executable
KIT = HERE / "kit.py"

# Constituents a `custody: required` app needs green. ux_lint/diff_ux join as WP-B/WP-I
# land; until a verb exists it records absent -> RED in required mode (correct: a required
# app is not fully gated until those checks exist). stamp-mode apps never require any.
# ADR-093: the two BEHAVIOURAL legs join the required set, and that is the point of the ADR.
# Before it, the required set was six presence/shape/contract checks and the one constituent that
# observes a running system could not block anything. An app whose every artefact is well-formed
# and which no person can use passed — for fifteen deployments. Both legs carry `applicable`, so
# an app declaring no scenarios and an app with no build are not punished for what they do not have.
# 2026-08-06: `totality` joins the required set, and it is the most consequential addition
# since the behavioural legs. Every other structural check grades the projector against ITSELF
# — `drift` re-projects and diffs against disk, so a projector that DROPS a declared field drops
# it on both sides, the two agree, and it reports IN_SYNC. It did exactly that on 2026-08-05
# with four declared fields missing, one of which was the column a cross-record guard counted
# against: the guard threw, FAILED OPEN, and a deregistration went through with no liability
# safeguard. `totality` is the only check that is an INDEPENDENT second encoding of the
# projection contract — it asks whether what the MODEL declared is present in what was produced.
# Its first runs blocked all three apps (32, 4 and 24 findings in the three reference apps).
# 2026-08-13: `requirements_coverage` joins the required set (verification-seam ruling).
# It is the only constituent whose denominator is the CUSTOMER'S document rather than
# something the design authored, so it is the only one that can see a requirement the
# customer paid for that no part of the build claims. It was written in July, has never
# been a gate constituent, and its `claimed` verdict meant "the id string appeared in a
# design file" — a requirement named once in a comment counted as covered. Both halves are
# fixed together, because either alone would be worse: a strict verb nobody runs, or a
# lax verb the gate now trusts.
REQUIRED_SET = ("validate", "spec_lint", "diff_reference", "drift", "suite", "ux_lint",
                "loss_report", "totality", "requirements_coverage")
BEHAVIOURAL = ("acceptance", "ui_probe")

VERB_CLI = {"validate": "validate", "spec_lint": "spec-lint", "loss_report": "loss-check",
            "diff_reference": "diff-reference",
            "requirements_coverage": "requirements",
            "ui_probe": "ui-probe",
            "drift": "drift", "suite": "suite", "ux_lint": "ux-lint", "diff_ux": "diff-ux",
            "totality": "totality",
            "lint_decisions": "lint-decisions", "citation_check": "citation-check"}

# Honest-scope labels (review §F.3): what each gate's verdict actually PROVES — so "green" can
# never again read as "behaves". presence = a thing exists · shape = it is well-formed · contract
# = it matches a declared interface · coverage = every decision is answered · behaviour = the
# running system was observed to do it. Only `acceptance` is behaviour.
SCOPE = {"validate": "shape+contract", "spec_lint": "coverage", "loss_report": "coverage",
         "diff_reference": "contract",
         # fidelity = every requirement the CUSTOMER'S document carries is realized by an
         # artefact or signed off. The only label in this table whose denominator is not
         # something the design authored.
         "requirements_coverage": "fidelity",
         "drift": "shape", "suite": "presence", "ux_lint": "presence+shape",
         "diff_ux": "contract", "acceptance": "behaviour", "ui_probe": "behaviour",
         # transmission = what the model DECLARED was found in what was produced, checked by a
         # second encoding rather than by re-running the producer. The only label of its kind.
         "totality": "transmission",
         "lint_decisions": "shape", "citation_check": "coverage"}


def _sha(path: pathlib.Path) -> str:
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()


def _now() -> str:
    return _dt.datetime.now().isoformat(timespec="seconds")


def _load(path: pathlib.Path) -> dict:
    p = pathlib.Path(path)
    return (yaml.safe_load(p.read_text(encoding="utf-8")) or {}) if p.is_file() else {}


def app_paths(model: pathlib.Path) -> dict:
    """Convention-resolved companion paths (some may be absent — absence is a finding)."""
    m = pathlib.Path(model).resolve()
    d = m.parent
    design = d / "design"
    realisms = sorted(d.glob("*.realism.yaml")) + sorted(design.glob("*.realism.yaml"))
    # The inventory is the foundation ledger PLUS every slice's derived ledger. Reading only the
    # first was the gate measuring coverage against a fraction of what the app had decided.
    derived = sorted((design / "derive").glob("*/decisions.yaml"))
    return {"model": m, "app_dir": d, "design": design,
            "decisions": design / "decisions.yaml", "derived": derived,
            "subjects": design / "subjects.yaml",
            "realism": realisms[0] if realisms else None, "generated": d / "generated", "build": d / "build",
            "kit_yaml": d / ".kit.yaml", "report": design / "gate-report.yaml",
            "realization": design / "realization.yaml",
            "requirements": design / "requirements.yaml",
            "loss_report": design / "loss-report.yaml"}


def _existing(paths) -> dict:
    return {str(p): _sha(p) for p in paths if p and pathlib.Path(p).is_file()}


def _constituent_plan(P: dict) -> dict:
    """verb -> (kit argv | None-if-input-missing, [input paths for the freshness manifest])."""
    m = P["model"]
    return {
        "validate":       ([str(m)], [m]),
        "spec_lint":      (None if not P["decisions"].is_file()
                           else [str(P["decisions"]), *[str(p) for p in P["derived"]],
                                 "--subjects", str(P["subjects"])],
                           [P["decisions"], *P["derived"], P["subjects"]]),
        "diff_reference": (None if not P["realism"]
                           else [str(m), "--realism", str(P["realism"])],
                           [m, P["realism"]] if P["realism"] else [m]),
        "drift":          ([str(m), str(P["generated"])], [m]),
        # Runs unconditionally, like drift. An app that generated nothing gets totality's own
        # refusal (exit 3) rather than a silent skip — "nothing produced" is not "nothing wrong".
        "totality":       ([str(m), "--generated", str(P["generated"]),
                            "--build", str(P["build"])], [m]),
        "suite":          ([str(m)], [m]),
        "ux_lint":        (None if not P["build"].is_dir()
                           else [str(m), "--build", str(P["build"])],
                           sorted(P["build"].rglob("*.json")) if P["build"].is_dir() else []),
        # UB-14b: two schema slots that gate_report.py declared but never populated, so a green
        # report could not carry them and their absence read as "not required". Both have had a
        # working kit verb all along; only the wiring was missing. They follow the same
        # input-conditional shape as spec_lint / diff_reference — no input, no constituent.
        "lint_decisions": (None if not P["decisions"].is_file() else [str(P["decisions"])],
                           [P["decisions"]]),
        # schema-0.2 §3.6. Ten constituents passed honestly while the file recording what the
        # model CANNOT enforce sat unread beside them. Input-conditional like the others: an app
        # that lost nothing has no report, and absence of loss is not a finding.
        "loss_report": (None if not P["loss_report"].is_file() else [str(P["loss_report"])],
                        [P["loss_report"]]),
        "citation_check": (None if not P["realization"].is_file()
                           else [str(P["realization"]), "--decisions", str(P["decisions"])],
                           [P["realization"], P["decisions"]]),
        # Input-conditional like spec_lint and diff_reference: an app with no requirement
        # register has no constituent, which in `custody: required` mode reads RED — and
        # that is the correct reading, not a punishment. A build with no line back to the
        # customer's document is exactly what this constituent exists to refuse.
        "requirements_coverage": (None if not P["requirements"].is_file()
                                  else ["coverage", str(P["requirements"]),
                                        "--design", str(P["design"]),
                                        "--model", str(m), "--quiet"],
                                  [P["requirements"], m]),
    }


def _run(verb: str, argv: list[str]) -> tuple[int, str]:
    try:
        r = subprocess.run([PY, str(KIT), VERB_CLI[verb], *argv], capture_output=True, text=True)
    except Exception as e:  # noqa: BLE001
        return 127, f"{verb}: could not run ({e})"
    tail = (r.stdout or r.stderr or "").strip().splitlines()
    return r.returncode, (tail[-1][:200] if tail else "")


def custody_mode(P: dict) -> str:
    return _load(P["kit_yaml"]).get("custody", "stamp")   # absent => stamp (backwards compatible)


def custody_declared(P: dict) -> bool:
    """Was the posture CHOSEN, or did it fall out of a missing .kit.yaml?

    `stamp` makes every required check optional for GREEN, and it is what an app with no
    .kit.yaml silently gets. So a brand-new country application starts at the weakest posture
    the platform offers and — until this flag existed — had no way to tell. The default is left
    alone for backwards compatibility; what changes is that it can now be SEEN.
    """
    return "custody" in (_load(P["kit_yaml"]) or {})


def app_class(P: dict) -> str:
    """The application CLASS, from .kit.yaml. Default `service` — the ordinary case, and the one
    every existing app keeps without editing a file.

    F-CFG-28 (the owner, 13 Aug 2026): a KERNEL-class application is platform machinery that no customer
    asked for in a requirements document — the configuration catalogue, the module register. It
    has no customer-requirements corpus, so `diff_reference` has nothing to diff a model against.
    That is a fact about the class, not a defect in the app and not something a waiver should
    paper over. The class is declared HERE, in the same file that declares the custody posture,
    because both answer the same question: what kind of application is this, and what may
    therefore be measured about it.
    """
    return str((_load(P["kit_yaml"]) or {}).get("app_class", "service"))


# Constituents that DO NOT APPLY to a class of application, with the reason each is not applicable.
# Deliberately a table and not a flag: every entry has to name a constituent, a class and a reason,
# so a future N/A can be read and argued with rather than discovered in a branch. Nothing is
# skipped silently — an entry here produces a VISIBLE constituent carrying `applicable: false` and
# an N/A-BY-PROFILE summary, exactly as the behavioural legs already do (ADR-077, ADR-093).
NA_BY_PROFILE = {
    ("kernel", "diff_reference"):
        "kernel-class app has no customer-requirements corpus to diff the model against "
        "(F-CFG-28, the owner, 13 Aug 2026; revisit if S2C defines kernel-app realism)",
    # 2026-08-14. `requirements_coverage` joined REQUIRED_SET at 3837f30, AFTER the F-CFG-28
    # ruling, and asks that ruling's exact question of the same class of app: its denominator is
    # the CUSTOMER'S requirements document (scope `fidelity`), which a kernel app does not have.
    # The catalogue session found this and REFUSED to extend its own exemption table to a check
    # that appeared after the ruling — correct conduct, and the precedent it set is that a
    # constituent joining the required set after a ruling RE-ASKS the ruling. The owner re-asked and
    # ruled. This entry is that ruling, not a session's inference from it.
    ("kernel", "requirements_coverage"):
        "a fidelity check whose denominator is the customer's requirements document is "
        "N/A-by-profile for an app whose requirements ARE the decision ledger "
        "(F-CFG-31, the owner, 13 Aug 2026; revisit if a kernel app is ever given a requirement register)",
}


def _acceptance_constituent(P: dict, kit_version: str) -> dict:
    """The behavioural leg (ADR-077): reads the RECORDED live `kit test` result — it does not run
    scenarios here (the live run needs an instance). Freshness keys on the model sha, so a model
    change re-STALEs it; a result whose recorded model_sha != current is stale too. `applicable`
    is True only when the model declares scenarios — an app with none is not-applicable, not red."""
    m = P["model"]
    scenarios = bool((_load(m).get("acceptance") or {}).get("scenarios"))
    result_path = P["app_dir"] / "design" / "acceptance-result.yaml"
    base = {"ran_at": _now(), "tool_version": kit_version, "scope": SCOPE["acceptance"],
            "inputs": {str(m): _sha(m)}}
    if not scenarios:
        return {**base, "exit": 0, "applicable": False, "summary": "no scenarios declared — not applicable"}
    if not result_path.is_file():
        return {**base, "exit": 127, "applicable": True,
                "summary": "no acceptance-result — run `kit test <app> --instance <X>`"}
    res = _load(result_path).get("acceptance_result") or {}
    base["inputs"][str(result_path)] = _sha(result_path)
    if res.get("model_sha256") != _sha(m):
        return {**base, "exit": 1, "applicable": True,
                "summary": "acceptance-result stale (ran against a different model) — re-run `kit test`"}
    return {**base, "exit": int(res.get("exit", 1)), "applicable": True,
            "summary": f"{res.get('passed', 0)}/{res.get('total', 0)} scenario(s) executed on "
                       f"{res.get('instance', '?')} ({res.get('ran_at', '?')})"}


def _ui_probe_constituent(P: dict, kit_version: str) -> dict:
    """The reachability leg (ADR-093): reads the RECORDED `kit ui-probe` result.

    Freshness keys on the sha of the USERVIEW JSON that was probed, not on the model — a rebuild
    that changes a menu invalidates the probe even when the model is untouched, which is exactly
    the case that let a readonly FormMenu survive fifteen deployments.
    `applicable` is False when the app has no build to probe."""
    uv_dir = P["build"] / "userviews"
    uv_files = sorted(uv_dir.glob("*.json")) if uv_dir.is_dir() else []
    result_path = P["app_dir"] / "design" / "ui-probe-result.yaml"
    base = {"ran_at": _now(), "tool_version": kit_version, "scope": SCOPE["ui_probe"], "inputs": {}}
    if not uv_files:
        return {**base, "exit": 0, "applicable": False,
                "summary": "no built userview — nothing to probe"}
    base["inputs"][str(uv_files[0])] = _sha(uv_files[0])
    if not result_path.is_file():
        return {**base, "exit": 127, "applicable": True,
                "summary": "never probed — run `kit ui-probe <app> --build <dir> --instance <X>`"}
    res = _load(result_path).get("ui_probe_result") or {}
    base["inputs"][str(result_path)] = _sha(result_path)
    if res.get("userview_sha256") != _sha(uv_files[0]):
        return {**base, "exit": 1, "applicable": True,
                "summary": "ui-probe result stale (a different userview was probed) — re-run it"}
    unproven = res.get("unproven") or 0
    return {**base, "exit": int(res.get("exit", 1)), "applicable": True,
            "summary": f"{res.get('kept', 0)}/{res.get('total', 0)} menus keep their promise on "
                       f"{res.get('instance', '?')}"
                       + (f" ({unproven} unproven — no data)" if unproven else "")}


def assemble(model: pathlib.Path, kit_version: str) -> dict:
    P = app_paths(model)
    klass = app_class(P)
    constituents = {}
    for verb, (argv, inputs) in _constituent_plan(P).items():
        scope = SCOPE.get(verb, "")
        if argv is None:
            # F-CFG-28: a constituent that does not APPLY to this class of application is
            # recorded as not-applicable and passes, in the same shape the behavioural legs
            # already use. Note the ORDER: this branch is reached only when the input is
            # genuinely absent. A kernel app that DOES carry a realism file gets the real check
            # run against it — the class never suppresses evidence that exists.
            reason = NA_BY_PROFILE.get((klass, verb))
            if reason:
                constituents[verb] = {
                    "ran_at": _now(), "tool_version": kit_version, "scope": scope, "inputs": {},
                    "exit": 0, "applicable": False,
                    "summary": f"N/A-BY-PROFILE — app_class {klass}: {reason}"}
                continue
            constituents[verb] = {"ran_at": _now(), "tool_version": kit_version, "scope": scope,
                                  "inputs": {}, "exit": 127, "summary": f"skipped — missing input for {verb}"}
            continue
        code, summary = _run(verb, argv)
        block = {"ran_at": _now(), "tool_version": kit_version, "scope": scope,
                 "inputs": _existing(inputs), "exit": code, "summary": summary}
        # 2026-08-06: exit 3 means the check RAN and found its population empty. That is not a
        # pass and not a failure of the thing being graded — it is an absence of evidence, and a
        # reader must be able to tell the two reds apart. It still blocks GREEN in `required`
        # posture, because "nothing was measured" is not "nothing is wrong".
        if code == OBSERVED_NOTHING:
            block["observed"] = "nothing"
        constituents[verb] = block
    constituents["acceptance"] = _acceptance_constituent(P, kit_version)   # ADR-077 behavioural leg
    constituents["ui_probe"] = _ui_probe_constituent(P, kit_version)       # ADR-093 reachability leg
    rep = {"app": _load(model).get("app", {}).get("id", pathlib.Path(model).stem),
           "model_sha256": _sha(model), "kit_version": kit_version,
           "custody_mode": custody_mode(P), "custody_declared": custody_declared(P),
           "assembled_at": _now(), "constituents": constituents}
    rep["verdict"] = derive_verdict(rep, signed=False)
    return rep


def _stale(rep: dict) -> bool:
    for c in (rep.get("constituents") or {}).values():
        for path, sha in (c.get("inputs") or {}).items():
            p = pathlib.Path(path)
            if not p.is_file() or _sha(p) != sha:
                return True
    return False


def derive_verdict(rep: dict, signed: bool | None = None) -> str:
    if _stale(rep):
        return "STALE"
    if rep.get("custody_mode") == "required":
        cons = rep.get("constituents") or {}
        required = list(REQUIRED_SET)
        for leg in BEHAVIOURAL:               # declared and applicable -> it must be green
            c = cons.get(leg)
            if c and c.get("applicable"):
                required.append(leg)
        for verb in required:
            c = cons.get(verb)
            if not c or c.get("exit", 1) != 0:
                return "RED"
    if signed is None:
        signed = bool(rep.get("signature"))
    return "GREEN" if signed else "UNSIGNED"


def _canonical(rep: dict) -> dict:
    """Report substance, minus display-only verdict and volatile timestamps — so a re-check
    (verdict only) or a no-substantive-change re-assemble keeps the GATED stamp STABLE and
    does not spuriously re-drift L3 (CH-01 review point #4)."""
    body = {k: v for k, v in rep.items() if k not in ("verdict", "assembled_at")}
    cons = {v: {k: x for k, x in (c or {}).items() if k != "ran_at"}
            for v, c in (body.get("constituents") or {}).items()}
    return {**body, "constituents": cons} if "constituents" in body else body


def report_sha(rep: dict) -> str:
    return hashlib.sha256(
        yaml.safe_dump(_canonical(rep), sort_keys=True, allow_unicode=True).encode("utf-8")).hexdigest()


def _validate_against_schema(rep: dict) -> None:
    """The report is validated against its OWN schema before it is written. Skipped
    silently only if jsonschema is unavailable. This exists because three fields the
    assembler intentionally writes (acceptance, scope, applicable) sat outside the
    schema for months: nothing ever checked, so nothing ever failed."""
    try:
        import jsonschema
    except ImportError:
        return
    schema_path = pathlib.Path(__file__).resolve().parent.parent / "schemas" / "gate-report.schema.yaml"
    if not schema_path.exists():
        return
    schema = yaml.safe_load(schema_path.read_text(encoding="utf-8"))
    errs = sorted(jsonschema.Draft202012Validator(schema).iter_errors({"gate_report": rep}),
                  key=lambda e: list(e.absolute_path))
    if errs:
        detail = "; ".join(f"{'/'.join(str(x) for x in e.absolute_path)}: {e.message}"
                           for e in errs[:4])
        raise SystemExit(f"gate-report does not satisfy its own schema — refusing to write: {detail}")


def _write(P: dict, rep: dict) -> None:
    _validate_against_schema(rep)
    P["design"].mkdir(parents=True, exist_ok=True)
    P["report"].write_text(
        "# Computed by `kit gate` — do not hand-edit (ADR-069). Freshness is sha-keyed.\n"
        + yaml.safe_dump({"gate_report": rep}, sort_keys=False, allow_unicode=True),
        encoding="utf-8", newline="\n")


def _read_report(P: dict) -> dict | None:
    return (_load(P["report"]) or {}).get("gate_report") if P["report"].is_file() else None


def cmd_assemble(a) -> int:
    P = app_paths(a.app)
    kv = str(_load(P["kit_yaml"]).get("kit_version", "unknown"))
    rep = assemble(a.app, kv)
    _write(P, rep)
    posture = rep["custody_mode"]
    if not rep.get("custody_declared", True):
        posture += " — DEFAULTED, not chosen (no `custody:` in .kit.yaml)"
    print(f"gate: assembled {P['report']} — verdict {rep['verdict']} (custody_mode {posture})")
    # F-CFG-28: an N/A constituent is announced on the console as well as written to the report.
    # A not-applicable check that only a reader of the YAML can find is a silent skip wearing a
    # field name, and the whole objection to waiving `diff_reference` was that it would be unseen.
    for verb, c in (rep.get("constituents") or {}).items():
        if str(c.get("summary", "")).startswith("N/A-BY-PROFILE"):
            print(f"gate: {verb} — {c['summary']}")
    if not rep.get("custody_declared", True) and rep["custody_mode"] == "stamp":
        print("gate: NOTE — under `stamp` every required check is optional for GREEN, and this "
              "app never chose that posture. Declare `custody:` in .kit.yaml to say what you mean.")
    return 0


def cmd_check(a) -> int:
    P = app_paths(a.app)
    rep = _read_report(P)
    if rep is None:
        print("gate: no report (UNGATED)")
        return 1
    # 2026-08-06: `check` NO LONGER WRITES. It used to recompute the verdict and rewrite the
    # report — so a verb named *check* mutated a committed, signed file, and the only way to
    # learn the true verdict was to destroy the artefact you were asking about. It happened
    # twice by accident in one day. A read-shaped verb must not write.
    stored   = rep.get("verdict")
    computed = derive_verdict(rep)
    print(f"gate: verdict {computed}")
    if stored and stored != computed:
        print(f"gate: the STORED verdict reads {stored} — this report is out of date with its "
              f"own inputs. Re-run `kit gate assemble` (and re-sign) to correct it; `check` will "
              f"not rewrite a signed artefact.")
    return 0 if computed == "GREEN" else 1


def load_signers() -> list[dict]:
    """The signers registry (UB-12, ex TA-01 T1 / ADR-074): contracts/signers.yaml.
    Two or more registered identities arm the separation-of-duties ERROR."""
    p = HERE.parent / "contracts" / "signers.yaml"
    if not p.is_file():
        return []
    return (_load(p) or {}).get("signers", []) or []


def check_signer(who: str, authors: list[str], registry: list[dict]) -> tuple[bool, str | None]:
    """(ok, message). With >=2 registered identities: an unregistered signer or an
    author-as-signer is REFUSED. With no registry (or one identity): v1 signer-on-record
    — author-as-signer allowed with a warning (owner ruling 2026-07-18)."""
    if len(registry) >= 2:
        ids = {s.get("id") for s in registry}
        if who not in ids:
            return False, (f"signer {who!r} is not a registered identity "
                           f"(contracts/signers.yaml: {', '.join(sorted(str(i) for i in ids))})")
        if who in authors:
            return False, (f"signer {who!r} is also an author — separation of duties is "
                           f"ENFORCED now that a second identity is registered (UB-12; "
                           f"was a v1 warning)")
        return True, None
    if who in authors:
        return True, (f"WARNING signer {who!r} is also an author — allowed in v1 "
                      f"(signer-on-record); separation enforced once a second identity exists.")
    return True, None


def cmd_sign(a) -> int:
    P = app_paths(a.app)
    rep = _read_report(P)
    if rep is None:
        print("gate: nothing to sign — assemble first")
        return 1
    authors = _load(a.app).get("model", {}).get("authors", []) or []
    ok, msg = check_signer(a.who, authors, load_signers())
    if not ok:
        print(f"gate: REFUSED — {msg}")
        return 1
    if msg:
        print(f"gate: {msg}")
    rep["signature"] = {"signer": a.who, "date": _dt.date.today().isoformat()}
    rep["verdict"] = derive_verdict(rep, signed=True)
    _write(P, rep)
    print(f"gate: signed by {a.who} — verdict {rep['verdict']}")
    return 0 if rep["verdict"] == "GREEN" else 1


def resolve(model: pathlib.Path) -> str:
    """The custody string gen/build_app/deploy stamp: GATED:<sha> only if a fresh, green,
    signed report exists; UNGATED otherwise (absence of information is never credible)."""
    P = app_paths(model)
    rep = _read_report(P)
    if rep is None or derive_verdict(rep) != "GREEN":
        return "UNGATED"
    return f"GATED:{report_sha(rep)}"


def resolve_dir(app_dir) -> str:
    """resolve() when only the app directory is known (build_app has no model path)."""
    report = pathlib.Path(app_dir) / "design" / "gate-report.yaml"
    if not report.is_file():
        return "UNGATED"
    rep = (_load(report) or {}).get("gate_report")
    if rep is None or derive_verdict(rep) != "GREEN":
        return "UNGATED"
    return f"GATED:{report_sha(rep)}"


def cmd_resolve(a) -> int:
    print(resolve(a.app))
    return 0


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="gate_report", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="verb", required=True)
    for verb, fn in (("assemble", cmd_assemble), ("check", cmd_check), ("resolve", cmd_resolve)):
        p = sub.add_parser(verb)
        p.add_argument("app", type=pathlib.Path)
        p.set_defaults(fn=fn)
    p = sub.add_parser("sign")
    p.add_argument("app", type=pathlib.Path)
    p.add_argument("--as", dest="who", required=True)
    p.set_defaults(fn=cmd_sign)
    return ap


def main() -> int:
    a = build_parser().parse_args()
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
