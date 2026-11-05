# -*- coding: utf-8 -*-
"""
Engineering figures for the PHACK presentation.

Every figure is created at the exact size (in slide points) of the box it is placed in,
and all axes are positioned in absolute points. Font sizes are therefore real on-slide
point sizes (>= 9 pt), and nothing is stretched when the picture is inserted.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.patheffects as pe
import numpy as np

plt.rcParams["font.sans-serif"] = ["Calibri", "Segoe UI", "Arial", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

NAVY = "#003366"
BLUE = "#006699"
MID = "#0088B8"
CYAN = "#00A8CC"
GREEN = "#1E824C"
RED = "#C0392B"
RED_L = "#D9534F"
ORANGE = "#E67E22"
GREY = "#5A646E"
DARK = "#191E24"
BG = "#F8FAFD"


# ----------------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------------
def new_fig(w, h):
    return plt.figure(figsize=(w / 72.0, h / 72.0), facecolor=BG)


def axp(fig, w, h, left, bottom, width, height):
    """Axes placed with absolute point coordinates measured from the bottom-left corner."""
    return fig.add_axes([left / w, bottom / h, width / w, height / h])


def overlay(fig, w, h):
    """Transparent full-figure axes in point coordinates (origin bottom-left)."""
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    ax.axis("off")
    return ax


def ftitle(fig, w, h, x, y_from_top, text, size=10.5, ha="center"):
    fig.text(x / w, 1 - y_from_top / h, text, ha=ha, va="center", fontsize=size, fontweight="bold", color=NAVY)


def style_axes(ax, grid_axis="x"):
    ax.set_facecolor("#FFFFFF")
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    for sp in ("left", "bottom"):
        ax.spines[sp].set_color("#8FA3B8")
    ax.tick_params(axis="both", labelsize=9, colors=DARK)
    ax.tick_params(axis="y", length=0)
    if grid_axis:
        ax.grid(axis=grid_axis, linestyle=":", color="#B8C6D6", alpha=0.9, zorder=0)
    ax.set_axisbelow(True)


def axis_label(ax, text, size=9.5):
    ax.set_xlabel(text, fontsize=size, fontweight="bold", color=NAVY, labelpad=3)


def hbar(ax, labels, values, colors, texts, xmax, fs=9.5, height=0.62, thr=0.55):
    """Horizontal bars (first label on top) with value labels inside long bars and outside short ones."""
    n = len(labels)
    y = np.arange(n)
    ax.barh(y, values, color=colors, height=height, edgecolor=NAVY, linewidth=0.8, zorder=3)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=fs, fontweight="bold", color=DARK)
    ax.set_ylim(n - 0.5, -0.5)
    ax.set_xlim(0, xmax)
    for yy, v, t in zip(y, values, texts):
        if v / float(xmax) > thr:
            ax.text(v - 0.012 * xmax, yy, t, ha="right", va="center", fontsize=fs, fontweight="bold",
                    color="white", zorder=5)
        else:
            ax.text(v + 0.015 * xmax, yy, t, ha="left", va="center", fontsize=fs, fontweight="bold",
                    color=DARK, zorder=5)
    style_axes(ax, "x")


def box(ax, x, y, w, h, color, edge="#FFFFFF", lw=1.2, rounding=5):
    p = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=%s" % rounding,
                               facecolor=color, edgecolor=edge, linewidth=lw)
    ax.add_patch(p)
    return p


def chevron(ax, x, y, w, h, notch, color, first=False):
    left_notch = 0 if first else notch
    pts = [(x, y), (x + w - notch, y), (x + w, y + h / 2.0), (x + w - notch, y + h), (x, y + h),
           (x + left_notch, y + h / 2.0)]
    ax.add_patch(patches.Polygon(pts, closed=True, facecolor=color, edgecolor="#FFFFFF", linewidth=1.4))


def comma(x, nd=1):
    return ("%.*f" % (nd, x)).replace(".", ",")


# ----------------------------------------------------------------------------
# slide 3 – consortium value chain + country funding donut      (670 x 130)
# ----------------------------------------------------------------------------
def make_fig_slide3_consortium():
    W, H = 670, 130
    fig = new_fig(W, H)
    ov = overlay(fig, W, H)
    ftitle(fig, W, H, 225, 10, "Teljes európai K+F+I értéklánc – 6 partner, 4 ország", 10.5)

    chain = [
        ("BIO", "IT", "Fermentáció", "50 PM · 550 k€", MID),
        ("BME", "HU", "Kompound", "144 PM · 1,05 M€", NAVY),
        ("MOL", "HU", "Síkfólia", "100 PM · 850 k€", "#004C99"),
        ("ALFA", "HU", "Formázás", "90 PM · 650 k€", GREEN),
        ("PCOFF", "AT", "Töltés", "40 PM · 350 k€", CYAN),
        ("RWTH", "DE", "Lebomlás+LCA", "96 PM · 750 k€", BLUE),
    ]
    x0, cw, step, cy, ch = 6, 76, 72, 56, 44
    for i, (abbr, cc, role, money, col) in enumerate(chain):
        x = x0 + i * step
        chevron(ov, x, cy, cw, ch, 11, col, first=(i == 0))
        ov.text(x + cw / 2.0 + (4 if i else 0), cy + ch / 2.0 + 6, abbr, ha="center", va="center", fontsize=10.5,
                fontweight="bold", color="white")
        ov.text(x + cw / 2.0 + (4 if i else 0), cy + ch / 2.0 - 8, cc, ha="center", va="center", fontsize=9,
                fontweight="bold", color="#D6EAF8")
        ov.text(x + cw / 2.0, cy - 11, role, ha="center", va="center", fontsize=9.5, fontweight="bold", color=NAVY)
        ov.text(x + cw / 2.0, cy - 26, money, ha="center", va="center", fontsize=9, color=DARK)

    ftitle(fig, W, H, 560, 10, "Forrásmegoszlás országonként (4,2 M€)", 10.5)
    axd = axp(fig, W, H, 452, 12, 96, 96)
    axd.pie([60.7, 17.9, 13.1, 8.3], colors=[GREEN, BLUE, MID, GREY], startangle=90, counterclock=False,
            wedgeprops=dict(width=0.38, edgecolor="white", linewidth=1.5))
    axd.text(0, 0.06, "61%", ha="center", va="center", fontsize=14, fontweight="bold", color=GREEN)
    axd.text(0, -0.28, "HU", ha="center", va="center", fontsize=9.5, fontweight="bold", color=NAVY)
    for k, (c, t) in enumerate([(GREEN, "HU  2,55 M€ (61%)"), (BLUE, "DE  0,75 M€ (18%)"),
                                (MID, "IT  0,55 M€ (13%)"), (GREY, "AT  0,35 M€ (8%)")]):
        yy = 86 - k * 20
        ov.add_patch(patches.Rectangle((556, yy - 5), 10, 10, facecolor=c, edgecolor="none"))
        ov.text(571, yy, t, ha="left", va="center", fontsize=9.5, fontweight="bold", color=DARK)
    return fig


# ----------------------------------------------------------------------------
# slide 4 – heat resistance + 5-layer barrier film cross-section  (670 x 172)
# ----------------------------------------------------------------------------
def make_fig_slide4_capsule_barrier():
    W, H = 670, 172
    fig = new_fig(W, H)
    ov = overlay(fig, W, H)

    ftitle(fig, W, H, 168, 11, "Hőállóság 90–95°C (93±2°C) / 15–19 bar alatt", 10.5)
    ax = axp(fig, W, H, 112, 32, 215, 92)
    hbar(ax, ["Sima PLA\n(Tg 55–65°C)", "PHACK PHA/PHBH", "Primer Al / PP"], [58, 115, 145], [RED_L, GREEN, GREY],
         ["58°C – megroggyan", "105–120°C – stabil", ">140°C"], 175)
    ax.axvspan(90, 98, color="#FADBD8", alpha=0.6, zorder=1)
    ax.axvline(95, color=RED, linestyle="--", linewidth=1.5, zorder=4)
    ax.text(95, 1.04, "Kávéfőzés: 90–95°C (max. 19 bar)", transform=ax.get_xaxis_transform(), ha="center",
            va="bottom", fontsize=9, fontweight="bold", color=RED)
    axis_label(ax, "Alakstabilitási határhőmérséklet (°C)")

    ftitle(fig, W, H, 507, 11, "5-rétegű koextrudált bio-barrier fólia · 380–400 µm", 10.5)
    layers = [
        (26, NAVY, "PHA/PHBH külső · 180 µm (teherviselő)"),
        (12, CYAN, "Bio-Tie tapadóréteg · 15 µm"),
        (18, GREEN, "NFC / PGA barrier · 20 µm (OTR < 0,05)"),
        (12, CYAN, "Bio-Tie tapadóréteg · 15 µm"),
        (24, BLUE, "PHA belső · 150 µm (UH-hegeszthető)"),
    ]
    gap, x, y = 2, 372, 142
    top = y
    for k, (hh, col, label) in enumerate(layers):
        y -= hh
        ov.add_patch(patches.Rectangle((x, y), 86, hh, facecolor=col, edgecolor="white", linewidth=1.2))
        ov.text(x + 43, y + hh / 2.0, str(k + 1), ha="center", va="center", fontsize=9.5, fontweight="bold",
                color="white")
        ov.plot([x + 86, x + 104], [y + hh / 2.0, y + hh / 2.0], color="#8FA3B8", linewidth=0.9)
        ov.text(x + 108, y + hh / 2.0, label, ha="left", va="center", fontsize=9.5, fontweight="bold", color=DARK)
        y -= gap
    bottom = y + gap
    ov.annotate("", xy=(362, top), xytext=(362, bottom),
                arrowprops=dict(arrowstyle="<->", color=NAVY, lw=1.1))
    ov.text(354, (top + bottom) / 2.0, "Σ 380–400 µm", rotation=90, ha="center", va="center", fontsize=9,
            fontweight="bold", color=NAVY)
    return fig


# ----------------------------------------------------------------------------
# slide 5 – TRL 3 -> 7 stage-gate staircase                      (670 x 244)
# ----------------------------------------------------------------------------
def make_fig_slide5_trl_roadmap():
    W, H = 670, 244
    fig = new_fig(W, H)
    ftitle(fig, W, H, 340, 12, "A PHACK 48 hónapos stage-gate technológiai érettségi pályája (TRL 3 → TRL 7)", 11.5)
    ax = axp(fig, W, H, 44, 46, 614, 158)
    stages = [
        ("M1\nLabor PoC", 3, GREY, "BME & Danimer\nalapkutatás"),
        ("M12–M24\nMS1 · MS2 kapu", 4, BLUE, "50 kg kompound\n1 000 db kapszula"),
        ("M25–M30\nFélüzemi fólia", 5, MID, "MOL 5-rétegű\n0,40 mm síkfólia"),
        ("M36\nMS3 ipari pilot", 6, NAVY,         "100 000 db kapszula\nlegyártva (D3.2)"),
                ("M48\nÜzemi validáció", 7, GREEN, "400 db/perc töltés\nEN 13432 (D4.1)"),
    ]
    x = np.arange(5)
    ys = [s[1] for s in stages]
    ax.bar(x, ys, width=0.62, color=[s[2] for s in stages], edgecolor=NAVY, linewidth=1.0, zorder=3)
    ax.plot(x, ys, color=CYAN, marker="D", markersize=7, linewidth=2.2, zorder=4)
    for xi, s in zip(x, stages):
        ax.text(xi, s[1] / 2.0, "TRL %d" % s[1], ha="center", va="center", fontsize=13, fontweight="bold",
                color="white", zorder=5)
        ax.text(xi, s[1] + 0.55, s[3], ha="center", va="bottom", fontsize=9.5, fontweight="bold", color=DARK,
                zorder=5, bbox=dict(boxstyle="round,pad=0.25", facecolor="#F2F7FC", edgecolor="#C3D5E8", lw=0.8))
    ax.set_ylim(0, 10.3)
    ax.set_xlim(-0.55, 4.55)
    ax.set_xticks(x)
    ax.set_xticklabels([s[0] for s in stages], fontsize=9.5, fontweight="bold", color=NAVY)
    ax.set_yticks([0, 2, 4, 6, 8])
    ax.set_ylabel("TRL szint", fontsize=9.5, fontweight="bold", color=NAVY)
    style_axes(ax, "y")
    ax.tick_params(axis="x", length=0)
    return fig


# ----------------------------------------------------------------------------
# slide 6 – EU waste fate + cradle-to-grave LCA                  (670 x 174)
# ----------------------------------------------------------------------------
def make_fig_slide6_waste_and_lca():
    W, H = 670, 174
    fig = new_fig(W, H)
    ftitle(fig, W, H, 160, 11, "Kapszulák sorsa (NL, WUR 2025) és a PHACK cél", 10.5)
    ax1 = axp(fig, W, H, 150, 34, 165, 96)
    hbar(ax1, ["PHACK cél\n(komposzt / biogáz)", "Visszagyűjtve\n(alumínium, NL)",
               "Nincs visszagyűjtés\n(égető / lerakó)"], [100, 25, 75], [GREEN, "#7F8C8D", RED_L],
         ["100% szerves körforgás", "~25%", "~75% hulladék"], 105, fs=9)
    axis_label(ax1, "Arány (%)")

    ftitle(fig, W, H, 520, 11, "LCA (WUR 2023): g CO₂e / kg kávé, kávé nélkül", 10.5)
    ax2 = axp(fig, W, H, 478, 34, 182, 96)
    hbar(ax2, ["Alumínium kapszula\n(40% újrahasznosított)", "Komposztálható\nkapszula (komposzt)",
               "PHACK cél\n(WP4 LCA)"], [779, 741, 584], [RED, ORANGE, GREEN],
         ["779 g", "741 g", "≤584 g · cél: −25%"], 900, fs=9, thr=0.7)
    axis_label(ax2, "g CO₂e / kg csomagolt kávé (kávé nélkül)")
    return fig


# ----------------------------------------------------------------------------
# slide 7 – biodegradation kinetics + environments                (670 x 170)
# ----------------------------------------------------------------------------
def make_fig_slide7_biodeg_comparison():
    W, H = 670, 170
    fig = new_fig(W, H)
    ftitle(fig, W, H, 175, 11, "Házi komposztálási kinetika (20–30°C, NF T51-800)", 10.5)
    ax1 = axp(fig, W, H, 44, 36, 262, 96)
    days = np.linspace(0, 360, 120)
    ax1.plot(days, 96 * (1 - np.exp(-days / 75.0)), color=GREEN, linewidth=2.6, label="PHACK PHA/PHBH")
    ax1.plot(days, 98 * (1 - np.exp(-days / 65.0)), color=BLUE, linestyle="--", linewidth=1.6,
             label="Cellulóz-referencia")
    ax1.plot(days, 8 * days / 360.0, color=RED, linewidth=2.2, label="Sima PLA (<10%)")
    ax1.axhline(90, color=GREEN, linestyle=":", linewidth=1.3)
    ax1.text(8, 87, "90% küszöb", ha="left", va="top", fontsize=9, fontweight="bold", color=GREEN)
    ax1.set_xlim(0, 360)
    ax1.set_ylim(0, 112)
    ax1.set_ylabel("Lebomlás (%)", fontsize=9.5, fontweight="bold", color=NAVY)
    axis_label(ax1, "Idő (nap) – NF T51-800")
    ax1.legend(loc="center right", bbox_to_anchor=(1.0, 0.45), fontsize=9, frameon=True, facecolor="white",
               edgecolor="#C3D5E8")
    style_axes(ax1, "y")

    ftitle(fig, W, H, 505, 11, "Lebomlási képesség 4 környezetben", 10.5)
    ax2 = axp(fig, W, H, 470, 36, 190, 96)
    envs = ["Tengervíz (20°C)", "Házi komposzt\n(20–30°C)", "Ipari komposzt\n(58°C)", "Biogázüzem\n(30–45 nap)"]
    pha = [92, 95, 98, 94]
    pla = [3, 8, 92, 12]
    y = np.arange(4)
    ax2.barh(y - 0.2, pha, height=0.36, color=GREEN, edgecolor=NAVY, linewidth=0.6, label="PHACK PHA", zorder=3)
    ax2.barh(y + 0.2, pla, height=0.36, color=RED_L, edgecolor=NAVY, linewidth=0.6, label="PLA", zorder=3)
    for yy, a, b in zip(y, pha, pla):
        ax2.text(a - 2, yy - 0.2, "%d%%" % a, ha="right", va="center", fontsize=8.5, fontweight="bold",
                 color="white", zorder=5)
        if b > 50:
            ax2.text(b - 2, yy + 0.2, "%d%%" % b, ha="right", va="center", fontsize=8.5, fontweight="bold",
                     color="white", zorder=5)
        else:
            ax2.text(b + 2, yy + 0.2, "%d%%" % b, ha="left", va="center", fontsize=8.5, fontweight="bold",
                     color=DARK, zorder=5)
    ax2.set_yticks(y)
    ax2.set_yticklabels(envs, fontsize=9, fontweight="bold", color=DARK)
    ax2.set_ylim(3.6, -0.6)
    ax2.set_xlim(0, 105)
    axis_label(ax2, "Biodegradáció (%)")
    ax2.legend(loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=2, fontsize=9, frameon=False,
               handlelength=1.2, columnspacing=1.2)
    style_axes(ax2, "x")
    return fig


# ----------------------------------------------------------------------------
# slide 8 – process chain                                         (670 x 100)
# ----------------------------------------------------------------------------
def make_fig_slide8_process_chain():
    W, H = 670, 100
    fig = new_fig(W, H)
    ov = overlay(fig, W, H)
    nodes = [
        ("1 Fermentáció", "Danimer (IT)", "UCO → PHBH", NAVY),
        ("2 Kompoundálás", "BME (HU)", "orotinsav-nukl.", "#005588"),
        ("3 Síkfólia", "MOL (HU)", "0,40 mm ±3%", BLUE),
        ("4 Termoformálás", "ALFA (HU)", "60–70°C · <3,5 s", MID),
        ("5 Töltés + UH", "PackCoffee (AT)", "400 db/perc", CYAN),
        ("6 Lebomlás, LCA", "RWTH (DE)", "EN 13432", GREEN),
    ]
    w, step, y, h = 116, 110.5, 10, 80
    for i, (t1, t2, t3, col) in enumerate(nodes):
        x = 3 + i * step
        chevron(ov, x, y, w, h, 15, col, first=(i == 0))
        cx = x + w / 2.0 + (5 if i else 0) - 3
        ov.text(cx, y + 56, t1, ha="center", va="center", fontsize=9.5, fontweight="bold", color="white")
        ov.text(cx, y + 40, t2, ha="center", va="center", fontsize=9.5, fontweight="bold", color="#D6EAF8")
        ov.text(cx, y + 24, t3, ha="center", va="center", fontsize=9, color="white")
    return fig


# ----------------------------------------------------------------------------
# slide 14 – WP PERT chart                                        (670 x 174)
# ----------------------------------------------------------------------------
def make_fig_slide14_pert():
    W, H = 670, 174
    fig = new_fig(W, H)
    ov = overlay(fig, W, H)
    ftitle(fig, W, H, 335, 9, "Munkacsomagok és feladatok kapcsolati hálója (PERT – T1.1–T5.3, MS1–MS3)", 10.2)
    wps = [
        ("WP1 · Specifikáció", "RWTH | M1–M12 | 68 PM → MS1", "#005588", [
            "T1.1 Gépi tűrések (±0,1 mm)",
            "T1.2 Nyers PHA/PHBH audit",
            "T1.3 EU 10/2011 & PPWR → D1.1",
        ]),
        ("WP2 · Kompoundálás", "BME | M6–M24 | 144 PM → MS2", NAVY, [
            "T2.1 Orotinsav/talkum nukl.",
            "T2.2 Kétcsigás extr. (170°C)",
            "T2.3 50 kg & 1k db → D2.1",
        ]),
        ("WP3 · Fólia & formázás", "MOL | M18–M36 | 136 PM → MS3", BLUE, [
            "T3.1 5-rétegű fólia (0,40 mm)",
            "T3.2 Temperált szersz. (65°C)",
            "T3.3 100k db & UH → D3.1–3.2",
        ]),
        ("WP4 · Lebomlás & LCA", "RWTH | M24–M44 | 96 PM → TRL 7", GREEN, [
            "T4.1 EN 13432 & NF T51-800",
            "T4.2 OECD 208 & migráció → D4.1",
            "T4.3 ISO 14040 LCA → D4.2",
        ]),
    ]
    bw, gap, y_wp, bh_wp = 148, 21.3, 122, 34
    for i, (a, b, col, t_list) in enumerate(wps):
        x = 6 + i * (bw + gap)
        box(ov, x, y_wp, bw, bh_wp, col, rounding=6)
        ov.text(x + bw / 2.0, y_wp + 22, a, ha="center", va="center", fontsize=9.5, fontweight="bold", color="white")
        ov.text(x + bw / 2.0, y_wp + 9, b, ha="center", va="center", fontsize=8.0, fontweight="bold", color="#D6EAF8")
        if i < 3:
            ov.annotate("", xy=(x + bw + gap - 2, y_wp + bh_wp / 2.0), xytext=(x + bw + 2, y_wp + bh_wp / 2.0),
                        arrowprops=dict(arrowstyle="-|>", color=NAVY, lw=1.8))
        stem_x = x + 7
        ov.plot([stem_x, stem_x], [y_wp, 47], color=col, linewidth=1.4)
        for t_idx, t_txt in enumerate(t_list):
            ty = 96 - t_idx * 29
            ov.plot([stem_x, x + 14], [ty + 11, ty + 11], color=col, linewidth=1.2)
            box(ov, x + 14, ty, bw - 14, 22, "#FFFFFF", edge=col, lw=1.1, rounding=4)
            ov.text(x + 14 + (bw - 14) / 2.0, ty + 11, t_txt, ha="center", va="center", fontsize=7.8,
                    fontweight="bold", color=DARK)

    box(ov, 6, 4, 658, 28, "#E0ECF8", edge=NAVY, lw=1.2, rounding=6)
    ov.text(335, 21, "WP5 · Projektmenedzsment, IPR & Disszemináció (BME | M1–M48 | 76 PM) — T5.1 Irányítás · T5.2 EPO szabadalom · T5.3 Q1 OA & CEN",
            ha="center", va="center", fontsize=8.6, fontweight="bold", color=NAVY)
    ov.text(335, 10, "→ D5.1 Honlap & DMP (M6) · D5.2 Zárójelentés (M48)   |   Teljes konzorciumi ráfordítás: 520 PM (4,2 M€)",
            ha="center", va="center", fontsize=8.3, fontweight="bold", color=BLUE)
    return fig


# ----------------------------------------------------------------------------
# slide 15 – WP1/WP2 kinetics and thermal map                     (670 x 146)
# ----------------------------------------------------------------------------
def make_fig_slide15_wp12_kinetics():
    W, H = 670, 146
    fig = new_fig(W, H)
    ftitle(fig, W, H, 165, 10, "WP2 · Kristályosodási kinetika gyorsítása (DSC)", 10.5)
    ax1 = axp(fig, W, H, 126, 32, 190, 82)
    hbar(ax1, ["Nyers PHA\n(nukleálatlan)", "PHA + talkum\n(1,5 m/m%)", "PHACK kompound\n(orotinsav + talkum)"],
         [68, 22, 6.5], [RED_L, ORANGE, GREEN], ["68 mp – túl lassú", "22 mp", "6,5 mp – cél < 3,5 s"], 90,
         fs=9, thr=0.6)
    ax1.axvline(8, color=NAVY, linestyle="--", linewidth=1.2, zorder=4)
    axis_label(ax1, "Kristályosodási felezési idő t₁/₂ (mp, 65°C)", 9)

    ftitle(fig, W, H, 510, 10, "WP1–WP2 · Termikus és feldolgozási ablak", 10.5)
    ax2 = axp(fig, W, H, 440, 32, 218, 82)
    hbar(ax2, ["Üvegesedés (Tg)", "Temperált szerszám", "Kávéfőzés (HDT)", "Extrúziós ablak", "Termikus bomlás"],
         [5, 65, 105, 170, 195], [GREY, MID, GREEN, NAVY, RED],
         ["~2°C", "60–70°C", "105°C", "165–175°C", ">185°C – tiltott"], 235, fs=9, thr=0.7)
    axis_label(ax2, "Hőmérséklet (°C) – DSC / TGA / reológia", 9)
    return fig


# ----------------------------------------------------------------------------
# slide 16 – WP3: film cross-section + thermoforming cycle        (670 x 174)
# ----------------------------------------------------------------------------
def make_fig_slide16_wp3_architecture():
    W, H = 670, 174
    fig = new_fig(W, H)
    ov = overlay(fig, W, H)
    ftitle(fig, W, H, 160, 11, "MOL 5-rétegű bio-barrier síkfólia · keresztmetszet", 10.5)
    layers = [("PHA külső · 180 µm", 180, NAVY), ("Bio-Tie · 15 µm", 15, CYAN), ("NFC / PGA barrier · 20 µm", 20, GREEN),
              ("Bio-Tie · 15 µm", 15, CYAN), ("PHA belső · 150 µm", 150, BLUE)]
    scale, x, y = 0.30, 40, 146
    top = y
    centers = []
    for label, t, col in layers:
        hh = t * scale
        y -= hh
        ov.add_patch(patches.Rectangle((x, y), 84, hh, facecolor=col, edgecolor="white", linewidth=0.8))
        centers.append(y + hh / 2.0)
    bottom = y
    label_ys = np.linspace(top - 8, bottom + 8, 5)
    for (label, t, col), cy, ly in zip(layers, centers, label_ys):
        ov.plot([x + 84, x + 104, x + 116], [cy, cy, ly], color="#8FA3B8", linewidth=0.9)
        ov.text(x + 120, ly, label, ha="left", va="center", fontsize=9.5, fontweight="bold", color=DARK)
    ov.annotate("", xy=(28, top), xytext=(28, bottom), arrowprops=dict(arrowstyle="<->", color=NAVY, lw=1.1))
    ov.text(18, (top + bottom) / 2.0, "380–400 µm (±3%)", rotation=90, ha="center", va="center", fontsize=9,
            fontweight="bold", color=NAVY)

    ftitle(fig, W, H, 505, 11, "ALFA temperált termoformálás · ciklusidő (mp)", 10.5)
    ax = axp(fig, W, H, 468, 34, 192, 96)
    steps = ["IR előmelegítés", "Vákuum + túlnyomás", "Kristályosítás 60–70°C", "UH hegesztés"]
    start = [0, 0.9, 1.7, 3.2]
    dur = [0.9, 0.8, 1.5, 0.3]
    cols = [ORANGE, BLUE, NAVY, GREEN]
    yy = np.arange(4)
    ax.barh(yy, dur, left=start, color=cols, height=0.6, edgecolor=NAVY, linewidth=0.8, zorder=3)
    for k in range(4):
        txt = "%s mp" % comma(dur[k])
        if dur[k] >= 0.7:
            ax.text(start[k] + dur[k] / 2.0, k, txt, ha="center", va="center", fontsize=9, fontweight="bold",
                    color="white", zorder=5)
        else:
            ax.text(start[k] - 0.08, k, txt + " (400 db/perc)", ha="right", va="center", fontsize=9,
                    fontweight="bold", color=DARK, zorder=5)
    ax.set_yticks(yy)
    ax.set_yticklabels(steps, fontsize=9, fontweight="bold", color=DARK)
    ax.set_ylim(3.5, -0.5)
    ax.set_xlim(0, 5.3)
    ax.axvline(3.5, color=RED, linestyle="--", linewidth=1.3, zorder=4)
    ax.text(3.5, 1.04, "Σ < 3,5 mp", transform=ax.get_xaxis_transform(), ha="center", va="bottom", fontsize=9,
            fontweight="bold", color=RED)
    axis_label(ax, "Folyamatidő (mp) · kamratűrés ±0,1 mm")
    style_axes(ax, "x")
    return fig


# ----------------------------------------------------------------------------
# slide 20 – risk matrix                                          (270 x 228)
# ----------------------------------------------------------------------------
def make_fig_slide20_risk_heatmap():
    W, H = 270, 228
    fig = new_fig(W, H)
    ftitle(fig, W, H, 135, 12, "Kockázati mátrix (mitigáció előtt → után)", 10.5)
    ax = axp(fig, W, H, 66, 40, 196, 160)
    grid = np.array([[2, 3, 3], [1, 2, 3], [1, 1, 2]])
    cmap = matplotlib.colors.ListedColormap(["#D4EFDF", "#FCF3CF", "#FADBD8"])
    ax.imshow(grid, cmap=cmap, extent=[0, 3, 0, 3], origin="lower", aspect="auto")
    for i in (1, 2):
        ax.axvline(i, color=NAVY, lw=0.9)
        ax.axhline(i, color=NAVY, lw=0.9)
    for tick_axis, setter in ((ax.set_xticks, ax.set_xticklabels), (ax.set_yticks, ax.set_yticklabels)):
        tick_axis([0.5, 1.5, 2.5])
        setter(["Alacsony", "Közepes", "Magas"], fontsize=9.5, fontweight="bold", color=NAVY)
    ax.tick_params(length=0)
    ax.set_xlabel("Súlyosság", fontsize=10, fontweight="bold", color=NAVY, labelpad=3)
    ax.set_ylabel("Valószínűség", fontsize=10, fontweight="bold", color=NAVY, labelpad=3)
    halo = [pe.withStroke(linewidth=2.6, foreground="white")]
    pts = [
        ("R1", (2.5, 1.5), (1.72, 0.72), RED, (0.12, 0.22)),
        ("R2", (1.45, 1.45), (0.68, 0.7), BLUE, (0.12, 0.22)),
        ("R3", (1.3, 0.3), (0.3, 0.3), "#7D3C98", (0.12, 0.2)),
    ]
    for lbl, p0, p1, col, off in pts:
        ax.annotate("", xy=p1, xytext=p0, arrowprops=dict(arrowstyle="-|>", color=col, lw=1.8, shrinkA=5, shrinkB=5))
        ax.plot(*p0, "o", color=col, markersize=9, markeredgecolor="white", zorder=5)
        ax.plot(*p1, "s", color=GREEN, markersize=9, markeredgecolor="white", zorder=5)
        ax.text(p0[0] + off[0], p0[1] + off[1], lbl, fontsize=10, fontweight="bold", color=col, path_effects=halo,
                zorder=6)
        ax.text(p1[0] + off[0], p1[1] + off[1], lbl + "'", fontsize=10, fontweight="bold", color=GREEN,
                path_effects=halo, zorder=6)
    return fig


# ----------------------------------------------------------------------------
# slide 21 – Gantt chart                                          (670 x 216)
# ----------------------------------------------------------------------------
def make_fig_slide21_gantt_timeline():
    W, H = 670, 216
    fig = new_fig(W, H)
    ftitle(fig, W, H, 335, 9, "Részfeladat-szintű (T1.1–T5.3) 48 hónapos Gantt-ütemterv · mérföldkövek és eredmények", 10.0)
    ax = axp(fig, W, H, 210, 28, 448, 164)
    tasks = [
        ("WP1 · T1.1 Gépi tűrések (±0,1 mm)", 0, 6, MID, "M1–M6"),
        ("WP1 · T1.2 Nyers PHA/PHBH audit", 3, 9, MID, "M4–M9"),
        ("WP1 · T1.3 EU 10/2011 & PPWR", 6, 12, MID, "D1.1 · MS1 (M12)"),
        ("WP2 · T2.1 Orotinsav/talkum nukl.", 5, 14, NAVY, "M6–M14"),
        ("WP2 · T2.2 Kétcsigás kompoundálás", 10, 20, NAVY, "M11–M20"),
        ("WP2 · T2.3 Reológia & 50 kg (1k db)", 16, 24, NAVY, "D2.1 · MS2 (M24)"),
        ("WP3 · T3.1 5-rétegű síkfólia (MOL)", 17, 28, BLUE, "M18–M28"),
        ("WP3 · T3.2 Temperált szersz. (ALFA)", 21, 32, BLUE, "M22–M32"),
        ("WP3 · T3.3 100k db pilot & UH", 28, 36, BLUE, "D3.1–3.2 · MS3 (M36)"),
        ("WP4 · T4.1 EN 13432 & NF T51-800", 23, 42, GREEN, "M24–M42"),
        ("WP4 · T4.2 Ökotoxicitás & migráció", 30, 44, GREEN, "D4.1 (M44)"),
        ("WP4 · T4.3 ISO 14040/44 LCA", 32, 44, GREEN, "D4.2 (M44)"),
        ("WP5 · T5.1 Menedzsment & QA", 0, 48, GREY, "D5.2 (M48)"),
        ("WP5 · T5.2 IPR, EPO szabadalom", 12, 48, GREY, "M13–M48"),
        ("WP5 · T5.3 Disszemináció & CEN", 0, 48, GREY, "D5.1 (M6) … M48"),
    ]
    for k, (label, a, b, col, tag) in enumerate(tasks):
        ax.barh(k, b - a, left=a, height=0.72, color=col, edgecolor=NAVY, linewidth=0.5, zorder=3)
        ax.text(a + (b - a) / 2.0, k, tag, ha="center", va="center", fontsize=6.8, fontweight="bold", color="white",
                zorder=5)
    for m, tag in ((12, "MS1 (M12)"), (24, "MS2 (M24)"), (36, "MS3 (M36)"), (44, "D4.1/4.2")):
        ax.axvline(m, color=RED, linestyle="--", linewidth=1.1, zorder=4)
        ax.text(m, 1.01, tag, transform=ax.get_xaxis_transform(), ha="center", va="bottom", fontsize=7.8,
                fontweight="bold", color=RED)
    ax.set_yticks(range(len(tasks)))
    ax.set_yticklabels([t[0] for t in tasks], fontsize=7.4, fontweight="bold", color=NAVY)
    ax.set_ylim(len(tasks) - 0.35, -0.65)
    ax.set_xlim(0, 48.5)
    ax.set_xticks([0, 6, 12, 18, 24, 30, 36, 42, 48])
    ax.set_xticklabels(["M1", "M6", "M12", "M18", "M24", "M30", "M36", "M42", "M48"], fontsize=8.2,
                       fontweight="bold", color=NAVY)
    axis_label(ax, "Hónap (1. év: M1–M12 · 2. év: M13–M24 · 3. év: M25–M36 · 4. év: M37–M48)", 8.5)
    style_axes(ax, "x")
    return fig


# ----------------------------------------------------------------------------
# slide 22 – budget                                               (670 x 170)
# ----------------------------------------------------------------------------
def make_fig_slide22_budget():
    W, H = 670, 170
    fig = new_fig(W, H)
    ftitle(fig, W, H, 175, 11, "Költségkategóriák megoszlása (4,2 M€)", 10.5)
    ax1 = axp(fig, W, H, 120, 34, 200, 94)
    hbar(ax1, ["Személyi (520 PM)", "Utazás és ellátás", "Eszközök", "Egyéb áru/szolg.", "Indirekt (25%)"],
         [50, 3, 16, 11, 20], [NAVY, MID, CYAN, BLUE, GREY],
         ["2,08 M€ · 50%", "0,13 M€ · 3%", "0,67 M€ · 16%", "0,48 M€ · 11%", "0,84 M€ · 20%"], 78)
    axis_label(ax1, "Az összköltségvetés %-ában")

    ftitle(fig, W, H, 515, 11, "Partnerek költségkerete és emberhónapja", 10.5)
    ax2 = axp(fig, W, H, 412, 34, 246, 94)
    hbar(ax2, ["BME (HU)", "MOL (HU)", "RWTH (DE)", "ALFA (HU)", "BIO (IT)", "PCOFF (AT)"],
         [1050, 850, 750, 650, 550, 350], [NAVY, "#004C99", BLUE, GREEN, MID, GREY],
         ["1,05 M€ · 144 PM", "850 k€ · 100 PM", "750 k€ · 96 PM", "650 k€ · 90 PM", "550 k€ · 50 PM",
          "350 k€ · 40 PM"], 1450, fs=9, thr=0.5, height=0.66)
    axis_label(ax2, "ezer € · hazai arány: 60,7% (2,55 M€)")
    return fig


# ----------------------------------------------------------------------------
# slide 11 – KPI mini charts                                      (146 x 128)
# ----------------------------------------------------------------------------
def make_fig_logo(w=175, h=200, dark=True):
    """PHACK emblem on a transparent background: bio-capsule with a leaf inside a closed material loop."""
    from matplotlib.path import Path

    fig = plt.figure(figsize=(w / 72.0, h / 72.0), facecolor="none")
    ax = overlay(fig, w, h)
    cx, cy, r = w / 2.0, h / 2.0, 80.0 * min(w / 175.0, h / 200.0)
    k = r / 80.0
    loop_cols = ("#2FD0F0", "#3EDC8C") if dark else (CYAN, GREEN)
    ink = "#FFFFFF" if dark else NAVY
    cup_col = "#2BB673" if dark else GREEN

    # closed loop: two counter-clockwise arcs, each ending in an arrowhead
    for (a0, a1), col in zip(((12, 158), (192, 338)), loop_cols):
        th = np.radians(np.linspace(a0, a1, 80))
        ax.plot(cx + r * np.cos(th), cy + r * np.sin(th), color=col, lw=6.5 * k, solid_capstyle="butt")
        t = np.radians(a1)
        p = np.array([cx + r * np.cos(t), cy + r * np.sin(t)])
        tang = np.array([-np.sin(t), np.cos(t)])
        nrm = np.array([np.cos(t), np.sin(t)])
        ax.add_patch(patches.Polygon([p + tang * 17 * k, p + nrm * 12 * k, p - nrm * 12 * k], closed=True, color=col, lw=0))

    # capsule cup and lid
    ax.add_patch(patches.Polygon([(cx - 36 * k, cy + 34 * k), (cx + 36 * k, cy + 34 * k),
                                  (cx + 24 * k, cy - 48 * k), (cx - 24 * k, cy - 48 * k)],
                                 closed=True, facecolor=cup_col, edgecolor=ink, lw=2.2 * k, joinstyle="round"))
    ax.add_patch(patches.FancyBboxPatch((cx - 42 * k, cy + 34 * k), 84 * k, 11 * k,
                                        boxstyle=f"round,pad=0,rounding_size={4 * k}",
                                        facecolor=ink, edgecolor=ink, lw=1))

    # leaf cut into the cup body
    verts = [(cx, cy - 36 * k), (cx - 30 * k, cy - 14 * k), (cx - 22 * k, cy + 18 * k), (cx, cy + 26 * k),
             (cx + 22 * k, cy + 18 * k), (cx + 30 * k, cy - 14 * k), (cx, cy - 36 * k)]
    codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4, Path.CURVE4, Path.CURVE4, Path.CURVE4]
    ax.add_patch(patches.PathPatch(Path(verts, codes), facecolor="#FFFFFF", edgecolor="none"))
    ax.plot([cx, cx], [cy - 34 * k, cy + 14 * k], color=cup_col, lw=2.0 * k, solid_capstyle="round")
    for dy, dx in ((-10, 11), (2, 10)):
        ax.plot([cx, cx + dx * k], [cy + dy * k, cy + (dy + 9) * k], color=cup_col, lw=1.5 * k, solid_capstyle="round")
        ax.plot([cx, cx - dx * k], [cy + dy * k, cy + (dy + 9) * k], color=cup_col, lw=1.5 * k, solid_capstyle="round")
    return fig


def make_fig_kpi(n):
    W, H = 146, 128
    fig = new_fig(W, H)
    ov = overlay(fig, W, H)
    if n == 1:
        ftitle(fig, W, H, 73, 9, "Önköltség-index (Al = 100)", 9.5)
        ax = axp(fig, W, H, 20, 24, 118, 68)
        ax.bar([0, 1], [100, 100], width=0.6, color=[GREY, GREEN], edgecolor=NAVY, linewidth=0.8, zorder=3)
        ax.bar([1], [10], bottom=[100], width=0.6, color="#A9DFBF", edgecolor=NAVY, linewidth=0.8, hatch="///",
               zorder=3)
        ax.text(0, 50, "100", ha="center", va="center", fontsize=11, fontweight="bold", color="white", zorder=5)
        ax.text(1, 50, "100", ha="center", va="center", fontsize=11, fontweight="bold", color="white", zorder=5)
        ax.text(1, 114, "≤ +10%", ha="center", va="bottom", fontsize=10, fontweight="bold", color=GREEN, zorder=5)
        ax.set_ylim(0, 135)
        ax.set_xlim(-0.55, 1.55)
        ax.set_xticks([0, 1])
        ax.set_xticklabels(["Al-kapszula", "PHACK"], fontsize=9, fontweight="bold", color=NAVY)
        ax.set_yticks([])
        style_axes(ax, None)
        ax.spines["left"].set_visible(False)
        ax.tick_params(axis="x", length=0)
    elif n == 2:
        ftitle(fig, W, H, 73, 9, "Piacpenetráció", 9.5)
        axd = axp(fig, W, H, 38, 34, 70, 70)
        axd.pie([2, 98], colors=[GREEN, "#D5DDE6"], startangle=90, counterclock=False,
                wedgeprops=dict(width=0.36, edgecolor="white", linewidth=1.2))
        axd.text(0, 0, ">2%", ha="center", va="center", fontsize=14, fontweight="bold", color=GREEN)
        box(ov, 12, 4, 122, 24, GREEN, rounding=6)
        ov.text(73, 16, "≥25% CO₂e ↓", ha="center", va="center", fontsize=11, fontweight="bold", color="white")
    elif n == 3:
        ftitle(fig, W, H, 73, 9, "Idő a >90% lebomlásig", 9.5)
        ax = axp(fig, W, H, 56, 28, 82, 66)
        hbar(ax, ["Ipari\n(58°C)", "Házi\n(20–25°C)"], [6, 12], [BLUE, GREEN], ["<6 hó", "<12 hó"], 13.5, fs=9,
             thr=0.4, height=0.55)
        ax.set_xticks([0, 6, 12])
        axis_label(ax, "hónap", 9)
    else:
        ftitle(fig, W, H, 73, 9, "12 hó aroma, tasak nélkül", 9.5)
        for m in range(12):
            r, c = divmod(m, 6)
            x = 8 + c * 22.5
            y = 80 - r * 22
            box(ov, x, y, 20, 19, GREEN, rounding=3)
            ov.text(x + 10, y + 9.5, str(m + 1), ha="center", va="center", fontsize=9, fontweight="bold",
                    color="white")
        box(ov, 6, 24, 64, 22, NAVY, rounding=6)
        ov.text(38, 35, "OTR<0,05", ha="center", va="center", fontsize=9.5, fontweight="bold", color="white")
        box(ov, 76, 24, 64, 22, BLUE, rounding=6)
        ov.text(108, 35, "WVTR<1–2", ha="center", va="center", fontsize=9.5, fontweight="bold", color="white")
        ov.text(73, 10, "külső védőtasak nélkül", ha="center", va="center", fontsize=9, color=GREY)
    return fig
