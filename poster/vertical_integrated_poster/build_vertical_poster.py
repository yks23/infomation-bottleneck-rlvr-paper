from __future__ import annotations

import math
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = Path(__file__).resolve().parent
PNG_OUT = OUT_DIR / "vertical_information_integral_poster.png"
PDF_OUT = OUT_DIR / "vertical_information_integral_poster.pdf"

W, H = 3000, 5000
M = 105
RESAMPLE_LANCZOS = getattr(getattr(Image, "Resampling", Image), "LANCZOS")

COLORS = {
    "bg": "#F5F7FB",
    "ink": "#111827",
    "muted": "#526070",
    "navy": "#111A2E",
    "white": "#FFFFFF",
    "line": "#D8DEE9",
    "teal": "#0F766E",
    "blue": "#2563EB",
    "green": "#16803C",
    "red": "#BE123C",
    "orange": "#C2410C",
    "yellow": "#FBBF24",
    "panel": "#FFFFFF",
    "panel2": "#F8FAFC",
    "pink": "#FCE7F3",
    "mint": "#DCFCE7",
    "sky": "#E0F2FE",
    "rose": "#FFE4E6",
}

FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
FONT_MONO_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"


def font(size: int, bold: bool = False, mono: bool = False) -> ImageFont.FreeTypeFont:
    path = FONT_MONO_BOLD if mono and bold else FONT_MONO if mono else FONT_BOLD if bold else FONT_REG
    return ImageFont.truetype(path, size)


F = {
    "title": font(118, True),
    "subtitle": font(44),
    "section": font(56, True),
    "subsection": font(34, True),
    "body": font(31),
    "body_bold": font(31, True),
    "small": font(25),
    "tiny": font(21),
    "metric": font(56, True),
    "label": font(24, True),
    "formula": font(28, mono=True),
    "formula_bold": font(30, bold=True, mono=True),
}


def xywh(box):
    x, y, w, h = box
    return (x, y, x + w, y + h)


def text_size(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont) -> tuple[int, int]:
    bbox = draw.textbbox((0, 0), text, font=fnt)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def wrap_text(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont, width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    cur = ""
    for word in words:
        candidate = word if not cur else cur + " " + word
        if text_size(draw, candidate, fnt)[0] <= width:
            cur = candidate
        else:
            if cur:
                lines.append(cur)
            if text_size(draw, word, fnt)[0] <= width:
                cur = word
            else:
                approx = max(6, int(width / max(text_size(draw, "M", fnt)[0], 1)))
                pieces = textwrap.wrap(word, width=approx)
                lines.extend(pieces[:-1])
                cur = pieces[-1]
    if cur:
        lines.append(cur)
    return lines


def draw_paragraph(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    width: int,
    fnt: ImageFont.ImageFont,
    fill: str = COLORS["ink"],
    line_gap: int = 9,
    max_lines: int | None = None,
) -> int:
    x, y = xy
    lines = wrap_text(draw, text, fnt, width)
    if max_lines is not None:
        lines = lines[:max_lines]
    _, line_h = text_size(draw, "Ag", fnt)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += line_h + line_gap
    return y


def card(draw: ImageDraw.ImageDraw, box, fill=COLORS["panel"], outline=COLORS["line"], radius=34, shadow=True):
    x, y, w, h = box
    if shadow:
        draw.rounded_rectangle((x + 10, y + 14, x + w + 10, y + h + 14), radius=radius, fill="#D8DEE933")
    draw.rounded_rectangle(xywh(box), radius=radius, fill=fill, outline=outline, width=2)


def metric_card(draw, box, label, value, color):
    x, y, w, h = box
    card(draw, box, fill="#FFFFFF", radius=24, shadow=False)
    draw.text((x + 26, y + 22), label.upper(), font=F["label"], fill=COLORS["muted"])
    draw.text((x + 26, y + 62), value, font=F["metric"], fill=color)


def arrow(draw, start, end, fill, width=8):
    draw.line((start, end), fill=fill, width=width)
    sx, sy = start
    ex, ey = end
    ang = math.atan2(ey - sy, ex - sx)
    head = 28
    pts = [
        (ex, ey),
        (ex - head * math.cos(ang - 0.45), ey - head * math.sin(ang - 0.45)),
        (ex - head * math.cos(ang + 0.45), ey - head * math.sin(ang + 0.45)),
    ]
    draw.polygon(pts, fill=fill)


def draw_formula_box(draw, box, title, lines, color):
    x, y, w, h = box
    card(draw, box, fill="#F8FAFC", radius=26, shadow=False)
    draw.text((x + 28, y + 22), title, font=F["subsection"], fill=color)
    yy = y + 78
    for line in lines:
        draw.text((x + 28, yy), line, font=F["formula"], fill=COLORS["ink"])
        yy += 42


def draw_fig(draw, img: Image.Image, box, caption: str):
    x, y, w, h = box
    card(draw, box, fill="#FFFFFF", radius=24, shadow=False)
    inner = (x + 20, y + 20, w - 40, h - 84)
    iw, ih = img.size
    scale = min(inner[2] / iw, inner[3] / ih)
    nw, nh = int(iw * scale), int(ih * scale)
    resized = img.resize((nw, nh), RESAMPLE_LANCZOS)
    px = x + 20 + (inner[2] - nw) // 2
    py = y + 20 + (inner[3] - nh) // 2
    canvas.paste(resized, (px, py))
    draw_paragraph(draw, (x + 22, y + h - 56), caption, w - 44, F["tiny"], fill=COLORS["muted"], line_gap=2, max_lines=2)


def draw_axis(draw, box, title, xlabel="", ylabel=""):
    x, y, w, h = box
    draw.rounded_rectangle(xywh(box), radius=20, fill="#FFFFFF", outline=COLORS["line"], width=2)
    draw.text((x + 24, y + 18), title, font=F["subsection"], fill=COLORS["ink"])
    px0, py0 = x + 70, y + h - 70
    px1, py1 = x + w - 35, y + 80
    draw.line((px0, py0, px1, py0), fill="#94A3B8", width=3)
    draw.line((px0, py0, px0, py1), fill="#94A3B8", width=3)
    if xlabel:
        draw.text((x + w // 2 - 35, y + h - 43), xlabel, font=F["tiny"], fill=COLORS["muted"])
    if ylabel:
        draw.text((x + 16, y + 84), ylabel, font=F["tiny"], fill=COLORS["muted"])
    return px0, py0, px1, py1


def plot_polyline(draw, pts, fill, width=6):
    if len(pts) > 1:
        draw.line(pts, fill=fill, width=width, joint="curve")


def draw_alphazero_chart(draw, box):
    px0, py0, px1, py1 = draw_axis(draw, box, "Renewable 50/50 frontier", "training time", "info")
    n = 42
    entropy_pts = []
    integral_pts = []
    for i in range(n):
        t = i / (n - 1)
        entropy = 0.87 + 0.08 * math.sin(4 * math.pi * t)
        integral = 0.05 + 0.9 * t
        x = px0 + (px1 - px0) * t
        entropy_pts.append((x, py0 - (py0 - py1) * entropy))
        integral_pts.append((x, py0 - (py0 - py1) * integral))
    plot_polyline(draw, entropy_pts, COLORS["teal"], 7)
    plot_polyline(draw, integral_pts, COLORS["orange"], 7)
    draw.text((px0 + 18, py1 + 24), "H(reward) ~ high", font=F["tiny"], fill=COLORS["teal"])
    draw.text((px0 + 300, py1 + 88), "integral grows with T", font=F["tiny"], fill=COLORS["orange"])
    draw.text((px0 + 26, py0 - 44), "p(win) stays near 1/2", font=F["tiny"], fill=COLORS["muted"])


def draw_connect4_bars(draw, box):
    x, y, w, h = box
    card(draw, box, fill="#FFFFFF", radius=20, shadow=False)
    draw.text((x + 24, y + 18), "Connect4 evidence", font=F["subsection"], fill=COLORS["ink"])
    data = [
        ("self-play", 0.886, 0.625),
        ("fixed-rand", 0.778, 0.573),
        ("fixed-weak", 0.804, 0.458),
        ("shaping", 0.864, 0.750),
    ]
    chart = (x + 70, y + 90, w - 110, h - 155)
    cx, cy, cw, ch = chart
    draw.line((cx, cy + ch, cx + cw, cy + ch), fill="#94A3B8", width=3)
    draw.line((cx, cy, cx, cy + ch), fill="#94A3B8", width=3)
    group_w = cw / len(data)
    maxv = 1.0
    for idx, (name, rwin, mwin) in enumerate(data):
        gx = cx + idx * group_w + 18
        bw = 38
        for j, (val, col) in enumerate([(rwin, COLORS["teal"]), (mwin, COLORS["blue"])]):
            bh = int(ch * val / maxv)
            bx = int(gx + j * (bw + 8))
            by = int(cy + ch - bh)
            draw.rounded_rectangle((bx, by, bx + bw, cy + ch), radius=8, fill=col)
        draw.text((int(gx - 4), cy + ch + 12), name, font=F["tiny"], fill=COLORS["muted"])
    draw.rounded_rectangle((x + w - 220, y + 24, x + w - 30, y + 84), radius=18, fill="#F8FAFC")
    draw.rectangle((x + w - 198, y + 44, x + w - 175, y + 62), fill=COLORS["teal"])
    draw.text((x + w - 166, y + 39), "random", font=F["tiny"], fill=COLORS["muted"])
    draw.rectangle((x + w - 93, y + 44, x + w - 70, y + 62), fill=COLORS["blue"])
    draw.text((x + w - 62, y + 39), "weak", font=F["tiny"], fill=COLORS["muted"])


def draw_llm_collapse_chart(draw, box):
    px0, py0, px1, py1 = draw_axis(draw, box, "Fixed math prompts collapse", "steps", "p")
    colors = [COLORS["blue"], COLORS["red"], COLORS["teal"], COLORS["orange"], COLORS["green"]]
    for k, col in enumerate(colors):
        pts = []
        direction = 1 if k % 2 == 0 else 0
        for i in range(44):
            t = i / 43
            if direction:
                p = 0.18 + 0.82 / (1 + math.exp(-9 * (t - 0.45 + 0.06 * k)))
            else:
                p = 0.82 - 0.78 / (1 + math.exp(-9 * (t - 0.42 + 0.04 * k)))
            x = px0 + (px1 - px0) * t
            y = py0 - (py0 - py1) * p
            pts.append((x, y))
        plot_polyline(draw, pts, col, 6)
    draw.line((px0, py0 - (py0 - py1) * 0.5, px1, py0 - (py0 - py1) * 0.5), fill="#CBD5E1", width=3)
    draw.text((px0 + 18, py0 - (py0 - py1) * 0.5 - 38), "effective band near p=1/2", font=F["tiny"], fill=COLORS["muted"])
    draw.text((px0 + 18, py1 + 18), "all-wrong", font=F["tiny"], fill=COLORS["red"])
    draw.text((px1 - 150, py1 + 18), "all-right", font=F["tiny"], fill=COLORS["green"])


def draw_watermelon_geometry(draw, box):
    x, y, w, h = box
    card(draw, box, fill="#FFFFFF", radius=24, shadow=False)
    draw.text((x + 24, y + 18), "RL sharpening: watermelon -> seeds", font=F["subsection"], fill=COLORS["ink"])
    cx, cy = x + 220, y + 230
    draw.ellipse((cx - 150, cy - 90, cx + 150, cy + 90), fill="#16A34A", outline="#0F766E", width=10)
    draw.ellipse((cx - 122, cy - 66, cx + 122, cy + 66), fill="#FB7185")
    for dx, dy in [(-70, -20), (-25, 32), (35, -28), (82, 25), (5, 2)]:
        draw.ellipse((cx + dx - 10, cy + dy - 16, cx + dx + 10, cy + dy + 16), fill="#111827")
    draw.text((cx - 155, cy + 118), "broad rollout distribution", font=F["tiny"], fill=COLORS["muted"])
    arrow(draw, (x + 430, cy), (x + 650, cy), COLORS["red"], 9)
    seed_centers = [
        (x + 750, y + 145),
        (x + 880, y + 220),
        (x + 730, y + 325),
        (x + 1010, y + 150),
        (x + 1050, y + 320),
        (x + 925, y + 395),
    ]
    for i, (sx, sy) in enumerate(seed_centers):
        draw.ellipse((sx - 26, sy - 40, sx + 26, sy + 40), fill="#111827")
        draw.ellipse((sx - 8, sy - 22, sx + 8, sy + 6), fill="#FFFFFF66")
        draw.text((sx - 20, sy + 50), f"s{i+1}", font=F["tiny"], fill=COLORS["muted"])
    for a, b, col in [(0, 1, COLORS["blue"]), (1, 3, COLORS["teal"]), (2, 5, COLORS["orange"]), (3, 4, COLORS["red"]), (1, 5, "#94A3B8")]:
        draw.line((seed_centers[a], seed_centers[b]), fill=col, width=4)
    draw_paragraph(
        draw,
        (x + 78, y + h - 150),
        "A source prompt is represented by its transfer fingerprint T_i = [DeltaP_i1, ..., DeltaP_iN]. Distances between fingerprints turn a fixed dataset into a geometry.",
        w - 150,
        F["small"],
        fill=COLORS["ink"],
        line_gap=7,
    )


def paste_asset(name: str) -> Image.Image:
    return Image.open(ROOT / name).convert("RGB")


canvas = Image.new("RGB", (W, H), COLORS["bg"])
draw = ImageDraw.Draw(canvas)

# Subtle background grid.
for gx in range(0, W, 120):
    draw.line((gx, 0, gx, H), fill="#EEF2F7", width=1)
for gy in range(0, H, 120):
    draw.line((0, gy, W, gy), fill="#EEF2F7", width=1)

# Header.
draw.rounded_rectangle((M, 70, W - M, 600), radius=46, fill=COLORS["navy"])
draw.text((M + 70, 130), "Why LLM Math RL Is Not AlphaZero", font=F["title"], fill=COLORS["white"])
draw_paragraph(
    draw,
    (M + 76, 275),
    "AlphaZero keeps sampling a renewable 50/50 frontier. Fixed LLM math datasets collapse into all-right or all-wrong prompts, so the useful information integral is finite.",
    W - 2 * M - 150,
    F["subtitle"],
    fill="#E5E7EB",
    line_gap=16,
    max_lines=2,
)
draw.rounded_rectangle((M + 72, 468, M + 720, 545), radius=28, fill="#1F2937")
draw.text((M + 108, 486), "rollout/path information integral", font=F["small"], fill="#FFFFFF")
draw.rounded_rectangle((M + 758, 468, M + 1265, 545), radius=28, fill="#064E3B")
draw.text((M + 792, 486), "finite LLM projection", font=F["small"], fill="#FFFFFF")
draw.rounded_rectangle((M + 1305, 468, M + 1930, 545), radius=28, fill="#7F1D1D")
draw.text((M + 1338, 486), "watermelon -> seeds", font=F["small"], fill="#FFFFFF")
draw.rounded_rectangle((M + 1972, 468, M + 2715, 545), radius=28, fill="#1E3A8A")
draw.text((M + 2008, 486), "transfer geometry of prompts", font=F["small"], fill="#FFFFFF")

# Core logic card.
logic = (M, 645, W - 2 * M, 390)
card(draw, logic, fill=COLORS["panel"], radius=36)
x, y, w, h = logic
draw.text((x + 46, y + 34), "Core logic", font=F["section"], fill=COLORS["ink"])
draw_formula_box(
    draw,
    (x + 50, y + 120, 820, 215),
    "AlphaZero-like self-play",
    [
        "p_t(win) ~= 1/2",
        "I_T = sum_t H_b(p_t) ~= T",
        "No fixed dataset cap as T grows",
    ],
    COLORS["teal"],
)
draw_formula_box(
    draw,
    (x + 985, y + 120, 820, 215),
    "Fixed LLM math RLVR",
    [
        "P_i = sum_t H_b(p_i(t))",
        "G_i = sum_t H_b(p_i(t)) Delta p_i^+",
        "0 <= G_i <= 1 bit per prompt",
    ],
    COLORS["blue"],
)
draw_formula_box(
    draw,
    (x + 1920, y + 120, 820, 215),
    "Dataset geometry",
    [
        "T_i = [DeltaP_i1, ..., DeltaP_iN]",
        "d(i,j) = 1 - cos(T_i, T_j)",
        "Joint useful mass <= sum of parts",
    ],
    COLORS["red"],
)

# Section 1.
s1 = (M, 1080, W - 2 * M, 1050)
card(draw, s1, fill=COLORS["panel"], radius=38)
x, y, w, h = s1
draw.text((x + 46, y + 32), "1. Traditional RL: the information integral can keep growing", font=F["section"], fill=COLORS["teal"])
draw_alphazero_chart(draw, (x + 50, y + 125, 835, 420))
draw_connect4_bars(draw, (x + 925, y + 125, 835, 420))
draw_paragraph(
    draw,
    (x + 1810, y + 135),
    "The important AlphaZero fact is not merely that the reward is terminal and binary. Self-play changes the rollout distribution itself. The current agent keeps meeting opponents and positions near its own ability, so roughly half the rollouts can remain positive and half negative.",
    880,
    F["body"],
    fill=COLORS["ink"],
    line_gap=12,
)
draw_paragraph(
    draw,
    (x + 1810, y + 405),
    "Therefore the accumulated information integral is controlled by continuing interaction and update budget, not by a fixed list of questions.",
    880,
    F["body_bold"],
    fill=COLORS["teal"],
    line_gap=12,
)
metric_card(draw, (x + 50, y + 605, 520, 150), "self-play vs random", "0.886", COLORS["teal"])
metric_card(draw, (x + 605, y + 605, 520, 150), "self-play vs weak", "0.625", COLORS["teal"])
metric_card(draw, (x + 1160, y + 605, 520, 150), "shaped vs weak", "0.750", COLORS["teal"])
draw_paragraph(
    draw,
    (x + 50, y + 810),
    "Poster takeaway: self-play renews the frontier. It can keep creating informative rollouts instead of depleting a finite source.",
    w - 100,
    F["body_bold"],
    fill=COLORS["ink"],
    line_gap=12,
)

# Section 2.
s2 = (M, 2185, W - 2 * M, 1325)
card(draw, s2, fill=COLORS["panel"], radius=38)
x, y, w, h = s2
draw.text((x + 46, y + 32), "2. LLM math RLVR: fixed questions have finite useful information", font=F["section"], fill=COLORS["blue"])
draw_llm_collapse_chart(draw, (x + 50, y + 125, 620, 430))
draw_fig(
    draw,
    paste_asset("poster/llm_rl/assets/figures/geometry40/p_small_multiples.png"),
    (x + 710, y + 125, 620, 430),
    "Per-prompt p_i(t) trajectories.",
)
draw_fig(
    draw,
    paste_asset("poster/llm_rl/assets/figures/geometry40/bounded_information_budget.png"),
    (x + 1370, y + 125, 620, 430),
    "Cumulative Bernoulli projection.",
)
draw_fig(
    draw,
    paste_asset("poster/llm_rl/assets/figures/geometry40/diag_vs_offdiag_transfer_histogram.png"),
    (x + 2030, y + 125, 620, 430),
    "Self transfer dominates off-diagonal.",
)
draw_formula_box(
    draw,
    (x + 50, y + 620, 820, 250),
    "Per-prompt finite score",
    [
        "H_b(p) = -p log2 p - (1-p) log2(1-p)",
        "G_i = sum_t H_b(p_i(t)) Delta p_i^+(t)",
        "0 <= G_i <= 1 bit",
    ],
    COLORS["blue"],
)
draw_paragraph(
    draw,
    (x + 930, y + 625),
    "A math prompt often leaves the useful middle band: the model either solves it reliably or fails it reliably. Once rollout rewards are all 1 or all 0, the binary verifier carries little local contrast. Over a fixed dataset, each question has its own cap, and the joint cap is usually smaller than the sum because update directions and transfer fingerprints are not perfectly aligned.",
    1690,
    F["body"],
    fill=COLORS["ink"],
    line_gap=12,
)
metric_card(draw, (x + 50, y + 955, 500, 145), "used projection", "41.5%", COLORS["blue"])
metric_card(draw, (x + 590, y + 955, 500, 145), "diag DeltaP", "0.0706", COLORS["blue"])
metric_card(draw, (x + 1130, y + 955, 500, 145), "offdiag DeltaP", "0.0091", COLORS["blue"])
metric_card(draw, (x + 1670, y + 955, 500, 145), "offdiag / diag", "0.129", COLORS["blue"])
metric_card(draw, (x + 2210, y + 955, 430, 145), "additivity", "0.871", COLORS["blue"])
draw_paragraph(
    draw,
    (x + 50, y + 1150),
    "This is the poster's bounded-information evidence: not h2(p) as the whole definition, but the finite Bernoulli projection of a rollout/path integral on a fixed verifier dataset.",
    w - 100,
    F["body_bold"],
    fill=COLORS["ink"],
    line_gap=12,
)

# Section 3.
s3 = (M, 3565, W - 2 * M, 1080)
card(draw, s3, fill=COLORS["panel"], radius=38)
x, y, w, h = s3
draw.text((x + 46, y + 32), "3. What RL actually does: shrink a distribution into problem seeds", font=F["section"], fill=COLORS["red"])
draw_watermelon_geometry(draw, (x + 50, y + 125, 1160, 560))
draw_fig(
    draw,
    paste_asset("poster/llm_rl/assets/figures/geometry40/cluster_heatmap.png"),
    (x + 1250, y + 125, 660, 560),
    "Directed transfer matrix.",
)
draw_fig(
    draw,
    paste_asset("poster/llm_rl/assets/figures/geometry40/seed_geometry_sharpness_embedding.png"),
    (x + 1950, y + 125, 690, 560),
    "Problem seeds embedded by transfer fingerprints.",
)
draw_formula_box(
    draw,
    (x + 50, y + 745, 820, 230),
    "Dataset distance",
    [
        "DeltaP_ij = p_j(after train i) - p_j(base)",
        "T_i = [DeltaP_i1, ..., DeltaP_iN]",
        "d(i,j) = 1 - cos(T_i, T_j)",
    ],
    COLORS["red"],
)
draw_paragraph(
    draw,
    (x + 930, y + 750),
    "The same bounded-integral story gives a practical tool. Train on source i, evaluate target j, and use the directed transfer matrix as a map of the dataset. Strong diagonal dominance means the dataset is close to additive; sparse off-diagonal edges reveal reusable skills, clusters, and possible curriculum shortcuts.",
    1700,
    F["body"],
    fill=COLORS["ink"],
    line_gap=12,
)

# Footer.
footer = (M, 4685, W - 2 * M, 230)
card(draw, footer, fill="#111827", outline="#111827", radius=34, shadow=False)
x, y, w, h = footer
draw.text((x + 42, y + 30), "Research program", font=F["subsection"], fill=COLORS["white"])
draw_paragraph(
    draw,
    (x + 42, y + 84),
    "Measure the rollout/path information integral, identify when fixed verifier datasets run out of useful middle-band signal, and use transfer geometry to allocate prompts, renew the frontier, and test whether LLM math RL can become less data-additive.",
    w - 84,
    F["body"],
    fill="#E5E7EB",
    line_gap=10,
)

canvas.save(PNG_OUT, quality=95)
canvas.save(PDF_OUT, "PDF", resolution=180.0)
print(PNG_OUT)
print(PDF_OUT)
