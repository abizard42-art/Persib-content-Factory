#!/usr/bin/env python3
"""Render a 9:16 Starting XI reveal clip with FFmpeg.

Input JSON format:
{
  "title": "PREDIKSI STARTING XI",
  "players": [
    {"number": 1, "name": "Nama Pemain", "position": "GK",
     "x": 0.08, "y": 0.50, "photo": "assets/players/player.jpg"}
  ]
}
Pitch coordinates x/y are normalized 0..1. Photo is optional and must be locally
available to the runner. If absent, a number tile is shown instead.
"""
import argparse
import json
import math
import os
import subprocess
import tempfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1080, 1920, 30
BG = (5, 10, 18)
WHITE = (245, 249, 255)
MUTED = (155, 176, 197)
BLUE = (8, 123, 210)
PANEL = (10, 20, 33)


def font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for p in candidates:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def rounded(draw, xy, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def crop_circle(path, size):
    if path and Path(path).is_file():
        im = Image.open(path).convert("RGB")
        side = min(im.size)
        left, top = (im.width-side)//2, (im.height-side)//2
        im = im.crop((left, top, left+side, top+side)).resize((size, size))
    else:
        im = Image.new("RGB", (size, size), (36, 91, 139))
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse((1, 1, size-2, size-2), fill=255)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(im, (0, 0), mask)
    return out


def draw_pitch(im, players, active):
    d = ImageDraw.Draw(im)
    x0, y0, x1, y1 = 64, 440, 470, 1165
    rounded(d, (x0, y0, x1, y1), 18, (13, 59, 48), (105, 166, 143), 3)
    d.rectangle((x0+2, y0+2, x1-2, y1-2), outline=(177, 222, 203), width=2)
    d.line((x0, (y0+y1)//2, x1, (y0+y1)//2), fill=(177, 222, 203), width=2)
    d.ellipse((x0+110, (y0+y1)//2-110, x0+296, (y0+y1)//2+110), outline=(177, 222, 203), width=2)
    d.rectangle((x0, y0+210, x0+95, y1-210), outline=(177, 222, 203), width=2)
    d.rectangle((x1-95, y0+210, x1, y1-210), outline=(177, 222, 203), width=2)
    for i, p in enumerate(players):
        px = x0 + int(float(p.get("x", .5)) * (x1-x0))
        py = y0 + int(float(p.get("y", .5)) * (y1-y0))
        r = 20
        if i == active:
            d.ellipse((px-r-10, py-r-10, px+r+10, py+r+10), outline=(80, 185, 255), width=7)
            d.ellipse((px-r, py-r, px+r, py+r), fill=WHITE, outline=BLUE, width=5)
        elif i < active:
            d.ellipse((px-r, py-r, px+r, py+r), fill=(28, 132, 208), outline=WHITE, width=3)
        else:
            d.ellipse((px-r, py-r, px+r, py+r), fill=(22, 47, 65), outline=(116, 143, 164), width=3)
    return im


def draw_card(d, p, idx, x, y, w, h, reveal, active):
    # reveal 0..1. Horizontal squeeze simulates a card flip.
    angle = abs(math.cos(max(0.0, min(1.0, reveal)) * math.pi))
    card_w = max(8, int(w * angle))
    cx = x + w//2
    left, right = cx-card_w//2, cx+card_w//2
    if reveal < .5:
        fill, edge = (17, 39, 59), (54, 82, 108)
    else:
        fill, edge = (13, 53, 88), BLUE
    rounded(d, (left, y, right, y+h), 10, fill, edge, 3 if active else 2)
    if reveal < .5 or card_w < 110:
        if card_w > 30:
            label = p.get("position", "POS")
            d.text((cx, y+h//2), label, font=font(18, True), fill=(144, 170, 194), anchor="mm")
        return
    photo_size = min(48, h-10)
    photo = crop_circle(p.get("photo"), photo_size)
    im_dummy = None
    # caller draws image on a frame layer; reserve photo slot as a stylized portrait tile
    d.ellipse((left+8, y+(h-photo_size)//2, left+8+photo_size, y+(h+photo_size)//2), fill=(184, 213, 235), outline=WHITE, width=2)
    num = str(p.get("number", idx+1)).zfill(2)
    d.text((left+photo_size+18, y+h//2), num, font=font(27, True), fill=WHITE, anchor="lm")
    name_x = left+photo_size+78
    max_name = max(40, right-name_x-8)
    name = str(p.get("name", "PEMAIN")).upper()
    while d.textbbox((0,0), name, font=font(18, True))[2] > max_name and len(name) > 5:
        name = name[:-1]
    d.text((name_x, y+13), name, font=font(18, True), fill=WHITE)
    d.text((name_x, y+39), str(p.get("position", "POS")), font=font(14), fill=(172, 205, 229))


def render_frame(players, title, revealed_count, current_idx, current_progress, frame_no):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    # subtle header
    d.rectangle((0, 0, W, 250), fill=(8, 14, 24))
    d.text((62, 58), "PERSIB CONTENT FACTORY", font=font(42, True), fill=WHITE)
    d.text((64, 119), "BOBOTOH EDITORIAL DESK", font=font(20, True), fill=MUTED)
    rounded(d, (700, 65, 1015, 145), 16, (13, 53, 88), BLUE, 2)
    d.text((857, 105), title.upper(), font=font(22, True), fill=WHITE, anchor="mm")
    d.rectangle((0, 242, W, 250), fill=BLUE)
    # visual panel
    rounded(d, (48, 285, 1032, 1215), 26, PANEL, (39, 66, 91), 3)
    d.text((82, 325), "STARTING XI REVEAL", font=font(23, True), fill=(103, 190, 255))
    d.text((82, 370), "11 PEMAIN • SATU PER SATU", font=font(34, True), fill=WHITE)
    draw_pitch(im, players, current_idx if current_idx >= 0 else -1)
    d = ImageDraw.Draw(im)
    # player cards to right, one compact row per player
    card_x, card_y, card_w, card_h, gap = 500, 440, 490, 59, 6
    for i, p in enumerate(players):
        y = card_y + i*(card_h+gap)
        if y+card_h > 1165:
            break
        if i < revealed_count:
            progress = 1.0
        elif i == current_idx:
            progress = current_progress
        else:
            progress = 0.0
        draw_card(d, p, i, card_x, y, card_w, card_h, progress, i == current_idx)
    # host placeholder
    rounded(d, (48, 1250, 1032, 1850), 26, (9, 17, 29), (39, 66, 91), 3)
    d.text((82, 1295), "BOBOTOH CASUALS HOST", font=font(23, True), fill=(103, 190, 255))
    # silhouette placeholder, intentionally not final chibi artwork
    d.ellipse((430, 1370, 650, 1590), fill=(201, 143, 104), outline=(119, 79, 58), width=5)
    d.arc((405, 1345, 675, 1535), 180, 355, fill=(22, 24, 30), width=42)
    rounded(d, (355, 1570, 725, 1795), 70, (18, 42, 65), (66, 112, 146), 5)
    rounded(d, (660, 1600, 730, 1670), 34, (10, 49, 87), (95, 185, 245), 3)
    d.text((695, 1635), "FCC", font=font(18, True), fill=WHITE, anchor="mm")
    d.text((540, 1810), "HOST PLACEHOLDER • MASTER CHIBI MENYUSUL", font=font(18, True), fill=MUTED, anchor="mm")
    d.text((540, 1888), "DEMO LINEUP — BUKAN SUSUNAN RESMI", font=font(17, True), fill=(122, 145, 166), anchor="mm")
    return im


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="visual/demo-lineup.json")
    ap.add_argument("--output", default="output/starting-xi-reveal.mp4")
    ap.add_argument("--fps", type=int, default=FPS)
    args = ap.parse_args()
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    players = data.get("players", [])
    if len(players) != 11:
        raise SystemExit("Input harus berisi tepat 11 pemain.")
    for p in players:
        if not p.get("name") or not p.get("position"):
            raise SystemExit("Setiap pemain wajib punya name dan position.")
    title = data.get("title", "PREDIKSI STARTING XI")
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="persib-xi-") as tmp:
        frames = Path(tmp)
        # staggered reveal: 0.52s per player, 0.48s flip, plus 1.5s final hold
        step = int(args.fps * 0.52)
        flip = max(2, int(args.fps * 0.48))
        total = step * 10 + flip + int(args.fps * 1.5)
        for f in range(total):
            idx = min(10, f // step)
            local = f - idx*step
            if f < step*11:
                progress = max(0.0, min(1.0, local / flip))
                revealed = idx
                active = idx
            else:
                progress, revealed, active = 1.0, 11, -1
            frame = render_frame(players, title, revealed, active, progress, f)
            frame.save(frames / f"frame_{f:05d}.png", optimize=False)
        cmd = [
            "ffmpeg", "-y", "-loglevel", "error", "-framerate", str(args.fps),
            "-i", str(frames / "frame_%05d.png"), "-c:v", "libx264",
            "-pix_fmt", "yuv420p", "-preset", "ultrafast", "-crf", "22",
            "-movflags", "+faststart", str(out)
        ]
        subprocess.run(cmd, check=True)
    print(f"Rendered: {out} ({total/args.fps:.1f}s, 1080x1920)")


if __name__ == "__main__":
    main()
