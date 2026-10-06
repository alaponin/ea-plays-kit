#!/usr/bin/env python3
"""specmap — the picture of the work, and the route through it, drawn from the register.

    kit spec map      the things of the method in their bands, and the numbered crossings
    kit spec route    every crossing in the order the work is done, with what states it and
                      the skill that performs it

Both read `templates/spec/slots.yaml` and nothing else, so that the picture cannot show a
line the register does not carry and the route cannot name an act the register does not
cite. How many things and crossings there are is the register's own `counts:` entry
(METHOD-2026-09-25-12); nothing here states a number of its own. The notation is the one
`_working/2026-09-14_improving_the_method/02_SCHEMA.md` §5 fixes; the standard's own figure 6
is drawn by that standard's build source and is not redrawn here.

Exit: 0 drawn · 1 the register carries something the picture cannot draw · 2 could not run.
"""
from __future__ import annotations

import argparse
import pathlib
import sys

import yaml

HERE = pathlib.Path(__file__).resolve().parent
KIT_ROOT = HERE.parent
SLOTS = KIT_ROOT / "templates" / "spec" / "slots.yaml"

BANDS = [
    ("once", "once", "Settled once for the whole system"),
    ("goal", "per-goal", "Walked again for every goal"),
    ("beside", "alongside", "Running alongside"),
    ("made", "produced", "Produced, and written by nobody"),
]
FORMS = ("stated", "kit", "elsewhere", "absent")


def load(path: pathlib.Path):
    spec = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(spec, dict) or "slots" not in spec:
        raise ValueError(f"{path} carries no slots")
    return spec


def form_of(how) -> str | None:
    if not isinstance(how, dict):
        return None
    rest = [k for k in how if k not in ("note", "owner")]
    return rest[0] if len(rest) == 1 else None


def seam_entries(spec):
    """Every seam entry of every slot that carries a `how`, slot order, takes then gives."""
    for s in spec["slots"]:
        for side in ("takes", "gives"):
            for e in (s.get("seams") or {}).get(side) or []:
                if "how" in e:
                    yield s, side, e


def skill_line(spec, receiving) -> str:
    """The skill that performs a crossing: the one the register's `skill` cell names on the row
    the crossing gives to, that row being where the person is when the crossing is made
    (04_TARGET_STATE.md section 2). A crossing that ends outside the twelve things, or on a row
    for which the method has no skill, says so and gives the reason the register gives."""
    row = next((s for s in spec["slots"] if s["n"] == str(receiving)), None)
    if row is None:
        return "no skill of the method: the crossing ends outside the things the register holds"
    sk = row.get("skill")
    if isinstance(sk, dict):
        return "no skill of the method: " + _short(sk.get("absent", ""), 90)
    return str(sk)


def has_skill(spec, receiving) -> bool:
    row = next((s for s in spec["slots"] if s["n"] == str(receiving)), None)
    return bool(row) and not isinstance(row.get("skill"), dict) and bool(row.get("skill"))


def node(n, title) -> str:
    return f'S{n}["{n} · {title}"]'


def cmd_map(spec) -> int:
    hs = spec.get("handovers") or []
    titles = {s["n"]: s["title"] for s in spec["slots"]}
    outside = spec.get("outside") or {}
    placed: dict[str, str] = {}
    lines = ["flowchart TB"]
    for key, cadence, caption in BANDS:
        members = [s for s in spec["slots"]
                   if (s.get("cadence") or [None])[0] == cadence]
        # a thing written in two cadences shows in the later band too, and carries no line
        second = [s for s in spec["slots"] if cadence in (s.get("cadence") or [])[1:]]
        if not members and not second:
            continue
        lines.append(f'  subgraph {key}["{caption}"]')
        lines.append("    direction LR")
        for s in members:
            placed[s["n"]] = key
            lines.append("    " + node(s["n"], _short(s["title"])))
        for s in second:
            lines.append(f'    S{s["n"]}b["{s["n"]} · {_short(s["title"], 48)} '
                         f'— {cadence}"]')
        lines.append("  end")
    for name, what in outside.items():
        lines.append(f'  {name}(["{name} — {_short(what)}"])')

    drawn = 0
    broken = 0
    problems = []
    for h in hs:
        a, b = str(h["from"]), str(h["to"])
        for end in (a, b):
            if end not in titles and end not in outside:
                problems.append(f"handover {h['h']}: {end} is neither a slot nor an endpoint")
        arrow = "-." if h.get("state") == "broken" else "--"
        tail = ".->" if h.get("state") == "broken" else "-->"
        label = f'{h["h"]}'
        if h.get("state") == "broken":
            label += " · broken"
            broken += 1
        elif h.get("state") == "holds-on-paper":
            label += " · holds on paper"
        if h.get("stands_at") == "program":
            label += " · a program stands here"
        src = f"S{a}" if a in titles else a
        dst = f"S{b}" if b in titles else b
        lines.append(f'  {src} {arrow} "{label}" {tail} {dst}')
        drawn += 1

    print("\n".join(lines))
    print()
    print(f"{drawn} lines drawn, {broken} of them broken, from "
          f"{len(spec['slots'])} slot rows.")
    want = spec.get("counts") or {}
    if want.get("things") is not None and want["things"] != len(spec["slots"]):
        problems.append(f"the register states {want['things']} things and carries "
                        f"{len(spec['slots'])} slot rows")
    if want.get("handovers") is not None and want["handovers"] != len(hs):
        problems.append(f"the register states {want['handovers']} handovers and carries {len(hs)}")
    for p in problems:
        print("  - " + p)
    return 1 if problems else 0


def _short(text, n=64):
    text = " ".join(str(text).split())
    return text if len(text) <= n else text[:n - 1].rstrip() + "…"


def cmd_route(spec) -> int:
    hs = {int(h["h"]): h for h in (spec.get("handovers") or [])}
    carried: dict[int, tuple] = {}
    unnumbered = []
    for s, side, e in seam_entries(spec):
        if "handover" in e:
            carried[int(e["handover"])] = (s, side, e)
        else:
            unnumbered.append((s, side, e))

    stated = (spec.get("counts") or {}).get("handovers")
    print(f"THE {stated if stated is not None else len(hs)} NUMBERED CROSSINGS, in the order the "
          f"method standard numbers them")
    print()
    tally = {f: [] for f in FORMS}
    problems = []
    skilled: list[int] = []
    unskilled: list[int] = []
    for num in sorted(hs):
        h = hs[num]
        entry = carried.get(num)
        head = f"{num:>2}  {h['from']} -> {h['to']}   {_short(h.get('crosses'), 70)}"
        print(head)
        state = h.get("state", "?")
        print(f"      state       {state}"
              + (f"; closed by {h['closes_with']}" if h.get("closes_with") else ""))
        print(f"      skill       {skill_line(spec, h['to'])}")
        skilled.append(num) if has_skill(spec, h["to"]) else unskilled.append(num)
        if entry is None:
            print("      how         NOTHING IN THE REGISTER CARRIES THIS NUMBER")
            problems.append(f"handover {num} is carried by no seam entry")
            print()
            continue
        _s, _side, e = entry
        f = form_of(e["how"])
        if f is None:
            problems.append(f"handover {num} carries a how in no single form")
            print("      how         MALFORMED")
            print()
            continue
        tally[f].append(num)
        print(f"      how         {f}: {_short(e['how'][f], 200)}")
        if e["how"].get("note"):
            print(f"                  note: {_short(e['how']['note'], 200)}")
        if e["how"].get("owner"):
            print(f"                  owner: {e['how']['owner']}")
        print()

    print("THE SEAMS THE ROUTE CROSSES THAT THE FIGURE DOES NOT NUMBER")
    print()
    for s, side, e in unnumbered:
        end = e.get("from") if side == "takes" else e.get("to")
        arrow = f"{end} -> {s['n']}" if side == "takes" else f"{s['n']} -> {end}"
        f = form_of(e["how"])
        print(f"      {arrow}   {_short(e['what'], 70)}")
        print(f"      skill       {skill_line(spec, s['n'] if side == 'takes' else end)}")
        print(f"      how         {f}: {_short(e['how'][f], 200)}")
        print()

    print("THE COUNT")
    for f in FORMS:
        nums = tally[f]
        print(f"  {f:<10} {len(nums):>2}   handovers {', '.join(str(n) for n in nums) or '—'}")
    total = sum(len(v) for v in tally.values())
    print(f"  {'total':<10} {total:>2}   and {len(unnumbered)} unnumbered seams beside them")
    print(f"  skill      {len(skilled):>2}   crossings whose receiving row names a skill: "
          f"{', '.join(str(n) for n in skilled) or '—'}")
    print(f"  no skill   {len(unskilled):>2}   crossings whose receiving row has none: "
          f"{', '.join(str(n) for n in unskilled) or '—'}")
    for p in problems:
        print("  - " + p)
    return 1 if problems else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="kit spec map|route", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=("map", "route"))
    ap.add_argument("--slots", type=pathlib.Path, default=SLOTS)
    a = ap.parse_args(argv)
    if not a.slots.exists():
        print(f"could not run: {a.slots} is not there", file=sys.stderr)
        return 2
    try:
        spec = load(a.slots)
    except Exception as exc:                                   # noqa: BLE001
        print(f"could not run: {exc}", file=sys.stderr)
        return 2
    return cmd_map(spec) if a.mode == "map" else cmd_route(spec)


if __name__ == "__main__":
    sys.exit(main())
