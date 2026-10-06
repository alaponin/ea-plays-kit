#!/usr/bin/env python3
"""projection_trial.py — the kit's projections tried as a whole, before anything is written (ADR-107).

Two defects found by building two applications (a delivery's hand-off of 5 October 2026, items 1 and
4) had one cause: the kit ran its projectors one at a time, each into the output folder, and
nothing asked whether all of them could project the model before the first one wrote.

  * `kit validate` admitted models that `kit gen` refused: one application validated
    with exit 0 and its form projector refused 28 constructs (one delivery's build); the trial
    of another application's model refused 152. The validator never ran the projectors' checks, so
    "admitted" did not mean "can be generated".
  * `kit gen all` wrote part of a build while the form projector refused: 38 files were written
    in one delivery's run, with no forms among them.

This module is the one place that runs every projector of `kit gen` over a model, exactly as
`kit gen` runs them (the same scripts, the same arguments, the same order), into a folder of its
own. `kit gen` writes into the output folder only what a trial in which every projector
succeeded wrote; `kit validate` reports, as errors, the refusals the projectors print.

The projectors stay as they are: each still validates its input, refuses with a sentence and
emits nothing on a refusal (docs/DEVELOPER-GUIDE.md section 7). The refusals are read from what
each prints under its header lines (`PROJECT: <n> error(s)`, the line every projector of the kit
prints when it refuses), so the validator states exactly the sentences `kit gen` states.
"""
from __future__ import annotations

import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent

# The projectors `kit gen` runs, in the order `kit gen all` runs them. tools/kit.py reads this map
# for its verb's choices, so the trial and the verb can never run different projectors.
GEN_SCRIPTS = {"forms": "project_forms.py", "datalists": "project_datalists.py",
               "reports": "project_reports.py", "seed": "project_seed.py",
               "userview": "project_userview.py", "dashboards": "project_dashboards.py",
               "workflow": "project_workflow.py", "lifecycle": "project_lifecycle.py",
               "views": "project_views.py"}
PER_FEATURE = {"forms", "datalists", "reports"}
# A projector's header line: SCHEMA, LINT, DELTA/CONTRACT, PROJECT, LIFECYCLE, then what follows.
HEADER = re.compile(r"^([A-Z][A-Z/]*):\s*(.*)$")


class Result:
    """One projector's run: its target, its exit code, and every line it printed."""

    def __init__(self, target: str, code: int, output: str):
        self.target, self.code, self.output = target, code, output

    @property
    def refusals(self) -> list[str]:
        """The sentences the projector refused with: the `  - ` lines under a header line that
        counts errors (`PROJECT: 146 error(s) — nothing emitted`, `LIFECYCLE: 1 error(s) —
        refusing to project`, and the schema and lint headers the projectors print before they
        project), or the `PROJECT:` line itself where the refusal is written on it (the userview
        projector, a list of values). A projector that failed in another way is reported by its
        exit code and its last line, so that a failure is never read as a success."""
        if self.code == 0:
            return []
        lines = self.output.splitlines()
        out, under = [], False
        for ln in lines:
            m = HEADER.match(ln)
            if m:
                rest = m.group(2).strip()
                under = "error(s)" in rest
                if not under and m.group(1) == "PROJECT" and rest:
                    out.append(rest)
                continue
            if under and ln.startswith("  - "):
                out.append(ln[4:])
            elif under and not ln.startswith("  "):
                under = False
        if not out:
            last = next((ln for ln in reversed(lines) if ln.strip()), "(it printed nothing)")
            out.append(f"the projector exited {self.code}: {last.strip()}")
        return out


def run_all(app, out, custody: str = "UNGATED", feature: str | None = None,
            fixture=None, targets=None) -> list[Result]:
    """Run each projector `kit gen` runs for `targets` (default: all) over `app` into `out`, as
    `kit gen` runs it, capturing what each prints. Every projector runs, so that every refusal
    is found in one pass."""
    results = []
    for t in (targets or list(GEN_SCRIPTS)):
        extra = (["--feature", feature] if feature and t in PER_FEATURE else []) \
            + (["--fixture", str(fixture)] if fixture and t == "seed" else [])
        cmd = [sys.executable, str(HERE / GEN_SCRIPTS[t]), str(app), "--out", str(out),
               "--custody", custody, *extra]
        r = subprocess.run(cmd, capture_output=True, text=True)
        results.append(Result(t, r.returncode, r.stdout + r.stderr))
    return results


def refusals(app, custody: str = "UNGATED") -> list[tuple[str, str]]:
    """(projector, sentence) for every refusal of every projector of `kit gen all` over `app`,
    tried in a folder of its own that is removed afterwards. An empty list: `kit gen all` would
    project the model."""
    trial = pathlib.Path(tempfile.mkdtemp(prefix="kit-projection-trial-"))
    try:
        return [(r.target, s) for r in run_all(app, trial / "gen", custody) for s in r.refusals]
    finally:
        shutil.rmtree(trial, ignore_errors=True)


def first_nonzero(results: list[Result]) -> int:
    """The exit code `kit gen` has always returned: the last projector's code that was not 0."""
    rc = 0
    for r in results:
        rc = r.code or rc
    return rc


def publish(staged: pathlib.Path, out: pathlib.Path) -> None:
    """Copy every file the trial wrote into `out`, keeping its place; nothing in `out` is removed
    (no projector removes anything from its output folder either)."""
    for p in sorted(staged.rglob("*")):
        if p.is_file():
            dest = out / p.relative_to(staged)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, dest)


def say(results: list[Result], staged: pathlib.Path, out) -> None:
    """Print what each projector printed, naming the output folder where it named the trial's."""
    for r in results:
        text = r.output.replace(str(staged), str(pathlib.Path(out)))
        sys.stdout.write(text if text.endswith("\n") or not text else text + "\n")
    sys.stdout.flush()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: projection_trial.py <app.yaml> — print every refusal of kit gen all")
    found = refusals(sys.argv[1])
    for t, s in found:
        print(f"  - {t}: {s}")
    print(f"{len(found)} refusal(s)")
    sys.exit(2 if found else 0)
