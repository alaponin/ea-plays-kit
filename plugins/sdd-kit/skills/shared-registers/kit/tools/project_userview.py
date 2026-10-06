#!/usr/bin/env python3
"""Project the neutral userview spec from a Layer-1 application model's `navigation`.

Pure, deterministic projection under the standard projector contract (validate first,
byte-identical for identical input, provenance-stamped, totality-refuses constructs the
target generator cannot realize). The target is the PROJECT-NEUTRAL reference generator
`joget-platform-plugins/reference-app/generators/gen_userview.py` — not a project-forked
delivery generator — so the projection carries no project content (ADR-023).

    navigation (L1)  ->  <out>/<userviewId>.uv.yml  ->  gen_userview  ->  userview JSON

Menu support: `form` → FormMenu, `list` → DataListMenu, `crud` → CrudMenu (the entity's
bound form + its companion list), `report` → the inlined JasperReportsMenu, `dashboard` →
the dashboard's inlined SqlChartMenu chart(s), `inbox` → InboxMenu. `html`/`api`/
`external_link` are refused (totality) — the neutral generator has no menu for them yet;
see docs/PROJECTION-DECISIONS.md (UV-series).

Usage:
    project_userview.py <app.yaml> --out <dir> [--schema <schema.yaml>]

Exit codes: 0 ok · 1 schema errors · 2 lint errors · 3 projection errors.
"""
from __future__ import annotations

import argparse
import hashlib
import pathlib
import sys

import yaml

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import validate as l1
import custody
import lov  # the administration of lists of values (METHOD-2026-09-25-02)
import acts  # the moves' forms and their hidden categories (METHOD-2026-09-25-04)

PROJECTOR = "project_userview.py"
PROJECTOR_VERSION = "0.1.0"

# L1 nav menu type -> neutral generator menu type (None => refused, totality register).
MENU_MAP = {"form": "form", "list": "datalist", "crud": "crud", "report": "report",
            "inbox": "inbox", "dashboard": "dashboard"}
UNREALIZED_MENUS = {"html", "api", "external_link"}


class ProjectionError(Exception):
    """A valid L1 construct this projector cannot (yet) realize in the neutral generator."""


class Index:
    def __init__(self, doc: dict):
        self.forms_by_entity: dict[str, list[dict]] = {}
        self.forms: dict[str, dict] = {}
        for f in doc.get("forms", []):
            self.forms_by_entity.setdefault(f["entity"], []).append(f)
            self.forms[f["id"]] = f


def only_read(ix: Index, form_id) -> bool:
    """A form the model places only for reading: its `purpose` is `view` (METHOD-2026-09-26-02,
    point 3 — the case workspace, for one, ended in Save)."""
    return (ix.forms.get(form_id) or {}).get("purpose") == "view"


def project_menu(m: dict, ix: Index, path: str) -> dict:
    mtype = m["type"]
    if mtype in UNREALIZED_MENUS:
        raise ProjectionError(
            f"{path}: menu type '{mtype}' has no realization in the neutral userview generator "
            f"(supported: form/list/crud; totality register, UV-series)")
    target = MENU_MAP.get(mtype)
    if target is None:
        raise ProjectionError(f"{path}: unknown menu type '{mtype}'")
    out = {"type": target, "label": m["label"]}
    if mtype == "form":
        out["formId"] = m["form"]
        if m.get("readonly") or only_read(ix, m["form"]):
            # display-only menu, offering no Save: the menu says so, or its form is placed only
            # for reading (point 3); default is a submittable form
            out["readonly"] = True
        if m.get("submit_label"):
            # the words on the form's button: a move's form says the move's label (point 3;
            # acts.augment gives each move's menu its label)
            out["submit_label"] = str(m["submit_label"])
    elif mtype == "list":
        out["datalistId"] = m["list"]
    elif mtype == "crud":
        forms = ix.forms_by_entity.get(m.get("entity"), [])
        ids = {f["id"] for f in forms}
        # an explicit `form` picks the add/edit/view form when the entity has several;
        # `list` picks an explicit companion datalist (else the list_<form> convention).
        fid = m.get("form")
        if fid:
            if fid not in ids:
                raise ProjectionError(f"{path}: crud menu form '{fid}' is not bound to entity "
                                      f"'{m.get('entity')}'")
        elif len(forms) == 1:
            fid = forms[0]["id"]
        else:
            raise ProjectionError(
                f"{path}: crud menu on entity '{m.get('entity')}' has {len(forms)} forms; set "
                f"`form` to pick the CrudMenu add/edit/view form")
        out["formId"] = fid
        # `edit_form` splits create from edit. It exists because a `purpose: create` form
        # carries NO lifecycle Action select (project_forms.is_create — correct, a create
        # advances nothing), so for any entity WITH a lifecycle the create form and the
        # edit form are legitimately different forms. Until registry 0.9.9 both userview
        # ids derived from this one `form` key, so the applicant's own record opened with
        # the create form and no way to submit it (TC-FR-001, 2026-08-07).
        efid = m.get("edit_form")
        if efid:
            if efid not in ids:
                raise ProjectionError(f"{path}: crud menu edit_form '{efid}' is not bound to "
                                      f"entity '{m.get('entity')}'")
            out["editFormId"] = efid
        out["datalistId"] = m.get("list") or f"list_{fid}"
        # M7 refinement: mode toggles — a case list must open records but never offer
        # New (audited/engine-only creation) or Delete (history retention, as one module's requirements ask).
        if m.get("add") is False:
            out["add"] = False
        if m.get("delete") is False:
            out["delete"] = False
        if only_read(ix, efid or fid):
            # the record the menu opens is only read: the platform's edit-mode read-only, with no
            # Save and no Edit button (point 3; gen_userview 0.11.0 `edit_readonly`)
            out["edit_readonly"] = True
    elif mtype == "report":
        out["reportId"] = m["report"]         # gen_userview inlines the generated JasperReportsMenu
    elif mtype == "dashboard":
        out["dashboardId"] = m["dashboard"]   # gen_userview inlines the dashboard's chart menus
    elif mtype == "inbox":
        pass                                  # all-assignments workflow task inbox (InboxMenu)
    return out


def project_category(cat: dict, ix: Index) -> dict:
    path = f"navigation/{cat['id']}"
    out: dict = {"id": cat["id"], "label": cat["label"]}
    roles = cat.get("roles")
    if roles:
        out["role"] = ";".join(roles)         # GroupPermission allowedGroupIds (;-delimited)
    if cat.get("hidden"):
        # METHOD-2026-09-25-04, item 4: a category whose menus open from a record and never from
        # the menu — the platform's own `hide` on a category (UserviewCategory, "yes"). Its menus
        # stay reachable by their address and keep the category's roles. The pinned gen_userview
        # (registry 0.11.0) writes it as the platform's "yes"; `kit totality` names a category the
        # spec hides and the build shows (T112), as a generator before 0.11.0 built every one.
        out["hide"] = True
    out["menus"] = [project_menu(m, ix, f"{path}/{m.get('label')}") for m in cat["menus"]]
    return out


def project_navigation(doc: dict, ix: Index) -> dict:
    nav = doc.get("navigation")
    if not nav:
        raise ProjectionError("model has no `navigation` to project")
    uv: dict = {"id": nav["userview_id"], "name": nav.get("name", nav["userview_id"])}
    categories = [project_category(c, ix) for c in nav.get("categories", [])]
    uv["categories"] = categories
    return {"userview": uv}


def menu_address(menu: dict):
    """The address (`customId`) the pinned gen_userview gives a projected menu, by its own rule:
    a CRUD menu `<list>_crud`, a list menu its list, a form menu its form, an inbox `inbox_<label>`
    (gen_userview crud_menu, datalist_menu, form_menu, inbox_menu). A report or a dashboard is the
    element its own generator made, inlined; its address is not derived here, so None."""
    t = menu.get("type")
    if t == "crud":
        return f"{menu.get('datalistId') or 'list_' + str(menu.get('formId'))}_crud"
    if t == "datalist":
        return menu.get("datalistId")
    if t == "form":
        return menu.get("formId")
    if t == "inbox":
        slug = "".join(c if c.isalnum() else "_" for c in str(menu.get("label", ""))).strip("_")
        return "inbox_" + (slug.lower() or "inbox")
    return None


def _opens(menu: dict) -> str:
    t = menu.get("type")
    if t == "crud":
        return (f"a CRUD menu over the list {menu.get('datalistId')}, opening a row in "
                f"{menu.get('editFormId') or menu.get('formId')}")
    if t == "form":
        return f"the form {menu.get('formId')}" + (" to read" if menu.get("readonly") else "")
    if t == "datalist":
        return f"the list {menu.get('datalistId')}"
    return f"a {t} menu"


def addresses_placed_twice(spec: dict) -> list[str]:
    """Every address the projected navigation hands the pinned generator for more than one menu
    (ADR-108; a delivery's hand-off of 6 October 2026, item 5, F-B2-07).

    The platform builds the menus of every category a person may see and takes, for an address,
    the last menu that carries it (UserviewService, jw-community wflow-core: `setCurrent` on each
    match, in order), so a second place of one address is reached by nobody who may see both, and
    a row's link to it (DL-06) opens the later place. The generator derives the address from the
    menu's list or form alone and takes none from the spec, so the projector cannot give the later
    place an address of its own; that is the generator's to change, and it is named for its owner
    in docs/PROJECTION-DECISIONS.md (UV-03). Until then the projector says so, for each address,
    rather than handing the generator a navigation whose second place no address reaches."""
    seen: dict = {}
    for cat in spec["userview"]["categories"]:
        for m in cat["menus"]:
            addr = menu_address(m)
            if addr:
                seen.setdefault(addr, []).append((cat, m))
    out = []
    for addr, places in seen.items():
        if len(places) < 2:
            continue
        where = "; ".join(
            f"{c['id']}{' (hidden)' if c.get('hide') else ''}{' for ' + c['role'] if c.get('role') else ''}: "
            f"'{m.get('label')}', {_opens(m)}" for c, m in places)
        kinds = {_opens(m) for _, m in places}
        out.append(
            f"navigation: the address '{addr}' is placed {len(places)} times — {where}. The pinned "
            f"userview generator derives a menu's address from its list or its form alone, so a "
            f"person who may see more than one of these places reaches only the last, in "
            f"{places[-1][0]['id']}" + ("" if len(kinds) == 1 else
                                         ", and what the others open is reached by no address"))
    return out


def provenance_header(doc: dict, source_name: str, sha: str) -> str:
    m = doc.get("model", {})
    return (
        "# =============================================================================\n"
        "# GENERATED — do not edit. Projected from the Layer-1 application model.\n"
        f"# projector:      {PROJECTOR} v{PROJECTOR_VERSION} (the spec kit)\n"
        f"# schema_version: {m.get('schema_version')}\n"
        f"# spec_version:   {m.get('spec_version')}\n"
        f"# source_model:   {source_name}\n"
        f"# source_sha256:  {sha}\n"
        "# =============================================================================\n")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("app", type=pathlib.Path)
    ap.add_argument("--out", type=pathlib.Path, required=True)
    ap.add_argument("--schema", type=pathlib.Path, default=l1.DEFAULT_SCHEMA)
    custody.add_arg(ap)
    args = ap.parse_args()

    schema = l1.load(args.schema)
    doc = l1.load(args.app)
    errs = l1.schema_errors(schema, doc)
    if errs:
        print(f"SCHEMA: {len(errs)} error(s) — refusing to project")
        for e in errs:
            print(f"  - {e}")
        return 1
    print("SCHEMA: ok")
    if l1.Lint(doc).run():
        print("LINT:   errors — refusing to project (run kit validate)")
        return 2
    print("LINT:   ok")
    derrs, dwarns = l1.delta_contract(doc)
    for w in dwarns:
        print(f"  ~ {w}")
    if derrs:
        print(f"DELTA/CONTRACT: {len(derrs)} error(s) — refusing to project")
        for e in derrs:
            print(f"  - {e}")
        return 2
    print("DELTA/CONTRACT: ok" + (f" ({len(dwarns)} warning(s))" if dwarns else ""))

    if not doc.get("navigation"):
        print("no navigation to project")
        return 0
    try:
        doc = lov.augment(doc, args.app)    # adds the administration categories (lov.py)
        doc = acts.augment(doc)             # adds the hidden categories of the moves (acts.py)
        spec = project_navigation(doc, Index(doc))
    except lov.LovError as exc:
        print(f"PROJECT: lists of values: {exc}")
        return 3
    except ProjectionError as exc:
        print(f"PROJECT: {exc}")
        return 3
    for w in addresses_placed_twice(spec):     # ADR-108: said, never handed over in silence
        print(f"  ~ {w}")

    sha = hashlib.sha256(args.app.read_bytes()).hexdigest()
    header = provenance_header(doc, args.app.name, sha)
    header += custody.line(args.custody)
    uv_id = spec["userview"]["id"]
    rel = pathlib.Path(f"{uv_id}.uv.yml")
    out_path = args.out / rel
    out_path.parent.mkdir(parents=True, exist_ok=True)
    body = yaml.safe_dump(spec, sort_keys=False, default_flow_style=False,
                          allow_unicode=True, width=4096)
    out_path.write_text(header + body, encoding="utf-8", newline="\n")
    print(f"  + {rel.as_posix()}")
    print(f"userview spec projected -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
