#!/usr/bin/env python3
"""ux_lint.py — the A-series: artefact lint over generated Joget JSON (WP-B / R2, ADR-070).

Every other kit check reads the L1 model; the generators (gen_userview / gen_forms) were
observed introducing UX violations AFTER the gates — a dead selection column, a dropped
storeValue (RCA RC-3). This lint reads the EMITTED JSON in a build dir, with the model
beside it, and fails on the corruption / integrity class. Seed rules A001–A006 are the six
earlier-exploration failures; error-severity is limited to that class; the family grows by the §12.3
ritual. It is a constituent of the gate-report and runs in build_app.py after generation.

    ux_lint.py <app.yaml> --build <build_dir>

Exit: 0 clean · 1 error-class finding(s).
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("ux_lint.py needs pyyaml (pip install pyyaml)")

SECRET_KEY_RE = re.compile(r"(api[_-]?key|secret|password|token|credential)", re.I)
ENV_REF_RE = re.compile(r"^\$\{env:[A-Z0-9_]+\}$")


def elements(node):
    """Yield every dict carrying a Joget className (element / menu), depth-first."""
    if isinstance(node, dict):
        if "className" in node:
            yield node
        for v in node.values():
            yield from elements(v)
    elif isinstance(node, list):
        for v in node:
            yield from elements(v)


def json_files(build: pathlib.Path, *subdirs):
    for sub in subdirs:
        d = build / sub
        if d.is_dir():
            yield from sorted(d.glob("*.json"))


class UxLint:
    def __init__(self, model: dict, build: pathlib.Path):
        self.model = model or {}
        self.build = build
        self.errors: list[str] = []
        self.warns: list[str] = []

    def err(self, rule, where, msg):
        self.errors.append(f"[{rule}] {where}: {msg}")

    # ---- A001 — the dead selection column (#3 · STA-01/05; L3 mirror of C1) ----
    def a001_dead_selection(self):
        for jf in json_files(self.build, "userviews"):
            doc = json.loads(jf.read_text(encoding="utf-8"))
            for el in elements(doc):
                cn = el["className"]
                if "CrudMenu" not in cn and "DataListMenu" not in cn:
                    continue
                p = el.get("properties", {})
                sel = (p.get("selectionType") or "").strip()
                cb = (p.get("checkboxPosition") or "").strip()
                if not sel and not cb:
                    continue                                    # no selection column — fine
                consumes = p.get("list-showDeleteButton") == "yes" or bool(p.get("bulkActions"))
                if not consumes:
                    self.err("A001", f"{jf.name}#{p.get('customId') or p.get('id')}",
                             f"{cn.split('.')[-1]} emits a selection column (selectionType={sel!r}) but "
                             f"has no selection-consuming action (delete off, no bulk) — a dead checkbox")

    # ---- A007 — an application nobody can use (found 2026-08-02 by the owner) ---------
    def a007_unusable_userview(self):
        """Every emitted userview must let a person CREATE something and OPEN something.

        Registration shipped fifteen times with a green gate, a green ux-lint and 11/11
        acceptance, and a human could do neither: all fifteen list menus were read-only
        DataListMenus (no row opens) and all five FormMenus carried readonly="true" (nothing
        submits). The acceptance suite could not see it — it drives the data API, which is a
        different door from the screen.

        The lesson this rule encodes is narrow and worth stating: the A-series was written to
        catch artefacts that are CORRUPT, and every check the kit had asked whether a thing was
        well-formed. Nothing asked whether the assembled application was REACHABLE. A dead
        checkbox column (A001) was a finding; an application where no record can be opened at
        all was clean.

        Two errors, and the second is narrower than the obvious version of it:
          NO OPENABLE SURFACE — the userview lists records (DataListMenu) and carries no CrudMenu
            at all, so no listed record can ever be opened. Always an error.
          EVERY FORM MENU IS READONLY — the userview declares FormMenus, which exist to let a
            person enter something, and not one of them accepts input.
        What is deliberately NOT an error: a userview with no FormMenu at all. An app whose
        records enter only through an engine or an audited API — a reference app's case worklists are
        exactly this — has no manual creation surface by design, and demanding one would be the
        lint inventing a requirement. The check fires on a DECLARED entry point that cannot be
        used, not on the absence of one.
        A userview that is deliberately a read-only console (a public register viewer, a
        dashboard shell) declares `x-read-only: true` on its navigation block and is exempt —
        an exemption that must be written down is the point.
        """
        nav = (self.model.get("navigation") or {})
        if nav.get("x-read-only"):
            return
        for jf in json_files(self.build, "userviews"):
            doc = json.loads(jf.read_text(encoding="utf-8"))
            forms, cruds, lists = [], [], []
            for el in elements(doc):
                cn, p = el["className"], el.get("properties", {})
                if cn.endswith(".FormMenu"):
                    forms.append(p)
                elif cn.endswith(".CrudMenu"):
                    cruds.append(p)
                elif cn.endswith(".DataListMenu"):
                    lists.append(p)
            if lists and not cruds:
                self.err("A007", jf.name,
                         f"no openable surface: {len(lists)} list menu(s) and no CrudMenu — no "
                         f"listed record can be opened, so every worklist is a dead end")
            # a FormMenu is read-only as the platform reads it, "Yes" (FormMenu, Joget DX 9.0.7),
            # which gen_userview writes since METHOD-2026-09-26-02; "true", which it wrote
            # before, is counted too, as the emission the lint was written against
            if forms and all((p.get("readonly") or "").strip().lower() in ("true", "yes")
                             for p in forms):
                self.err("A007", jf.name,
                         f"all {len(forms)} form menu(s) are readonly — a form menu exists to let "
                         f"a person enter something, and not one of them accepts input")

    # ---- A002 — smart_search wiring (#1 · IDR-01/04; L3 mirror of C3) ----------
    def a002_smart_search(self):
        for jf in json_files(self.build, "forms"):
            doc = json.loads(jf.read_text(encoding="utf-8"))
            field_ids = {el.get("properties", {}).get("id") for el in elements(doc)
                         if el.get("properties", {}).get("id")}
            for el in elements(doc):
                if "SmartSearch" not in el["className"]:
                    continue
                p = el.get("properties", {})
                eid = p.get("id")
                if not (p.get("storeValue") or "").strip():
                    self.err("A002", f"{jf.name}#{eid}",
                             "SmartSearchElement storeValue is empty — the picked id is stored nowhere")
                populate = (p.get("populate") or "").strip()
                if populate:
                    for pair in populate.split(","):
                        pair = pair.strip()
                        if ":" not in pair:
                            self.err("A002", f"{jf.name}#{eid}", f"populate entry {pair!r} is not src:dst")
                            continue
                        dst = pair.split(":", 1)[1].strip()
                        if dst and field_ids and dst not in field_ids:
                            self.err("A002", f"{jf.name}#{eid}",
                                     f"populate target {dst!r} is not a field id on this form")

    # ---- A003 — a literal secret in emitted JSON (invariant 8; L3 mirror of D1) -
    def a003_secrets(self):
        def scan(node, where):
            if isinstance(node, dict):
                for k, v in node.items():
                    if isinstance(v, str):
                        if SECRET_KEY_RE.search(k) and not ENV_REF_RE.match(v):
                            self.err("A003", where,
                                     f"key '{k}' holds a literal secret-shaped value in emitted JSON")
                    else:
                        scan(v, where)
            elif isinstance(node, list):
                for v in node:
                    scan(v, where)
        for jf in json_files(self.build, "forms", "userviews", "datalists", "reports", "dashboards"):
            scan(json.loads(jf.read_text(encoding="utf-8")), jf.name)

    # ---- A006 — a declared uniqueness with no realized enforcement in the build (#4/#5 ·
    #      ADR-072; the L3 corner of D-013). Lands with WP-H's unique-guard. -------------
    def a006_uniqueness_enforced(self):
        entities = {e["id"]: e for e in self.model.get("entities", [])}
        need = set()   # entities whose declared uniqueness must be enforced somewhere
        for eid, e in entities.items():
            # detection-enforced uniqueness (ADR-076 §6 / WP-2 step 4) is WATCHED, not guarded —
            # project_forms emits no guard for it, so it must not be expected here. Only
            # guard/validator uniqueness, or a bare attribute-level `unique` NOT covered by a
            # detection declaration, requires a realized guard.
            detection_attrs = set()
            guard_uniq = False
            for u in (e.get("uniqueness") or []):
                if (u.get("enforcement") or "guard").lower() == "detection":
                    detection_attrs.update(str(x) for x in (u.get("attrs") or []))
                else:
                    guard_uniq = True
            bare_unique = any(a.get("unique") and a["id"] not in detection_attrs
                              for a in e.get("attributes", []))
            if guard_uniq or bare_unique:
                need.add(eid)
        if not need:
            return
        # model-level escape: a bespoke plugin that reads/writes the entity may enforce it
        # itself (the same escape d013 uses, so the model and artefact corners agree).
        bespoke = set()
        for bp in self.model.get("bespoke_plugins", []):
            bespoke.update(bp.get("reads") or [])
            bespoke.update(bp.get("writes") or [])
        # tables whose emitted form carries a UniqueGuard validator binding
        guarded = set()
        for jf in json_files(self.build, "forms"):
            doc = json.loads(jf.read_text(encoding="utf-8"))
            table = doc.get("properties", {}).get("tableName")
            for el in elements(doc):
                cn = ((el.get("properties", {}) or {}).get("validator", {}) or {}).get("className", "")
                if "UniqueGuard" in cn:
                    if table:
                        guarded.add(table)
                    break
        for eid in sorted(need):
            if eid in bespoke:
                continue
            table = entities[eid].get("table") or eid
            if table not in guarded:
                self.err("A006", f"entity/{eid}",
                         "declares uniqueness but no unique-guard binding is realized in the "
                         "build (nor a bespoke validator) — the constraint ships unenforced "
                         "(ADR-072/076). [scope: presence+shape — that a refusal actually FIRES "
                         "is proven by the acceptance constituent / scenario t02, not by A006]")

    # ---- A008 — the honest count is rendered (UI_CONFORMANCE_REVIEW §8.3) -------------
    def a008_honest_count(self):
        """Every emitted datalist renders a total row count.

        This is the ONLY new check the conformance review places in the artefact layer, and its
        justification for being here rather than upstream is the whole of the review's (b)
        column: "§15 has no count-display field at all (G-A-09) — there is nothing in the model
        to check." Every other rule the review specifies is decided by the L1 model and is
        therefore checked in `boundary_lint.py`, before a single artefact exists.

        Reads emitted datalist JSON in the build dir for a count / total binding on every list.
        Asserts a total-row-count element is present and bound. Must not fire on lists declared
        `x-bounded-set: true`.

        Severity: WARN, and deliberately so. The review names A008 "also a candidate platform
        demand, and the register's own rule applies: check the theme first" — a theme that
        renders its own count would make every finding here a false positive, and a false
        positive is how a check gets switched off. It rises to error when the theme has been
        checked and the answer is written down.
        """
        bounded = {l["id"] for l in self.model.get("lists", [])
                   if l.get("x-bounded-set") is True}
        for jf in json_files(self.build, "datalists"):
            doc = json.loads(jf.read_text(encoding="utf-8"))
            lid = doc.get("id") or doc.get("properties", {}).get("id") or jf.stem
            if lid in bounded or any(b in jf.stem for b in bounded):
                continue
            blob = json.dumps(doc).lower()
            if any(tok in blob for tok in ("showrowcount", "totalrowcount",
                                           "showpagesize", "rowcount")):
                continue
            self.warns.append(
                f"[A008] {jf.name}: no total-row-count binding is emitted — a list that does "
                f"not say how many rows there are cannot be trusted about how many there are "
                f"(UI_CONFORMANCE_REVIEW §8.3; G-A-09 — §15 has no count-display field, so "
                f"this is a candidate platform demand: check the theme first)")

    # ---- A004 / A005 — the two dormant checks, and they now part company -------------
    # A004 (a field bound to derived/source/master provenance emitted editable) MOVES UP to the
    #   model layer per UI_CONFORMANCE_REVIEW §8.2 as M-R3-02 — where it turns out already to
    #   have been built, as validate.py's U004 (schema 0.2 realised `provenance`; WP-F). It is
    #   therefore not dormant awaiting a dependency; its dependency landed.
    # A005 (a SelectBox whose options load an operational entity — the infinite dropdown) is
    #   WITHDRAWN, not built, and the review's reason is recorded here so the next reader meets
    #   it rather than rediscovering it as an omission: "A005 is written to read emitted JSON
    #   ... The model decides this, so checking the output instead is checking the projector —
    #   which is C-01. Recommendation: withdraw A005 rather than build it, and record the
    #   withdrawal with its reason." Its model half is boundary_lint's M-R4-02; its artefact
    #   half is tests/test_projector_controls.py (C-01).

    # ---- A009 — a menu entry that stands outside a category (METHOD-2026-09-26-02, point 11) ----
    def a009_lone_entry(self):
        """No menu entry stands outside a category. The platform's theme, Dx8TrimedaTheme, shows
        a category that holds one entry as an entry of its own, not as a category, and the
        owner's word of 25 September 2026, given on one application, is that no
        menu entry stands outside a category. So a generated menu in which
        a category a person sees holds exactly one entry is refused, naming the category. A
        category the menu hides (`hide` "yes": the forms that belong to a record, opened from
        the record) is not shown at all and is not counted. The kit's administration of lists of
        values joins a category of one list with another (tools/lov.py, admin_categories); a
        category of the model's own navigation is the model's to join."""
        for jf in json_files(self.build, "userviews"):
            doc = json.loads(jf.read_text(encoding="utf-8"))
            for cat in doc.get("categories") or []:
                p = cat.get("properties") or {}
                if str(p.get("hide") or "").strip().lower() in ("yes", "true"):
                    continue
                menus = cat.get("menus") or []
                if len(menus) == 1:
                    only = (menus[0].get("properties") or {}).get("label") or "?"
                    self.err("A009", f"{jf.name}#{p.get('label') or p.get('id')}",
                             f"the category '{p.get('label') or p.get('id')}' holds one entry, "
                             f"'{only}', and the platform's theme shows a category of one entry "
                             f"as an entry of its own, outside any category — join it with "
                             f"another category (the owner's word of 25 September 2026: no menu "
                             f"entry stands outside a category)")

    def run(self):
        self.a001_dead_selection()
        self.a002_smart_search()
        self.a003_secrets()
        self.a006_uniqueness_enforced()
        self.a007_unusable_userview()
        self.a008_honest_count()
        self.a009_lone_entry()
        return self.errors, self.warns


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("app", type=pathlib.Path)
    ap.add_argument("--build", required=True, type=pathlib.Path)
    a = ap.parse_args()
    model = yaml.safe_load(a.app.read_text(encoding="utf-8")) if a.app.exists() else {}
    errs, warns = UxLint(model, a.build).run()
    for f in warns:
        print(f)
    for f in errs:
        print(f)
    if errs:
        print(f"\nux-lint: {len(errs)} error-class finding(s) under {a.build}")
        return 1
    print(f"ux-lint: clean under {a.build}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
