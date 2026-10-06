"""Use case diagrams in the house convention: a titled system boundary, the goals
as ovals inside it carrying their reference and their name, the roles as actors
outside it on both sides, and one association line per goal to the role that
pursues it.

Sizing follows the diagram standard:  font_in_doc = source_pt * (display / canvas).
The document places a figure at 16 cm (6.30 in), so a 7.2-inch canvas scales by
0.87 and 10 pt source text lands at 8.7 pt on the page. check_readable() computes
that for every figure and refuses to write one that falls below 7.5 pt.

Everything drawn is read from model.json, which extract.py writes from the model's
record headers: the system's name, the packages and their members, the actors and
their kinds, and the records the goals name. Nothing about one system is written here.
"""
import sys
sys.dont_write_bytecode = True
import json, pathlib, os, textwrap
import signal
try:                       # piping a report into `head` must not truncate the run
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (AttributeError, ValueError):
    pass
sys.path.insert(0, '.')
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Ellipse, Rectangle
import diag as G
from sanitise import clean

# the family is resolved once, in diag.pick_font(), against what is installed

M = json.load(open('model.json'))
os.makedirs('fig', exist_ok=True)

CANVAS_IN = 7.2
COL_CM, MAXH_CM, FLOOR_PT = 16.0, 21.0, 7.5

FS_TITLE = 15.0      # the title above the boundary
FS_FRAME = 12.0      # the boundary's own name
FS_ID = 11.5         # the reference on an oval
FS_NAME = 10.5       # the goal on an oval
FS_ACTOR = 10.5      # an actor's name
FS_BOX = 11.0

INK = "#1F2933"
NAVY = "#1F3864"
LINE = "#7E8C9A"
FRAME_EDGE = "#3E4C59"

# One accent and one wash per group: a dark accent over a very light fill, so
# text on the fill stays readable. Set them in project.py; the cycle below is a
# usable default for a model whose groups have no assigned colours yet.
_CYCLE = [("#1565C0", "#E3F2FD"), ("#2E7D32", "#E8F5E9"), ("#B71C1C", "#FFEBEE"),
          ("#E65100", "#FFF3E0"), ("#5E35B1", "#EDE7F6"), ("#00695C", "#E0F2F1"),
          ("#4527A0", "#EDE7F6"), ("#AD1457", "#FCE4EC"), ("#37474F", "#ECEFF1"),
          ("#455A64", "#ECEFF1"), ("#1F3864", "#E8EEF6")]
try:
    import project as P
    PALETTE = dict(getattr(P, 'PALETTE', {}) or {})
    DEFAULT = getattr(P, 'DEFAULT_COLOUR', ("#1F3864", "#E8EEF6"))
    SYSTEM_LABEL = getattr(P, 'SYSTEM_LABEL', None)
except ImportError:
    PALETTE, DEFAULT, SYSTEM_LABEL = {}, ("#1F3864", "#E8EEF6"), None

BY_ID = {u['id']: u for u in M['use_cases']}
GROUPS = []                     # the packages that hold at least one use case, in the model's order
for p in M['packages']:
    rows = [BY_ID[i] for i in p['members'] if i in BY_ID]
    if rows:
        GROUPS.append({'code': p['code'] or p['name'], 'name': p['name'], 'rows': rows})
for _i, _g in enumerate(GROUPS):
    PALETTE.setdefault(_g['code'], _CYCLE[_i % len(_CYCLE)])
PKG = {g['code']: g for g in GROUPS}
MAX_PER_FIG = 6


def check_readable(path, w, h, smallest):
    disp = COL_CM if COL_CM * h / w <= MAXH_CM else MAXH_CM * w / h
    eff = smallest * (disp / 2.54) / w
    if eff < FLOOR_PT:
        raise AssertionError(f"{path}: smallest text {eff:.1f} pt, floor {FLOOR_PT}")
    return eff


def new(w, h):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    ax.axis("off"); fig.subplots_adjust(0, 0, 1, 1)
    return fig, ax


def save(fig, path, w, h, smallest):
    eff = check_readable(path, w, h, smallest)
    G.save(fig, path, dpi=300)
    print(f"  {os.path.basename(path):26s} {w:.1f}x{h:.1f}in  smallest {eff:.1f}pt")
    return os.path.basename(path)


def title(ax, text, y=97.0):
    ax.text(50, y, text, ha="center", va="top", fontsize=FS_TITLE,
            fontweight="bold", color=NAVY)


def boundary(ax, x0, y0, x1, y1, name):
    ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, y1 - y0,
                                boxstyle="round,pad=0,rounding_size=1.6",
                                facecolor="#FFFFFF", edgecolor=FRAME_EDGE,
                                lw=1.6, zorder=1))
    # the boundary's own name is measured too: a long group name in a wider
    # font runs past the frame it titles
    t = G.fit_top_text(ax, (x0 + x1) / 2, y1 - 2.6, name, x1 - x0,
                       fontsize=FS_FRAME, colour=NAVY, max_lines=2)
    G._register(ax, "frame", (x0 + x1) / 2, (y0 + y1) / 2, x1 - x0, y1 - y0, name, t)


def usecase(ax, x, y, w, h, ref, name, accent, wash, wrap_at=26):
    ax.add_patch(Ellipse((x, y), w, h, facecolor=wash, edgecolor=accent,
                         lw=1.5, zorder=3))
    body = "\n".join(textwrap.wrap(name, wrap_at)) or name
    t = ax.text(x, y - h * 0.09, body, ha="center", va="center", fontsize=FS_NAME,
                color=INK, zorder=5, linespacing=1.35)
    idt = ax.text(x, y + h * 0.27, ref, ha="center", va="center", fontsize=FS_ID,
                  fontweight="bold", color=accent, zorder=5)
    G._register(ax, "oval", x, y, w, h, name, t, extra=[idt])
    return t


def stick(ax, x, y, label, s=1.0):
    ax.plot([x], [y + 3.6 * s], marker="o", ms=7.0 * s, mfc="white",
            mec=NAVY, mew=1.6, zorder=4)
    ax.plot([x, x], [y + 2.9 * s, y + 0.3 * s], color=NAVY, lw=1.6, zorder=3)
    ax.plot([x - 2.1 * s, x + 2.1 * s], [y + 2.2 * s] * 2, color=NAVY, lw=1.6, zorder=3)
    ax.plot([x - 1.8 * s, x, x + 1.8 * s], [y - 2.0 * s, y + 0.3 * s, y - 2.0 * s],
            color=NAVY, lw=1.6, zorder=3)
    # a name is never broken inside a word: "Re-identification Officer" wrapped as
    # "Re-identifica / tion Officer" for a whole version, and no geometry guard sees
    # it because nothing overlaps
    _lines = textwrap.wrap(label, 13, break_on_hyphens=False, break_long_words=False)
    ax.text(x, y - 3.4 * s, "\n".join(_lines), ha="center",
            va="top", fontsize=FS_ACTOR, fontweight="bold", color=NAVY,
            linespacing=1.25)


def assoc(ax, x1, y1, x2, y2, gutter=None):
    """An association, routed orthogonally through a clear vertical lane rather
    than straight. A straight line from an actor at the top to a goal at the
    bottom sweeps through the labels of the actors in between, which is invisible
    at page scale and obvious at full size."""
    pts = [(x1, y1), (x2, y2)] if gutter is None else \
          [(x1, y1), (gutter, y1), (gutter, y2), (x2, y2)]
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    ax.plot(xs, ys, color=LINE, lw=1.1, zorder=2, solid_capstyle="round",
            solid_joinstyle="round")
    store = getattr(ax, "_links", None)
    if store is None:
        store = ax._links = []
    for a, b in zip(pts, pts[1:]):
        store.append((a[0], a[1], b[0], b[1]))


def short_actor(a):
    a = clean(a or '')
    return a.split('—')[0].strip() if '—' in a else a


# =================================================================== overview
def fig_overview():
    """The system boundary with the actual groups inside it and the principal
    roles outside. Everything named here is read from the model, so the figure
    cannot invent a grouping the rest of the document does not use."""
    n = len(GROUPS)
    W, H = CANVAS_IN, 0.86 * max(n, 2) + 2.0
    fig, ax = new(W, H)
    title(ax, "The system, its groups of goals, and the people around it")

    BY1, BY0 = 91.0, 3.0
    boundary(ax, 28, BY0, 72, BY1, SYSTEM_LABEL or clean(M.get('system') or 'The system'))
    top, bot = BY1 - 7.5, BY0 + 2.5
    step = (top - bot) / max(n, 1)
    for i, g in enumerate(GROUPS):
        code = g['code']
        acc, wash = PALETTE.get(code, DEFAULT)
        y = top - step * (i + 0.5)
        h = step * 0.72
        ax.add_patch(FancyBboxPatch((30.5, y - h / 2), 39, h,
                                    boxstyle="round,pad=0,rounding_size=0.5",
                                    facecolor=wash, edgecolor=acc, lw=1.3, zorder=3))
        cnt = len(g['rows'])
        lbl = f"{clean(g['name'])} ({code}) · {cnt} goals"
        # the wrap is measured, not guessed: a character count that fits in one
        # font overflows in another, and the build must survive both
        t = G.fit_text(ax, 50, y, lbl, 39, h, fontsize=FS_NAME, colour=acc,
                       max_lines=3)
        G._register(ax, "box", 50, y, 39, h, clean(g['name']), t)

    # the roles that pursue goals, named exactly as the actor catalogue names them
    seen, roles = set(), []
    for a in M['actors']:
        r = clean(a['name'])
        if a['kind'] == 'primary' and r and r not in seen:
            seen.add(r); roles.append(r)
    lefts, rights = roles[0:8:2][:4], roles[1:8:2][:4]

    def spread(k):
        if k == 0:
            return []
        if k == 1:
            return [(BY1 + BY0) / 2]
        return [BY1 - 8 - i * (BY1 - BY0 - 16) / (k - 1) for i in range(k)]

    for a, y in zip(lefts, spread(len(lefts))):
        stick(ax, 9, y, a); assoc(ax, 13.5, y, 28, y)
    for a, y in zip(rights, spread(len(rights))):
        stick(ax, 91, y, a); assoc(ax, 72, y, 86.5, y)
    return save(fig, 'fig/f01_overview.png', W, H, FS_NAME)


# =================================================================== per group
def fig_package(code, rws, path, part=None):
    n = len(rws)
    acc, wash = PALETTE.get(code, DEFAULT)
    name = clean(PKG[code]['name'])
    W = CANVAS_IN
    H = 1.28 * n + 1.5
    fig, ax = new(W, H)
    heading = name if not part else f"{name} — part {part[0]} of {part[1]}"
    title(ax, heading)

    BY1, BY0 = 90.0, 4.0
    TITLE_BAND = 7.0                      # room under the boundary's own name
    boundary(ax, 25, BY0, 75, BY1, name)

    # the ovals must sit wholly inside the boundary and clear of its title
    avail = (BY1 - TITLE_BAND) - BY0
    oh = min(15.0, avail / n * 0.78)
    inner_top = BY1 - TITLE_BAND - oh / 2 - 1.0
    inner_bot = BY0 + oh / 2 + 1.5
    step = (inner_top - inner_bot) / max(1, n - 1) if n > 1 else 0
    ow = 44

    actors, sides = [], {}
    for r in rws:
        a = short_actor(r['actor'])
        if a and a not in actors:
            actors.append(a)
    for i, a in enumerate(actors):
        sides[a] = 'L' if i % 2 == 0 else 'R'
    lefts = [a for a in actors if sides[a] == 'L']
    rights = [a for a in actors if sides[a] == 'R']

    def spread(k):
        if k == 0:
            return []
        if k == 1:
            return [(inner_top + inner_bot) / 2]
        return [inner_top - i * (inner_top - inner_bot) / (k - 1) for i in range(k)]

    pos = {}
    for a, y in zip(lefts, spread(len(lefts))):
        stick(ax, 8, y, a); pos[a] = (12.5, y)
    for a, y in zip(rights, spread(len(rights))):
        stick(ax, 92, y, a); pos[a] = (87.5, y)

    for i, r in enumerate(rws):
        y = inner_top - i * step if n > 1 else (inner_top + inner_bot) / 2
        usecase(ax, 50, y, ow, oh, r['id'], clean(r['name']), acc, wash)
        a = short_actor(r['actor'])
        if a in pos:
            ax_, ay = pos[a]
            if ax_ < 50:
                assoc(ax, ax_, ay, 50 - ow / 2 - 0.5, y, gutter=20.0)
            else:
                assoc(ax, ax_, ay, 50 + ow / 2 + 0.5, y, gutter=80.0)
    for sh in getattr(ax, "_shapes", []):
        if sh["kind"] != "oval":
            continue
        if (sh["y0"] < BY0 + 0.5 or sh["y1"] > BY1 - 0.5
                or sh["x0"] < 25.5 or sh["x1"] > 74.5):
            raise AssertionError(f"{path}: the goal {sh['label'][:34]!r} is not "
                                 f"wholly inside the system boundary")
    return save(fig, path, W, H, FS_NAME)


# =================================================================== coverage
def fig_coverage(path):
    groups, codes = [], [g['code'] for g in GROUPS]
    for g in GROUPS:
        for r in g['rows']:
            a = short_actor(r['actor'])
            if a and a not in groups:
                groups.append(a)
    have = {(a, c): False for a in groups for c in codes}
    for g in GROUPS:
        for r in g['rows']:
            a = short_actor(r['actor'])
            if (a, g['code']) in have:
                have[(a, g['code'])] = True
    ng, nc = len(groups), len(codes)
    W, H = CANVAS_IN, 0.36 * max(ng, 3) + 1.3
    fig, ax = new(W, H)
    title(ax, "Which role uses which group")
    left, top = 40.0, 88.0
    cw = (97 - left) / max(nc, 1)
    rh = (top - 4) / max(1, ng)
    for j, c in enumerate(codes):
        acc, _ = PALETTE.get(c, DEFAULT)
        ax.text(left + cw * (j + 0.5), top + 2.5, c, ha="center", va="bottom",
                fontsize=FS_NAME, color=acc, fontweight="bold")
    for i, a in enumerate(groups):
        y = top - rh * (i + 0.5)
        ax.text(left - 2.5, y, textwrap.shorten(a, 32, placeholder="…"),
                ha="right", va="center", fontsize=FS_NAME, color=INK)
        for j, c in enumerate(codes):
            x = left + cw * (j + 0.5)
            acc, wash = PALETTE.get(c, DEFAULT)
            if have[(a, c)]:
                ax.add_patch(Rectangle((x - 1.4, y - rh * 0.22), 2.8, rh * 0.44,
                                       facecolor=acc, edgecolor=acc, lw=0.6))
            else:
                ax.add_patch(Rectangle((x - 1.4, y - rh * 0.22), 2.8, rh * 0.44,
                                       facecolor="#F4F6F8", edgecolor="#D3DBE2", lw=0.6))
    return save(fig, path, W, H, FS_NAME)


# =================================================================== information
def fig_entities(path):
    """The records the goals name, in two bands: those some goal changes, and those
    goals only read. Read from the record headers; no entity is named here."""
    changed, read = [], []
    for u in M['use_cases']:
        for e in u['entities'].get('changes', []):
            if e not in changed:
                changed.append(e)
    for u in M['use_cases']:
        for e in u['entities'].get('reads', []):
            if e not in changed and e not in read:
                read.append(e)
    bands = []
    palette = [("#1565C0", "#E3F2FD"), ("#2E7D32", "#E8F5E9")]
    for title_, items, (acc, wash) in (("Changed by a goal", changed, palette[0]),
                                        ("Only read by the goals", read, palette[1])):
        for k in range(0, len(items), 4):
            bands.append((title_ if k == 0 else "", items[k:k + 4], acc, wash))
    if not bands:
        return None
    W, H = CANVAS_IN, 1.25 * len(bands) + 0.9
    fig, ax = new(W, H)
    title(ax, "The records the goals read and change")
    bh = 88.0 / len(bands)
    for i, (t_, items, acc, wash) in enumerate(bands):
        y1 = 89 - bh * i
        y0 = y1 - bh * 0.84
        ax.add_patch(Rectangle((3, y0), 94, y1 - y0, facecolor="#FBFCFD",
                               edgecolor="#D3DBE2", lw=0.9, zorder=1))
        if t_:
            ax.text(6, (y0 + y1) / 2, textwrap.fill(t_, 16), ha="left", va="center",
                    fontsize=FS_NAME, color=acc, fontweight="bold", zorder=4)
        w = 60 / 4
        for j, it in enumerate(items):
            cx = 36 + w * (j + 0.5)
            ax.add_patch(FancyBboxPatch((cx - w * 0.44, (y0 + y1) / 2 - (y1 - y0) * 0.30),
                                        w * 0.88, (y1 - y0) * 0.60,
                                        boxstyle="round,pad=0,rounding_size=0.5",
                                        facecolor=wash, edgecolor=acc, lw=1.2, zorder=3))
            tt = G.fit_text(ax, cx, (y0 + y1) / 2, clean(it), w * 0.88, (y1 - y0) * 0.60,
                            fontsize=FS_NAME, colour=INK, weight="normal", max_lines=3)
            G._register(ax, "box", cx, (y0 + y1) / 2, w * 0.88, (y1 - y0) * 0.60, it, tt)
    return save(fig, path, W, H, FS_NAME)


if __name__ == '__main__':
    fig_overview()
    plan, idx = [], 2
    for g in GROUPS:
        rws = g['rows']
        nparts = max(1, -(-len(rws) // MAX_PER_FIG))
        size = -(-len(rws) // nparts)
        chunks = [rws[i:i + size] for i in range(0, len(rws), size)]
        names = []
        for k, ch in enumerate(chunks):
            sfx = f"_{k + 1}" if len(chunks) > 1 else ""
            part = (k + 1, len(chunks)) if len(chunks) > 1 else None
            nm = fig_package(g['code'], ch, f'fig/f{idx:02d}_pkg_{g["code"]}{sfx}.png', part)
            names.append((nm, part)); idx += 1
        plan.append({'code': g['code'], 'figs': names})
    cov = fig_coverage(f'fig/f{idx:02d}_coverage.png'); idx += 1
    ent = fig_entities(f'fig/f{idx:02d}_entities.png')
    # count what was written rather than adding a constant: the constant said four
    # non-package figures where three are drawn, and printed 26 for 25 files
    written = len(list(pathlib.Path('fig').glob('*.png')))
    json.dump({'packages': plan, 'coverage': cov, 'entities': ent, 'written': written},
              open('figplan.json', 'w'), indent=1)
    print(f"{written} figures")
