#!/usr/bin/env python3
"""kit — the spec kit's facade over its tools (ADR-008: CLI named `kit`).

    kit validate  <app.yaml>                              the interaction design gate (L021, SDD-11 §8),
                  then four-layer validation and the projection layer (every projector of
                  `kit gen all` tried; ADR-107); the gate is an error in every custody mode
    kit gen       forms|datalists|userview|dashboards|workflow|all <app> --out D  the projectors,
                  after the interaction design gate, which refuses first and writes nothing; the
                  output folder receives what they wrote only when every one succeeded (ADR-107)
    kit match     <app.yaml> --instance N [--instances P] pre-deploy platform match
    kit checklist <app.yaml> [--out F]                    platform review checklist
    kit trace     <app.yaml> [--out F] [--strict]         requirements→artefacts traceability;
                  exit 1 on a requirement with no realizing artefact (real since 2026-08-13)
    kit suite     <app.yaml> [--out F]                    acceptance → regression suite manifest
    kit diff-reference <app.yaml> --realism F [--out F]   realism gate: design ↔ anchor (Phase G)
    kit watch     <app.yaml> --out D [--once]              inner loop: validate + reproject what changed
    kit harvest   <app.jwa> --app ID [--out F]             migration: reverse a deployed .jwa → DRAFT L1 model
    kit lint-questions <cards.yaml>... [--against <open-set.yaml>]  D3: refuses a card set
                  that puts ids, class names or stage names to a human, or that drops an
                  assembled item (S2C-03/01 §3.3)
    kit rulings   assemble <app-dir>|lint <set>...|applied <set>... --evidence D  Stage D:
                  the open set is assembled deterministically, the owner rules, the ruling
                  set is the artefact, and what it TOUCHES is checked (S2C-03/01)
    kit lint-decisions <design/decisions.yaml>            Layer-0 decision-inventory structural gate (M0)
    kit seams     [--baseline F]                          seam lint: declared enforcement points, rules, subjects keys and gate slots all resolve (UB-13)
    kit breadth   <subjects.yaml>... --org-type T         org-type breadth: the canonical classes a PAERA type requires are present (UB-4)
    (kit sheet / lint-sheet / render / derive are RETIRED, 31 Aug 2026, ruling R-2 —
     the parameter-sheet path; whole in x_archive/retired-sheet-path-2026-08-31/)
    kit compile   <app.yaml> [--loss F] [--decisions F] [--realization F] [--input F]   Stage G
                  entry: the loss-report refusal — an unnamed schema gap fails naming the
                  entry; model validates; citations 100% (UB-11); and INPUT-VS-OUTPUT —
                  every input element lands, is recorded as a loss, or is an explicit
                  assumption, else exit 2 naming it (2026-08-13)
    kit lint-pattern <pattern.yaml> [--conformance S]     the pattern contract: typed sheet, nine-dim map, class resolution, conformance (UB-6)
    kit surfaces  <subjects.yaml> [--pattern P]           the supporting-surface inventory derived from the canonical entity inventory (F7)
    kit requirements extract <doc.md> [--out F] [--prefix P]   the customer's document → the requirement register (UB-1)
    kit requirements coverage <requirements.yaml> --design D [--model app.yaml]   the fidelity
                  axis: every requirement REALIZED BY AN ARTEFACT or signed off. A gate
                  constituent since 2026-08-13; an id string in a file is not a claim
    kit claims-lint <file>...                             authored gate-verdict claims fail (ADR-065; also runs inside validate)
    kit instantiate <subjects.yaml> --slice ID [--out F]  nine templates → skeleton TO_CONFIRM inventory (M3)
    kit walkthrough <scenarios.yaml> --decisions <F>      playback: scenarios → cited step-by-step narrative (M4)
    kit toconfirm <decisions.yaml>...                     the owner's open-questions (TO_CONFIRM) view (M4)
    kit spec-lint <decisions.yaml> [<more> ...] --subjects <F>   U-rules: does the inventory cover the subjects (M1)
    kit loss-check <loss-report.yaml>                    is a decision the model cannot enforce left open
    kit zone-check <app.yaml>                            is a standing value offered for editing in service
    kit adoption   <app.yaml> [--min R]                   does the app use what the schema already offers
    kit citation-check <realization.yaml> --decisions <F> the citation column: cite-or-ASSUMPTION (M1)
    kit regbb     <app.yaml> [--out F]                    GovStack RegBB channel contract ({serviceId}.yml)
    kit coverage  <app.yaml> [--out F] [--min PCT]        declarative-vs-bespoke coverage metric;
                  exit 1 on an unsized/unjustified bespoke entry or below --min. The
                  percentage itself stays INDICATIVE (S2C-04 §17)
    kit new       <appId> [--name N] [--out F]            scaffold a minimal model; its entry
                  model.interaction_design is written as a question, and the model is refused
                  until the question is answered with an accepted interaction design
    kit slot      <n> | --check                          the register of the things SDD-01 §4
                  names: one resolved row, or every row and every handover checked against the
                  standards root and the kit, their number read from the register itself
                  (SDD-01 §4 and §10; decisions D2 and D4)
    kit spec map  | route                                 the picture of the work drawn from
                  that register, and the route through it with what states each crossing
    kit spec new  <systemId> --name N --out D [--carry SLOT=PATH ...] [--prior D]
                  the specification tree: one folder per thing SDD-01 §4 names, every
                  slot README rendered from templates/spec/slots.yaml, carried artefacts
                  checksummed into their slots, and the planning commission emitted
    kit conform   <n> <artifact> [--verdicts F] [--checklist F]   the claim of conformance, one
                  line per rule of the row's checklist with its verdict and the check that
                  decided it; refuses a claim that is not rule by rule and a line citing a check
                  no program performs (PLAN.md §3.1; 01_PROCEDURE.md §5; route R2)
    kit skills    --check                                 every skill's pin against the document
                  in the standards root and the checklist's head: current, behind, or pinned to
                  a document not in the root; exit 1 on any but current (04_TARGET_STATE.md §5)
    kit stale     <n> <artifact> [--tree D]               what a change to one artifact makes
                  stale: read from the register's seams and what each artifact records it was
                  made from; it lists and changes nothing (plan M4, route R2)
    kit screens walk <screen record> [--out D] [--template F]   the clickable walk-through
                  produced from a screen record written to the template of SDD-07: one page
                  for every screen, every variation carried on a screen and every ending, each
                  stamped with the record's identifier, version and status; refuses a record
                  without a version or outside the template's form (SDD-07 §8; route R4).
                  Not `kit walkthrough`, which plays back scenarios
    kit diff      <old.yaml> <new.yaml> [--out F]         structural model diff (exit 1 on drift)
    kit drift     <app.yaml> <generated_dir>              provenance drift (IN_SYNC/STALE/HAND_EDITED/…)
    kit totality  <app.yaml> [--generated D] [--build D]  the T-series: every declaration lands in the
                  artefact or is refused out loud — drift compares the projector to itself,
                  totality compares it to the model (the four silent drops of 2026-08-05)
    kit tracker   [--evidence D]                          rebuild the build tracker across every app
    kit method    [--evidence D]                          rebuild the plain-English method view
    kit conformance <app.yaml>...                         clean-regenerable standing check (C5 · WP-5): each app still validates + projects
    kit gate      assemble|check|sign|resolve <app.yaml> [--as ID]  the custody gate-report (CH-01)
    kit deploy    <app.yaml> --instance N                 the interaction design gate, the
                  match-gate, then the delivery deploy
    kit seed      <app.yaml>                               the delivery seed engine
    kit test      <app.yaml>                               the delivery acceptance suite

The in-kit verbs (validate/gen/match/checklist) are self-contained and project-neutral.
deploy/seed/test orchestrate the SHIPPED delivery engines — they do not embed project
tooling: the command is supplied via an env var (KIT_DEPLOY_CMD / KIT_SEED_CMD /
KIT_TEST_CMD), so the kit stays free of project-specific script names. `deploy` runs the
interaction design gate first, then the platform-match gate, and refuses to hand off on either.
`gen` and `deploy` run the interaction design gate before anything else (METHOD-2026-09-25-12).

Exit codes propagate from the underlying tool; 3 = not-configured / setup error.
"""
from __future__ import annotations

import argparse
import os
import pathlib
import shlex
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
PY = sys.executable


def _run(cmd: list[str]) -> int:
    return subprocess.run(cmd).returncode


def _tool(name: str, *args: str) -> int:
    return _run([PY, str(HERE / name), *[str(a) for a in args]])


def cmd_validate(a) -> int:
    rc = _tool("validate.py", a.app)
    # ADR-065 / Job B #3: authored gate-verdict claims fail validation (claims-lint)
    return _tool("claims_lint.py", a.app) or rc


def cmd_validate_pack(a) -> int:
    args = [str(a.pack_dir)] + (["--write-hash"] if a.write_hash else [])
    return _tool("validate_pack.py", *args)


def cmd_new_pack(a) -> int:
    return _tool("validate_pack.py", "--scaffold", a.pack_id,
                 "--sector", a.sector, "--pattern", a.pattern, "--out", a.out)


def cmd_slot(a) -> int:
    """kit slot — resolve the register of the method's things against the documents."""
    args = ["--check"] if a.check else [a.n]
    if a.citations:
        args.append("--citations")
    return _tool("slot.py", *args)


def cmd_spec_map(a) -> int:
    """kit spec map / kit spec route — the picture and the route, from the register."""
    return _tool("specmap.py", a.mode)


def cmd_spec(a) -> int:
    """kit spec new — scaffold a specification tree (the things of SDD-01 §4)."""
    args = [a.system_id, "--out", a.out]
    if a.name:
        args += ["--name", a.name]
    for c in a.carry or []:
        args += ["--carry", c]
    if a.prior:
        args += ["--prior", a.prior]
    if a.force:
        args += ["--force"]
    return _tool("scaffold_spec.py", *args)


def cmd_conform(a) -> int:
    """kit conform — the claim of conformance of one artifact, rule by rule (route R2)."""
    args = [a.n, str(a.artifact)]
    for flag in ("verdicts", "checklist", "slots"):
        if getattr(a, flag, None):
            args += [f"--{flag}", str(getattr(a, flag))]
    return _tool("conform.py", *args)


def cmd_skills(a) -> int:
    """kit skills --check — every skill's pin against the root and the checklist's head."""
    if not a.check:
        print("kit skills: --check is the one act of this command (kit skills --check)",
              file=sys.stderr)
        return 2
    args = ["--check"]
    for flag in ("standards_root", "marketplace", "kit_root"):
        if getattr(a, flag, None):
            args += [f"--{flag.replace('_', '-')}", str(getattr(a, flag))]
    return _tool("skills_check.py", *args)


def cmd_stale(a) -> int:
    """kit stale — what a change to one artifact makes stale (plan M4, route R2)."""
    args = [a.n, str(a.artifact)]
    for flag in ("tree", "slots"):
        if getattr(a, flag, None):
            args += [f"--{flag}", str(getattr(a, flag))]
    return _tool("stale.py", *args)


def cmd_screens(a) -> int:
    """kit screens walk — the walk-through produced from a screen record (SDD-07 §8; route R4)."""
    args = [str(a.record)]
    for flag in ("out", "template"):
        if getattr(a, flag, None):
            args += [f"--{flag}", str(getattr(a, flag))]
    return _tool("screens_walk.py", *args)


# The projectors `kit gen` runs live in tools/projection_trial.py, which `kit validate` reads too, so
# that the verb and the validator can never run different projectors (ADR-107).
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
from projection_trial import GEN_SCRIPTS, PER_FEATURE as _PER_FEATURE  # noqa: E402


def _custody(app) -> str:
    try:
        import gate_report
        return gate_report.resolve(app)
    except Exception:
        return "UNGATED"


def _custody_refusal(app, verb: str) -> bool:
    """UB-12 (ex TA-01 T1): a custody:required app GENERATES AND DEPLOYS only with a
    fresh, green, signed gate report — anything else is an executed refusal (ADR-077),
    never a stamped warning."""
    try:
        import gate_report
        mode = gate_report.custody_mode(gate_report.app_paths(pathlib.Path(a_path := str(app))))
    except Exception:
        return False
    if mode != "required":
        return False
    custody = _custody(app)
    if str(custody).startswith("GATED"):
        return False
    print(f"kit {verb}: REFUSED — custody is `required` and the gate resolves {custody}; "
          f"a required app {verb}s only with a fresh, green, signed report "
          f"(kit gate assemble → sign). [CUSTODY-REFUSED]")
    return True


def _ixd_refusal(app, verb: str) -> bool:
    """The interaction design gate (rule L021, SDD-11 §8), run before anything else a verb does:
    True when it refuses the model, having said why. The same function as `kit validate`,
    `build_app.py` and `deploy_dx9.py` run; it reads no custody mode and no flag, so nothing a
    verb is given turns it off (METHOD-2026-09-25-12)."""
    if str(HERE) not in sys.path:
        sys.path.insert(0, str(HERE))
    import validate
    return validate.admit_or_refuse(app, f"kit {verb}") != 0


def cmd_gen(a) -> int:
    if _ixd_refusal(a.app, "gen"):
        return 2
    if _custody_refusal(a.app, "gen"):
        return 2
    custody = _custody(a.app)   # CH-01: stamp what the gate-report resolves to
    targets = list(GEN_SCRIPTS) if a.target == "all" else [a.target]
    # ADR-107 (a delivery's hand-off of 5 October 2026, item 4): a refused projection writes nothing.
    # Every projector asked for runs into a folder of its own; the output folder receives what
    # they wrote only when every one of them projected the model. Until then `kit gen all` wrote
    # the seed, the userview and the lifecycle of a model whose forms were refused (38 files of a
    # build with no form in one delivery's run).
    import shutil
    import tempfile
    import projection_trial as pt
    staged_root = pathlib.Path(tempfile.mkdtemp(prefix="kit-gen-"))
    staged = staged_root / "gen"
    try:
        results = pt.run_all(a.app, staged, custody, a.feature, getattr(a, "fixture", None), targets)
        pt.say(results, staged, a.out)
        rc = pt.first_nonzero(results)
        if rc:
            refused = [r.target for r in results if r.code]
            print(f"kit gen: {', '.join(refused)} refused — nothing written to {a.out}: a refused "
                  f"projection writes nothing (ADR-107); the lines above name what the others "
                  f"would have written")
            return rc
        pt.publish(staged, pathlib.Path(a.out))
        return 0
    finally:
        shutil.rmtree(staged_root, ignore_errors=True)


def cmd_match(a) -> int:
    extra = (["--instances", str(a.instances)] if a.instances else [])
    return _tool("platform_match.py", a.app, "--instance", a.instance, *extra)


def cmd_checklist(a) -> int:
    extra = (["--out", str(a.out)] if a.out else [])
    return _tool("review_checklist.py", a.app, *extra)


def cmd_trace(a) -> int:
    extra = (["--out", str(a.out)] if a.out else [])
    return _tool("emit_trace.py", a.app, *extra)


def cmd_suite(a) -> int:
    extra = (["--out", str(a.out)] if a.out else [])
    return _tool("emit_suite.py", a.app, *extra)


def cmd_diff_reference(a) -> int:
    extra = (["--out", str(a.out)] if a.out else [])
    return _tool("diff_reference.py", a.app, "--realism", str(a.realism), *extra)


def cmd_watch(a) -> int:
    extra = (["--once"] if a.once else []) + (["--interval", str(a.interval)] if a.interval else [])
    return _tool("watch.py", a.app, "--out", str(a.out), *extra)


def cmd_harvest(a) -> int:
    extra = (["--out", str(a.out)] if a.out else [])
    return _tool("harvest.py", a.jwa, "--app", a.app, *extra)


def cmd_lint_questions(a) -> int:
    """D3 — lints the QUESTION, not the answer: can the person being asked read it?"""
    extra = (["--against", str(a.against)] if a.against else []) \
        + (["--numbers-from", str(a.numbers_from)] if a.numbers_from else [])
    return _tool("lint_questions.py", *[str(p) for p in a.paths], *extra)


def cmd_rulings(a) -> int:
    """Stage D. `assemble` is deterministic; `applied` is computed from the tree, never read."""
    if a.mode == "assemble":
        extra = (["--out", str(a.out)] if a.out else []) \
            + (["--html", str(a.html)] if a.html else []) \
            + (["--title", a.title] if a.title else []) \
            + [x for k in (a.kind or []) for x in ("--kind", k)]
        return _tool("rulings.py", "assemble", str(a.design), *extra)
    if a.mode == "lint":
        return _tool("rulings.py", "lint", *[str(p) for p in a.paths])
    return _tool("rulings.py", a.mode, *[str(p) for p in a.paths],
                 "--evidence", str(a.evidence))


def cmd_requirements(a) -> int:
    if a.mode == "extract":
        extra = (["--out", a.out] if getattr(a, "out", None) else [])
        extra += (["--prefix", a.prefix] if getattr(a, "prefix", None) else [])
        return _tool("requirements.py", "extract", a.document, *extra)
    extra = ["--design", a.design] + (["--quiet"] if getattr(a, "quiet", False) else [])
    return _tool("requirements.py", "coverage", a.register, *extra)


def cmd_lint_decisions(a) -> int:
    return _tool("lint_decisions.py", a.path, *(["--quiet"] if a.quiet else []))


def cmd_claims_lint(a) -> int:
    return _tool("claims_lint.py", *[str(p) for p in a.files])


def cmd_seams(a) -> int:
    extra = ["--baseline", str(a.baseline)] if a.baseline else []
    return _tool("seams.py", *extra)


def cmd_breadth(a) -> int:
    return _tool("breadth.py", *[str(p) for p in a.subjects], "--org-type", a.org_type)


def cmd_compile(a) -> int:
    extra = (["--loss", str(a.loss)] if a.loss else []) \
        + (["--decisions", str(a.decisions)] if a.decisions else []) \
        + (["--realization", str(a.realization)] if a.realization else []) \
        + (["--no-validate"] if a.no_validate else [])
    return _tool("compile_l1.py", a.app, *extra)


def cmd_lint_pattern(a) -> int:
    extra = ["--conformance", str(a.conformance)] if a.conformance else []
    return _tool("lint_pattern.py", a.pattern, *extra)


def cmd_surfaces(a) -> int:
    extra = ["--pattern", str(a.pattern)] if a.pattern else []
    return _tool("surfaces.py", a.subjects, *extra)


def cmd_instantiate(a) -> int:
    extra = (["--out", str(a.out)] if a.out else []) + (["--dimensions", a.dimensions] if a.dimensions else [])
    return _tool("instantiate.py", a.subjects, "--slice", a.slice, *extra)


def cmd_walkthrough(a) -> int:
    extra = (["--out", str(a.out)] if a.out else []) + (["--strict"] if a.strict else [])
    return _tool("walkthrough.py", a.scenarios, "--decisions", str(a.decisions), *extra)


def cmd_toconfirm(a) -> int:
    extra = (["--out", str(a.out)] if a.out else [])
    return _tool("toconfirm.py", *[str(p) for p in a.decisions], *extra)


def cmd_spec_lint(a) -> int:
    extra = (["--allowlist", str(a.allowlist)] if a.allowlist else [])
    return _tool("spec_lint.py", *[str(p) for p in a.decisions],
                 "--subjects", str(a.subjects), *extra)


def cmd_adoption(a) -> int:
    """Does the app use what the schema already offers? (the guard_expr finding, 2026-08-05)"""
    return _tool("adoption.py", str(a.app), *(["--min", str(a.min)] if a.min else []))


def cmd_loss_check(a) -> int:
    """schema-0.2 §3.6: is this application carrying a decision its model cannot enforce?"""
    return _tool("loss_check.py", str(a.report))


def cmd_zone_check(a) -> int:
    """LOSS-002's obligation, mechanised: a zone-B value may not reach a screen that writes it."""
    args = [str(a.app)]
    if a.entity:
        args += ["--entity", a.entity]
    return _tool("zone_check.py", *args)


def cmd_citation_check(a) -> int:
    return _tool("citation_check.py", a.realization, "--decisions", str(a.decisions))


def cmd_regbb(a) -> int:
    extra = (["--out", str(a.out)] if a.out else [])
    return _tool("emit_regbb.py", a.app, *extra)


def cmd_coverage(a) -> int:
    extra = (["--out", str(a.out)] if a.out else [])
    return _tool("emit_coverage.py", a.app, *extra)


def cmd_new(a) -> int:
    extra = (["--name", a.name] if a.name else []) + (["--out", str(a.out)] if a.out else [])
    return _tool("scaffold_model.py", a.app_id, *extra)


def cmd_diff(a) -> int:
    extra = (["--out", str(a.out)] if a.out else [])
    return _tool("model_diff.py", a.old, a.new, *extra)


def cmd_drift(a) -> int:
    return _tool("drift.py", a.app, a.generated_dir)


def cmd_totality(a) -> int:
    """The T-series: model declarations vs emitted artefacts. drift compares the projector
    to itself (drop a field and both sides agree); totality compares it to the model."""
    extra = (["--generated", str(a.generated)] if a.generated else []) \
        + (["--build", str(a.build)] if a.build else [])
    return _tool("totality.py", str(a.app), *extra)


def cmd_reconcile(a) -> int:
    """ADR-103. drift says an instance was hand-edited; reconcile lifts the edit home.

    Acquire the deployed truth (.jwa export + a read-only DB leg), subtract everything
    the projectors own, classify what remains into exactly one RC disposition, and write
    a changeset for a person to rule on. `--apply` is the separate, later run.
    """
    args = [str(a.app)]
    if a.jwa:         args += ["--jwa", str(a.jwa)]
    if a.instance:    args += ["--instance", a.instance]
    if a.base:        args += ["--base", a.base]
    if a.strict_base: args += ["--strict-base"]
    if a.out:         args += ["--out", str(a.out)]
    if a.report_only: args += ["--report-only"]
    if a.apply:       args += ["--apply", str(a.apply)]
    return _tool("reconcile.py", *args)


def cmd_gate(a) -> int:
    extra = (["--as", a.who] if getattr(a, "who", None) else [])
    return _tool("gate_report.py", a.action, a.app, *extra)


def _delivery(verb: str, env_var: str, a) -> int:
    cmd = os.environ.get(env_var)
    if not cmd:
        print(f"kit {verb}: not configured — set {env_var} to the delivery {verb} command "
              f"(the kit orchestrates the shipped engine, it does not embed it).")
        return 3
    full = shlex.split(cmd) + [str(a.app)]
    print(f"kit {verb}: {' '.join(full)}")
    return _run(full)


def cmd_deploy(a) -> int:
    if _ixd_refusal(a.app, "deploy"):
        return 2
    if _custody_refusal(a.app, "deploy"):
        return 2
    rc = cmd_match(a)                       # pre-deploy gate first
    if rc != 0:
        print("kit deploy: platform match failed — refusing to hand off to deploy.")
        return rc
    import gate_report                      # CH-01 deploy refusals
    app_dir = pathlib.Path(a.app).resolve().parent
    gen = app_dir / "generated"
    if gen.is_dir() and _tool("drift.py", a.app, gen) != 0:
        print("kit deploy: build is STALE against the model (drift != clean) — refusing. Regenerate first.")
        return 2
    mode = gate_report.custody_mode(gate_report.app_paths(a.app))
    if mode == "required" and gate_report.resolve(a.app) == "UNGATED":
        print("kit deploy: custody:required app is UNGATED (no fresh, green, signed gate-report) — refusing.")
        return 2
    return _delivery("deploy", "KIT_DEPLOY_CMD", a)


def cmd_seed(a) -> int:
    return _delivery("seed", "KIT_SEED_CMD", a)


def cmd_ui_probe(a) -> int:
    """ADR-093: the reachability leg. Drives a real browser against the DEPLOYED app and asserts
    the promise each menu type makes — the door a person uses, which `kit test` does not."""
    argv = [a.app, "--build", str(a.build), "--instance", a.instance]
    if getattr(a, "headed", False):
        argv.append("--headed")
    return _tool("ui_probe.py", *argv)


def cmd_ui_journey(a) -> int:
    """The PATH leg. ui-probe proves each door opens; this proves a person can walk from one
    end of a procedure to the other. Every menu passed the probe on 2026-08-02 while three
    procedures were impassable — an applicant could create a draft and had no surface anywhere
    to submit it. Each journey creates real records through real screens and deletes exactly
    what it created."""
    argv = [a.app, "--instance", a.instance]
    for flag in ("journeys", "instances"):
        if getattr(a, flag, None):
            argv += [f"--{flag}", str(getattr(a, flag))]
    for flag in ("headed", "keep"):
        if getattr(a, flag, False):
            argv.append(f"--{flag}")
    return _tool("ui_journey.py", *argv)


def cmd_test(a) -> int:
    # A project engine (KIT_TEST_CMD) still wins; otherwise the kit's own run_suite.py executes
    # the model's acceptance block against a live instance — the ADR-077 behavioural leg.
    if os.environ.get("KIT_TEST_CMD"):
        return _delivery("test", "KIT_TEST_CMD", a)
    if not getattr(a, "instance", None):
        print("kit test: --instance <name> required (or set KIT_TEST_CMD for a project engine).")
        return 3
    argv = [a.app, "--instance", a.instance]
    if getattr(a, "instances", None):
        argv += ["--instances", a.instances]
    if getattr(a, "api_key", None):
        argv += ["--api-key", a.api_key]
    if getattr(a, "feature", None):
        argv += ["--feature", a.feature]
    if getattr(a, "out", None):
        argv += ["--out", str(a.out)]
    return _tool("run_suite.py", *argv)


def cmd_ux_lint(a) -> int:
    return _tool("ux_lint.py", a.app, "--build", str(a.build))


def cmd_conformance(a) -> int:
    return _tool("conformance.py", *[str(x) for x in a.apps])


def _stamp():
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")


def cmd_tracker(a) -> int:
    """Rebuild the build tracker across every application under the evidence repo."""
    extra = ["--evidence", str(a.evidence)] if a.evidence else []
    return _tool("tracker.py", _stamp(), *extra)


def cmd_method(a) -> int:
    """Rebuild the plain-English view of the method itself."""
    extra = ["--evidence", str(a.evidence)] if a.evidence else []
    return _tool("method_view.py", _stamp(), *extra)


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="kit", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="verb", required=True)

    p = sub.add_parser("validate"); p.add_argument("app", type=pathlib.Path); p.set_defaults(fn=cmd_validate)

    p = sub.add_parser("gen")
    p.add_argument("target", choices=list(GEN_SCRIPTS) + ["all"])   # stays in sync with GEN_SCRIPTS
    p.add_argument("app", type=pathlib.Path)
    p.add_argument("--out", required=True)
    p.add_argument("--feature")
    p.add_argument("--fixture", type=pathlib.Path,
                   help="seed target only: an additional seed source outside the model — "
                        "deployment scenery such as the rows ui-probe needs to prove a list")
    p.set_defaults(fn=cmd_gen)

    p = sub.add_parser("match")
    p.add_argument("app", type=pathlib.Path)
    p.add_argument("--instance", required=True)
    p.add_argument("--instances", type=pathlib.Path)
    p.set_defaults(fn=cmd_match)

    p = sub.add_parser("checklist")
    p.add_argument("app", type=pathlib.Path)
    p.add_argument("--out", type=pathlib.Path)
    p.set_defaults(fn=cmd_checklist)

    p = sub.add_parser("trace")
    p.add_argument("app", type=pathlib.Path)
    p.add_argument("--out", type=pathlib.Path)
    p.set_defaults(fn=cmd_trace)

    p = sub.add_parser("suite")
    p.add_argument("app", type=pathlib.Path)
    p.add_argument("--out", type=pathlib.Path)
    p.set_defaults(fn=cmd_suite)

    p = sub.add_parser("diff-reference")
    p.add_argument("app", type=pathlib.Path)
    p.add_argument("--realism", type=pathlib.Path, required=True)
    p.add_argument("--out", type=pathlib.Path)
    p.set_defaults(fn=cmd_diff_reference)

    p = sub.add_parser("watch")
    p.add_argument("app", type=pathlib.Path)
    p.add_argument("--out", type=pathlib.Path, required=True)
    p.add_argument("--interval", type=float, default=1.5)
    p.add_argument("--once", action="store_true")
    p.set_defaults(fn=cmd_watch)

    p = sub.add_parser("harvest")
    p.add_argument("jwa", type=pathlib.Path)
    p.add_argument("--app", required=True)
    p.add_argument("--out", type=pathlib.Path)
    p.set_defaults(fn=cmd_harvest)

    p = sub.add_parser("seams")
    p.add_argument("--baseline", type=pathlib.Path,
                   help="known-open baseline; exit 0 iff findings match it one for one")
    p.set_defaults(fn=cmd_seams)

    p = sub.add_parser("breadth")
    p.add_argument("subjects", nargs="+", type=pathlib.Path)
    p.add_argument("--org-type", required=True, dest="org_type")
    p.set_defaults(fn=cmd_breadth)


    p = sub.add_parser("ui-probe")
    p.add_argument("app", type=pathlib.Path)
    p.add_argument("--build", required=True, type=pathlib.Path)
    p.add_argument("--instance", required=True)
    p.add_argument("--headed", action="store_true")
    p.set_defaults(fn=cmd_ui_probe)

    p = sub.add_parser("ui-journey")
    p.add_argument("app", type=pathlib.Path)
    p.add_argument("--journeys", type=pathlib.Path,
                   help="default: <app dir>/design/journeys.yaml")
    p.add_argument("--instance", required=True)
    p.add_argument("--instances")
    p.add_argument("--headed", action="store_true")
    p.add_argument("--keep", action="store_true",
                   help="do NOT delete what the run created (for inspecting a failure)")
    p.set_defaults(fn=cmd_ui_journey)




    p = sub.add_parser("compile")
    p.add_argument("app", type=pathlib.Path)
    p.add_argument("--loss", type=pathlib.Path)
    p.add_argument("--decisions", type=pathlib.Path)
    p.add_argument("--realization", type=pathlib.Path)
    p.add_argument("--no-validate", action="store_true")
    p.set_defaults(fn=cmd_compile)

    p = sub.add_parser("lint-pattern")
    p.add_argument("pattern", type=pathlib.Path)
    p.add_argument("--conformance", type=pathlib.Path,
                   help="subjects.yaml — every expansion slot must be consumed by a parameter")
    p.set_defaults(fn=cmd_lint_pattern)

    p = sub.add_parser("surfaces")
    p.add_argument("subjects", type=pathlib.Path)
    p.add_argument("--pattern", type=pathlib.Path)
    p.set_defaults(fn=cmd_surfaces)

    p = sub.add_parser("lint-decisions")
    p.add_argument("path", type=pathlib.Path)
    p.add_argument("--quiet", action="store_true")
    p.set_defaults(fn=cmd_lint_decisions)

    p = sub.add_parser("lint-questions")
    p.add_argument("paths", nargs="+", type=pathlib.Path)
    p.add_argument("--against", type=pathlib.Path)
    p.add_argument("--numbers-from", type=pathlib.Path)
    p.set_defaults(fn=cmd_lint_questions)

    p = sub.add_parser("rulings")
    rl = p.add_subparsers(dest="mode", required=True)
    q = rl.add_parser("assemble")
    q.add_argument("design", type=pathlib.Path)
    q.add_argument("--out", type=pathlib.Path)
    q.add_argument("--html", type=pathlib.Path)
    q.add_argument("--title")
    q.add_argument("--kind", action="append")
    q.set_defaults(fn=cmd_rulings)
    q = rl.add_parser("lint")
    q.add_argument("paths", nargs="+", type=pathlib.Path)
    q.set_defaults(fn=cmd_rulings)
    q = rl.add_parser("applied")
    q.add_argument("paths", nargs="+", type=pathlib.Path)
    q.add_argument("--evidence", type=pathlib.Path, required=True)
    q.set_defaults(fn=cmd_rulings)
    q = rl.add_parser("todo")
    q.add_argument("paths", nargs="+", type=pathlib.Path)
    q.add_argument("--evidence", type=pathlib.Path, required=True)
    q.set_defaults(fn=cmd_rulings)

    p = sub.add_parser("requirements")
    rq = p.add_subparsers(dest="mode", required=True)
    q = rq.add_parser("extract")
    q.add_argument("document", type=pathlib.Path)
    q.add_argument("--out", type=pathlib.Path)
    q.add_argument("--prefix")
    q.set_defaults(fn=cmd_requirements)
    q = rq.add_parser("coverage")
    q.add_argument("register", type=pathlib.Path)
    q.add_argument("--design", type=pathlib.Path, required=True)
    q.add_argument("--quiet", action="store_true")
    q.set_defaults(fn=cmd_requirements)

    p = sub.add_parser("claims-lint")
    p.add_argument("files", nargs="+", type=pathlib.Path)
    p.set_defaults(fn=cmd_claims_lint)

    p = sub.add_parser("instantiate")
    p.add_argument("subjects", type=pathlib.Path)
    p.add_argument("--slice", required=True)
    p.add_argument("--out", type=pathlib.Path)
    p.add_argument("--dimensions")
    p.set_defaults(fn=cmd_instantiate)

    p = sub.add_parser("walkthrough")
    p.add_argument("scenarios", type=pathlib.Path)
    p.add_argument("--decisions", type=pathlib.Path, required=True)
    p.add_argument("--out", type=pathlib.Path)
    p.add_argument("--strict", action="store_true")
    p.set_defaults(fn=cmd_walkthrough)

    p = sub.add_parser("toconfirm")
    p.add_argument("decisions", type=pathlib.Path, nargs="+")
    p.add_argument("--out", type=pathlib.Path)
    p.set_defaults(fn=cmd_toconfirm)

    p = sub.add_parser("spec-lint")
    p.add_argument("decisions", type=pathlib.Path, nargs="+",
                   help="one or more inventories, read as one: the foundation ledger plus each "
                        "slice's derived ledger")
    p.add_argument("--subjects", type=pathlib.Path, required=True)
    p.add_argument("--allowlist", type=pathlib.Path)
    p.set_defaults(fn=cmd_spec_lint)

    p = sub.add_parser("adoption")
    p.add_argument("app", type=pathlib.Path)
    p.add_argument("--min", type=float, help="fail below this ratio (0.0-1.0)")
    p.set_defaults(fn=cmd_adoption)

    p = sub.add_parser("loss-check")
    p.add_argument("report", type=pathlib.Path)
    p.set_defaults(fn=cmd_loss_check)

    p = sub.add_parser("zone-check")
    p.add_argument("app", type=pathlib.Path)
    p.add_argument("--entity", default=None)
    p.set_defaults(fn=cmd_zone_check)

    p = sub.add_parser("citation-check")
    p.add_argument("realization", type=pathlib.Path)
    p.add_argument("--decisions", type=pathlib.Path, required=True)
    p.set_defaults(fn=cmd_citation_check)

    p = sub.add_parser("regbb")
    p.add_argument("app", type=pathlib.Path)
    p.add_argument("--out", type=pathlib.Path)
    p.set_defaults(fn=cmd_regbb)

    p = sub.add_parser("coverage")
    p.add_argument("app", type=pathlib.Path)
    p.add_argument("--out", type=pathlib.Path)
    p.set_defaults(fn=cmd_coverage)

    p = sub.add_parser("new")
    p.add_argument("app_id")
    p.add_argument("--name")
    p.add_argument("--out", type=pathlib.Path)
    p.set_defaults(fn=cmd_new)

    p = sub.add_parser("slot")
    p.add_argument("n", nargs="?", help="the slot number, as the register writes it: 00 to 10, or 08a")
    p.add_argument("--check", action="store_true")
    p.add_argument("--citations", action="store_true")
    p.set_defaults(fn=cmd_slot)

    p = sub.add_parser("spec")
    sp = p.add_subparsers(dest="mode", required=True)
    q = sp.add_parser("map"); q.set_defaults(fn=cmd_spec_map)
    q = sp.add_parser("route"); q.set_defaults(fn=cmd_spec_map)
    q = sp.add_parser("new")
    q.add_argument("system_id")
    q.add_argument("--name")
    q.add_argument("--out", type=pathlib.Path, required=True)
    q.add_argument("--carry", action="append", metavar="SLOT=PATH")
    q.add_argument("--prior", type=pathlib.Path)
    q.add_argument("--force", action="store_true")
    q.set_defaults(fn=cmd_spec)

    p = sub.add_parser("conform")
    p.add_argument("n", help="the row of the register, as it writes it: 01 to 09, or 08a")
    p.add_argument("artifact", type=pathlib.Path)
    p.add_argument("--verdicts", type=pathlib.Path)
    p.add_argument("--checklist", type=pathlib.Path)
    p.add_argument("--slots", type=pathlib.Path)
    p.set_defaults(fn=cmd_conform)

    p = sub.add_parser("skills")
    p.add_argument("--check", action="store_true")
    p.add_argument("--standards-root", type=pathlib.Path)
    p.add_argument("--marketplace", type=pathlib.Path)
    p.add_argument("--kit-root", type=pathlib.Path)
    p.set_defaults(fn=cmd_skills)

    p = sub.add_parser("stale")
    p.add_argument("n", help="the row of the register the changed artifact belongs to")
    p.add_argument("artifact", type=pathlib.Path)
    p.add_argument("--tree", type=pathlib.Path)
    p.add_argument("--slots", type=pathlib.Path)
    p.set_defaults(fn=cmd_stale)

    p = sub.add_parser("screens")
    sw = p.add_subparsers(dest="mode", required=True)
    q = sw.add_parser("walk", help="the clickable walk-through produced from a screen record")
    q.add_argument("record", type=pathlib.Path, help="the screen record, a filled copy of the template")
    q.add_argument("--out", type=pathlib.Path)
    q.add_argument("--template", type=pathlib.Path)
    q.set_defaults(fn=cmd_screens)

    p = sub.add_parser("validate-pack")
    p.add_argument("pack_dir", type=pathlib.Path)
    p.add_argument("--write-hash", action="store_true")
    p.set_defaults(fn=cmd_validate_pack)

    p = sub.add_parser("new-pack")
    p.add_argument("pack_id")
    p.add_argument("--sector", required=True)
    p.add_argument("--pattern", required=True)
    p.add_argument("--out", required=True)
    p.set_defaults(fn=cmd_new_pack)

    p = sub.add_parser("diff")
    p.add_argument("old", type=pathlib.Path)
    p.add_argument("new", type=pathlib.Path)
    p.add_argument("--out", type=pathlib.Path)
    p.set_defaults(fn=cmd_diff)

    p = sub.add_parser("drift")
    p.add_argument("app", type=pathlib.Path)
    p.add_argument("generated_dir", type=pathlib.Path)
    p.set_defaults(fn=cmd_drift)

    p = sub.add_parser("totality")
    p.add_argument("app", type=pathlib.Path)
    p.add_argument("--generated", type=pathlib.Path,
                   help="default: <app dir>/generated")
    p.add_argument("--build", type=pathlib.Path,
                   help="default: <app dir>/build (skipped, with a note, if absent)")
    p.set_defaults(fn=cmd_totality)

    p = sub.add_parser("reconcile",
                       help="lift analyst console edits on a deployed app back into the L1 model")
    p.add_argument("app", type=pathlib.Path)
    p.add_argument("--jwa", type=pathlib.Path, help="the exported .jwa (deployed truth)")
    p.add_argument("--instance", help="instance name for the read-only seed/vocabulary leg")
    p.add_argument("--base", help="base model ref when the artefact carries no stamp: "
                                  "a git rev, a path, or a model sha256")
    p.add_argument("--strict-base", action="store_true",
                   help="refuse (exit 3) rather than run in two-way degraded mode")
    p.add_argument("--out", type=pathlib.Path,
                   help="changeset dir (default <app dir>/design/reconcile)")
    p.add_argument("--report-only", action="store_true",
                   help="print findings; write no changeset")
    p.add_argument("--apply", type=pathlib.Path, metavar="CHANGESET",
                   help="apply the accepted items of a ruled changeset to the model")
    p.set_defaults(fn=cmd_reconcile)

    p = sub.add_parser("gate")
    p.add_argument("action", choices=["assemble", "check", "sign", "resolve"])
    p.add_argument("app", type=pathlib.Path)
    p.add_argument("--as", dest="who")
    p.set_defaults(fn=cmd_gate)

    p = sub.add_parser("deploy")
    p.add_argument("app", type=pathlib.Path)
    p.add_argument("--instance", required=True)
    p.add_argument("--instances", type=pathlib.Path)
    p.set_defaults(fn=cmd_deploy)

    p = sub.add_parser("seed"); p.add_argument("app", type=pathlib.Path); p.set_defaults(fn=cmd_seed)

    p = sub.add_parser("test")
    p.add_argument("app", type=pathlib.Path)
    p.add_argument("--instance", help="live instance to run the acceptance scenarios against")
    p.add_argument("--instances", type=pathlib.Path)
    p.add_argument("--api-key", dest="api_key")
    p.add_argument("--feature")
    p.add_argument("--out", type=pathlib.Path,
                   help="where the kit's runner writes its result (default: "
                        "design/acceptance-result.yaml beside the model, where the gate report "
                        "reads it)")
    p.set_defaults(fn=cmd_test)

    p = sub.add_parser("ux-lint")
    p.add_argument("app", type=pathlib.Path)
    p.add_argument("--build", type=pathlib.Path, required=True)
    p.set_defaults(fn=cmd_ux_lint)

    p = sub.add_parser("tracker")
    p.add_argument("--evidence", type=pathlib.Path, default=None,
                   help="evidence repo root (default: the sibling checkout)")
    p.set_defaults(fn=cmd_tracker)

    p = sub.add_parser("method")
    p.add_argument("--evidence", type=pathlib.Path, default=None)
    p.set_defaults(fn=cmd_method)

    p = sub.add_parser("conformance")
    p.add_argument("apps", nargs="+", type=pathlib.Path)
    p.set_defaults(fn=cmd_conformance)

    return ap


def main() -> int:
    args = build_parser().parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
