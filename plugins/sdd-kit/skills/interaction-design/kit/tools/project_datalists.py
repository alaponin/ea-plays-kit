#!/usr/bin/env python3
"""Project Layer-2 datalist specs (gen_datalists input) from a Layer-1 application model.

Pure, deterministic projection:
    validated application model (L1)  ->  <out>/<feature>/datalists/DL-<listId>.spec.yml (L2)

Same contract as the forms projector (tools/project_forms.py): validate first (refuse
invalid input), pure function of the document (byte-identical output for identical input),
provenance-stamped, and valid L1 constructs with no realization in gen_datalists are
refused loudly (totality rule) — never silently dropped. Dispositions are logged in
docs/PROJECTION-DECISIONS.md; the L1->L2 map is tools/MAPPING-datalists.md.

Scope (v0.1): both source paths are projected and proven by oracle round-trip — the QUERY
source (JDBC binder) against a shipped query list (ADR-018), and the ENTITY source (form-row
binder) against a shipped case list (ADR-019; DL-01 in docs/PROJECTION-DECISIONS.md).

Row acts: `link` is a raw hyperlink; `open_form` resolves to the CRUD menu the userview
projection makes for the target form (DL-06), and is refused when the model declares none.

Usage:
    project_datalists.py <app.yaml> --out <dir> [--feature <id>] [--schema <schema.yaml>]

Exit codes: 0 ok · 1 schema errors · 2 lint errors · 3 projection errors.
"""
from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import sys

import yaml

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import validate as l1
import custody  # tools/validate.py — the single validation entry point
import project_userview as uvp  # the userview projector: its CRUD menu resolution is shared, not copied
import lov  # the administration of lists of values (METHOD-2026-09-25-02)

PROJECTOR = "project_datalists.py"
PROJECTOR_VERSION = "0.1.0"

# gen_datalists filter types it can realize (SelectBox / TextField / DateRange). Everything
# else in the L1 enum needs a plugin filter gen_datalists does not emit — refused (totality).
# `status` is sugar: a select whose options are the entity's lifecycle states.
FILTER_TYPES = {"text", "select", "date_range"}
# Column formats gen_datalists realizes on a query column.
QUERY_FORMATS = {"none", "date", "datetime"}
# Row-action kinds realizable: a raw hyperlink, and a row that opens a form, which resolves
# to the CRUD menu the userview projection makes for that form (DL-06, 24 Sep 2026).
# launch_process / execute_transition / delete have no generator element — refused.
LINK_ACTION = "link"
OPEN_FORM_ACTION = "open_form"
# The neutral generator names a CrudMenu `<datalistId>_crud`
# (joget-platform-plugins reference-app/generators/gen_userview.py, crud_menu). The datalistId
# comes from project_userview.project_menu, called below; only this suffix lives in the
# generator, and tests/test_datalists_open_form.py runs that generator to prove the two agree.
CRUD_ID_SUFFIX = "_crud"


class ProjectionError(Exception):
    """A valid L1 construct this projector cannot (yet) realize in L2."""


# A date column shows the date in the application's one date convention, the one its forms' date
# controls show (project_forms.date_format; METHOD-2026-09-25-01, item 22). The convention is
# written in the DatePicker's dialect (`dd` the day, `mm` the month, `yy` the four-digit year;
# delta D-057); the list's DateFormatter reads Java's, so each admitted form has its Java pattern.
# The schema admits these three and no other (application-model.schema.yaml, app.conventions).
DEFAULT_DATE_FORMAT = "dd/mm/yy"
JAVA_DATE_PATTERN = {"dd/mm/yy": "dd/MM/yyyy", "dd.mm.yy": "dd.MM.yyyy", "dd-mm-yy": "dd-MM-yyyy"}


def date_pattern(ix: "Index", with_time: bool = False, path: str = "app/conventions") -> str:
    conv = str(((ix.doc.get("app") or {}).get("conventions") or {}).get("date_format")
               or DEFAULT_DATE_FORMAT)
    if conv not in JAVA_DATE_PATTERN:
        raise ProjectionError(f"{path}: date_format '{conv}' has no list pattern (admitted: "
                              f"{', '.join(JAVA_DATE_PATTERN)})")
    # METHOD-2026-09-26-02, point 5: a date and time is shown DD/MM/YYYY HH:mm, as the forms'
    # date-and-time control shows it (project_forms.DATETIME_PROPS); it was shown with its seconds
    return JAVA_DATE_PATTERN[conv] + (" HH:mm" if with_time else "")


# The format a date and time is stored in, as the column reads it before it shows it: the forms'
# control stores yyyy-MM-dd HH:mm, and joget-transition-guard writes a moment it sets as
# yyyy-MM-dd HH:mm:ss. The formatter parses the stored value from its start (SimpleDateFormat),
# so this one pattern reads both; the generator's own default for a pattern with the time,
# yyyy-MM-dd HH:mm:ss, would leave a value stored without seconds unread and shown as stored.
STORED_DATETIME = "yyyy-MM-dd HH:mm"


class Index:
    def __init__(self, doc: dict, app_path=None):
        self.doc = doc
        self.app_path = app_path        # where a list's `file` of values is read from
        self.entities = {e["id"]: e for e in doc.get("entities", [])}
        self.queries = {q["id"]: q for q in doc.get("queries", [])}
        self.vocabularies = {v["id"]: v for v in doc.get("vocabularies", [])}
        self.forms_by_entity: dict[str, list[dict]] = {}
        for f in doc.get("forms", []):
            self.forms_by_entity.setdefault(f["entity"], []).append(f)
        self.forms = {f["id"]: f for f in doc.get("forms", [])}
        self.lists = {x["id"]: x for x in doc.get("lists", [])}
        self.app_id = (doc.get("app") or {}).get("id")
        self.userview_id = (doc.get("navigation") or {}).get("userview_id")
        self.crud_by_form, self.crud_refused = _crud_menus(doc)


def _crud_menus(doc: dict) -> tuple[dict[str, list[dict]], list[str]]:
    """The CRUD menus the userview projection makes, keyed by the form each opens an existing
    row with, in navigation order. Each menu is resolved by project_userview.project_menu
    itself, so its form, edit form and list are the ones the userview projection carries.
    A CrudMenu opens a row with its edit form, and with its form when it has none (gen_userview
    crud_menu: `editFormId or formId`; tools/totality.py check_crud_edit_form mirrors the same).
    Returns (menus by form, paths of CRUD menus the userview projector itself refuses)."""
    by_form: dict[str, list[dict]] = {}
    refused: list[str] = []
    uix = uvp.Index(doc)
    for cat in (doc.get("navigation") or {}).get("categories", []):
        for m in cat.get("menus", []):
            if m.get("type") != "crud":
                continue
            path = f"navigation/{cat['id']}/{m.get('label')}"
            try:
                spec = uvp.project_menu(m, uix, path)
            except uvp.ProjectionError:
                refused.append(path)
                continue
            by_form.setdefault(spec.get("editFormId") or spec["formId"], []).append(spec)
    return by_form, refused


def crud_menu_id(menu_spec: dict) -> str:
    """The customId of a CRUD menu as the userview projection names it (see CRUD_ID_SUFFIX)."""
    return f"{menu_spec['datalistId']}{CRUD_ID_SUFFIX}"


def _humanize(code: str) -> str:
    return code.replace("_", " ").strip().capitalize() if code else code


def _derive_select_options(flt: dict, ix: Index, entity: dict | None, path: str):
    """A select filter with no explicit `options` derives them from the model: the entity's
    lifecycle states when the attr is its status_attr, else an enum attr's vocabulary rows.
    Returns a list of {value,label} or None (no derivation → a plain select, '- any -' only)."""
    attr_id = flt.get("attr")
    if not entity or not attr_id:
        return None
    lc = entity.get("lifecycle") or {}
    if lc.get("status_attr") == attr_id:
        # a state is offered by its name, as the state model names it (item 1)
        return [{"value": s["id"], "label": s.get("name") or _humanize(s["id"])}
                for s in lc.get("states", [])]
    a = {x["id"]: x for x in entity.get("attributes", [])}.get(attr_id)
    if a and a.get("type") == "enum" and a.get("vocabulary"):
        v = ix.vocabularies.get(a["vocabulary"])
        if not v:
            raise ProjectionError(f"{path}: attr '{attr_id}' references unknown vocabulary "
                                  f"'{a['vocabulary']}'")
        code_is_label = bool(v.get("display_code"))
        return [{"value": r["code"], "label": r["code"] if code_is_label else r.get("name", r["code"])}
                for r in v.get("rows", [])]
    return None


# --------------------------------------------------------------------------- #
# Column / filter / action projection                                          #
# --------------------------------------------------------------------------- #

def _options_formatter(attr: dict, ix: Index, path: str) -> dict:
    """OptionsValueFormatter over the form bound to the attribute's referenced entity."""
    if attr.get("type") != "ref":
        raise ProjectionError(
            f"{path}: column format 'options' needs a `ref` attribute (to derive the "
            f"lookup form); attribute type is '{attr.get('type')}'")
    target_id = attr["ref"]["entity"]
    target = ix.entities[target_id]
    forms = ix.forms_by_entity.get(target_id, [])
    if len(forms) != 1:
        raise ProjectionError(
            f"{path}: ref to '{target_id}' needs exactly one bound form to derive the "
            f"options formDefId (found {len(forms)})")
    fmt = {"type": "optionsValue", "formDefId": forms[0]["id"]}
    pk_attr = (target.get("pk") or {}).get("attr")
    if pk_attr:
        fmt["idColumn"] = pk_attr
    if attr["ref"].get("display"):
        fmt["labelColumn"] = attr["ref"]["display"]
    return fmt


def _status_badge_formatter(cid: str, entity: dict | None, path: str) -> dict:
    """A lifecycle-aware badge: derive a value→tone map from the entity's lifecycle states.
    Each state's `tone` wins; absent → grey (initial) / green (terminal) / amber (intermediate).
    gen_datalists renders this as a BeanShellFormatter emitting a coloured HTML pill."""
    lc = (entity or {}).get("lifecycle") or {}
    if not lc or lc.get("status_attr") != cid:
        raise ProjectionError(
            f"{path}: column format 'status_badge' must be on the entity's lifecycle status_attr "
            f"(status_attr is {lc.get('status_attr')!r}) — it colours the state value")
    tones = {}
    for s in lc.get("states", []):
        tones[s["id"]] = s.get("tone") or (
            "grey" if s.get("initial") else "green" if s.get("terminal") else "amber")
    return {"type": "status_badge", "tones": tones}


# METHOD-2026-09-25-04, item 6 (row 16): the two hash variables a first-paint scope may name —
# the person signed in and the page's record — with any quotes and escape the model gave them.
_SCOPE_TOKEN = re.compile(r"'?#(currentUser\.username|requestParam\.[A-Za-z_]\w*)(?:\?sql)?#'?")


def _qualify_predicate(where: str, attr_ids: list[str]) -> str:
    """Prefix bare attribute identifiers with `e.customProperties.` so a form-row binder can use
    the predicate as HQL. Longest ids first so 'status' does not corrupt 'status_date'; an
    already-qualified reference is left alone.

    The scope may name `#currentUser.username#` and `#requestParam.<name>#` (item 6; lint L020).
    Each is held out of the qualification, and written back as a quoted literal escaped for SQL
    (`'#requestParam.case?sql#'`): the platform resolves it when the list is read, a value the
    address carries cannot close the quote, and an attribute that shares a name with the
    parameter is not mistaken for it."""
    held: list = []

    def _hold(m):
        held.append(m.group(1))
        return f"\x00{len(held) - 1}\x00"

    out = _SCOPE_TOKEN.sub(_hold, where or "")
    for aid in sorted(attr_ids, key=len, reverse=True):
        out = re.sub(rf"(?<![\w.]){re.escape(aid)}(?![\w])", f"e.customProperties.{aid}", out)
    return re.sub(r"\x00(\d+)\x00", lambda m: f"'#{held[int(m.group(1))]}?sql#'", out)


def project_column(col: dict, ix: Index, attrs: dict, is_query: bool,
                   entity: dict | None, path: str, joined: set | None = None) -> dict:
    fmt = col.get("format", "none")
    if is_query:
        cid = col.get("expr")
        if not cid:
            raise ProjectionError(f"{path}: a query-source column needs `expr` (the SQL column alias)")
        if fmt not in QUERY_FORMATS:
            raise ProjectionError(
                f"{path}: column format '{fmt}' has no realization on a query column in "
                f"gen_datalists (only none/date/datetime; options/status_badge need an entity "
                f"source, currency/link are unrealized — totality register)")
        a = {}
    elif "expr" in col and joined:
        # source.joins (2026-08-08): a `<joinedTable>.<column>` expression is
        # legal exactly when its prefix names a DECLARED join's table — the
        # deployed reference-portal registers are AdvancedFormRowDataListBinder
        # lists whose columns all read through the binder joins. Formats follow
        # the query-column rules (the value arrives as a joined cell).
        cid = col["expr"]
        prefix = cid.split(".", 1)[0]
        if prefix not in joined:
            raise ProjectionError(
                f"{path}: expression column '{cid}' reads through '{prefix}', which "
                f"is not the table of a declared source.joins entity (declared: "
                f"{', '.join(sorted(joined))})")
        if fmt not in QUERY_FORMATS:
            raise ProjectionError(
                f"{path}: column format '{fmt}' has no realization on a joined "
                f"column (only none/date/datetime)")
        a = {}
    else:
        cid = col.get("attr")
        if not cid:
            raise ProjectionError(
                f"{path}: an entity-source column needs `attr` (an `expr` column "
                f"needs the list to declare `source.joins` naming its form)")
        a = attrs.get(cid, {})
        if fmt in ("currency", "link"):
            raise ProjectionError(
                f"{path}: column format '{fmt}' has no formatter in gen_datalists "
                f"(currency/link are unrealized — totality register)")
    out = {"id": cid, "label": col.get("label", cid)}
    if fmt == "date":
        out["formatter"] = {"type": "date", "format": date_pattern(ix)}
    elif fmt == "datetime":
        out["formatter"] = {"type": "date", "format": date_pattern(ix, with_time=True),
                            "dataFormat": STORED_DATETIME}
    elif fmt == "options" and a.get("type") == "enum":
        lab = lov.label_formatter_for(ix.doc, a.get("vocabulary")) or \
            _fixed_label_formatter(ix, a.get("vocabulary"), path)
        out["formatter"] = lab
    elif fmt == "options":
        out["formatter"] = _options_formatter(a, ix, path)
    elif fmt == "status_badge":
        out["formatter"] = _status_badge_formatter(cid, entity, path)
    elif fmt == "none" and a.get("type") == "enum":
        # METHOD-2026-09-25-04, item 1 (the lists-of-values report, "Found, not fixed", item 4):
        # a column of a coded value shows its label, read from the list's own table when the list
        # is shown, so a value relabelled or retired in the administration shows as it stands.
        # METHOD-2026-09-26-02, point 19 (a): a FIXED list shows its label too, from its values.
        lab = lov.label_formatter_for(ix.doc, a.get("vocabulary"))
        if not lab:
            v = ix.vocabularies.get(a.get("vocabulary")) or {}
            if v and not v.get("display_code"):
                lab = _fixed_label_formatter(ix, v["id"], path)
        if lab:
            out["formatter"] = lab
    return out


def _fixed_label_formatter(ix: Index, vid, path: str) -> dict:
    """METHOD-2026-09-26-02, point 19 (a): the column over a field bound to a FIXED list shows
    the value's label. A fixed list keeps its values in the model and has no table to read, so
    its values and labels are written into the column's formatter: the platform's own
    OptionsValueFormatter reads its `options` grid of value and label (jw-enterprise-plugins
    9.0.7, OptionsValueFormatter.getOptionMap), which the pinned gen_datalists (registry 0.11.0)
    writes from the spec's `options`. A list that shows its code (display_code) shows the code.
    Until this round the column was refused ("a fixed list has no table to read its labels
    from"), and a model that fixed a list the design fixes lost its labels (an issue found in testing)."""
    v = ix.vocabularies.get(vid)
    if v is None:
        raise ProjectionError(f"{path}: the column's list '{vid}' is not a list of the model")
    try:
        rows = lov.rows_of(v, ix.app_path)
    except lov.LovError as exc:
        raise ProjectionError(f"{path}: the labels of the fixed list '{vid}' cannot be read: {exc}")
    code_is_label = bool(v.get("display_code"))
    return {"type": "optionsValue",
            "options": [{"value": str(r["code"]),
                         "label": str(r["code"] if code_is_label else r.get("name", r["code"]))}
                        for r in rows]}


def project_filter(flt: dict, ix: Index, entity: dict | None, path: str) -> dict:
    ftype = flt["type"]
    if ftype == "status":                         # sugar → a lifecycle-driven select
        if not (entity and (entity.get("lifecycle") or {}).get("status_attr")):
            raise ProjectionError(f"{path}: filter type 'status' needs the source entity to have a "
                                  f"lifecycle with a status_attr")
        ftype = "select"
    if ftype not in FILTER_TYPES:
        raise ProjectionError(
            f"{path}: filter type '{ftype}' is not realizable in gen_datalists "
            f"(only text/select/status/date_range; cascading_select needs a plugin filter "
            f"type gen_datalists does not emit — totality register)")
    fid = flt.get("expr") or flt.get("attr")
    if not fid:
        raise ProjectionError(f"{path}: a filter needs `expr` (query column) or `attr`")
    out = {"id": fid, "label": flt.get("label", fid), "type": ftype}
    if flt.get("param"):
        out["param"] = flt["param"]
    if ftype == "select":
        opts = list(flt.get("options", []))
        if not opts:                              # derive from lifecycle states / enum vocabulary
            derived = _derive_select_options(flt, ix, entity, path)
            if derived is not None:
                opts = derived
        out["options"] = opts
        # METHOD-2026-09-26-02, point 4: a filter over a list the application maintains reads the
        # list while the application runs, through the options binder the form's drop-down over
        # it has (lov.filter_binder), so it offers the values in force, in their order, as they
        # stand when the list is shown — not the values written into it at the build. The inline
        # options stay beneath it, as the values the build knew.
        attr = ({a["id"]: a for a in (entity or {}).get("attributes", [])}.get(flt.get("attr"))
                or {}) if not flt.get("expr") else {}
        vid = attr.get("vocabulary") if attr.get("type") == "enum" else None
        if vid and not flt.get("options") and lov.filter_binder(ix.doc, vid):
            v = ix.vocabularies.get(vid) or {}
            if not v.get("groups"):
                out["optionsBinder"] = lov.filter_binder(ix.doc, vid)
                return out
            return _divided_filter(out, v, ix, entity, path)
    return out


def _divided_filter(out: dict, v: dict, ix: Index, entity: dict, path: str) -> list:
    """A filter over a DIVIDED list is chosen in two steps: the category, then the value within
    it (the ruling on long lists; point 4). The category's filter comes first and names nothing;
    the value's filter names it as its control, and the platform then offers only the values
    whose category — the third column of the value's binder — is the one chosen (gen_datalists
    0.11.0, `controlField`). Like every filter, the category's narrows the list's rows by its own
    column, so the rows must carry the category: the category's filter stands on the attribute of
    the list's record that holds a value of the list of categories. A record that holds none
    cannot be narrowed by category, and a filter over its divided list is refused rather than
    offered as one step of more than nine values (UX-01 IDR-05)."""
    groups = v["groups"]
    cat = next((a for a in (entity or {}).get("attributes", [])
                if a.get("type") == "enum" and a.get("vocabulary") == groups), None)
    if cat is None:
        raise ProjectionError(
            f"{path}: the filter over {out['id']} reads the list {v.get('name') or v['id']}, which "
            f"is divided into the categories of {groups}, so it is chosen in two steps: the "
            f"category, then the value. The platform's filter narrows the list's rows by the "
            f"category as well, and the record {(entity or {}).get('id')} holds no value of "
            f"{groups} to narrow them by. Give the record an attribute bound to {groups} that "
            f"holds the category of its {out['id']}, or leave the filter out; one step would offer "
            f"more than nine values (UX-01 IDR-05)")
    gv = ix.vocabularies.get(groups) or {}
    first = {"id": cat["id"], "label": gv.get("name") or cat.get("name") or cat["id"],
             "type": "select", "options": _derive_select_options(
                 {"attr": cat["id"]}, ix, entity, path) or [],
             "optionsBinder": lov.filter_binder(ix.doc, groups)}
    out["optionsBinder"] = lov.filter_binder(ix.doc, v["id"], with_category=True)
    out["controlField"] = cat["id"]
    return [first, out]


def _open_form_action(act: dict, path: str, ix: Index, list_id: str) -> dict:
    """`open_form` → a row link into the CRUD menu that opens a row with the target form, in
    edit mode on this row's id — the shape a shipped list carries
    (`#request.contextPath#/web/userview/<app>/<userview>/_/<crud customId>?_mode=edit`,
    hrefColumn id, hrefParam id). Where several CRUD menus open rows with the form, the one
    whose list is this list wins, else the first in navigation order (DL-06)."""
    form = act.get("form")
    menus = ix.crud_by_form.get(form or "", [])
    if not menus:
        entity = (ix.forms.get(form or "") or {}).get("entity", "<the form's entity>")
        note = (f" (the userview projector refuses the CRUD menu(s) at "
                f"{', '.join(ix.crud_refused)}, so they make no menu)" if ix.crud_refused else "")
        raise ProjectionError(
            f"{path}: open_form opens form '{form}', and there is no CRUD menu in `navigation` "
            f"that opens a row with it{note} — declare one (type: crud, entity: '{entity}', "
            f"with form: '{form}' and no edit_form, or edit_form: '{form}') and the row "
            f"resolves to that menu; use type 'link' with an explicit href for a raw row link")
    own = [m for m in menus if m["datalistId"] == list_id]
    menu = (own or menus)[0]
    href = (f"#request.contextPath#/web/userview/{ix.app_id}/{ix.userview_id}/_/"
            f"{crud_menu_id(menu)}?_mode=edit")
    return {"label": act.get("label", "Open"), "href": href,
            "hrefColumn": act.get("href_column", "id"), "hrefParam": act.get("href_param", "id")}


# --------------------------------------------------------------------------- #
# Acts on another record, on a list, and on the rows chosen (METHOD-2026-09-28-07, the kit's    #
# gap G1). Each is the platform's hyperlink action (org.joget.apps.datalist.lib.               #
# HyperlinkDataListAction, wflow-core 9.0.7): on a row it links to `href` with `hrefParam` set  #
# to the row's value of `hrefColumn`; among the list's own actions it is a button over the      #
# list, and writes each chosen row's value of `hrefColumn`, joined by ';', into `hrefParam`     #
# (its executeAction). The menu an act opens and the parameter the opened form reads are found #
# as a form's act finds them (project_forms._menu_for_form and _carried_param), so that one     #
# act opens one form one way from a row, from the rows chosen and from a record.               #
# --------------------------------------------------------------------------- #
OPEN_LIST_ACTION = "open_list"


def _uv_href(ix: Index, menu: str, add: bool = False) -> str:
    return (f"#request.contextPath#/web/userview/{ix.app_id}/{ix.userview_id}/_/{menu}"
            + ("?_mode=add" if add else ""))


def _row_key(ix: Index, lst: dict) -> str:
    """The column that names a row's own record as a reference to it is read: its business key
    (`pk.attr`) where the row's entity has one, else the row's identifier."""
    ent = ix.entities.get(l1.list_record_entity(lst, ix.doc) or "") or {}
    return l1.ref_key(ent) or "id"


def _form_menu(ix: Index, form: str, path: str):
    import project_forms as pfm
    try:
        return pfm._menu_for_form(ix.doc, form, path)
    except pfm.ProjectionError as exc:
        raise ProjectionError(str(exc))


def _form_param(ix: Index, target: dict, carried: str, path: str) -> str:
    import project_forms as pfm
    try:
        return pfm._carried_param(target, carried, ix, path)
    except pfm.ProjectionError as exc:
        raise ProjectionError(str(exc))


def _open_form_carrying(act: dict, path: str, ix: Index, lst: dict) -> dict:
    """`open_form` naming the record it carries (`record`, `carries`): the form opened is either a
    form of that record — the row opens it in the CRUD menu that edits a row with the form, by the
    record's row identifier, which the column holds — or a form that makes or reads a record for
    it, which the row opens through the menu that opens the form, in the parameter the form reads
    the record from, as a form's act does."""
    form = act.get("form") or ""
    target = ix.forms.get(form)
    if target is None:
        raise ProjectionError(f"{path}: open_form opens form '{form}', which is not in the model")
    carried = l1.row_act_carries(act, lst, ix.doc) or target.get("entity")
    col = act.get("record")
    if carried == target.get("entity"):
        menus = ix.crud_by_form.get(form, [])
        if not menus:
            raise ProjectionError(
                f"{path}: open_form opens form '{form}' on the record of '{carried}' the row names, "
                f"and there is no CRUD menu in `navigation` that opens a row with it — declare one "
                f"(type: crud, with form or edit_form '{form}') in a category with `hidden: true`")
        ent_id = l1.list_record_entity(lst, ix.doc)
        if col and ent_id:
            a = {x["id"]: x for x in (ix.entities.get(ent_id) or {}).get("attributes", [])}.get(col)
            held = ix.entities.get(((a or {}).get("ref") or {}).get("entity") or "") or {}
            if not a or a.get("type") != "ref" or l1.ref_key(held):
                raise ProjectionError(
                    f"{path}: open_form opens form '{form}' on the record the column '{col}' names, "
                    f"and a CRUD menu opens a row by its identifier: "
                    + (f"'{col}' is no reference of '{ent_id}'" if not a or a.get("type") != "ref"
                       else f"'{col}' holds the record's key ({l1.ref_key(held)}), not its "
                            f"identifier")
                    + " — source the list from a query that gives the record's identifier in a "
                      "column, and name that column")
        menu = next((m for m in menus if m["datalistId"] == lst.get("id")), menus[0])
        return {"label": act.get("label", "Open"),
                "href": _uv_href(ix, crud_menu_id(menu)) + "?_mode=edit",
                "hrefColumn": col or "id", "hrefParam": "id"}
    menu, add = _form_menu(ix, form, path)
    param = _form_param(ix, target, carried, path)
    if not col:
        if carried != l1.list_record_entity(lst, ix.doc):
            raise ProjectionError(
                f"{path}: open_form carries a record of '{carried}', which is not the row's own; "
                f"name the column of the row that holds it (`record`)")
        col = _row_key(ix, lst)
    return {"label": act.get("label", "Open"), "href": _uv_href(ix, menu, add),
            "hrefColumn": col, "hrefParam": param}


def _open_list_action(act: dict, path: str, ix: Index, lst: dict) -> dict:
    """`open_list`: the list `list`, narrowed to the record the row names. The row's value goes in
    the address parameter `param`, which the list opened reads (#requestParam.<param>#, in its
    first-paint scope or its query); the list is opened through the menu that shows it."""
    lid, param = act.get("list") or "", act.get("param")
    target = ix.lists.get(lid)
    if target is None:
        raise ProjectionError(f"{path}: open_list opens the list '{lid}', which is not a list of "
                              f"the model")
    if not param:
        raise ProjectionError(f"{path}: open_list names no `param`, the address parameter the list "
                              f"'{lid}' reads the row's value from")
    reads = str(target.get("default_scope") or "")
    q = ix.queries.get((target.get("source") or {}).get("query") or "")
    reads += " " + str((q or {}).get("sql") or "")
    if f"#requestParam.{param}" not in reads:
        raise ProjectionError(
            f"{path}: open_list gives the list '{lid}' the row's value in the parameter '{param}', "
            f"and that list reads no such parameter — narrow it by #requestParam.{param}# in its "
            f"default_scope (or its query)")
    menu = None
    for cat in (ix.doc.get("navigation") or {}).get("categories", []):
        for m in cat.get("menus", []):
            if m.get("type") == "list" and m.get("list") == lid:
                menu = menu or lid
            elif m.get("type") == "crud" and m.get("list") == lid:
                menu = menu or f"{lid}{CRUD_ID_SUFFIX}"
    if menu is None:
        raise ProjectionError(f"{path}: open_list opens the list '{lid}', and no menu of the "
                              f"navigation shows it — place it on a menu of a category with "
                              f"`hidden: true`")
    return {"label": act.get("label", "Open"), "href": _uv_href(ix, menu),
            "hrefColumn": act.get("record") or _row_key(ix, lst), "hrefParam": param}


def chosen_action(ca: dict, path: str, ix: Index, lst: dict) -> dict:
    """An act on the rows chosen: a button over the list that opens the form `form` through the
    menu that opens it, carrying the chosen rows' records, joined by ';', in the parameter
    `param`, a field the form places (the platform gives a field the value of the address
    parameter of its name: FormUtil.getElementPropertyValue, wflow-core 9.0.7)."""
    form = ca.get("form") or ""
    target = ix.forms.get(form)
    if target is None:
        raise ProjectionError(f"{path}: the act '{ca.get('label')}' opens form '{form}', which is "
                              f"not in the model")
    placed = {f.get("attr") or f.get("id") for s in target.get("sections") or []
              for f in s.get("fields") or []}
    if ca.get("param") not in placed:
        raise ProjectionError(
            f"{path}: the act '{ca.get('label')}' carries the chosen records in '{ca.get('param')}', "
            f"which form '{form}' does not place — the form receives them in that field")
    menu, add = _form_menu(ix, form, path)
    return {"label": ca.get("label"), "href": _uv_href(ix, menu, add),
            "hrefColumn": ca.get("record") or _row_key(ix, lst), "hrefParam": ca["param"]}


def act_source_sql(lst: dict, ix: Index, path: str) -> tuple:
    """METHOD-2026-09-28-07 (the kit's gap G2): (the statement, the entity) of a list sourced from
    an act on chosen rows — the records of the list the act is taken on whose key the act's
    record holds in the field `param`, for the act the person signed in took last (its record's
    `createdby` and `datecreated`, the platform's own columns of every form's table). The key is
    the column the act carries (its `record`, else the row's key)."""
    ca, acted = l1.chosen_act(ix.doc, (lst.get("source") or {}).get("act"))
    if ca is None:
        raise ProjectionError(f"{path}: source.act names '{(lst.get('source') or {}).get('act')}', "
                              f"which is no act on chosen rows of the model (chosen_actions)")
    own = ((acted or {}).get("source") or {}).get("entity")
    ent = ix.entities.get(l1.row_act_carries(ca, acted, ix.doc) or "")
    if ent is None:
        raise ProjectionError(f"{path}: the act '{ca['id']}' is taken on the list "
                              f"'{acted.get('id')}', and names no entity whose records it carries "
                              f"(`carries`); the records it was taken on cannot be read")
    target = ix.forms.get(ca.get("form") or "") or {}
    act_ent = ix.entities.get(target.get("entity") or "")
    if act_ent is None:
        raise ProjectionError(f"{path}: the act '{ca['id']}' opens form '{ca.get('form')}', which "
                              f"records it on no entity of the model")
    attrs = {a["id"] for a in ent.get("attributes", [])}
    # the column each chosen value is compared with: the row's own attribute the act names, on a
    # list of the records it carries; else the carried record's key as a reference to it is read
    # (its business key, else its identifier)
    key = (ca.get("record") if ent["id"] == own and ca.get("record") else None) \
        or (l1.ref_key(ent) or "id")
    keycol = "r.id" if key == "id" else f"r.c_{key}"
    cols = []
    for c in lst.get("columns", []):
        if c.get("attr") not in attrs:
            raise ProjectionError(f"{path}: a list sourced from the act '{ca['id']}' shows the "
                                  f"records of '{ent['id']}', and '{c.get('attr') or c.get('expr')}' "
                                  f"is no attribute of it")
        cols.append(f"r.c_{c['attr']} AS {c['attr']}")
    latest = (f"(SELECT x.c_{ca['param']} FROM app_fd_{act_ent['table']} x WHERE x.createdby = "
              f"'#currentUser.username?sql#' ORDER BY x.datecreated DESC LIMIT 1)")
    db = ((ix.doc.get("app") or {}).get("platform") or {}).get("db")
    cond = (f"{keycol} = ANY (string_to_array({latest}, ';'))" if db == "postgres" else
            f"FIND_IN_SET({keycol}, REPLACE({latest}, ';', ',')) > 0")
    sql = f"SELECT r.id AS id, {', '.join(cols)} FROM app_fd_{ent['table']} r WHERE {cond}"
    return sql, ent


def project_action(act: dict, path: str, ix: Index, list_id: str, lst: dict | None = None) -> dict:
    lst = lst if lst is not None else ix.lists.get(list_id, {"id": list_id})
    if act["type"] == OPEN_FORM_ACTION and (act.get("record") or act.get("carries")):
        return _open_form_carrying(act, path, ix, lst)
    if act["type"] == OPEN_LIST_ACTION:
        return _open_list_action(act, path, ix, lst)
    if act["type"] == OPEN_FORM_ACTION:
        return _open_form_action(act, path, ix, list_id)
    if act["type"] != LINK_ACTION:
        raise ProjectionError(
            f"{path}: action type '{act['type']}' has no realization in gen_datalists — a row "
            f"act that launches a process, executes a transition or deletes has no generator "
            f"element (totality register, DL-04); a row that opens a form is `open_form`, and a "
            f"raw row link is type 'link' with an explicit href")
    if not act.get("href"):
        raise ProjectionError(f"{path}: a link action needs an explicit `href`")
    ra = {"label": act.get("label", "Open"), "href": act["href"]}
    if act.get("href_column"):
        ra["hrefColumn"] = act["href_column"]
    if act.get("href_param"):
        ra["hrefParam"] = act["href_param"]
    return ra


# --------------------------------------------------------------------------- #
# List projection                                                              #
# --------------------------------------------------------------------------- #

def project_list(lst: dict, ix: Index) -> dict:
    lid = lst["id"]
    path = f"lists/{lid}"
    src = lst["source"]
    is_query = "query" in src

    attrs: dict = {}
    entity_obj: dict | None = None
    extra_condition = None
    join_forms: set = set()
    if src.get("act"):
        # METHOD-2026-09-28-07 (the kit's gap G2): the records an act on chosen rows was taken
        # on, read by the platform's JDBC list binder from the statement the kit writes; the
        # columns are the attributes of those records, formatted as an entity list's are
        if lst.get("default_scope") or lst.get("extra_condition"):
            raise ProjectionError(f"{path}: a list sourced from an act shows the records the act "
                                  f"was taken on, and takes no default_scope or extra_condition")
        sql, entity_obj = act_source_sql(lst, ix, path)
        attrs = {a["id"]: a for a in entity_obj.get("attributes", [])}
        binder = {"type": "jdbc", "primaryKey": "id", "sql": sql}
    elif is_query:
        q = ix.queries.get(src["query"])
        if not q:
            raise ProjectionError(f"{path}: unknown query '{src['query']}'")
        if not q.get("sql"):
            raise ProjectionError(f"{path}: query '{src['query']}' has no sql")
        binder = {"type": "jdbc", "primaryKey": "id", "sql": q["sql"]}
        if lst.get("extra_condition"):
            raise ProjectionError(f"{path}: extra_condition applies to entity-source lists only "
                                  f"(query lists carry the predicate in the SQL)")
        if lst.get("default_scope"):
            raise ProjectionError(f"{path}: default_scope applies to entity-source lists only — "
                                  f"a query list carries its scope in the SQL. Refusing rather "
                                  f"than dropping it (see the note on default_scope below)")
    else:
        entity = ix.entities[src["entity"]]                 # lint L002 guarantees existence
        entity_obj = entity
        attrs = {a["id"]: a for a in entity.get("attributes", [])}
        candidates = ix.forms_by_entity.get(src["entity"], [])
        form_id = src.get("form")
        if form_id:
            if form_id not in {f["id"] for f in candidates}:
                raise ProjectionError(f"{path}: source.form '{form_id}' is not a form bound to "
                                      f"entity '{src['entity']}'")
        elif len(candidates) == 1:
            form_id = candidates[0]["id"]
        else:
            raise ProjectionError(
                f"{path}: entity '{src['entity']}' has {len(candidates)} forms; set source.form "
                f"to pick the form whose table the row binder reads")
        binder = {"type": "form", "formDefId": form_id}
        # source.joins (2026-08-08): the joined register. Each join names a child
        # ENTITY whose TABLE the binder joins on `<table>.<fk>` = parent `id` —
        # the exact AdvancedFormRowDataListBinder shape both deployed
        # reference-portal registers carry (the deployed join key is the table:
        # location_table, not the form id residencyForm). Validated here: the
        # entity must exist and the fk must be one of its attributes.
        joins = src.get("joins") or []
        jtables = []
        for j in joins:
            je = ix.entities.get(j.get("entity"))
            if je is None:
                raise ProjectionError(
                    f"{path}: source.joins names '{j.get('entity')}', which is "
                    f"not an entity in the model")
            jattrs = {a["id"] for a in je.get("attributes", [])}
            if j.get("fk") not in jattrs:
                raise ProjectionError(
                    f"{path}: source.joins on '{j.get('entity')}' joins by "
                    f"'{j.get('fk')}', which is not an attribute of that entity "
                    f"— no column to join on")
            jtables.append(je.get("table") or je["id"])
        if joins:
            binder["joins"] = [{"table": t, "fk": j["fk"]}
                               for t, j in zip(jtables, joins)]
        join_forms = set(jtables)
        # default_scope is REALIZED here as of 2026-08-02, and until then it was not realized
        # anywhere. `validate` U005 has required every list to declare it (or waive it) since
        # WRK-04, so every list in every app has been carrying a first-paint scope that was
        # silently dropped on the way to the binder: a reference app's "open work only" comment described
        # behaviour its app did not have, and registration's intake queue showed other people's
        # unsubmitted drafts. A check that demands a declaration nothing realizes is worse than no
        # check — it manufactures the appearance of a decision.
        # Both land on the same target, so they AND together: default_scope is the first-paint
        # scope the model asserts, extra_condition a hard binder predicate; a list may carry both.
        preds = [p for p in (lst.get("default_scope"), lst.get("extra_condition")) if p]
        joined = " AND ".join(f"({p})" for p in preds) if len(preds) > 1 else \
            (preds[0] if preds else None)
        # ...and QUALIFIED to HQL. The form-row binder resolves columns as
        # `e.customProperties.<attr>`, so a bare `status != 'draft'` matches nothing and the list
        # comes back EMPTY — which makes a scope that does not work indistinguishable from a
        # queue with no work in it. Found by driving the browser: the intake inbox went from
        # showing drafts to showing nothing at all. Same contract as the unique guard's scope
        # predicate (project_forms._qualify_predicate, ADR-072).
        extra_condition = _qualify_predicate(joined, list(attrs)) if joined else None

    columns = [project_column(c, ix, attrs, is_query, entity_obj,
                              f"{path}/columns/{i}",
                              joined=None if is_query else join_forms)
               for i, c in enumerate(lst["columns"])]
    filters = []
    for i, f in enumerate(lst.get("filters", [])):
        got = project_filter(f, ix, entity_obj, f"{path}/filters/{i}")
        # a filter over a divided list is two, the category's first (point 4); a filter the model
        # also names over the same category stands once, where the first of them stands
        for one in (got if isinstance(got, list) else [got]):
            if one["id"] not in {x["id"] for x in filters}:
                filters.append(one)
    row_actions = [project_action(a, f"{path}/actions/{i}", ix, lid, lst)
                   for i, a in enumerate(lst.get("actions", []))]
    list_actions = [chosen_action(a, f"{path}/chosen_actions/{i}", ix, lst)
                    for i, a in enumerate(lst.get("chosen_actions", []))]

    dl: dict = {"id": lid, "name": lst["name"], "binder": binder, "columns": columns}
    if extra_condition:
        dl["extraCondition"] = extra_condition
    if filters:
        dl["filters"] = filters
    if row_actions:
        dl["rowActions"] = row_actions
    if list_actions:
        # METHOD-2026-09-28-07: the acts on the rows chosen, the list's own actions (gen_datalists
        # writes them among the datalist's `actions`, where the platform shows each as a button)
        dl["actions"] = list_actions
    sort = lst.get("sort")
    if sort and sort.get("by"):
        dl["sort"] = {"column": sort["by"], "desc": sort.get("dir", "desc") == "desc"}
    return {"datalist": dl}


# --------------------------------------------------------------------------- #
# Emission (identical convention to project_forms.py)                          #
# --------------------------------------------------------------------------- #

def provenance_header(doc: dict, source_name: str, source_sha256: str) -> str:
    m = doc.get("model", {})
    return (
        "# =============================================================================\n"
        "# GENERATED — do not edit. Projected from the Layer-1 application model.\n"
        f"# projector:      {PROJECTOR} v{PROJECTOR_VERSION} (the spec kit)\n"
        f"# schema_version: {m.get('schema_version')}\n"
        f"# spec_version:   {m.get('spec_version')}\n"
        f"# source_model:   {source_name}\n"
        f"# source_sha256:  {source_sha256}\n"
        "# =============================================================================\n")


def emit(spec: dict, header: str, out_path: pathlib.Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    body = yaml.safe_dump(spec, sort_keys=False, default_flow_style=False,
                          allow_unicode=True, width=4096)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(header)
        fh.write(body)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("app", type=pathlib.Path)
    ap.add_argument("--out", type=pathlib.Path, required=True)
    ap.add_argument("--feature")
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
    lint = l1.Lint(doc).run()
    if lint:
        print(f"LINT:   {len(lint)} error(s) — refusing to project")
        for e in lint:
            print(f"  - {e}")
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

    source_sha256 = hashlib.sha256(args.app.read_bytes()).hexdigest()
    header = provenance_header(doc, args.app.name, source_sha256)
    header += custody.line(args.custody)
    try:
        doc = lov.augment(doc, args.app)    # the lists-of-values administration (lov.py)
    except lov.LovError as exc:
        print("PROJECT: 1 error(s) — nothing emitted")
        print(f"  - lists of values: {exc}")
        return 3
    ix = Index(doc, args.app)

    lists = doc.get("lists", [])
    if args.feature:
        lists = [l for l in lists if l.get("feature") == args.feature]

    projected, errors = [], []
    for lst in lists:
        try:
            spec = project_list(lst, ix)
        except ProjectionError as exc:
            errors.append(str(exc))
            continue
        feature_dir = lst.get("feature") or "_app"
        rel = pathlib.Path(feature_dir) / "datalists" / f"DL-{lst['id']}.spec.yml"
        projected.append((rel, spec))

    if errors:
        print(f"PROJECT: {len(errors)} error(s) — nothing emitted")
        for e in errors:
            print(f"  - {e}")
        return 3

    # the list of each maintained vocabulary (lov.py): code, label, parent, order, standing
    if not args.feature or args.feature == lov.FEATURE:
        projected += lov.datalist_specs(doc)

    for rel, spec in projected:
        emit(spec, header, args.out / rel)
        print(f"  + {rel.as_posix()}")
    print(f"{len(projected)} datalist spec(s) projected -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
