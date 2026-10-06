#!/usr/bin/env python3
"""Project Layer-2 form specs (form-generator input YAML) from a Layer-1 application model.

Pure, deterministic projection:
    validated application model (L1)  ->  <out>/<feature>/forms/F-<formId>.spec.yml (L2)

Contract:
  * Validates the model first via tools/validate.py (same package: schema + lint).
    Invalid input is refused — nothing is emitted.
  * Pure function of the input document: no clock, no network, no database, no
    environment reads. Identical input produces byte-identical output.
  * Provenance header (schema_version, spec_version, projector version, sha256 of
    the source model) is written as a comment block into every emitted file.
  * Emits ONLY the properties the model derives; every generator-supplied default
    that is deliberately omitted is listed in tools/MAPPING-forms.md.
  * Valid L1 constructs with no realization in the target generator's element set
    are refused with an explicit error (totality rule) — never silently dropped.
    The register of these constructs lives in docs/PROJECTION-DECISIONS.md.

Usage:
    project_forms.py <app.yaml> --out <dir> [--feature <id>] [--schema <schema.yaml>]

Exit codes: 0 ok · 1 schema errors · 2 lint errors · 3 projection errors.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import sys

import yaml

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import validate as l1
import custody  # tools/validate.py — the single validation entry point
import lov      # the administration of lists of values (METHOD-2026-09-25-02)
import acts     # the acts of a record: moves and forms opened from it (METHOD-2026-09-25-04)

PROJECTOR = "project_forms.py"
PROJECTOR_VERSION = "0.2.0"

# --------------------------------------------------------------------------- #
# Generator input contract (joget-form-gen "Output C" format, gen_forms.py).   #
# --------------------------------------------------------------------------- #

# Part of the generator's input contract: a field whose LABEL carries one of
# these phrases is rendered read-only unless the spec sets an explicit
# readonly/managed key. The projector never RELIES on this inference — it emits
# an explicit `readonly` whenever the model's intent differs from what the
# generator would infer — but it must know the rule so a display label can
# never silently flip a field's editability.
MANAGED_LABEL = re.compile(
    r"\b(set by|managed by|managed\)|copied from|on submit|by engine|by rollup|by the engine)\b",
    re.I)

# Human-readable fallback label from a snake_case id, so a form never shows a raw
# attribute id (e.g. "date_of_birth_inc"). Explicit field `label` or attribute
# `name` always win; this only fires when neither is given.
_LABEL_ABBR = {"tin": "TIN", "id": "ID", "nid": "NID", "no": "No.", "dob": "DoB",
               "vat": "VAT", "paye": "PAYE", "ltu": "LTU", "url": "URL", "api": "API"}
_LABEL_EXPAND = {"inc": "/ incorporation", "reg": "registration", "pct": "%"}

def humanize_label(fid: str) -> str:
    words = str(fid).split("_")
    out = []
    for i, w in enumerate(words):
        lw = w.lower()
        if lw in _LABEL_ABBR:
            out.append(_LABEL_ABBR[lw])
        elif lw in _LABEL_EXPAND:
            out.append(_LABEL_EXPAND[lw])
        elif i == 0:
            out.append(w[:1].upper() + w[1:])
        else:
            out.append(lw)
    return " ".join(out)

# L1 attribute type -> (default L2 field type, storeNumeric)
ATTR_TYPE_MAP = {
    "string":   ("textfield",  False),
    "text":     ("textarea",   False),
    "integer":  ("textfield",  True),
    "decimal":  ("textfield",  True),
    "boolean":  ("checkbox",   False),
    "date":     ("date",       False),
    # METHOD-2026-09-26-02, point 5: a date and time is the platform's DatePicker in its dateTime
    # mode, shown day first with the time (DD/MM/YYYY HH:mm; DATETIME_PROPS). It was a text field
    # showing the stored value, year first (an issue found in testing) — MAPPING-forms.md
    "datetime": ("date",       False),
    "enum":     ("select",     False),
    "ref":      ("select",     False),
    "file":     ("fileupload", False),
    "json":     ("textarea",   False),   # raw JSON payloads edit as multi-line text
}

# L1 control override -> L2 field type
CONTROL_MAP = {
    "text": "textfield", "textarea": "textarea", "number": "textfield",
    "select": "select", "radio": "radio", "checkbox": "checkbox",
    "date": "date", "datetime": "date", "hidden": "hidden",
    "id_generator": "id_generator", "file": "fileupload", "lookup": "select",
    "grid": "grid", "custom_html": "html",
    # `custom` (2026-08-08, owner full-fidelity objective): a deployed element
    # carried VERBATIM - config.element {className, properties} straight from
    # the export, realized untouched by gen_forms 0.9.12. Guarded: without a
    # config.element body the control still refuses (project_field).
    "custom": "verbatim",
    # `smart_search` (ADR-108, a delivery's hand-off of 5 October 2026, item 2): the class-name
    # pass-through the totality register named (D-10) — the pinned generator's search element,
    # joget-smart-search's SmartSearchElement, with the settings the model names in the field's
    # `config` (_smart_search_field). It left UNREALIZED_CONTROLS with this entry.
    "smart_search": "smart_search",
    # `wizard_slot` is positional, realized in project_form's section loop
    # (it needs the form's wizard block); reaching project_field with it is a bug.
}

# Valid L1 constructs with NO realization in the generator's element set.
# Totality rule: refuse loudly; extending the generator is a separate,
# regression-gated decision (docs/PROJECTION-DECISIONS.md).
UNREALIZED_CONTROLS = {"calculation", "concat", "embedded_list", "gis_polygon"}

# L2 field types whose generator element carries a readonly property.
READONLY_CAPABLE = {"textfield", "textarea", "select", "date", "grid"}
# Elements that are inherently non-user-editable: a model readonly intent is
# vacuously satisfied (P-BUG-01, docs/PROJECTION-DECISIONS.md).
READONLY_VACUOUS = {"id_generator", "hidden", "html"}
# L2 field types whose generator element derives a DefaultValidator from `required`.
REQUIRED_CAPABLE = {"textfield", "textarea", "select", "radio", "checkbox",
                    "date", "fileupload"}
# ADR-108 (a delivery's hand-off of 6 October 2026, item 1, F-B2-02): an attribute's `default` is the
# value of the element that places it. The generator writes a spec's `value` on these elements...
DEFAULT_BY_VALUE = {"textfield", "select", "radio", "date"}
# ...and writes an empty value on these whatever the spec says (gen_forms: HiddenField, TextArea,
# CheckBox, PopupSelectBox), so the default reaches them through `props`, which the generator
# merges into the element's properties last. Until then nothing stamped the moment a row was
# written on a screen form (a hidden field, or a date and time, with no value), and a row's
# version was a hidden field with no value.
DEFAULT_BY_PROPS = {"hidden", "textarea", "checkbox", "popupselect"}
# The settings the pinned search element reads from a field's `config` (gen_forms, `smart_search`);
# every other setting the model names for it is written through `props`.
SEARCH_CONFIG_KEYS = {"apiEndpoint", "apiId", "apiKey", "storeValue", "entityLabel",
                      "simpleSearch", "populate", "displayMode", "displayColumns",
                      "nationalIdPattern", "nationalIdMinLength", "autoSelectSingleResult",
                      "showRecents", "maxRecents"}


class ProjectionError(Exception):
    """A valid L1 construct this projector cannot (yet) realize in L2."""


# ---- how a value is shown (METHOD-2026-09-25-04, item 1) ------------------------------
# A date is shown day first: the DatePicker's own dialect (delta D-057), DD/MM/YYYY. The model's
# `app.conventions.date_format` may name another day-first form; the schema admits no other.
DEFAULT_DATE_FORMAT = "dd/mm/yy"
# A date and time (METHOD-2026-09-26-02, point 5; the ruling on the interaction design step, point
# 4): the DatePicker in its dateTime mode shows the date in the form above, a space, and the time
# in 24 hours, HH:mm (DatePicker.getTimeFormat, Joget DX 9.0.7: "HH:mm" when format24hr is "true",
# else "hh:mm a") — DD/MM/YYYY HH:mm. The value is stored, and read back, as yyyy-MM-dd HH:mm; a
# moment the transition guard writes with its seconds (yyyy-MM-dd HH:mm:ss) reads by the same
# pattern, which does not ask for the seconds.
# `dataFormat` is the DATE part only (ADR-108; a delivery's hand-off of 6 October 2026, item 2,
# F-B2-02): in its dateTime mode the platform stores `dataFormat + " " + getTimeFormat()`
# (DatePicker.formatData and formattedValue, jw-community wflow-core). It was yyyy-MM-dd HH:mm, so
# the time was written twice — `2026-10-04 15:30 15:30` on 71 fields of one application
# — a value the relay could not read as a moment (a delivery's finding OM-4).
DATETIME_PROPS = {"datePickerType": "dateTime", "format24hr": "true",
                  "dataFormat": "yyyy-MM-dd"}
# A yes-or-no the person may only read is the word, never "true" or "false" (RL-23). An unticked
# checkbox stores nothing, so the empty value reads "No" as well.
YES_NO_OPTIONS = ({"value": "true", "label": "Yes"}, {"value": "false", "label": "No"},
                  {"value": "", "label": "No"})


def date_format(ix) -> str:
    return str((ix.conventions or {}).get("date_format") or DEFAULT_DATE_FORMAT)


# ---- the record an act carries (METHOD-2026-09-25-04, item 4) ----------------------------
# The one plugin the pinned gen_forms binds for `loadBinder: prefill`, and the catalog's short
# names for it (contracts/registry-mirror.yaml, catalog_aliases).
PREFILL_PLUGIN = "joget-form-prefill"


def _prefill_owner(component: str) -> str:
    """The registry plugin a catalog component name resolves to (the mirror's aliases)."""
    try:
        aliases = (l1.load_mirror() or {}).get("catalog_aliases") or {}
    except Exception:                                  # noqa: BLE001 — no mirror: the name itself
        aliases = {}
    return str(aliases.get(component, component))


def _carry_record(form: dict, entity: dict, sections: list, ix, path: str):
    """METHOD-2026-09-25-04, item 4: the record an act carries to the form it opens.

    A form whose `prefill` reads its key from the address (keySources requestParam) was opened
    from a record — the record of the prefill's lookup form. Every field of this form that
    refers to that record and that the prefill fills is the CARRIED REFERENCE: it is shown as a
    read-only field bound to the record (never a hidden field that takes whatever the address
    gives), and on save the form's root guard refuses it empty and refuses it when it names no
    row of the record's table — which closes the first slice's finding that a crafted link can
    name a case that does not exist. Returns (rules, exists) lines for the root guard, and the
    ids of the carried fields (METHOD-2026-09-26-02, point 1: the prefill must find its key again
    when the form is saved — see project_form)."""
    pf = form.get("prefill") or {}
    if not any(str(k.get("source", "")).lower() == "requestparam" and k.get("name")
               for k in pf.get("keySources") or []):
        return [], [], []
    forms = {f["id"]: f for f in ix.doc.get("forms", [])}
    src_form = forms.get(pf.get("formId"))
    src = ix.entities.get((src_form or {}).get("entity")) if src_form else None
    if src is None and pf.get("table"):
        src = next((e for e in ix.entities.values() if e.get("table") == pf["table"]), None)
    if src is None:
        return [], [], []
    attrs = {a["id"]: a for a in entity.get("attributes", [])}
    filled = {str(m.get("to")) for m in pf.get("mappings") or []}
    ename = (src.get("name") or src["id"]).lower()
    key = acts.key_attr(src)
    sform = (src_form or {}).get("id") or next(
        (f["id"] for f in ix.forms_by_entity.get(src["id"], [])), "")
    rules, exists, carried = [], [], []
    for sec in sections:
        for i, f in enumerate(sec["fields"]):
            a = attrs.get(f.get("id"))
            if not a or a.get("type") != "ref" or (a.get("ref") or {}).get("entity") != src["id"] \
                    or f["id"] not in filled:
                continue
            label = f.get("label") or a.get("name") or humanize_label(f["id"])
            sec["fields"][i] = {"id": f["id"], "type": "textfield", "label": label,
                                "readonly": True}
            carried.append(f["id"])
            rules.append(f"{f['id']}||{f['id']}|This form opens from its {ename}: open the "
                         f"{ename} and choose the act there.")
            if key and sform:
                exists.append("|".join(["", "", sform, src["table"], key, f["id"], "",
                                        f"The {ename} this form was opened with does not "
                                        f"exist."]))
    for line in rules + exists:
        if "\n" in line:
            raise ProjectionError(f"{path}: a carried reference's rule holds a newline")
    return rules, exists, carried


# ---- lists that fit their record, and a choice that fills (METHOD-2026-09-25-04, item 6) ----
OPTIONS_QUERY_KEY = "x-options-query"   # a projector-internal marker, removed before emission
JDBC_OPTIONS_BINDER = "org.joget.plugin.enterprise.JdbcOptionsBinder"
_QUERY_PARAM = re.compile(r"\$P\{([A-Za-z_]\w*)\}")


def carried_param(form: dict) -> str | None:
    """The address parameter a form's record arrives in: the name of its prefill's
    `requestParam` key source (item 4), or None when the form carries no record."""
    for ks in ((form.get("prefill") or {}).get("keySources") or []):
        if str(ks.get("source", "")).lower() == "requestparam" and ks.get("name"):
            return str(ks["name"])
    return None


def _options_query(form: dict, sections: list, ix, path: str) -> None:
    """Bind every field that names an `options_query` to the enterprise JDBC options binder.

    The query is one of the model's `queries[]` with exactly one parameter — the identifier of the
    record the form was opened with (row 4 of the analysis's table 7.3). Its `$P{param}` is
    replaced by that record's key as the address carries it, escaped for SQL
    (`'#requestParam.<name>?sql#'`); the platform resolves the hash variable when it reads the
    form, and the binder reads the query's first column as the value, the second as the label
    and a third, when there is one, as the grouping."""
    fields = [f for s in sections for f in s["fields"] if OPTIONS_QUERY_KEY in f]
    if not fields:
        return
    param = carried_param(form)
    queries = {q["id"]: q for q in ix.doc.get("queries", [])}
    for f in fields:
        qid = f.pop(OPTIONS_QUERY_KEY)
        fpath = f"{path}/{f.get('id')}"
        if not param:
            raise ProjectionError(
                f"{fpath}: options_query '{qid}' reads the record the form is opened with, and "
                f"this form carries none — give it a `prefill` reading the record from the "
                f"address (keySources requestParam)")
        q = queries.get(qid)
        if q is None:
            raise ProjectionError(f"{fpath}: options_query names '{qid}', which is not one of "
                                  f"the model's queries (lint L011)")
        params = [p["id"] for p in q.get("params") or []]
        if len(params) != 1:
            raise ProjectionError(
                f"{fpath}: options_query '{qid}' must take exactly one parameter, the carried "
                f"record's identifier; it declares {len(params)}")
        sql = " ".join(str(q["sql"]).split())
        if "?" in sql or "#" in sql:
            raise ProjectionError(
                f"{fpath}: the SQL of query '{qid}' holds '?' or '#', which the options binder "
                f"and the platform's hash variables would read as their own")
        named = set(_QUERY_PARAM.findall(sql))
        if named != {params[0]}:
            raise ProjectionError(
                f"{fpath}: the SQL of query '{qid}' must use its parameter as "
                f"$P{{{params[0]}}}; it names {sorted(named) or 'none'}")
        sql = _QUERY_PARAM.sub(f"'#requestParam.{param}?sql#'", sql)
        _with_props(f, optionsBinder={
            "className": JDBC_OPTIONS_BINDER,
            "properties": {"jdbcDatasource": "default", "useAjax": "", "addEmpty": "true",
                           "emptyLabel": "", "sql": sql}})


def _populate_pairs(value) -> list:
    """A smart search's `populate` as [(source column, field)]: the plugin's own "a:b,c:d"
    string, or a mapping."""
    if isinstance(value, dict):
        return [(str(k).strip(), str(v).strip()) for k, v in value.items()]
    out = []
    for pair in [p for p in str(value or "").split(",") if p.strip()]:
        src, _, dst = pair.partition(":")
        out.append((src.strip(), dst.strip()))
    return out


def _lock_populated(sections: list, path: str) -> list:
    """METHOD-2026-09-25-04, item 6 (row 7, the kit's part): a smart search's choice FILLS the
    form's fields its `populate` maps, and LOCKS them.

    Each mapped field must be a field of this form, or the choice fills nothing. The lock is not
    the platform's read-only: a read-only element stores the value it was loaded with, never the
    one the page wrote into it (delta D-069, "a readonly key populated only in the DOM (e.g.
    SmartSearch populate) can store blank"), so a mapped field is emitted editable to the platform
    and locked in the page by the search itself: every search the kit places names its record
    (record_search; the kit refuses a search placed by its control), and the element locks the
    fields its property `locks` names (joget-smart-search 8.2.0) — read-only to the keyboard, out of
    the tab order, closed to the pointer. The person cannot type into them or pick another value,
    and what the choice wrote is what is saved. The kit placed a script of its own for the lock,
    `kit_locked_fields`, until METHOD-2026-09-28-07 (the search round's section 7, item 2): it did
    what the element's property does, and it is gone. Returns the fields the choice fills, in
    order."""
    fields = {f.get("id"): f for s in sections for f in s["fields"]}
    filled: list = []
    for s in sections:
        for f in s["fields"]:
            if f.get("type") != "smart_search":
                continue
            cfg = f.get("config") if isinstance(f.get("config"), dict) else {}
            pairs = _populate_pairs(cfg.get("populate", f.get("populate")))
            for src, dst in pairs:
                if not src or not dst:
                    raise ProjectionError(f"{path}/{f.get('id')}: populate entry '{src}:{dst}' "
                                          f"is not <source column>:<field>")
                tgt = fields.get(dst)
                if tgt is None or dst == f.get("id"):
                    raise ProjectionError(
                        f"{path}/{f.get('id')}: the search's choice fills '{dst}', which is not "
                        f"another field of this form — the choice would fill nothing")
                tgt["readonly"] = False
                if isinstance(tgt.get("props"), dict):
                    tgt["props"].pop("readonlyLabel", None)
                if dst not in filled:
                    filled.append(dst)
            if pairs:
                text = ",".join(f"{a}:{b}" for a, b in pairs)
                f.setdefault("config", {})["populate"] = text
                if "populate" in f:
                    f["populate"] = text
    return filled


# ---- the state as a badge (METHOD-2026-09-25-04, item 2) -------------------------------
BADGE_KEY = "x-state-badge"          # a projector-internal marker, removed before emission
BADGE_FIELD = "state_badge_style"
TONE_HEX = {"grey": "#546e7a", "blue": "#1565c0", "green": "#2e7d32",
            "amber": "#ef6c00", "red": "#c62828"}   # the list badge's colours (gen_datalists)


def state_tones(lc: dict) -> dict:
    """code -> tone for every state: the state's own `tone`, else grey for the initial state,
    green for a terminal one and amber in between — the rule the list's badge follows."""
    return {s["id"]: s.get("tone") or ("grey" if s.get("initial") else
                                       "green" if s.get("terminal") else "amber")
            for s in lc.get("states", [])}


def badge_style(badges: list) -> str:
    """The style that draws each status field as a badge in its state's colour. `badges` is
    [(field id, {code: tone})]. The platform's labelled value renders the state's name inside
    `.readonly_label span`, and the code in a hidden field beside it; the colour is keyed on that
    hidden field (`:has`), matching the field by its name or a sub-form's `<prefix>_<name>`."""
    rules = ["/* STA-03 (UX-01): the state is shown as a badge carrying its tone, never chosen —"
             " generated by the kit (METHOD-2026-09-25-04, item 2) */"]
    for fid, tones in badges:
        cell = (f'.form-cell:has(> input[type=hidden][name="{fid}"]),'
                f' .form-cell:has(> input[type=hidden][name$="_{fid}"])')
        rules.append(f"{cell.replace(', ', ' .readonly_label span, ')} .readonly_label span "
                     f"{{ display:inline-block; padding:2px 10px; border-radius:11px; color:#fff;"
                     f" font-size:12px; line-height:18px; font-weight:600; white-space:nowrap;"
                     f" background:{TONE_HEX['grey']}; }}")
        for code, tone in tones.items():
            sel = (f'.form-cell:has(> input[type=hidden][name="{fid}"][value="{code}"]) '
                   f'.readonly_label span, .form-cell:has(> input[type=hidden][name$="_{fid}"]'
                   f'[value="{code}"]) .readonly_label span')
            rules.append(f"{sel} {{ background:{TONE_HEX.get(tone, TONE_HEX['grey'])}; }}")
    return "<style>\n" + "\n".join(rules) + "\n</style>"


def place_badge_style(spec: dict) -> bool:
    """Take the badge markers off the status fields of a form spec and place the one style that
    draws them, at the END of the first section that holds one — the end, so that the element,
    which shows nothing, moves no field into another column (gen_forms deals a section's fields
    to its columns in turn). Returns whether it placed it."""
    badges, first = {}, None
    for sec in spec.get("sections") or []:
        for f in sec.get("fields") or []:
            tones = f.pop(BADGE_KEY, None)
            if tones is not None:
                badges.setdefault(f["id"], tones)
                first = first or sec
    if not badges or any(f.get("id") == BADGE_FIELD for s in spec["sections"] for f in s["fields"]):
        return False
    first["fields"].append({"id": BADGE_FIELD, "type": "html",
                            "html": badge_style(sorted(badges.items()))})
    return True


def _with_props(out: dict, **props) -> dict:
    """Merge generator properties into the field's `props` channel (gen_forms 0.9.12: residual
    element properties merged LAST). A key the model already set in its own `config.props` wins."""
    merged = dict(props)
    merged.update(out.get("props") or {})
    out["props"] = merged
    return out


def _default_text(value) -> str:
    """An attribute's default as an element's value: a yes-or-no as the platform's "true" or
    "false" (the value a CheckBox option carries), anything else as its text (ADR-108)."""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def _smart_search_field(fld: dict, a: dict, fid: str, cfg: dict, sec_managed: bool,
                        path: str) -> dict:
    """`control: smart_search` (ADR-108; a delivery's hand-off of 5 October 2026, item 2): the
    class-name pass-through the totality register named for it (docs/PROJECTION-DECISIONS.md,
    D-10). The element is the pinned generator's search element (gen_forms type `smart_search`,
    joget-smart-search's `global.govstack.smartsearch.element.SmartSearchElement`); its settings
    are the ones the model names in the field's `config`, passed through and none invented:
    those the generator reads from a field's `config` (SEARCH_CONFIG_KEYS) stay there, and every
    other one — the record it searches (`recordTable`) and the columns it reads, the words when
    nothing is found — is written through `props`, which the generator merges into the element's
    properties last. `config.props` is merged after them and wins.

    Refused, as the house rule asks (a weaker element is never emitted): a search that names
    neither the record it searches (`recordTable`) nor a service to ask (`apiEndpoint`), which
    would search nothing; one that names no column to store the choice in (`storeValue`, or
    `idField`), which the kit's lint of the build refuses (A002); and a search the person may only
    read — the element has no read-only state. A reference to a data dictionary registry placed
    as a search with no `control` keeps the derived record search (record_search), which this does
    not touch."""
    own = {k: v for k, v in cfg.items() if k not in ("props", "column")}
    named = dict(own, **(cfg.get("props") or {}))
    if not (named.get("recordTable") or named.get("apiEndpoint")):
        raise ProjectionError(
            f"{path}: control 'smart_search' names neither the record it searches "
            f"(config.recordTable) nor the service it asks (config.apiEndpoint); the search "
            f"element would search nothing")
    if not (named.get("storeValue") or named.get("idField")):
        raise ProjectionError(
            f"{path}: control 'smart_search' names no column whose value the field stores when a "
            f"result is chosen (config.storeValue); the choice would be stored nowhere (A002)")
    if bool(fld.get("readonly")) or (sec_managed and "readonly" not in fld) or fld.get("held_by"):
        raise ProjectionError(
            f"{path}: readonly is not realizable on generator element 'smart_search'")
    out = {"id": fid, "type": "smart_search",
           "label": fld["label"] if "label" in fld else (a.get("name") or humanize_label(fid)),
           "config": {k: v for k, v in own.items() if k in SEARCH_CONFIG_KEYS}}
    if own.get("idField"):
        out["idField"] = own["idField"]
    if fld["required"] if "required" in fld else bool(a.get("required")):
        out["required"] = True
    rest = {k: v for k, v in own.items() if k not in SEARCH_CONFIG_KEYS and k != "idField"}
    rest.update(cfg.get("props") or {})
    if rest:
        out["props"] = rest
    if "column" in cfg:
        out["column"] = cfg["column"]     # explicit layout tag (0.9.12)
    return out


# --------------------------------------------------------------------------- #
# Model indexes                                                                #
# --------------------------------------------------------------------------- #

class Index:
    def __init__(self, doc: dict, app_path=None):
        self.doc = doc
        self.app_path = app_path
        # KP-01: the domain data dictionary drives the derivation contract
        self.dd = l1.load_dd(doc, app_path)
        self.dd_sets = {st['id']: st for st in self.dd.get('sets', [])}
        self.entities = {e["id"]: e for e in doc.get("entities", [])}
        self.vocabs = {v["id"]: v for v in doc.get("vocabularies", [])}
        self.forms_by_entity: dict[str, list[dict]] = {}
        for f in doc.get("forms", []):
            self.forms_by_entity.setdefault(f["entity"], []).append(f)
        self.conventions = (doc.get("app", {}).get("conventions") or {})

        # Datalists per source entity — the popup search-select (IDR-05) derives its
        # popup list from here when a ref targets an operational (unbounded) entity.
        self.lists_by_entity: dict[str, list[dict]] = {}
        for lst in doc.get("lists", []):
            ent_id = (lst.get("source") or {}).get("entity")
            if ent_id:
                self.lists_by_entity.setdefault(ent_id, []).append(lst)

        # Attributes a datalist column displays, grouped by the form whose row binder
        # reads them (ADR-029). A datalist bound via AdvancedFormRowDataListBinder can
        # only load a column whose attribute is a field on the bound form; a lifecycle-
        # or audit-managed attribute (status, submitted_at, …) is otherwise absent, so
        # the column renders blank though the value is stored. project_form uses this to
        # mirror each missing attribute as a read-only display field. Only UNAMBIGUOUS
        # bindings count — an explicit source.form, or an entity with exactly one form —
        # mirroring project_datalists' binder resolution; an ambiguous entity is left
        # untouched exactly as the datalist projector would refuse it.
        self.list_attrs_by_form: dict[str, list[str]] = {}
        for lst in doc.get("lists", []):
            src = lst.get("source") or {}
            ent_id = src.get("entity")
            if not ent_id:
                continue                                   # query-sourced (jdbc) lists carry their own SELECT
            cands = [f["id"] for f in self.forms_by_entity.get(ent_id, [])]
            form_id = src.get("form")
            if not form_id:
                if len(cands) != 1:
                    continue                               # ambiguous — cannot attribute columns to one form
                form_id = cands[0]
            elif form_id not in cands:
                continue
            bucket = self.list_attrs_by_form.setdefault(form_id, [])
            for c in lst.get("columns", []):
                a = c.get("attr")
                if a and a not in bucket:
                    bucket.append(a)


# --------------------------------------------------------------------------- #
# Field projection                                                             #
# --------------------------------------------------------------------------- #

def _lookup_for_ref(attr: dict, ix: Index, cfg: dict, path: str) -> dict:
    """FormOptionsBinder lookup over the form bound to the referenced entity."""
    if "lookup" in cfg:                       # explicit passthrough wins
        return dict(cfg["lookup"])
    target_id = attr["ref"]["entity"]
    target = ix.entities[target_id]
    candidates = ix.forms_by_entity.get(target_id, [])
    if len(candidates) != 1:
        raise ProjectionError(
            f"{path}: ref to entity '{target_id}' needs exactly one form bound to it "
            f"to derive the lookup formDefId (found {len(candidates)}); "
            f"set an explicit config.lookup on the field")
    lookup = {"formDefId": candidates[0]["id"]}
    pk_attr = (target.get("pk") or {}).get("attr")
    if pk_attr:
        lookup["idColumn"] = pk_attr          # business key column stores the value
    display = attr["ref"].get("display")
    if display:
        lookup["labelColumn"] = display
    return lookup


def _search_list_for_ref(attr: dict, ix: Index, cfg: dict, path: str) -> str:
    """The datalist backing a popup search-select (IDR-05). Explicit config.search_list
    wins; otherwise the target entity must have exactly ONE datalist bound to it —
    with several (e.g. a scoped worklist plus a register), the model must say which
    one is the search surface."""
    if cfg.get("search_list"):
        return str(cfg["search_list"])
    target_id = attr["ref"]["entity"]
    lists = ix.lists_by_entity.get(target_id, [])
    if len(lists) != 1:
        raise ProjectionError(
            f"{path}: ref to operational entity '{target_id}' needs a search-select "
            f"popup list, but {len(lists)} datalists bind that entity — set "
            f"config.search_list on the field to name the search surface")
    return lists[0]["id"]


def record_search(attr: dict, target: dict, ix: Index, cfg: dict, list_id: str, path: str) -> dict:
    """METHOD-2026-09-28-01 (an engagement's point 8; the kit's gap G4, removed):
    the settings of the library's smart search element (joget-smart-search 8.2.0, `recordTable`
    and the properties beside it) for a reference the model places as a search, each read from
    the model and none written into the element:

      the record searched       the table of the entity the reference names (app_fd_<table>);
      searched exactly          its key, `pk.attr` (else the data dictionary set's `key`), which
                                is also what the field stores;
      searched by a fragment    the attribute the reference shows, `ref.display`;
      the result's columns      the columns of the list the model names as the search's result
                                (`config.search_list`), with their labels;
      what a choice fills       `config.populate`, <attribute of the record>:<field of the form>;
      what is locked            every field `config.populate` names (the element locks what the
                                choice fills; _lock_populated keeps those fields editable to the
                                platform, which saves what the page wrote);
      the words when nothing    `config.not_found`, `{searched}` standing for what was typed
      is found                  (application-model.schema.yaml names it).

    Every setting that names a column names one the record holds, or the projection refuses: the
    element reads the columns it is given, and a column the record lacks would fail every search
    (a fill from a value the record does not hold is refused too, rather than left unfilled —
    house rule 2 of docs/DEVELOPER-GUIDE.md)."""
    tid = target["id"]
    attrs = {x["id"]: x for x in target.get("attributes", [])}
    key = (target.get("pk") or {}).get("attr") or (ix.dd_sets.get(tid) or {}).get("key")
    if not key or key not in attrs:
        raise ProjectionError(
            f"{path}: the search looks in {tid}, and the model names no key of it to search "
            f"exactly (the entity's pk.attr, or its data dictionary set's key)")
    display = (attr.get("ref") or {}).get("display")
    if display and display not in attrs:
        raise ProjectionError(f"{path}: the reference shows '{display}', which is no attribute of {tid}")
    lst = next((x for x in ix.doc.get("lists", []) if x.get("id") == list_id), None)
    if lst is not None and (lst.get("source") or {}).get("query"):
        return _view_search(attr, tid, key, display, lst, ix, cfg, path)
    if lst is None or (lst.get("source") or {}).get("entity") != tid:
        raise ProjectionError(
            f"{path}: the search's result, the list '{list_id}', "
            + ("is not a list of the model" if lst is None else f"shows another record than {tid}, "
               f"which the reference names") + "; config.search_list names the list the result is")
    columns = []
    for c in lst.get("columns", []):
        ca = c.get("attr")
        if ca not in attrs:
            raise ProjectionError(f"{path}: the search's result, the list '{list_id}', shows "
                                  f"'{ca or c.get('expr')}', which is no attribute of {tid}")
        columns.append({"column": "c_" + ca,
                        "label": c.get("label") or attrs[ca].get("name") or humanize_label(ca)})
    carried, locks = [], []
    for src, dst in _populate_pairs(cfg.get("populate")):
        if src not in attrs:
            raise ProjectionError(
                f"{path}: the search's choice fills {dst or '(no field)'} from '{src}', which is no "
                f"attribute of {tid}, the record the search looks in; the element would fail every "
                f"search on a column the record lacks. Fill {dst or 'the field'} from an attribute of "
                f"{tid}, or take the pair out of config.populate")
        carried.append(f"c_{src}:{dst}")
        if dst and dst not in locks:
            locks.append(dst)
    settings = {"recordTable": "app_fd_" + target["table"], "exactColumn": "c_" + key}
    if display and display != key:
        settings["fragmentColumn"] = "c_" + display
    settings.update({"storeValue": "c_" + key, "resultColumns": columns,
                     "populate": ",".join(carried), "locks": ",".join(locks),
                     "entityLabel": str(cfg.get("entityLabel") or target.get("name") or tid).lower()})
    if cfg.get("not_found"):
        settings["notFound"] = str(cfg["not_found"])
    return settings


def _view_search(attr: dict, tid: str, key: str, display, lst: dict, ix: Index, cfg: dict,
                 path: str) -> dict:
    """METHOD-2026-09-28-07 (the kit's gap G5; the search round's section 7, item 1): the search
    looks in a view, not in the table of the record the reference names. Its result is a list
    sourced from one of the model's queries, and that query is a view of the database
    (`queries[].view`, made by the kit when it loads the starting data). The view's rows are the
    records searched; the field still stores the key of the record it refers to, which the view
    carries under the key's own name, beside what the record does not hold — another record's
    value (its open case) or the copy of a value another system holds. The element reads the
    view's columns by the names the query gives them with AS; a column the query does not name
    is refused, since the element would fail every search on it."""
    qid = lst["source"]["query"]
    q = next((x for x in ix.doc.get("queries", []) if x.get("id") == qid), None)
    if q is None:
        raise ProjectionError(f"{path}: the search's result, the list '{lst['id']}', reads the "
                              f"query '{qid}', which is not a query of the model")
    if not q.get("view"):
        raise ProjectionError(
            f"{path}: the search's result, the list '{lst['id']}', reads the query '{qid}', which "
            f"is no view of the database; the search reads a table or a view by its name. Give "
            f"the query a `view` name, or source the result from the record {tid}")
    if q.get("params"):
        raise ProjectionError(f"{path}: the query '{qid}' the search looks in takes parameters; "
                              f"a view takes none")
    cols = l1.query_columns(q)

    def need(name, what):
        if name not in cols:
            raise ProjectionError(
                f"{path}: the search looks in the view {q['view']} (the query '{qid}'), and {what} "
                f"'{name}', which the query does not name with AS; the element would fail every "
                f"search on a column the view lacks")

    need(key, f"the reference's key, which the field stores, is")
    columns = []
    for c in lst.get("columns", []):
        ce = c.get("expr")
        need(ce, "the result shows")
        columns.append({"column": ce, "label": c.get("label") or humanize_label(ce)})
    carried, locks = [], []
    for src, dst in _populate_pairs(cfg.get("populate")):
        need(src, f"the choice fills {dst or '(no field)'} from")
        carried.append(f"{src}:{dst}")
        if dst and dst not in locks:
            locks.append(dst)
    settings = {"recordTable": q["view"], "exactColumn": key}
    if display and display != key:
        need(display, "the reference shows")
        settings["fragmentColumn"] = display
    target = ix.entities.get(tid) or {}
    settings.update({"storeValue": key, "resultColumns": columns,
                     "populate": ",".join(carried), "locks": ",".join(locks),
                     "entityLabel": str(cfg.get("entityLabel") or target.get("name") or tid).lower()})
    if cfg.get("not_found"):
        settings["notFound"] = str(cfg["not_found"])
    return settings


def _static_options(attr: dict, ix: Index, path: str) -> list[dict]:
    """The inline options of a FIXED vocabulary (one the application does not maintain; a
    maintained one binds its list instead — lov.lookup_for). The label only, on the owner's word
    of 25 September 2026, which replaces UX-01 TRM-02's "code — label" rendering; the code is
    stored. A cascading vocabulary's options carry the parent code as their grouping."""
    vocab = ix.vocabs[attr["vocabulary"]]
    try:
        rows = lov.rows_of(vocab, ix.app_path)
    except lov.LovError as exc:
        raise ProjectionError(f"{path}: {exc}")
    if not rows:
        raise ProjectionError(
            f"{path}: vocabulary '{vocab['id']}' has no rows and no file; it would deploy as an "
            f"empty drop-down (lint L017)")
    out = []
    for r in rows:
        # a list whose business code is itself the label shows its code (item 1, `display_code`)
        o = {"value": r["code"],
             "label": r["code"] if vocab.get("display_code") else (r.get("name") or r["code"])}
        if vocab.get("parent"):
            o["grouping"] = r.get("parent_code", "")
        out.append(o)
    return out


def project_field(fld: dict, entity: dict, ix: Index, sec_managed: bool, path: str) -> dict:
    attrs = {a["id"]: a for a in entity.get("attributes", [])}
    bound = "attr" in fld
    a = attrs.get(fld["attr"], {}) if bound else {}
    fid = fld["attr"] if bound else fld["id"]
    path = f"{path}/{fid}"
    cfg = fld.get("config") or {}
    control = fld.get("control")

    # ---- verbatim passthrough (owner objective 2026-08-08): a deployed element
    # whose config the export carries whole - re-emitted untouched. Guarded:
    # `custom` without an element body still refuses (nothing to carry).
    if control == "custom":
        el = cfg.get("element") or {}
        if not el.get("className"):
            raise ProjectionError(
                f"{path}: control 'custom' needs config.element {{className, "
                f"properties}} - the verbatim passthrough carries a deployed "
                f"element, it does not invent one")
        out = {"id": fid, "type": "verbatim",
               "element": {"className": el["className"],
                           "properties": el.get("properties") or {}}}
        if "column" in cfg:
            out["column"] = cfg["column"]     # explicit layout tag (0.9.12)
        return out

    # ---- totality: refuse constructs the generator cannot express ----------
    if control in UNREALIZED_CONTROLS:
        raise ProjectionError(
            f"{path}: control '{control}' has no realization in the form generator "
            f"(totality register, docs/PROJECTION-DECISIONS.md)")
    if fld.get("validator"):
        raise ProjectionError(
            f"{path}: custom validator objects are not expressible in the generator's "
            f"DefaultValidator contract (totality register)")
    if control == "smart_search":
        return _smart_search_field(fld, a, fid, cfg, sec_managed, path)

    # ---- L2 field type ------------------------------------------------------
    if control:
        ftype = CONTROL_MAP.get(control)
        if ftype is None:
            raise ProjectionError(f"{path}: unknown control '{control}'")
        numeric = control == "number" or (
            ftype == "textfield" and a.get("type") in ("integer", "decimal"))
    else:
        atype = a.get("type")
        if atype == "computed":
            raise ProjectionError(
                f"{path}: computed attributes (calculation/concat realization) have no "
                f"element in the form generator (totality register)")
        if atype not in ATTR_TYPE_MAP:
            raise ProjectionError(f"{path}: no default control mapping for attribute type '{atype}'")
        ftype, numeric = ATTR_TYPE_MAP[atype]

    # ---- KP-01 derivation contract: a bound attribute's dd `semantic` DRIVES the
    # control, overriding any naive field control (this is what makes period-as-text
    # unauthorable — the model author cannot pick the wrong control for a period).
    sem = a.get("semantic")
    dd_kind, dd_control = l1.dd_control_for(ix.dd, sem) if sem else (None, None)
    if dd_control == "period_picker":
        st = ix.dd_sets.get(sem[3:], {})
        out = {"id": fid, "type": "period_picker",
               "label": fld.get("label") or a.get("name") or humanize_label(fid),
               "readonly": bool(fld.get("readonly") or sec_managed)}
        spec = st.get("spec", {})
        out["periodicities"] = spec.get("periodicities", ["monthly", "quarterly", "annual"])
        if spec.get("window"):
            out["window"] = spec["window"]
        if st.get("depends_on"):
            out["dependsOn"] = st["depends_on"]     # periodicity resolves from this field
        for k, v in cfg.items():
            out[k] = v
        return out

    # ---- a yes-or-no (METHOD-2026-09-25-04, item 1; RL-23): an editable one is a checkbox; one
    # the person may only read is the word "Yes" or "No", a labelled value — never "true" or
    # "false" in a text control (the platform's checkbox cannot be read-only, which is why models
    # placed it as `control: text`).
    if bound and a.get("type") == "boolean" and control in (None, "checkbox", "text"):
        ro_bool = bool(fld["readonly"]) if "readonly" in fld else sec_managed
        if ro_bool:
            yn = {"id": fid, "type": "select", "readonly": True,
                  "label": fld["label"] if "label" in fld
                  else (a.get("name") or humanize_label(fid)),
                  "static_options": [dict(o) for o in YES_NO_OPTIONS]}
            return _with_props(yn, readonlyLabel="true")
        ftype, numeric = "checkbox", False

    # ---- STA-03 (UX-01/UX-02): the lifecycle status renders FROM the state model —
    # the human label, never the raw code ("in_progress" -> "In progress"). Native
    # realization = a read-only SelectBox over the declared states (Joget renders the
    # matched option's LABEL for a readonly select). Status is never user-editable
    # (STA-03), so a bound status field is always this read-only, label-rendering
    # control wherever it is placed — header, list-completion Status, or the cascade
    # controlField on the Actions tab. This is what stops a raw enum leaking to screen.
    _lc = entity.get("lifecycle") or {}
    if bound and fid == _lc.get("status_attr"):
        disp = {"id": fid, "type": "select", "readonly": True,
                "label": fld.get("label") or a.get("name") or humanize_label(fid),
                "static_options": [{"value": s["id"],
                                    "label": s.get("name") or humanize_label(s["id"])}
                                   for s in _lc.get("states", [])]}
        # default to the lifecycle INITIAL state so a row created through this form
        # (e.g. the API {id}-only create the acceptance runner and engines use) is never
        # statusless — the mm guard matches exact from->to and '' has no legal move.
        # An existing record's stored status overrides this default on load.
        _v = (fld.get("config") or {}).get("value") or next(
            (s["id"] for s in _lc.get("states", []) if s.get("initial")), None)
        if _v:
            disp["value"] = _v
        if fld.get("controlField"):
            disp["controlField"] = fld["controlField"]
        # METHOD-2026-09-25-04, item 2 (STA-03; row 12 of the analysis's table 7.3): the state
        # is shown as a BADGE carrying its state's tone, never as a drop-down. The platform's
        # read-only rendering of a SelectBox shows the state's name as text (`readonlyLabel`,
        # selectBox.ftl) beside a hidden field holding the code; the badge's colour is keyed on
        # that hidden field by a style the form carries once (BADGE_KEY, placed by
        # project_form). No script: a style is enough, and the words carry the state, so the
        # colour never carries it alone (ACC-03).
        _with_props(disp, readonlyLabel="true")
        disp[BADGE_KEY] = state_tones(_lc)
        return disp

    # label VERBATIM when the model carries the key - '' included (a deployed
    # element saved label-less shows NO label; owner objective 2026-08-08).
    # Absent key: authored behaviour kept (attribute name, then humanized id).
    label = fld["label"] if "label" in fld \
        else (a.get("name") or humanize_label(fid))
    out: dict = {"id": fid, "type": ftype}

    if ftype == "html":
        out["html"] = cfg.get("html", "")
        for k, v in cfg.items():
            if k != "html":
                out[k] = v
        return out

    out["label"] = label

    # ---- options / bindings -------------------------------------------------
    if fld.get("options_query"):
        # METHOD-2026-09-25-04, item 6 (row 4, L3): a list that depends on the record the form
        # was opened with is the model's query over that record, read by the enterprise JDBC
        # options binder when the form opens. The binder is bound by project_form, which knows
        # the parameter the form's record arrives in (_options_query).
        if ftype not in ("select", "radio"):
            raise ProjectionError(
                f"{path}: options_query gives the options of a drop-down or of radio buttons; "
                f"control '{control or ftype}' takes no options")
        out["static_options"] = []
        out[OPTIONS_QUERY_KEY] = str(fld["options_query"])
    elif ftype in ("select", "radio"):
        if bound and a.get("type") == "enum":
            # a maintained vocabulary binds its own list (lov.py); a fixed one stays inline
            lk = lov.lookup_for(ix.doc, a["vocabulary"])
            if lk:
                out["lookup"] = lk
                # a divided list (item 7): chosen in two steps, its options read with their
                # categories from the two tables at run time (lov.divided_binder)
                jb = lov.divided_binder(ix.doc, a["vocabulary"])
                if jb:
                    _with_props(out, optionsBinder=jb)
            else:
                out["static_options"] = _static_options(a, ix, path)
        elif bound and a.get("type") == "ref":
            # IDR-05/AP-04 (UX-01 §3): decide the selection mechanism by the REFERENCED
            # SET, never by habit. An operational entity (unbounded — it grows with
            # operations; proxy: it has a lifecycle, overridable via entity `scale:`)
            # gets a datalist-popup search-select with server-side search and paging;
            # a dropdown over such a set is the amnesiac anti-pattern at national scale.
            # Bounded sets (config/md_* entities, no lifecycle) keep the dropdown.
            # Read-only refs stay display lookups on either branch.
            target = ix.entities[a["ref"]["entity"]]
            scale = target.get("scale") or ("operational" if target.get("lifecycle") else "bounded")
            editable = not (fld.get("readonly") or a.get("readonly") or sec_managed)
            # KP-01: a ref to a dd md.registry set is a PARTIAL-KNOWLEDGE smart search
            # (owner-corrected 14.07) — search with whatever facts are known, ranked
            # candidates, explicit pick. Realized by joget-smart-search. Other
            # operational refs stay the popup search-select; bounded refs stay dropdown.
            reg = ix.dd_sets.get(a["ref"]["entity"])
            is_registry = bool(reg and reg.get("kind") == "md.registry")
            if scale == "operational" and editable and is_registry:
                out["type"] = "smart_search"
                out["listId"] = _search_list_for_ref(a, ix, cfg, path)
                out["displayField"] = a["ref"].get("display") or \
                    (target.get("pk") or {}).get("attr") or "id"
                out["idField"] = (target.get("pk") or {}).get("attr", "")
                if cfg:
                    # gen_forms' smart_search element reads its knobs (apiEndpoint, apiId,
                    # apiKey, displayColumns, storeValue, nationalIdPattern) from a nested
                    # `config` dict — keep them there rather than flattening to top level.
                    out["config"] = dict(cfg)
                # METHOD-2026-09-28-01: the element searches the record the reference names,
                # every setting read from the model (record_search); written through `props`,
                # which gen_forms merges into the element's properties last.
                _with_props(out, **record_search(a, target, ix, cfg, out["listId"], path))
            elif scale == "operational" and editable:
                out["type"] = "popupselect"
                out["listId"] = _search_list_for_ref(a, ix, cfg, path)
                out["displayField"] = a["ref"].get("display") or \
                    (target.get("pk") or {}).get("attr") or "id"
                out["idField"] = (target.get("pk") or {}).get("attr", "")
            else:
                out["lookup"] = _lookup_for_ref(a, ix, cfg, path)
        elif "lookup" in cfg or "static_options" in cfg or "users" in cfg:
            # `users` (UX-02 §3, W-11): a CONFIGURED-REGISTRY selection over the
            # directory — options come from the platform's user store filtered by
            # group/org/dept (e.g. users: {group: dm_officer}); the username is
            # stored. Officers/staff are never typed free-text. Passthrough below.
            pass
        else:
            raise ProjectionError(
                f"{path}: select/radio needs an enum attribute, a ref attribute, or an "
                f"explicit config lookup/static_options/users")

    if ftype == "grid":
        child = fld["child"]                          # schema-required for grid
        child_entity = ix.entities[child["entity"]]
        parent = child_entity.get("parent") or {}
        union = child_entity.get("parent_union") or {}
        fk = parent.get("fk_attr") or union.get("fk_attr")
        if not fk:
            raise ProjectionError(
                f"{path}: grid child entity '{child['entity']}' declares no parent.fk_attr "
                f"(or parent_union.fk_attr) to derive the grid foreignKey")
        child_attrs = {ca["id"]: ca for ca in child_entity.get("attributes", [])}
        out["formDefId"] = child["form"]
        out["foreignKey"] = fk
        if union:
            # ADR-091: the grid's parent is ONE member of the union, so the discriminator
            # must be pinned — otherwise the grid shows rows belonging to other case types.
            member = next((m for m in union.get("members", [])
                           if m["entity"] == entity.get("id")), None)
            if member is None:
                raise ProjectionError(
                    f"{path}: grid child '{child['entity']}' declares a parent_union that does "
                    f"not include '{entity.get('id')}' — this form cannot own those rows (ADR-091)")
            out["x-union-discriminator"] = {"attr": union["discriminator"],
                                            "equals": member["when"]}
        cols = []
        for col in child.get("columns", []):
            cols.append({"value": col,
                         "label": (child_attrs.get(col, {}).get("name") or humanize_label(col))})
        if cols:
            out["columns"] = cols
        if fld.get("deletable"):
            out["deleteGridData"] = True     # FormGrid row-remove (gen_forms honors this)

    if ftype == "id_generator":
        pk = entity.get("pk") or {}
        if bound and pk.get("attr") == fid and pk.get("format"):
            out["format"] = pk["format"]

    # ---- value / numeric / required -----------------------------------------
    # an attribute's default is the element's value (ADR-108): written as the spec's `value` where
    # the generator reads it; the elements it does not read it on take it through `props`, after
    # the `config` pass-through below, so that a value the model names there wins
    if a.get("default") is not None and ftype in DEFAULT_BY_VALUE:
        out["value"] = str(a["default"]) if ftype == "date" else a["default"]
    if numeric and ftype == "textfield":
        out["storeNumeric"] = True
    required = fld["required"] if "required" in fld else bool(a.get("required"))
    if required:
        if ftype not in REQUIRED_CAPABLE:
            raise ProjectionError(
                f"{path}: required is not realizable on generator element '{ftype}'")
        out["required"] = True

    # ---- readonly ------------------------------------------------------------
    # desired = the model's intent; inferred = what the generator would decide on
    # its own (section lock or managed-label phrase). Emit an explicit key whenever
    # intent and inference could diverge, so model truth always wins.
    desired = bool(fld.get("readonly", False)) or (sec_managed and "readonly" not in fld)
    # METHOD-2026-09-28-07 (the kit's gap G5): a value another system holds is shown, and no
    # person changes it; where a search's choice fills it, _lock_populated makes it editable to
    # the platform again (delta D-069) and the search locks it (`locks`)
    desired = desired or bool(fld.get("held_by"))
    ro_file = False
    if ftype in READONLY_CAPABLE:
        if desired and not sec_managed:
            out["readonly"] = True
        elif not desired and (sec_managed or MANAGED_LABEL.search(label)):
            out["readonly"] = False
    elif desired and ftype == "fileupload":
        # ADR-108 (a delivery's hand-off of 5 October 2026, item 3): a file field the person may only
        # read shows its file and offers no means to replace it. The platform's FileUpload honours
        # `readonly` "true" (fileUpload.ftl: the file's link, no remove, no drop zone, no file
        # input); the pinned generator writes no such key, so it goes through `props` below.
        ro_file = True
    elif desired and ftype not in READONLY_VACUOUS:
        raise ProjectionError(
            f"{path}: readonly is not realizable on generator element '{ftype}'")

    # ---- element-specific passthrough (schema `config`, PASSTHROUGH channel) --
    for k, v in cfg.items():
        out[k] = v
    if ro_file:
        _with_props(out, readonly="true")
    if a.get("default") is not None and out.get("type") in DEFAULT_BY_PROPS:
        _with_props(out, value=_default_text(a["default"]))

    # ---- how the value is shown (METHOD-2026-09-25-04, item 1) ---------------
    # A coded value, a reference or a directory user the person may only read is shown as its
    # label — a labelled value, the platform's own read-only rendering of a SelectBox
    # (`readonlyLabel`, selectBox.ftl) — never as a disabled drop-down (RL-41).
    if desired and out.get("type") == "select":
        _with_props(out, readonlyLabel="true")
    # Every date control shows the date day first, in the one form the application names; a date
    # and time shows the time after it, in 24 hours (point 5).
    if out.get("type") == "date":
        _with_props(out, format=date_format(ix))
        if control == "datetime" or (not control and a.get("type") == "datetime"):
            _with_props(out, **DATETIME_PROPS)
    return out


# --------------------------------------------------------------------------- #
# Form projection                                                              #
# --------------------------------------------------------------------------- #

def _qualify_predicate(where: str, attr_ids: list[str]) -> str:
    """Prefix bare attribute identifiers in a uniqueness scope predicate with
    `e.customProperties.` so unique-guard (WP-H / ADR-072) can use it as HQL. Longest ids
    first so 'status' does not corrupt 'status_date'; already-qualified refs are left."""
    out = where or ""
    for aid in sorted(attr_ids, key=len, reverse=True):
        out = re.sub(rf"(?<![\w.]){re.escape(aid)}(?![\w])", f"e.customProperties.{aid}", out)
    return out


def _wizard_section(form: dict, wiz: dict, ix: Index, path: str) -> dict:
    """The trailing-section wizard realization for models that do not place a
    `wizard_slot` (authored models; harvested ones mark the deployed position)."""
    return {"columns": 1, "fields": [_wizard_field(form, wiz, ix, path)]}


def _wizard_field(form: dict, wiz: dict, ix: Index, path: str) -> dict:
    """The wizard realization (2026-08-08): purpose:wizard -> one section carrying a
    `multipaged` element gen_forms already realizes (it has, for detail_360, since
    ADR-068 — the wizard gap was this projector branch, not the generator).

    Every constant here is a measured fact of the two deployed reference-portal
    wizards, not a preference: page labels are authored (steps[].label, falling
    back to the step form's name); subFormParentId is the step entity's
    parent.fk_attr (the same key harvest lifts it from); parentSubFormId is
    steps[].parent_field; validate is TRUE on every page of both deployed wizards
    (the VAL-03 empty-validate rule is a detail_360 tabs rule — a wizard page
    validates on Next); ajaxMode is EMPTY on both; displayMode is tab."""
    forms_by_id = {f["id"]: f for f in ix.doc.get("forms", [])}
    pages = []
    for s in wiz.get("steps", []):
        st = {"form": s} if isinstance(s, str) else dict(s)
        sf = forms_by_id.get(st["form"])
        if sf is None:
            raise ProjectionError(
                f"{path}: wizard step '{st['form']}' is not a form in the model - "
                f"a page over a form the app does not carry cannot render")
        ent = ix.entities.get(sf.get("entity")) or {}
        fk = ((ent.get("parent") or {}).get("fk_attr")
              or (ent.get("parent_union") or {}).get("fk_attr") or "")
        page = {"formDefId": st["form"],
                "label": st.get("label") or sf.get("name")
                or humanize_label(st["form"])}
        if fk:
            page["subFormParentId"] = fk
        if st.get("parent_field"):
            page["parentSubFormId"] = st["parent_field"]
        page["validate"] = True
        pages.append(page)
    field = {"id": wiz.get("id") or f"{form['id']}Wizard", "type": "multipaged",
             "displayMode": "tab", "ajaxMode": False, "pages": pages,
             "partiallyStore": bool(wiz.get("partial_store", True))}
    if wiz.get("store_main_on_partial"):
        field["storeMainFormOnPartiallyStore"] = True
    # residual deployed root props (wizard.config, 2026-08-08): prevButtonlabel
    # 'Previous' on the deployed reference wizard - gen_forms merges them LAST.
    if wiz.get("config"):
        field["props"] = dict(wiz["config"])
    return field


def project_form(form: dict, ix: Index) -> dict:
    fid = form["id"]
    path = f"forms/{fid}"
    if form.get("purpose") == "wizard" and not form.get("wizard"):
        raise ProjectionError(
            f"{path}: purpose wizard with no wizard block - there are no pages to "
            f"realize (application-model.schema.yaml requires the block)")
    if form.get("post_actions"):
        raise ProjectionError(
            f"{path}: post_actions need the catalog component contract to resolve a "
            f"postProcessor class; not derivable in projector v{PROJECTOR_VERSION} "
            f"(totality register)")
    # form.validation / form.permissions / form.purpose are deliberately NOT
    # projected here: they are realized by other projectors (validator plugins,
    # userview permissions, CRUD wiring). Documented in MAPPING-forms.md.

    entity = ix.entities[form["entity"]]
    table_mode = ix.conventions.get("form_table", "entity")
    if table_mode == "form_id":
        table = fid                      # Joget-native default: tableName == formDefId
    elif table_mode == "entity":
        table = entity["table"]
    else:
        raise ProjectionError(f"{path}: unknown conventions.form_table '{table_mode}'")

    fm = {"id": fid, "name": form["name"], "table": table}
    desc = form.get("description") or form.get("x-description")  # D-01 promoted; x- bridge kept for back-compat
    if desc:
        fm["description"] = desc

    # form-level prefill (D-10, PASSTHROUGH): the model's config body is copied
    # verbatim to the generator's `loadBinder: prefill` block — the projector
    # synthesizes nothing. `component` is the kit's catalog binding (which plugin
    # realizes this), not a plugin property, so it is dropped from the emitted body.
    # Realization + config-shape validation belong to the form-prefill component
    # contract, not this projector.
    prefill = form.get("prefill")
    if prefill:
        # METHOD-2026-09-25-04, item 4 (RL-44): the component a prefill names is HONOURED, not
        # dropped. It is resolved through the catalog's aliases to the plugin that realizes it;
        # the pinned gen_forms binds exactly one load binder for `loadBinder: prefill` —
        # joget-form-prefill's FormPrefillLoadBinder — so any other component is refused here
        # rather than realized, silently, as that binder with the wrong configuration.
        comp = str(prefill.get("component") or "")
        owner = _prefill_owner(comp)
        if owner != PREFILL_PLUGIN:
            raise ProjectionError(
                f"{path}: prefill names component '{comp}', and the pinned form generator binds "
                f"only {PREFILL_PLUGIN}'s FormPrefillLoadBinder for a prefill — realizing '{comp}' "
                f"as that binder would put the wrong binder on the form with a configuration it "
                f"does not read (RL-44). Name `form-prefill` (joget-form-prefill), or budget the "
                f"component's binder as a bespoke plugin and a generator that emits it")
        fm["loadBinder"] = "prefill"
        fm["prefill"] = {k: v for k, v in prefill.items() if k != "component"}

    sections = []
    for sec in form.get("sections") or []:        # a wizard shell may carry none
        s: dict = {}
        if sec.get("id"):
            # authored section ids reach the generated JSON (2026-08-08): the
            # deployed reference-portal sections carry authored ids
            # (activitiesSection, ...) a round trip must reproduce.
            # split_detail_360 strips them - its CTX-02 chrome targets the
            # generator-minted #section1.
            s["id"] = sec["id"]
        if sec.get("label"):
            s["label"] = sec["label"]
        s["columns"] = sec.get("columns", 2)      # L1 default is 2; generator default is 1
        managed = bool(sec.get("readonly", False))
        if managed:
            s["managed"] = True
        flds = []
        for f in sec["fields"]:
            if f.get("control") == "wizard_slot":
                # positional wizard realization (owner objective 2026-08-08):
                # the deployed MultiPagedForm sits INSIDE a section between
                # other elements (reference shell: banner then wizard) - the slot
                # marks where, the wizard block says what.
                if not form.get("wizard"):
                    raise ProjectionError(
                        f"{path}/{sec['id']}: a wizard_slot with no wizard "
                        f"block - there is nothing to place in it")
                flds.append(_wizard_field(form, form["wizard"], ix, path))
            else:
                flds.append(project_field(f, entity, ix, managed,
                                          f"{path}/{sec['id']}"))
        s["fields"] = flds
        sections.append(s)

    # ---- METHOD-2026-09-25-04, item 4: the record the form was opened from, carried read-only
    carried_rules, carried_exists, carried_ids = _carry_record(form, entity, sections, ix, path)
    if carried_ids and fm.get("prefill"):
        # METHOD-2026-09-26-02, point 1: the carried field is read-only, and the platform saves a
        # read-only field with the value the load binder gives it on the submit (delta D-069).
        # The form menu posts to its own address with `?_action=submit` alone, so the address's
        # parameter the form was opened with is gone by then; the field's own name is not — the
        # page posts it. Where the model's prefill reads its key under another name, the field's
        # own name follows it as the next key source ("first non-empty wins"), so that the
        # record the form was opened with is the record it saves, on the field the model names.
        ks = list(fm["prefill"].get("keySources") or [])
        named = {str(k.get("name")) for k in ks if str(k.get("source", "")).lower() == "requestparam"}
        ks += [{"source": "requestParam", "name": c} for c in carried_ids if c not in named]
        fm["prefill"]["keySources"] = ks
    # ---- item 6: options read by the model's query over that record; a search that fills
    _options_query(form, sections, ix, path)
    if sections:
        _lock_populated(sections, path)

    # ---- a cascading FIXED vocabulary filters on its parent through the platform's own
    # controlField: its options carry the parent code as their grouping (_static_options) and the
    # field bound to the parent vocabulary on this form is the control. A maintained vocabulary
    # cascades through the script lov.py places at the head of the form instead.
    _vattrs = {a["id"]: a for a in entity.get("attributes", [])}
    _vfields = [f for s in sections for f in s["fields"]]
    _by_vocab: dict = {}
    for f in _vfields:
        va = _vattrs.get(f.get("id"))
        if va and va.get("type") == "enum" and f.get("type") == "select":
            _by_vocab.setdefault(va["vocabulary"], f["id"])
    for f in _vfields:
        va = _vattrs.get(f.get("id"))
        if not (va and va.get("type") == "enum" and "static_options" in f) \
                or (f.get("props") or {}).get("optionsBinder"):
            continue
        par = (ix.vocabs.get(va["vocabulary"]) or {}).get("parent")
        if par and par in _by_vocab and not f.get("controlField"):
            f["controlField"] = _by_vocab[par]

    # ---- wizard realization (2026-08-08): the shell's own fields first (parcel-
    # Registration carries two hidden columns beside its wizard), then the pages.
    # A placed wizard_slot already realized it inline at the deployed position.
    _slot_placed = any(f.get("control") == "wizard_slot"
                       for sec in form.get("sections") or [] for f in sec["fields"])
    if form.get("wizard") and not _slot_placed:
        sections.append(_wizard_section(form, form["wizard"], ix, path))

    # ---- grid-child foreign key (ADR-035): a form whose entity is a grid child must carry the
    # parent FK as a HiddenField, or the parent FormGrid's row binder throws on that path
    # (the app_fd_<child>.application_id 'null' failure). gen_forms links grids by this field.
    # NOT for wizard steps (2026-08-08): the wizard page's subFormParentId does the parent
    # wiring there - the deployed a child table ships WITHOUT its parent_id column,
    # and minting one invented a section the deployed form does not have.
    union = entity.get("parent_union") or {}
    fk = (entity.get("parent") or {}).get("fk_attr") or union.get("fk_attr")
    # ADR-091: a union child must ALSO carry the discriminator — the parent grid pins it
    # (x-union-discriminator), so without the column the pin has no path to bind.
    carry = [] if form.get("purpose") == "wizard_step" \
        else [a for a in (fk, union.get("discriminator")) if a]
    known = {a["id"] for a in entity.get("attributes", [])}
    placed_fk = {f.get("attr") or f.get("id")
                 for sec in form.get("sections") or [] for f in sec["fields"]}
    def _hidden(a):
        # a hidden carrier is written by the grid binder, not by a user, so requiredness is
        # neither realizable on the element nor meaningful here — the parent's grid supplies it.
        fld = dict(next(x for x in entity["attributes"] if x["id"] == a))
        fld.pop("required", None)
        stub = dict(entity, attributes=[fld] + [x for x in entity["attributes"] if x["id"] != a])
        return project_field({"attr": a, "control": "hidden"}, stub, ix, False, f"{path}/_fk")

    hidden = [_hidden(a) for a in carry if a in known and a not in placed_fk]
    if hidden:
        sections.append({"columns": 1, "fields": hidden})

    # ---- list-completion (ADR-029): make every datalist column loadable by this
    # form's row binder. Mirror each attribute a bound datalist displays but the form
    # does not place as a READ-ONLY display field, so its column resolves instead of
    # rendering blank. Refs/grids/computed/json/file are skipped (not scalar display
    # columns); the value stays engine-owned (readonly). Deterministic: model order.
    placed = {f.get("attr") or f.get("id")
              for sec in form.get("sections") or [] for f in sec["fields"]}
    scalar = {a["id"]: a for a in entity.get("attributes", [])}
    NON_SCALAR = {"ref", "computed", "json", "file"}
    missing = [a for a in ix.list_attrs_by_form.get(fid, [])
               if a not in placed and a in scalar and scalar[a].get("type") not in NON_SCALAR]
    if missing:
        # a record created through this form gets the lifecycle INITIAL state as the engine-owned
        # default of its status field, so a new row is never statusless (ADR-033).
        lc = entity.get("lifecycle") or {}
        status_attr = lc.get("status_attr")
        initial = next((s["id"] for s in lc.get("states", []) if s.get("initial")), None)
        status_fields = []
        for a in missing:
            spec = {"attr": a, "control": "text", "readonly": True, "label": humanize_label(a)}
            if a == status_attr and initial:
                spec["config"] = {"value": initial}   # PASSTHROUGH -> the field's default value
            status_fields.append(project_field(spec, entity, ix, False, f"{path}/_status"))
        sections.append({"label": "Status", "columns": 1, "fields": status_fields})

    # ---- transition actions (ADR-034): when the entity has a user-triggered lifecycle, add an
    # Action select (the transitions legal for this form's roles) + the TransitionGuard post-
    # submission processor that drives StatusManager on save. All generated from the model's
    # transitions + effects — so "records that flow" is a projection, not hand-wiring.
    # ---- unique-guard (WP-H / ADR-072 · placement ADR-076): an entity that declares
    # `uniqueness` carries a count-then-refuse form validator on its forms — emitted here
    # (entity-driven, like the TransitionGuard block), realized by gen_forms onto the FORM
    # ROOT validator slot (ADR-076: the root always runs — D-067 — and a readonly key cannot
    # skip it — D-068), verified in the build by A006, required by D-013. The bare `where`
    # scope predicate is qualified to HQL against this entity's attributes; the plugin derives
    # form id + table from the root, so no formDefId is emitted (Finding B's seam removed).
    uniqs = entity.get("uniqueness") or []
    _uguard = None
    if uniqs:
        _attr_ids = [a["id"] for a in entity.get("attributes", [])]
        for u in uniqs:
            _keys = u.get("attrs") or []
            if not _keys:
                continue
            if (u.get("enforcement") or "guard").lower() == "detection":
                continue   # detection-enforced uniqueness is WATCHED (integrity scenario + admin
                           # datalist), never form-guarded — the key is not form-writable (D-066/069)
            _scope = u.get("where", "")
            _msg = u.get("message") or (
                "A record with the same " + ", ".join(_keys) + " already exists"
                + (" (scope: " + _scope + ")" if _scope else "") + ".")
            _uguard = {
                "attrs": ",".join(_keys),
                "where": _qualify_predicate(_scope, _attr_ids),
                "message": _msg}
            break   # v1: one guard per form; a second constraint is a follow-on

    out = {"form": fm, "sections": sections}
    if _uguard:
        out["unique_guard"] = _uguard
    lcx = entity.get("lifecycle") or {}
    status_attr_x = lcx.get("status_attr")
    is_create = bool(status_attr_x) and form.get("purpose") == "create"
    if is_create:
        # ADR-034 refinement (a reference build's walkthrough): a create-purpose form advances no
        # lifecycle — no Action select, no TRANSITION guard (a record being created has no
        # move to make). It DOES stamp the lifecycle INITIAL state as the status field's
        # default, because the mm-config guard matches exact from->to rows: '' has no legal
        # moves, so a statusless record is permanently stuck (the latent manual-case bug).
        #
        # D-097: this branch used to `return out` here. "No lifecycle action" was correct;
        # returning was not — the return also skipped the require-guard block at the end of
        # this function, so NO create form in ANY application could ever carry a root guard.
        # A model could declare "creating this refused without a TIN", it would validate,
        # generate and deploy, and nothing at the keyboard would enforce it — the same
        # fail-open shape as the August registration guard. Skip the transition block only
        # (below), and fall through to the guard block, which is about the RECORD, not
        # about a move.
        placed_now = {f.get("attr") or f.get("id") for sec in sections for f in sec["fields"]}
        initial = next((st["id"] for st in lcx.get("states", []) if st.get("initial")), None)
        if initial and status_attr_x not in placed_now:
            fld = project_field({"attr": status_attr_x, "control": "text", "readonly": True,
                                 "label": humanize_label(status_attr_x),
                                 "config": {"value": initial}}, entity, ix, False,
                                f"{path}/_lcinit")
            sections.append({"label": "Status", "columns": 1, "fields": [fld]})
    # ---- the acts of the record (METHOD-2026-09-25-04, items 3 and 4). Until this round the
    # person's moves were one "Action" drop-down on every record form, offered whatever the
    # state (by cascade) and made on Save by a TransitionGuard on the form — a post-processor the
    # platform does not run when a record is edited through a CRUD menu (delta D-015), which is
    # how every record form is reached. Now each act is a BUTTON named after it: a move opens
    # that move's own trigger form (synthesize_trigger_forms), created as a new record, where the
    # post-processor does run; a form act opens the form it names with the record carried. The
    # buttons are drawn by a small runtime piece (tools/acts.py) that offers a move only in the
    # states it leaves from and disables it, with the move's guard in words, where the record's
    # facts say the guard does not hold (STA-01, STA-02). The record form keeps no post-processor.
    acts_here = acts.acts_of(form, entity)
    if acts_here:
        placed_now = {f.get("attr") or f.get("id") for sec in sections for f in sec["fields"]}
        extra = []
        if any(a["kind"] == "move" for a in acts_here) and status_attr_x \
                and status_attr_x not in placed_now:
            # the buttons read the record's state from the page: it is shown, as its badge
            extra.append(project_field({"attr": status_attr_x, "readonly": True}, entity, ix,
                                       False, f"{path}/_acts"))
        key = acts.key_attr(entity)
        if key and key not in placed_now:
            # the buttons carry the record's key: it rides on the page, hidden
            extra.append(project_field({"attr": key, "control": "hidden", "required": False},
                                       entity, ix, False, f"{path}/_acts"))
        if extra:
            sections.append({"label": "Status", "columns": 1, "fields": extra})
        sections.append({"label": acts.ACTS_SECTION, "columns": 1,
                         "fields": _act_bar(form, entity, acts_here, sections, ix, path)})

    # ---- form post_processor, verbatim (owner objective 2026-08-08): both
    # deployed reference-portal shells carry FormQualityPostProcessor runOn 'both'.
    # The form root has ONE postProcessor slot; when the entity's lifecycle
    # already claims it (TransitionGuard above), refuse loudly - realizing
    # either one silently under the other would enforce less than the model says.
    _pp = form.get("post_processor")
    if _pp:
        if out.get("postProcessor"):
            raise ProjectionError(
                f"{path}: the form root has ONE postProcessor slot and the "
                f"lifecycle's TransitionGuard already claims it; post_processor "
                f"'{_pp['class_name']}' cannot also be realized")
        out["postProcessor"] = {"className": _pp["class_name"],
                                "runOn": _pp.get("run_on", "create"),
                                "properties": _pp.get("properties") or {}}

    # ---- require-guard (UB-14b, registry 0.9.6): an entity's `validations` — "when this field
    # holds this value, these fields are mandatory" — reached ONLY the RegBB emitter until now.
    # A conditional requirement declared in the model validated, generated, deployed, and was
    # enforced by nothing on the Joget path; registration's REG-FR-041 (a refusal must carry a
    # reason) was law on paper and nothing at the keyboard, and the acceptance case asserting it
    # failed against the running app. It is realized on the same FORM ROOT validator slot
    # UniqueGuard uses (ADR-076: the root always runs, and a readonly or conditionally-hidden
    # field cannot skip it).
    #
    # Placed LAST, after the lifecycle-action section: the condition field of the common case is
    # `lc_action`, which is synthesized above. Computing the placed-field set any earlier makes
    # every action-conditional rule silently unplaceable — the exact failure mode this whole
    # block exists to end.
    #
    # Totality, not best effort. A rule is emitted only onto a form that can actually enforce it,
    # and anything the validator does not realize REFUSES rather than emitting a guard that
    # quietly enforces less than the model declares.
    # ---- live field lookup (D-098, registry 0.9.8): the model's form-level `lookup` block.
    # Rewrites each mapped target field into the joget-lookup-field element and returns the
    # store-side `exists` line that keeps SR-3 honest. Placed here, next to the guards, for
    # the same reason they are: it needs the FINAL field set (the lifecycle/status/FK carriers
    # above may have placed the target), and its refusal rides the one root validator slot.
    lkx = _lookup_block(form, entity, out, path, ix)

    rg = _require_guard(entity, out, path)
    eg = _exists_guard(entity, out, path, ix)
    if lkx:
        eg = dict(eg)
        eg["exists"] = "\n".join(x for x in (eg.get("exists"), lkx) if x)
    if rg or eg:
        block = dict(rg.get("require_guard") or {})
        block.update(eg)
        out["require_guard"] = block
    if carried_rules or carried_exists:
        if out.get("unique_guard"):
            raise ProjectionError(
                f"{path}: form '{fid}' needs both a unique guard and the check of the record it "
                f"was opened with, and Joget's form root carries exactly ONE validator. Refusing "
                f"rather than silently dropping one; a composite guard is the fix.")
        block = dict(out.get("require_guard") or {})
        for k, lines in (("rules", carried_rules), ("exists", carried_exists)):
            if lines:
                block[k] = "\n".join(x for x in [block.get(k), *lines] if x)
        out["require_guard"] = block
    place_badge_style(out)      # item 2: the state as a badge, drawn by one style per form
    if form.get("layout") != "detail_360":
        # the act bar stands at the head of a flat form, in its own section so that no field
        # changes column; a record console carries it in its header (split_detail_360)
        bar = [s for s in out["sections"] if s.get("label") == acts.ACTS_SECTION
               and any(f.get("id") == acts.ACTS_FIELD for f in s["fields"])]
        for s in bar:
            out["sections"].remove(s)
            out["sections"].insert(0, s)
    return out


def _menu_entry_for_form(doc: dict, form_id: str):
    """(the menu, its type) the navigation opens `form_id` with: the first form menu of the form,
    else the first CRUD menu that ADDS with it; (None, None) when there is none. The navigation
    includes the categories the kit adds (hidden ones among them)."""
    for cat in (doc.get("navigation") or {}).get("categories", []):
        for m in cat.get("menus", []):
            if m.get("type") == "form" and m.get("form") == form_id:
                return m, "form"
    for cat in (doc.get("navigation") or {}).get("categories", []):
        for m in cat.get("menus", []):
            if m.get("type") == "crud" and m.get("form") == form_id and m.get("add") is not False:
                return m, "crud"
    return None, None


def _menu_for_form(doc: dict, form_id: str, path: str):
    """(menu customId, opens as a new record?) of the menu the navigation opens `form_id` with —
    a form menu, or a CRUD menu that ADDS with it (`_menu_entry_for_form`). Either way the form
    opens as a NEW record, which the form's prefill fills from the record the act carries; an act
    that stands on a value and opens a form of the record that value names is therefore admitted
    only on a menu that cannot save (`_act_bar`; METHOD-2026-09-28-07, version 2)."""
    m, kind = _menu_entry_for_form(doc, form_id)
    if kind == "form":
        return form_id, False
    if kind == "crud":
        return f"{m.get('list') or 'list_' + form_id}_crud", True
    raise ProjectionError(
        f"{path}: an act opens form '{form_id}', and no menu of the navigation opens it — place "
        f"it on a menu of a category with `hidden: true` (a form that belongs to a record is "
        f"never on a visible menu), and the act opens it from there")


def _carried_param(target: dict, carries: str, ix, path: str) -> str:
    """The address parameter the form an act opens reads the carried record from: the request
    parameter its `prefill` names, else the reference field that points at the carried record."""
    for ks in ((target.get("prefill") or {}).get("keySources") or []):
        if str(ks.get("source", "")).lower() == "requestparam" and ks.get("name"):
            return str(ks["name"])
    tent = ix.entities.get(target.get("entity"), {})
    refs = {a["id"] for a in tent.get("attributes", [])
            if a.get("type") == "ref" and (a.get("ref") or {}).get("entity") == carries}
    placed = [f.get("attr") for s in target.get("sections") or [] for f in s.get("fields", [])
              if f.get("attr") in refs]
    if placed:
        return placed[0]
    raise ProjectionError(
        f"{path}: an act opens form '{target['id']}' carrying a record of '{carries}', and that "
        f"form reads no such record — give it a `prefill` from the address (keySources "
        f"requestParam) or a field that refers to '{carries}'")


# The platform's permission a bar of acts carries: the same plugin, over the same groups, as the
# kit's userview categories (gen_userview permission; delta D-044 for the ;-delimited ids).
ACT_PERMISSION_CLASS = "org.joget.apps.userview.lib.GroupPermission"


def _act_bar(form: dict, entity: dict, acts_here: list, sections: list, ix, path: str) -> list:
    """The act bar of a record's form: its buttons as data, drawn at run time (tools/acts.py).

    One bar for each set of roles the moves name, each shown only to those roles by the
    platform's own permission on the element (METHOD-2026-09-25-01, item 20): a GroupPermission
    naming the move's roles, the groups the kit's own categories name (gen_userview permission),
    and `permissionReadonlyHidden`, without which the platform shows an element a person may not
    use as read-only rather than hiding it (Element.isHidden, wflow-core 9.0.7). A person who may
    not make a move is not offered its button; the trigger form's hidden category and the guard
    (checkRoles) still refuse him if he reaches it by its address. The first bar is `kit_acts`,
    each other `kit_acts_<roles>`, and an act that names no roles (a form it opens) stands in a
    bar with no permission, `kit_acts_any`. Until then one bar held every act, for every viewer."""
    doc = ix.doc
    lc = entity.get("lifecycle") or {}
    moves = {t["id"]: t for t in acts.user_transitions(entity)}
    forms = {f["id"]: f for f in doc.get("forms", [])}
    nav = doc.get("navigation") or {}
    placed = {f.get("attr") or f.get("id"): f for s in sections for f in s["fields"]}
    items = []
    for a in acts_here:
        if a["kind"] == "move":
            t = moves.get(a["transition"])
            if t is None:
                raise ProjectionError(
                    f"{path}: act '{a['label']}' makes the move '{a['transition']}', which is not "
                    f"a move a person makes on '{entity['id']}' (a user-triggered transition that "
                    f"names its roles)")
            gx = str(t.get("guard_expr") or "")
            why = t.get("guard") or (f"Not available while {gx} does not hold" if gx else "")
            items.append(({"label": a["label"], "transition": t["id"],
                           # the move's form headed with this button's words (point 3)
                           "menu": acts.move_form(doc, entity["id"], t["id"], a["label"]),
                           "param": acts.RECORD_PARAM, "from": [t["from"]], "expr": gx,
                           "why": why}, tuple(sorted(a.get("roles") or t.get("roles") or []))))
        else:
            target = forms.get(a["form"])
            if target is None:
                raise ProjectionError(f"{path}: act '{a['label']}' opens form '{a['form']}', "
                                      f"which is not in the model")
            menu, add = _menu_for_form(doc, a["form"], path)
            if a.get("stands_on") and a["carries"] == target.get("entity") \
                    and not carried_param(target):
                # METHOD-2026-09-28-07: a form opened for another record of its own entity reads
                # that record only through its prefill; a field of the form that refers to its own
                # entity (the record it follows) would take the key as its own value
                raise ProjectionError(
                    f"{path}: act '{a['label']}' opens form '{a['form']}' for another record of "
                    f"'{a['carries']}', the one its value '{a['stands_on']}' names, and that form "
                    f"reads no record from the address — give it a `prefill` whose keySources read "
                    f"the record's key from the address (requestParam)")
            if a.get("stands_on") and a["carries"] == target.get("entity"):
                # METHOD-2026-09-28-07, version 2 (the review's gap 1): the act bar holds the
                # record's key, not its row identifier, and the menu opens the form as a NEW record,
                # which the prefill fills from the record the value names — the person reads that
                # record's values on a new, unsaved form. On a menu that saves, saving would write a
                # second record, so the act stands only on a form menu that cannot save: `readonly`
                # on the menu, or a form whose purpose is `view` (project_userview.only_read). A CRUD
                # menu's add mode always saves; its read-only setting is for edit mode alone
                m, kind = _menu_entry_for_form(doc, a["form"])
                if not (kind == "form" and (m.get("readonly") or target.get("purpose") == "view")):
                    where = (f"the CRUD menu '{menu}', which adds a record with it" if kind == "crud"
                             else "its form menu, which saves")
                    raise ProjectionError(
                        f"{path}: act '{a['label']}' stands on the value '{a['stands_on']}' and opens "
                        f"form '{a['form']}' for the record of '{a['carries']}' that value names; the "
                        f"form opens as a new record filled from that record, on {where}, so saving "
                        f"it would write a second record — place form '{a['form']}' on a form menu "
                        f"with `readonly: true` in a category with `hidden: true`, or give the form "
                        f"`purpose: view`, and the act opens it there: the person reads the record's "
                        f"values, and each move made from it reaches the record by its key")
            item = {"label": a["label"], "form": a["form"], "menu": menu, "add": add,
                    "param": _carried_param(target, a["carries"], ix, path)}
            if a.get("stands_on"):
                # METHOD-2026-09-28-07 (the kit's gap G1): the act stands on a value of this form;
                # the bar offers it only while the value is set (`via`: an act whose carried value
                # is empty is not drawn), and carries the record it names
                if a["stands_on"] not in placed:
                    raise ProjectionError(
                        f"{path}: act '{a['label']}' stands on the value '{a['stands_on']}', which "
                        f"this form does not place")
                item["via"] = a["stands_on"]
            elif a["carries"] != entity["id"]:
                via = [fid for fid, f in placed.items()
                       if (({x["id"]: x for x in entity.get("attributes", [])}.get(f.get("id"))
                            or {}).get("ref") or {}).get("entity") == a["carries"]]
                if not via:
                    raise ProjectionError(
                        f"{path}: act '{a['label']}' carries a record of '{a['carries']}', and "
                        f"this form shows no field that refers to one")
                item["via"] = via[0]
            items.append((item, tuple(sorted(a.get("roles") or []))))
    groups: dict = {}                                  # roles -> their acts, in first-seen order
    for item, roles in items:
        groups.setdefault(roles, []).append(item)
    bars = []
    for n, (roles, group) in enumerate(groups.items()):
        payload = {"base": f"/jw/web/userview/{(doc.get('app') or {}).get('id')}/"
                           f"{nav.get('userview_id')}/_/",
                   "key": acts.key_attr(entity), "status": lc.get("status_attr") or "",
                   "acts": group}
        bar = {"id": acts.ACTS_FIELD if n == 0 else
               f"{acts.ACTS_FIELD}_{'_'.join(roles) if roles else 'any'}",
               "type": "html", "html": acts.bar_html(payload)}
        if roles:
            _with_props(bar, permission={"className": ACT_PERMISSION_CLASS,
                                         "properties": {"allowedGroupIds": ";".join(roles)}},
                        permissionReadonlyHidden="true")
        bars.append(bar)
    return bars


def _lookup_block(form: dict, entity: dict, out: dict, path: str, ix) -> str:
    """Realize a form's `lookup:` block. Returns the `exists` line for the root guard ('' none).

    What this closes. A clearance request must name a taxpayer the register knows. Three
    designs were tried and rejected: a SelectBox over the register (unusable past a demo —
    thousands of rows in a dropdown), and twice a browse-the-register-first flow (the
    applicant knows their own TIN; making them find themselves in a list first is a detour,
    not a service). What is left is the obvious thing: TYPE THE KEY, SEE THE NAME. That needs
    an element that watches a TEXT field and resolves it live, which is what registry 0.9.8
    added to joget-lookup-field.

    Two halves, and the second is the one that matters. The element is a SCREEN aid: it shows
    the name, and on an unknown key it clears and says not-found. It cannot refuse a save —
    JavaScript never can. So unless the model opts out, this also emits an UNCONDITIONAL
    `exists` precondition onto the form root, where RequireGuard runs on every save including
    ones that never rendered a screen. Without it "the field went blank" would be the whole
    of the enforcement, and a POST straight to the data API would carry any invented TIN
    into the table (SR-3).

    Totality: every coordinate is checked against the model. A lookup that cannot be wired
    is a build refusal — the failure mode of a mis-wired one is a permanently blank field,
    which reads as "nobody filled that in" and is exactly the kind of silence this kit refuses
    to ship.
    """
    lk = form.get("lookup")
    if not lk:
        return ""
    fid = out["form"]["id"]
    watch, ent_id, match = lk["watch"], lk["entity"], lk["match"]

    # index the placed fields by id so a target can be REWRITTEN in place
    placed = {}
    for sec in out["sections"]:
        for i, f in enumerate(sec["fields"]):
            placed[f.get("id")] = (sec, i, f)

    if watch not in placed:
        raise ProjectionError(
            f"{path}: lookup watches '{watch}', which is not a field on form '{fid}'. A field "
            f"the form does not carry cannot be typed into and cannot be watched.")
    wf = placed[watch][2]
    if wf.get("readonly") or wf.get("managed"):
        raise ProjectionError(
            f"{path}: lookup watches '{watch}', which this form renders READONLY. The whole "
            f"point of a live lookup is that the key is entered here; a readonly key can only "
            f"arrive from somewhere else, and `prefill` is the construct for that.")

    target = ix.entities.get(ent_id)
    if target is None:
        raise ProjectionError(f"{path}: lookup entity '{ent_id}' is not in the model.")
    tattrs = {a["id"] for a in target.get("attributes", [])}
    if match not in tattrs:
        raise ProjectionError(
            f"{path}: lookup matches on '{match}', which is not an attribute of entity "
            f"'{ent_id}' — there is no column to look the key up by.")
    tforms = [f["id"] for f in (ix.forms_by_entity.get(ent_id) or [])]
    if len(tforms) != 1:
        raise ProjectionError(
            f"{path}: lookup entity '{ent_id}' is bound to {len(tforms)} forms "
            f"({', '.join(sorted(tforms)) or 'none'}); the element addresses its source by FORM "
            f"id, so exactly one is needed to derive it unambiguously.")
    lookup_form = tforms[0]

    not_found = lk.get("not_found_message") or (
        f"No {target.get('name') or ent_id} matches this {humanize_label(match)}.")

    for m in lk["mappings"]:
        src, dst = m["from"], m["to"]
        if src not in tattrs:
            raise ProjectionError(
                f"{path}: lookup maps from '{src}', which is not an attribute of entity "
                f"'{ent_id}' — there is nothing to read.")
        if dst not in placed:
            raise ProjectionError(
                f"{path}: lookup maps to '{dst}', which is not a field on form '{fid}'. The "
                f"element IS the target field; with no field to become, the mapping would be "
                f"declared and realized by nothing.")
        if dst == watch:
            raise ProjectionError(
                f"{path}: lookup maps onto '{watch}', the field it watches — the element would "
                f"overwrite the key that drives it.")
        sec, i, old = placed[dst]
        el = {"id": dst, "type": "lookup_field",
              "label": old.get("label") or humanize_label(dst),
              "sourceFieldId": watch,
              "lookupFormId": lookup_form,
              "lookupColumn": src,
              "lookupKeyColumn": match,
              "displayType": "hidden" if old.get("type") == "hidden" else (
                  "readonly" if (old.get("readonly") or old.get("managed")) else "editable"),
              "notFoundMessage": not_found}
        if lk.get("debounce_ms") is not None:
            el["inputDebounceMs"] = int(lk["debounce_ms"])
        if old.get("required"):
            el["required"] = True
        sec["fields"][i] = el
        placed[dst] = (sec, i, el)

    if lk.get("enforce_on_save") is False:
        return ""
    # SR-3. The condition field is EMPTY = unconditional: this is a property of the row, not
    # of an action, and a create form has no action field to hang it on. An empty key is NOT
    # this rule's business (the guard skips it) — requiredness is said elsewhere, and it must
    # be said, or an unresolvable key would be refused while a missing one sailed through.
    _req = wf.get("required") or any(
        v.get("when", {}).get("field") == watch and watch in (v.get("require_fields") or [])
        for v in (entity.get("validations") or []))
    if not _req:
        raise ProjectionError(
            f"{path}: lookup enforces '{watch}' on save, but nothing in the model makes "
            f"'{watch}' REQUIRED on this form. The existence rule deliberately ignores an "
            f"empty key (blank is a requiredness question, not a not-found one), so as declared "
            f"an empty key would save while an unknown one was refused. Mark the attribute "
            f"required, add a validation, or set enforce_on_save: false and say why.")
    if out.get("unique_guard"):
        raise SystemExit(
            f"{path}: form '{fid}' needs both a unique guard and the lookup's existence "
            f"precondition, and Joget's form root carries exactly ONE validator. Refusing "
            f"rather than silently dropping one; a composite guard is the fix.")
    msg = lk.get("enforce_message") or (
        f"The {humanize_label(watch)} entered is not on the "
        f"{target.get('name') or ent_id}. This record cannot be saved against a key the "
        f"register does not hold.")
    line = "|".join(["", "", lookup_form, target["table"], match, watch, "", msg])
    for part in (lookup_form, target["table"], match, watch):
        if "|" in str(part) or "\n" in str(part):
            raise ProjectionError(f"{path}: lookup coordinate '{part}' contains the rules "
                                  f"encoding's separator.")
    return line


def _require_guard(entity: dict, out: dict, path: str) -> dict:
    """{'require_guard': {...}} for the rules this form can enforce, or {} for none.

    Placement rule: the CONDITION field must be on the form (a form that cannot see the
    condition can never trip the rule, and guarding it would be noise). The REQUIRED fields
    need only be attributes of the entity — the guard reads the stored row when a required
    field is not on the form, because the rule is about the record, not about one request
    payload. That is what lets the ADR-066 engine surface (action field only, by design) be
    guarded on the same terms as the officer's form instead of being the way around it."""
    placed = {f.get("attr") or f.get("id") for sec in out["sections"] for f in sec["fields"]}
    known = placed | {a["id"] for a in entity.get("attributes", [])}
    fid = out["form"]["id"]
    rules = []
    for v in (entity.get("validations") or []):
        if v.get("require_grids") or v.get("min_entries") is not None:
            raise SystemExit(
                f"{path}: entity '{entity.get('id')}' declares a validation with require_grids/"
                f"min_entries, which RequireGuard does not realize (it enforces require_fields "
                f"only). Emitting the rule without them would enforce less than the model says.")
        when = v.get("when") or {}
        wf, we = when.get("field"), str(when.get("equals", ""))
        need = list(v.get("require_fields") or [])
        if not wf or not need:
            continue
        if wf not in placed:
            continue          # this form cannot see the condition — not its rule to enforce
        unknown = [f for f in need if f not in known]
        if unknown:
            raise SystemExit(
                f"{path}: a validation on entity '{entity.get('id')}' requires field(s) "
                f"({', '.join(unknown)}) that are neither on form '{fid}' nor attributes of the "
                f"entity — there is nothing for the guard to read, on the form or on the row.")
        for part, label in ((wf, "when.field"), (we, "when.equals"), (",".join(need), "require_fields")):
            if "|" in part or "\n" in part:
                raise SystemExit(f"{path}: validation {label} contains a '|' or a newline, which "
                                 f"is the rules encoding's separator.")
        rules.append(f"{wf}|{we}|{','.join(need)}|{v.get('message') or ''}")

    if not rules:
        return {}
    if out.get("unique_guard"):
        raise SystemExit(
            f"{path}: form '{fid}' needs both a unique guard and a require guard, and Joget's form "
            f"root carries exactly ONE validator. Refusing rather than silently dropping one; a "
            f"composite guard is the fix when a model first needs both.")
    return {"require_guard": {"rules": "\n".join(rules)}}



def _exists_guard(entity: dict, out: dict, path: str, ix=None) -> dict:
    """{'exists': '<lines>'} for the transitions[].requires this form can enforce, or {}.

    A `requires` block says: WHEN THIS ACTION IS TAKEN, a row must exist over there. It is the
    mirror of `uniqueness` — that one refuses when a count is positive, this one when a count is
    zero — and it is what ten of registration's fifteen guards were waiting for. Until 2026-08-05
    those ten were prose, because TransitionGuard.evalGuard reads one attribute of one row, and
    one of them ("a passed or explicitly waived safeguard record exists — no TIN is cancelled
    without one") was PROVED unenforced by walking a case straight through it.

    Placement follows _require_guard exactly: the condition field is `lc_action`, so the rule is
    emitted only onto a form that carries it. Both land in the SAME RequireGuard config — the
    root has one validator slot, and a second plugin would have been mutually exclusive with the
    first on every lifecycle form.
    """
    lc = entity.get("lifecycle") or {}
    placed = {f.get("attr") or f.get("id") for sec in out["sections"] for f in sec["fields"]}
    if "lc_action" not in placed:
        return {}
    fid = out["form"]["id"]
    lines = []
    for t in (lc.get("transitions") or []):
        req = t.get("requires")
        if not req:
            continue
        other = req.get("entity")
        match = req.get("match") or {}
        their, ours = match.get("their"), match.get("ours", "id")
        msg = req.get("message") or ""
        if not (other and their):
            raise SystemExit(
                f"{path}: transition '{t.get('id')}' declares `requires` without an entity and a "
                f"match.their — there is nothing to count and nothing to correlate on.")
        oe = (ix.entities.get(other) if ix else None)
        if oe is None:
            raise SystemExit(f"{path}: transition '{t.get('id')}' requires entity '{other}', "
                             f"which is not in the model.")
        oforms = (ix.forms_by_entity.get(other) or []) if ix else []
        if not oforms:
            raise SystemExit(
                f"{path}: transition '{t.get('id')}' requires a row of '{other}', but no form is "
                f"bound to it — the guard counts through a form's table and has nothing to count "
                f"through. Refusing rather than emitting a guard that cannot fire.")
        oform = req.get("form") or oforms[0]["id"]
        otable = oe.get("table")
        oattrs = {a["id"] for a in oe.get("attributes", [])}
        if their not in oattrs:
            raise SystemExit(f"{path}: transition '{t.get('id')}' correlates on '{their}', which "
                             f"is not an attribute of '{other}'.")
        if ours != "id" and ours not in {a["id"] for a in entity.get("attributes", [])}:
            raise SystemExit(f"{path}: transition '{t.get('id')}' correlates from '{ours}', which "
                             f"is not an attribute of '{entity.get('id')}' (use `id` for the row's "
                             f"own key).")
        # The predicate names COLUMNS, and a Joget column exists only where a form places the
        # field. An attribute on no form is not a field, it is a note — and counting against a
        # column that does not exist throws, which makes the guard FAIL OPEN and lets the
        # transition through. That happened on 2026-08-05 with check_type/outcome on
        # verification_record: the guard was installed, deployed, and silently permissive. Refuse
        # here rather than emit a precondition that cannot be evaluated.
        placed_there = {fl.get("attr") or fl.get("id")
                        for f in oforms for sec in (f.get("sections") or [])
                        for fl in (sec.get("fields") or [])}
        named = set(re.findall(r"\b([a-z][a-z0-9_]*)\b\s*(?:=|!=|<>|<|>|in\b|not\b)",
                               req.get("where", ""), re.I))
        unplaced = sorted((named & oattrs) - placed_there - {their})
        if unplaced:
            raise SystemExit(
                f"{path}: transition '{t.get('id')}' requires a predicate over "
                f"{', '.join(unplaced)} on '{other}', which no form of that entity places — so "
                f"Joget never creates the column and the guard would count against nothing, throw, "
                f"and fail open. Place the field(s) on a form of '{other}', or drop them from the "
                f"predicate.")
        if their not in placed_there:
            raise SystemExit(
                f"{path}: transition '{t.get('id')}' correlates on '{their}', which no form of "
                f"'{other}' places — same reason: no field, no column, no guard.")
        where = _qualify_predicate(req.get("where", ""), sorted(oattrs))
        parts = [t.get("id"), oform, otable, their, ours, where]
        for v in parts:
            if "|" in str(v) or "\n" in str(v):
                raise SystemExit(f"{path}: transition '{t.get('id')}' requires-field {v!r} contains "
                                 f"a '|' or newline, which is the encoding's separator.")
        lines.append(f"lc_action|{t.get('id')}|{oform}|{otable}|{their}|{ours}|{where}|{msg}")
    if not lines:
        return {}
    if out.get("unique_guard"):
        raise SystemExit(
            f"{path}: form '{fid}' needs both a unique guard and a cross-record precondition, and "
            f"Joget's form root carries exactly ONE validator. Refusing rather than silently "
            f"dropping one.")
    return {"exists": "\n".join(lines)}

def split_detail_360(form: dict, spec: dict) -> list:
    """ADR-068 / W-9 (UX-01 CTX-02): render an edit form's sections as a tabbed record
    console. Returns [console_spec, tab_spec, ...] replacing the flat projection.

    Partition: authored sections marked header:true (default: the first) stay on the
    console above the tabs — the context header. Every other authored section becomes a
    tab bound to a per-tab form over the SAME table (empty MultiPagedForm page keys =
    the pages share the console's primary key, i.e. the same row). Synthesized sections
    route by kind: the Lifecycle-action block becomes the Actions tab (with the status
    field injected for the cascading select's controlField dependency, and the
    TransitionGuard postProcessor attached); Status/list-completion/_fk sections stay
    on the console. The guard is attached to BOTH the console and the Actions tab —
    whichever store fires it first consumes lc_action; the other run no-ops (the guard
    returns when the loaded row's action field is empty), so double-fire is safe.
    """
    fid = form["id"]
    fm = spec["form"]
    authored = form.get("sections", [])
    built = spec["sections"]
    n = len(authored)

    def tab_id(suffix: str) -> str:
        pas = "".join(w.capitalize() for w in suffix.split("_"))
        tid = f"{fid}Tab{pas}"
        if len(tid) > 24:
            raise ProjectionError(f"forms/{fid}: tab form id '{tid}' exceeds the 24-char "
                                  f"Joget cap — shorten the section id")
        return tid

    marked = {i for i, s in enumerate(authored) if s.get("header")}
    header_idx = marked or {0}
    # detail_360 keeps the generator-minted section ids: the CTX-02 chrome CSS
    # targets #section1 (the pinned header, first by construction), so authored
    # ids are stripped from the split's sections.
    for b in built:
        b.pop("id", None)
    header_secs, tabs = [], []
    for i, sec in enumerate(authored):
        if i in header_idx:
            header_secs.append(built[i])
        else:
            sid = sec["id"][4:] if sec["id"].startswith("sec_") else sec["id"]
            label = built[i].get("label") or humanize_label(sid)
            tabs.append((tab_id(sid), label, built[i], bool(sec.get("readonly"))))

    actions_secs, extra_header = [], []
    for b in built[n:]:
        (actions_secs if b.get("label") == "Lifecycle action" else extra_header).append(b)

    if len(tabs) + (1 if actions_secs else 0) < 2:
        raise ProjectionError(f"forms/{fid}: layout detail_360 needs at least two tabs "
                              f"(non-header sections + Actions) — unmark a header section")

    tab_specs, pages = [], []
    for tid, label, b, ro in tabs:
        tab_specs.append({"form": {"id": tid, "name": f"{fm['name']} — {label}",
                                   "table": fm["table"],
                                   "description": f"detail_360 tab of {fid} (ADR-068)"},
                          "sections": [b]})
        pages.append({"label": label, "formDefId": tid, "readonly": ro})
    if actions_secs:
        status_field = (spec.get("postProcessor", {}).get("properties", {})
                        .get("statusField", ""))
        placed = {f.get("id") for s in actions_secs for f in s["fields"]}
        if status_field and status_field not in placed:
            # the cascading Action select's controlField must live on the SAME form def.
            # Hidden, not shown: the current state is displayed as a label in the context
            # header (STA-03); on the Actions tab it only needs to carry the value the
            # cascade reads, so a raw enum never leaks onto the tab.
            actions_secs[0]["fields"].insert(0, {"id": status_field, "type": "hidden"})
        tid = tab_id("actions")
        tspec = {"form": {"id": tid, "name": f"{fm['name']} — Actions", "table": fm["table"],
                          "description": f"detail_360 actions tab of {fid} (ADR-068)"},
                 "sections": actions_secs}
        if "postProcessor" in spec:
            tspec["postProcessor"] = dict(spec["postProcessor"])
        tab_specs.append(tspec)
        pages.append({"label": "Actions", "formDefId": tid, "readonly": False})

    # CTX-02 context-header chrome (pattern: context-header) — CSS-only, no scripts.
    # #section1 is the generator's stable id for the console's first section (the
    # pinned header, first by construction); .form-column carries an inline width the
    # band overrides. Verified against the live DX9 section/column templates.
    if header_secs:
        header_secs[0]["fields"].insert(0, {"id": "ctx_header_style", "type": "html", "html": (
            "<style>\n"
            "/* CTX-02 context header — generated chrome; fix in the projector pattern block */\n"
            "#section1 { background:#f7f8fa; border:1px solid #e3e6ea; border-radius:8px;"
            " padding:14px 20px 6px; margin-bottom:16px; }\n"
            "#section1 > .form-column { width:100% !important; float:none; }\n"
            "#section1 .form-cell { display:inline-block; vertical-align:top;"
            " width:auto !important; min-width:185px; margin:0 30px 12px 0;"
            " float:none !important; }\n"
            "#section1 .form-cell > label.label { display:block !important;"
            " float:none !important; width:auto !important; white-space:nowrap;"
            " font-size:11px; text-transform:uppercase; letter-spacing:.05em;"
            " color:#6b7280; font-weight:600; margin:0 0 2px 0 !important; }\n"
            "#section1 .form-cell > input, #section1 .form-cell > select,\n"
            "#section1 .form-cell > textarea, #section1 .form-cell-value {"
            " display:block !important; float:none !important; width:100% !important;"
            " min-width:170px; box-sizing:border-box; white-space:nowrap;"
            " overflow:hidden; text-overflow:ellipsis; }\n"
            "/* read-only values are TEXT, not inputs: strip every control affordance so\n"
            "   the header reads as an identity card, not a data-entry form */\n"
            "#section1 input, #section1 select, #section1 textarea,\n"
            "#section1 .form-cell-value {"
            " border:none !important; background:transparent !important;"
            " box-shadow:none !important; outline:none !important;"
            " padding:0 !important; margin:0 !important; height:auto !important;"
            " min-height:0 !important; line-height:1.3 !important;"
            " font-weight:600 !important; font-size:14px !important; color:#111827 !important;"
            " -webkit-appearance:none !important; -moz-appearance:none !important;"
            " appearance:none !important; }\n"
            "#section1 select { background-image:none !important; text-indent:0; }\n"
            "#section1 .dropdown-toggle, #section1 .caret, #section1 .fa-caret-down,\n"
            "#section1 .icon-caret-down { display:none !important; }\n"
            "#section1 .customHtml { margin:0; }\n"
            "/* an empty read-only figure/date shows nothing, not a format hint (MM/DD/YYYY) */\n"
            "#section1 input::placeholder { color:transparent !important; }\n"
            "/* the one editable control (officer assignment) keeps a light affordance */\n"
            "#section1 .form-cell[class*='assigned_officer'] select,\n"
            "#section1 select[name$='assigned_officer'] {"
            " border:1px solid #cbd5e1 !important; background:#fff !important;"
            " border-radius:6px !important; padding:4px 26px 4px 8px !important;"
            " font-weight:500 !important; -webkit-appearance:auto !important;"
            " -moz-appearance:auto !important; appearance:auto !important; }\n"
            "/* FIN-04: figures are ledger-owned; state provenance + the absence rule */\n"
            "#section1::after { content:'Figures are read from the systems that hold them"
            " \\2014 this application authors no amount; a blank figure means no"
            " feed received yet, not zero.'; display:block; clear:both; margin-top:4px;"
            " padding-top:6px; border-top:1px dashed #e3e6ea; font-size:11px;"
            " color:#6b7280; font-weight:400; }\n"
            "</style>")})

    console_sections = header_secs + extra_header + [{
        "label": "", "columns": 1,
        "fields": [{"id": "tabs360", "type": "multipaged", "displayMode": "tab",
                    "ajaxMode": True, "pages": pages}]}]
    console = {"form": fm, "sections": console_sections}
    if "postProcessor" in spec:
        console["postProcessor"] = spec["postProcessor"]
    if "unique_guard" in spec:
        # ADR-076: the console is the edit store path — CrudMenu _mode=edit fires the root
        # validator (probe-proven on frmCase), so the uniqueness guard rides the console root.
        console["unique_guard"] = spec["unique_guard"]
    if "require_guard" in spec:
        # Same store path, same reason. The guard rides the console root AND the tab that
        # carries the condition field, because either can be the form that is submitted:
        # the console for an edit save, the Actions tab for a lifecycle move. A rule enforced
        # on only one of the two is a rule with a documented way around it.
        console["require_guard"] = spec["require_guard"]
        conds = {r.split("|", 1)[0] for r in spec["require_guard"]["rules"].splitlines() if r.strip()}
        for t in tab_specs:
            if conds & {f.get("attr") or f.get("id") for sec in t["sections"] for f in sec["fields"]}:
                t["require_guard"] = spec["require_guard"]
    return [console] + tab_specs


def _start_process(t: dict) -> str:
    """The process a transition launches on arrival, or ''.

    A `trigger: process` transition (approve/refuse on a registration) belongs to a workflow
    ACTIVITY, not to a form's action select — so the only way a human ever reaches it is an
    assignment, and an assignment only exists if something started an instance. On 2026-08-03
    nothing did: taxRegistration shipped a reg_review process definition, a start whitelist,
    and no caller. An application could be created, submitted and put under verification, and
    from there only bounce to pending_documents and back. Declaring the launch as an EFFECT of
    the transition that arrives at the deciding state puts it where the reader already looks
    for what a move does — beside audit, set_attr and notify — instead of in a second place
    that can silently disagree with the lifecycle. See ADR-094.
    """
    ids = [e.get("process") for e in t.get("effects", [])
           if e.get("type") == "start_process" and e.get("process")]
    if len(ids) > 1:
        raise SystemExit(f"transition '{t.get('id')}' starts more than one process {ids} — "
                         "the config carries one; split the transition or use a process fork")
    pid = ids[0] if ids else ""
    if any(c in pid for c in "|>"):
        raise SystemExit(f"process id '{pid}' contains a config separator ('|' or '>')")
    return pid


def _set_now_fields(t: dict) -> str:
    """CSV of attrs a transition stamps with 'now' (the ADR-034 set-now effect encoding)."""
    return ",".join(e["attr"] for e in t.get("effects", [])
                    if e.get("type") == "set_attr" and "now" in str(e.get("value", "")).lower())


def synthesize_engine_form(entity: dict, ix: Index):
    """ADR-066: the ENGINE-EVENTS surface — one synthesized, API-only form per lifecycle
    entity, carrying ALL its transitions (user + system) as a TransitionGuard config.

    Rationale: ADR-034 puts user transitions on the authored forms; system transitions
    (adapter callbacks: dispatch/deliver/fail; timers: expire) have no surface, yet the
    engines that fire them — and the acceptance runner standing in for those engines —
    need one. This form is that boundary: it carries ONLY the action field and the
    result echo, so an API post of {id, lc_action} can never blank business columns
    (the form-store step writes only the columns of fields ON the form), and it never
    places the status field (the guard loads the row fresh and is the sole status
    writer). It is emitted at projection time only — it is NOT part of the L1 model's
    forms list, so datalist binder resolution and form-count ambiguity rules are
    unaffected. Not navigable: no userview menu references it; reachable through the
    generated app data API (credential-gated), which is exactly the trust boundary the
    runtime adapters use. Returns (feature, spec) or None.
    """
    lc = entity.get("lifecycle") or {}
    status_attr = lc.get("status_attr")
    transitions = lc.get("transitions", [])
    if not (status_attr and transitions):
        return None
    table_mode = ix.conventions.get("form_table", "entity")
    if table_mode != "entity":
        # per-form tables make "the entity's table" ambiguous — no engine surface there
        print(f"  ~ engine surface for '{entity['id']}' skipped: conventions.form_table="
              f"'{table_mode}' (needs 'entity')")
        return None
    pascal = "".join(w.capitalize() for w in entity["id"].split("_"))
    fid = f"frm{pascal}Events"
    cfg = "|".join(f"{t['id']}>{t['to']}>{_set_now_fields(t)}>{t.get('guard_expr', '')}"
                   f">{_start_process(t)}" for t in transitions)
    spec = {
        "form": {"id": fid,
                 "name": f"{entity.get('name', entity['id'])} Engine Events",
                 "table": entity["table"],
                 "description": ("ADR-066 engine surface — transition events from engines/"
                                 "adapters (and the acceptance runner as their surrogate). "
                                 "API-only; not in any userview. Post {id, lc_action}; the "
                                 "TransitionGuard validates against the mm lifecycle config "
                                 "and is the sole status writer.")},
        "sections": [{"label": "Engine event", "columns": 1, "fields": [
            {"id": "lc_action", "type": "hidden", "label": "Action"},
            {"id": "transition_result", "type": "textfield",
             "label": "Last action result", "readonly": True}]}],
        "postProcessor": {
            "className": "com.fiscaladmin.joget.transitionguard.TransitionGuard",
            "runOn": "both",
            "properties": {"entity": entity["id"], "tableName": entity["table"],
                           "statusField": status_attr, "actionField": "lc_action",
                           "transitions": cfg}},
    }
    # The engine surface carries every transition, including the user ones — so a conditional
    # requirement guarded on the officer's form and not here would be a documented way round it
    # for anyone holding the app's API credential. It carries only the action field by design,
    # which is why RequireGuard reads the stored row for a required field that is not on the
    # form: the rule is about the record.
    _p = f"engine:{entity['id']}"
    _rg = _require_guard(entity, spec, _p)
    _eg = _exists_guard(entity, spec, _p, ix)
    if _rg or _eg:
        _block = dict(_rg.get("require_guard") or {})
        _block.update(_eg)
        spec["require_guard"] = _block
    return (entity.get("feature") or "_app", spec)


_NUMBER = re.compile(r"^-?\d+(\.\d+)?$")


def _guard_hql(expr: str, attrs: dict) -> str | None:
    """A move's guard (`<attribute> <eq|ne> <word>`) as the predicate the root guard counts with,
    or None where it is not asked on the form. Only a guard over a word the record holds is asked:
    joget-transition-guard compares numbers as numbers (an empty value counting as nought), and a
    number held as text is not compared so by a count over the table without a cast whose words
    differ from one database to another — such a guard stays the post-processor's, and the act bar
    shows its button disabled, with the guard in words, where the page's facts say it fails."""
    parts = expr.split()
    if len(parts) != 3 or parts[1] not in ("eq", "ne") or parts[0] not in attrs:
        return None
    attr, op, lit = parts
    if _NUMBER.match(lit) or not re.match(r"^[A-Za-z0-9_\-.]+$", lit):
        return None
    col = f"e.customProperties.{attr}"
    if op == "eq":
        return f"{col} = '{lit}'"
    return f"({col} <> '{lit}' OR {col} IS NULL)"


def _target_form(entity: dict, ix) -> str:
    """The form the trigger form reads the record through. FormDataDao reads a row through a
    form's own mapping (delta D-050), so the form must place the record's key and its state:
    the first form of the entity that places both, else its first form."""
    key, status = acts.key_attr(entity), (entity.get("lifecycle") or {}).get("status_attr")
    forms = ix.forms_by_entity.get(entity["id"], [])
    for f in forms:
        placed = {x.get("attr") for s in f.get("sections") or [] for x in s.get("fields", [])}
        if (not key or key in placed) and status in placed:
            return f["id"]
    if forms:
        return forms[0]["id"]
    raise ProjectionError(
        f"entities/{entity['id']}: a person makes moves on '{entity['id']}' and the model binds "
        f"no form to it — the move's form has no form to read the record through")


def synthesize_trigger_forms(entity: dict, ix) -> list:
    """METHOD-2026-09-25-04, item 3: one TRIGGER FORM per move a person makes — the form the
    move's button opens, created as a new record so that its post-processor runs (delta D-015:
    runOn create is the proven path; a CRUD edit never runs it). Returns [(feature, spec)].

    The form, over the entity's table of acts:
      * the record, read only — its key and its state, filled from the record by the
        joget-form-prefill binder from the key in the address (`record`), never typed;
      * the move, a hidden field holding the move's id, and its reason where it has one;
      * what the move needs entered, where the model conditions a requirement on the move
        (`validations` with `when: {field: lc_action, equals: <move>}`), copied to the record;
      * what came of it, written by the post-processor.
    The root guard refuses an act saved without its record, or naming a record that does not
    exist; joget-transition-guard, in its target mode, applies the move to the record named,
    refuses an actor whose roles the move's row in mmEntityTransition does not name (item 5),
    and writes the result on the act."""
    moves = acts.user_transitions(entity)
    if not moves:
        return []
    table_mode = ix.conventions.get("form_table", "entity")
    if table_mode != "entity":
        print(f"  ~ trigger forms for '{entity['id']}' skipped: conventions.form_table="
              f"'{table_mode}' (needs 'entity')")
        return []
    eid = entity["id"]
    lc = entity["lifecycle"]
    status = lc["status_attr"]
    key = acts.key_attr(entity)
    attrs = {a["id"]: a for a in entity.get("attributes", [])}
    tform = _target_form(entity, ix)
    act_table = acts.act_table(entity)
    ename = entity.get("name") or humanize_label(eid)
    out = []
    # METHOD-2026-09-26-02, point 3: one trigger form for each set of words a button of the move
    # says (acts.plan), headed with those words — the label the model's act gives the move, not
    # the move's identifier made into words, which is what a form that declares no acts offers
    mplan = (ix.doc.get(acts.PLAN_KEY) or acts.plan(ix.doc)).get(eid) or {}
    states = {s["id"]: s.get("name") or humanize_label(s["id"]) for s in lc.get("states", [])}
    tform_placed = {x.get("attr") or x.get("id") for f in ix.forms_by_entity.get(eid, [])
                    if f["id"] == tform for s in f.get("sections") or []
                    for x in s.get("fields", [])}
    labelled = [(t, words, fid) for t in moves
                for words, fid in ((mplan.get(t["id"]) or {}).get("forms")
                                   or [(acts.humanize(t["id"]), acts.trigger_form_id(eid, t["id"]))])]
    for t, label, fid in labelled:
        tid = t["id"]
        path = f"acts/{fid}"
        key_label = (attrs.get(key) or {}).get("name") or (humanize_label(key) if key else ename)
        head = [{"id": acts.KEY_FIELD, "type": "textfield", "label": key_label, "readonly": True},
                {"id": acts.STATE_FIELD, "type": "select", "readonly": True,
                 "label": (attrs.get(status) or {}).get("name") or humanize_label(status),
                 "static_options": [{"value": s["id"],
                                     "label": s.get("name") or humanize_label(s["id"])}
                                    for s in lc.get("states", [])],
                 "props": {"readonlyLabel": "true"}, BADGE_KEY: state_tones(lc)}]
        if not key:
            # no business key: the record is named by its row identifier, as the address
            # carries it; the post-processor refuses one that names no record
            head[0]["value"] = f"#requestParam.{acts.RECORD_PARAM}#"
        move = [{"id": acts.ACTION_FIELD, "type": "hidden", "props": {"value": tid}}]
        copy_fields, rules, exists = [], [], []
        reason = t.get("reason")
        if reason:
            rf = {"id": acts.REASON_FIELD, "label": "Reason"}
            if reason.get("vocabulary"):
                rf["type"] = "select"
                lk = lov.lookup_for(ix.doc, reason["vocabulary"])
                if lk:
                    rf["lookup"] = lk
                else:
                    rf["static_options"] = _static_options(
                        {"vocabulary": reason["vocabulary"]}, ix, path)
            else:
                rf["type"] = "textarea"
            if reason.get("required", True):
                rf["required"] = True
            move.append(rf)
        for v in entity.get("validations") or []:
            when = v.get("when") or {}
            if when.get("field") != acts.ACTION_FIELD or str(when.get("equals")) != tid:
                continue
            need = [f for f in (v.get("require_fields") or []) if f in attrs]
            for f in need:
                if f not in copy_fields:
                    move.append(project_field({"attr": f, "required": False}, entity, ix, False,
                                              f"{path}/inputs"))
                    copy_fields.append(f)
            rules.append(f"{acts.ACTION_FIELD}|{tid}|{','.join(need)}|{v.get('message') or ''}")
        move.append({"id": acts.RESULT_FIELD, "type": "textfield", "label": "What came of it",
                     "readonly": True})
        rules.insert(0, f"{acts.ACTION_FIELD}|{tid}|{acts.KEY_FIELD}|This move is made from its "
                        f"record: open the {ename.lower()} and choose the move there.")
        target_table = entity["table"]
        if key:
            exists.append("|".join(["", "", tform, target_table, key, acts.KEY_FIELD, "",
                                    f"No {ename.lower()} has this {key_label.lower()}."]))
            # METHOD-2026-09-26-02, point 1: a move that is refused says why, in words, on the
            # screen. The root guard refuses before anything is saved, and the platform shows a
            # refusal on the form's root at the head of the form (form.ftl, Joget DX 9.0.7). What
            # the post-processor would otherwise refuse after the save, and write only on the act,
            # is asked here first: the record stands in the state the move leaves from, and the
            # move's guard, where the guard reads a word the record holds, holds.
            # The count reads the record through the form `tform`, and a form reads only the
            # columns it places (delta D-050): a column it does not place is not asked, since a
            # count the platform cannot make refuses every save (joget-require-guard, fail-closed).
            sname = states.get(t["from"], t["from"])
            if status in tform_placed:
                exists.append("|".join([
                    "", "", tform, target_table, key, acts.KEY_FIELD,
                    f"e.customProperties.{status} = '{t['from']}'",
                    f"{label} is made only when the {ename.lower()} is {sname}, and this "
                    f"{ename.lower()} is not {sname} now."]))
            gq = _guard_hql(str(t.get("guard_expr") or ""),
                            {a: attrs[a] for a in attrs if a in tform_placed})
            if gq:
                exists.append("|".join([
                    "", "", tform, target_table, key, acts.KEY_FIELD, gq,
                    t.get("guard") or f"{label} is not made while {t['guard_expr']} does not "
                                      f"hold."]))
        req = t.get("requires")
        mappings = ([{"from": key, "to": acts.KEY_FIELD}] if key else []) + \
            [{"from": status, "to": acts.STATE_FIELD}]
        if req:
            ours = (req.get("match") or {}).get("ours", "id")
            ofld = "record_id" if ours == "id" else ours
            if ofld not in {x["id"] for x in head}:
                head.append({"id": ofld, "type": "textfield", "readonly": True,
                             "label": "Record identifier" if ours == "id"
                             else ((attrs.get(ours) or {}).get("name") or humanize_label(ours))})
                mappings.append({"from": ours, "to": ofld})
            other = ix.entities.get(req.get("entity")) or {}
            oforms = ix.forms_by_entity.get(req.get("entity")) or []
            if not oforms:
                raise ProjectionError(f"{path}: move '{tid}' requires a row of "
                                      f"'{req.get('entity')}', which no form is bound to")
            where = _qualify_predicate(req.get("where", ""),
                                       sorted(a["id"] for a in other.get("attributes", [])))
            exists.append("|".join([acts.ACTION_FIELD, tid, req.get("form") or oforms[0]["id"],
                                    other.get("table", ""), (req.get("match") or {}).get("their", ""),
                                    ofld, where, req.get("message") or ""]))
        for part in rules + exists:
            if "\n" in part:
                raise ProjectionError(f"{path}: a rule of move '{tid}' holds a newline")
        fm = {"id": fid, "name": f"{label} — {ename}", "table": act_table,
              "description": f"The move '{tid}' of {eid}, made from its record "
                             f"(METHOD-2026-09-25-04; trigger form, delta D-015)"}
        if key:
            fm["loadBinder"] = "prefill"
            fm["prefill"] = {"enabled": True, "onlyOnAdd": True,
                             "keySources": [{"source": "requestParam", "name": acts.RECORD_PARAM}],
                             "formId": tform, "table": target_table, "matchField": key,
                             "mappings": mappings}
        elif req:
            raise ProjectionError(f"{path}: move '{tid}' requires another record, and "
                                  f"'{eid}' has no business key (`pk.attr`) to read the record by")
        spec = {"form": fm,
                "sections": [{"label": ename, "columns": 1, "fields": head},
                             {"label": label, "columns": 1, "fields": move}],
                "postProcessor": {
                    "className": acts.GUARD_CLASS, "runOn": "create",
                    "properties": {
                        "entity": eid, "tableName": target_table, "statusField": status,
                        "actionField": acts.ACTION_FIELD,
                        "transitions": f"{tid}>{t['to']}>{_set_now_fields(t)}>"
                                       f"{t.get('guard_expr', '')}>{_start_process(t)}",
                        "targetField": acts.KEY_FIELD, "targetKeyColumn": key,
                        "targetForm": tform, "actForm": fid, "actTable": act_table,
                        "checkRoles": "true",
                        "reasonField": acts.REASON_FIELD if reason else "",
                        "copyFields": ",".join(copy_fields)}},
                "require_guard": {"rules": "\n".join(r for r in rules if r),
                                  **({"exists": "\n".join(exists)} if exists else {})}}
        place_badge_style(spec)
        out.append((entity.get("feature") or "_app", spec))
    return out


# --------------------------------------------------------------------------- #
# Emission                                                                     #
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
    ap.add_argument("app", type=pathlib.Path, help="Layer-1 application model YAML")
    ap.add_argument("--out", type=pathlib.Path, required=True, help="output directory (build area)")
    ap.add_argument("--feature", help="project only forms tagged with this feature id")
    ap.add_argument("--schema", type=pathlib.Path, default=l1.DEFAULT_SCHEMA)
    custody.add_arg(ap)
    args = ap.parse_args()

    # ---- rule: refuse invalid input (schema, then lint) ----------------------
    schema = l1.load(args.schema)
    doc = l1.load(args.app)
    errs = l1.schema_errors(schema, doc)
    if errs:
        print(f"SCHEMA: {len(errs)} error(s) — refusing to project")
        for e in errs:
            print(f"  - {e}")
        return 1
    print("SCHEMA: ok")
    lint = l1.Lint(doc, args.app).run()
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
        print(f"PROJECT: 1 error(s) — nothing emitted")
        print(f"  - lists of values: {exc}")
        return 3
    doc = acts.augment(doc)                 # the moves' forms and their hidden menus (acts.py)
    ix = Index(doc, args.app)

    forms = doc.get("forms", [])
    if args.feature:
        forms = [f for f in forms if f.get("feature") == args.feature]

    projected, errors = [], []
    for form in forms:                                  # document order — deterministic
        try:
            spec = project_form(form, ix)
            specs = (split_detail_360(form, spec)       # ADR-068: console + per-tab forms
                     if form.get("layout") == "detail_360" else [spec])
        except ProjectionError as exc:
            errors.append(str(exc))
            continue
        feature_dir = form.get("feature") or "_app"
        for sp in specs:
            lov.attach_script(sp, doc)     # each spec is loaded on its own, so each carries it
            rel = pathlib.Path(feature_dir) / "forms" / f"F-{sp['form']['id']}.spec.yml"
            projected.append((rel, sp))

    # ---- ADR-066: synthesized engine-events surfaces (document order — deterministic)
    authored_ids = {f["id"] for f in doc.get("forms", [])}
    for entity in doc.get("entities", []):
        if args.feature and (entity.get("feature") or "_app") != args.feature:
            continue
        syn = synthesize_engine_form(entity, ix)
        if syn is None:
            continue
        feature_dir, spec = syn
        fid = spec["form"]["id"]
        if fid in authored_ids:
            errors.append(f"forms/{fid}: engine-surface id collides with an authored form "
                          f"(rename the authored form or the entity)")
            continue
        rel = pathlib.Path(feature_dir) / "forms" / f"F-{fid}.spec.yml"
        projected.append((rel, spec))

    # ---- METHOD-2026-09-25-04, item 3: one trigger form per move a person makes
    taken = authored_ids | {sp["form"]["id"] for _, sp in projected}
    for entity in doc.get("entities", []):
        if args.feature and (entity.get("feature") or "_app") != args.feature:
            continue
        try:
            trig = synthesize_trigger_forms(entity, ix)
        except ProjectionError as exc:
            errors.append(str(exc))
            continue
        for feature_dir, spec in trig:
            fid = spec["form"]["id"]
            if fid in taken:
                errors.append(f"forms/{fid}: the trigger form of a move collides with a form of "
                              f"the model (rename the model's form)")
                continue
            taken.add(fid)
            lov.attach_script(spec, doc)
            projected.append((pathlib.Path(feature_dir) / "forms" / f"F-{fid}.spec.yml", spec))

    if errors:
        print(f"PROJECT: {len(errors)} error(s) — nothing emitted")
        for e in errors:
            print(f"  - {e}")
        return 3

    for rel, spec in projected:
        emit(spec, header, args.out / rel)
        print(f"  + {rel.as_posix()}")
    print(f"{len(projected)} form spec(s) projected -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
