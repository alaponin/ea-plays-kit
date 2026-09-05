#!/usr/bin/env python3
"""The repo's one runnable check. Guards acceptance criteria 2, 3 and 8.

  2  every play id in play-map.json has a fixture folder and a README row,
     with exactly one primary skill, and that skill ships in the plugin
  3  every expected.md declares the full provenance-header field set
  8  the shared references are in sync (delegated to sync-shared.sh --check)
  9  Progressa appears in the plugin only as tagged fixture material that agrees
     with tests/progressa.md, no real country leaks in, and the fixture tree holds
     one country

Run: python3 tests/check_fixtures.py
"""
import glob, json, os, re, subprocess, sys

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

# --- 9: Progressa appears in the plugin only as tagged, consistent fixture material
FIXTURE_TOKENS = re.compile(r"\b(Progressa|PDGA|PNIA|PNEA|MoEYS|PLR|Linkup|PayPro)\b")
MARKER = "<!-- fixture: Progressa (fictional)"
# The shared references name Progressa as a field rule, not as fixture content, and a
# SKILL.md declares its fixture files under a `Fixture material` sub-heading instead of
# carrying the marker itself.
EXEMPT = {"provenance-header.md", "output-contract.md", "workbook-chain.md",
          "source-tiers.md", "SKILL.md"}
# Every divergence a review has found; add to it, never prune it. One regex each, kept
# next to the fixture they guard rather than in a parser.
DENY = [
    (r"Youth and Sport", "MoEYS is the Ministry of Education, Youth and Skills"),
    (r"PDGA[^.\n]*payments|payments[^.\n]*PDGA",
     "payments are the Central Bank of Progressa's PayPro, not PDGA's"),
    (r"Establishment Decree",
     "the fixture gives PDGA no decree — a coordinating mandate, a unit under the "
     "Ministry of ICT (§1, §4)"),
    (r"Enrolment system", "PLR runs no system — it is planned, not started (§6)"),
    (r"\bDGA\b", "the body is PDGA — Progressa Digital Government Authority"),
    (r"backbone not yet operational|no backbone exists",
     "Linkup is live in pilot; the gap is MoEYS membership (§1)"),
    (r"contested between MoEYS", "the fixture assigns the NLR to MoEYS (§2)"),
]
# trigger → the exact string tests/progressa.md uses, which the file must also carry
CANON = [
    (r"Ministry of Education, Youth and \w+", "Ministry of Education, Youth and Skills"),
    (r"\bPayPro\b", "Central Bank of Progressa"),
    (r"\(PLR\)\s*\|", "not started"),  # the bodies-table row, not any mention
]
GAMBIA_OK = ("ea-comparator-evidence/references/known-frameworks.md",
             "country-context-pack/references/api-guide.md")

for path in sorted(glob.glob(f"{PLUGIN}/**/*.md", recursive=True)):
    rel = os.path.relpath(path, ROOT)
    text = open(path).read()
    if FIXTURE_TOKENS.search(text):
        check(os.path.basename(path) in EXEMPT or text.startswith(MARKER),
              f"{rel}: names Progressa material but line 1 is not the fixture marker")
        for pat, why in DENY:
            check(not re.search(pat, text),
                  f"{rel}: diverges from tests/progressa.md — {why}")
        for pat, must in CANON:
            check(not re.search(pat, text) or must in text,
                  f"{rel}: matches {pat!r} but never says {must!r}, as tests/progressa.md does")
    check("Gambia" not in text or rel.endswith(GAMBIA_OK),
          f"{rel}: real-country material — the fixture country is Progressa")

# The fixture tree is one-country: nothing but the two files each play needs.
for pid in sorted(os.listdir(f"{ROOT}/tests/plays")):
    d = f"{ROOT}/tests/plays/{pid}"
    if not os.path.isdir(d):
        continue
    extra = set(os.listdir(d)) - {"input.md", "expected.md", ".DS_Store"}
    check(not extra, f"tests/plays/{pid}: not a Progressa-only fixture folder: {sorted(extra)}")


if fails:
    print(f"FAIL — {len(fails)} problem(s):", file=sys.stderr)
    for f in fails:
        print(f"  - {f}", file=sys.stderr)
    sys.exit(1)
print(f"ok — {len(MAP)} plays, {len(shipped)} skills, provenance fields, README table "
      f"and one tagged Progressa all check out")
