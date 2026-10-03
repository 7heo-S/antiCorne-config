#!/usr/bin/env python3
"""Generate the icons drawn on the nice!view status screens.

- widgets/status_icons.c/.h: layer, modifier and caps icons (left half only)
- widgets/tray_icons.c/.h: battery frame, charging bolt and Bluetooth icons (both halves)

Icons are drawn upright (as read on the keyboard) and emitted as LVGL
LV_IMG_CF_INDEXED_1BIT images whose palette follows the widget colors
(index 0 = LVGL_BACKGROUND, index 1 = LVGL_FOREGROUND), so they honor
CONFIG_NICE_VIEW_DISP_WIDGET_INVERTED like the rest of the status screen.

Layer icons are indexed by layer position in config/corne_choc_pro.keymap.

Requires Pillow and DejaVu Sans. Run from anywhere:
    python3 boards/shields/nice_view_disp/tools/gen_status_icons.py
"""
import pathlib

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

LAYER_W, LAYER_H = 68, 66  # must match widgets/status.c
MOD_W, MOD_H = 33, 21
BT_W, BT_H = 13, 11  # number or pill; a 4 px band below holds the paired mark
BT_MARK_H = 4
BT_PROFILES = 5

# layer icons, by layer index: (name, how to draw it); the drawing functions are below
LAYERS = [("optimot", lambda: key_grid("opti", cols=2, key=30, gap=3)),
          ("symbol", lambda: key_grid("<&\\>", cols=2, key=30, gap=3)),
          ("greek", lambda: key_grid("ωπτι", cols=2, key=30, gap=3)),
          ("navigation", lambda: compass_rose()),
          ("function", lambda: text_image(LAYER_W, LAYER_H, "⚙", 60, pad=4)),
          ("accent", lambda: key_grid("ōâṕï", cols=2, key=30, gap=3, fill_frac=0.76))]
# in home-row order (A I E U): Gui, Alt, Ctrl, Shift (glyphs are drawn below)
MODS = ["gui", "alt", "ctrl", "shift"]
SS = 8  # supersampling factor for the drawn glyphs


def text_image(w, h, text, max_size, pad=2):
    """Largest crisp rendering of `text` that fits in w x h, centered on its actual ink."""
    for size in range(max_size, 6, -1):
        font = ImageFont.truetype(FONT_BOLD, size)
        probe = Image.new("1", (4 * size * len(text), 3 * size), 0)
        d = ImageDraw.Draw(probe)
        d.fontmode = "1"
        d.text((size, size), text, font=font, fill=1)
        left, top, right, bottom = probe.getbbox()
        if right - left <= w - 2 * pad and bottom - top <= h - 2 * pad:
            break
    ink = probe.crop((left, top, right, bottom))
    im = Image.new("1", (w, h), 0)
    im.paste(ink, ((w - ink.width) // 2, (h - ink.height) // 2))
    return np.array(im, np.uint8)


def key_grid(labels, cols, key, gap, fill_frac=0.62):
    """Rounded outline keys in a grid (like the Optimot logo), one label per key.

    All labels share a font size and a baseline, and the union of their ink is
    centered in the keys, so accents and descenders line up across keys.
    """
    rows = -(-len(labels) // cols)
    for size in range(40, 5, -1):
        font = ImageFont.truetype(FONT_BOLD, size)
        boxes = [ImageDraw.Draw(Image.new("1", (1, 1))).textbbox((0, 0), c, font=font) for c in labels]
        top, bottom = min(b[1] for b in boxes), max(b[3] for b in boxes)
        if bottom - top <= key * fill_frac and max(b[2] - b[0] for b in boxes) <= key * fill_frac:
            break
    img = np.zeros((LAYER_H, LAYER_W), np.uint8)
    x0 = (LAYER_W - (cols * key + (cols - 1) * gap)) // 2
    y0 = (LAYER_H - (rows * key + (rows - 1) * gap)) // 2
    outline = supersampled(key, key, lambda d, s: d.rounded_rectangle(
        s(0, 0, key, key), radius=6 * SS, outline=255, width=int(1.6 * SS)))
    for k, (c, box) in enumerate(zip(labels, boxes)):
        label = Image.new("1", (key, key), 0)
        d = ImageDraw.Draw(label)
        d.fontmode = "1"
        d.text(((key - (box[2] - box[0])) / 2 - box[0], (key - (bottom - top)) / 2 - top), c,
               font=font, fill=1)
        x, y = x0 + (k % cols) * (key + gap), y0 + (k // cols) * (key + gap)
        img[y:y + key, x:x + key] |= outline | np.array(label, np.uint8)
    return img


def compass_rose():
    """Four long and four short points around a hollow centre."""
    def draw(d, s):
        cx, cy = LAYER_W / 2, LAYER_H / 2
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            d.polygon(s(cx + dx * 28, cy + dy * 28, cx - dy * 6, cy + dx * 6, cx + dy * 6, cy - dx * 6), fill=255)
        for dx, dy in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            d.polygon(s(cx + dx * 14, cy + dy * 14, cx + (dx - dy) * 4, cy + (dy + dx) * 4,
                        cx + (dx + dy) * 4, cy + (dy - dx) * 4), fill=255)
        d.ellipse(s(cx - 4, cy - 4, cx + 4, cy + 4), fill=0)
    return supersampled(LAYER_W, LAYER_H, draw, soften=0.4)


def supersampled(w, h, draw_fn, soften=0.0):
    """Draw at SS x resolution in pixel units, optionally round the corners, reduce to 1 bit."""
    big = Image.new("L", (w * SS, h * SS), 0)
    draw_fn(ImageDraw.Draw(big), lambda *xy: [v * SS for v in xy])
    if soften:
        big = big.filter(ImageFilter.GaussianBlur(soften * SS))
    small = big.resize((w, h), Image.BOX)
    return (np.array(small) > 127).astype(np.uint8)


def round_line(d, s, points, width):
    """Polyline with round caps and joints."""
    d.line(s(*sum(points, ())), fill=255, width=int(width * SS), joint="curve")
    for x, y in points:
        r = width / 2
        d.ellipse(s(x - r, y - r, x + r, y + r), fill=255)


def glyph_gui(d, s, cx, cy):
    for dx, dy in ((0, -5), (-5, 0), (5, 0), (0, 5)):
        d.ellipse(s(cx + dx - 2.2, cy + dy - 2.2, cx + dx + 2.2, cy + dy + 2.2), fill=255)


def glyph_alt(d, s, cx, cy):
    round_line(d, s, [(cx - 6, cy - 3.5), (cx - 2, cy - 3.5), (cx + 2, cy + 3.5), (cx + 6, cy + 3.5)], 2.2)
    round_line(d, s, [(cx + 1.5, cy - 3.5), (cx + 6, cy - 3.5)], 2.2)


def glyph_ctrl(d, s, cx, cy):
    round_line(d, s, [(cx - 6.5, cy + 3), (cx, cy - 3.5), (cx + 6.5, cy + 3)], 2.8)


def arrow(d, s, cx, top, half, head_h, stem_half, stem_bottom):
    d.polygon(s(cx, top, cx + half, top + head_h, cx + stem_half, top + head_h,
                cx + stem_half, stem_bottom, cx - stem_half, stem_bottom,
                cx - stem_half, top + head_h, cx - half, top + head_h), fill=255)


def glyph_shift(d, s, cx, cy):
    arrow(d, s, cx, cy - 7.5, 7.5, 7.5, 3.2, cy + 7)


def glyph_caps(d, s, cx, cy):
    arrow(d, s, cx, cy - 8, 6.5, 6.5, 2.6, cy + 2)
    d.rounded_rectangle(s(cx - 4, cy + 4.5, cx + 4, cy + 7.5), radius=1.2 * SS, fill=255)


GLYPHS = {"gui": (glyph_gui, 0), "alt": (glyph_alt, 0), "ctrl": (glyph_ctrl, 0),
          "shift": (glyph_shift, 0.9), "caps": (glyph_caps, 0.6)}


def tile(w, h, active, glyph=None, text=None, outlined=False):
    """Bare glyph when idle; rounded filled pill with the glyph knocked out when active.

    `outlined` draws a pill outline around the bare glyph instead (half-active state).
    """
    fn, soften = GLYPHS[glyph] if glyph else (None, 0)
    ink = np.zeros((h, w), np.uint8)
    if fn:
        ink |= supersampled(w, h, lambda d, s: fn(d, s, w / 2, h / 2), soften)
    elif text:
        ink |= text_image(w, h, text, 40, pad=2)
    radius = min(6, h / 2)
    if outlined:
        frame = supersampled(w, h, lambda d, s: d.rounded_rectangle(
            s(0.5, 0.5, w - 0.5, h - 0.5), radius=radius * SS, outline=255, width=int(1.4 * SS)))
        return ink | frame
    if not active:
        return ink
    pill = supersampled(w, h, lambda d, s: d.rounded_rectangle(s(0, 0, w, h), radius=radius * SS, fill=255))
    return pill & (1 - ink)


TRAY_W, TRAY_H = 22, 16  # connection icons, right-aligned at the top of each screen
BATTERY_W, BATTERY_H = 33, 16
BOLT_W, BOLT_H = 11, 18


def bt_rune(d, s, cx):
    round_line(d, s, [(cx - 3.5, 4.5), (cx + 3.5, 11), (cx, 14.5), (cx, 1.5), (cx + 3.5, 5), (cx - 3.5, 11.5)], 1.7)


def tray_bt(mark):
    def draw(d, s):
        bt_rune(d, s, 16)
        if mark == "x":
            round_line(d, s, [(3, 5), (8, 10)], 1.7)
            round_line(d, s, [(3, 10), (8, 5)], 1.7)
        elif mark == "dots":
            for x in (2.5, 6, 9.5):
                d.ellipse(s(x - 1.3, 11.2, x + 1.3, 13.8), fill=255)
    return supersampled(TRAY_W, TRAY_H, draw)


def battery_frame():
    def draw(d, s):
        d.rounded_rectangle(s(0, 2, 29, 14), radius=3.5 * SS, fill=255)
        d.rounded_rectangle(s(1.2, 3.2, 27.8, 12.8), radius=2.5 * SS, fill=0)
        d.rounded_rectangle(s(30, 5.5, 32.5, 10.5), radius=1.2 * SS, fill=255)
    return supersampled(BATTERY_W, BATTERY_H, draw)


def bolt_image():
    """2-bit: 0 transparent, 1 background outline, 2 foreground bolt."""
    bolt = supersampled(BOLT_W, BOLT_H, lambda d, s: d.polygon(
        s(7.5, 0.5, 1.5, 10, 5, 10, 3.5, 17.5, 9.5, 7.5, 6, 7.5, 8, 0.5), fill=255), soften=0.4)
    halo = bolt.copy()
    for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        halo |= np.roll(np.roll(bolt, dy, 0), dx, 1)
    return np.where(bolt == 1, 2, np.where(halo == 1, 1, 0)).astype(np.uint8)


def build_tray():
    return {
        "tray_icon_ble_connected": tray_bt(None),
        "tray_icon_ble_disconnected": tray_bt("x"),
        "tray_icon_ble_open": tray_bt("dots"),
        "battery_frame": battery_frame(),
    }


def build():
    icons = {}
    for name, draw in LAYERS:
        icons[f"layer_icon_{name}"] = draw()
    for name in MODS:
        icons[f"mod_icon_{name}_off"] = tile(MOD_W, MOD_H, False, glyph=name)
        icons[f"mod_icon_{name}_on"] = tile(MOD_W, MOD_H, True, glyph=name)
    # caps state is shown on the Shift tile
    icons["shift_icon_caps_word"] = tile(MOD_W, MOD_H, False, glyph="caps", outlined=True)
    icons["shift_icon_caps_lock"] = tile(MOD_W, MOD_H, True, glyph="caps")
    for i in range(BT_PROFILES):
        number = tile(BT_W, BT_H, False, text=str(i + 1))
        blank = np.zeros((BT_MARK_H, BT_W), np.uint8)
        mark = blank.copy()
        mark[2:4, 4:9] = 1  # short bar under paired profiles
        icons[f"bt_icon_{i + 1}_off"] = np.vstack([number, blank])
        icons[f"bt_icon_{i + 1}_paired"] = np.vstack([number, mark])
        icons[f"bt_icon_{i + 1}_on"] = np.vstack([tile(BT_W, BT_H, True, text=str(i + 1)), blank])
    return icons


def c_image(name, img, bpp=1, palette="PALETTE"):
    h, w = img.shape
    per_byte = 8 // bpp
    stride = (w + per_byte - 1) // per_byte
    data = bytearray(stride * h)
    for y in range(h):
        for x in range(w):
            shift = 8 - bpp * (x % per_byte + 1)
            data[y * stride + x // per_byte] |= int(img[y, x]) << shift
    rows = ",\n".join("    " + ", ".join(f"0x{b:02x}" for b in data[i:i + 16])
                      for i in range(0, len(data), 16))
    palette_size = 4 * 2 ** bpp
    return (f"static const uint8_t {name}_map[] = {{\n    {palette}\n{rows}\n}};\n\n"
            f"const lv_img_dsc_t {name} = {{\n"
            f"    .header.cf = LV_IMG_CF_INDEXED_{bpp}BIT,\n    .header.always_zero = 0,\n"
            f"    .header.reserved = 0,\n    .header.w = {w},\n    .header.h = {h},\n"
            f"    .data_size = {palette_size + len(data)},\n    .data = {name}_map,\n}};\n")


PALETTE_DEFS = """/* index 0 = LVGL_BACKGROUND, index 1 = LVGL_FOREGROUND (LVGL white shows as a dark pixel) */
#if CONFIG_NICE_VIEW_DISP_WIDGET_INVERTED
#define PALETTE 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff, 0xff,
#define PALETTE_2BIT 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, \\
                     0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00,
#else
#define PALETTE 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0xff,
#define PALETTE_2BIT 0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff, \\
                     0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00,
#endif
"""


def main():
    icons = build()
    body = "\n".join(c_image(n, img) for n, img in icons.items())
    layer_names = ", ".join(f"&layer_icon_{n}" for n, _ in LAYERS)
    bt_rows = ",\n".join(f"    {{&bt_icon_{i}_off, &bt_icon_{i}_paired, &bt_icon_{i}_on}}" for i in range(1, BT_PROFILES + 1))
    mod_rows = ",\n".join(f"    {{&mod_icon_{n}_off, &mod_icon_{n}_on}}" for n in MODS)
    src = f"""/* Generated by tools/gen_status_icons.py - do not edit. */

#include <lvgl.h>

#include "status_icons.h"

{PALETTE_DEFS}
{body}
const lv_img_dsc_t *const layer_icons[LAYER_ICONS_COUNT] = {{{layer_names}}};

const lv_img_dsc_t *const mod_icons[4][2] = {{
{mod_rows},
}};

const lv_img_dsc_t *const bt_icons[BT_ICONS_COUNT][3] = {{
{bt_rows},
}};
"""
    hdr = f"""/* Generated by tools/gen_status_icons.py - do not edit. */

#pragma once

#include <lvgl.h>

#define LAYER_ICON_W {LAYER_W}
#define LAYER_ICON_H {LAYER_H}
#define MOD_ICON_W {MOD_W}
#define MOD_ICON_H {MOD_H}
#define BT_ICON_W {BT_W}
#define BT_ICON_H {BT_H + BT_MARK_H}
#define LAYER_ICONS_COUNT {len(LAYERS)}
#define BT_ICONS_COUNT {BT_PROFILES}

/* Indexed by layer position in the keymap */
extern const lv_img_dsc_t *const layer_icons[LAYER_ICONS_COUNT];
/* [Gui, Alt, Ctrl, Shift][off, on] */
extern const lv_img_dsc_t *const mod_icons[4][2];
/* Shift tile while caps word (outlined pill) or caps lock (filled pill) is on */
extern const lv_img_dsc_t shift_icon_caps_word;
extern const lv_img_dsc_t shift_icon_caps_lock;
/* [profile][unpaired, paired, active] */
extern const lv_img_dsc_t *const bt_icons[BT_ICONS_COUNT][3];
"""
    widgets = pathlib.Path(__file__).resolve().parent.parent / "widgets"
    (widgets / "status_icons.c").write_text(src)
    (widgets / "status_icons.h").write_text(hdr)

    tray = build_tray()
    body = "\n".join(c_image(n, img) for n, img in tray.items())
    body += "\n" + c_image("bolt", bolt_image(), bpp=2, palette="PALETTE_2BIT")
    (widgets / "tray_icons.c").write_text(f"""/* Generated by tools/gen_status_icons.py - do not edit. */

#include <lvgl.h>

#include "tray_icons.h"

{PALETTE_DEFS}
{body}""")
    decls = "\n".join(f"extern const lv_img_dsc_t {n};" for n in [*tray, "bolt"])
    (widgets / "tray_icons.h").write_text(f"""/* Generated by tools/gen_status_icons.py - do not edit. */

#pragma once

#include <lvgl.h>

#define TRAY_ICON_W {TRAY_W}
#define TRAY_ICON_H {TRAY_H}

{decls}
""")
    print(f"wrote status_icons.c/.h and tray_icons.c/.h in {widgets}")
    return icons


if __name__ == "__main__":
    main()
