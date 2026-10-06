import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Ellipse, FancyArrowPatch, Rectangle
import matplotlib.patheffects as pe
import textwrap, math

# The document's body font is Calibri; Carlito is its metric-compatible clone
# and is what a Linux build usually has. Naming an absent family does NOT fail
# loudly — matplotlib silently substitutes its default, whose wider glyphs make
# every label overflow its shape, and the geometry guard then reports eleven
# "defects" that are really one missing font. So resolve the family against what
# is actually installed, and say which one was used.
FONT_PREFERENCE = ["Carlito", "Calibri", "Lato", "Helvetica Neue", "Arial",
                   "Liberation Sans", "DejaVu Sans"]


def pick_font(preference=None, announce=True):
    import os
    from matplotlib import font_manager as fm
    forced = os.environ.get("UCM_FONT")
    have = {f.name for f in fm.fontManager.ttflist}
    order = ([forced] if forced else []) + list(preference or FONT_PREFERENCE)
    for name in order:
        if name in have:
            plt.rcParams["font.family"] = name
            if announce:
                print(f"figures drawn in {name}"
                      + ("" if name in ("Carlito", "Calibri")
                         else "  (not metric-compatible with the document's "
                              "Calibri — the guards allow for it)"))
            return name
    raise SystemExit(
        "none of these fonts is installed: " + ", ".join(order) +
        "\nInstall one (Linux: fonts-crosextra-carlito; macOS: brew install "
        "--cask font-carlito) or set UCM_FONT to a family you do have.")


FONT = pick_font()

INK      = "#1F2933"
MUTED    = "#5B6B7B"
SYS_FILL = "#F4F8FB"
SYS_EDGE = "#2C5D7C"
ACTOR    = "#3E4C59"
OVAL = ("#2C5D7C", "#FFFFFF")      # edge, fill of a plain oval


def wrap(s, n):
    return "\n".join(textwrap.wrap(s, n)) if s else ""


def new(w, h):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    ax.axis("off"); ax.set_aspect("auto")
    fig.subplots_adjust(0, 0, 1, 1)
    return fig, ax


def actor(ax, x, y, label, colour=ACTOR, scale=1.0, align="center", fs=7.2):
    """Stick figure with the label below it."""
    s = scale
    ax.plot([x], [y + 3.1 * s], marker="o", ms=4.6 * s, mfc="white",
            mec=colour, mew=1.25, zorder=4)
    ax.plot([x, x], [y + 2.5 * s, y + 0.4 * s], color=colour, lw=1.25, zorder=3)
    ax.plot([x - 1.7 * s, x + 1.7 * s], [y + 2.0 * s] * 2, color=colour, lw=1.25, zorder=3)
    ax.plot([x - 1.4 * s, x, x + 1.4 * s], [y - 1.5 * s, y + 0.4 * s, y - 1.5 * s],
            color=colour, lw=1.25, zorder=3)
    return ax.text(x, y - 2.6 * s, wrap(label, 17), ha=align, va="top",
                   fontsize=fs, color=INK, linespacing=1.25)


def oval(ax, x, y, w, h, label, colours=OVAL, fs=7.0, tag=None, wrap_at=22):
    ec, fc = colours
    ax.add_patch(Ellipse((x, y), w, h, facecolor=fc, edgecolor=ec, lw=1.15, zorder=3))
    t = ax.text(x, y, wrap(label, wrap_at), ha="center", va="center",
                fontsize=fs, color=INK, zorder=5, linespacing=1.2)
    _register(ax, "oval", x, y, w, h, label, t)
    if tag:
        ax.text(x, y - h / 2 - 1.4, tag, ha="center", va="top",
                fontsize=6.0, color=MUTED, zorder=5)


def _register(ax, kind, x, y, w, h, label, txt=None, extra=None):
    """A shape may own more than one label — a use case oval carries its reference
    as well as its name — and every label it owns is checked to fit inside it."""
    store = getattr(ax, "_shapes", None)
    if store is None:
        store = ax._shapes = []
    store.append({"kind": kind, "x": x, "y": y, "w": w, "h": h,
                  "x0": x - w / 2, "y0": y - h / 2, "x1": x + w / 2, "y1": y + h / 2,
                  "label": label, "txt": txt, "extra": list(extra or [])})


def check_overlaps(ax, tol=0.15):
    """Peers of the same kind must not overlap. Frames are containers and exempt."""
    shapes = [s for s in getattr(ax, "_shapes", []) if s["kind"] != "frame"]
    bad = []
    for i in range(len(shapes)):
        a, b = shapes[i], None
        for j in range(i + 1, len(shapes)):
            b = shapes[j]
            if a["kind"] != b["kind"]:
                continue
            ox = min(a["x1"], b["x1"]) - max(a["x0"], b["x0"])
            oy = min(a["y1"], b["y1"]) - max(a["y0"], b["y0"])
            if ox > tol and oy > tol:
                bad.append(f"{a['kind']} {a['label'][:34]!r} overlaps "
                           f"{b['label'][:34]!r} by {ox:.1f}x{oy:.1f}")
    return bad


def fit_text(ax, x, y, text, box_w, box_h, *, fontsize, colour,
             weight="bold", max_lines=3, pad=0.4, linespacing=1.2):
    """Place a label wrapped so that it actually fits the shape it names.

    A wrap width in CHARACTERS is a guess about glyph widths, and the guess is
    wrong the moment the build runs on a machine with a different font. So try
    successively tighter wraps, measure each one, and keep the first that fits —
    the widest wrap that works, so the label stays as readable as the shape
    allows. Returns the Text artist, ready to hand to _register().
    """
    fig = ax.figure
    fig.canvas.draw()
    rend = fig.canvas.get_renderer()
    inv = ax.transData.inverted()
    words = len(text.split())
    best = None
    for width in range(max(len(text), 12), 9, -2):
        lines = textwrap.wrap(text, width)
        if len(lines) > max_lines:
            continue
        t = ax.text(x, y, "\n".join(lines), ha="center", va="center",
                    fontsize=fontsize, color=colour, fontweight=weight,
                    zorder=5, linespacing=linespacing)
        bb = inv.transform_bbox(t.get_window_extent(rend))
        if (bb.width <= box_w - 2 * pad) and (bb.height <= box_h - 2 * pad):
            return t
        best = t
        t.remove()
        best = None
    # nothing fits: place the tightest wrap and let the guard report it, rather
    # than silently drawing a label that overruns its box
    return ax.text(x, y, "\n".join(textwrap.wrap(text, 12)), ha="center",
                   va="center", fontsize=fontsize, color=colour,
                   fontweight=weight, zorder=5, linespacing=linespacing)


def fit_top_text(ax, x, y, text, box_w, *, fontsize, colour, weight="bold",
                 max_lines=2, pad=1.2, linespacing=1.15):
    """A top-anchored title, wrapped so it fits the width it sits over."""
    fig = ax.figure
    fig.canvas.draw()
    rend = fig.canvas.get_renderer()
    inv = ax.transData.inverted()
    for width in range(max(len(text), 12), 9, -2):
        lines = textwrap.wrap(text, width)
        if len(lines) > max_lines:
            continue
        t = ax.text(x, y, "\n".join(lines), ha="center", va="top",
                    fontsize=fontsize, fontweight=weight, color=colour,
                    zorder=4, linespacing=linespacing)
        bb = inv.transform_bbox(t.get_window_extent(rend))
        if bb.width <= box_w - 2 * pad:
            return t
        t.remove()
    return ax.text(x, y, "\n".join(textwrap.wrap(text, 14)), ha="center",
                   va="top", fontsize=fontsize, fontweight=weight,
                   color=colour, zorder=4, linespacing=linespacing)


def _check_one(s, bb, bad, pad):
    if s["kind"] == "oval":
        worst = 0.0
        for cx in (bb.x0, bb.x1):
            for cy in (bb.y0, bb.y1):
                v = ((cx - s["x"]) / (s["w"] / 2)) ** 2 + ((cy - s["y"]) / (s["h"] / 2)) ** 2
                worst = max(worst, v)
        if worst > 1.0:
            bad.append(f"oval {s['label'][:34]!r}: text reaches "
                       f"{worst ** 0.5:.2f} of the ellipse radius")
    else:
        p = 0.2 if s["kind"] == "frame" else pad
        over = (max(0, s["x0"] + p - bb.x0) + max(0, bb.x1 - (s["x1"] - p))
                + max(0, s["y0"] + p - bb.y0) + max(0, bb.y1 - (s["y1"] - p)))
        if over > 0.05:
            bad.append(f"{s['kind']} {s['label'][:34]!r}: text overflows its shape "
                       f"by {over:.2f}")


def check_text_fits(fig, ax, pad=0.4):
    """A label must stay inside the shape it belongs to."""
    fig.canvas.draw()
    rend = fig.canvas.get_renderer()
    inv = ax.transData.inverted()
    bad = []
    for s in getattr(ax, "_shapes", []):
        for t in ([s["txt"]] if s.get("txt") is not None else []) + s.get("extra", []):
            bb = inv.transform_bbox(t.get_window_extent(rend))
            _check_one(s, bb, bad, pad)

    # free-standing text must not straddle any shape's border: fully inside a
    # container, or fully outside it, never across the line
    owned = set()
    for s in getattr(ax, "_shapes", []):
        if s.get("txt") is not None:
            owned.add(id(s["txt"]))
        for e in s.get("extra", []):
            owned.add(id(e))
    for t in ax.texts:
        if id(t) in owned or not t.get_text().strip():
            continue
        bb = inv.transform_bbox(t.get_window_extent(rend))
        for s in getattr(ax, "_shapes", []):
            ox = min(bb.x1, s["x1"]) - max(bb.x0, s["x0"])
            oy = min(bb.y1, s["y1"]) - max(bb.y0, s["y0"])
            if ox <= 0.2 or oy <= 0.2:
                continue                      # no meaningful intersection
            # a label must sit clear of the border, not on it
            CLEAR = 0.6
            inside = (bb.x0 >= s["x0"] + CLEAR and bb.x1 <= s["x1"] - CLEAR
                      and bb.y0 >= s["y0"] + CLEAR and bb.y1 <= s["y1"] - CLEAR)
            container = s["kind"] == "frame" or not s["label"].strip()
            if container and inside:
                continue                      # legitimately sits within a container
            label = t.get_text().replace("\n", " ")[:34]
            bad.append(f"text {label!r} crosses the border of "
                       f"{s['kind']} {s['label'][:28]!r}")
            break
    return bad


def box(ax, x, y, w, h, label, fc="#FFFFFF", ec=SYS_EDGE, fs=7.4, bold=False,
        pad=0.28, va="center", lw=1.1, wrap_at=30, ls="-"):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                                boxstyle=f"round,pad=0,rounding_size={pad}",
                                facecolor=fc, edgecolor=ec, lw=lw, linestyle=ls, zorder=3))
    ty = y if va == "center" else y + h / 2 - 1.2
    t = ax.text(x, ty, wrap(label, wrap_at), ha="center", va=va, fontsize=fs,
                color=INK, zorder=5, fontweight="bold" if bold else "normal",
                linespacing=1.25)
    _register(ax, "box", x, y, w, h, label.replace("\n", " "), t)


def system_frame(ax, x, y, w, h, title, fill=SYS_FILL):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                                boxstyle="round,pad=0,rounding_size=1.2",
                                facecolor=fill, edgecolor=SYS_EDGE, lw=1.5, zorder=1))
    t = ax.text(x, y + h / 2 - 2.6, title, ha="center", va="center",
                fontsize=8.6, color=SYS_EDGE, fontweight="bold", zorder=4)
    _register(ax, "frame", x, y, w, h, title, t)   # container; its title is checked below


def link(ax, x1, y1, x2, y2, colour="#9AA5B1", lw=0.85, style="-"):
    ax.plot([x1, x2], [y1, y2], color=colour, lw=lw, ls=style, zorder=2)
    store = getattr(ax, "_links", None)
    if store is None:
        store = ax._links = []
    store.append((x1, y1, x2, y2))


def _seg_hits_rect(p, q, r, pad=0.35):
    """Does the segment p→q pass through the rectangle r (x0,y0,x1,y1)?"""
    x0, y0, x1, y1 = r[0] - pad, r[1] - pad, r[2] + pad, r[3] + pad
    (px, py), (qx, qy) = p, q
    dx, dy = qx - px, qy - py
    t0, t1 = 0.0, 1.0
    for num, den in ((x0 - px, dx), (px - x1, -dx), (y0 - py, dy), (py - y1, -dy)):
        if den == 0:
            if num > 0:
                return False
            continue
        t = num / den
        if den > 0:
            if t > t1: return False
            t0 = max(t0, t)
        else:
            if t < t0: return False
            t1 = min(t1, t)
    return t0 <= t1


def check_lines_clear_of_text(fig, ax):
    """A connector must not be drawn through a label. This is the fault that kept
    coming back: it is invisible at page scale and obvious at full resolution."""
    links = getattr(ax, "_links", [])
    if not links:
        return []
    fig.canvas.draw()
    rend = fig.canvas.get_renderer()
    inv = ax.transData.inverted()
    owned = set()
    for s in getattr(ax, "_shapes", []):
        if s.get("txt") is not None:
            owned.add(id(s["txt"]))
        for e in s.get("extra", []):
            owned.add(id(e))
    bad = []
    for t in ax.texts:
        if id(t) in owned or not t.get_text().strip():
            continue
        bb = inv.transform_bbox(t.get_window_extent(rend))
        r = (bb.x0, bb.y0, bb.x1, bb.y1)
        for (x1, y1, x2, y2) in links:
            if _seg_hits_rect((x1, y1), (x2, y2), r):
                bad.append(f"a connector is drawn through the label "
                           f"{t.get_text().replace(chr(10), ' ')[:34]!r}")
                break
    return bad


def arrow(ax, p1, p2, colour=MUTED, lw=1.0, style="-|>", rad=0.0, ls="-"):
    ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle=style, mutation_scale=9,
                                 color=colour, lw=lw, linestyle=ls,
                                 connectionstyle=f"arc3,rad={rad}", zorder=2,
                                 shrinkA=2, shrinkB=2))


def caption(ax, text):
    ax.text(50, 1.2, text, ha="center", va="bottom", fontsize=6.6,
            color=MUTED, style="italic")


def save(fig, path, dpi=220):
    for ax in fig.axes:
        bad = (check_overlaps(ax) + check_text_fits(fig, ax)
               + check_lines_clear_of_text(fig, ax))
        if bad:
            raise AssertionError(f"{path}: geometry check failed\n  " + "\n  ".join(bad))
    fig.savefig(path, dpi=dpi, bbox_inches="tight", pad_inches=0.06,
                facecolor="white")
    plt.close(fig)
    return path
