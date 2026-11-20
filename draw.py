#!/usr/bin/env python3
"""Draw the entry image for make.fun bounty news-image-20261120.

Deterministic newspaper-style infographic (1024x1024) summing up the
world news of Friday 20 November 2026. No network, no randomness,
no timestamps: the same run always writes the same bytes.

Run:  python3 draw.py            (writes entry.png next to this file)
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
HERE = os.path.dirname(os.path.abspath(__file__))

PAPER = (253, 252, 247)   # warm paper white
INK = (18, 18, 18)        # near-black text
RED = (178, 34, 34)       # accent red (masthead rules, labels)
GRAY = (96, 96, 96)       # secondary text
LIGHT = (238, 236, 229)   # "also today" strip background
RULE = (205, 202, 193)    # hairline gray

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def load(path, size):
    return ImageFont.truetype(path, size)


def wrap(text, fnt, max_w):
    """Greedy word wrap to a pixel width."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if fnt.getlength(trial) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def centred(d, y, text, fnt, fill):
    x = (W - d.textlength(text, font=fnt)) / 2
    d.text((x, y), text, font=fnt, fill=fill)
    return y + fnt.size


# ------------------------------------------------------------------ icons
def icon_flags(d, x, y, s, c):
    # Two crossed flag poles with waving flags (Europe / summit).
    d.line([x + s * 0.30, y + s * 0.10, x + s * 0.30, y + s * 0.95],
           fill=c, width=4)
    d.line([x + s * 0.70, y + s * 0.10, x + s * 0.70, y + s * 0.95],
           fill=c, width=4)
    d.polygon([(x + s * 0.30, y + s * 0.10), (x + s * 0.05, y + s * 0.22),
               (x + s * 0.30, y + s * 0.34)], fill=c)
    d.polygon([(x + s * 0.70, y + s * 0.10), (x + s * 0.95, y + s * 0.22),
               (x + s * 0.70, y + s * 0.34)], fill=c)


def icon_burst(d, x, y, s, c):
    cx, cy = x + s / 2, y + s / 2
    pts = []
    for i in range(16):
        r = s * 0.5 if i % 2 == 0 else s * 0.22
        a = math.pi * i / 8 - math.pi / 2
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    d.polygon(pts, fill=c)
    d.ellipse([cx - s * 0.10, cy - s * 0.10, cx + s * 0.10, cy + s * 0.10],
              fill=PAPER)


def icon_globe(d, x, y, s, c):
    d.ellipse([x, y, x + s, y + s], outline=c, width=4)
    d.ellipse([x + s * 0.28, y, x + s * 0.72, y + s], outline=c, width=3)
    d.line([x, y + s * 0.5, x + s, y + s * 0.5], fill=c, width=3)
    d.arc([x, y + s * 0.18, x + s, y + s * 0.82], 200, 340, fill=c, width=3)
    d.arc([x, y + s * 0.18, x + s, y + s * 0.82], 20, 160, fill=c, width=3)


def icon_chart(d, x, y, s, c):
    # Rising bar chart with an arrow (economy / inflation).
    base = y + s * 0.88
    d.line([x + s * 0.08, base, x + s * 0.95, base], fill=c, width=4)
    heights = (0.30, 0.48, 0.38, 0.66)
    for i, h in enumerate(heights):
        bx = x + s * (0.12 + i * 0.21)
        d.rectangle([bx, base - s * h, bx + s * 0.13, base], fill=c)
    d.line([x + s * 0.10, y + s * 0.30, x + s * 0.88, y + s * 0.06],
           fill=c, width=4)
    d.polygon([(x + s * 0.88, y + s * 0.06), (x + s * 0.72, y + s * 0.04),
               (x + s * 0.86, y + s * 0.20)], fill=c)


def icon_shield(d, x, y, s, c):
    # Shield outline with a check mark (police / security operation).
    d.polygon([(x + s * 0.10, y + s * 0.08), (x + s * 0.90, y + s * 0.08),
               (x + s * 0.90, y + s * 0.52), (x + s * 0.50, y + s * 0.95),
               (x + s * 0.10, y + s * 0.52)], outline=c, width=4)
    d.line([x + s * 0.32, y + s * 0.48, x + s * 0.46, y + s * 0.64],
           fill=c, width=5)
    d.line([x + s * 0.46, y + s * 0.64, x + s * 0.72, y + s * 0.30],
           fill=c, width=5)


def icon_ballot(d, x, y, s, c):
    # Ballot box with a slip going in (election).
    d.rectangle([x + s * 0.08, y + s * 0.42, x + s * 0.92, y + s * 0.92],
                outline=c, width=4)
    d.line([x + s * 0.38, y + s * 0.42, x + s * 0.62, y + s * 0.42],
           fill=c, width=4)
    d.polygon([(x + s * 0.30, y + s * 0.05), (x + s * 0.68, y + s * 0.05),
               (x + s * 0.60, y + s * 0.42), (x + s * 0.38, y + s * 0.42)],
              outline=c, width=3)
    d.line([x + s * 0.30, y + s * 0.66, x + s * 0.70, y + s * 0.66],
           fill=c, width=3)


# ---------------------------------------------------------------- content
STORIES = [
    ("EUROPE", icon_flags,
     "Britain and EU agree Brexit reset",
     "Food trade eased, 100,000 youth visas a year; divisions remain."),
    ("UKRAINE", icon_burst,
     "Russia strikes Kyiv overnight",
     "Ballistic missiles spark fires in several districts of the capital."),
    ("TRADE", icon_globe,
     "APEC publishes Shenzhen Outlook",
     "21 economies back open trade, data rules and AI safeguards."),
    ("ECONOMY", icon_chart,
     "Japan inflation cements rate-hike bets",
     "Core CPI up 2.2% in October; Bank of Japan seen hiking in December."),
    ("HAITI", icon_shield,
     "Haiti police kill 34 in gang raid",
     "Martissant corridor retaken in the first big push in five years."),
    ("AMERICAS", icon_ballot,
     "Bukele seeks a third term",
     "El Salvador's president registers for February vote critics call unchecked."),
]

ALSO_TODAY = (
    "Fiona, the internet-famous hippo, dies at 9 in Cincinnati after "
    "swallowing a visitor's hat.  "
    "White House fires its national cyber director after a wave of tech "
    "outages.  "
    "California warns of king tides and heavy rain over Nov 24-26."
)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    f_kicker = load(SANS_B, 20)
    f_title = load(SERIF_B, 66)
    f_sub = load(SERIF, 20)
    f_label = load(SANS_B, 15)
    f_head = load(SANS_B, 27)
    f_cap = load(SANS, 18)
    f_also = load(SANS, 18)
    f_also_b = load(SANS_B, 18)
    f_foot = load(SANS, 13)

    # ---- masthead
    y = 30
    y = centred(d, y, "THE WORLD IN ONE DAY", f_kicker, RED)
    y = centred(d, y + 6, "20 NOVEMBER 2026", f_title, INK)
    y = centred(d, y + 2, "Friday  \u2022  Six stories that defined the day",
                f_sub, GRAY)
    d.line([36, 182, W - 36, 182], fill=RED, width=4)
    d.line([36, 189, W - 36, 189], fill=RULE, width=1)

    # ---- story grid: 2 cols x 3 rows
    col_x = [36, 524]
    col_w = 464
    row_y = [206, 436, 666]
    row_h = 214
    for i, (label, icon, head, cap) in enumerate(STORIES):
        x = col_x[i % 2]
        y = row_y[i // 2]
        icon(d, x, y + 6, 62, RED)
        tx = x + 80
        tw = col_w - 80
        d.text((tx, y), label, font=f_label, fill=RED)
        hy = y + 24
        for line in wrap(head, f_head, tw)[:2]:
            d.text((tx, hy), line, font=f_head, fill=INK)
            hy += 33
        cy = hy + 4
        for line in wrap(cap, f_cap, tw)[:2]:
            d.text((tx, cy), line, font=f_cap, fill=GRAY)
            cy += 23
        if i // 2 < 2:
            d.line([x, y + row_h - 8, x + col_w, y + row_h - 8],
                   fill=RULE, width=1)

    # ---- also today strip
    sy = 896
    d.rectangle([36, sy, W - 36, sy + 74], fill=LIGHT)
    d.rectangle([36, sy, 44, sy + 74], fill=RED)
    label = "ALSO TODAY:  "
    lx = 58
    d.text((lx, sy + 10), label, font=f_also_b, fill=RED)
    lw = f_also_b.getlength(label)
    lines = wrap(ALSO_TODAY, f_also, W - 36 - lx - lw - 14)
    ty = sy + 10
    d.text((lx + lw, ty), lines[0], font=f_also, fill=INK)
    ty += 24
    for line in lines[1:]:
        d.text((lx, ty), line, font=f_also, fill=INK)
        ty += 24

    # ---- footer
    centred(d, 986,
            "Sources: Reuters  \u2022  The Times  \u2022  Kyiv Independent  "
            "\u2022  MLex  \u2022  Aju Press  \u2022  WSJ  \u2022  AP  "
            "\u2022  Inshorts",
            f_foot, GRAY)

    out = os.path.join(HERE, "entry.png")
    img.save(out, format="PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
