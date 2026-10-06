#!/usr/bin/env python3
"""compile — Stage G entry: the loss-report refusal in software (UB-11, ex TA-01 T3).

The compile contract (S2C-03 §7 / RUNBOOK-upstream §4): the Layer-1 model is produced
from the signed design, and EVERY design element is either expressed in L1 or listed in
`design/loss-report.yaml` as a NAMED schema gap — what could not be expressed, how it
landed instead, and the schema construct it demands (`feeds`). A silent inexpressible
(dropped, not reported) is the §2.4 failure one level up. This verb makes the refusal
executable (ADR-077: "enforced" means an executed refusal):

  * a non-empty loss report with an UNNAMED gap — empty/missing `what` or `feeds` —
    FAILS with exit 2 naming the entry (COMPILE-LOSS-UNNAMED);
  * a loss entry citing a decision that does not exist, or is not VERIFIED, fails —
    flattening an undecided thing is worse than flattening a decided one;
  * duplicate loss ids fail (the roadmap feed must be addressable);
  * the L1 model must pass `kit validate` (schema + L-rules) — the compile runs it;
  * with --realization, the citation column must be 100% (`citation_check`);
  * INPUT-VS-OUTPUT (13 Aug 2026, verification-seam ruling): every element of the input
    either LANDS in the model, or appears in `losses`, or carries an explicit assumption —
    else the build fails with exit 2 naming the element (COMPILE-INPUT-UNRECONCILED). The
    old contract checked only the AUTHORED loss list, so an element dropped silently AND
    omitted from that list passed the verb whose whole purpose is to prevent exactly that.

The verb VERIFIES the compile contract; authoring the model remains the
`s2c-compile-to-l1` skill's method, now reduced to guidance around this refusal.

    kit compile <app.yaml> [--loss F] [--decisions F] [--realization F] [--no-validate]
"""
from __future__ import annotations

import argparse
import pathlib
import subprocess
import sys

import yaml

HERE = pathlib.Path(__file__).resolve().parent

RULE_UNNAMED = "COMPILE-LOSS-UNNAMED"   # seam-lint-registered rule id (ADR-088)

RULE_UNRECONCILED = "COMPILE-INPUT-UNRECONCILED"

REQUIRED_FIELDS = ("what", "landed_as", "feeds")

# Top-level collections of the L1 model that an input element's `ref` may land in.
MODEL_COLLECTIONS = ("entities", "forms", "lists", "processes", "dashboards", "reports",
                     "vocabularies", "catalog", "queries", "seed", "features",
                     "bespoke_plugins", "interfaces", "roles", "navigation", "requirements")


def _model_index(model: dict) -> dict:
    """collection -> {ids}. Membership is what "landed" means, and nothing more."""
    idx: dict[str, set] = {}
    for coll in MODEL_COLLECTIONS:
        node = model.get(coll)
        if isinstance(node, list):
            idx[coll] = {str(i.get("id")) for i in node if isinstance(i, dict) and i.get("id")}
        elif isinstance(node, dict):
            ids = set()
            for k, v in node.items():
                if isinstance(v, list):
                    ids |= {str(i.get("id")) for i in v if isinstance(i, dict) and i.get("id")}
                else:
                    ids.add(str(k))
            idx[coll] = ids
    return idx


def reconcile_input(inputs: dict, model: dict, loss: dict) -> tuple[list[dict], list[str]]:
    """INPUT-VS-OUTPUT: every input element lands, is recorded as a loss, or is an
    explicit assumption. Anything else is UNRECONCILED and the build fails.

    The hole this closes (S2C-04 v1.1 §11.1, "the compile cannot see an unrecorded loss"):
    the compile verb's only check was over the AUTHORED loss list, so a design element
    dropped silently AND omitted from the loss report passed the verb whose whole purpose
    is to make silent dropping impossible.

    The verdict is deliberately named UNRECONCILED and not DROPPED. A `ref` whose first
    segment is not a model collection — `rules.trigger_dedup`, `params.phone_sla_days` —
    may well have landed inside a guard or a seed row; what the compile can say is that it
    cannot SHOW that it landed and nothing accounts for it. That is the finding, and
    over-claiming it as a drop would be its own kind of dishonesty.
    """
    idx = _model_index(model)
    recorded = set()
    for e in loss.get("losses", []) or []:
        for k in ("decision", "id", "ref", "covers"):
            v = e.get(k)
            for x in ([v] if isinstance(v, str) else (v or [])):
                recorded.add(str(x))
        # a loss whose `what` names the ref verbatim accounts for it too
        recorded.add(str(e.get("what") or ""))

    rows, unreconciled = [], []
    elements = inputs.get("items") or inputs.get("elements") or []
    for i, el in enumerate(elements):
        if not isinstance(el, dict):
            continue
        ref = str(el.get("ref") or el.get("id") or f"items[{i}]")
        verdict = None
        parts = ref.split(".")
        if parts[0] in idx and len(parts) > 1 and parts[1] in idx[parts[0]]:
            verdict = "LANDED"
        elif parts[0] in idx and len(parts) == 1:
            verdict = "LANDED"
        elif ref in recorded or str(el.get("decision") or "\0") in recorded \
                or any(ref in r for r in recorded if r):
            verdict = "RECORDED"
        elif str(el.get("assumption") or "").strip():
            verdict = "ASSUMPTION"
        else:
            verdict = "UNRECONCILED"
            unreconciled.append(
                f"{ref}: the compile cannot show this input element landed in the model, "
                f"and no loss entry and no assumption accounts for it [{RULE_UNRECONCILED}]")
        rows.append({"ref": ref, "verdict": verdict})
    return rows, unreconciled


def _load(p):
    return yaml.safe_load(pathlib.Path(p).read_text(encoding="utf-8")) or {}


def check_loss_report(loss: dict, decisions: dict | None) -> list[str]:
    """Return findings. Empty == every loss is a named, decided, addressable gap."""
    out: list[str] = []
    entries = loss.get("losses", []) or []
    by_id = {d.get("id"): d for d in (decisions or {}).get("decisions", []) or []}

    seen: set[str] = set()
    for i, e in enumerate(entries):
        lid = e.get("id") or f"losses[{i}]"
        if lid in seen:
            out.append(f"{lid}: duplicate loss id — the schema roadmap cannot address it")
        seen.add(lid)
        for f in REQUIRED_FIELDS:
            if not str(e.get(f) or "").strip():
                out.append(f"{lid}: loss entry with no named schema gap — {f!r} is empty; "
                           f"a silent inexpressible is a hard failure [{RULE_UNNAMED}]")
        did = e.get("decision")
        if did and decisions is not None:
            d = by_id.get(did)
            if d is None:
                out.append(f"{lid}: cites {did} which is not in the decision inventory — "
                           f"a loss must trace to a decided thing")
            elif d.get("status") != "VERIFIED":
                out.append(f"{lid}: cites {did} whose status is {d.get('status')} — "
                           f"flattening an undecided thing is refused")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("app", type=pathlib.Path)
    ap.add_argument("--loss", type=pathlib.Path,
                    help="default: <app dir>/design/loss-report.yaml")
    ap.add_argument("--decisions", type=pathlib.Path,
                    help="default: <app dir>/design/decisions.yaml")
    ap.add_argument("--realization", type=pathlib.Path,
                    help="run citation_check against --decisions as part of the compile gate")
    ap.add_argument("--no-validate", action="store_true",
                    help="skip the kit-validate leg (loss-report gate only)")
    ap.add_argument("--input", type=pathlib.Path,
                    help="the design's element declaration for the input-vs-output "
                         "reconciliation; default: <app dir>/design/realization.yaml")
    ap.add_argument("--no-input-check", action="store_true",
                    help="skip the input-vs-output reconciliation (says so out loud)")
    a = ap.parse_args()

    base = a.app.parent
    loss_path = a.loss or base / "design" / "loss-report.yaml"
    dec_path = a.decisions or base / "design" / "decisions.yaml"

    if not loss_path.is_file():
        print(f"compile: no loss report at {loss_path} — an absent report asserts "
              f"ZERO inexpressibles; state that with an empty `losses:` list instead")
        return 3
    decisions = _load(dec_path) if dec_path.is_file() else None
    if decisions is None:
        print(f"compile: no decision inventory at {dec_path}")
        return 3

    findings = check_loss_report(_load(loss_path), decisions)
    for f in findings:
        print(f"  FAIL  {f}")
    if findings:
        print(f"compile: REFUSED — {len(findings)} loss-report finding(s); nothing is "
              f"flattened silently (the loss report IS the schema roadmap feed)")
        return 2

    n = len(_load(loss_path).get("losses", []) or [])
    print(f"compile: loss report OK — {n} named schema gap(s), every one decided and addressable")

    rc = 0

    # ---- input-vs-output reconciliation ----
    in_path = a.input if a.input else base / "design" / "realization.yaml"
    if a.no_input_check:
        print("compile: NOTE — input-vs-output reconciliation SKIPPED by --no-input-check. "
              "This run cannot see an element that was dropped and never recorded.")
    elif not pathlib.Path(in_path).is_file():
        if a.input:
            print(f"compile: no input declaration at {in_path}")
            return 3
        print(f"compile: NOTE — no input declaration at {in_path}, so the input-vs-output "
              f"reconciliation DID NOT RUN. The loss-report gate above is a check over the "
              f"AUTHORED list only; a design element dropped silently and omitted from that "
              f"list is invisible to this run.")
    else:
        if not a.app.is_file():
            print(f"compile: not found: {a.app}")
            return 3
        rows, unreconciled = reconcile_input(_load(in_path), _load(a.app), _load(loss_path))
        for u in unreconciled:
            print(f"  FAIL  {u}")
        landed = len([r for r in rows if r["verdict"] == "LANDED"])
        rec = len([r for r in rows if r["verdict"] == "RECORDED"])
        asm = len([r for r in rows if r["verdict"] == "ASSUMPTION"])
        print(f"compile: input-vs-output — {len(rows)} element(s): {landed} landed · "
              f"{rec} recorded as a loss · {asm} explicit assumption · "
              f"{len(unreconciled)} UNRECONCILED")
        if unreconciled:
            print(f"compile: REFUSED — {len(unreconciled)} input element(s) unaccounted for")
            return 2
    if not a.no_validate:
        if not a.app.is_file():
            print(f"compile: not found: {a.app}")
            return 3
        r = subprocess.run([sys.executable, str(HERE / "validate.py"), str(a.app)])
        if r.returncode != 0:
            print("compile: FAIL — the emitted model does not validate")
            rc = 1
    if a.realization:
        r = subprocess.run([sys.executable, str(HERE / "citation_check.py"),
                            str(a.realization), "--decisions", str(dec_path)])
        if r.returncode != 0:
            print("compile: FAIL — the citation column is not 100%")
            rc = 1
    if rc == 0:
        print("compile: OK — the compile contract holds"
              + ("" if a.no_validate else " (model validates)")
              + (", citation column 100%" if a.realization else ""))
    return rc


if __name__ == "__main__":
    sys.exit(main())
