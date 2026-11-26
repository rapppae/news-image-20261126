#!/usr/bin/env python3
"""Render the 26 November 2026 world-news poster (1024x1024 PNG).

Drawn from scratch with Pillow: header, six story cards with simple
vector icons, and a bottom ticker of three more stories. No photos,
no network, no external assets — DejaVu fonts from the system.
Run:  python3 draw.py   (writes entry.png next to this file)
"""

import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
OUT = HERE / "entry.png"
SIZE = 1024

BG = (13, 22, 40)
CARD = (24, 38, 66)
CARD_EDGE = (58, 86, 130)
INK = (238, 242, 247)
MUTED = (168, 182, 199)
GOLD = (255, 209, 102)
RED = (230, 87, 87)

SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


F_TITLE = font(SERIF_B, 46)
F_SUB = font(SANS, 24)
F_TAG = font(SANS_B, 19)
F_HEAD = font(SANS_B, 27)
F_BODY = font(SANS, 20)
F_TICK = font(SANS_B, 19)
F_FOOT = font(SANS, 17)

STORIES = [
    ("TRADE WAR", (255, 209, 102),
     "US proposes tariffs on 14 partners",
     "Washington targets China, the EU, Japan and India after an "
     "8-month overcapacity probe — 25% on Indian goods."),
    ("GULF IN FLAMES", (230, 87, 87),
     "Houthis hit Saudi ports and refinery",
     "Yemen's Houthis claim strikes on Ras Tanura and Riyadh; "
     "oil prices climb as Gulf shipping fears grow."),
    ("CAIRO", (255, 159, 67),
     "Fuel tanker fire kills at least 31",
     "A tanker overturns and bursts into flames on Cairo's ring "
     "road; about 21 more people are hurt."),
    ("SPACE", (124, 196, 255),
     "First Pakistani astronaut reaches Tiangong",
     "Muhammad Zeeshan Ali boards China's space station aboard "
     "Shenzhou-24 — the first foreign guest there."),
    ("UKRAINE", (82, 183, 136),
     "Kyiv says 5 Russian jets hit at airbase",
     "Ukraine claims a strike on Savasleyka airfield damaged "
     "three MiG-31s and two Su-34 fighter-bombers."),
    ("ORBIT", (187, 134, 252),
     "FCC clears SpaceX's 1m-satellite plan",
     "US regulators authorise up to a million satellites to run "
     "orbital data centres for AI — scientists uneasy."),
]

TICKER = [
    "Macy's parade postponed",
    "Nasdaq nears bear market",
    "Liverpool win 3–0",
]


def wrap(draw, text, fnt, width):
    """Greedy word wrap to a pixel width."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def icon(draw, kind, cx, cy, color):
    """Small vector pictogram per story, drawn with primitives."""
    if kind == 0:  # tariff chart bars
        for i, h in enumerate((26, 40, 56)):
            x = cx - 30 + i * 24
            draw.rectangle([x, cy + 28 - h, x + 16, cy + 28], fill=color)
        draw.line([cx - 36, cy - 34, cx + 36, cy - 34], fill=color, width=4)
    elif kind == 1:  # flame: teardrop body with a hot gold core
        draw.ellipse([cx - 20, cy - 6, cx + 20, cy + 30], fill=color)
        draw.polygon([(cx, cy - 34), (cx + 16, cy + 2), (cx - 16, cy + 2)], fill=color)
        draw.ellipse([cx - 9, cy + 6, cx + 9, cy + 28], fill=GOLD)
    elif kind == 2:  # tanker truck
        draw.rectangle([cx - 34, cy - 14, cx + 6, cy + 10], fill=color)
        draw.rectangle([cx + 10, cy - 6, cx + 32, cy + 10], fill=color)
        draw.ellipse([cx - 26, cy + 8, cx - 12, cy + 22], fill=INK)
        draw.ellipse([cx + 14, cy + 8, cx + 28, cy + 22], fill=INK)
    elif kind == 3:  # rocket
        draw.polygon([(cx, cy - 36), (cx + 14, cy - 4), (cx + 8, cy + 22),
                      (cx - 8, cy + 22), (cx - 14, cy - 4)], fill=color)
        draw.polygon([(cx - 8, cy + 20), (cx, cy + 38), (cx + 8, cy + 20)], fill=GOLD)
        draw.ellipse([cx - 5, cy - 12, cx + 5, cy - 2], fill=BG)
    elif kind == 4:  # jet
        draw.polygon([(cx - 34, cy), (cx + 30, cy - 8), (cx + 36, cy),
                      (cx + 30, cy + 8)], fill=color)
        draw.polygon([(cx - 6, cy - 6), (cx - 18, cy - 24), (cx - 26, cy - 24),
                      (cx - 16, cy - 4)], fill=color)
        draw.polygon([(cx - 6, cy + 6), (cx - 18, cy + 24), (cx - 26, cy + 24),
                      (cx - 16, cy + 4)], fill=color)
    else:  # satellite
        draw.rectangle([cx - 8, cy - 8, cx + 8, cy + 8], fill=color)
        draw.rectangle([cx - 36, cy - 5, cx - 12, cy + 5], fill=color)
        draw.rectangle([cx + 12, cy - 5, cx + 36, cy + 5], fill=color)
        draw.line([cx, cy + 8, cx + 10, cy + 26], fill=color, width=3)
        draw.ellipse([cx + 4, cy + 22, cx + 16, cy + 34], fill=GOLD)


def main():
    img = Image.new("RGB", (SIZE, SIZE), BG)
    d = ImageDraw.Draw(img)

    # subtle vertical bands in the background
    for x in range(0, SIZE, 64):
        d.rectangle([x, 0, x + 32, SIZE], fill=(16, 27, 48))

    # header
    d.rectangle([0, 0, SIZE, 132], fill=(10, 17, 32))
    d.rectangle([0, 132, SIZE, 136], fill=GOLD)
    d.text((48, 18), "THE WORLD IN ONE IMAGE", font=F_TITLE, fill=INK)
    d.text((48, 84), "Thursday 26 November 2026  ·  Six stories that defined the day",
           font=F_SUB, fill=MUTED)
    d.text((SIZE - 48, 16), "26", font=font(SERIF_B, 64), fill=GOLD, anchor="ra")
    d.text((SIZE - 48, 92), "NOV 2026", font=F_TAG, fill=GOLD, anchor="ra")

    # six cards: 2 columns x 3 rows
    cw, ch, gap = 464, 232, 18
    x0, y0 = 28, 156
    for i, (tag, color, head, body) in enumerate(STORIES):
        x = x0 + (i % 2) * (cw + gap)
        y = y0 + (i // 2) * (ch + gap)
        d.rounded_rectangle([x, y, x + cw, y + ch], radius=14,
                            fill=CARD, outline=CARD_EDGE, width=2)
        d.rectangle([x, y, x + 6, y + ch], fill=color)
        icon(d, i, x + 62, y + 62, color)
        d.text((x + 108, y + 18), tag, font=F_TAG, fill=color)
        for ln, line in enumerate(wrap(d, head, F_HEAD, cw - 132)):
            d.text((x + 108, y + 46 + ln * 32), line, font=F_HEAD, fill=INK)
        n_head = len(wrap(d, head, F_HEAD, cw - 132))
        for ln, line in enumerate(wrap(d, body, F_BODY, cw - 48)):
            d.text((x + 24, y + 52 + n_head * 32 + ln * 26), line,
                   font=F_BODY, fill=MUTED)

    # ticker strip
    ty = y0 + 3 * ch + 2 * gap + 8
    d.rounded_rectangle([28, ty, SIZE - 28, ty + 60], radius=12,
                        fill=(10, 17, 32), outline=CARD_EDGE, width=2)
    d.text((48, ty + 18), "ALSO TODAY", font=F_TICK, fill=GOLD)
    d.text((200, ty + 18), "  •  ".join(TICKER), font=F_BODY, fill=INK)

    # footer
    d.text((48, SIZE - 30),
           "Sources: BBC, The Hindu, One Turn — 26 Nov 2026",
           font=F_FOOT, fill=MUTED)
    d.text((SIZE - 48, SIZE - 30), "make.fun · news-image-20261126",
           font=F_FOOT, fill=MUTED, anchor="ra")

    img.save(OUT, optimize=True)
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
