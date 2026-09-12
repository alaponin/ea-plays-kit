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

# --- 2b: the description stays a trigger blurb, not a second body -------------
# Every skill's description is loaded into context before any skill runs, so the 22 of
# them are a standing cost. They reached 1,850 characters before 0.3.0, restating the
# procedure the body already carries. Keep what selects the skill — what it makes, which
# plays, the trigger phrases, a sibling disambiguator — and leave the rest to the body.
# The ceiling is a ratchet: lower it when the longest come down, never raise it.
DESC_MAX = 1500  # ea-legal-context and ea-governance-drafter sit closest, near 1,450
for name in sorted(shipped):
    fm = open(f"{PLUGIN}/skills/{name}/SKILL.md").read().split("---")[1]
    m = re.search(r"^description: >-\n((?:  .*\n)+)", fm, re.M)
    check(m is not None, f"{name}: no folded 'description: >-' block in the frontmatter")
    if m:
        desc = " ".join(l.strip() for l in m.group(1).splitlines())
        check(len(desc) <= DESC_MAX,
              f"{name}: description is {len(desc)} chars, over the {DESC_MAX} ceiling — "
              f"move the procedure into the body and keep the triggers")

# --- 2c: every reference resolves, and every skill-specific reference is used --
# Both directions. A `references/x.md` the SKILL.md names must exist, or the skill breaks
# in the folder a learner uploaded. And a file in references/ that nothing names is either
# a dead file or a dropped mention.
#
# sync-shared.sh copies shared/*.md into EVERY skill unconditionally — that is the
# contract, not an accident, and it is why those five are exempt from the second
# direction. Do not make the sync course-aware to satisfy this check: which course a
# skill serves is the most volatile fact about it (v0.3.0 moved eight skills from one
# course to two), and a skill that loses a chain it turns out to need fails inside a
# folder that has already been uploaded. A file shipped and never opened costs disk; a
# file needed and not shipped costs the learner.
SHARED = {os.path.basename(f) for f in glob.glob(f"{PLUGIN}/shared/*.md")}
for name in sorted(shipped):
    skill_md = open(f"{PLUGIN}/skills/{name}/SKILL.md").read()
    named = set(re.findall(r"references/([a-z0-9-]+\.md)", skill_md))
    for ref in sorted(named):
        check(os.path.isfile(f"{PLUGIN}/skills/{name}/references/{ref}"),
              f"{name}: SKILL.md names references/{ref}, which is not in the folder")
    for f in sorted(glob.glob(f"{PLUGIN}/skills/{name}/references/*.md")):
        ref = os.path.basename(f)
        check(ref in named or ref in SHARED,
              f"{name}: references/{ref} ships but SKILL.md never names it")
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
    "workbook-chain-kp2.md", # names Progressa's frozen federation identifiers as a rule
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
check(len(chain) == 37, f"workbook-chain.md: parsed {len(chain)} artefact rows, expected 37")
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

# --- 10b: and the chain agrees with itself the other way round --------------
# Every play a Feeds cell names must list that artefact in its own Consumes cell. Without
# this direction a one-way edge survives every check, which is how A10 -> 2.5 and
# A15 -> 4.4/4.7 sat in the file unnoticed and read as dead ends on the GitBook.
consumes_of = {play: set(re.findall(r"\bA\d+(?: rev\.\d+)?\b", consumed))
               for _, play, consumed, _ in chain if re.fullmatch(r"\d+\.\d+", play)}
for art, play, _, fed in chain:
    if art == "A0":
        continue
    for target in re.findall(r"\b\d+\.\d+\b", fed):
        check(target not in consumes_of or art in consumes_of[target],
              f"workbook-chain.md: {art} Feeds lists {target}, but {target} does not consume {art}")

# --- 10c: play-map.json Consumes equals the chain's ---------------------------
# The map is what the GitBook's "Bring" line reads; the chain is what its "feeds" line reads.
# They drifted for ten plays before 0.2.3 and nothing compared them.
_map = json.load(open(f"{ROOT}/tests/play-map.json"))
_chain_consumes = {play: consumed for _, play, consumed, _ in chain}
for play, consumed in _chain_consumes.items():
    if play in _map:
        check(_map[play]["consumes"] == consumed,
              f"play-map.json: {play} consumes {_map[play]['consumes']!r}, "
              f"chain says {consumed!r}")


# =============================================================================
# KP2 — the Government Interoperability Framework plays (v0.3.0)
# Same criteria, second course. KP2 play ids collide with KP1's (both have a 2.4), so the
# KP2 fixtures live under tests/kp2/, its map is tests/kp2/play-map.json, and its chain is
# shared/workbook-chain-kp2.md with B-numbered artefacts.
# =============================================================================
KP2 = f"{ROOT}/tests/kp2"
MAP2 = json.load(open(f"{KP2}/play-map.json"))
check(os.path.isfile(f"{KP2}/progressa-supplement.md"),
      "tests/kp2/progressa-supplement.md missing (A0 §8–§10 for Progressa)")

# --- 2: KP2 fixtures exist and are complete ---------------------------------
for pid, m in MAP2.items():
    d = f"{KP2}/plays/{pid}"
    for f in ("input.md", "expected.md"):
        check(os.path.isfile(f"{d}/{f}"), f"kp2/{pid}: missing {f}")
    check(isinstance(m["skill"], str) and m["skill"], f"kp2/{pid}: no primary skill")
    check(m["skill"] in shipped,
          f"kp2/{pid}: primary skill {m['skill']!r} does not ship in the plugin")
    for s in m["also"]:
        check(s in shipped, f"kp2/{pid}: also-runs skill {s!r} does not ship")
stray2 = set(os.listdir(f"{KP2}/plays")) - set(MAP2) - {".DS_Store"}
check(not stray2, f"kp2 fixture folders not in tests/kp2/play-map.json: {sorted(stray2)}")

# --- 3: KP2 provenance header field set --------------------------------------
for pid in MAP2:
    p = f"{KP2}/plays/{pid}/expected.md"
    if not os.path.isfile(p):
        continue
    text = open(p).read()
    for field in FIELDS:
        check(f"**{field}**" in text,
              f"kp2/{pid}/expected.md: provenance field {field!r} not required")
    check("Posts, not names" in text, f"kp2/{pid}/expected.md: posts-not-names rule missing")
    check("no file, no chart" in text, f"kp2/{pid}/expected.md: text-only rule missing")
    check(f"**Artefact** {MAP2[pid]['artefact']}" in text,
          f"kp2/{pid}/expected.md: header does not name {MAP2[pid]['artefact']!r}")

# --- 2: the README's KP2 table maps every KP2 play to its primary skill --------
kp2_readme = readme[readme.find("## Play → skill — KP2"):] if "## Play → skill — KP2" in readme else ""
check(bool(kp2_readme), "plugin README: no '## Play → skill — KP2' section")
for pid, m in MAP2.items():
    row = re.search(rf"^\|\s*{re.escape(pid)}\s*\|(.+)$", kp2_readme, flags=re.M)
    check(row is not None, f"kp2/{pid}: no row in the plugin README KP2 play table")
    if row:
        check(f"`{m['skill']}`" in row.group(1),
              f"kp2/{pid}: README KP2 row does not name its primary skill {m['skill']}")

# --- 10: the KP2 chain agrees with itself, both ways ------------------------
CHAIN2_ROW = re.compile(
    r"^\|\s*\*\*(B\d+)\*\*[^|]*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*$", re.M)
chain2 = CHAIN2_ROW.findall(open(f"{PLUGIN}/shared/workbook-chain-kp2.md").read())
check(len(chain2) == 38, f"workbook-chain-kp2.md: parsed {len(chain2)} artefact rows, expected 38")
PLAY2 = r"(?:\d+\.\d+|home)"
produces2 = {art: set(re.findall(rf"\b{PLAY2}\b", fd)) for art, _, _, fd in chain2}
consumes2 = {play: set(re.findall(r"\bB\d+\b", consumed)) for _, play, consumed, _ in chain2}
for art, play, consumed, _ in chain2:
    for dep in re.findall(r"\bB\d+\b", consumed):
        check(dep in produces2, f"workbook-chain-kp2.md: {play} consumes {dep}, which has no row")
        check(dep not in produces2 or play in produces2[dep],
              f"workbook-chain-kp2.md: {play} consumes {dep}, but {dep} Feeds does not list {play}")
for art, play, _, fed in chain2:
    for target in re.findall(rf"\b{PLAY2}\b", fed):
        check(target not in consumes2 or art in consumes2[target],
              f"workbook-chain-kp2.md: {art} Feeds lists {target}, but {target} does not consume {art}")

# --- 10c: tests/kp2/play-map.json Consumes equals the KP2 chain's -------------
chain2_consumes = {play: consumed for _, play, consumed, _ in chain2}
for play, consumed in chain2_consumes.items():
    check(play in MAP2, f"workbook-chain-kp2.md: play {play} has no entry in tests/kp2/play-map.json")
    if play in MAP2:
        check(MAP2[play]["consumes"] == consumed,
              f"tests/kp2/play-map.json: {play} consumes {MAP2[play]['consumes']!r}, "
              f"chain says {consumed!r}")
for play in MAP2:
    check(play in chain2_consumes, f"tests/kp2/play-map.json: {play} has no row in workbook-chain-kp2.md")

# --- 11: every play the KP2 GitBook lists as 'no skill yet' now has a gif-* primary ----
# The three skill names the KP2 AI tips cite must ship under exactly those names.
for name in ("gif-decree-draft", "gif-semantic-map", "gif-openapi-gen"):
    check(name in shipped, f"the KP2 tips name `{name}`, which does not ship")


if fails:
    print(f"FAIL — {len(fails)} problem(s):", file=sys.stderr)
    for f in fails:
        print(f"  - {f}", file=sys.stderr)
    sys.exit(1)
print(f"ok — {len(MAP)} KP1 plays, {len(MAP2)} KP2 plays, {len(shipped)} skills, provenance fields, "
      f"README tables, one tagged Progressa and two consistent workbook chains all check out")
