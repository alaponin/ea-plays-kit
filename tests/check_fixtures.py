#!/usr/bin/env python3
"""The repo's one runnable check. Guards acceptance criteria 2, 3 and 8.

  2  every play id in play-map.json has a fixture folder and a README row,
     with exactly one primary skill, and that skill ships in the plugin
  3  every expected.md declares the full provenance-header field set
  8  the shared references are in sync (delegated to sync-shared.sh --check)

Run: python3 tests/check_fixtures.py
"""
import json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLUGIN = f"{ROOT}/plugins/ea-plays"
MAP = json.load(open(f"{ROOT}/tests/play-map.json"))
FIELDS = ["Artefact", "Country", "Sector", "Built", "Skill", "Consumed",
          "Feeds", "Sources", "Unverified lines"]
fails = []

def check(cond, msg):
    if not cond:
        fails.append(msg)

# --- 2: fixtures exist and are complete -------------------------------------
shipped = {d for d in os.listdir(f"{PLUGIN}/skills")
           if os.path.isfile(f"{PLUGIN}/skills/{d}/SKILL.md")}
for pid, m in MAP.items():
    d = f"{ROOT}/tests/plays/{pid}"
    for f in ("input.md", "expected.md"):
        check(os.path.isfile(f"{d}/{f}"), f"{pid}: missing {f}")
    check(isinstance(m["skill"], str) and m["skill"],
          f"{pid}: no primary skill")
    check(m["skill"] in shipped,
          f"{pid}: primary skill {m['skill']!r} does not ship in the plugin")
    for s in m["also"]:
        check(s in shipped, f"{pid}: also-runs skill {s!r} does not ship")

stray = set(os.listdir(f"{ROOT}/tests/plays")) - set(MAP) - {".DS_Store"}
check(not stray, f"fixture folders not in play-map.json: {sorted(stray)}")

# --- 3: provenance header field set -----------------------------------------
for pid in MAP:
    p = f"{ROOT}/tests/plays/{pid}/expected.md"
    if not os.path.isfile(p):
        continue
    text = open(p).read()
    for field in FIELDS:
        check(f"**{field}**" in text,
              f"{pid}/expected.md: provenance field {field!r} not required")
    check("Posts, not names" in text, f"{pid}/expected.md: posts-not-names rule missing")
    check("no file, no chart" in text, f"{pid}/expected.md: text-only rule missing")

# The shared reference the skills read must define the same nine fields.
ph = open(f"{PLUGIN}/shared/provenance-header.md").read()
for field in FIELDS:
    check(f"**{field}**" in ph, f"shared/provenance-header.md: field {field!r} undefined")

# --- 2: README maps every play to its primary skill --------------------------
readme = open(f"{PLUGIN}/README.md").read() if os.path.isfile(f"{PLUGIN}/README.md") else ""
for pid, m in MAP.items():
    row = re.search(rf"^\|\s*{re.escape(pid)}\s*\|(.+)$", readme, flags=re.M)
    check(row is not None, f"{pid}: no row in the plugin README play table")
    if row:
        check(f"`{m['skill']}`" in row.group(1),
              f"{pid}: README row does not name its primary skill {m['skill']}")

# --- 8: shared references in sync -------------------------------------------
r = subprocess.run(["bash", f"{PLUGIN}/scripts/sync-shared.sh", "--check"],
                   capture_output=True, text=True)
check(r.returncode == 0, f"shared references drifted:\n{r.stderr.strip()}")

if fails:
    print(f"FAIL — {len(fails)} problem(s):", file=sys.stderr)
    for f in fails:
        print(f"  - {f}", file=sys.stderr)
    sys.exit(1)
print(f"ok — {len(MAP)} plays, {len(shipped)} skills, provenance fields and README table all check out")
