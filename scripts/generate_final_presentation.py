# -*- coding: utf-8 -*-
"""
Generate Final Presentation for PHACK (HORIZON-CL6-2026-CIRCBIO RIA)
Aligns strictly with:
- etc/FHG HE sablon 2026.pptx (visual theme, BME/PT 4:3 layouts, colors)
- etc/FHG mintaprezentáció 2026.pdf (flow across 24 slides + PERT/engineering diagrams)
- SPEAKER_NOTES.md & DEFENSE_QA.md & PROJECT_CONTEXT.md (100% numerical and technical parity)
"""

import io
import os
import sys
import pptx
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR) if os.path.basename(SCRIPT_DIR) == "scripts" else SCRIPT_DIR
DOCS_DIR = os.path.join(BASE_DIR, "docs") if os.path.isdir(os.path.join(BASE_DIR, "docs")) else BASE_DIR
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from build_and_verify_notes import get_slide_data, count_words

# Color Palette
COLOR_BME_NAVY = RGBColor(0, 51, 102)       # #003366 Deep BME Navy
COLOR_BME_BLUE = RGBColor(0, 102, 153)      # #006699 Primary Accent Blue
COLOR_CYAN = RGBColor(0, 168, 204)          # #00A8CC Cyan Highlight
COLOR_GREEN = RGBColor(30, 130, 76)         # #1E824C Bio Green Accent
COLOR_DARK_TEXT = RGBColor(25, 30, 36)      # #191E24 Dark charcoal body text
COLOR_MUTED_TEXT = RGBColor(90, 100, 110)   # #5A646E Secondary text
COLOR_WHITE = RGBColor(255, 255, 255)       # #FFFFFF
COLOR_HEADER_BG = RGBColor(0, 51, 102)      # #003366 Table Header Navy
COLOR_ROW_ALT = RGBColor(242, 247, 252)     # #F2F7FC Alternating row light blue
COLOR_CARD_BG = RGBColor(248, 250, 253)     # #F8FAFD Card light gray-blue
COLOR_CARD_BORDER = RGBColor(195, 213, 232) # #C3D5E8 Card border
COLOR_CARD_TITLE_BG = RGBColor(224, 236, 248) # #E0ECF8 Card header band
COLOR_GANTT_ACTIVE = RGBColor(0, 51, 102)
COLOR_GANTT_PLAN = RGBColor(195, 222, 245)

plt.rcParams["font.sans-serif"] = ["Calibri", "Segoe UI", "Arial", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False


def set_font(run, name="Calibri", size=10, bold=False, italic=False, color=COLOR_DARK_TEXT):
    run.font.name = name
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color


def create_card(slide, left, top, width, height, title="", title_bg=COLOR_CARD_TITLE_BG,
                border_color=COLOR_CARD_BORDER, bg_color=COLOR_CARD_BG, accent_color=COLOR_BME_BLUE):
    """Creates a clean rectangular card container with subtle rounded corners and a distinct header band."""
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(left / 72), Inches(top / 72), Inches(width / 72), Inches(height / 72)
    )
    try:
        shape.adjustments[0] = 0.02
    except Exception:
        pass
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    shape.line.color.rgb = border_color
    shape.line.width = Pt(1.1)

    if title:
        hdr_h = 24
        hdr = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches((left + 1) / 72), Inches((top + 1) / 72),
            Inches((width - 2) / 72), Inches(hdr_h / 72)
        )
        hdr.fill.solid()
        hdr.fill.fore_color.rgb = title_bg
        hdr.line.fill.background()

        bar = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches((left + 1) / 72), Inches((top + 1) / 72),
            Inches(4 / 72), Inches(hdr_h / 72)
        )
        bar.fill.solid()
        bar.fill.fore_color.rgb = accent_color
        bar.line.fill.background()

        tb = slide.shapes.add_textbox(
            Inches((left + 8) / 72), Inches((top + 1) / 72),
            Inches((width - 12) / 72), Inches(hdr_h / 72)
        )
        tf = tb.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf.margin_left = Inches(4 / 72)
        tf.margin_right = Inches(4 / 72)
        tf.margin_top = Inches(1 / 72)
        tf.margin_bottom = Inches(1 / 72)
        p = tf.paragraphs[0]
        p.text = title
        set_font(p.runs[0], size=10.5, bold=True, color=COLOR_BME_NAVY)
    return shape


def add_header_elements(slide, title_text, subtitle_text, slide_num_str):
    """Formats the BME PT header bar and adds subtitle and slide number."""
    if slide.shapes.title:
        title_shape = slide.shapes.title
        title_shape.text = title_text
        tf = title_shape.text_frame
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.LEFT
        set_font(p.runs[0], size=20, bold=True, color=COLOR_WHITE)

    sub_box = slide.shapes.add_textbox(Inches(25 / 72), Inches(70 / 72), Inches(595 / 72), Inches(22 / 72))
    sub_tf = sub_box.text_frame
    sub_tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    sub_tf.margin_left = sub_tf.margin_right = sub_tf.margin_top = sub_tf.margin_bottom = 0
    sub_p = sub_tf.paragraphs[0]
    sub_p.text = subtitle_text
    set_font(sub_p.runs[0], size=11, bold=True, color=COLOR_BME_NAVY)

    num_box = slide.shapes.add_textbox(Inches(620 / 72), Inches(70 / 72), Inches(75 / 72), Inches(22 / 72))
    num_tf = num_box.text_frame
    num_tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    num_tf.margin_left = num_tf.margin_right = num_tf.margin_top = num_tf.margin_bottom = 0
    num_p = num_tf.paragraphs[0]
    num_p.alignment = PP_ALIGN.RIGHT
    num_p.text = slide_num_str
    set_font(num_p.runs[0], size=11.5, bold=True, color=COLOR_BME_NAVY)


def fit_table(table, base_font, max_font):
    """Picks the largest font size at which every cell fits its column, and the matching row heights (pt)."""
    total_h = sum(r.height for r in table.rows) / 12700.0
    widths = [c.width / 12700.0 for c in table.columns]
    n_rows = len(table.rows)

    def row_heights(size):
        heights = []
        for r in range(n_rows):
            h = 0.0
            for c, w in enumerate(widths):
                n = _wrap_line_count(table.cell(r, c).text_frame.text, size, w - 8, char_w=0.47, word_w=0.54)
                if n is None:
                    return None
                h = max(h, n * size * 1.2 + 7)
            heights.append(h)
        return heights

    size = max_font
    while size > base_font:
        hs = row_heights(size)
        if hs is not None and sum(hs) <= total_h:
            return size, hs, total_h
        size -= 0.25
    return base_font, row_heights(base_font) or [total_h / n_rows] * n_rows, total_h


def style_table(table, header_bg=COLOR_HEADER_BG, header_fg=COLOR_WHITE, alt_bg=COLOR_ROW_ALT, font_size=8.8,
                max_font=None):
    """Applies clean BME styling to a table; enlarges the font to use the table's height. Returns the font size."""
    base_font = font_size
    font_size, heights, total_h = fit_table(table, base_font, max_font or min(base_font + 3.0, 11.5))
    extra = max(0.0, total_h - sum(heights))
    n_body = max(1, len(heights) - 1)
    for idx, row in enumerate(table.rows):
        row.height = int((heights[idx] + (extra / n_body if idx else 0)) * 12700)
    for col_idx, cell in enumerate(table.rows[0].cells):
        cell.fill.solid()
        cell.fill.fore_color.rgb = header_bg
        tf = cell.text_frame
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf.margin_left = tf.margin_right = Inches(4 / 72)
        tf.margin_top = tf.margin_bottom = Inches(2.5 / 72)
        for p in tf.paragraphs:
            p.alignment = PP_ALIGN.CENTER if col_idx in [0, 2, 3, 4, 5, 6] and len(table.columns) >= 4 else PP_ALIGN.LEFT
            for r in p.runs:
                set_font(r, size=font_size, bold=True, color=header_fg)

    for row_idx in range(1, len(table.rows)):
        row = table.rows[row_idx]
        row_bg = alt_bg if row_idx % 2 == 1 else COLOR_WHITE
        for col_idx, cell in enumerate(row.cells):
            cell.fill.solid()
            cell.fill.fore_color.rgb = row_bg
            tf = cell.text_frame
            tf.vertical_anchor = MSO_ANCHOR.MIDDLE
            tf.margin_left = tf.margin_right = Inches(4 / 72)
            tf.margin_top = tf.margin_bottom = Inches(2.5 / 72)
            for p in tf.paragraphs:
                for r in p.runs:
                    is_bold = (col_idx == 0 or (col_idx == 1 and len(row.cells) <= 3))
                    fg = COLOR_BME_NAVY if col_idx == 0 else COLOR_DARK_TEXT
                    set_font(r, size=font_size, bold=is_bold, color=fg)
    return font_size


def embed_note(slide, slide_info):
    """Embeds the exact compliant speaker note into the PPTX slide."""
    notes_slide = slide.notes_slide
    tf = notes_slide.notes_text_frame
    note_content = (
        f"=== DIA {slide_info['num']}/24: {slide_info['title']} ===\n"
        f"Előadó: {slide_info['speaker_name']} ({slide_info['role']})\n"
        f"Időkeret: {slide_info['seconds']} mp ({slide_info['start_time']} - {slide_info['end_time']}) | Szószám: {count_words(slide_info['speech'])} szó\n"
        f"Vizuális horgony: {slide_info['visual_anchor']}\n\n"
        f"ELŐADÓI SZÖVEG:\n\"{slide_info['speech']}\"\n\n"
        f"SZÍNPADI INSTRUKCIÓ:\n{slide_info['stage_cue']}"
    )
    tf.text = note_content


import re as _re

HIGHLIGHT_PATTERN = _re.compile(
    r"((?:10\s+milliárd|53\s+milliárd|100\s*000\s*db|1\s*000\s*db|500\s+millió|500\s+tonna|"
    r"4,2\s*millió\s*EUR|4,2M\s*EUR|4\s*200\s*000\s*€|520\s*PM|520\s+személyhónap|50\s*kg|"
    r"TRL\s*3(?:\s*➔\s*TRL\s*7|\s*➔\s*6/7)?|TRL\s*6/7|TRL\s*6|TRL\s*7|TRL\s*4|TRL\s*5|"
    r"15–19\s*bar|max\.\s*19\s*bar|95°C|90–95°C|93±2°C|120°C|55–60°C|55–65°C|58°C|60–70°C|20–25°C|20–30°C|165–175°C|"
    r"HDT\s*>\s*95–105°C|Tm\s*>\s*140°C|Tm\s*≈\s*145–170°C|"
    r"OTR\s*<\s*0,05(?:\s*cm³/\(kapszula·nap(?:·bar)?\))?|WVTR\s*<\s*1,0–2,0\s*g/\(m²·nap\)|"
    r"0,40\s*mm|380–400\s*µm|±0,1\s*mm|±3%|<\s*3,5\s*mp|400\s*db/perc|20–35\s*kHz|30–45\s*nap|"
    r"EN\s*13432|NF\s*T51-800|ISO\s*14855|ISO\s*14040(?:/44|/14044)?|EU\s*10/2011|PPWR(?:\s*9\.\s*cikk)?|"
    r"AGA\s*Art\.\s*6\.2\.B|25%|≥\s*25%\s*CO₂e|≥\s*25%|<\s*\+10%|>\s*2%|>\s*90%|>90%|zéró\s+mikroműanyag|"
    r"5-rétegű|orotinsav\w*|temperált|bölcsőtől-sírig|Cradle-to-Grave|PHA/PHBH|KPI\s*[1-4]|"
    r"D1\.1|D2\.1|D3\.1|D3\.2|D4\.1|D4\.2|D5\.1|D5\.2|MS1|MS2|MS3|WP1|WP2|WP3|WP4|WP5))",
    _re.IGNORECASE
)


def _append_rich_runs(paragraph, text, font_size, base_color=COLOR_DARK_TEXT, hl_color=COLOR_BME_BLUE):
    parts = HIGHLIGHT_PATTERN.split(text)
    for part in parts:
        if not part:
            continue
        r = paragraph.add_run()
        r.text = part
        if HIGHLIGHT_PATTERN.fullmatch(part):
            set_font(r, size=font_size, bold=True, color=hl_color)
        else:
            set_font(r, size=font_size, bold=False, color=base_color)


def populate_text_box(tb, items, font_size=9.5, bullet=True, space_after=4.0, max_size=13.0):
    """Fills a text box with bullet points or paragraphs with highlighted lead-ins and rich keyword emphasis.

    font_size is the minimum size; the text is enlarged up to max_size as long as it fits the box."""
    base_size = font_size
    if tb.width / 12700.0 > 600:
        max_size = max(max_size, 14.0)
    font_size = fit_font_size(items, tb.width / 12700.0, tb.height / 12700.0, base_size, bullet, space_after, max_size)
    space_after = space_after * font_size / base_size
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(6 / 72)
    tf.margin_right = Inches(6 / 72)
    tf.margin_top = Inches(4 / 72)
    tf.margin_bottom = Inches(4 / 72)

    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(space_after)
        prefix = "▸ " if bullet else ""
        if isinstance(item, tuple):
            p.text = prefix + item[0]
            set_font(p.runs[0], size=font_size, bold=True, color=COLOR_BME_NAVY)
            _append_rich_runs(p, item[1], font_size, base_color=COLOR_DARK_TEXT, hl_color=COLOR_BME_BLUE)
        else:
            p.text = prefix if prefix else ""
            if prefix and p.runs:
                set_font(p.runs[0], size=font_size, bold=True, color=COLOR_BME_NAVY)
            _append_rich_runs(p, item, font_size, base_color=COLOR_DARK_TEXT, hl_color=COLOR_BME_BLUE)


def add_fig_to_slide(slide, fig, left_pt, top_pt, width_pt, height_pt, dpi=240):
    """Renders a matplotlib figure into an in-memory PNG stream and places it on the slide without distortion."""
    fig_w, fig_h = fig.get_size_inches() * 72.0
    scale = min(width_pt / fig_w, height_pt / fig_h)
    pic_w, pic_h = fig_w * scale, fig_h * scale
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=dpi, facecolor=fig.get_facecolor())
    plt.close(fig)
    buf.seek(0)
    slide.shapes.add_picture(
        buf,
        Inches((left_pt + (width_pt - pic_w) / 2) / 72), Inches(top_pt / 72),
        Inches(pic_w / 72), Inches(pic_h / 72)
    )


def _wrap_line_count(text, size, width_pt, char_w=0.45, word_w=None):
    """Estimates the wrapped line count of a text at a font size; None if a word is wider than the box."""
    max_chars = max(4.0, width_pt / (size * char_w))
    max_word = max(4.0, width_pt / (size * (word_w or char_w)))
    lines = 0
    for part in text.split("\n"):
        words = part.split()
        if not words:
            lines += 1
            continue
        cur = 0.0
        line_cnt = 1
        for w in words:
            if len(w) > max_word:
                return None
            if cur == 0:
                cur = len(w)
            elif cur + 1 + len(w) <= max_chars:
                cur += 1 + len(w)
            else:
                line_cnt += 1
                cur = len(w)
        lines += line_cnt
    return lines


def _item_text(item, bullet):
    body = (item[0] + item[1]) if isinstance(item, tuple) else item
    return ("▸ " if bullet else "") + body


def fit_font_size(items, width_pt, height_pt, base_size, bullet, space_after, max_size=13.0):
    """Largest font size (base_size..max_size) at which the bullet list still fits the text box."""
    size = max_size
    while size > base_size:
        sa = space_after * size / base_size
        total = 8.0
        ok = True
        for item in items:
            n = _wrap_line_count(_item_text(item, bullet), size, width_pt - 12)
            if n is None:
                ok = False
                break
            total += n * size * 1.2 + sa
        if ok and total <= height_pt:
            return size
        size -= 0.25
    return base_size


from phack_figures import (  # noqa: E402
    make_fig_slide3_consortium, make_fig_slide4_capsule_barrier, make_fig_slide5_trl_roadmap,
    make_fig_slide6_waste_and_lca, make_fig_slide7_biodeg_comparison, make_fig_slide8_process_chain,
    make_fig_slide14_pert, make_fig_slide15_wp12_kinetics, make_fig_slide16_wp3_architecture,
    make_fig_slide20_risk_heatmap, make_fig_slide21_gantt_timeline, make_fig_slide22_budget, make_fig_kpi, make_fig_logo,
)


def build_all_slides():
    template_path = os.path.join(BASE_DIR, "etc", "FHG HE sablon 2026.pptx")
    if not os.path.exists(template_path):
        template_path = os.path.abspath(os.path.join(BASE_DIR, "..", "2026 GYAKORLAT", "L1 pályázatírás", "FHG HE sablon 2026.pptx"))
    output_path = os.path.join(BASE_DIR, "PHACK_Prezentacio_Vegleges.pptx")
    slides_data = get_slide_data()

    prs = pptx.Presentation(template_path)

    # Remove existing 15 template slides
    rId_list = [prs.slides._sldIdLst[i].rId for i in range(len(prs.slides))]
    for rId in rId_list:
        prs.part.drop_rel(rId)
    prs.slides._sldIdLst.clear()

    print("Building 24 slides on official course template with diagrams and 100% parity...")

    # =========================================================================
    # SLIDE 1: Címlap (Layout 0: Címdia)
    # =========================================================================
    s1 = prs.slides.add_slide(prs.slide_layouts[0])
    for sh in list(s1.shapes):
        sp = sh._element
        sp.getparent().remove(sp)

    tb_num1 = s1.shapes.add_textbox(Inches(620 / 72), Inches(25 / 72), Inches(75 / 72), Inches(22 / 72))
    p_num1 = tb_num1.text_frame.paragraphs[0]
    p_num1.alignment = PP_ALIGN.RIGHT
    p_num1.text = "1/24"
    set_font(p_num1.runs[0], size=11.5, bold=True, color=COLOR_CYAN)

    def centered_box(top, height, left=45, width=630):
        tb = s1.shapes.add_textbox(Inches(left / 72), Inches(top / 72), Inches(width / 72), Inches(height / 72))
        tb.text_frame.word_wrap = True
        return tb

    tb_tag = centered_box(106, 22)
    p_tag = tb_tag.text_frame.paragraphs[0]
    p_tag.alignment = PP_ALIGN.CENTER
    p_tag.text = "HORIZON EUROPE KUTATÁSI ÉS INNOVÁCIÓS PÁLYÁZAT (RIA)"
    set_font(p_tag.runs[0], size=12.5, bold=True, color=COLOR_CYAN)

    tb_main = centered_box(124, 50)
    p_main = tb_main.text_frame.paragraphs[0]
    p_main.alignment = PP_ALIGN.CENTER
    p_main.text = "PHACK"
    set_font(p_main.runs[0], size=42, bold=True, color=COLOR_WHITE)

    tb_sub = centered_box(176, 62)
    p_sub1 = tb_sub.text_frame.paragraphs[0]
    p_sub1.alignment = PP_ALIGN.CENTER
    p_sub1.text = "Biológiailag 100%-ban Lebomló PHA-Alapú Kávékapszula és Élelmiszercsomagolási Rendszer"
    set_font(p_sub1.runs[0], size=15.5, bold=True, color=COLOR_WHITE)
    p_sub2 = tb_sub.text_frame.add_paragraph()
    p_sub2.alignment = PP_ALIGN.CENTER
    p_sub2.space_before = Pt(4)
    p_sub2.text = "HORIZON-CL6-2026-CIRCBIO (RIA) | 48 hónap | 4,2M EUR | TRL 3 ➔ TRL 7"
    set_font(p_sub2.runs[0], size=11.5, bold=True, color=COLOR_CYAN)

    add_fig_to_slide(s1, make_fig_logo(126, 144), 297, 240, 126, 144)

    tb_meta = centered_box(376, 36)
    for i, line in enumerate(["Fenntartható Hulladékgazdálkodás (BMEGEPTNX01 / BMEGEPTMSVFEHU-01)",
                              "GY02 gyakorlat, P01 projekttéma | Konzorciumvezető: BME Polimertechnika Tanszék | 2026.11.12."]):
        p_meta = tb_meta.text_frame.paragraphs[0] if i == 0 else tb_meta.text_frame.add_paragraph()
        p_meta.alignment = PP_ALIGN.CENTER
        p_meta.text = line
        set_font(p_meta.runs[0], size=11.5, bold=(i == 0), color=COLOR_WHITE)
    embed_note(s1, slides_data[0])

    def setup_content_slide(idx, title, subtitle):
        s = prs.slides.add_slide(prs.slide_layouts[1])
        for sh in list(s.shapes):
            if sh != s.shapes.title:
                sp = sh._element
                sp.getparent().remove(sp)
        add_header_elements(s, title, subtitle, f"{idx}/24")
        embed_note(s, slides_data[idx - 1])
        return s

    # =========================================================================
    # SLIDE 2: Alapadatok (Layout 1)
    # =========================================================================
    s2 = setup_content_slide(2, "Alapadatok", "Általános pályázati információk és absztrakt")
    t2_shape = s2.shapes.add_table(5, 2, Inches(25 / 72), Inches(96 / 72), Inches(530 / 72), Inches(150 / 72))
    t2 = t2_shape.table
    t2.columns[0].width = Inches(135 / 72)
    t2.columns[1].width = Inches(395 / 72)
    t2_data = [
        ["Rövidítés (Acronym)", "PHACK – PHA Coffee Capsule Packaging"],
        ["Pályázat címe", "Biológiailag lebomló PHA-alapú kávékapszula és élelmiszercsomagolási rendszer fejlesztése"],
        ["Pályázati felhívás & Futamidő", "HORIZON-CL6-2026-CIRCBIO (Research and Innovation Action – RIA) | 48 hónap (4 év)"],
        ["Összköltségvetés & Támogatás", "4,2 millió EUR (4 200 000 €) | 100%-os EU támogatási intenzitás | 520 személyhónap (PM)"],
        ["Szabad kulcsszavak", "PHA, polihidroxialkanoát, bio-alapú kávékapszula, 5-rétegű koextrúzió, termoformálás, házi komposztálás (NF T51-800)"]
    ]
    for r_idx, row in enumerate(t2_data):
        for c_idx, val in enumerate(row):
            t2.cell(r_idx, c_idx).text = val
    fs2 = style_table(t2, header_bg=COLOR_CARD_TITLE_BG, header_fg=COLOR_BME_NAVY, font_size=9.0, max_font=9.8)
    for r in range(5):
        t2.cell(r, 0).fill.solid()
        t2.cell(r, 0).fill.fore_color.rgb = COLOR_CARD_TITLE_BG
        set_font(t2.cell(r, 0).text_frame.paragraphs[0].runs[0], size=fs2, bold=True, color=COLOR_BME_NAVY)

    add_fig_to_slide(s2, make_fig_logo(131, 150, dark=False), 564, 96, 131, 150)

    create_card(s2, 25, 254, 670, 260, title="Pályázati Összefoglaló (Executive Abstract)")
    tb_abs = s2.shapes.add_textbox(Inches(35 / 72), Inches(284 / 72), Inches(650 / 72), Inches(224 / 72))
    abs_items = [
        ("A piaci és környezeti probléma: ", "Évente több mint 10 milliárd hagyományos alumínium és fosszilis műanyag (PP) kávékapszula kerül kommunális hulladéklerakókba vagy égetőkbe az EU-ban, mivel a nedves kávézacc miatt a visszagyűjtési arány alacsony (NL: kb. 25%)."),
        ("A PHACK innovatív megoldása: ", "100%-ban természetes eredetű, mezőgazdasági melléktermékekből és használt sütőolajból (UCO) bakteriális fermentációval előállított polihidroxialkanoát (PHA/PHBH) kávékapszula és zárófólia kifejlesztése."),
        ("Műszaki és feldolgozástechnológiai áttörés: ", "Orotinsavval nukleált hőstabil bio-kompound (HDT > 95–105°C, Tm > 140°C) és 5-rétegű bio-barrier síkfólia (0,40 mm, OTR < 0,05 cm³/(kapszula·nap·bar)) koextrúziója és temperált termoformálása, amely ellenáll a 90–95°C-os (93±2°C) víznek és 15–19 bar (max. 19 bar) nyomásnak."),
        ("Zárt szerves körforgás és TRL 3 ➔ TRL 7 ugrás: ", "A kapszula a kávézaccal együtt, szétválasztás nélkül komposztálható házi kerti talajban (20–25°C, NF T51-800: 20–30°C) és biogázüzemben (EN 13432), zéró mikroműanyaggal. 48 hónap alatt TRL 3-ról 100 000 db-os üzemi demonstrációig (TRL 7) jutunk.")
    ]
    populate_text_box(tb_abs, abs_items, font_size=9.5, bullet=True, space_after=5.0)

    # =========================================================================
    # SLIDE 3: Konzorcium (Layout 1 + Value-Chain & Country Chart)
    # =========================================================================
    s3 = setup_content_slide(3, "Konzorcium", "3.2 A résztvevők és a konzorcium egészének kapacitása – Résztvevők listája (Táblázat 3.2)")
    t3_shape = s3.shapes.add_table(7, 6, Inches(25 / 72), Inches(94 / 72), Inches(670 / 72), Inches(182 / 72))
    t3 = t3_shape.table
    t3.columns[0].width = Inches(25 / 72)
    t3.columns[1].width = Inches(222 / 72)
    t3.columns[2].width = Inches(52 / 72)
    t3.columns[3].width = Inches(56 / 72)
    t3.columns[4].width = Inches(46 / 72)
    t3.columns[5].width = Inches(269 / 72)
    t3_data = [
        ["#", "Résztvevő Hivatalos Neve", "Rövidítés", "Típus", "Ország", "Szerepkör az Értékláncban (Büdzsé | Erőforrás)"],
        ["1", "Budapesti Műszaki és Gazdaságtudományi Egyetem", "BME", "RTO", "HU", "Koordinátor, PHA kompound receptúra és labortesztek (1,05M € | 144 PM)"],
        ["2", "MOL Magyar Olaj- és Gázipari Nyrt.", "MOL", "IND", "HU", "Ipari kompoundálás, 5-rétegű síkfólia koextrúzió (850k € | 100 PM)"],
        ["3", "Alfa Industry Csomagolástechnikai Kft.", "ALFA", "SME", "HU", "Temperált termoformáló szerszám, kapszula mélyhúzás (650k € | 90 PM)"],
        ["4", "RWTH Aachen University", "RWTH", "RTO", "DE", "Biodegradáció (EN 13432, NF T51-800), ökotoxicitás, LCA (750k € | 96 PM)"],
        ["5", "Danimer / Bio-on EU PHA Pilot (Kaneka PHBH ref.)", "BIO", "IND", "IT", "Mikrobiális PHA/PHBH fermentáció bio-hulladékból (550k € | 50 PM)"],
        ["6", "PackCoffee Europe Barista Alliance", "PCOFF", "ASSO/IND", "AT", "Iparági szövetség, töltősori teszt (400 db/perc), UH hegesztés (350k € | 40 PM)"]
    ]
    for r_idx, row in enumerate(t3_data):
        for c_idx, val in enumerate(row):
            t3.cell(r_idx, c_idx).text = val
    style_table(t3, font_size=8.2)

    create_card(s3, 25, 282, 670, 102, title="Konzorciumi Kapacitás (RTO: kutatóhely | IND: nagyvállalat | SME: KKV | ASSO: szövetség) és Alvállalkozás")
    tb_c3 = s3.shapes.add_textbox(Inches(35 / 72), Inches(308 / 72), Inches(650 / 72), Inches(72 / 72))
    c3_items = [
        ("Teljes értéklánc (4 ország, 6 partner, 4 szereplőtípus): ", "2 kutatóegyetem (RTO: BME, RWTH), 2 ipari nagyvállalat (IND: MOL, BIO/Kaneka-Danimer), 1 szerszámgyártó KKV (SME: ALFA) és 1 iparági szövetség/töltőüzem (ASSO/IND: PackCoffee). Hazai arány: 60,7% (2,55M EUR, 334 PM)."),
        ("Miért nincs logisztikai partner? (Subcontracting): ", "A Horizon Europe AGA Art. 6.2.B és 9.3 alapján a szállítás nem K+F tevékenység, így alvállalkozásként számolható el (elkerülve a 25% indokolatlan overheadet és a Criterion 3 pontlevonást).")
    ]
    populate_text_box(tb_c3, c3_items, font_size=8.4, bullet=True, space_after=2.0)

    fig3 = make_fig_slide3_consortium()
    add_fig_to_slide(s3, fig3, 25, 384, 670, 130)

    # =========================================================================
    # SLIDE 4: Kiválóság - Célkitűzések és Ambíciók (Layout 1 + Diagram)
    # =========================================================================
    s4 = setup_content_slide(4, "Kiválóság", "1.1 Célkitűzések és ambíciók – Stratégiai célok és műszaki ambíció")
    create_card(s4, 25, 96, 325, 240, title="Stratégiai Célkitűzések (4 Pillér)")
    tb_s4_l = s4.shapes.add_textbox(Inches(35 / 72), Inches(124 / 72), Inches(305 / 72), Inches(206 / 72))
    s4_l_items = [
        ("1. Hőstabil PHA/PHBH kompound: ", "Baktériumok által szintetizált polihidroxialkanoát mátrix optimalizálása orotinsav és talkum nukleálószerekkel."),
        ("2. 5-rétegű bio-barrier szerkezet: ", "Koextrudált záróréteg (OTR < 0,05 cm³/(kapszula·nap·bar)) a 12 hónapos aromastabilitásért védőgáz nélkül."),
        ("3. 100% Biológiai lebonthatóság: ", "Házi komposztban (20–25°C, NF T51-800: 20–30°C) és ipari komposztban (EN 13432) zéró mikroműanyag-képződéssel."),
        ("4. Drop-in ipari kompatibilitás: ", "Nespresso-kompatibilis geometria (±0,1 mm) és 400 db/perc töltősori alkalmazhatóság.")
    ]
    populate_text_box(tb_s4_l, s4_l_items, font_size=8.8, bullet=True, space_after=3.0)

    create_card(s4, 370, 96, 325, 240, title="Műszaki Ambíció és Túlmutatás a PLA-n")
    tb_s4_r = s4.shapes.add_textbox(Inches(380 / 72), Inches(124 / 72), Inches(305 / 72), Inches(206 / 72))
    s4_r_items = [
        ("A jelenlegi PLA kapszulák kudarca: ", "A piaci bio-kapszulák többsége PLA alapú, amely alacsony üvegesedési hőmérséklete (Tg ≈ 55–60°C, irodalmi: 55–65°C) miatt a forró extrakció során ellágyul, és csak ipari komposztálóban (>58°C) bomlik le."),
        ("Extrém kávéfőzési igénybevétel: ", "A PHACK kompound (HDT > 95–105°C, Tm > 140°C) alakstabil marad a 90–95°C-os (93±2°C) vízhőmérséklet és a 15–19 bar (max. 19 bar) extrakciós nyomás alatt."),
        ("Zárt tápanyag-körforgás: ", "A nitrogénben, foszforban és káliumban gazdag kávézacc a kapszulával együtt közvetlenül a kerti komposztba vagy a MOHU barna kukába dobható.")
    ]
    populate_text_box(tb_s4_r, s4_r_items, font_size=8.8, bullet=True, space_after=3.5)

    fig4 = make_fig_slide4_capsule_barrier()
    add_fig_to_slide(s4, fig4, 25, 342, 670, 172)

    # =========================================================================
    # SLIDE 5: Kiválóság - TRL Ugrás (Layout 1 + Stage-Gate Chart)
    # =========================================================================
    s5 = setup_content_slide(5, "Kiválóság", "1.1 Célkitűzések és ambíciók – Technológiai érettségi szintek (TRL 3 ➔ TRL 7)")
    create_card(s5, 25, 96, 325, 168, title="Kiindulási Szint: TRL 3 (Laboratóriumi PoC)")
    tb_s5_l = s5.shapes.add_textbox(Inches(35 / 72), Inches(124 / 72), Inches(305 / 72), Inches(136 / 72))
    s5_l_items = [
        ("Kísérleti elvigazolás (M1): ", "A BME Polimertechnika Tanszék és a Danimer laboratóriumaiban kis méretű próbatesteken igazoltuk a módosított PHA/PHBH termoformálhatósági elvét."),
        ("Meglévő mérési bázis: ", "Előzetes DSC, TGA és kapilláris reológiai görbék, valamint alapanyag-tisztasági vizsgálatok."),
        ("Feloldandó korlát: ", "A nyers PHA lassú kristályosodásának és szűk termikus ablakának ipari léptékű áthidalása.")
    ]
    populate_text_box(tb_s5_l, s5_l_items, font_size=8.8, bullet=True, space_after=3.0)

    create_card(s5, 370, 96, 325, 168, title="Célállapot: TRL 6/7 (Ipari & Üzemi Demonstráció)")
    tb_s5_r = s5.shapes.add_textbox(Inches(380 / 72), Inches(124 / 72), Inches(305 / 72), Inches(136 / 72))
    s5_r_items = [
        ("TRL 6 Ipari Pilot (M36, MS3): ", "A MOL ipari koextrudáló során 0,40 mm-es 5-rétegű bio-barrier síkfólia gyártása, az ALFA többfészkes temperált szerszámában történő mélyhúzás és 100 000 db kapszula legyártása (D3.2)."),
        ("TRL 7 Üzemi Validáció (M44–M48): ", "A 100 000 db-os tétel 400 db/perc automata töltősori üzemeltetése (PackCoffee), barista tesztelése és akkreditált EN 13432 / NF T51-800 igazolása (D4.1, M44)."),
        ("RIA kompatibilitás: ", "A 100 000 db nem kereskedelmi eladás, hanem statisztikai folyamatképesség (Cpk > 1,33) és EN 13432 mintaszükséglet.")
    ]
    populate_text_box(tb_s5_r, s5_r_items, font_size=8.8, bullet=True, space_after=3.0)

    fig5 = make_fig_slide5_trl_roadmap()
    add_fig_to_slide(s5, fig5, 25, 270, 670, 244)

    # =========================================================================
    # SLIDE 6: Kiválóság - Piaci Probléma és Statisztikák (Layout 1 + Chart)
    # =========================================================================
    s6 = setup_content_slide(6, "Kiválóság", "1.1 Célkitűzések és ambíciók – A piaci probléma és hulladékstatisztikák")
    create_card(s6, 25, 96, 325, 238, title="A Globális és EU Hulladékprobléma Dimenziója")
    tb_s6_l = s6.shapes.add_textbox(Inches(35 / 72), Inches(124 / 72), Inches(305 / 72), Inches(204 / 72))
    s6_l_items = [
        ("~53 milliárd db/év az EU-ban (WUR-becslés, 2023): ", "Az egyadagos kávékapszulák piaca évi ~7–8,5%-kal bővül (Straits Research, Sci. Rep. 2020), a használt kapszuláknak azonban csak mintegy negyedét gyűjtik vissza (NL, WUR 2025)."),
        ("~75% nem kerül visszagyűjtésre (>10 milliárd db/év): ", "A kapszulában maradó nedves, olajos kávézacc miatt a mechanikai válogatás gazdaságtalan, így a kommunális vegyes kukába, égetőbe vagy lerakóba kerülnek."),
        ("Drasztikus erőforrás-pazarlás: ", "1 kg primer alumínium előállítása bauxitból globális átlagban ~15 kg CO₂e kibocsátással jár (IAI, 2022) egyetlen 30 másodperces kávéfőzésért.")
    ]
    populate_text_box(tb_s6_l, s6_l_items, font_size=8.8, bullet=True, space_after=3.5)

    create_card(s6, 370, 96, 325, 238, title="Szigorodó EU Szabályozás (PPWR, SUP & EPR)")
    tb_s6_r = s6.shapes.add_textbox(Inches(380 / 72), Inches(124 / 72), Inches(305 / 72), Inches(204 / 72))
    s6_r_items = [
        ("EU PPWR Rendelet (2025/40, alkalmazás: 2026. aug. 12.): ", "A rendelet kifejezetten nevesíti a kávékapszulákat; a merev, nem fém kapszulák komposztálhatóságát a tagállamok előírhatják (9. cikk (2) a))."),
        ("SUP Irányelv és PFAS tilalom: ", "Az egyszer használatos fosszilis műanyagok és fluorozott záróbevonatok kivezetése az élelmiszercsomagolásból."),
        ("MOHU EPR díjak és bio-hulladék gyűjtés: ", "A nem komposztálható kapszulák EPR díjai drasztikusan nőnek, míg a PHACK kapszula a barna kukába dobva biometánná és humusszá alakul.")
    ]
    populate_text_box(tb_s6_r, s6_r_items, font_size=8.8, bullet=True, space_after=3.5)

    fig6 = make_fig_slide6_waste_and_lca()
    add_fig_to_slide(s6, fig6, 25, 340, 670, 174)

    # =========================================================================
    # SLIDE 7: Kiválóság - Miért a PHA a Jövő Anyaga? (Layout 1)
    # =========================================================================
    s7 = setup_content_slide(7, "Kiválóság", "1.1 Anyagválasztás – Miért a PHA a jövő anyaga? (PHA vs. PLA összehasonlítás)")
    t7_shape = s7.shapes.add_table(6, 4, Inches(25 / 72), Inches(96 / 72), Inches(670 / 72), Inches(240 / 72))
    t7 = t7_shape.table
    t7.columns[0].width = Inches(135 / 72)
    t7.columns[1].width = Inches(160 / 72)
    t7.columns[2].width = Inches(170 / 72)
    t7.columns[3].width = Inches(205 / 72)
    t7_data = [
        ["Szempont / Tulajdonság", "Hagyományos Al / PP", "PLA (Politejsav)", "PHACK – Módosított PHA / PHBH"],
        ["Alapanyag eredete", "Fosszilis kőolaj / Bauxit bányászat", "Ipari kukorica (élelmiszerrel verseng)", "100% bio-hulladék (UCO, melasz – bakteriális szintézis)"],
        ["Hőállóság kávéfőzéskor", "Kiváló (>150°C), de energiaigényes", "Nem megfelelő (Tg ≈ 55–60°C [55–65°C], meglágyul)", "Kiváló (HDT > 95–105°C, 120°C-ig stabil, 93±2°C / 15–19 bar)"],
        ["Lebomlási képesség", "Nem bomlik le (több száz év)", "Csak ipari komposztálóban (>58°C); biogázban nem bomlik", "Házi komposzt (20–30°C, 6–12 hó, NF T51-800), biogáz (30–45 nap) és víz"],
        ["Gáz- és aromazárás (OTR)", "Kiváló OTR, de zacc miatt nem hasznosul", "Gyenge OTR (extra védőtasak kell)", "5-rétegű bio-barrier: OTR < 0,05 cm³/(kapszula·nap·bar)"],
        ["Életciklus CO₂e (LCA)", "Primer Al: ~15 kg CO₂e/kg (IAI 2022), kapszula ~1 g", "WUR 2023: a komposztálható kapszula GWP-je kissé az Al alatt van", "Cél: ≥25% CO₂e-csökkentés az Al-hoz képest (WP4 LCA)"]
    ]
    for r_idx, row in enumerate(t7_data):
        for c_idx, val in enumerate(row):
            t7.cell(r_idx, c_idx).text = val
    style_table(t7, font_size=8.6)

    fig7 = make_fig_slide7_biodeg_comparison()
    add_fig_to_slide(s7, fig7, 25, 344, 670, 170)

    # =========================================================================
    # SLIDE 8: Kiválóság - Technológiai Módszertan (Layout 1 + Flow Diagram)
    # =========================================================================
    s8 = setup_content_slide(8, "Kiválóság", "1.2 Műszaki és technológiai módszertan – A teljes K+F folyamatlánc")
    steps_data = [
        ("1. Baktériumos Fermentáció", "Danimer / Bio-on (IT)", "Mezőgazdasági melléktermékekből és UCO-ból nagy tisztaságú mikrobiális PHBH kopolimer bioszintézise."),
        ("2. Kétcsigás Kompoundálás", "BME & MOL (HU)", "Bio-nukleálószerek (orotinsav, talkum) és bio-lágyítók bekeverése a gyors kristályosodásért (<10 mp)."),
        ("3. Síkfólia Koextrúzió", "MOL Nyrt. (HU)", "0,40 mm (0,35–0,45 mm) vastag, 5-rétegű bio-barrier síkfólia (NFC/PGA maggal) gyártása ±3% tűréssel."),
        ("4. Temperált Termoformálás", "Alfa Industry (HU)", "Többfészkes, 60–70°C-ra temperált szerszámban precíziós mélyhúzás (<3,5 mp ciklusidő, ±0,1 mm)."),
        ("5. Töltés & UH Hegesztés", "PackCoffee Alliance (AT)", "Nagysebességű (400 db/perc) töltés, 20–35 kHz ultrahangos bio-fedőfólia hegesztés és barista teszt."),
        ("6. Biodegradáció és LCA", "RWTH Aachen (DE)", "Akkreditált EN 13432, NF T51-800 és ISO 14855 lebomlási tesztek, ökotoxicitás és ISO 14040/44 LCA.")
    ]
    for i, step in enumerate(steps_data):
        row = i // 3
        col = i % 3
        c_left = 25 + col * 228
        c_top = 96 + row * 158
        create_card(s8, c_left, c_top, 214, 150, title=step[0])
        tb_step = s8.shapes.add_textbox(Inches((c_left + 8) / 72), Inches((c_top + 26) / 72), Inches(198 / 72), Inches(120 / 72))
        step_items = [
            ("Partner: ", step[1]),
            ("Műszaki tartalom: ", step[2])
        ]
        populate_text_box(tb_step, step_items, font_size=8.8, bullet=True, space_after=3.0)

    fig8 = make_fig_slide8_process_chain()
    add_fig_to_slide(s8, fig8, 25, 414, 670, 100)

    # =========================================================================
    # SLIDE 9: Hatások - Igények és Célcsoportok (Layout 1)
    # =========================================================================
    s9 = setup_content_slide(9, "Hatások összefoglalása", "2.1 A projekt útjai a hatás eléréséhez – Specifikus igények és célcsoportok")
    t9_shape = s9.shapes.add_table(4, 3, Inches(25 / 72), Inches(96 / 72), Inches(670 / 72), Inches(260 / 72))
    t9 = t9_shape.table
    t9.columns[0].width = Inches(210 / 72)
    t9.columns[1].width = Inches(220 / 72)
    t9.columns[2].width = Inches(240 / 72)
    t9_data = [
        ["Specifikus Igények", "Várt Eredmények (KPI)", "Tervezett Projektintézkedések (WP-k)"],
        ["Kávépörkölők és márkák:\nMegfelelés a PPWR komposztálhatósági előírásainak milliárdos gépcsere nélkül.", "Drop-in Nespresso-kompatibilis (±0,1 mm) bio-kapszula; KPI 1: < +10% önköltség-prémium; KPI 4: OTR < 0,05 cm³/(kapszula·nap·bar).", "Meglévő 400 db/perc sebességű töltősorokon futtatható kapszulageometria és 20–35 kHz ultrahangos hegesztés (WP3)."],
        ["Csomagolóipari gyártók (KKV-k):\nHőstabil, gyorsan kristályosodó granulátum nagyüzemi mélyhúzáshoz.", "Termoformálási ciklusidő < 3,5 mp, falvastagság-tűrés ±3% (0,40 mm), HDT > 95–105°C, zéró utózsugorodás.", "Orotinsavval nukleált PHA kompound receptúra és 60–70°C temperált szerszámtechnológia átadása (WP2, WP3)."],
        ["Fogyasztók és hulladékkezelők:\nEgyszerű, szétválasztás nélküli higiénikus komposztálhatóság.", "KPI 3: > 90% lebomlás házi komposztban (<12 hó, NF T51-800) és ipari/biogázüzemben (<6 hó, EN 13432), zéró mikroműanyag.", "„Hová dobjam?” lakossági edukációs kampány és akkreditált komposztálhatósági tanúsítás (WP4, WP5)."]
    ]
    for r_idx, row in enumerate(t9_data):
        for c_idx, val in enumerate(row):
            t9.cell(r_idx, c_idx).text = val
    style_table(t9, font_size=8.6)

    create_card(s9, 25, 364, 670, 150, title="Rendszerszintű Ipari és Jogszabályi Illeszkedés (EU Green Deal & PPWR)")
    tb_c9 = s9.shapes.add_textbox(Inches(35 / 72), Inches(392 / 72), Inches(650 / 72), Inches(116 / 72))
    c9_items = [
        ("Drop-in technológiai transzfer (CAPEX-mentes átállás): ", "A kávépörkölőknek és csomagolóüzemeknek nem kell új töltősorokat vásárolniuk: a PHACK kapszula közvetlenül kiváltja az alumínium és PP kapszulákat."),
        ("Másodlagos bio-nyersanyagok valorizációja: ", "A projekt élelmiszerláncot nem veszélyeztető mezőgazdasági melléktermékeket (melasz, használt sütőolaj – UCO) kapcsol össze a magas hozzáadott értékű csomagolóiparral.")
    ]
    populate_text_box(tb_c9, c9_items, font_size=9.2, bullet=True, space_after=4.5)

    # =========================================================================
    # SLIDE 10: Hatások - Környezeti, Gazdasági, Társadalmi (Layout 1)
    # =========================================================================
    s10 = setup_content_slide(10, "Hatások összefoglalása", "2.1 A projekt útjai a hatás eléréséhez – Célcsoportok, kimenetelek és hatások")
    t10_shape = s10.shapes.add_table(4, 3, Inches(25 / 72), Inches(96 / 72), Inches(670 / 72), Inches(260 / 72))
    t10 = t10_shape.table
    t10.columns[0].width = Inches(195 / 72)
    t10.columns[1].width = Inches(230 / 72)
    t10.columns[2].width = Inches(245 / 72)
    t10_data = [
        ["Érintett Célcsoport", "Projekt Kimenetel (KPI)", "Hosszú Távú Rendszerszintű Hatás (KPI)"],
        ["Környezet és Klímavédelem:\nEurópai ökoszisztéma és talajok.", "KPI 2: > 2% piaci penetráció (évi >500 millió bio-kapszula kiváltása és komposztálása a célrégióban 2030-ig).", "Évi ~500 tonna alumínium/műanyag kapszulahulladék megelőzése és KPI 3: ≥25% CO₂e lábnyom-csökkentés (ISO 14040/44)."],
        ["Csomagolóipari KKV-k és Ipar:\nKelet-közép-európai gyártóbázis.", "Szabadalmaztatott, méretnövelhető PHA kompound és koextrúziós/termoformálási know-how (KPI 1: < +10% önköltség).", "Önkormányzati lerakási díjak és EPR költségek drasztikus csökkentése; 120 új zöld munkahely."],
        ["Hulladékgazdálkodók (MOHU):\nKomposztáló és biogázüzemek.", "Zaccos kapszulák közvetlen barna kukás gyűjtése, utóválogatás nélkül (KPI 3: > 90% biodegradáció).", "Tiszta szerves frakció: értékes nitrogén-, foszfor- és káliumdús humusz és magasabb biometán-hozam."]
    ]
    for r_idx, row in enumerate(t10_data):
        for c_idx, val in enumerate(row):
            t10.cell(r_idx, c_idx).text = val
    style_table(t10, font_size=8.8)

    create_card(s10, 25, 364, 670, 150, title="Mérhető Ökológiai, Gazdasági és Társadalmi Hasznok")
    tb_c10 = s10.shapes.add_textbox(Inches(35 / 72), Inches(392 / 72), Inches(650 / 72), Inches(116 / 72))
    c10_items = [
        ("Talajszerkezet-javítás és tápanyag-visszapótlás: ", "A kávézacc értékes N-P-K (nitrogén, foszfor, kálium) tápanyagforrás, amely a PHA kapszulával együtt elbomolva táplálja a talaj mikroflóráját."),
        ("Biogázüzemi szinergia (MOHU barna kuka): ", "Mezofil/termofil anaerob rothasztókban a PHA 30–45 nap alatt biometánná (CH₄) alakul, növelve a hazai megújuló energiatermelést.")
    ]
    populate_text_box(tb_c10, c10_items, font_size=9.2, bullet=True, space_after=4.5)

    # =========================================================================
    # SLIDE 11: Hatások - KPI Mutatók (Layout 1 - 100% Parity with Speech & Tests)
    # =========================================================================
    s11 = setup_content_slide(11, "Hatások összefoglalása", "2.1 Mérhető célértékek – A 4 kulcsfontosságú teljesítménymutató (KPI)")
    kpis = [
        ("< +10% Önköltség Prémium", "1. KPI: Versenyképes Gyártási Önköltség",
         "Az ipari méretnövelés (WP3) és a másodlagos szénforrások (UCO/melasz) révén az előállítási önköltség legfeljebb 10%-kal haladja meg a hagyományos kapszulákét (feltételezett PHA ár 2030-ra: 2,8–3,5 €/kg; EPR díjakkal teljes árparitás)."),
        ("> 2% Piaci Penetráció & ≥25% CO₂e", "2. KPI: Piaci Részesedés és Klímahatás",
         "A projekt zárását követő 2 éven belül legalább 2%-os piaci penetráció a közép-európai prémium szegmensben (100 000 db TRL 7 demonstráció után), ≥25% CO₂e megtakarítási céllal bölcsőtől-sírig (Cradle-to-Grave) ISO 14040/44 LCA szerint."),
        ("> 90% Lebomlás (<12 hó / <6 hó)", "3. KPI: Szabványos Házi és Ipari Komposztálhatóság",
         "Akkreditált EN 13432 és NF T51-800 szerinti >90%-os tömegveszteség és biodegradáció házi komposztban 12 hónapon (180–360 nap, 20–25°C [NF T51-800: 20–30°C]), ipari komposztálóban 6 hónapon (180 nap, 58°C) belül, zéró mikroműanyaggal."),
        ("OTR < 0,05 cm³/(kapszula·nap)", "4. KPI: Precíziós Oxigén- és Aromazárás",
         "5-rétegű koextrudált bio-barrier rétegrendszerrel (OTR < 0,05 cm³/(kapszula·nap·bar), WVTR < 1,0–2,0 g/(m²·nap)) biztosított 12 hónapos prémium kávé-aromastabilitás külső védőtasak nélkül.")
    ]
    for i, kpi in enumerate(kpis):
        row = i // 2
        col = i % 2
        c_left = 25 + col * 345
        c_top = 96 + row * 210
        create_card(s11, c_left, c_top, 330, 202, title=kpi[1])

        tb_stat = s11.shapes.add_textbox(Inches((c_left + 10) / 72), Inches((c_top + 28) / 72), Inches(310 / 72), Inches(34 / 72))
        p_stat = tb_stat.text_frame.paragraphs[0]
        p_stat.text = kpi[0]
        set_font(p_stat.runs[0], size=19.0, bold=True, color=COLOR_BME_BLUE)

        tb_desc = s11.shapes.add_textbox(Inches((c_left + 8) / 72), Inches((c_top + 66) / 72), Inches(172 / 72), Inches(132 / 72))
        populate_text_box(tb_desc, [kpi[2]], font_size=8.6, bullet=False, max_size=10.5)

        add_fig_to_slide(s11, make_fig_kpi(i + 1), c_left + 182, c_top + 68, 140, 128)

    # =========================================================================
    # SLIDE 12: Hatások - Ismeretterjesztési Terv (Layout 1)
    # =========================================================================
    s12 = setup_content_slide(12, "Ismeretterjesztési terv", "2.2 A hatás maximalizálását célzó intézkedések – Ismeretterjesztés és nyílt tudomány")
    pillars = [
        ("1. Q1 Publikációk és Konferenciák", [
            ("5+ db Q1 Gold Open Access cikk: ", "Publikálás a BME és RWTH közös kutatásaiból vezető folyóiratokban (Polymer Degradation and Stability, ACS Sustainable Chemistry & Engineering, Packaging Technology)."),
            ("Nemzetközi konferenciák: ", "Előadások a Biopolymer Summit, SPE ANTEC és European Bioplastics konferenciákon."),
            ("Féléves ipari workshopok: ", "Gyakorlati bemutatók európai csomagolóipari mérnököknek és kávépörkölőknek.")
        ]),
        ("2. Nyílt Tudomány (Open Science & FAIR)", [
            ("Nyílt Anyagadatbázis: ", "A PHA/PHBH reológiai, kristályosodási és biodegradációs mérési adatsorainak publikálása az EU Open Research / Zenodo repozitóriumban."),
            ("FAIR alapelvek: ", "Findable, Accessible, Interoperable, Reusable kutatási adatok a teljes konzorciumban."),
            ("Adatkezelési Terv (DMP): ", "A WP5 keretében a 6. hónaptól élő, folyamatosan frissített Data Management Plan."),
            ("Nemi dimenzió: ", "Kiegyensúlyozott nemi arány a WP-vezetésben és a kutatócsoportokban; a kommunikáció nemtől függetlenül szólítja meg a háztartásokat."),
            ("Interdiszciplinaritás: ", "Polimerkémia, feldolgozástechnika, mikrobiológia, LCA és szabályozás együttműködése a 6 lépéses láncban.")
        ]),
        ("3. Európai Szabványosítás (CEN)", [
            ("CEN/TC 249 munkacsoport: ", "Aktív szakértői részvétel az európai műanyagipari és bio-csomagolási szabványosítási bizottságban."),
            ("NF T51-800 harmonizáció: ", "Módszertani javaslatok a házi komposztálhatósági és biogázüzemi vizsgálati szabványok összeurópai egységesítésére."),
            ("IPR és Know-how védelem: ", "Európai szabadalmi bejelentés (EPO) a nukleált PHA kompoundra a publikálás előtt."),
            ("Hasznosítás és versenytársak: ", "A kompound és a gyártástechnológia átadása pörkölőknek és csomagolóknak (9. dia); versenytárs termékek: alumínium- és PLA-kapszulák (7. dia).")
        ])
    ]
    for i, pil in enumerate(pillars):
        c_left = 25 + i * 228
        create_card(s12, c_left, 96, 214, 418, title=pil[0])
        tb_pil = s12.shapes.add_textbox(Inches((c_left + 8) / 72), Inches(126 / 72), Inches(198 / 72), Inches(380 / 72))
        populate_text_box(tb_pil, pil[1], font_size=9.2, bullet=True, space_after=6.0)

    # =========================================================================
    # SLIDE 13: Hatások - Kommunikációs Terv (Layout 1)
    # =========================================================================
    s13 = setup_content_slide(13, "Kommunikációs terv", "2.2 A hatás maximalizálását célzó intézkedések – Célközönségek és kommunikációs csatornák")
    t13_shape = s13.shapes.add_table(5, 4, Inches(25 / 72), Inches(96 / 72), Inches(670 / 72), Inches(268 / 72))
    t13 = t13_shape.table
    t13.columns[0].width = Inches(155 / 72)
    t13.columns[1].width = Inches(175 / 72)
    t13.columns[2].width = Inches(225 / 72)
    t13.columns[3].width = Inches(115 / 72)
    t13_data = [
        ["Célközönség", "Kommunikációs Csatorna", "Tartalom és Fő Üzenet", "Becsült Közönségméret"],
        ["Fogyasztók és Lakosság:\nKávéfogyasztó háztartások", "Többnyelvű weboldal, közösségi média, „Hová dobjam?” videók", "Házi komposztálási és barna kukás útmutató, zöldmosás elleni edukáció", "> 500 000 fő / év\n(EU & HU lakosság)"],
        ["Kávépörkölők és Csomagolók:\nEurópai élelmiszeripar", "Szakmai kiállítások (World of Coffee, Interpack), mintacsomagok", "Drop-in Nespresso-kompatibilitás, OTR < 0,05 és ciklusidő < 3,5 mp", "50+ európai pörkölő\nés 150+ KKV"],
        ["Szabályozók és Döntéshozók:\nEU, minisztériumok, MOHU", "Szakpolitikai tájékoztatók (Policy Briefs), CEN kerekasztalok", "EU PPWR 9. cikk végrehajtása, EN 13432 / NF T51-800 EPR díjkedvezmény", "25+ szakpolitikai\nés hatósági szerv"],
        ["Egyetemi Hallgatók (MSc/PhD):\nA jövő mérnökgenerációja", "BME és RWTH MSc tananyagok, laborgyakorlatok, TDK/diplomák", "Biopolimer kompoundálás, 5-rétegű koextrúzió és ISO 14040 LCA", "300+ mérnökhallgató\n(BME & RWTH)"]
    ]
    for r_idx, row in enumerate(t13_data):
        for c_idx, val in enumerate(row):
            t13.cell(r_idx, c_idx).text = val
    style_table(t13, font_size=8.8)

    create_card(s13, 25, 372, 670, 142, title="A „Hová dobjam?” Edukációs Kampány és a Zöldmosás (Greenwashing) Elleni Fellépés")
    tb_c13 = s13.shapes.add_textbox(Inches(35 / 72), Inches(400 / 72), Inches(650 / 72), Inches(108 / 72))
    c13_items = [
        ("Szelektív gyűjtési tévhitek felszámolása: ", "A lakosság gyakran a sárga (műanyag) kukába dobja a biopolimereket, szennyezve a PET/PP újrahasznosítást. Kampányunk piktogramokkal és time-lapse lebomlási videókkal irányítja a kapszulát a barna kukába vagy kerti komposztba."),
        ("Policy Briefs a döntéshozóknak: ", "Tudományos alapú javaslatcsomagok a környezetvédelmi minisztériumoknak és a MOHU-nak az EN 13432 / NF T51-800 tanúsított PHA csomagolások EPR-díjkedvezményéhez.")
    ]
    populate_text_box(tb_c13, c13_items, font_size=9.0, bullet=True, space_after=4.0)

    # =========================================================================
    # SLIDE 14: Megvalósítás - Munkacsomagok Struktúrája (Layout 1 + PERT Chart)
    # =========================================================================
    s14 = setup_content_slide(14, "Megvalósítás", "Táblázat 3.1a Munkacsomagok áttekintő listája")
    t14_shape = s14.shapes.add_table(7, 7, Inches(25 / 72), Inches(96 / 72), Inches(670 / 72), Inches(238 / 72))
    t14 = t14_shape.table
    t14.columns[0].width = Inches(52 / 72)
    t14.columns[1].width = Inches(280 / 72)
    t14.columns[2].width = Inches(62 / 72)
    t14.columns[3].width = Inches(76 / 72)
    t14.columns[4].width = Inches(72 / 72)
    t14.columns[5].width = Inches(64 / 72)
    t14.columns[6].width = Inches(64 / 72)
    t14_data = [
        ["WP #", "Munkacsomag Címe", "Fő résztv. #", "Vezető", "Emberhónap", "Kezdő hó", "Befejező hó"],
        ["WP 1", "Igényfelmérés, alapanyag specifikáció és szabályozás", "4",         "RWTH", "68 PM", "M1", "M12"],
                ["WP 2", "PHA kompoundálás és termoformálható receptúrafejlesztés", "1", "BME", "144 PM", "M6", "M24"],
                ["WP 3", "Síkfólia koextrúzió és kísérleti termoformálás (100k db)", "2", "MOL", "136 PM", "M18", "M36"],
                ["WP 4", "Biodegradáció, élelmiszerbiztonság és LCA elemzés", "4", "RWTH", "96 PM", "M24", "M44"],
                ["WP 5", "Projektmenedzsment, IPR, disszemináció és hasznosítás", "1", "BME", "76 PM", "M1", "M48"],
                ["Összesen", "Teljes Konzorciumi Kutatói és Mérnöki Ráfordítás", "1–6", "BME (Koord.)", "520 PM", "M1", "M48"]
    ]
    for r_idx, row in enumerate(t14_data):
        for c_idx, val in enumerate(row):
            t14.cell(r_idx, c_idx).text = val
    style_table(t14, font_size=8.6, max_font=9.0)

    fig14 = make_fig_slide14_pert()
    add_fig_to_slide(s14, fig14, 25, 340, 670, 174)

    # =========================================================================
    # SLIDE 15: Megvalósítás - WP1 és WP2 Részletei (Layout 1 + Table 3.1b + Chart)
    # =========================================================================
    def add_wp_table_31b(slide, left_pt, top_pt, width_pt, height_pt, col0_w_pt, rows_data, base_font=7.8, max_font=8.8):
        t_shape = slide.shapes.add_table(
            len(rows_data), 2,
            Inches(left_pt / 72), Inches(top_pt / 72),
            Inches(width_pt / 72), Inches(height_pt / 72)
        )
        tbl = t_shape.table
        tbl.columns[0].width = Inches(col0_w_pt / 72)
        tbl.columns[1].width = Inches((width_pt - col0_w_pt) / 72)
        for r_idx, (k_txt, v_txt) in enumerate(rows_data):
            tbl.cell(r_idx, 0).text = k_txt
            tbl.cell(r_idx, 1).text = v_txt
        fs = style_table(tbl, font_size=base_font, max_font=max_font)
        for r_idx in range(1, len(rows_data)):
            c0 = tbl.cell(r_idx, 0)
            c0.fill.solid()
            c0.fill.fore_color.rgb = COLOR_CARD_TITLE_BG
            for p in c0.text_frame.paragraphs:
                for run in p.runs:
                    set_font(run, size=fs, bold=True, color=COLOR_BME_NAVY)
            c1 = tbl.cell(r_idx, 1)
            raw_lines = rows_data[r_idx][1].split("\n")
            tf1 = c1.text_frame
            tf1.clear()
            tf1.word_wrap = True
            tf1.vertical_anchor = MSO_ANCHOR.MIDDLE
            tf1.margin_left = tf1.margin_right = Inches(4 / 72)
            tf1.margin_top = tf1.margin_bottom = Inches(2 / 72)
            for l_i, line in enumerate(raw_lines):
                p = tf1.paragraphs[0] if l_i == 0 else tf1.add_paragraph()
                p.space_after = Pt(1.5)
                if ":" in line and (line.startswith("▸") or line.startswith("T") or line.startswith("D")):
                    head, tail = line.split(":", 1)
                    r0 = p.add_run()
                    r0.text = head + ":"
                    set_font(r0, size=fs, bold=True, color=COLOR_BME_NAVY)
                    _append_rich_runs(p, tail, fs, base_color=COLOR_DARK_TEXT, hl_color=COLOR_BME_BLUE)
                else:
                    _append_rich_runs(p, line, fs, base_color=COLOR_DARK_TEXT, hl_color=COLOR_BME_BLUE)
        return tbl

    s15 = setup_content_slide(15, "Megvalósítás", "Táblázat 3.1b Munkacsomagok részletei – WP1 és WP2 (Alapanyag és Kompoundálás)")
    wp1_rows = [
        ("Táblázat 3.1b – WP1", "WP1: Igényfelmérés, specifikáció és szabályozás (M1–M12 | 68 PM)"),
        ("Vezető & Résztvevők", "Vezető: 4-RWTH (26 PM) | Partnerek: 1-BME (18), 2-MOL (8), 3-ALFA (6), 5-BIO (6), 6-PCOFF (4)"),
        ("Célok (Objectives)", "Nespresso-kompatibilis gépi tűrések (±0,1 mm), nyers PHA/PHBH tisztasági és EU 10/2011 + PPWR előírások rögzítése."),
        ("Feladatok (T1.1–T1.3)", "▸ T1.1 Gépi és extrakciós tűrések: 400 db/perc töltősori tűrés (±0,1 mm), 90–95°C (93±2°C), 15–19 bar (PackCoffee).\n▸ T1.2 Nyers PHA audit (GPC/NMR): Mikrobiális PHA/PHBH tételek molekulatömeg- és tisztasági vizsgálata (Danimer/BIO).\n▸ T1.3 Jogszabályi megfelelés: EU 10/2011 migrációs (<10 mg/dm²) és EU PPWR 9. cikk (2) a) komposztálhatósági audit."),
        ("Eredmény & Mérföldkő", "D1.1 Követelményspecifikáció (M12, R, PU) ➔ MS1 mérföldkő (M12)")
    ]
    add_wp_table_31b(s15, 25, 96, 325, 266, 86, wp1_rows, base_font=7.6, max_font=8.4)

    wp2_rows = [
        ("Táblázat 3.1b – WP2", "WP2: PHA kompoundálás és receptúrafejlesztés (M6–M24 | 144 PM)"),
        ("Vezető & Résztvevők", "Vezető: 1-BME (78 PM) | Partnerek: 2-MOL (30), 5-BIO (14), 4-RWTH (12), 3-ALFA (10)"),
        ("Célok (Objectives)", "Hőstabil (HDT > 95–105°C, Tm > 140°C), gyorsan kristályosodó (t₁/₂ < 8 mp) PHA/PHBH kompound kifejlesztése."),
        ("Feladatok (T2.1–T2.3)", "▸ T2.1 Orotinsavas nukleálás: 0,5–1,0% orotinsav, talkum és citrát bio-lágyítók szűrése (HDT > 95–105°C).\n▸ T2.2 Kétcsigás kompoundálás: Alacsony nyírású csigaprofil (165–175°C) a β-eliminációs bomlás megelőzésére.\n▸ T2.3 Reológia & DSC/TGA/DMA: Kristályosodási kinetika (t₁/₂ < 8 mp); 50 kg granulátum és 1 000 db labor kapszula."),
        ("Eredmény & Mérföldkő", "D2.1 PHA kompound receptúra (M24, R, PU) ➔ MS2 mérföldkő (M24)")
    ]
    add_wp_table_31b(s15, 370, 96, 325, 266, 86, wp2_rows, base_font=7.6, max_font=8.4)

    fig15 = make_fig_slide15_wp12_kinetics()
    add_fig_to_slide(s15, fig15, 25, 368, 670, 146)

    # =========================================================================
    # SLIDE 16: Megvalósítás - WP3 Részletei (Layout 1 + Table 3.1b + Diagram)
    # =========================================================================
    s16 = setup_content_slide(16, "Megvalósítás", "Táblázat 3.1b Munkacsomagok részletei – WP3 (Síkfólia koextrúzió és termoformálás)")
    wp3_rows = [
        ("Táblázat 3.1b – Munkacsomag", "WP3: Síkfólia koextrúzió, temperált termoformálás és töltősori pilot (M18–M36 | 136 PM)"),
        ("Vezető & Résztvevők (PM)", "Vezető: 2-MOL Nyrt. (56 PM) | Partnerek: 3-ALFA (56 PM), 1-BME (12 PM), 6-PCOFF (8 PM), 5-BIO (4 PM) – Összesen: 136 PM"),
        ("Célok (Objectives)", "0,40 mm-es 5-rétegű bio-barrier síkfólia (OTR < 0,05) ipari koextrúziója, <3,5 mp ciklusidejű temperált termoformálás és 100 000 db kapszula pilot gyártása (TRL 6)."),
        ("Munkaleírás és feladatok\n(T3.1 – T3.3)", "▸ T3.1 5-rétegű bio-barrier síkfólia koextrúziója (MOL): 0,40 mm (380–400 µm, ±3% tűrés) síkfólia gyártása (PHA 180 µm / Bio-Tie 15 µm / Nanocellulóz vagy PGA barrier 20 µm / Bio-Tie 15 µm / PHA 150 µm) temperált chill-roll hengerekkel.\n▸ T3.2 Temperált szerszámos precíziós termoformálás (ALFA): Többfészkes, 60–70°C-ra temperált termoformáló szerszám tervezése és mélyhúzás (<3,5 mp ciklusidő, ±0,1 mm kamratűrés, utózsugorodás-mentes kristályosítás).\n▸ T3.3 100 000 db-os demonstrációs gyártás és UH hegesztés (PackCoffee): 100 000 db kapszula ipari próbatöltése (400 db/perc) és 20–35 kHz-es ultrahangos bio-fedőfólia hegesztése."),
        ("Eredmények & Mérföldkő", "D3.1 Koextrúziós és termoformálási protokoll (M36, R, SEN) | D3.2 100 000 db demonstrációs kapszula (M36, DEM, PU) ➔ MS3 (M36)")
    ]
    add_wp_table_31b(s16, 25, 96, 670, 238, 128, wp3_rows, base_font=8.0, max_font=8.9)

    fig16 = make_fig_slide16_wp3_architecture()
    add_fig_to_slide(s16, fig16, 25, 340, 670, 174)

    # =========================================================================
    # SLIDE 17: Megvalósítás - WP4 és WP5 Részletei (Layout 1 + Table 3.1b)
    # =========================================================================
    s17 = setup_content_slide(17, "Megvalósítás", "Táblázat 3.1b Munkacsomagok részletei – WP4 és WP5 (Validáció és Menedzsment)")
    wp4_rows = [
        ("Táblázat 3.1b – WP4", "WP4: Biodegradáció, élelmiszerbiztonság és LCA elemzés (M24–M44 | 96 PM)"),
        ("Vezető & Résztvevők", "Vezető: 4-RWTH Aachen (42 PM) | Partnerek: 5-BIO (18 PM), 6-PCOFF (16 PM), 3-ALFA (12 PM), 1-BME (8 PM)"),
        ("Fő célkitűzés\n(Objectives)", "Akkreditált ipari (EN 13432), házi (NF T51-800) és biogázüzemi lebonthatósági tanúsítás, OECD 208 ökotoxikológia, EU 10/2011 migráció és bölcsőtől-sírig ISO 14040/44 LCA (TRL 7)."),
        ("Munkaleírás és feladatok\n(T4.1 – T4.3)", "▸ T4.1 Biodegradáció (EN 13432, NF T51-800, ISO 14855): Respirometriás CO₂-fejlődés és dezintegráció mérése házi komposztban (20–25°C [NF T51-800: 20–30°C], <12 hó), ipari komposztban (58°C, <6 hó) és anaerob biogázüzemben (30–45 nap).\n▸ T4.2 Ökotoxikológia és élelmiszer-migráció: OECD 208 csíranövény- és földigiliszta-toxicitási tesztek a kávézaccos komposzton; EU 10/2011 kioldódási vizsgálat (<10 mg/dm²) 95°C/19 bar extrakció után.\n▸ T4.3 Teljes ISO 14040/14044 LCA: Bölcsőtől-sírig (Cradle-to-Grave) szén-dioxid lábnyom számítás (cél: ≥25% CO₂e csökkenés az alumínium kapszulához képest)."),
        ("Szállítandó eredmények\n(Deliverables)", "D4.1 Akkreditált biodegradációs és ökotoxicitási jelentés (M44, R, PU)\nD4.2 Teljes bölcsőtől-sírig ISO 14040/44 LCA hatástanulmány (M44, R, PU)")
    ]
    add_wp_table_31b(s17, 25, 96, 325, 418, 88, wp4_rows, base_font=8.0, max_font=8.9)

    wp5_rows = [
        ("Táblázat 3.1b – WP5", "WP5: Projektmenedzsment, IPR, disszemináció és hasznosítás (M1–M48 | 76 PM)"),
        ("Vezető & Résztvevők", "Vezető: 1-BME (28 PM, Koord.) | Partnerek: 4-RWTH (16 PM), 6-PCOFF (12 PM), 5-BIO (8 PM), 2-MOL (6 PM), 3-ALFA (6 PM)"),
        ("Fő célkitűzés\n(Objectives)", "A konzorcium operatív, pénzügyi és jogi irányítása (40 PM), minőségbiztosítás, IPR védelem, szabványosítás és tudományos/lakossági disszemináció (36 PM)."),
        ("Munkaleírás és feladatok\n(T5.1 – T5.3)", "▸ T5.1 Konzorciumi irányítás és minőségbiztosítás: Steering Committee negyedéves ülések, Horizon Europe pénzügyi jelentések, etikai és Stage-Gate (MS1–MS3) monitoring.\n▸ T5.2 Szellemi tulajdon (IPR) és üzleti hasznosítás: Konzorciumi megállapodás (CA), közös európai szabadalom (EPO) a nukleált PHA kompoundra és licencmodell kidolgozása.\n▸ T5.3 Disszemináció, képzés és „Hová dobjam?” kampány: Projekt weboldal, FAIR DMP, 5 db Q1 Open Access publikáció, CEN/TC 249 szabványosítás, MSc tananyag és lakossági edukáció."),
        ("Szállítandó eredmények\n(Deliverables)", "D5.1 Honlap, DMP és disszeminációs terv (M6, DEC, PU)\nD5.2 Záró technikai, IPR és pénzügyi jelentés (M48, R, PU)")
    ]
    add_wp_table_31b(s17, 370, 96, 325, 418, 88, wp5_rows, base_font=8.0, max_font=8.9)

    # =========================================================================
    # SLIDE 18: Megvalósítás - Mérföldkövek (Layout 1)
    # =========================================================================
    s18 = setup_content_slide(18, "Megvalósítás", "Táblázat 3.1d Mérföldkövek listája")
    t18_shape = s18.shapes.add_table(4, 5, Inches(25 / 72), Inches(96 / 72), Inches(670 / 72), Inches(238 / 72))
    t18 = t18_shape.table
    t18.columns[0].width = Inches(75 / 72)
    t18.columns[1].width = Inches(220 / 72)
    t18.columns[2].width = Inches(65 / 72)
    t18.columns[3].width = Inches(75 / 72)
    t18.columns[4].width = Inches(235 / 72)
    t18_data = [
        ["Mérföldkő #", "Mérföldkő Megnevezése", "WP #", "Határidő", "Ellenőrzési Eszközök"],
        ["MS1", "Élelmiszeripari követelményrendszer és végleges alapanyag-specifikáció", "WP1", "12. hónap (M12)", "Elfogadott D1.1 követelményspecifikációs jelentés, igazolt EU 10/2011 alapanyag-tisztaság és ±0,1 mm gépi tűrések."],
        ["MS2", "Optimalizált PHA kompound és 1 000 db laboratóriumi kapszula", "WP2", "24. hónap (M24)", "50 kg kompound granulátum (D2.1), sikeres DSC/HDT (>95°C) mérések és az első 1 000 db működőképes labor kapszula."],
        ["MS3", "100 000 db ipari prototípus gyártása és előzetes EN 13432 audit", "WP3, WP4", "36. hónap (M36)", "100 000 db legyártott kapszula (D3.2), 400 db/perc töltősori jegyzőkönyv (OTR < 0,05) és sikeres EN 13432 előzetes audit."]
    ]
    for r_idx, row in enumerate(t18_data):
        for c_idx, val in enumerate(row):
            t18.cell(r_idx, c_idx).text = val
    style_table(t18, font_size=8.8)

    create_card(s18, 25, 344, 670, 170, title="Go / No-Go Kaputechnológiai Minőségbiztosítás")
    tb_c18 = s18.shapes.add_textbox(Inches(35 / 72), Inches(372 / 72), Inches(650 / 72), Inches(136 / 72))
    c18_items = [
        ("Szigorú Go/No-Go döntési kapuk: ", "Minden mérföldkő (MS1: M12, MS2: M24, MS3: M36) műszaki és pénzügyi kapuként szolgál. A költséges ipari szerszámozás és nagysorozatú extrúzió csak az MS2 laboratóriumi prototípusok (1 000 db) sikeres nyomáspróbája után indul el."),
        ("Teljes visszakövethetőség: ", "A mérföldkövek közvetlenül kapcsolódnak a szerződéses deliverable-ökhöz (D1.1 ➔ MS1; D2.1 ➔ MS2; D3.1/D3.2 ➔ MS3), biztosítva a kockázatmentes TRL 3 ➔ TRL 7 előrehaladást.")
    ]
    populate_text_box(tb_c18, c18_items, font_size=9.2, bullet=True, space_after=4.5)

    # =========================================================================
    # SLIDE 19: Megvalósítás - Eredmények / Deliverables (All 8 Deliverables D1.1-D5.2)
    # =========================================================================
    s19 = setup_content_slide(19, "Megvalósítás", "Táblázat 3.1c Eredmények listája (D1.1 – D5.2)")
    t19_shape = s19.shapes.add_table(9, 7, Inches(25 / 72), Inches(96 / 72), Inches(670 / 72), Inches(276 / 72))
    t19 = t19_shape.table
    t19.columns[0].width = Inches(50 / 72)
    t19.columns[1].width = Inches(265 / 72)
    t19.columns[2].width = Inches(48 / 72)
    t19.columns[3].width = Inches(67 / 72)
    t19.columns[4].width = Inches(80 / 72)
    t19.columns[5].width = Inches(85 / 72)
    t19.columns[6].width = Inches(75 / 72)
    t19_data = [
        ["Kód", "Szállítandó Eredmény Megnevezése", "WP", "Vezető", "Típus", "Hozzáférés", "Határidő"],
        ["D1.1", "Csomagolási, gépészeti és élelmiszerbiztonsági követelményspecifikáció", "WP1", "RWTH", "Jelentés (R)", "Nyilvános (PU)", "M12"],
        ["D2.1", "Optimalizált PHA/PHBH kompound receptúra és reológiai jegyzőkönyv", "WP2", "BME", "Jelentés (R)", "Nyilvános (PU)", "M24"],
        ["D3.1", "5-rétegű bio-barrier síkfólia koextrúziós és termoformálási protokoll", "WP3", "MOL", "Jelentés (R)", "Bizalmas (SEN)", "M36"],
        ["D3.2", "100 000 db demonstrációs kapszula prototípus és barista töltősori audit", "WP3", "ALFA", "Prototípus (DEM)", "Nyilvános (PU)", "M36"],
        ["D4.1", "Akkreditált biodegradációs (EN 13432, NF T51-800) és ökotoxicitási jelentés", "WP4", "RWTH", "Jelentés (R)", "Nyilvános (PU)", "M44"],
        ["D4.2", "Teljes bölcsőtől-sírig (Cradle-to-Grave) ISO 14040/44 LCA hatástanulmány", "WP4", "RWTH", "Jelentés (R)", "Nyilvános (PU)", "M44"],
        ["D5.1", "Projekt weboldal, Adatkezelési Terv (DMP) és disszeminációs stratégia", "WP5", "BME", "Web/Terv (DEC)", "Nyilvános (PU)", "M6"],
        ["D5.2", "Záró technikai, IPR hasznosítási és pénzügyi összefoglaló jelentés", "WP5", "BME", "Jelentés (R)", "Nyilvános (PU)", "M48"]
    ]
    for r_idx, row in enumerate(t19_data):
        for c_idx, val in enumerate(row):
            t19.cell(r_idx, c_idx).text = val
    style_table(t19, font_size=8.0)

    create_card(s19, 25, 380, 670, 134, title="Nyílt Tudomány (PU) és Ipari Know-how Védelem (SEN) Egyensúlya")
    tb_c19 = s19.shapes.add_textbox(Inches(35 / 72), Inches(408 / 72), Inches(650 / 72), Inches(100 / 72))
    c19_items = [
        ("Teljes szerződéses lefedettség (8 kulcs deliverable): ", "A tudományos, biodegradációs (D4.1) és LCA (D4.2) eredmények nyilvánosak (PU), míg a MOL és ALFA gyártási finomhangolási paraméterei (D3.1) bizalmasak (SEN) az európai ipari versenyelőny védelmében."),
        ("Színpadi átadás (19 ➔ 20. dia): ", "A kritikus műszaki és piaci kockázatok (R1–R3) ismertetésére innovációs felelősünk, Hallgató 4 tér vissza.")
    ]
    populate_text_box(tb_c19, c19_items, font_size=8.9, bullet=True, space_after=3.5)

    # =========================================================================
    # SLIDE 20: Megvalósítás - Kockázatkezelési Mátrix (Layout 1)
    # =========================================================================
    s20 = setup_content_slide(20, "Megvalósítás", "Táblázat 3.1e Kritikus kockázatok a megvalósítás során")
    t20_shape = s20.shapes.add_table(4, 5, Inches(25 / 72), Inches(96 / 72), Inches(670 / 72), Inches(182 / 72))
    t20 = t20_shape.table
    t20.columns[0].width = Inches(48 / 72)
    t20.columns[1].width = Inches(192 / 72)
    t20.columns[2].width = Inches(62 / 72)
    t20.columns[3].width = Inches(93 / 72)
    t20.columns[4].width = Inches(275 / 72)
    t20_data = [
        ["Kód", "Kritikus Szakmai / Piaci Kockázat Leírása", "WP #", "Valósz. / Súly.", "Konkrét Kockázatcsökkentő Intézkedés (Mitigáció)"],
        ["R1", "A PHA termikus degradációja (β-elimináció) és szűk feldolgozási ablaka (165–180°C)", "WP2, WP3", "Közepes / Magas", "Természetes hőstabilizátorok, PHBH kopolimer és bio-lágyítók alkalmazása; alacsony nyírású csigageometria és szigorú olvadékhőmérséklet-szabályozás."],
        ["R2", "Gáz- és aromazárási hiányosságok vagy delamináció a mélyhúzott falrészeken", "WP3, WP4", "Közepes / Közepes", "5-rétegű koextrúzió Bio-Tie tapadórétegekkel és NFC/PGA barrier maggal; temperált (60–70°C) szerszám és folyamatos OTR (<0,05) ellenőrzés."],
        ["R3", "Másodlagos kristályosodás vagy az alapanyag-árprémium miatti piaci ellenállás", "WP2, WP5", "Alacsony / Közepes", "Orotinsavas nukleálás a szerszámban történő teljes kristályosításhoz (±0,1 mm); UCO/melasz szénforrás, méretgazdaságosság (<+10%) és PPWR jogszabályi kényszer."]
    ]
    for r_idx, row in enumerate(t20_data):
        for c_idx, val in enumerate(row):
            t20.cell(r_idx, c_idx).text = val
    style_table(t20, font_size=8.5)

    fig20 = make_fig_slide20_risk_heatmap()
    add_fig_to_slide(s20, fig20, 25, 286, 270, 228)

    create_card(s20, 305, 286, 390, 108, title="Kettős barrier tartalék (R2) és kockázatfigyelés")
    tb_r20a = s20.shapes.add_textbox(Inches(313 / 72), Inches(312 / 72), Inches(374 / 72), Inches(80 / 72))
    populate_text_box(tb_r20a, [
        ("Tartalék-barrier: ", "az 5-rétegű szerkezet NFC és PGA barrier magja egymás tartaléka; delamináció vagy OTR-túllépés esetén a másik réteg megtartja a 0,05 cm³/(kapszula·nap) célt."),
        ("Korai jelzés: ", "folyamatos OTR-ellenőrzés minden WP3 gyártási tételen."),
    ], font_size=8.8, bullet=True, space_after=3.0)

    create_card(s20, 305, 402, 390, 112, title="Negyedéves Steering Committee ellenőrzés")
    tb_r20b = s20.shapes.add_textbox(Inches(313 / 72), Inches(428 / 72), Inches(374 / 72), Inches(84 / 72))
    populate_text_box(tb_r20b, [
        ("Kockázatnapló: ", "a Steering Committee negyedévente felülvizsgálja a valószínűség/súly értékeket és a mitigációs intézkedéseket."),
        ("Eszkaláció: ", "a kritikus kockázatokat a Hallgató 4 felügyeli, és a Hallgató 6 felé továbbítja döntésre."),
    ], font_size=8.8, bullet=True, space_after=3.0)

    # =========================================================================
    # SLIDE 21: Megvalósítás - Gantt Ütemterv (Layout 1)
    # =========================================================================
    s21 = setup_content_slide(21, "Megvalósítás", "3.1 A megvalósítás minősége és hatékonysága – 48 hónapos Gantt ütemterv")
    t21_shape = s21.shapes.add_table(6, 5, Inches(25 / 72), Inches(94 / 72), Inches(670 / 72), Inches(198 / 72))
    t21 = t21_shape.table
    t21.columns[0].width = Inches(230 / 72)
    t21.columns[1].width = Inches(110 / 72)
    t21.columns[2].width = Inches(110 / 72)
    t21.columns[3].width = Inches(110 / 72)
    t21.columns[4].width = Inches(110 / 72)

    headers_gantt = ["Munkacsomag & Részfeladatok (T1.1–T5.3)", "1. Év (M1 – M12)", "2. Év (M13 – M24)", "3. Év (M25 – M36)", "4. Év (M37 – M48)"]
    for c, h in enumerate(headers_gantt):
        t21.cell(0, c).text = h
    style_table(t21, font_size=8.2, max_font=9.4)

    gantt_rows = [
        ("WP1: Specifikáció & Szabályozás (RWTH, 68 PM)\nT1.1 Tűrések · T1.2 PHA audit · T1.3 PPWR", [("ACTIVE", "M1–M12: T1.1–T1.3\n➔ D1.1 & MS1"), ("NONE", "–"), ("NONE", "–"), ("NONE", "–")]),
        ("WP2: PHA Kompoundálás (BME, 144 PM)\nT2.1 Nukleálás · T2.2 Extrúzió · T2.3 50 kg/1k db", [("PLAN", "M6–M12: T2.1–T2.2"), ("ACTIVE", "M13–M24: T2.2–T2.3\n➔ D2.1 & MS2"), ("NONE", "–"), ("NONE", "–")]),
        ("WP3: Síkfólia & Termoformálás (MOL/ALFA, 136 PM)\nT3.1 5-rétegű fólia · T3.2 Szerszám · T3.3 100k db", [("NONE", "–"), ("PLAN", "M18–M24: T3.1–T3.2"), ("ACTIVE", "M25–M36: T3.1–T3.3\n➔ D3.1–3.2 & MS3"), ("NONE", "–")]),
        ("WP4: Biodegradáció & LCA (RWTH, 96 PM)\nT4.1 EN 13432 · T4.2 Migráció · T4.3 LCA", [("NONE", "–"), ("NONE", "–"), ("PLAN", "M24–M36: T4.1–T4.2"), ("ACTIVE", "M37–M44: T4.1–T4.3\n➔ D4.1 & D4.2")]),
        ("WP5: Menedzsment & Disszemináció (BME, 76 PM)\nT5.1 Irányítás · T5.2 IPR/EPO · T5.3 Q1/CEN", [("ACTIVE", "T5.1 & T5.3\n➔ D5.1 (M6)"), ("ACTIVE", "T5.1–T5.3:\nIPR & EPO"), ("ACTIVE", "T5.1–T5.3:\nCEN & Workshop"), ("ACTIVE", "T5.1–T5.3\n➔ D5.2 (M48)")])
    ]

    for r_idx, (wp_title, quarters) in enumerate(gantt_rows, 1):
        cell0 = t21.cell(r_idx, 0)
        cell0.text = wp_title
        cell0.fill.solid()
        cell0.fill.fore_color.rgb = COLOR_CARD_TITLE_BG
        for p_idx, p in enumerate(cell0.text_frame.paragraphs):
            for r in p.runs:
                set_font(r, size=8.4 if p_idx == 0 else 7.6, bold=(p_idx == 0), color=COLOR_BME_NAVY if p_idx == 0 else COLOR_DARK_TEXT)

        for q_idx, (status, label) in enumerate(quarters, 1):
            cell = t21.cell(r_idx, q_idx)
            cell.text = label
            cell.fill.solid()
            tf = cell.text_frame
            tf.vertical_anchor = MSO_ANCHOR.MIDDLE
            for p in tf.paragraphs:
                p.alignment = PP_ALIGN.CENTER
                for r in p.runs:
                    if status == "ACTIVE":
                        cell.fill.fore_color.rgb = COLOR_BME_NAVY
                        set_font(r, size=8.2, bold=True, color=COLOR_WHITE)
                    elif status == "PLAN":
                        cell.fill.fore_color.rgb = COLOR_GANTT_PLAN
                        set_font(r, size=8.2, bold=True, color=COLOR_BME_NAVY)
                    else:
                        cell.fill.fore_color.rgb = COLOR_ROW_ALT
                        set_font(r, size=8.2, bold=False, color=COLOR_MUTED_TEXT)

    fig21 = make_fig_slide21_gantt_timeline()
    add_fig_to_slide(s21, fig21, 25, 298, 670, 216)

    # =========================================================================
    # SLIDE 22: Megvalósítás - Költségvetés és Erőforrások (100% Parity + Chart)
    # =========================================================================
    s22 = setup_content_slide(22, "A projekt költségei",     "Konzorciumi költségvetés (4,2M EUR) és Táblázat 3.1f Emberi erőforrás megoszlás (520 PM)")
    create_card(s22, 25, 96, 325, 244, title="Költségvetési kategóriák és indoklás (4,2M EUR)")
    t22_l_shape = s22.shapes.add_table(7, 3, Inches(31 / 72), Inches(124 / 72), Inches(313 / 72), Inches(210 / 72))
    t22_l = t22_l_shape.table
    t22_l.columns[0].width = Inches(105 / 72)
    t22_l.columns[1].width = Inches(34 / 72)
    t22_l.columns[2].width = Inches(174 / 72)
    t22_l_data = [
        ["Költségkategória", "Arány", "Összeg (€) & Indoklás (Sablon 14. dia)"],
        ["Személyi jellegű költségek", "50%", "2 080 000 € (520 PM × 4 000 €/PM kutatói és mérnöki bér)"],
        ["Utazás és ellátás", "3%", "130 000 € (8 konzorciumi ülés, 6 EU konferencia, pilot-utak)"],
        ["Felszerelés / Eszközök", "16%", "670 000 € (5-rétegű fej, 60–70°C szerszám, UH-fej amortizáció)"],
        ["Egyéb áru, munka, szolgáltatás", "11%", "480 000 € (2,5 t PHA, EN 13432 audit, logisztikai alvállalkozás)"],
        ["Indirekt költség (25% átalány)", "20%", "840 000 € (HE 25% rezsiátalány a 3,36M € közvetlen költségre)"],
        ["Összesen (100% EU RIA)", "100%", "4 200 000 € (4,2M EUR – 100% EU finanszírozás)"]
    ]
    for r_idx, row in enumerate(t22_l_data):
        for c_idx, val in enumerate(row):
            t22_l.cell(r_idx, c_idx).text = val
    style_table(t22_l, font_size=7.6, max_font=8.6)

    create_card(s22, 358, 96, 337, 244, title="Táblázat 3.1f Emberi erőforrás (PM / WP) és büdzsé")
    t22_r_shape = s22.shapes.add_table(8, 8, Inches(364 / 72), Inches(124 / 72), Inches(325 / 72), Inches(200 / 72))
    t22_r = t22_r_shape.table
    col_w22 = [58, 30, 30, 30, 30, 30, 45, 72]
    for c_i, w_val in enumerate(col_w22):
        t22_r.columns[c_i].width = Inches(w_val / 72)
    t22_r_data = [
        ["Partner", "WP1", "WP2", "WP3", "WP4", "WP5", "Össz. PM", "Büdzsé (€)"],
        ["1. BME (HU)", "18", "78", "12", "8", "28", "144 PM", "1 050 000 €"],
        ["2. MOL (HU)", "8", "30", "56", "–", "6", "100 PM", "850 000 €"],
        ["3. ALFA (HU)", "6", "10", "56", "12", "6", "90 PM", "650 000 €"],
        ["4. RWTH (DE)", "26", "12", "–", "42", "16", "96 PM", "750 000 €"],
        ["5. BIO (IT)", "6", "14", "4", "18", "8", "50 PM", "550 000 €"],
        ["6. PCOFF (AT)", "4", "–", "8", "16", "12", "40 PM", "350 000 €"],
        ["Összesen", "68", "144", "136", "96", "76", "520 PM", "4 200 000 €"]
    ]
    for r_idx, row in enumerate(t22_r_data):
        for c_idx, val in enumerate(row):
            t22_r.cell(r_idx, c_idx).text = val
    style_table(t22_r, font_size=8.0, max_font=8.2)
    for row in t22_r.rows:
        for cell in row.cells:
            cell.text_frame.margin_left = cell.text_frame.margin_right = Inches(2 / 72)

    fig22 = make_fig_slide22_budget()
    add_fig_to_slide(s22, fig22, 25, 344, 670, 170)

    # =========================================================================
    # SLIDE 23: Csoporttagok (Layout 1 - GY02)
    # =========================================================================
    s23 = setup_content_slide(23, "Csoporttagok", "Hallgatói munkamegosztás és Horizon Europe szerepkörök")
    t23_shape = s23.shapes.add_table(7, 4, Inches(25 / 72), Inches(96 / 72), Inches(670 / 72), Inches(315 / 72))
    t23 = t23_shape.table
    t23.columns[0].width = Inches(28 / 72)
    t23.columns[1].width = Inches(162 / 72)
    t23.columns[2].width = Inches(85 / 72)
    t23.columns[3].width = Inches(395 / 72)
    t23_data = [
        ["#", "Csoporttag Neve", "Neptun-kód", "Elvégzett Feladat és Horizon Europe Szerepkör (Előadott Diák & Időkeret)"],
        ["1", "Hallgató 1 (Koordinátor)", "NEPTUN1", "Project Coordinator (Coord): Alapadatok, célkitűzések, 6 fős nemzetközi konzorcium és értéklánc felépítése (1–3. dia | 90 mp)"],
        ["2", "Hallgató 2 (K+F 1)", "NEPTUN2", "Research & Dev 1 (RD1): Anyagtudományi koncepció, TRL 3 ➔ 7 ugrás, PHA vs. PLA mátrix és 6 lépéses gyártástechnológia (4–8. dia | 160 mp)"],
        ["3", "Hallgató 3 (K+F 2)", "NEPTUN3", "Research & Dev 2 (RD2): Munkacsomagok (WP1–WP5, 520 PM), kompoundálás, 5-rétegű koextrúzió, termoformálás és LCA (14–17. dia | 120 mp)"],
        ["4", "Hallgató 4 (Innováció)", "NEPTUN4", "Innovation & Exploitation (Innov): Piaci igények (PPWR), társadalmi hatások, 4 fő KPI és kritikus kockázatok mátrixa (9–11. és 20. dia | 150 mp)"],
        ["5", "Hallgató 5 (Disszemináció)", "NEPTUN5", "Dissemination & Communication (Dissz): 5 db Q1 publikáció, nyílt tudomány (FAIR), CEN szabványosítás, „Hová dobjam?” kampány (12–13. dia | 80 mp)"],
        ["6", "Hallgató 6 (Pénzügy)", "NEPTUN6", "Management & Finance (Fin): MS1–MS3 mérföldkövek, D1.1–D5.2 eredmények, 4 éves Gantt, 4,2M EUR büdzsé és zárszó (18–19. és 21–24. dia | 120 mp)"]
    ]
    for r_idx, row in enumerate(t23_data):
        for c_idx, val in enumerate(row):
            t23.cell(r_idx, c_idx).text = val
    style_table(t23, font_size=8.4)

    create_card(s23, 25, 420, 670, 94, title="Tantárgyi, Csoport és Prezentációs Adatok")
    tb_c23 = s23.shapes.add_textbox(Inches(35 / 72), Inches(446 / 72), Inches(650 / 72), Inches(62 / 72))
    c23_items = [
        ("Kurzus: ", "BMEGEPTNX01 / BMEGEPTMSVFEHU-01 Fenntartható hulladékgazdálkodás | BME Gépészmérnöki Kar, Polimertechnika Tanszék"),
        ("Csoport és Időkeret: ", "GY02 gyakorlat, P01 projekttéma | 24 dia (pontosan 12:00 perc / 720 mp előadás + 3:00 perc bírálói vitablokk) | Dátum: 2026.11.12.")
    ]
    populate_text_box(tb_c23, c23_items, font_size=9.0, bullet=False, space_after=3.0)

    # =========================================================================
    # SLIDE 24: Összefoglalás és kérdések (Layout 11: Záróoldal)
    # =========================================================================
    s24 = prs.slides.add_slide(prs.slide_layouts[11])
    for sh in list(s24.shapes):
        sp = sh._element
        sp.getparent().remove(sp)

    tb_num24 = s24.shapes.add_textbox(Inches(620 / 72), Inches(25 / 72), Inches(75 / 72), Inches(22 / 72))
    p_num24 = tb_num24.text_frame.paragraphs[0]
    p_num24.alignment = PP_ALIGN.RIGHT
    p_num24.text = "24/24"
    set_font(p_num24.runs[0], size=11.5, bold=True, color=COLOR_CYAN)

    tb_close = s24.shapes.add_textbox(Inches(50 / 72), Inches(125 / 72), Inches(620 / 72), Inches(65 / 72))
    p_close = tb_close.text_frame.paragraphs[0]
    p_close.alignment = PP_ALIGN.CENTER
    p_close.text = "Köszönjük szépen a figyelmet!"
    set_font(p_close.runs[0], size=32, bold=True, color=COLOR_WHITE)

    tb_motto = s24.shapes.add_textbox(Inches(50 / 72), Inches(198 / 72), Inches(620 / 72), Inches(65 / 72))
    tb_motto.text_frame.word_wrap = True
    p_motto = tb_motto.text_frame.paragraphs[0]
    p_motto.alignment = PP_ALIGN.CENTER
    p_motto.text = "„PHACK – Fenntartható és biológiailag 100%-ban lebomló kávékapszula a jövő körforgásos gazdaságáért.”"
    set_font(p_motto.runs[0], size=15, bold=True, color=COLOR_CYAN)

    create_card(s24, 60, 282, 600, 110, bg_color=RGBColor(255, 255, 255), border_color=COLOR_CYAN)
    tb_qa = s24.shapes.add_textbox(Inches(72 / 72), Inches(286 / 72), Inches(576 / 72), Inches(102 / 72))
    tb_qa.text_frame.word_wrap = True
    tb_qa.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
    qa_p1 = tb_qa.text_frame.paragraphs[0]
    qa_p1.alignment = PP_ALIGN.CENTER
    qa_p1.text = "Várjuk a tisztelt Bírálóbizottság és a Hallgatóság kérdéseit!"
    set_font(qa_p1.runs[0], size=17, bold=True, color=COLOR_BME_NAVY)

    qa_p2 = tb_qa.text_frame.add_paragraph()
    qa_p2.alignment = PP_ALIGN.CENTER
    qa_p2.space_before = Pt(8)
    qa_p2.text = "HORIZON-CL6-2026-CIRCBIO (RIA) | 4,2M EUR | 520 PM | TRL 3 ➔ TRL 7 | 100 000 db Prototípus"
    set_font(qa_p2.runs[0], size=11.5, bold=True, color=COLOR_BME_BLUE)

    qa_p3 = tb_qa.text_frame.add_paragraph()
    qa_p3.alignment = PP_ALIGN.CENTER
    qa_p3.space_before = Pt(6)
    qa_p3.text = "Prezentáció időtartama: pontosan 12:00 perc (720 mp) | Szakmai vitablokk: 3:00 perc (GY02)"
    set_font(qa_p3.runs[0], size=11, bold=False, color=COLOR_DARK_TEXT)

    embed_note(s24, slides_data[23])

    print("Saving presentation to:", output_path)
    prs.save(output_path)
    print("Presentation saved successfully with 24 slides!")
    return output_path


def render_slides_to_png(pptx_path):
    """Exports all 24 slides to high-resolution 1280x960 PNG images via PowerPoint COM with retry logic."""
    import time
    import shutil
    import tempfile
    render_dir = os.path.join(BASE_DIR, "slides_rendered")
    os.makedirs(render_dir, exist_ok=True)
    try:
        import win32com.client
        # Copy PPTX to local temp directory before opening in PowerPoint to avoid OneDrive lock/callee rejection
        tmp_dir = tempfile.mkdtemp(prefix="phack_ppt_")
        tmp_pptx = os.path.join(tmp_dir, "PHACK_Prezentacio_Vegleges.pptx")
        shutil.copy2(pptx_path, tmp_pptx)

        def com_retry(fn, retries=15, delay=0.4):
            for attempt in range(retries):
                try:
                    return fn()
                except Exception:
                    if attempt == retries - 1:
                        raise
                    time.sleep(delay)

        ppt = com_retry(lambda: win32com.client.Dispatch("PowerPoint.Application"))
        pres = com_retry(lambda: ppt.Presentations.Open(tmp_pptx, ReadOnly=True, Untitled=False, WithWindow=False))
        try:
            count = com_retry(lambda: pres.Slides.Count)
            for idx in range(1, count + 1):
                out_png = os.path.abspath(os.path.join(render_dir, f"slide_{idx:02d}.png"))
                com_retry(lambda i=idx, p=out_png: pres.Slides(i).Export(p, "PNG", 1280, 960))
            print(f"Rendered {count} slides to {render_dir} (1280x960 PNG).")
        finally:
            com_retry(lambda: pres.Close())
            shutil.rmtree(tmp_dir, ignore_errors=True)
    except Exception as e:
        print(f"Note: PowerPoint COM rendering skipped or failed: {e}")


if __name__ == "__main__":
    out = build_all_slides()
    render_slides_to_png(out)
