#!/usr/bin/env python3
"""Scaffold a minimal Layer-1 application model (`kit new`).

Emits a starter `<appId>.app.yaml` — a real, if tiny, model to grow from: one requirement,
one feature, one role, one entity with a generated key, and a create form. Enterprise / DX 9.0
/ Postgres, so no delta rule fires; no config blocks, so no contract check applies.

It is REFUSED by `kit validate`, `kit gen`, the build and the deploy until one question is
answered (METHOD-2026-09-25-12; SDD-11, section 8). The entry `model.interaction_design` is
written as that question: which interaction design, accepted by the owner, is this model
written from? The model names it by its path relative to the model and its SHA-256 checksum,
and the interaction design gate (rule L021 of tools/validate.py, an error in every custody
mode) admits the model only when the named document is there, unchanged, baselined with a
name and a date, covers the goals the model's screens name, and agrees with the model. The
scaffold passes every other layer of `kit validate` (schema · lint · delta · contract) as it
stands; once the question is answered with such a document, it passes the gate too.

Alongside the model it writes a sibling `.kit.yaml` — the build pin + custody policy
(ADR-069). A new app is born `custody: required`: `kit build` / `kit deploy` refuse to
produce or ship an artefact until `design/gate-report.yaml` is GREEN and signed
(`kit gate` … `kit gate sign`). Existing apps default to `stamp`; flipping the new app
down to `stamp` is a one-line, owner-visible commit (DP-2, visibility before blockage).

Usage:
    scaffold_model.py <appId> [--name NAME] [--out FILE]

Exit: 0 written · 1 refused (output exists and --force not given).
"""
from __future__ import annotations

import argparse
import os
import pathlib
import sys

import yaml

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import validate as l1  # for the current schema version (no hardcode → no bump churn)

HEADER = ("# Scaffolded by `kit new` — a minimal Layer-1 model. Grow it, then\n"
          "# `kit validate`. Replace the placeholders; keep ids snake_case.\n"
          "#\n"
          "# ONE QUESTION TO ANSWER FIRST — model.interaction_design. Which interaction design,\n"
          "# accepted by the owner, is this model written from? Name it by its path relative to\n"
          "# this file and its SHA-256 checksum (`shasum -a 256 <the file>`). Until it is answered,\n"
          "# kit validate, kit gen, the build and the deploy refuse this model (rule L021; SDD-11,\n"
          "# The Interaction Design, section 8), in every custody mode. The document is written\n"
          "# from the kit's template, templates/spec/INTERACTION_DESIGN.md.tmpl.\n")

# What the entry holds until the question is answered: the interaction design gate reads it as
# the question unanswered (validate.IXD_QUESTION) and refuses the model on check 1.
QUESTION = {
    "path": f"{l1.IXD_QUESTION}: the interaction design the owner accepted, its path relative to this file",
    "sha256": f"{l1.IXD_QUESTION}: its SHA-256 checksum",
}

KIT_YAML_HEADER = (
    "# Written by `kit new` — the build pin + custody policy for this app (ADR-069).\n"
    "#\n"
    "# custody: required — a NEW app refuses UNGATED generation and deploy. `kit build`\n"
    "#   and `kit deploy` stay blocked until design/gate-report.yaml is GREEN and signed:\n"
    "#     kit gate <app>.app.yaml                    # assemble from the real gate exits\n"
    "#     kit gate sign <app>.app.yaml --as <name>   # signer must not be a model author\n"
    "#   To adopt the existing-app posture instead, set `custody: stamp` — builds proceed\n"
    "#   and every artefact is visibly marked UNGATED. That change is a per-app, owner-\n"
    "#   visible commit (DP-2: visibility before blockage).\n"
    "#\n"
    "# generators — the pinned plugin library `kit build` resolves L2->L3 against. The pin\n"
    "#   is version-matched at build time (build_app.py); an unset version fails closed.\n"
)

REGISTRY_TODO = "TODO-set-registry-version"


def resolve_registry_version() -> str:
    """Best-effort read of registry_version from the pinned plugin library
    ($JOGET_PLUGINS_HOME/registry.yaml), so the scaffold is born pinned to the library it
    was generated against. Falls back to a loud TODO when the library is not resolvable at
    scaffold time — build_app.py's version-match refusal then makes the unset pin fail
    closed rather than silently building against whatever happens to be on PATH."""
    home = os.environ.get("JOGET_PLUGINS_HOME")
    if not home:
        return REGISTRY_TODO
    reg = pathlib.Path(os.path.expanduser(home)) / "registry.yaml"
    if not reg.exists():
        return REGISTRY_TODO
    try:
        found = (yaml.safe_load(reg.read_text(encoding="utf-8")) or {}).get("registry_version")
    except Exception:
        return REGISTRY_TODO
    return str(found) if found else REGISTRY_TODO


def kit_yaml_doc() -> dict:
    """The sibling `.kit.yaml`: custody policy + build pin. Kept out of the app model on
    purpose — custody and the generator pin are build-environment facts, not Layer-1."""
    return {
        "custody": "required",
        "kit_version": l1.schema_version(),
        "generators": {
            "registry_version": resolve_registry_version(),
            "path": "reference-app/generators",
        },
    }


def scaffold(app_id: str, name: str) -> dict:
    return {
        "model": {"schema_version": l1.schema_version(), "spec_version": "0.1.0",
                  "status": "draft", "authors": ["TODO"],
                  "interaction_design": dict(QUESTION)},
        "app": {"id": app_id, "name": name,
                "platform": {"dx": "9.0", "edition": "enterprise", "db": "postgres"}},
        "requirements": [
            {"id": "FR-001", "text": "TODO: the first requirement.", "source": "TODO"}],
        "features": [{"id": "F01", "name": "Core", "requirements": ["FR-001"]}],
        "roles": [{"id": "user", "name": "User"}],
        "entities": [{
            "id": "thing", "name": "Thing", "kind": "main", "table": "thing", "feature": "F01",
            "pk": {"strategy": "id_generator", "format": "TH-??????", "attr": "thing_no"},
            "attributes": [
                {"id": "thing_no", "type": "string", "length": 12,
                 "description": "Business key, generated."},
                {"id": "title", "type": "string", "required": True, "length": 120}]}],
        "forms": [{
            "id": "frmThing", "name": "Thing", "entity": "thing", "purpose": "create",
            "feature": "F01",
            "persona": "user",   # U008 (CTX-01 Q1): who uses this screen
            "trigger": {"kind": "menu",   # U008 (CTX-01 Q2): how it is reached
                        "justification": "reached from the app menu (scaffold default; refine per UX-01 CTX-01)"},
            "sections": [{"id": "sec_main", "label": "Thing", "columns": 2, "fields": [
                {"attr": "thing_no", "control": "id_generator", "readonly": True},
                {"attr": "title", "provenance": "entered",   # U002 (PRE-01/02): value fields declare provenance
                 "justification": "captured from the user at create time (scaffold default)"}]}],
            "permissions": {"roles": ["user"]}}],
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("app_id")
    ap.add_argument("--name")
    ap.add_argument("--out", type=pathlib.Path)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    out = args.out or pathlib.Path(f"{args.app_id}.app.yaml")
    if out.exists() and not args.force:
        print(f"refusing to overwrite {out} (pass --force)")
        return 1
    doc = scaffold(args.app_id, args.name or args.app_id)
    body = yaml.safe_dump(doc, sort_keys=False, default_flow_style=False,
                          allow_unicode=True, width=4096)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(HEADER + body, encoding="utf-8", newline="\n")
    print(f"scaffolded {out} — now run: kit validate {out}")
    print("  ? model.interaction_design is written as a question: name the interaction design the "
          "owner accepted, by its path and SHA-256 checksum. Until it is answered, the model is "
          "refused (rule L021; SDD-11, section 8).")

    # Sibling .kit.yaml — the pin + custody policy (ADR-069). Never clobber an existing
    # one: an app already in flight may carry a tuned custody posture we must not reset.
    kit_out = out.parent / ".kit.yaml"
    if kit_out.exists():
        print(f"  · kept existing {kit_out} (custody posture unchanged)")
    else:
        kit_body = yaml.safe_dump(kit_yaml_doc(), sort_keys=False,
                                  default_flow_style=False, allow_unicode=True, width=4096)
        kit_out.write_text(KIT_YAML_HEADER + kit_body, encoding="utf-8", newline="\n")
        print(f"  + {kit_out} (custody: required — gate the app before you build or deploy)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
