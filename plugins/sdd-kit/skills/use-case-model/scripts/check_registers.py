# -*- coding: utf-8 -*-
"""Check that a consolidation has actually disposed of everything it opened.

    python3 check_registers.py --inventory inventory.md --disposition disposition.md \
                               --rulings rulings.md

Every argument is optional; the checks that need a file it was not given are
skipped and said to be skipped, so the script is useful from the first artefact.

What it enforces is the arithmetic of the consolidation, not its judgement:

  · every input in the register carries an absorption verdict
  · every conflict the inventory raises appears in the disposition register
  · every conflict carries a verdict from the closed vocabulary
  · every conflict whose verdict sends it to the owner has a ruling
  · every ruling answers a conflict that exists
  · no identifier is used twice, and none is skipped in its series

A gap in any of these is a silent decision waiting to happen: an input nobody
said what to do with, a conflict resolved by whoever wrote the paragraph, or a
ruling on a question that has since been withdrawn.

The two vocabularies default to the neutral words of the consolidate step's own
tables (references/consolidate.md): pass --verdicts and --absorption with a
register's own words when it uses others, because a checker that assumes words
the registers do not use reports every healthy row as a hole. The checker prints
the vocabulary it used, so that a report can be read against it.
"""
import argparse
import re
import signal
import sys

try:                       # piping the report into `head` must not raise
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (AttributeError, ValueError):
    pass
from collections import Counter

ap = argparse.ArgumentParser()
ap.add_argument('--inventory')
ap.add_argument('--disposition')
ap.add_argument('--rulings')
ap.add_argument('--conflict-prefix', default='CF')
ap.add_argument('--input-prefix', default='I')
ap.add_argument('--ruling-prefix', default='R')
ap.add_argument('--owner-verdict', default="owner's to rule",
                help='the verdict that sends a conflict to the owner')
ap.add_argument('--absorption', default=(
    'fully absorbed|partly absorbed|not absorbed|not applicable'),
    help='the closed absorption vocabulary, pipe-separated. Set it to YOUR '
         'register\'s words: a checker that assumes a vocabulary the artefact '
         'does not use reports every healthy row as a hole.')
ap.add_argument('--verdicts', default=(
    "settled by the ranking source|settled by the second source|narrowed|"
    "owner's to rule|third-party|not a conflict"),
    help='the closed vocabulary, pipe-separated')
A = ap.parse_args()

VERDICTS = [v.strip() for v in A.verdicts.split('|')]
BAD, NOTE = [], []
print(f"vocabulary: verdicts {' | '.join(VERDICTS)}; the owner's verdict {A.owner_verdict!r}; "
      f"absorption {' | '.join(v.strip() for v in A.absorption.split('|'))}")


def read(p):
    return open(p, encoding='utf-8').read() if p else None


def rows(text, id_pat):
    """Table rows whose first cell is an identifier of the given shape."""
    out = []
    for line in (text or '').split('\n'):
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if not cells or not re.match(id_pat, cells[0].strip('`* ')):
            continue
        out.append([c.strip('`* ') if i == 0 else c for i, c in enumerate(cells)])
    return out


def series(ids, prefix):
    """Duplicates and gaps in an identifier series."""
    nums = sorted({int(m.group(1)) for i in ids
                   if (m := re.match(rf'{prefix}-(\d+)$', i))})
    for i, n in Counter(ids).items():
        if n > 1:
            BAD.append(f"{i} appears {n} times")
    if nums:
        missing = [n for n in range(min(nums), max(nums) + 1) if n not in nums]
        if missing:
            NOTE.append(f"{prefix} series skips {', '.join(f'{prefix}-{n}' for n in missing)}"
                        f" — withdrawn, or lost?")
    return nums


inv, dis, rul = read(A.inventory), read(A.disposition), read(A.rulings)

# ------------------------------------------------------------------ inputs
if inv:
    irows = rows(inv, rf'{A.input_prefix}-\d+$')
    series([r[0] for r in irows], A.input_prefix)
    ABSORB = re.compile('|'.join(re.escape(v.strip())
                                 for v in A.absorption.split('|')), re.I)
    for r in irows:
        if not any(ABSORB.search(c) for c in r[1:]):
            BAD.append(f"input {r[0]} carries no absorption verdict — nothing "
                       f"says what happened to it")
    print(f"inventory: {len(irows)} inputs")
else:
    print("inventory: not given, skipped")

# --------------------------------------------------------------- conflicts
raised = set()
if inv:
    raised = set(re.findall(rf'\b{A.conflict_prefix}-\d+\b', inv))

disposed, owner_cards = {}, set()
if dis:
    drows = rows(dis, rf'{A.conflict_prefix}-\d+$')
    series([r[0] for r in drows], A.conflict_prefix)
    for r in drows:
        row = ' | '.join(r)
        hit = [v for v in VERDICTS if v.lower() in row.lower()]
        if not hit:
            BAD.append(f"conflict {r[0]} carries no verdict from the closed "
                       f"vocabulary — an undisposed conflict is a decision "
                       f"waiting to be taken by whoever writes that paragraph")
        else:
            disposed[r[0]] = hit[0]
            if A.owner_verdict.lower() in row.lower():
                owner_cards.add(r[0])
    print(f"disposition: {len(drows)} conflicts, {len(owner_cards)} to the owner")
    for c in sorted(raised - set(disposed)):
        BAD.append(f"conflict {c} is raised in the inventory but has no row in "
                   f"the disposition register")
    for c in sorted(set(disposed) - raised):
        if raised:
            NOTE.append(f"conflict {c} is disposed of but the inventory does "
                        f"not raise it")
else:
    print("disposition: not given, skipped")

# ----------------------------------------------------------------- rulings
if rul and dis:
    ruled = set()
    for m in re.finditer(rf'\b{A.conflict_prefix}-\d+\b', rul):
        ruled.add(m.group(0))
    rids = re.findall(rf'^#{{1,4}}\s*({A.ruling_prefix}-\d+)\b', rul, re.M) or \
           re.findall(rf'\b({A.ruling_prefix}-\d+)\b', rul)
    series(sorted(set(rids)), A.ruling_prefix)
    print(f"rulings: {len(set(rids))} rulings citing {len(ruled)} conflicts")
    for c in sorted(owner_cards - ruled):
        BAD.append(f"conflict {c} was sent to the owner but no ruling cites it "
                   f"— either it is still open, or it was decided quietly")
    for c in sorted(ruled - set(disposed)):
        NOTE.append(f"a ruling cites {c}, which is not in the disposition "
                    f"register")
elif A.rulings:
    print("rulings: given, but the disposition register is needed to check them")
else:
    print("rulings: not given, skipped")

# ------------------------------------------------------------------ report
if NOTE:
    print(f"\nLOOK — {len(NOTE)}")
    for n in NOTE:
        print(f"  {n}")
if BAD:
    print(f"\nFAIL — {len(BAD)}")
    for b in BAD:
        print(f"  {b}")
    print(f"\nThe consolidation has {len(BAD)} holes in it.")
    sys.exit(1)
print("\nCONSOLIDATION IS CLOSED" + (f" · {len(NOTE)} things to look at" if NOTE else ""))
