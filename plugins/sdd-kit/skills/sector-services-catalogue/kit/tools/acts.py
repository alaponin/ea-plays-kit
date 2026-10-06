#!/usr/bin/env python3
"""The acts of a record: a move made by a button named after it, and a form opened from the record
it belongs to (METHOD-2026-09-25-04, items 3 and 4).

What a person sees. A record with a lifecycle shows its state as a badge (item 2) and, above its
fields, one button for each act it offers: a move of its lifecycle ("Close the case"), or a form
that belongs to it ("Choose the enforcement acts"). A move's button is offered only in the states
the move leaves from, and is shown disabled, with the move's guard in words, where the record's
own facts say the guard does not hold (STA-01, STA-02). The single "Action" drop-down the kit used
to place on every record form is gone.

How a move is made. The platform runs a form's post-processor when a record is CREATED through a
form, and not when one is edited through a CRUD menu (delta D-015). So each move a person makes
gets its own small form — a "trigger form" — over a table of acts: the button opens it with the
record's key in the address, the form shows the record read-only (filled from the record by the
joget-form-prefill binder), asks for the move's reason when the move has one, and on save the
joget-transition-guard post-processor applies the move to the record named, checks the role that
may make it (item 5), and writes what came of it on the act. The act is a record in its own
right: who asked for which move on which record, when, why, and with what result.

Where the forms stand. The trigger forms stand in hidden categories of the navigation — one per
set of roles, visible to those roles only, and never shown in the menu — so that they open from
their record and from nowhere else (item 4).

This module is pure: the same model gives the same names, the same plan and the same markup.
"""
from __future__ import annotations

import copy
import hashlib
import json
import re

PLAN_KEY = "x-acts-plan"
ACTS_FIELD = "kit_acts"               # the act bar on a record's form
ACTS_SECTION = "Acts"                 # the synthesized section that carries it
KEY_FIELD = "record_key"              # the trigger form's read-only field naming the record
# The address parameter a move's button carries is the name of the field that shows the record
# on the move's form (METHOD-2026-09-26-02, point 1). The platform saves a read-only field with
# the value its load binder gives it on the submit, never the value the page posts (delta D-069),
# and the form menu posts to its own address with `?_action=submit` alone (FormMenu, Joget DX
# 9.0.7: the submit address is the menu's address and `?_action=submit`, and `&id=` for a record
# that exists), so a parameter of the address that opened the form is gone when it is saved. The
# prefill binder reads its key again on the submit, from the request's parameters: under the
# field's own name it finds the value the page posts; under any other name it found nothing, and
# the act was saved naming no record (an issue found in testing: "no record is named").
RECORD_PARAM = KEY_FIELD
STATE_FIELD = "record_state"          # the trigger form's badge of the record's state
ACTION_FIELD = "lc_action"            # the move a trigger form makes (hidden, fixed)
RESULT_FIELD = "transition_result"    # what came of it
REASON_FIELD = "reason"               # the move's reason, where it has one
ID_CAP = 24                           # D-022: 24-character form-id / table-name cap
GUARD_CLASS = "com.fiscaladmin.joget.transitionguard.TransitionGuard"


class ActsError(Exception):
    """A model whose acts cannot be generated."""


# --------------------------------------------------------------------------- #
# Names                                                                         #
# --------------------------------------------------------------------------- #

def pascal(s: str) -> str:
    return "".join(w[:1].upper() + w[1:] for w in re.split(r"[^A-Za-z0-9]+", s) if w)


def _h4(s: str) -> str:
    return hashlib.sha1(s.encode("utf-8")).hexdigest()[:4]


def _cap(name: str, cap: int = ID_CAP) -> str:
    """The name when it fits the cap; else the name cut short and a 4-hex digest of the whole."""
    return name if len(name) <= cap else name[:cap - 4] + _h4(name)


def humanize(tid: str) -> str:
    s = str(tid).replace("_", " ").strip()
    return s[:1].upper() + s[1:]


def trigger_form_id(entity_id: str, tid: str) -> str:
    """`act` + the entity + the move, e.g. actDcaseClose. Past the 24-character cap the ENTITY's
    part is shortened first, so the move stays readable, and three hex characters of the whole
    name keep two shortened names apart: actPermitApSubmitb7e."""
    e, t = pascal(entity_id), pascal(tid)
    full = "act" + e + t
    if len(full) <= ID_CAP:
        return full
    room = ID_CAP - 3 - len(t) - 3
    if room >= 3:
        return "act" + e[:room] + t + _h4(full)[:3]
    return _cap(full)


def act_table(entity: dict) -> str:
    return _cap(str(entity["table"]) + "_act")


# --------------------------------------------------------------------------- #
# The moves a person makes, and the plan the projectors share                  #
# --------------------------------------------------------------------------- #

def user_transitions(entity: dict) -> list:
    """The moves a person makes: user-triggered transitions that name the roles that may make
    them — the same set the kit's Action select used to offer."""
    lc = entity.get("lifecycle") or {}
    if not lc.get("status_attr"):
        return []
    return [t for t in lc.get("transitions", [])
            if t.get("trigger", "user") == "user" and t.get("roles")]


def key_attr(entity: dict) -> str:
    """The record's key as a form stores a reference to it: its business key (`pk.attr`) when
    the model declares one, else the platform's row identifier ('')."""
    return str((entity.get("pk") or {}).get("attr") or "")


def move_labels(doc: dict) -> dict:
    """{entity id: {tid: [labels]}} — the words the model's `acts` give each move, in the order its
    forms give them (METHOD-2026-09-26-02, point 3: the move's form is headed with, and its button
    says, the label the model's acts give the move, not the move's identifier made into words).
    Two acts that give one move different words — the enforcement action's `conclude`, "Record the
    telephone contact" on one form and "File the visit report" on another — give it a form for
    each. A form that declares no acts offers the move under its identifier made into words, and
    its button opens the form of the move's first label; a move no act names keeps its identifier
    made into words (plan)."""
    ents = {e["id"]: e for e in doc.get("entities", [])}
    out: dict = {}
    for f in doc.get("forms", []):
        e = ents.get(f.get("entity"))
        if not e or not user_transitions(e) or "acts" not in f:
            continue
        for a in acts_of(f, e):
            if a["kind"] != "move":
                continue
            seen = out.setdefault(e["id"], {}).setdefault(a["transition"], [])
            if a["label"] not in seen:
                seen.append(a["label"])
    return out


def label_form_id(entity_id: str, tid: str, n: int, label: str) -> str:
    """The trigger form of the move `tid` under its n-th label: the first keeps the move's own
    form id (trigger_form_id); another label, the same move's form headed otherwise, takes a
    short digest of its words (actEnforcementActConcl3f1)."""
    return trigger_form_id(entity_id, tid) if n == 0 else \
        trigger_form_id(entity_id, f"{tid}_{_h4(label)}")


def plan(doc: dict) -> dict:
    """{entity id: {tid: {form, table, label, forms, roles, from, to}}} for every move a person
    makes. `forms` is [(label, form id)], one trigger form for each set of words a button of the
    move says; `form` and `label` are the first of them."""
    out: dict = {}
    labels = move_labels(doc)
    for e in doc.get("entities", []):
        moves = user_transitions(e)
        if not moves:
            continue
        table = act_table(e)
        out[e["id"]] = {}
        for t in moves:
            words = (labels.get(e["id"]) or {}).get(t["id"]) or [humanize(t["id"])]
            forms = [(w, label_form_id(e["id"], t["id"], n, w)) for n, w in enumerate(words)]
            out[e["id"]][t["id"]] = {"form": forms[0][1], "table": table, "label": forms[0][0],
                                     "forms": forms, "roles": list(t.get("roles") or []),
                                     "from": t["from"], "to": t["to"]}
    return out


def move_form(doc: dict, entity_id: str, tid: str, label: str) -> str:
    """The trigger form a button of the move `tid` saying `label` opens."""
    info = ((doc.get(PLAN_KEY) or plan(doc)).get(entity_id) or {}).get(tid) or {}
    for words, fid in info.get("forms") or []:
        if words == label:
            return fid
    return info.get("form") or trigger_form_id(entity_id, tid)


def _category_id(roles: list) -> str:
    joined = "_".join(sorted(roles))
    cid = "cat_acts_" + joined
    return cid if len(cid) <= 40 else "cat_acts_" + _h4(joined)


def augment(doc: dict) -> dict:
    """The model with a hidden category of the navigation for the trigger forms of each set of
    roles (item 4: a form that belongs to a record never stands on a visible menu). The model
    given is not changed. Idempotent."""
    if doc.get(PLAN_KEY) is not None:
        return doc
    d = copy.deepcopy(doc)
    p = plan(d)
    d[PLAN_KEY] = p
    nav = d.get("navigation")
    if not nav or not p:
        return d
    names = {r["id"]: r.get("name") or r["id"] for r in d.get("roles", [])}
    by_roles: dict = {}
    for eid in sorted(p):
        for tid, info in p[eid].items():
            key = tuple(sorted(info["roles"]))
            for words, fid in info["forms"]:
                # the page is headed with the button's words, and its button says them
                # (METHOD-2026-09-26-02, point 3; the form menu's submitButtonLabel)
                by_roles.setdefault(key, []).append(
                    {"type": "form", "label": words, "form": fid, "submit_label": words})
    cats = []
    for roles, menus in sorted(by_roles.items()):
        cats.append({"id": _category_id(list(roles)),
                     "label": "Moves — " + ", ".join(names.get(r, r) for r in roles),
                     "roles": list(roles), "hidden": True, "x-acts-generated": True,
                     "menus": menus})
    nav.setdefault("categories", []).extend(cats)
    return d


# --------------------------------------------------------------------------- #
# The acts a record's form offers                                              #
# --------------------------------------------------------------------------- #

def on_value_carries(entity: dict, field_id) -> str | None:
    """The entity whose record the value `field_id` of a record of `entity` names, when its
    attribute is a reference (METHOD-2026-09-28-07: an act standing on that value carries it)."""
    if not field_id:
        return None
    a = next((x for x in entity.get("attributes", []) if x.get("id") == field_id), None) or {}
    return (a.get("ref") or {}).get("entity") if a.get("type") == "ref" else None


def acts_of(form: dict, entity: dict) -> list:
    """The acts the form declares in `acts`, or — where it declares none — one act per move a
    person makes, for a form that is not a create form, offered to the form's roles as the Action
    select was (ADR-034). Each act: {kind: move|form, label, transition|form, carries, roles}."""
    if form.get("purpose") == "create" and "acts" not in form:
        return []
    moves = {t["id"]: t for t in user_transitions(entity)}
    if "acts" in form:
        out = []
        for a in form.get("acts") or []:
            if a.get("transition"):
                t = moves.get(a["transition"]) or {}
                out.append({"kind": "move", "label": a["label"], "transition": a["transition"],
                            "carries": entity["id"], "roles": a.get("roles") or t.get("roles", [])})
            else:
                one = {"kind": "form", "label": a["label"], "form": a["form"],
                       "carries": a.get("carries") or on_value_carries(entity, a.get("stands_on"))
                       or entity["id"], "roles": a.get("roles") or []}
                # METHOD-2026-09-28-07 (the kit's gap G1): an act that stands on a value of the
                # form — offered only while the value holds, carrying the record it names
                if a.get("stands_on"):
                    one["stands_on"] = a["stands_on"]
                out.append(one)
        return out
    form_roles = set((form.get("permissions") or {}).get("roles", []))
    return [{"kind": "move", "label": humanize(t["id"]), "transition": t["id"],
             "carries": entity["id"], "roles": list(t.get("roles") or [])}
            for t in moves.values() if not form_roles or set(t.get("roles") or []) & form_roles]


# --------------------------------------------------------------------------- #
# The act bar: the buttons, and the small runtime piece that offers them       #
# --------------------------------------------------------------------------- #

_BAR = """<div class="kit-acts" data-kit-acts="1"></div>
<style>
.kit-acts { display:flex; flex-wrap:wrap; gap:8px; align-items:flex-start; margin:4px 0 12px; }
.kit-acts .kit-act-wrap { display:inline-flex; flex-direction:column; max-width:280px; }
.kit-acts .kit-act.disabled { opacity:.55; cursor:not-allowed; pointer-events:none; }
.kit-acts .kit-act-why { font-size:11px; color:rgb(107,114,128); margin-top:2px; }
</style>
<script>
(function () {
  var A = %(payload)s;
  function field(n) {
    var e = document.querySelector('[name="' + n + '"]');
    if (!e) { var all = document.querySelectorAll('[name$="_' + n + '"]'); e = all.length ? all[0] : null; }
    return e;
  }
  function val(n) {
    /* the value a field holds as the page shows the record: a drop-down's chosen option, even
       a disabled one; a labelled value's hidden field; an input's value. null: not on the page */
    var e = field(n);
    if (!e) { return null; }
    if (e.tagName === "SELECT") { var o = e.options[e.selectedIndex]; return o ? o.value : ""; }
    return e.value || "";
  }
  function urlId() {
    var m = /[?&]id=([^&]*)/.exec(window.location.search);
    return m ? decodeURIComponent(m[1]) : "";
  }
  function holds(expr) {
    /* the move's guard over the record's own facts, as joget-transition-guard reads it:
       <attribute> <eq|ne|gt|lt|ge|le> <literal>. A fact not on the page cannot be judged here,
       and the move is offered: the post-processor judges it on save */
    var p = String(expr).trim().split(/\\s+/);
    if (p.length < 3) { return true; }
    var raw = val(p[0]);
    if (raw === null) { return true; }
    raw = String(raw).trim();
    var lit = p.slice(2).join(" "), a = parseFloat(raw === "" ? "0" : raw), b = parseFloat(lit);
    var num = !isNaN(a) && !isNaN(b) && /^-?[0-9.]+$/.test(raw === "" ? "0" : raw) && /^-?[0-9.]+$/.test(lit);
    switch (p[1]) {
      case "eq": return num ? a === b : raw === lit;
      case "ne": return num ? a !== b : raw !== lit;
      case "gt": return num && a > b;
      case "lt": return num && a < b;
      case "ge": return num && a >= b;
      case "le": return num && a <= b;
    }
    return true;
  }
  function base() {
    var p = window.location.pathname, i = p.indexOf("/_/");
    return i >= 0 ? p.slice(0, i + 3) : A.base;
  }
  function draw() {
    var bar = document.querySelector('.kit-acts[data-kit-acts="1"]:not([data-drawn])');
    if (!bar) { return; }
    bar.setAttribute("data-drawn", "1");
    var key = A.key ? val(A.key) : urlId();
    if (!key) { return; }                          /* a record not yet saved has no acts */
    var state = A.status ? val(A.status) : null;
    A.acts.forEach(function (a) {
      if (a.from && state !== null && a.from.indexOf(state) < 0) { return; }   /* not from here */
      var carried = a.via ? val(a.via) : key;
      if (!carried) { return; }
      var wrap = document.createElement("span"), el;
      wrap.className = "kit-act-wrap";
      if (a.expr && !holds(a.expr)) {
        el = document.createElement("span");
        el.className = "btn kit-act disabled";
        el.setAttribute("aria-disabled", "true");
        el.title = a.why;
        var why = document.createElement("span");
        why.className = "kit-act-why";
        why.textContent = a.why;
        el.textContent = a.label;
        wrap.appendChild(el);
        wrap.appendChild(why);
      } else {
        el = document.createElement("a");
        el.className = "btn btn-primary kit-act";
        el.href = base() + a.menu + "?" + (a.add ? "_mode=add&" : "") +
                  encodeURIComponent(a.param) + "=" + encodeURIComponent(carried);
        el.textContent = a.label;
        wrap.appendChild(el);
      }
      if (a.transition) { el.setAttribute("data-transition", a.transition); }
      if (a.form) { el.setAttribute("data-form", a.form); }
      bar.appendChild(wrap);
    });
  }
  if (document.readyState === "loading") { document.addEventListener("DOMContentLoaded", draw); }
  else { draw(); }
})();
</script>"""


def bar_html(payload: dict) -> str:
    return _BAR % {"payload": json.dumps(payload, sort_keys=True, separators=(",", ":"),
                                         ensure_ascii=False)}


def payload_from_html(html: str) -> dict:
    """The act bar's payload read back out of its markup (for tests and counts)."""
    m = re.search(r"var A = (\{.*?\});\n", html, re.S)
    return json.loads(m.group(1)) if m else {}
