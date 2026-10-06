#!/usr/bin/env python3
"""build_app.py — the one pinned build: Layer-2 specs -> Joget JSON -> .jwa,
using the generator set PINNED in .kit.yaml (never an ad-hoc fork path).

It resolves the generator library from $JOGET_PLUGINS_HOME (or --plugins-home),
verifies that library's registry_version matches the pin in .kit.yaml, then runs
the neutral generators over the projected Layer-2 specs and packages the result.
If the version does not match, or the library is not where the pin says, the build
FAILS — that refusal is the pin (it stops the C2 "generators only in an untracked
fork" risk from recurring).

    build_app.py --model taxRegistration.app.yaml \
        --app taxRegistration --name "Tax Registration" --out build/out \
        --forms specs/F01/forms specs/F02/forms \
        --datalists specs/F01/datalists \
        --userview specs/reg.uv.yml [--dashboard specs/reg.dash.yml] \
        [--workflow specs/reg.wf.yml] [--kit-yaml .kit.yaml] [--plugins-home DIR]

Before anything else it runs the interaction design gate (rule L021 of tools/validate.py;
SDD-11 section 8; METHOD-2026-09-25-12) on the model `--model` names, and refuses the build when
the gate refuses the model — in every custody mode, with nothing to turn it off. It then refuses
any spec it is given that was not projected from that model: every `*.spec.yml` of the directories
it is given, and the userview, dashboard and workflow specs, must carry the model's SHA-256 in
their `# source_sha256:` provenance line. A spec written by hand carries none and is refused. The
build writes, beside the archive, `<app>.admission.yaml`: which model and which interaction design
the archive was admitted from, with their checksums and the archive's. deploy_dx9.py deploys an
archive only with that record, and runs the gate again on the model it names.

Then deploy the produced <out>/<app>.jwa with deploy_dx9.py (see DEPLOY.md)."""
from __future__ import annotations
import argparse
import datetime as _dt
import hashlib
import os
import pathlib
import subprocess
import sys

try:
    import yaml
except ImportError:
    sys.exit("build_app.py needs pyyaml (pip install pyyaml)")


def die(msg: str):
    sys.exit(f"[build] FAIL: {msg}")


HERE = pathlib.Path(__file__).resolve().parent
ADMISSION_SUFFIX = ".admission.yaml"     # <app>.admission.yaml beside <app>.jwa


def _spec_files(dirs: list, files: list) -> list:
    """Every spec the generators will read: the `*.spec.yml` directly in each directory (as the
    generators list them), and the single spec files."""
    out = []
    for d in dirs:
        p = pathlib.Path(d)
        if p.is_dir():
            out += sorted(x for x in p.iterdir() if x.is_file() and x.name.endswith(".spec.yml"))
    out += [pathlib.Path(f) for f in files if f]
    return out


def _source_sha(spec: pathlib.Path) -> str | None:
    """The model checksum a projected spec's provenance header carries, or None."""
    try:
        with open(spec, encoding="utf-8") as fh:
            for i, line in enumerate(fh):
                if line.startswith("# source_sha256:"):
                    return line.split(":", 1)[1].strip()
                if i > 40:
                    break
    except OSError:
        return None
    return None


def admit(a) -> dict:
    """The interaction design gate, first; then every spec given must come from that model.
    Returns what the admission record needs. Refuses (exits) otherwise."""
    sys.path.insert(0, str(HERE))
    import validate
    if validate.admit_or_refuse(a.model, "[build]") != 0:
        sys.exit(2)
    model = pathlib.Path(a.model).resolve()
    model_sha = hashlib.sha256(model.read_bytes()).hexdigest()
    specs = _spec_files([*a.forms, *a.datalists, *a.reports],
                        [a.userview, a.dashboard, a.workflow])
    foreign = [(s, _source_sha(s)) for s in specs if _source_sha(s) != model_sha]
    if foreign:
        lines = "\n    ".join(f"{s}: {'no provenance line' if sha is None else 'projected from ' + sha}"
                              for s, sha in foreign[:12])
        more = f"\n    … and {len(foreign) - 12} more" if len(foreign) > 12 else ""
        die(f"{len(foreign)} of the {len(specs)} spec(s) given were not projected from the admitted "
            f"model {model.name} (SHA-256 {model_sha}) — refusing. A build is made only from the "
            f"specs `kit gen` projected from the model the interaction design gate admitted:\n    "
            f"{lines}{more}")
    doc = yaml.safe_load(model.read_text(encoding="utf-8")) or {}
    entry = (doc.get("model") or {}).get("interaction_design") or {}
    ixd = (model.parent / str(entry.get("path"))).resolve()
    return {"model": str(model), "model_sha256": model_sha,
            "interaction_design": str(ixd), "interaction_design_sha256": str(entry.get("sha256")),
            "specs": len(specs)}


def write_admission(out: pathlib.Path, app: str, jwa: pathlib.Path, adm: dict) -> pathlib.Path:
    record = {"admission": {
        "rule": "L021, the interaction design gate (SDD-11 section 8); tools/validate.py",
        "admitted_at": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "app": app,
        "jwa": jwa.name,
        "jwa_sha256": hashlib.sha256(jwa.read_bytes()).hexdigest(),
        "model": adm["model"],
        "model_sha256": adm["model_sha256"],
        "interaction_design": adm["interaction_design"],
        "interaction_design_sha256": adm["interaction_design_sha256"],
        "specs_checked": adm["specs"],
    }}
    path = out / f"{app}{ADMISSION_SUFFIX}"
    path.write_text("# Written by build_app.py — do not hand-edit. deploy_dx9.py deploys the archive\n"
                    "# only with this record, and runs the interaction design gate again on the\n"
                    "# model it names (METHOD-2026-09-25-12).\n"
                    + yaml.safe_dump(record, sort_keys=False, allow_unicode=True),
                    encoding="utf-8", newline="\n")
    return path


# The one date every member of an archive carries: the first moment the zip format can store.
ARCHIVE_TIME = (1980, 1, 1, 0, 0, 0)


def fix_archive_times(jwa: pathlib.Path) -> None:
    """Rewrite the archive with every member stamped ARCHIVE_TIME (ADR-108; a delivery's hand-off of
    6 October 2026, item 6; C-255 F-10). The pinned build_jwa.py writes each member with the
    clock's time (zipfile `writestr` with a name), so two builds of one model never gave the same
    bytes: BUILD-A's two archives differed in that header alone, and were the same once it was
    fixed (a04_compare.out). The build promises the same output for the same input
    (docs/DEVELOPER-GUIDE.md section 1), and the admission record names the archive's checksum,
    so the time is fixed here, before that checksum is taken. Names, order, contents,
    compression and attributes are kept; the generator is not changed."""
    import io
    import zipfile
    if not zipfile.is_zipfile(jwa):
        return                          # nothing to fix: a library's stand-in that writes no archive
    src = jwa.read_bytes()
    buf = io.BytesIO()
    with zipfile.ZipFile(io.BytesIO(src)) as zin, zipfile.ZipFile(buf, "w") as zout:
        for info in zin.infolist():
            fixed = zipfile.ZipInfo(info.filename, date_time=ARCHIVE_TIME)
            fixed.compress_type = info.compress_type
            fixed.external_attr = info.external_attr
            fixed.create_system = info.create_system
            fixed.comment = info.comment
            zout.writestr(fixed, zin.read(info.filename))
    jwa.write_bytes(buf.getvalue())


def run(argv: list[str]):
    if subprocess.run(argv).returncode:
        die("generator failed: " + " ".join(map(str, argv)))


def resolve_generators(kit_yaml: str, plugins_home: str | None) -> pathlib.Path:
    """Resolve + version-check the pinned generator set. This IS the pin."""
    ky = pathlib.Path(kit_yaml)
    if not ky.exists():
        die(f".kit.yaml not found: {ky} (the build must be pinned)")
    pin = (yaml.safe_load(ky.read_text()) or {}).get("generators") or {}
    want = str(pin.get("registry_version", ""))
    home = plugins_home or os.environ.get("JOGET_PLUGINS_HOME")
    if not home:
        die("plugins library unknown: pass --plugins-home or set JOGET_PLUGINS_HOME "
            "(the build never reaches into an ad-hoc fork path)")
    home = pathlib.Path(os.path.expanduser(home))
    reg = home / "registry.yaml"
    if not reg.exists():
        die(f"not a plugins library (no registry.yaml): {home}")
    found = str((yaml.safe_load(reg.read_text()) or {}).get("registry_version", ""))
    if found != want:
        die(f"generator version mismatch: .kit.yaml pins {want!r}, {home} is {found!r} — refusing")
    gen = home / pin.get("path", "reference-app/generators")
    if not gen.exists():
        die(f"pinned generator path missing: {gen}")
    print(f"[build] generators: {gen}  (pinned registry_version {want})")
    return gen


BUILD_ARTEFACTS = (".json", ".jwa")


def prior_build_artefacts(out: pathlib.Path) -> list[pathlib.Path]:
    """What makes a build NOT the first one. The bootstrap's single objective condition —
    a question about the filesystem, not about intent."""
    if not pathlib.Path(out).is_dir():
        return []
    return sorted(p for p in pathlib.Path(out).rglob("*")
                  if p.is_file() and p.suffix in BUILD_ARTEFACTS)


def bootstrap_first_build(app_dir: pathlib.Path, out: pathlib.Path, a, gate_report) -> None:
    """CH-01 bootstrap (KR-15) — the first build of a `custody: required` app.

    The deadlock this resolves is not a policy inconvenience, it is an unsatisfiable
    constraint: `build_app` refuses to build a required app until the gate is GREEN, and the
    gate cannot be green until a build exists, because two of its required constituents
    (`ux_lint`, `totality`) read `build/`. On a first build there is no ordering that
    satisfies both. The escape that was refused — dropping the .kit.yaml version pin — is not
    taken here and the pin is untouched: the pin answers "which generators", the gate answers
    "was this reviewed", and trading one for the other pays a debt with a different debt.

    What the bootstrap does and does not do. It permits exactly one artefact to exist: the
    first `build/`, so the gate has something to read and can then return a verdict that means
    something. It does NOT make the app gated — `gate_report.resolve()` still returns UNGATED,
    every projected spec keeps its `# custody: UNGATED` header, every form and userview keeps
    its `[UNGATED build]` description prefix, and `kit gen` and `kit deploy` refuse exactly as
    before. The seal that matters is on the deploy, and this does not touch it.

    Its tooth is the condition above: once ANY build artefact exists the flag is refused, so
    it cannot become a general way around the gate. And it records itself — a build produced
    without a gate leaves a permanent, machine-readable statement that it was.
    """
    prior = prior_build_artefacts(out)
    if prior:
        die(f"--first-build refused: {out} already holds {len(prior)} build artefact(s) "
            f"(e.g. {prior[0].name}). The bootstrap exists only for the build that cannot "
            f"exist yet; this app HAS been built, so the gate can read it — run `kit gate` "
            f"and fix what it reports.")

    ky = pathlib.Path(a.kit_yaml).resolve()
    report = app_dir / "design" / "gate-report.yaml"
    verdict = "absent (no gate-report has been assembled)"
    if report.is_file():
        rep = (yaml.safe_load(report.read_text(encoding="utf-8")) or {}).get("gate_report") or {}
        verdict = str(rep.get("verdict") or "unknown")

    record = {
        "first_build": {
            "rule": "CH-01 bootstrap (KR-15)",
            "recorded_at": _dt.datetime.now().isoformat(timespec="seconds"),
            "app": a.app,
            "out": str(out),
            "custody_mode": "required",
            "custody_at_build": "UNGATED",
            "gate_verdict_at_build": verdict,
            "kit_yaml_sha256": hashlib.sha256(ky.read_bytes()).hexdigest(),
            "spec_inputs": sorted(map(str, [*a.forms, *a.datalists, *a.reports,
                                            *filter(None, (a.userview, a.dashboard, a.workflow))])),
            "why": ("The gate's ux_lint and totality constituents read build/; on a first "
                    "build there is none, so the required set could not go green by any "
                    "ordering. This build was produced to make the gate computable."),
            "what_this_does_not_grant": (
                "Not custody. This build is UNGATED: kit gen and kit deploy still refuse, "
                "the specs keep their UNGATED provenance headers, and the artefacts keep "
                "their [UNGATED build] description prefix. Assemble the gate against this "
                "build, read it, and build again normally once it is green and signed."),
        }
    }
    (app_dir / "design").mkdir(parents=True, exist_ok=True)
    (app_dir / "design" / "first-build.yaml").write_text(
        "# Written by `build_app --first-build` — do not hand-edit. A build produced without\n"
        "# a gate says so here, permanently (CH-01 bootstrap, KR-15).\n"
        + yaml.safe_dump(record, sort_keys=False, allow_unicode=True),
        encoding="utf-8", newline="\n")
    print("[build] CH-01 BOOTSTRAP (KR-15): first build of a custody:required app, produced "
          "UNGATED so the gate can read it.")
    print(f"[build] recorded in {app_dir / 'design' / 'first-build.yaml'} — this build is NOT "
          f"gated and does not deploy.")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", required=True,
                    help="the application model the specs were projected from; the interaction "
                         "design gate runs on it before anything else, and every spec given must "
                         "carry its SHA-256 (METHOD-2026-09-25-12)")
    ap.add_argument("--app", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--forms", nargs="*", default=[], help="one or more form-spec dirs")
    ap.add_argument("--datalists", nargs="*", default=[], help="one or more datalist-spec dirs")
    ap.add_argument("--reports", nargs="*", default=[], help="one or more report-spec dirs")
    ap.add_argument("--userview")
    ap.add_argument("--dashboard")
    ap.add_argument("--workflow")
    ap.add_argument("--kit-yaml", default=".kit.yaml")
    ap.add_argument("--plugins-home")
    ap.add_argument("--first-build", action="store_true",
                    help="CH-01 bootstrap (KR-15): produce the FIRST build of a custody:required "
                         "app, so the gate's build-reading constituents (ux_lint, totality) have "
                         "something to read. Refused once any build artefact exists. Grants no "
                         "custody — gen and deploy still refuse — and records itself in "
                         "design/first-build.yaml.")
    a = ap.parse_args()

    adm = admit(a)                      # L021 first: nothing is built from a model it refuses
    gen = resolve_generators(a.kit_yaml, a.plugins_home)
    # CH-01 custody: a required-mode app refuses to build without a green gate-report.
    _mode = (yaml.safe_load(pathlib.Path(a.kit_yaml).read_text()) or {}).get("custody", "stamp")
    out = pathlib.Path(a.out)
    if _mode == "required":
        import gate_report
        app_dir = pathlib.Path(a.kit_yaml).resolve().parent
        if gate_report.resolve_dir(app_dir) == "UNGATED":
            if not a.first_build:
                die("custody:required app is UNGATED (no fresh, green, signed gate-report) — "
                    "run `kit gate`. If this app has NEVER been built, the gate cannot go green "
                    "by any ordering — its ux_lint and totality constituents read build/ — so "
                    "re-run with --first-build (CH-01 bootstrap, KR-15).")
            bootstrap_first_build(app_dir, out, a, gate_report)
    elif a.first_build:
        die("--first-build is meaningless under custody:stamp — a stamp-mode app never refuses "
            "to build, so there is no deadlock to break. Remove the flag.")
    for sub in ("forms", "datalists", "reports", "userviews", "dashboards", "workflow"):
        (out / sub).mkdir(parents=True, exist_ok=True)

    for d in a.forms:
        run(["python3", str(gen / "gen_forms.py"), d, str(out / "forms")])
    for d in a.datalists:
        run(["python3", str(gen / "gen_datalists.py"), d, str(out / "datalists")])
    for d in a.reports:                       # reports before the userview: it inlines their menus
        run(["python3", str(gen / "gen_reports.py"), d, str(out / "reports")])
    if a.dashboard:                           # dashboards before the userview: it inlines their charts
        run(["python3", str(gen / "gen_dashboards.py"), a.dashboard, str(out / "dashboards")])
    if a.userview:
        run(["python3", str(gen / "gen_userview.py"), a.userview,
             str(out / "userviews"), str(out / "reports"), str(out / "dashboards")])
    if a.workflow:
        run(["python3", str(gen / "gen_workflow.py"), a.workflow, str(out / "workflow"), a.app])

    # WP-B / ADR-070: the A-series artefact lint over the just-generated JSON. A build must
    # not ship a UX violation the model was clean of (RC-3): required -> fail, stamp -> warn.
    uxl = pathlib.Path(__file__).resolve().parent / "ux_lint.py"
    if uxl.exists() and subprocess.run([sys.executable, str(uxl), os.devnull, "--build", str(out)]).returncode:
        if _mode == "required":
            die("ux-lint found error-class UX violations in the generated build — refusing (custody: required).")
        print("[build] WARNING: ux-lint findings above — custody:stamp, proceeding, but this build is not clean.")

    jwa = out / f"{a.app}.jwa"
    run(["python3", str(gen / "build_jwa.py"), str(out), a.app, a.name, str(jwa)])
    fix_archive_times(jwa)              # ADR-108: the same model builds the same archive, byte for byte
    rec = write_admission(out, a.app, jwa, adm)
    print(f"[build] admission recorded -> {rec}")
    print(f"[build] OK -> {jwa}")


if __name__ == "__main__":
    main()
