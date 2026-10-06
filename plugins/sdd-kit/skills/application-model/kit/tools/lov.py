#!/usr/bin/env python3
"""The administration of lists of values that every generated application carries.

Decided on the owner's word of 25 September 2026 (METHOD-2026-09-25-02): an application the kit
generates carries, with no design in its model, a complete administration of its lists of values.

  * Every vocabulary that is not `fixed` gets its own storage (one table per list), a form to add a
    value, a form to change one, a list, and its first values loaded from the model (its `rows`, or
    the CSV file its `file` names). Every entity of kind `md_lookup` that is not `fixed` gets a form
    and a list where the model gives it none; its first values are the model's `seed` as before.
  * The userview gains the administration's categories, visible only to the role that maintains
    the lists (the model's `maintained_by`, else the application's administrator role), one entry
    per list, grouped by the record that uses each list and no category holding more than nine
    (METHOD-2026-09-25-04, item 7, which replaced the single alphabetical category of the
    orchestrator's amendment of 25 Sep 2026, 08:58 UTC). A value can
    be added, its label changed, its order changed and it can be retired. Nothing is ever deleted:
    the entry offers no delete, and the form that changes a value does not let its code change,
    because records hold the code.
  * A list of more than nine values in force is divided into categories (`groups`, another list of
    values); a value names its category, the form that adds or changes it requires one, and a
    drop-down over the list is chosen in two steps, the category and then the value within it.
  * Every drop-down that binds such a vocabulary draws its options from that list, shows the label
    only, and offers only the values in force, in the list's order; a retired value stays shown on
    a record that already holds it. A cascading list (a vocabulary with a `parent`) offers only the
    values of the parent value chosen on the same form.

How the drop-down does it on the platform. Joget's FormOptionsBinder loads every row of the list
(in force and retired, so that a record holding a retired value keeps it on display and on save —
the platform refuses a submitted value that is not among the options it loaded) and, given several
grouping columns separated by ';', writes their values into each option's `grouping` attribute.
A short script the kit places at the head of the form then removes the retired options that are
not the record's own value, keeps only the children of the parent value chosen, and puts the
options in the list's order. A fixed vocabulary keeps inline options, label only, and cascades
through the platform's own controlField.

This module is pure: the same model gives the same plan, the same ids and the same script.
"""
from __future__ import annotations

import copy
import csv
import hashlib
import json
import pathlib
import re

FEATURE = "_lov"                      # the feature folder every generated artefact lands in
STANDING_VOCAB = "lov__standing"      # the fixed list of a value's two standings
IN_FORCE, RETIRED = "in_force", "retired"
STANDING_ROWS = [{"code": IN_FORCE, "name": "In force"}, {"code": RETIRED, "name": "Retired"}]
ID_CAP = 24                           # D-022: 24-character form-id / table-name cap
FORM_CAP = ID_CAP - len("Edit")       # so that the change form's id fits the cap too
ADMIN_LABEL = "Administration — lists of values"
# The administration's categories are named after the record that uses each list (METHOD-2026-09-
# 25-04, item 7): "Lists of values — Debt case", and "Lists of values — shared lists".
LISTS_LABEL = "Lists of values"
SHARED_LABEL = "shared lists"
# No step of a selection offers more than nine values, and seven is the aim (UX-01 IDR-05, the
# owner's word of 25 September 2026; rulings/2026-09-25-long-lists-are-chosen-by-category.yaml).
MOST = 9
SCRIPT_FIELD = "lov_script"
# The role the application's administrator holds, recognised by its id (exactly one must match).
ADMIN_ROLE_IDS = {"administrator", "admin", "system_administrator", "sys_admin", "sysadmin",
                  "app_administrator", "application_administrator"}
ADMIN_ROLE_SUFFIXES = ("_administrator", "_admin")
PLAN_KEY = "x-lov-plan"

# ---- the code of a value added in the administration (METHOD-2026-09-26-02, point 9) ----------
# The owner's word of 25 September 2026: "all code must be automatically generated on saving". The
# form that adds a value asks for its label, and the code is made when the value is saved:
#
#   * in a list whose label is shown (the default), by the platform's own ID generator
#     (IdGeneratorField, Joget DX 9.0.7) in its distributed mode (`isDistributedGeneration`): the
#     number AppUtil.idGenerator takes from DistributedIdGenerator.nextId — 41 bits of the
#     milliseconds since 1 January 2015, 10 bits of the server's node and a 12-bit sequence,
#     drawn under a lock and refused when the clock has gone back — written in full (the format
#     `?`). No two values are ever given the same number, whatever the list, the version of the
#     application or the deploy: the counter of the ordinary mode lives in the application's
#     version, which every deploy makes anew, and started again at one (delta D-066). The first
#     values keep the codes the model gives them, and a first value whose code is a run of fifteen
#     or more digits, the shape of a made code, is refused, so the two can never meet. The field
#     is hidden on the add form, where it has nothing to show yet; the code is shown, read-only,
#     on the form that changes the value and in the list;
#   * in a list whose code is its label (`display_code`: the debt category, C1 to C6), what the
#     person types under "Label" is the code the list shows, and the label is made from it on
#     saving: a hidden field whose value, `#requestParam.code#`, the platform reads when the form
#     is saved and stores alone ("valueOnly"; HiddenField, Joget DX 9.0.7). The unique guard on
#     the code refuses, before anything is saved, a label the list already holds.
MADE_CODE_FORMAT = "?"
MADE_CODE_SHAPE = re.compile(r"^\d{15,}$")
ADD_CODE_MADE = {"attr": "code", "control": "id_generator", "required": False,
                 "config": {"props": {"format": MADE_CODE_FORMAT,
                                      "isDistributedGeneration": "true", "hidden": "true"}}}
ADD_CODE_SHOWN = ({"attr": "code", "label": "Label"},
                  {"attr": "name", "control": "hidden", "required": False,
                   "config": {"props": {"value": "#requestParam.code#",
                                        "useDefaultWhenEmpty": "valueOnly"}}})


class LovError(Exception):
    """A model the administration of its lists of values cannot be generated for."""


# --------------------------------------------------------------------------- #
# Names                                                                         #
# --------------------------------------------------------------------------- #

def pascal(s: str) -> str:
    return "".join(w[:1].upper() + w[1:] for w in re.split(r"[^A-Za-z0-9]+", s) if w)


def _h4(s: str) -> str:
    return hashlib.sha1(s.encode("utf-8")).hexdigest()[:4]


def _cap(base: str, stem: str, cap: int, sep: str = "") -> str:
    """base+stem when it fits the cap; else base + the stem cut short + a 4-hex digest of the
    whole stem (with `sep` before it), so that two long stems never meet on one name."""
    full = base + stem
    if len(full) <= cap:
        return full
    keep = cap - len(base) - len(sep) - 4
    if keep < 1:
        raise LovError(f"cannot fit a name for '{stem}' under the {cap}-character cap "
                       f"after the prefix '{base}'")
    return base + stem[:keep] + sep + _h4(stem)


def table_prefix(doc: dict) -> str:
    """Tables are shared by every application on an instance (D-028), so every table the
    administration adds is prefixed with the application's id, lower-cased (at most 8 letters)."""
    app_id = str((doc.get("app") or {}).get("id") or "app")
    return (re.sub(r"[^a-z0-9]", "", app_id.lower())[:8] or "app") + "_"


def names_for(doc: dict, vid: str) -> dict:
    p = pascal(vid)
    form = _cap("lov", p, FORM_CAP)
    return {"entity": f"lov_{vid}",
            "table": _cap(table_prefix(doc) + "lv_", vid, ID_CAP, sep="_"),
            "form": form, "edit_form": form + "Edit",
            "datalist": _cap("lsLov", p, ID_CAP)}


def names_for_entity(ent: dict) -> dict:
    p = pascal(ent["id"])
    return {"form": _cap("lov", p, ID_CAP), "datalist": _cap("lsLov", p, ID_CAP)}


# --------------------------------------------------------------------------- #
# Who maintains what                                                           #
# --------------------------------------------------------------------------- #

def admin_role(doc: dict):
    """The application's administrator role: the one role whose id is an administrator's id
    (administrator, admin, system_administrator, … or ending in _administrator or _admin).
    None when no role, or more than one, answers to it."""
    hits = [r["id"] for r in doc.get("roles", [])
            if r.get("id") in ADMIN_ROLE_IDS or str(r.get("id", "")).endswith(ADMIN_ROLE_SUFFIXES)]
    return hits[0] if len(hits) == 1 else None


def maintained_vocabularies(doc: dict) -> list:
    return [v for v in doc.get("vocabularies", [])
            if not v.get("fixed") and v.get("id") != STANDING_VOCAB]


def maintained_md_lookups(doc: dict) -> list:
    return [e for e in doc.get("entities", [])
            if e.get("kind") == "md_lookup" and not e.get("fixed")
            and not e.get("x-lov-generated")]


def maintainer(doc: dict, obj: dict, what: str) -> str:
    role = obj.get("maintained_by") or admin_role(doc)
    if not role:
        ids = [r.get("id") for r in doc.get("roles", [])]
        raise LovError(
            f"{what} is maintained in the application, but the model names no role that "
            f"maintains it and no administrator role the kit can recognise (a role whose id is "
            f"'administrator', 'admin', 'system_administrator' or ends in '_administrator' or "
            f"'_admin'; the model's roles are {ids}). Add that role, name `maintained_by`, or "
            f"mark the list `fixed: true`.")
    return role


# --------------------------------------------------------------------------- #
# The first values                                                             #
# --------------------------------------------------------------------------- #

def rows_of(vocab: dict, app_path=None) -> list:
    """The vocabulary's first values: its inline `rows`, else the CSV file `file` names
    (code,name[,parent_code[,group]]; a first line reading `code,…` is a header), relative to the
    model."""
    if vocab.get("rows"):
        return [dict(r) for r in vocab["rows"]]
    if not vocab.get("file"):
        return []
    if app_path is None:
        raise LovError(f"vocabulary '{vocab['id']}' names the file '{vocab['file']}', and the "
                       f"model's own path is not known, so the file cannot be found")
    path = pathlib.Path(app_path).parent / vocab["file"]
    if not path.is_file():
        raise LovError(f"vocabulary '{vocab['id']}' names the file '{vocab['file']}', which is "
                       f"not at {path}")
    out = []
    with open(path, encoding="utf-8", newline="") as fh:
        for i, rec in enumerate(csv.reader(fh)):
            if not rec or not rec[0].strip():
                continue
            if i == 0 and rec[0].strip().lower() == "code":
                continue
            row = {"code": rec[0].strip(), "name": (rec[1].strip() if len(rec) > 1 else rec[0].strip())}
            if len(rec) > 2 and rec[2].strip():
                row["parent_code"] = rec[2].strip()
            if len(rec) > 3 and rec[3].strip():
                row["group"] = rec[3].strip()
            out.append(row)
    return out


# --------------------------------------------------------------------------- #
# The plan, added to the model as the projectors read it                       #
# --------------------------------------------------------------------------- #

def _grouping(has_parent: bool) -> str:
    return ("parent_code;" if has_parent else "") + "standing;sort_order"


def lookup_for(doc: dict, vid: str):
    """The drop-down binding of a maintained vocabulary, or None for a fixed one. A list whose
    business code is itself the label (`display_code: true`) shows its code (METHOD-2026-09-25-04,
    item 1)."""
    info = ((doc.get(PLAN_KEY) or {}).get("vocab") or {}).get(vid)
    if not info:
        return None
    return {"formDefId": info["form"], "idColumn": "code",
            "labelColumn": "code" if info.get("display_code") else "name",
            "groupingColumn": _grouping(bool(info["parent"]))
            + (";group_code" if info.get("groups") else "")}


def divided_binder(doc: dict, vid: str):
    """The options binder of a drop-down over a DIVIDED list — one whose values fall into
    categories (`groups`; METHOD-2026-09-25-04, item 7, the owner's word of 25 September 2026). Or
    None for an undivided one, which keeps the form options binder of `lookup_for`.

    The person chooses in two steps, the category and then the value within it. The category is
    not stored: it is drawn by the form's script from the options of the value's own drop-down,
    whose grouping carries, after the value's standing and order, the category's code, label,
    order and standing — read at run time from the list of categories' own table, so a category
    relabelled, reordered or retired in the administration shows as it now stands. The platform's
    form options binder reads one table; the enterprise JDBC options binder reads the two joined
    (its first column is the value, its second the label, its third the grouping)."""
    plan = (doc.get(PLAN_KEY) or {}).get("vocab") or {}
    info = plan.get(vid)
    if not info or not info.get("groups"):
        return None
    ginfo = plan.get(info["groups"])
    if not ginfo:
        return None
    label = "v.c_code" if info.get("display_code") else "v.c_name"
    glabel = "g.c_code" if ginfo.get("display_code") else "g.c_name"
    parts = (["v.c_parent_code"] if info["parent"] else []) + [
        "v.c_standing", "COALESCE(v.c_sort_order, '')", "COALESCE(v.c_group_code, '')",
        f"REPLACE(COALESCE({glabel}, ''), ';', ',')", "COALESCE(g.c_sort_order, '')",
        f"COALESCE(g.c_standing, '{IN_FORCE}')"]
    grouping = "CONCAT(" + ", ';', ".join(parts) + ")"
    sql = (f"SELECT v.c_code, {label}, {grouping} FROM app_fd_{info['table']} v "
           f"LEFT JOIN app_fd_{ginfo['table']} g ON g.c_code = v.c_group_code "
           f"ORDER BY {label}")
    return {"className": "org.joget.plugin.enterprise.JdbcOptionsBinder",
            "properties": {"jdbcDatasource": "default", "useAjax": "", "addEmpty": "true",
                           "emptyLabel": "", "sql": sql}}


def filter_binder(doc: dict, vid: str, with_category: bool = False):
    """The options binder a list's select filter over a maintained vocabulary reads the list
    through while the application runs (METHOD-2026-09-26-02, point 4): the platform's enterprise
    JDBC options binder, as a form's drop-down over a divided list has it (divided_binder), over
    the list's own table. It offers the values in force, in the list's order, labelled as the
    list shows them (its code where the code is the label); with `with_category`, the value's
    category as the third column, the grouping by which the platform keeps, in a filter that
    names a control, the values of the category chosen there (SelectBoxDataListFilterType,
    `controlField`; gen_datalists 0.11.0). None for a fixed vocabulary, which has no table."""
    info = ((doc.get(PLAN_KEY) or {}).get("vocab") or {}).get(vid)
    if not info:
        return None
    label = "c_code" if info.get("display_code") else "c_name"
    cols = f"c_code, {label}" + (", c_group_code" if with_category else "")
    sql = (f"SELECT {cols} FROM app_fd_{info['table']} WHERE c_standing = '{IN_FORCE}' "
           f"ORDER BY {order_sql(doc)}")
    return {"className": "org.joget.plugin.enterprise.JdbcOptionsBinder",
            "properties": {"jdbcDatasource": "default", "useAjax": "", "addEmpty": "",
                           "emptyLabel": "", "sql": sql}}


def label_formatter_for(doc: dict, vid: str):
    """The list-column formatter that shows a maintained vocabulary's label, read from the
    list's own table when the list is shown — so a value relabelled or retired in the
    administration shows as it now stands (METHOD-2026-09-25-04, item 1; the lists-of-values
    report's "Found, not fixed", item 4). None for a fixed vocabulary, which has no table."""
    lk = lookup_for(doc, vid)
    if not lk:
        return None
    return {"type": "optionsValue", "formDefId": lk["formDefId"], "idColumn": "code",
            "labelColumn": lk["labelColumn"]}


def augment(doc: dict, app_path=None) -> dict:
    """The model with its lists-of-values administration added as the constructs the projectors
    already read: an md_lookup entity, an add form, a change form and first values for each
    maintained vocabulary; a form and a list for a maintained md_lookup entity that has none; and
    the administration categories in `navigation`. The model given is not changed. Idempotent."""
    if doc.get(PLAN_KEY) is not None:
        return doc
    d = copy.deepcopy(doc)
    vocabs = maintained_vocabularies(d)
    mds = maintained_md_lookups(d)
    plan = {"vocab": {}, "forms": {}, "datalists": [], "entities": {}}
    d[PLAN_KEY] = plan
    if not vocabs and not mds:
        return d

    ent_ids = {e["id"] for e in d.get("entities", [])}
    form_ids = {f["id"] for f in d.get("forms", [])}
    list_ids = {l["id"] for l in d.get("lists", [])}
    tables = {e.get("table") for e in d.get("entities", [])}
    by_id = {v["id"]: v for v in d.get("vocabularies", [])}
    taken: set = set()

    def claim(kind: str, name: str, existing: set, what: str):
        if name in existing or name in taken:
            raise LovError(f"the {kind} '{name}' the administration of {what} needs is already "
                           f"used in the model; rename the model's one")
        taken.add(name)

    entries = []                                      # (role, label, menu)
    if vocabs and STANDING_VOCAB not in by_id:
        d.setdefault("vocabularies", []).append(
            {"id": STANDING_VOCAB, "name": "Standing", "fixed": True, "x-lov-generated": True,
             "rows": [dict(r) for r in STANDING_ROWS]})
    for v in vocabs:
        vid = v["id"]
        n = names_for(d, vid)
        what = f"the list of values '{vid}'"
        claim("entity", n["entity"], ent_ids, what)
        claim("table", n["table"], tables, what)
        for k in ("form", "edit_form"):
            claim("form", n[k], form_ids, what)
        claim("list", n["datalist"], list_ids, what)
        par = v.get("parent")
        pinfo = by_id.get(par) if par else None
        parent_kept = bool(pinfo) and not pinfo.get("fixed")
        grp = v.get("groups")
        ginfo = by_id.get(grp) if grp else None
        if grp and (not ginfo or ginfo.get("fixed") or v.get("fixed")):
            raise LovError(f"the list of values '{vid}' is divided into the categories of "
                           f"'{grp}', and a divided list and its categories are both lists the "
                           f"application maintains (lint U026)")
        plan["vocab"][vid] = {**n, "parent": par or "", "name": v.get("name") or vid,
                              "parent_form": names_for(d, par)["form"] if parent_kept else "",
                              "display_code": bool(v.get("display_code")),
                              "groups": grp or "",
                              "group_form": names_for(d, grp)["form"] if grp else "",
                              "group_name": (ginfo or {}).get("name") or grp or ""}
        plan["forms"][n["form"]] = {"vocab": vid, "parent_form": plan["vocab"][vid]["parent_form"]}
        plan["datalists"].append(vid)

    for v in vocabs:
        vid = v["id"]
        info = plan["vocab"][vid]
        par = info["parent"]
        attrs = [{"id": "code", "name": "Code", "type": "string", "required": True, "unique": True},
                 {"id": "name", "name": "Label", "type": "string", "required": True}]
        if par:
            pname = (by_id.get(par) or {}).get("name") or par
            if info["parent_form"]:
                attrs.append({"id": "parent_code", "name": pname, "type": "ref", "required": True,
                              "ref": {"entity": f"lov_{par}", "display": "name"}})
            else:
                attrs.append({"id": "parent_code", "name": pname, "type": "enum",
                              "vocabulary": par, "required": True})
        if info["groups"]:
            # item 7: a value of a divided list names its category, which the form that adds or
            # changes the value requires
            attrs.append({"id": "group_code", "name": info["group_name"], "type": "ref",
                          "required": True,
                          "ref": {"entity": f"lov_{info['groups']}", "display": "name"}})
        attrs += [{"id": "sort_order", "name": "Order", "type": "integer", "required": True},
                  {"id": "standing", "name": "Standing", "type": "enum",
                   "vocabulary": STANDING_VOCAB, "required": True, "default": IN_FORCE}]
        shown = bool(info.get("display_code"))
        d.setdefault("entities", []).append({
            "id": info["entity"], "name": f"List of values: {info['name']}", "kind": "md_lookup",
            "table": info["table"], "feature": FEATURE, "scale": "bounded",
            "pk": {"attr": "code"}, "attributes": attrs, "x-lov-generated": True,
            "uniqueness": [{"attrs": ["code"],
                            "message": ("This label is already in the list." if shown else
                                        "This code is already in the list.")}]})

        def fields(edit: bool):
            if edit:
                out = [{"attr": "code", "readonly": True}, {"attr": "name"}]
            elif shown:
                out = [dict(ADD_CODE_SHOWN[0]), copy.deepcopy(ADD_CODE_SHOWN[1])]
            else:
                out = [dict(ADD_CODE_MADE, config={"props": dict(
                    ADD_CODE_MADE["config"]["props"],
                    envVariable=f"{info['form']}Counter")}), {"attr": "name"}]
            if par:
                f = {"attr": "parent_code"}
                if info["parent_form"]:
                    f["config"] = {"lookup": lookup_for(d, par)}
                out.append(f)
            if info["groups"]:
                out.append({"attr": "group_code", "required": True,
                            "config": {"lookup": lookup_for(d, info["groups"])}})
            return out + [{"attr": "sort_order"}, {"attr": "standing"}]

        for key, edit, purpose in (("form", False, "create"), ("edit_form", True, "edit")):
            d.setdefault("forms", []).append({
                "id": info[key], "name": info["name"], "entity": info["entity"],
                "purpose": purpose, "feature": FEATURE, "x-lov-generated": True,
                "sections": [{"id": "sec_value", "label": info["name"], "columns": 1,
                              "fields": fields(edit)}]})

        seed_rows = []
        for r in rows_of(v, app_path):
            if not shown and MADE_CODE_SHAPE.match(str(r.get("code", ""))):
                raise LovError(
                    f"the list of values '{vid}' gives the first value '{r.get('name', '')}' the "
                    f"code {r['code']}, a run of fifteen or more digits — the shape of a code the "
                    f"application makes when a value is added (point 9 of METHOD-2026-09-26-02): "
                    f"a code the model gives is never one the application could make, so that no "
                    f"two values of the list meet on one code. Give the value a code of another "
                    f"shape.")
        for i, r in enumerate(rows_of(v, app_path)):
            row = {"code": r["code"], "name": r.get("name", r["code"]),
                   "sort_order": (i + 1) * 10, "standing": IN_FORCE}
            if par and r.get("parent_code"):
                row["parent_code"] = r["parent_code"]
            if info["groups"] and r.get("group"):
                row["group_code"] = r["group"]
            seed_rows.append(row)
        if seed_rows:
            d.setdefault("seed", []).append({"entity": info["entity"], "order": 5,
                                             "rows": seed_rows, "x-lov-generated": True})
        role = maintainer(d, v, f"the list of values '{vid}'")
        entries.append((role, info["name"], {
            "type": "crud", "label": info["name"], "entity": info["entity"],
            "form": info["form"], "edit_form": info["edit_form"], "list": info["datalist"],
            "delete": False}))

    nav = d.get("navigation") or {}
    navigated = _navigated_entities(d)
    for e in mds:
        eid = e["id"]
        n = names_for_entity(e)
        what = f"the list of values '{eid}'"
        forms = [f for f in d.get("forms", []) if f.get("entity") == eid]
        if not forms:
            claim("form", n["form"], form_ids, what)
            flds = [{"attr": a["id"]} for a in e.get("attributes", [])
                    if a.get("type") not in ("computed",)]
            forms = [{"id": n["form"], "name": e.get("name") or eid, "entity": eid,
                      "purpose": "edit", "feature": FEATURE, "x-lov-generated": True,
                      "sections": [{"id": "sec_value", "label": e.get("name") or eid,
                                    "columns": 1, "fields": flds}]}]
            d.setdefault("forms", []).extend(forms)
        lists = [l for l in d.get("lists", []) if (l.get("source") or {}).get("entity") == eid]
        if not lists:
            claim("list", n["datalist"], list_ids, what)
            cols = [{"attr": a["id"],
                     "label": a.get("name") or a["id"].replace("_", " ").capitalize()}
                    for a in e.get("attributes", [])
                    if a.get("type") in ("string", "integer", "decimal", "date", "datetime",
                                         "boolean", "enum")][:6]
            lists = [{"id": n["datalist"], "name": e.get("name") or eid, "feature": FEATURE,
                      "source": {"entity": eid, "form": forms[0]["id"]}, "columns": cols,
                      "x-lov-generated": True}]
            d.setdefault("lists", []).extend(lists)
        plan["entities"][eid] = {"form": forms[0]["id"], "datalist": lists[0]["id"]}
        if eid in navigated:
            continue                                  # the model already gives it an entry
        role = maintainer(d, e, what)
        entries.append((role, e.get("name") or eid, {
            "type": "crud", "label": e.get("name") or eid, "entity": eid,
            "form": forms[0]["id"], "list": lists[0]["id"], "delete": False}))

    if nav and entries:
        nav.setdefault("categories", []).extend(admin_categories(d, entries))
    return d


def _navigated_entities(doc: dict) -> set:
    """Entities the model's own navigation already opens: a CRUD menu over them, or a form or
    list menu whose form or list is theirs."""
    forms = {f["id"]: f.get("entity") for f in doc.get("forms", [])}
    lists = {l["id"]: (l.get("source") or {}).get("entity") for l in doc.get("lists", [])}
    out = set()
    for c in (doc.get("navigation") or {}).get("categories", []):
        for m in c.get("menus", []):
            if m.get("entity"):
                out.add(m["entity"])
            if m.get("form") in forms:
                out.add(forms[m["form"]])
            if m.get("list") in lists:
                out.add(lists[m["list"]])
    out.discard(None)
    return out


def list_users(doc: dict) -> dict:
    """The records that use each list: {menu entity (`lov_<vocabulary>`, or an md_lookup entity's
    id) -> set of the ids of the model's own entities whose attributes draw on it}. A list that
    is the parent of a cascading list, or the categories of a divided one, is used wherever that
    list is used."""
    by_vocab: dict = {}
    by_ent: dict = {}
    for e in doc.get("entities", []):
        if e.get("x-lov-generated"):
            continue
        for a in e.get("attributes", []):
            if a.get("type") == "enum" and a.get("vocabulary"):
                by_vocab.setdefault(a["vocabulary"], set()).add(e["id"])
            elif a.get("type") == "ref":
                by_ent.setdefault((a.get("ref") or {}).get("entity"), set()).add(e["id"])
    vocabs = doc.get("vocabularies", [])
    for _ in range(len(vocabs)):                        # a chain of parents settles in as many
        for v in vocabs:
            for up in (v.get("parent"), v.get("groups")):
                if up and by_vocab.get(v["id"]):
                    by_vocab.setdefault(up, set()).update(by_vocab[v["id"]])
    out = {f"lov_{vid}": set(s) for vid, s in by_vocab.items()}
    for eid, s in by_ent.items():
        out.setdefault(eid, set()).update(s)
    return out


def grouping_of(doc: dict) -> tuple:
    """How the administration groups the lists of values — a setting of the model
    (METHOD-2026-09-26-02, point 10): `navigation.lists_of_values.grouping`, either `by_record`,
    the default, which applies the ruling on long lists, point 3, or `one_category`, one category
    holding every list of values in the order of their labels, named by
    `navigation.lists_of_values.category`. Returns (grouping, the category's name)."""
    s = ((doc.get("navigation") or {}).get("lists_of_values") or {})
    grouping = str(s.get("grouping") or "by_record")
    return grouping, str(s.get("category") or LISTS_LABEL)


def _balanced(items: list, most: int = MOST) -> list:
    """`items` in parts of no more than `most`, as even as they can be, in their order: ten are
    five and five, never nine and one (METHOD-2026-09-26-02, point 11 — a part of one entry
    would stand in the menu as an entry of its own)."""
    if len(items) <= most:
        return [items]
    n = -(-len(items) // most)
    size, extra = divmod(len(items), n)
    out, i = [], 0
    for k in range(n):
        step = size + (1 if k < extra else 0)
        out.append(items[i:i + step])
        i += step
    return out


def _names_joined(words: list) -> str:
    return words[0] if len(words) == 1 else ", ".join(words[:-1]) + " and " + words[-1]


def admin_categories(doc: dict, entries: list) -> list:
    """The administration's own entries, in categories shown to the role that maintains them.

    Two groupings, a setting of the model (grouping_of; METHOD-2026-09-26-02, point 10):

      * by_record, the default (METHOD-2026-09-25-04, item 7; the ruling on long lists, point 3):
        a list used by one record stands in that record's category, a list used by several
        records — or by none — in the category of shared lists; no category holds more than nine,
        a larger one is divided in parts, as even as they can be, in the order of the labels. A
        category that would hold one list is joined with the smallest other category of the same
        role, and the joined category is named after both (point 11: the platform's theme shows a
        category of one entry as an entry of its own). The administrator's categories come first,
        the records in the order of their names, the shared lists last.
      * one_category: one category for each role that maintains lists, named as the model names
        it ("Admin"), holding every list of values that role keeps, in the order of their labels.
        The limit of nine stays with the drop-downs and the steps of a choice (U026), not with
        this menu: the owner's word for one application leaves no room for it."""
    admin = admin_role(doc)
    names = {r["id"]: r.get("name") or r["id"] for r in doc.get("roles", [])}
    grouping, cat_name = grouping_of(doc)
    by_label = lambda x: (x[0].casefold(), x[1]["entity"])          # noqa: E731
    roles = sorted({r for r, _, _ in entries}, key=lambda r: (r != admin, r))
    cats = []
    if grouping == "one_category":
        for role in roles:
            mine = sorted(((lbl, m) for r, lbl, m in entries if r == role), key=by_label)
            label = cat_name if role == admin else f"{cat_name} — {names.get(role, role)}"
            cats.append({"id": f"cat_lov_{role}", "label": label, "roles": [role],
                         "x-lov-generated": True, "menus": [m for _, m in mine]})
        return cats
    records = {e["id"]: e.get("name") or e["id"] for e in doc.get("entities", [])}
    users = list_users(doc)
    order = lambda k: (k == "", records.get(k, k).casefold(), k)       # noqa: E731
    for role in roles:
        by_key: dict = {}
        for r, lbl, m in entries:
            if r != role:
                continue
            used = sorted(users.get(m["entity"], set()))
            by_key.setdefault(used[0] if len(used) == 1 else "", []).append((lbl, m))
        groups = [{"keys": [k], "items": by_key[k]} for k in sorted(by_key, key=order)]
        while len(groups) > 1:
            lone = next((g for g in groups if len(g["items"]) == 1), None)
            if lone is None:
                break
            others = [g for g in groups if g is not lone]
            partner = min(others, key=lambda g: (len(g["items"]), groups.index(g)))
            partner["keys"] = sorted(partner["keys"] + lone["keys"], key=order)
            partner["items"] += lone["items"]
            groups.remove(lone)
        for g in groups:
            words = [records.get(k, k) for k in g["keys"] if k] + \
                ([SHARED_LABEL] if "" in g["keys"] else [])
            parts = _balanced(sorted(g["items"], key=by_label))
            stem = "_".join(k or "shared" for k in g["keys"])
            for n, part in enumerate(parts, 1):
                label = f"{LISTS_LABEL} — {_names_joined(words)}"
                if len(parts) > 1:
                    label += f" ({n} of {len(parts)})"
                if role != admin:
                    label += f" — {names.get(role, role)}"
                cid = f"cat_lov_{role}_{stem}" + (f"_{n}" if len(parts) > 1 else "")
                cats.append({"id": cid, "label": label, "roles": [role],
                             "x-lov-generated": True, "menus": [m for _, m in part]})
    return cats


# --------------------------------------------------------------------------- #
# The list of each maintained vocabulary (Layer 2, gen_datalists input)         #
# --------------------------------------------------------------------------- #

def order_sql(doc: dict, column: str = "c_sort_order") -> str:
    """The list's *Order* read as a number. Every column of a Joget table is text, so a list bound
    to the form sorts 10, 100, 110, 20 (one application's report on its deploy,
    \"Found, not fixed\", item 3). The cast is written for the application's database:
    PostgreSQL's NUMERIC keeps "10" as 10; MySQL takes DECIMAL. An empty order sorts last."""
    db = str(((doc.get("app") or {}).get("platform") or {}).get("db") or "postgres")
    kind = "DECIMAL(12,2)" if db == "mysql" else "NUMERIC"
    return f"CAST(NULLIF({column}, '') AS {kind})"


def datalist_sql(doc: dict, info: dict) -> str:
    """The administration list of one maintained vocabulary, read straight from its table so
    that *Order* is ordered and shown as a number (METHOD-2026-09-25-04, item 1)."""
    cols = ["id", "c_code AS code", "c_name AS name"]
    if info["parent"]:
        cols.append("c_parent_code AS parent_code")
    if info.get("groups"):
        cols.append("c_group_code AS group_code")
    cols += [f"{order_sql(doc)} AS sort_order", "c_standing AS standing"]
    return f"SELECT {', '.join(cols)} FROM app_fd_{info['table']}"


def datalist_specs(doc: dict) -> list:
    """[(relative path, spec)] — one list per maintained vocabulary: code, label, the parent's
    label for a cascading list, order and standing, in the list's order. The list reads its table
    through a query so that *Order* sorts as a number, as the drop-downs order it (the form-row
    binder sorts every column as text)."""
    plan = doc.get(PLAN_KEY) or {}
    out = []
    for vid in plan.get("datalists", []):
        info = plan["vocab"][vid]
        cols = [{"id": "code", "label": "Code"}, {"id": "name", "label": "Label"}]
        if info["parent"]:
            pname = next((v.get("name") for v in doc.get("vocabularies", [])
                          if v["id"] == info["parent"]), None) or info["parent"]
            col = {"id": "parent_code", "label": pname}
            if info["parent_form"]:
                col["formatter"] = {"type": "optionsValue", "formDefId": info["parent_form"],
                                    "idColumn": "code", "labelColumn": "name"}
            cols.append(col)
        if info.get("groups"):
            cols.append({"id": "group_code", "label": info["group_name"],
                         "formatter": {"type": "optionsValue", "formDefId": info["group_form"],
                                       "idColumn": "code", "labelColumn": "name"}})
        cols += [{"id": "sort_order", "label": "Order"},
                 {"id": "standing", "label": "Standing",
                  "formatter": {"type": "status_badge",
                                "tones": {IN_FORCE: "green", RETIRED: "grey"}}}]
        spec = {"datalist": {"id": info["datalist"], "name": info["name"],
                             "binder": {"type": "jdbc", "primaryKey": "id",
                                        "sql": datalist_sql(doc, info)},
                             "columns": cols, "sort": {"column": "sort_order", "desc": False}}}
        out.append((pathlib.Path(FEATURE) / "datalists" / f"DL-{info['datalist']}.spec.yml", spec))
    return out


# --------------------------------------------------------------------------- #
# The script at the head of every form that holds a maintained drop-down       #
# --------------------------------------------------------------------------- #

_SCRIPT = """<script>
(function ($) {
  if (!$) { return; }
  var LOV = %(lov)s;
  function parts(o) {
    /* grouping: [parent;]standing;order[;category;its label;its order;its standing] — the
       parent before the value's standing, the category after its order (a divided list). */
    var g = (o.getAttribute("grouping") || "").split(";"), i = -1, k;
    for (k = 0; k < g.length; k++) {
      if (g[k] === "%(in)s" || g[k] === "%(out)s") { i = k; break; }
    }
    function at(n) { return (i >= 0 && g.length > i + n) ? g[i + n] : ""; }
    return { p: i > 0 ? g.slice(0, i).join(";") : "", s: i >= 0 ? g[i] : "%(in)s",
             o: at(1) === "" ? NaN : parseFloat(at(1)),
             c: at(2), cl: at(3), co: at(4) === "" ? NaN : parseFloat(at(4)),
             cs: at(5) || "%(in)s" };
  }
  function byOrder(a, b) {
    var ao = isNaN(a.o) ? 1e9 : a.o, bo = isNaN(b.o) ? 1e9 : b.o;
    if (ao !== bo) { return ao - bo; }
    return a.l < b.l ? -1 : (a.l > b.l ? 1 : 0);
  }
  function find(id) {
    return $("select").filter(function () {
      var n = this.name || "";
      return n === id || (LOV.suffix[id] && n.slice(-(id.length + 1)) === "_" + id);
    });
  }
  function sv(s) {
    /* The value the drop-down holds. Not jQuery's .val(): on a read-only drop-down Joget marks
       every option disabled, and .val() gives nothing for a chosen option that is disabled,
       while the browser still knows which option is chosen. Failing that, the hidden field
       Joget writes beside a read-only drop-down (selectBox.ftl) holds the value. */
    if (!s) { return ""; }
    var o = s.selectedIndex >= 0 ? s.options[s.selectedIndex] : null;
    if (o && o.value !== "") { return o.value; }
    var h = $(s).siblings("input[type=hidden]").filter(function () { return this.name === s.name; });
    return h.length ? (h.first().val() || "") : (o ? o.value : "");
  }
  function wire(id, pid, cat) {
    find(id).each(function () {
      var s = this, ro = !!s.disabled, orig = sv(s), all = [], c = null;
      $(s).find("option").each(function () {
        var t = parts(this);
        all.push({ v: this.value, l: $(this).text(), g: this.getAttribute("grouping") || "",
                   p: t.p, s: t.s, o: t.o, c: t.c, cl: t.cl, co: t.co, cs: t.cs });
      });
      if (cat) {
        /* A divided list (UX-01 IDR-05): the person chooses the category first, then the value
           within it. The category is a drop-down of the page only — it has no name, so it is
           never sent and never stored — set from the stored value when the record opens. It
           offers the categories in force that hold a value in force, and the record's own. */
        var mine = "", seen = {}, cats = [];
        all.forEach(function (x) { if (x.v !== "" && x.v === orig) { mine = x.c; } });
        all.forEach(function (x) {
          if (x.v === "" || x.c === "" || seen[x.c]) { return; }
          if (x.c !== mine && (x.cs === "%(out)s" || x.s === "%(out)s")) { return; }
          seen[x.c] = true;
          cats.push({ v: x.c, l: x.cl || x.c, o: x.co });
        });
        cats.sort(byOrder);
        c = $("<select/>").addClass("kit-lov-category").attr("aria-label", cat)
          .attr("title", cat).css("margin-right", "6px");
        c.append($("<option/>").attr("value", "").text(""));
        cats.forEach(function (x) {
          var op = $("<option/>").attr("value", x.v).text(x.l);
          if (x.v === mine) { op.prop("selected", true).attr("selected", "selected"); }
          c.append(op);
        });
        if (ro) { c.prop("disabled", true).attr("disabled", "disabled"); }
        $(s).before(c);
        c.on("change", function () { draw(); $(s).trigger("change"); });
      }
      function draw() {
        var cur = ro ? orig : sv(s), pv = pid ? sv(find(pid).get(0)) : null;
        var cv = c ? (c.val() || "") : null;
        var keep = all.filter(function (x) {
          if (x.v === "") { return true; }
          if (pv !== null && x.p !== pv) { return false; }
          if (cv !== null && x.c !== cv) { return false; }
          return x.s !== "%(out)s" || x.v === orig;
        });
        keep.sort(function (a, b) {
          if (a.v === "") { return -1; }
          if (b.v === "") { return 1; }
          return byOrder(a, b);
        });
        $(s).empty();
        keep.forEach(function (x) {
          var op = $("<option/>").attr("value", x.v).attr("grouping", x.g).text(x.l);
          if (x.v === cur) { op.prop("selected", true).attr("selected", "selected"); }
          if (ro) { op.prop("disabled", true).attr("disabled", "disabled"); }
          $(s).append(op);
        });
      }
      draw();
      if (pid) {
        $(document).on("change", "select", function () {
          if (find(pid).is(this)) { draw(); $(s).trigger("change"); }
        });
      }
    });
  }
  $(function () {
    for (var i = 0; i < LOV.fields.length; i++) {
      wire(LOV.fields[i][0], LOV.fields[i][1], LOV.fields[i][2] || "");
    }
  });
})(window.jQuery);
</script>"""


def script_html(fields: list, suffix: dict) -> str:
    """The script for [(field id, parent field id or '')] or [(field id, parent, category)] — the
    category being the name of a divided list's categories (item 7); `suffix` says, per field id,
    whether a prefixed parameter name (a sub-form's `<prefix>_<id>`) may also be matched."""
    payload = json.dumps({"fields": [list(x) for x in fields], "suffix": suffix},
                         sort_keys=True, separators=(",", ":"))
    return _SCRIPT % {"lov": payload, "in": IN_FORCE, "out": RETIRED}


def attach_script(spec: dict, doc: dict) -> bool:
    """Place the script at the head of a form spec that holds a drop-down over a maintained
    vocabulary. Returns whether it did. Run on every form spec a model form becomes (a
    record console and each of its tabs), because each is loaded on its own."""
    forms = (doc.get(PLAN_KEY) or {}).get("forms") or {}
    secs = spec.get("sections") or []
    flds = [f for s in secs for f in (s.get("fields") or [])]
    if not forms or not flds or any(f.get("id") == SCRIPT_FIELD for f in flds):
        return False
    ids = [f.get("id") for f in flds if f.get("id")]
    found = []
    for f in flds:
        info = forms.get((f.get("lookup") or {}).get("formDefId"))
        if f.get("type") != "select" or not info:
            continue
        parent = ""
        if info["parent_form"]:
            parent = next((g["id"] for g in flds
                           if (g.get("lookup") or {}).get("formDefId") == info["parent_form"]), "")
        vinfo = ((doc.get(PLAN_KEY) or {}).get("vocab") or {}).get(info["vocab"]) or {}
        if vinfo.get("groups"):
            found.append((f["id"], parent, vinfo.get("group_name") or vinfo["groups"]))
        else:
            found.append((f["id"], parent))
    if not found:
        return False
    watched = {x for pair in found for x in pair[:2] if x}
    suffix = {i: not any(o != i and o.endswith("_" + i) for o in ids) for i in sorted(watched)}
    secs[0].setdefault("fields", []).insert(0, {"id": SCRIPT_FIELD, "type": "html",
                                                "html": script_html(found, suffix)})
    return True
