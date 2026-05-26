#!/usr/bin/env python3
"""
Excalidraw Content Graphics Generator

Generates .excalidraw JSON files from structured content.
Output files can be dragged into excalidraw.com for native rendering
with hand-drawn Virgil font, hachure fills, and pastel palette.

Usage:
    python3 excalidraw_generator.py demo1       # "Why Your Feed Isn't Growing"
    python3 excalidraw_generator.py demo2       # "The Weekly Content Rhythm"
    python3 excalidraw_generator.py demo1 demo2 # Both

As a module:
    from excalidraw_generator import rect, text, arrow, labeled_box, save
"""

import json
import random
import string
import sys
import os

# ── Palette ────────────────────────────────────────────────────────

PALETTE = {
    "sky_blue":  "#a5d8ff",
    "mint":      "#b2f2bb",
    "lavender":  "#d0bfff",
    "pink":      "#ffc9c9",
    "yellow":    "#ffec99",
    "peach":     "#ffd8a8",
    "coral":     "#ffa8a8",
    "purple":    "#eebefa",
}

PALETTE_LIST = list(PALETTE.values())
STROKE = "#1e1e1e"
GRAY = "#868e96"
TRANSPARENT = "transparent"

# ── Defaults ───────────────────────────────────────────────────────

FONT_VIRGIL = 1
ROUGHNESS = 1
FILL_HACHURE = "hachure"
STROKE_WIDTH = 2
LINE_HEIGHT = 1.25
CHAR_WIDTH = 0.55

# ── Internal state ─────────────────────────────────────────────────

_idx = 0


def _reset():
    global _idx
    _idx = 0


def _id():
    return "".join(random.choices(string.ascii_letters + string.digits, k=21))


def _seed():
    return random.randint(1, 2**31 - 1)


def _index():
    global _idx
    val = f"a{_idx}"
    _idx += 1
    return val


# ── Text helpers ───────────────────────────────────────────────────

def strip_em(t):
    return t.replace("—", " - ").replace("–", "-")


def tw(t, size):
    """Estimate rendered text width for Virgil font."""
    lines = t.split("\n")
    longest = max(lines, key=len)
    return len(longest) * size * CHAR_WIDTH


def th(t, size):
    """Estimate rendered text height."""
    return t.count("\n") * size * LINE_HEIGHT + size * LINE_HEIGHT


def wrap(t, size, max_w):
    """Word-wrap text to fit within max_w pixels."""
    words = t.split()
    lines, cur = [], ""
    for w in words:
        test = f"{cur} {w}".strip()
        if len(test) * size * CHAR_WIDTH > max_w and cur:
            lines.append(cur)
            cur = w
        else:
            cur = test
    if cur:
        lines.append(cur)
    return "\n".join(lines)


# ── Element factories ─────────────────────────────────────────────

def _base(typ, x, y, w, h, **kw):
    return {
        "id": kw.pop("id", _id()),
        "type": typ,
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "angle": 0,
        "strokeColor": kw.pop("strokeColor", STROKE),
        "backgroundColor": kw.pop("backgroundColor", TRANSPARENT),
        "fillStyle": kw.pop("fillStyle", FILL_HACHURE),
        "strokeWidth": kw.pop("strokeWidth", STROKE_WIDTH),
        "strokeStyle": kw.pop("strokeStyle", "solid"),
        "roughness": kw.pop("roughness", ROUGHNESS),
        "opacity": kw.pop("opacity", 100),
        "groupIds": kw.pop("groupIds", []),
        "frameId": None,
        "index": _index(),
        "roundness": kw.pop("roundness", None),
        "seed": _seed(),
        "version": 1,
        "versionNonce": _seed(),
        "isDeleted": False,
        "boundElements": kw.pop("boundElements", None),
        "updated": 1700000000000,
        "link": None,
        "locked": False,
    }


def rect(x, y, w, h, bg=TRANSPARENT, **kw):
    return _base("rectangle", x, y, w, h,
                 backgroundColor=bg,
                 roundness={"type": 3},
                 **kw)


def text(x, y, content, size=20, align="center", valign="middle",
         container_id=None, w=None, h=None, **kw):
    content = strip_em(content)
    if w is None:
        w = tw(content, size)
    if h is None:
        h = th(content, size)
    el = _base("text", x, y, w, h,
               roundness=None,
               fillStyle="solid",
               strokeWidth=0,
               **kw)
    el.update({
        "text": content,
        "fontSize": size,
        "fontFamily": FONT_VIRGIL,
        "textAlign": align,
        "verticalAlign": valign,
        "containerId": container_id,
        "originalText": content,
        "autoResize": True,
        "lineHeight": LINE_HEIGHT,
    })
    return el


def arrow(x, y, points, start_bind=None, end_bind=None, **kw):
    dx = abs(points[-1][0] - points[0][0])
    dy = abs(points[-1][1] - points[0][1])
    el = _base("arrow", x, y, max(dx, 1), max(dy, 1),
               roundness={"type": 2},
               **kw)
    el.update({
        "points": points,
        "lastCommittedPoint": None,
        "startBinding": start_bind,
        "endBinding": end_bind,
        "startArrowhead": None,
        "endArrowhead": "arrow",
    })
    return el


def diamond(x, y, w, h, bg=TRANSPARENT, **kw):
    return _base("diamond", x, y, w, h,
                 backgroundColor=bg,
                 roundness={"type": 2},
                 **kw)


def ellipse(x, y, w, h, bg=TRANSPARENT, **kw):
    return _base("ellipse", x, y, w, h,
                 backgroundColor=bg,
                 roundness={"type": 2},
                 **kw)


def line_el(x, y, points, **kw):
    dx = abs(points[-1][0] - points[0][0])
    dy = abs(points[-1][1] - points[0][1])
    el = _base("line", x, y, max(dx, 1), max(dy, 1),
               roundness={"type": 2},
               **kw)
    el.update({
        "points": points,
        "lastCommittedPoint": None,
        "startBinding": None,
        "endBinding": None,
        "startArrowhead": None,
        "endArrowhead": None,
    })
    return el


# ── Composite helpers ──────────────────────────────────────────────

def labeled_box(x, y, w, h, bg, label, size=24, group_id=None):
    """Rectangle with bound centered text. Returns (elements, rect_id)."""
    rid = _id()
    tid = _id()
    gids = [group_id] if group_id else []

    wrapped = wrap(label, size, w - 20)
    t_w = w - 10
    t_h = th(wrapped, size)
    t_x = x + 5
    t_y = y + (h - t_h) / 2

    r = rect(x, y, w, h, bg=bg, id=rid,
             boundElements=[{"type": "text", "id": tid}],
             groupIds=gids)
    t = text(t_x, t_y, wrapped, size=size, container_id=rid,
             w=t_w, h=t_h, id=tid, groupIds=gids)
    return [r, t], rid


def standalone_text(cx, y, content, size=20, color=STROKE):
    """Centered standalone text at given center-x and y."""
    w = tw(content, size)
    return text(cx - w / 2, y, content, size=size, w=w, strokeColor=color)


def day_card(x, y, w, h, bg, day, icon, post_type, desc):
    """Card for the weekly grid: day name, icon, type, description."""
    els = []
    gid = _id()
    inner = w - 30

    els.append(rect(x, y, w, h, bg=bg, groupIds=[gid]))

    # Day name
    dw = tw(day, 28)
    els.append(text(x + (w - dw) / 2, y + 12, day, size=28,
                    w=dw, groupIds=[gid]))

    # Icon
    iw = tw(icon, 42)
    els.append(text(x + (w - iw) / 2, y + 50, icon, size=42,
                    w=iw, groupIds=[gid]))

    # Post type label
    pw = tw(post_type, 22)
    els.append(text(x + (w - pw) / 2, y + 105, post_type, size=22,
                    w=pw, groupIds=[gid]))

    # Description
    wd = wrap(desc, 14, inner)
    dw2 = min(tw(wd, 14), inner)
    els.append(text(x + (w - dw2) / 2, y + 140, wd, size=14,
                    w=dw2, strokeColor=GRAY, groupIds=[gid]))

    return els


def pillar_box(x, y, w, h, bg, icon, label, sublabel):
    """Tall pillar with icon at top, label, and sublabel."""
    els = []
    gid = _id()
    inner = w - 16

    els.append(rect(x, y, w, h, bg=bg, groupIds=[gid]))

    iw = tw(icon, 36)
    els.append(text(x + (w - iw) / 2, y + 20, icon, size=36,
                    w=iw, groupIds=[gid]))

    els.append(text(x + 8, y + 70, label, size=18,
                    w=inner, groupIds=[gid]))

    wsub = wrap(sublabel, 16, inner)
    els.append(text(x + 8, y + 100, wsub, size=16,
                    w=inner, strokeColor=GRAY, groupIds=[gid]))

    return els


def connect(elements, src_id, dst_id, src_face="bottom", dst_face="top"):
    """Arrow between two existing elements. Mutates their boundElements."""
    src = next(e for e in elements if e["id"] == src_id)
    dst = next(e for e in elements if e["id"] == dst_id)

    faces = {
        "top":    lambda e: (e["x"] + e["width"] / 2, e["y"]),
        "bottom": lambda e: (e["x"] + e["width"] / 2, e["y"] + e["height"]),
        "left":   lambda e: (e["x"], e["y"] + e["height"] / 2),
        "right":  lambda e: (e["x"] + e["width"], e["y"] + e["height"] / 2),
    }
    sx, sy = faces[src_face](src)
    ex, ey = faces[dst_face](dst)

    aid = _id()
    a = arrow(sx, sy, [[0, 0], [ex - sx, ey - sy]],
              start_bind={"elementId": src_id, "focus": 0, "gap": 5},
              end_bind={"elementId": dst_id, "focus": 0, "gap": 5},
              id=aid)

    for el in (src, dst):
        if el.get("boundElements") is None:
            el["boundElements"] = []
        el["boundElements"].append({"type": "arrow", "id": aid})

    return a


# ── File I/O ───────────────────────────────────────────────────────

def save(elements, path):
    """Save elements list as a .excalidraw JSON file."""
    doc = {
        "type": "excalidraw",
        "version": 2,
        "source": "https://excalidraw.com",
        "elements": elements,
        "appState": {
            "gridSize": None,
            "viewBackgroundColor": "#ffffff",
            "currentItemFontFamily": FONT_VIRGIL,
        },
        "files": {},
    }
    with open(path, "w") as f:
        json.dump(doc, f, indent=2)
    return path


# ── Demo 1: Why Your Feed Isn't Growing ────────────────────────────

def demo_feed_growth():
    _reset()
    els = []
    CX = 680

    # Title
    els.append(standalone_text(CX, 25, "Why Your Feed Isn't Growing", size=36))

    # ── Left side ──

    LX = 80
    lh_els, lh_id = labeled_box(LX, 100, 440, 55, PALETTE["pink"],
                                "The Same-Post Trap", size=26)
    els.extend(lh_els)

    # 7 repeated house boxes (4 + 3) to show monotony
    small_w, small_h = 55, 42
    gap = 10
    for i in range(4):
        bx = LX + 20 + i * (small_w + gap)
        els.append(rect(bx, 185, small_w, small_h, bg=PALETTE["pink"]))
        iw = tw("\U0001f3e0", 16)
        els.append(text(bx + (small_w - iw) / 2, 190, "\U0001f3e0",
                        size=16, w=iw))
    for i in range(3):
        bx = LX + 20 + i * (small_w + gap)
        els.append(rect(bx, 235, small_w, small_h, bg=PALETTE["pink"]))
        iw = tw("\U0001f3e0", 16)
        els.append(text(bx + (small_w - iw) / 2, 240, "\U0001f3e0",
                        size=16, w=iw))

    # Decline indicator
    diw = tw("\U0001f4c9", 42)
    els.append(text(LX + 330, 200, "\U0001f4c9", size=42, w=diw))

    # Warning boxes
    w1_els, w1_id = labeled_box(LX, 310, 440, 55, PALETTE["peach"],
                                "Engagement Flatlines", size=22)
    els.extend(w1_els)
    w2_els, w2_id = labeled_box(LX, 385, 440, 55, PALETTE["peach"],
                                "They Scroll Past You", size=22)
    els.extend(w2_els)

    # Arrow from small boxes area to warning
    els.append(arrow(LX + 220, 277, [[0, 0], [0, 33]]))

    # ── VS circle ──

    vs_x, vs_y, vs_d = 560, 225, 85
    els.append(ellipse(vs_x, vs_y, vs_d, vs_d, bg=PALETTE["lavender"]))
    vw = tw("VS", 28)
    els.append(text(vs_x + (vs_d - vw) / 2, vs_y + 22, "VS", size=28, w=vw))

    # ── Right side ──

    RX = 720
    rh_els, rh_id = labeled_box(RX, 100, 440, 55, PALETTE["mint"],
                                "The 3-Pillar Mix", size=26)
    els.extend(rh_els)

    # Three pillars
    pw, ph, pgap = 140, 200, 10
    pillars = [
        (PALETTE["sky_blue"], "\U0001f3e0", "LISTINGS", "Sells Houses"),
        (PALETTE["peach"],    "\U0001f60a", "PERSONAL", "Gets You\nFollowed"),
        (PALETTE["yellow"],   "\U0001f4a1", "EDUCATIONAL", "Builds Trust"),
    ]
    for i, (bg, icon, label, sub) in enumerate(pillars):
        px = RX + 10 + i * (pw + pgap)
        els.extend(pillar_box(px, 180, pw, ph, bg, icon, label, sub))

    # Rise indicator (below pillars, not overlapping)
    riw = tw("\U0001f4c8", 36)
    els.append(text(RX + 360, 395, "\U0001f4c8", size=36, w=riw))

    # Result box
    rb_els, rb_id = labeled_box(RX, 430, 440, 55, PALETTE["mint"],
                                "People Hire Agents They Know", size=22)
    els.extend(rb_els)

    # Footer
    els.append(standalone_text(CX, 530,
               "Mix the post types. Win the algorithm.", size=18, color=GRAY))

    return els


# ── Demo 2: The Weekly Content Rhythm ──────────────────────────────

def demo_weekly_rhythm():
    _reset()
    els = []
    CX = 590

    # Title + subtitle
    els.append(standalone_text(CX, 25, "The Weekly Content Rhythm", size=36))
    els.append(standalone_text(CX, 72,
               "7 days. 7 post types. Zero repetition.", size=18, color=GRAY))

    # Card grid
    CW, CH = 245, 195
    GAP = 25

    top_x0 = 65
    top_y = 115
    days_top = [
        ("MON", "\U0001f4ca", "Market Stat",       "Median price hit $X",     PALETTE["sky_blue"]),
        ("TUE", "\U0001f3e0", "Listing Spotlight",  "Feature one active",      PALETTE["peach"]),
        ("WED", "\U0001f4f1", "Behind the Scenes",  "15-sec showing clip",     PALETTE["yellow"]),
        ("THU", "\U0001f4a1", "Buyer/Seller Tip",   "Gets saved and shared",   PALETTE["mint"]),
    ]
    for i, (day, icon, ptype, desc, bg) in enumerate(days_top):
        cx = top_x0 + i * (CW + GAP)
        els.extend(day_card(cx, top_y, CW, CH, bg, day, icon, ptype, desc))

    bot_y = top_y + CH + GAP
    bot_total = 3 * CW + 2 * GAP
    top_total = 4 * CW + 3 * GAP
    bot_x0 = top_x0 + (top_total - bot_total) / 2

    days_bot = [
        ("FRI", "\U0001f4cd", "Community Spotlight", "Local spot or event",    PALETTE["lavender"]),
        ("SAT", "\U0001f3e1", "Open House / Recap",  "Promote or recap",       PALETTE["coral"]),
        ("SUN", "❤️",  "Personal Post",       "The human behind it",    PALETTE["pink"]),
    ]
    for i, (day, icon, ptype, desc, bg) in enumerate(days_bot):
        cx = bot_x0 + i * (CW + GAP)
        els.extend(day_card(cx, bot_y, CW, CH, bg, day, icon, ptype, desc))

    # Repeat indicator
    loop_y = bot_y + CH + 25
    els.append(standalone_text(CX, loop_y,
               "↻  Repeat weekly", size=22))

    # Curved arrow from SUN back to MON
    sun_cx = bot_x0 + 2 * (CW + GAP) + CW / 2
    mon_cx = top_x0 + CW / 2
    arr_y = bot_y + CH + 10
    els.append(arrow(sun_cx, arr_y, [
        [0, 0],
        [30, 35],
        [-(sun_cx - mon_cx) / 2, 55],
        [-(sun_cx - mon_cx) + 10, 35],
        [-(sun_cx - mon_cx) - 30, -5],
    ], strokeColor=GRAY, strokeWidth=1))

    # Footer
    footer_y = loop_y + 45
    els.append(standalone_text(CX, footer_y,
               "One post a day. Never the same type twice in a row.",
               size=18, color=GRAY))

    return els


# ── CLI ────────────────────────────────────────────────────────────

DEMOS = {
    "demo1": ("feed-growth.excalidraw", demo_feed_growth,
              "Why Your Feed Isn't Growing"),
    "demo2": ("weekly-rhythm.excalidraw", demo_weekly_rhythm,
              "The Weekly Content Rhythm"),
}


def main():
    if len(sys.argv) < 2 or "--help" in sys.argv:
        print("Usage: python3 excalidraw_generator.py [demo1] [demo2]")
        print()
        for key, (fname, _, desc) in DEMOS.items():
            print(f"  {key}  ->  {fname}  ({desc})")
        sys.exit(0)

    for arg in sys.argv[1:]:
        if arg not in DEMOS:
            print(f"Unknown: {arg}. Options: {', '.join(DEMOS.keys())}")
            continue
        fname, builder, desc = DEMOS[arg]
        out = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
        elements = builder()
        save(elements, out)
        print(f"Saved {len(elements)} elements -> {out}")
        print(f"  Drag into excalidraw.com to view: \"{desc}\"")


if __name__ == "__main__":
    main()
