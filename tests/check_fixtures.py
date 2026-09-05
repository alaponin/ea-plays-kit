#!/usr/bin/env python3
"""Guards the machine-checkable acceptance criteria; the list is in tests/README.md.

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

# Its worked example names a version. A release that bumps plugin.json and forgets the
# example ships fourteen copies of a stale one, so the bump is checked, not remembered.
version = json.load(open(f"{PLUGIN}/.claude-plugin/plugin.json"))["version"]
check(f"v{version}" in ph,
      f"shared/provenance-header.md: header example does not name v{version}, "
      f"the version in plugin.json")

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
EXEMPT = {
    "provenance-header.md",  # names Progressa as a field rule, not as fixture content
    "output-contract.md",    # same
    "SKILL.md",              # declares its fixture files under a sub-heading instead
}
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
# The 30 Aug 2026 test country is legitimate in exactly two files: one comparator among
# several, and one entry in a source list.
REAL_COUNTRY_AS_COMPARATOR_OK = (
    "ea-comparator-evidence/references/known-frameworks.md",
    "country-context-pack/references/api-guide.md",
)

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
    check("Gambia" not in text or rel.endswith(REAL_COUNTRY_AS_COMPARATOR_OK),
          f"{rel}: the 30 Aug 2026 test country is back as this file's own context; "
          f"it belongs only as one comparator among several")

# The fixture tree is one-country: nothing but the two files each play needs.
for pid in sorted(os.listdir(f"{ROOT}/tests/plays")):
    d = f"{ROOT}/tests/plays/{pid}"
    if not os.path.isdir(d):
        continue
    extra = set(os.listdir(d)) - {"input.md", "expected.md", ".DS_Store"}
    check(not extra, f"tests/plays/{pid}: not a Progressa-only fixture folder: {sorted(extra)}")


# --- 10: the workbook chain agrees with itself ------------------------------
# Every artefact a play consumes must list that play in its producer's Feeds cell.
# A0 is exempt: its Feeds cell is prose, and the section table above it routes §1-§7.
CHAIN_ROW = re.compile(
    r"^\|\s*\*\*(A\d+(?: rev\.\d+)?)\*\*[^|]*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*$",
    re.M)
chain = CHAIN_ROW.findall(open(f"{PLUGIN}/shared/workbook-chain.md").read())
check(len(chain) == 38, f"workbook-chain.md: parsed {len(chain)} artefact rows, expected 38")
produces = {art: set(re.findall(r"\b\d+\.\d+\b", fd)) for art, _, _, fd in chain}
for art, play, consumed, _ in chain:
    if not re.fullmatch(r"\d+\.\d+", play):
        continue
    for dep in re.findall(r"\bA\d+(?: rev\.\d+)?\b", consumed):
        if dep == "A0":
            continue
        check(dep in produces, f"workbook-chain.md: {play} consumes {dep}, which has no row")
        check(dep not in produces or play in produces[dep],
              f"workbook-chain.md: {play} consumes {dep}, but {dep} Feeds does not list {play}")


if fails:
    print(f"FAIL — {len(fails)} problem(s):", file=sys.stderr)
    for f in fails:
        print(f"  - {f}", file=sys.stderr)
    sys.exit(1)
print(f"ok — {len(MAP)} plays, {len(shipped)} skills, provenance fields, README table, "
      f"one tagged Progressa and a consistent workbook chain all check out")
