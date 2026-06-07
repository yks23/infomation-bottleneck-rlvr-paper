from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
W, H = 2400, 3600
M = 90
RESAMPLE = getattr(getattr(Image, "Resampling", Image), "LANCZOS")

REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"


def f(size, bold=False, mono=False):
    return ImageFont.truetype(MONO if mono else BOLD if bold else REG, size)


F = {
    "title": f(94, True),
    "subtitle": f(38),
    "h": f(48, True),
    "body": f(30),
    "bold": f(31, True),
    "small": f(22),
    "metric": f(52, True),
    "mono": f(25, mono=True),
}

C = {
    "bg": "#F7F8FA",
    "ink": "#111827",
    "muted": "#5B6573",
    "line": "#D6DCE5",
    "navy": "#0B1020",
    "blue": "#2563EB",
    "teal": "#0F766E",
    "red": "#BE123C",
    "orange": "#C2410C",
    "green": "#15803D",
    "white": "#FFFFFF",
}


def size(d, text, font):
    b = d.textbbox((0, 0), text, font=font)
    return b[2] - b[0], b[3] - b[1]


def wrap(d, text, font, width):
    lines, cur = [], ""
    for word in text.split():
        cand = word if not cur else cur + " " + word
        if size(d, cand, font)[0] <= width:
            cur = cand
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(d, xy, text, width, font, color=C["ink"], gap=8, max_lines=None):
    x, y = xy
    lines = wrap(d, text, font, width)
    if max_lines:
        lines = lines[:max_lines]
    _, lh = size(d, "Ag", font)
    for line in lines:
        d.text((x, y), line, font=font, fill=color)
        y += lh + gap
    return y


def card(d, box, fill=C["white"], outline=C["line"], radius=28):
    x, y, w, h = box
    d.rounded_rectangle((x + 8, y + 10, x + w + 8, y + h + 10), radius=radius, fill="#D6DCE555")
    d.rounded_rectangle((x, y, x + w, y + h), radius=radius, fill=fill, outline=outline, width=2)


def metric(d, x, y, label, value, color):
    d.text((x, y), label.upper(), font=F["small"], fill=C["muted"])
    d.text((x, y + 30), value, font=F["metric"], fill=color)


def asset(path):
    return Image.open(ROOT / path).convert("RGB")


def fig(d, im, box, caption):
    x, y, w, h = box
    d.rounded_rectangle((x, y, x + w, y + h), radius=20, fill="#FFFFFF", outline=C["line"], width=2)
    inner = (x + 18, y + 18, w - 36, h - 72)
    s = min(inner[2] / im.width, inner[3] / im.height)
    nw, nh = int(im.width * s), int(im.height * s)
    im = im.resize((nw, nh), RESAMPLE)
    canvas.paste(im, (inner[0] + (inner[2] - nw) // 2, inner[1] + (inner[3] - nh) // 2))
    para(d, (x + 20, y + h - 52), caption, w - 40, F["small"], C["muted"], gap=2, max_lines=2)


def connect4_chart(d, box):
    x, y, w, h = box
    d.rounded_rectangle((x, y, x + w, y + h), radius=20, fill=C["white"], outline=C["line"], width=2)
    d.text((x + 22, y + 18), "Connect4 win rate", font=F["bold"], fill=C["ink"])
    data = [("self-play", .886, .625), ("fixed-rand", .778, .573), ("fixed-weak", .804, .458), ("shaping", .864, .750)]
    cx, cy, cw, ch = x + 70, y + 95, w - 120, h - 170
    d.line((cx, cy + ch, cx + cw, cy + ch), fill="#9AA6B2", width=3)
    d.line((cx, cy, cx, cy + ch), fill="#9AA6B2", width=3)
    gw = cw / len(data)
    for i, (name, random_win, weak_win) in enumerate(data):
        base = cx + i * gw + 26
        for j, (val, col) in enumerate([(random_win, C["teal"]), (weak_win, C["blue"])]):
            bh = int(ch * val)
            bx = int(base + j * 44)
            d.rounded_rectangle((bx, cy + ch - bh, bx + 34, cy + ch), radius=7, fill=col)
        d.text((int(base - 10), cy + ch + 14), name, font=F["small"], fill=C["muted"])
    d.rectangle((x + w - 240, y + 30, x + w - 218, y + 48), fill=C["teal"])
    d.text((x + w - 208, y + 26), "random", font=F["small"], fill=C["muted"])
    d.rectangle((x + w - 125, y + 30, x + w - 103, y + 48), fill=C["blue"])
    d.text((x + w - 94, y + 26), "weak", font=F["small"], fill=C["muted"])
    para(d, (x + 20, y + h - 52), "Self-play keeps a renewable frontier.", w - 40, F["small"], C["muted"], gap=2, max_lines=2)


canvas = Image.new("RGB", (W, H), C["bg"])
d = ImageDraw.Draw(canvas)

# Header
d.rounded_rectangle((M, 70, W - M, 470), radius=44, fill=C["navy"])
d.text((M + 55, 118), "Verifiable RL Has an Information Budget", font=F["title"], fill=C["white"])
para(
    d,
    (M + 60, 245),
    "AlphaZero renews its 50/50 frontier. Fixed LLM math datasets run out of useful middle-band signal. RL then sharpens a broad rollout distribution into problem seeds.",
    W - 2 * M - 120,
    F["subtitle"],
    "#E5E7EB",
    gap=12,
)

# Thesis strip
strip = (M, 520, W - 2 * M, 260)
card(d, strip, "#FFFFFF")
x, y, w, h = strip
d.text((x + 40, y + 34), "One-line thesis", font=F["h"], fill=C["ink"])
para(
    d,
    (x + 40, y + 100),
    "The unit is a rollout/path information integral. AlphaZero can keep adding information through self-play; fixed-prompt LLM RLVR mostly spends a finite verifier source; transfer geometry tells us which prompt seeds interact.",
    w - 80,
    F["body"],
    C["ink"],
    gap=10,
)

# Three columns/cards
top = 840
col_w = (W - 2 * M - 50) // 2

left = (M, top, col_w, 980)
right = (M + col_w + 50, top, col_w, 980)
card(d, left)
card(d, right)

x, y, w, h = left
d.text((x + 34, y + 28), "1. Traditional RL: renewable information", font=F["h"], fill=C["teal"])
para(d, (x + 34, y + 92), "Self-play keeps the policy near opponents and positions at its current level. Outcomes stay near half win / half loss, so the cumulative information integral can grow with training time.", w - 68, F["body"], gap=9)
metric(d, x + 34, y + 250, "self-play vs random", "0.886", C["teal"])
metric(d, x + 400, y + 250, "self-play vs weak", "0.625", C["teal"])
metric(d, x + 750, y + 250, "shaped vs weak", "0.750", C["teal"])
connect4_chart(d, (x + 34, y + 410, w - 68, 500))

x, y, w, h = right
d.text((x + 34, y + 28), "2. LLM math: finite middle band", font=F["h"], fill=C["blue"])
para(d, (x + 34, y + 92), "Math prompts often become all-right or all-wrong. For each prompt, useful Bernoulli-verifier information is finite; over the dataset, interaction directions make the joint useful cap smaller than a naive sum.", w - 68, F["body"], gap=9)
metric(d, x + 34, y + 250, "used projection", "41.5%", C["blue"])
metric(d, x + 360, y + 250, "diag DeltaP", "0.0706", C["blue"])
metric(d, x + 680, y + 250, "offdiag / diag", "0.129", C["blue"])
fig(d, asset("poster/llm_rl/assets/figures/geometry40/bounded_information_budget.png"), (x + 34, y + 410, (w - 92) // 2, 500), "Bounded Bernoulli projection.")
fig(d, asset("poster/llm_rl/assets/figures/geometry40/diag_vs_offdiag_transfer_histogram.png"), (x + 58 + (w - 92) // 2, y + 410, (w - 92) // 2, 500), "Self-transfer dominates.")

# Middle wide card
mid = (M, 1880, W - 2 * M, 760)
card(d, mid)
x, y, w, h = mid
d.text((x + 34, y + 30), "3. RL sharpens: watermelon -> seeds -> geometry", font=F["h"], fill=C["red"])
para(d, (x + 34, y + 96), "After RL, a broad rollout distribution becomes lower-entropy problem-conditioned seeds. Train on source i, evaluate target j, and the transfer matrix becomes a map of dataset distance.", 860, F["body"], gap=9)
d.rounded_rectangle((x + 34, y + 285, x + 930, y + 505), radius=20, fill="#F8FAFC", outline=C["line"], width=2)
d.text((x + 60, y + 315), "P_i = sum_t H_b(p_i(t))", font=F["mono"], fill=C["ink"])
d.text((x + 60, y + 355), "G_i = sum_t H_b(p_i(t)) * Delta p_i^+(t)", font=F["mono"], fill=C["ink"])
d.text((x + 60, y + 395), "T_i = [DeltaP_i1, ..., DeltaP_iN]", font=F["mono"], fill=C["ink"])
d.text((x + 60, y + 435), "d(i,j) = 1 - cos(T_i, T_j)", font=F["mono"], fill=C["ink"])
fig(d, asset("poster/llm_rl/assets/figures/geometry40/cluster_heatmap.png"), (x + 1030, y + 95, 520, 560), "Directed transfer matrix.")
fig(d, asset("poster/llm_rl/assets/figures/geometry40/seed_geometry_sharpness_embedding.png"), (x + 1600, y + 95, 520, 560), "Prompt seed geometry.")

# Diffusion supporting card
bot = (M, 2700, W - 2 * M, 540)
card(d, bot)
x, y, w, h = bot
d.text((x + 34, y + 28), "Supporting contrast: diffusion reward channels", font=F["h"], fill=C["green"])
para(d, (x + 34, y + 92), "Diffusion RL is not binary math verification, but it shows the same principle: more reward signal only helps when it distinguishes rollouts and aligns with the target evaluator. In the 10-prompt SDXL DDPO run, IR+PS has the richest active feedback diagnostic, while held-out HPSv2 is controlled by alignment.", 1180, F["body"], gap=9)
metric(d, x + 34, y + 275, "IR+PS I_acc", "0.9335", C["green"])
metric(d, x + 360, y + 275, "PS HPSv2 z", "-0.0947", C["green"])
metric(d, x + 680, y + 275, "IR+PS HPSv2 z", "-0.0958", C["green"])
fig(d, asset("poster/diffusion_rl/figures/information_bottleneck/final_active_channel_information.png"), (x + 1290, y + 90, 440, 390), "Active feedback information.")
fig(d, asset("poster/diffusion_rl/figures/main/cross_reward_matrix_final_z.png"), (x + 1780, y + 90, 360, 390), "Cross-reward alignment.")

# Footer
d.rounded_rectangle((M, 3290, W - M, 3520), radius=32, fill=C["navy"])
d.text((M + 36, 3330), "Poster takeaway", font=F["h"], fill=C["white"])
para(d, (M + 36, 3394), "To make LLM math RL more AlphaZero-like, do not only optimize harder. Renew the frontier, allocate rollouts to high-information prompts, enrich feedback, and use transfer geometry to avoid redundant data.", W - 2 * M - 72, F["body"], "#E5E7EB", gap=8)

canvas.save(OUT / "minimal_information_budget_poster.png", quality=95)
canvas.save(OUT / "minimal_information_budget_poster.pdf", "PDF", resolution=180)
print(OUT / "minimal_information_budget_poster.png")
print(OUT / "minimal_information_budget_poster.pdf")
