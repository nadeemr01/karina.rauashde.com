#!/usr/bin/env python3
"""Prepares the before/after gallery (Results page).

Reads the anonymised collages from ~/Downloads, finds each photo panel inside a collage
(white gutters), writes img/results/<id>.webp (no EXIF) and _src/results.json with the
panel boxes, which build.py uses to place the Before/After labels.
Needs Pillow + numpy:  <venv>/bin/python _src/prep_results.py
"""
import json
import os
import numpy as np
from PIL import Image, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
D = os.path.expanduser("~/Downloads")
BLUR = D + "/Photos eyes blurred/photo_2026-11-22 "
COMB = D + "/Before-after combined/Before-after "
B, A = "before", "after"

# id, source, category, title key, layout, labels for the panels in reading order
# layouts: 2c two columns · 2r two rows · 3c three columns · 1r2c one on top, two below
#          2c1r two on top, one below · 3r2c three rows of two
CASES = [
    ("lips-1", COMB + "1 - lips.jpeg", "lips", "lips", "2c", [B, A]),
    ("lips-2", BLUR + "20.05.21.jpeg", "lips", "lips", "3c", [B, A, A]),
    ("lips-3", COMB + "2 - lips.jpeg", "lips", "lips", "2c", [B, A]),
    ("lips-4", BLUR + "20.05.26.jpeg", "lips", "lips", "2c", [B, A]),
    ("lips-5", BLUR + "20.05.22.jpeg", "lips", "lips", "1r2c", [B, A, A]),
    ("lips-6", COMB + "5 - lips.jpeg", "lips", "lips", "2r", [B, A]),
    ("lips-7", COMB + "6 - lips.jpeg", "lips", "lips", "2c", [B, A]),
    ("botox-1", BLUR + "20.05.33.jpeg", "botox", "botox_upper", "3r2c", [B, A, B, A, B, A]),
    ("botox-2", BLUR + "20.05.34.jpeg", "botox", "gummy", "2c", [B, A]),
    ("vessels-1", BLUR + "20.05.32 (1).jpeg", "vessels", "vessels_face", "2c", [B, A]),
    ("vessels-2", BLUR + "20.05.32.jpeg", "vessels", "vessels_face", "2c", [B, A]),
    ("vessels-3", BLUR + "20.05.24.jpeg", "vessels", "vessels_cheek", "2r", [B, A]),
    ("vessels-4", BLUR + "20.05.31.jpeg", "vessels", "vessels_legs", "2c", [B, A]),
    ("vessels-5", BLUR + "20.05.29.jpeg", "vessels", "vessels_legs", "2c1r", [B, A, A]),
    ("vessels-6", BLUR + "20.05.25.jpeg", "vessels", "vessels_legs", "2c", [B, A]),
    ("vessels-7", BLUR + "20.05.30.jpeg", "vessels", "vessels_legs", "2c", [B, A]),
    ("skin-1", COMB + "3 - hair.jpeg", "skin", "hair", "2c", [B, A]),
    ("skin-2", COMB + "4 - skin lesion.jpeg", "skin", "lesion", "2c", [B, A]),
]
MAX = 1400  # longest side of the published image


def gutter(white, box, axis, frac_lo, frac_hi):
    """Whitest line across box (axis 0: vertical gutter -> x range, 1: horizontal -> y range)
    between frac_lo..frac_hi of its size. Returns (start, end); start == end when the photos touch."""
    x0, y0, x1, y1 = box
    sub = white[y0:y1, x0:x1]
    prof = sub.mean(axis=0) if axis == 0 else sub.mean(axis=1)
    n = len(prof)
    lo, hi = int(n * frac_lo), int(n * frac_hi)
    best = lo + int(np.argmax(prof[lo:hi]))
    if prof[best] < 0.9:
        mid = (lo + hi) // 2
        return (x0 if axis == 0 else y0) + mid, (x0 if axis == 0 else y0) + mid
    a = best
    while a > 0 and prof[a - 1] >= 0.9:
        a -= 1
    b = best
    while b < n - 1 and prof[b + 1] >= 0.9:
        b += 1
    off = x0 if axis == 0 else y0
    return off + a, off + b + 1


def trim(white, box):
    """Drop white margins around a panel."""
    x0, y0, x1, y1 = box
    sub = white[y0:y1, x0:x1]
    rows = sub.mean(axis=1) > 0.97
    cols = sub.mean(axis=0) > 0.97
    if rows.all() or cols.all():
        return box
    return (x0 + int(np.argmax(~cols)), y0 + int(np.argmax(~rows)),
            x1 - int(np.argmax(~cols[::-1])), y1 - int(np.argmax(~rows[::-1])))


def cols(white, box, n):
    x0, y0, x1, y1 = box
    edges = [x0]
    for i in range(1, n):
        a, b = gutter(white, box, 0, i / n - 0.12, i / n + 0.12)
        edges += [a, b]
    edges.append(x1)
    return [(edges[2 * i], y0, edges[2 * i + 1], y1) for i in range(n)]


def rows(white, box, n):
    x0, y0, x1, y1 = box
    edges = [y0]
    for i in range(1, n):
        a, b = gutter(white, box, 1, i / n - 0.2, i / n + 0.2)
        edges += [a, b]
    edges.append(y1)
    return [(x0, edges[2 * i], x1, edges[2 * i + 1]) for i in range(n)]


def panels_for(white, layout, size):
    full = trim(white, (0, 0, size[0], size[1]))
    if layout == "2c":
        ps = cols(white, full, 2)
    elif layout == "3c":
        ps = cols(white, full, 3)
    elif layout == "2r":
        ps = rows(white, full, 2)
    elif layout == "1r2c":
        top, bottom = rows(white, full, 2)
        ps = [top] + cols(white, bottom, 2)
    elif layout == "2c1r":
        top, bottom = rows(white, full, 2)
        ps = cols(white, top, 2) + [bottom]
    elif layout == "3r2c":
        ps = [p for r in rows(white, full, 3) for p in cols(white, r, 2)]
    else:
        raise ValueError(layout)
    return [trim(white, p) for p in ps]


def main():
    out_dir = os.path.join(ROOT, "img", "results")
    os.makedirs(out_dir, exist_ok=True)
    data = []
    for cid, src, cat, key, layout, labels in CASES:
        im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
        white = np.asarray(im).min(axis=2) > 232
        panels = panels_for(white, layout, im.size)
        assert len(panels) == len(labels), cid
        scale = min(1, MAX / max(im.size))
        out = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS) if scale < 1 else im
        out.save(os.path.join(out_dir, cid + ".webp"), "WEBP", quality=80, method=6)
        data.append(dict(
            id=cid, cat=cat, key=key, w=out.width, h=out.height,
            panels=[dict(label=l, x=round(p[0] / im.width * 100, 2), y=round(p[1] / im.height * 100, 2),
                         w=round((p[2] - p[0]) / im.width * 100, 2), h=round((p[3] - p[1]) / im.height * 100, 2))
                    for l, p in zip(labels, panels)],
        ))
        print(f"{cid:10} {out.width}x{out.height} {os.path.getsize(os.path.join(out_dir, cid + '.webp')) // 1024} KB "
              f"panels={[(round(p[0]), round(p[1]), round(p[2]), round(p[3])) for p in panels]}")
    with open(os.path.join(HERE, "results.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1)


if __name__ == "__main__":
    main()
