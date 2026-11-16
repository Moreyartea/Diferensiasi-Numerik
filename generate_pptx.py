import os
import io
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image

# Presentation generator script for Diferensiasi Numerik (Metode Numerik)
from pptx import Presentation  # type: ignore
from pptx.util import Inches, Pt  # type: ignore
from pptx.dml.color import RGBColor  # type: ignore
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR  # type: ignore
from pptx.enum.shapes import MSO_SHAPE  # type: ignore

def render_latex_image(latex_str, font_size=18, color='#1e3a8a'):
    """Renders LaTeX formula to a high-DPI transparent PNG buffer using matplotlib mathtext."""
    fig = plt.figure(figsize=(10, 2), dpi=300)
    fig.patch.set_alpha(0.0)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    ax.patch.set_alpha(0.0)
    if not (latex_str.startswith('$') and latex_str.endswith('$')):
        latex_str = f"${latex_str}$"
    ax.text(0.5, 0.5, latex_str, fontsize=font_size, ha='center', va='center', color=color)
    buf = io.BytesIO()
    plt.savefig(buf, format='png', transparent=True, bbox_inches='tight', pad_inches=0.04, dpi=300)
    plt.close(fig)
    buf.seek(0)
    im = Image.open(buf)
    w_px, h_px = im.size
    buf.seek(0)
    return buf, w_px, h_px

def generate_cover_illustration():
    """Generates a publication-quality curve and tangent line illustration for the cover slide."""
    fig, ax = plt.subplots(figsize=(5.2, 4.0), dpi=300)
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    x = np.linspace(0.4, 3.6, 200)
    y = np.sin(x - 0.4) * 1.5 + 2.0
    ax.plot(x, y, color='#1e3a8a', linewidth=3, label=r'$f(x)$')

    x0 = 1.6
    y0 = np.sin(x0 - 0.4) * 1.5 + 2.0
    slope = 1.5 * np.cos(x0 - 0.4)
    x_tangent = np.linspace(0.8, 2.6, 100)
    y_tangent = y0 + slope * (x_tangent - x0)
    ax.plot(x_tangent, y_tangent, color='#059669', linewidth=2.5, linestyle='--', label=r"Garis Singgung $f'(x_0)$")

    h = 0.9
    x1 = x0 + h
    y1 = np.sin(x1 - 0.4) * 1.5 + 2.0
    secant_slope = (y1 - y0) / h
    x_secant = np.linspace(1.1, 3.1, 100)
    y_secant = y0 + secant_slope * (x_secant - x0)
    ax.plot(x_secant, y_secant, color='#d97706', linewidth=2, linestyle=':', label=r'Beda Maju (Sekan)')

    ax.scatter([x0, x1], [y0, y1], color=['#059669', '#d97706'], s=75, zorder=5)
    ax.text(x0 - 0.1, y0 + 0.28, r'$(x_0, f(x_0))$', fontsize=10, fontweight='bold', color='#059669')
    ax.text(x1 - 0.15, y1 - 0.38, r'$(x_0+h, f(x_0+h))$', fontsize=10, fontweight='bold', color='#d97706')

    ax.axis('off')
    ax.legend(loc='upper left', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1', framealpha=0.95, fontsize=9.5)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', transparent=True, bbox_inches='tight', pad_inches=0.05, dpi=300)
    plt.close(fig)
    buf.seek(0)
    im = Image.open(buf)
    w_px, h_px = im.size
    buf.seek(0)
    return buf, w_px, h_px

def generate_error_bar_chart():
    """Generates an accurate horizontal bar chart for error reduction on Slide 20."""
    fig, ax = plt.subplots(figsize=(6.2, 2.1), dpi=300)
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    categories = ['Selisih Maju (h=0.10)', 'Selisih Maju (h=0.05)', 'Richardson N₂(0.10)']
    errors = [0.0148834, 0.0075761, 0.0002688]
    colors = ['#3b82f6', '#2563eb', '#059669']

    y_pos = np.arange(len(categories))
    bars = ax.barh(y_pos, errors, color=colors, height=0.52, edgecolor='#cbd5e1', linewidth=0.8)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories, fontsize=9, fontweight='bold', color='#1e293b')
    ax.invert_yaxis()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#cbd5e1')
    ax.spines['bottom'].set_color('#cbd5e1')
    ax.xaxis.grid(True, linestyle='--', alpha=0.5, color='#cbd5e1')
    ax.tick_params(axis='x', labelsize=8, colors='#64748b')

    for bar, err in zip(bars, errors):
        width = bar.get_width()
        text = f"{err:.7f}"
        if err < 0.001:
            text += " (28x lebih teliti! ★)"
        ax.text(width + 0.0003, bar.get_y() + bar.get_height()/2, text,
                va='center', ha='left', fontsize=8.5, fontweight='bold',
                color='#059669' if err < 0.001 else '#1e293b')

    ax.set_xlim(0, 0.0215)
    buf = io.BytesIO()
    plt.savefig(buf, format='png', transparent=True, bbox_inches='tight', pad_inches=0.05, dpi=300)
    plt.close(fig)
    buf.seek(0)
    im = Image.open(buf)
    w_px, h_px = im.size
    buf.seek(0)
    return buf, w_px, h_px

def create_presentation():
    prs = Presentation()
    # 16:9 widescreen dimensions: 13.333 x 7.5 inches
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6] # Blank slide layout

    # Color Palette: Minimalist White Theme
    COLOR_BG = RGBColor(255, 255, 255)
    COLOR_TEXT = RGBColor(15, 23, 42)      # Slate 900
    COLOR_MUTED = RGBColor(71, 85, 105)    # Slate 600
    COLOR_PRIMARY = RGBColor(30, 58, 138)  # Deep Navy Blue
    COLOR_PRIMARY_SOFT = RGBColor(239, 246, 255) # Blue 50
    COLOR_BLUE = RGBColor(37, 99, 235)     # Primary Blue
    COLOR_EMERALD = RGBColor(5, 150, 105)  # Emerald Green
    COLOR_AMBER = RGBColor(217, 119, 6)    # Amber 600
    COLOR_CARD = RGBColor(248, 250, 252)   # Slate 50
    COLOR_BORDER = RGBColor(226, 232, 240) # Slate 200
    COLOR_EMERALD_SOFT = RGBColor(236, 253, 245) # Emerald 50
    COLOR_AMBER_SOFT = RGBColor(254, 243, 199)   # Amber 100

    # Typography: Matching Web Inter & Mathematical Fonts
    FONT_MAIN = "Inter"
    FONT_MATH = "Cambria Math"
    FONT_MONO = "JetBrains Mono"

    def add_base_slide(cat_text, title_text, slide_num, notes_text=""):
        slide = prs.slides.add_slide(blank_layout)

        # White Background
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG
        bg.line.fill.background()

        # Header Box (Category & Title)
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(1.1))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0)
        tf.margin_bottom = Inches(0)
        tf.margin_left = Inches(0)
        tf.margin_right = Inches(0)

        # Category / Chapter indicator
        p_cat = tf.paragraphs[0]
        p_cat.text = cat_text.upper()
        p_cat.font.name = FONT_MAIN
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = COLOR_PRIMARY
        p_cat.space_after = Pt(4)

        # Slide Title
        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.name = FONT_MAIN
        p_title.font.size = Pt(24)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_TEXT

        # Footer Box (Divider + Attribution + Slide Number)
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(6.8), Inches(11.733), Inches(0.015))
        line.fill.solid()
        line.fill.fore_color.rgb = COLOR_BORDER
        line.line.fill.background()

        footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(6.85), Inches(11.733), Inches(0.4))
        ftf = footer_box.text_frame
        ftf.margin_top = Inches(0)
        ftf.margin_left = Inches(0)
        fp = ftf.paragraphs[0]
        fp.text = f"Metode Numerik — Imron dkk. (2022) | Slide {slide_num} dari 39"
        fp.font.name = FONT_MAIN
        fp.font.size = Pt(10)
        fp.font.color.rgb = COLOR_MUTED

        if notes_text:
            notes_slide = slide.notes_slide
            tf_notes = notes_slide.notes_text_frame
            tf_notes.text = notes_text

        return slide

    def add_callout_banner(slide, left, top, width, height, text, is_amber=False):
        banner = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        banner.fill.solid()
        banner.fill.fore_color.rgb = COLOR_AMBER_SOFT if is_amber else COLOR_EMERALD_SOFT
        banner.line.color.rgb = COLOR_AMBER if is_amber else COLOR_EMERALD
        banner.line.width = Pt(1.5)

        # Left accent stripe
        accent = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top + Inches(0.08), Inches(0.06), height - Inches(0.16))
        accent.fill.solid()
        accent.fill.fore_color.rgb = COLOR_AMBER if is_amber else COLOR_EMERALD
        accent.line.fill.background()

        tb = slide.shapes.add_textbox(left + Inches(0.22), top + Inches(0.08), width - Inches(0.44), height - Inches(0.16))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0)
        tf.margin_bottom = Inches(0)
        p = tf.paragraphs[0]
        p.text = text
        p.font.name = FONT_MAIN
        p.font.size = Pt(11)
        p.font.color.rgb = RGBColor(120, 53, 15) if is_amber else RGBColor(6, 78, 59)

    def add_custom_card(slide, left, top, width, height, title, items, border_color=None, bg_color=None, title_color=None, latex=None):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color if bg_color else COLOR_CARD
        card.line.color.rgb = border_color if border_color else COLOR_BORDER
        card.line.width = Pt(1.5 if border_color else 1)

        # Accent bar on left
        acc_col = border_color if border_color else (title_color if title_color else COLOR_PRIMARY)
        accent_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top + Inches(0.10), Inches(0.06), height - Inches(0.20))
        accent_bar.fill.solid()
        accent_bar.fill.fore_color.rgb = acc_col
        accent_bar.line.fill.background()

        items_top_offset = 0.12
        if title:
            tb_title = slide.shapes.add_textbox(left + Inches(0.22), top + Inches(0.10), width - Inches(0.44), Inches(0.35))
            tf_t = tb_title.text_frame
            tf_t.margin_top = Inches(0)
            tf_t.margin_bottom = Inches(0)
            tf_t.margin_left = Inches(0)
            p_title = tf_t.paragraphs[0]
            p_title.text = title
            p_title.font.name = FONT_MAIN
            p_title.font.size = Pt(13)
            p_title.font.bold = True
            p_title.font.color.rgb = title_color if title_color else COLOR_PRIMARY
            items_top_offset = 0.42

        if latex:
            buf, img_w, img_h = render_latex_image(latex, font_size=16, color='#1e3a8a')
            avail_w_in = (width / 914400.0) - 0.5
            avail_h_in = 0.65
            w_in = img_w / 300.0
            h_in = img_h / 300.0
            scale = min(avail_w_in / w_in, avail_h_in / h_in, 0.95)
            target_w_in = w_in * scale
            target_h_in = h_in * scale

            img_left = left + Inches(((width / 914400.0) - target_w_in) / 2)
            img_top = top + Inches(items_top_offset + 0.02)
            slide.shapes.add_picture(buf, img_left, img_top, Inches(target_w_in), Inches(target_h_in))
            items_top_offset += (target_h_in + 0.08)

        if items:
            rem_h = (height / 914400.0) - items_top_offset - 0.06
            tb_items = slide.shapes.add_textbox(left + Inches(0.22), top + Inches(items_top_offset), width - Inches(0.44), Inches(max(rem_h, 0.4)))
            tf_i = tb_items.text_frame
            tf_i.word_wrap = True
            tf_i.margin_top = Inches(0)
            tf_i.margin_bottom = Inches(0)
            tf_i.margin_left = Inches(0)
            tf_i.margin_right = Inches(0)

            for i, item in enumerate(items):
                p = tf_i.paragraphs[0] if i == 0 else tf_i.add_paragraph()
                p.text = item
                p.font.name = FONT_MAIN
                p.font.size = Pt(10)
                p.font.color.rgb = COLOR_TEXT
                p.space_after = Pt(2.5)

    def add_card(slide, left, top, width, height, title, items, badge="", accent_color=None):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD
        card.line.color.rgb = COLOR_BORDER
        card.line.width = Pt(1)

        # Left accent stripe
        chosen_accent = accent_color if accent_color else COLOR_PRIMARY
        accent_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top + Inches(0.12), Inches(0.06), height - Inches(0.24))
        accent_bar.fill.solid()
        accent_bar.fill.fore_color.rgb = chosen_accent
        accent_bar.line.fill.background()

        tb = slide.shapes.add_textbox(left + Inches(0.24), top + Inches(0.16), width - Inches(0.44), height - Inches(0.32))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0)
        tf.margin_bottom = Inches(0)
        tf.margin_left = Inches(0)
        tf.margin_right = Inches(0)

        p_title = tf.paragraphs[0]
        p_title.text = (f"[{badge}] " if badge else "") + title
        p_title.font.name = FONT_MAIN
        p_title.font.size = Pt(13.5)
        p_title.font.bold = True
        p_title.font.color.rgb = chosen_accent if accent_color else COLOR_PRIMARY
        p_title.space_after = Pt(6)

        for item in items:
            p = tf.add_paragraph()
            p.text = f"•  {item}"
            p.font.name = FONT_MAIN
            p.font.size = Pt(11)
            p.font.color.rgb = COLOR_TEXT
            p.space_after = Pt(4)

    def add_math_box(slide, left, top, width, height, label, math_text="", subtext="", latex=None, math_color='#1e3a8a'):
        box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        box.fill.solid()
        box.fill.fore_color.rgb = COLOR_CARD
        box.line.color.rgb = COLOR_BLUE
        box.line.width = Pt(1.5)

        accent_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top + Inches(0.08), Inches(0.06), height - Inches(0.16))
        accent_bar.fill.solid()
        accent_bar.fill.fore_color.rgb = COLOR_BLUE
        accent_bar.line.fill.background()

        tb_label = slide.shapes.add_textbox(left + Inches(0.25), top + Inches(0.10), width - Inches(0.5), Inches(0.35))
        tf_lbl = tb_label.text_frame
        tf_lbl.margin_top = Inches(0)
        tf_lbl.margin_bottom = Inches(0)
        p1 = tf_lbl.paragraphs[0]
        p1.text = label.upper()
        p1.font.name = FONT_MAIN
        p1.font.size = Pt(10)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_BLUE

        if latex:
            buf, img_w, img_h = render_latex_image(latex, font_size=18, color=math_color)
            avail_w_in = (width / 914400.0) - 0.5
            avail_h_in = (height / 914400.0) - (0.75 if subtext else 0.45)

            w_in = img_w / 300.0
            h_in = img_h / 300.0
            scale = min(avail_w_in / w_in, avail_h_in / h_in, 1.0)
            target_w_in = w_in * scale
            target_h_in = h_in * scale

            img_left = left + Inches(((width / 914400.0) - target_w_in) / 2)
            img_top = top + Inches(0.38 + (avail_h_in - target_h_in) / 2)
            slide.shapes.add_picture(buf, img_left, img_top, Inches(target_w_in), Inches(target_h_in))
        elif math_text:
            tb_m = slide.shapes.add_textbox(left + Inches(0.25), top + Inches(0.38), width - Inches(0.5), height - Inches(0.75 if subtext else 0.45))
            tf_m = tb_m.text_frame
            tf_m.word_wrap = True
            tf_m.margin_top = Inches(0)
            p2 = tf_m.paragraphs[0]
            p2.text = math_text
            p2.font.name = FONT_MATH
            p2.font.size = Pt(14)
            p2.font.bold = True
            p2.font.color.rgb = COLOR_TEXT
            p2.alignment = PP_ALIGN.CENTER

        if subtext:
            tb_sub = slide.shapes.add_textbox(left + Inches(0.25), top + height - Inches(0.38), width - Inches(0.5), Inches(0.3))
            tf_sub = tb_sub.text_frame
            tf_sub.margin_top = Inches(0)
            p3 = tf_sub.paragraphs[0]
            p3.text = subtext
            p3.font.name = FONT_MAIN
            p3.font.size = Pt(10)
            p3.font.color.rgb = COLOR_MUTED
            p3.alignment = PP_ALIGN.CENTER

    def add_table_data(slide, left, top, width, height, headers, rows, col_widths=None, best_row_indices=None):
        num_rows = len(rows) + 1
        num_cols = len(headers)
        table_shape = slide.shapes.add_table(num_rows, num_cols, left, top, width, height)
        table = table_shape.table

        for c_idx, h in enumerate(headers):
            cell = table.cell(0, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_PRIMARY
            p = cell.text_frame.paragraphs[0]
            p.text = str(h)
            p.font.name = FONT_MAIN
            p.font.bold = True
            p.font.size = Pt(11)
            p.font.color.rgb = RGBColor(255, 255, 255)
            p.alignment = PP_ALIGN.CENTER

        for r_idx, row in enumerate(rows):
            is_best = (best_row_indices and r_idx in best_row_indices) or any("⭐" in str(v) for v in row)
            for c_idx, val in enumerate(row):
                cell = table.cell(r_idx + 1, c_idx)
                cell.fill.solid()
                if is_best:
                    cell.fill.fore_color.rgb = COLOR_EMERALD_SOFT
                else:
                    cell.fill.fore_color.rgb = COLOR_BG if r_idx % 2 == 0 else COLOR_CARD

                p = cell.text_frame.paragraphs[0]
                p.text = str(val)
                p.font.name = FONT_MONO if any(ch.isdigit() for ch in str(val)) else FONT_MAIN
                p.font.size = Pt(10.5)
                if is_best:
                    p.font.bold = True
                    p.font.color.rgb = RGBColor(6, 78, 59)
                else:
                    p.font.color.rgb = COLOR_TEXT
                p.alignment = PP_ALIGN.CENTER

        if col_widths and len(col_widths) == num_cols:
            for c_idx, w in enumerate(col_widths):
                table.columns[c_idx].width = w

    # =========================================================================
    # SLIDE 1: COVER
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = COLOR_BG
    bg1.line.fill.background()

    notes_slide1 = s1.notes_slide
    tf_notes1 = notes_slide1.notes_text_frame
    tf_notes1.text = "Sapa audiens, sebut judul dan bab. Jelaskan bahwa hari ini kita membahas cara memperkirakan turunan fungsi hanya dari nilai-nilai fungsi. Gambar kurva dengan garis singgung mewakili ide utama: turunan adalah kemiringan garis singgung. Isi placeholder nama, dosen, dan program studi sebelum presentasi."

    bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.5), Inches(0.12), Inches(3.6))
    bar.fill.solid()
    bar.fill.fore_color.rgb = COLOR_PRIMARY
    bar.line.fill.background()

    tb1 = s1.shapes.add_textbox(Inches(1.1), Inches(1.3), Inches(7.2), Inches(2.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "METODE NUMERIK"
    p.font.name = FONT_MAIN
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLUE
    p.space_after = Pt(6)

    p2 = tf1.add_paragraph()
    p2.text = "DIFERENSIASI NUMERIK"
    p2.font.name = FONT_MAIN
    p2.font.size = Pt(40)
    p2.font.bold = True
    p2.font.color.rgb = COLOR_TEXT
    p2.space_after = Pt(6)

    p3 = tf1.add_paragraph()
    p3.text = "Pendekatan Nilai Turunan Fungsi melalui Polinomial Deret & Ekstrapolasi Richardson"
    p3.font.name = FONT_MAIN
    p3.font.size = Pt(14)
    p3.font.color.rgb = COLOR_MUTED

    meta_box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.1), Inches(4.1), Inches(7.0), Inches(2.6))
    meta_box.fill.solid()
    meta_box.fill.fore_color.rgb = COLOR_CARD
    meta_box.line.color.rgb = COLOR_BORDER
    mtf = meta_box.text_frame
    mtf.word_wrap = True

    mp0 = mtf.paragraphs[0]
    mp0.text = "ANGGOTA KELOMPOK:"
    mp0.font.name = FONT_MAIN
    mp0.font.size = Pt(11)
    mp0.font.bold = True
    mp0.font.color.rgb = COLOR_PRIMARY
    mp0.space_after = Pt(3)

    mp1 = mtf.add_paragraph()
    mp1.text = "1. Farel Luther Siagian (4253250041)       2. Fatih Taqiyyuddin (4253250057)\n3. Siti Zulayka Maulida Amali (4253250001)   4. Keegan Gibran Jehian (4253250029)"
    mp1.font.name = FONT_MAIN
    mp1.font.size = Pt(11)
    mp1.font.color.rgb = COLOR_TEXT
    mp1.space_after = Pt(8)

    mp2 = mtf.add_paragraph()
    mp2.text = "DOSEN PENGAMPU:"
    mp2.font.name = FONT_MAIN
    mp2.font.size = Pt(11)
    mp2.font.bold = True
    mp2.font.color.rgb = COLOR_PRIMARY
    mp2.space_after = Pt(2)

    mp3 = mtf.add_paragraph()
    mp3.text = "Debi Yandra Niska, S.Kom., M.Kom.    |    Tahun: 2026"
    mp3.font.name = FONT_MAIN
    mp3.font.size = Pt(11.5)
    mp3.font.bold = True
    mp3.font.color.rgb = COLOR_TEXT

    buf_cov, cov_w, cov_h = generate_cover_illustration()
    cov_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.3), Inches(1.4), Inches(4.3), Inches(5.3))
    cov_card.fill.solid()
    cov_card.fill.fore_color.rgb = COLOR_CARD
    cov_card.line.color.rgb = COLOR_BORDER
    cov_card.line.width = Pt(1)

    cov_target_w_in = 4.0
    cov_target_h_in = cov_target_w_in * (cov_h / cov_w)
    s1.shapes.add_picture(buf_cov, Inches(8.45), Inches(1.65), Inches(cov_target_w_in), Inches(cov_target_h_in))

    tb_cov = s1.shapes.add_textbox(Inches(8.4), Inches(5.95), Inches(4.1), Inches(0.6))
    tb_cov.text_frame.word_wrap = True
    p_cov = tb_cov.text_frame.paragraphs[0]
    p_cov.text = "Visualisasi: Garis singgung (turunan eksak) dihampiri oleh garis sekan (beda hingga)."
    p_cov.font.name = FONT_MAIN
    p_cov.font.size = Pt(9.5)
    p_cov.font.color.rgb = COLOR_MUTED
    p_cov.alignment = PP_ALIGN.CENTER

    # =========================================================================
    # SLIDE 2: PENGERTIAN DIFERENSIASI NUMERIK
    # =========================================================================
    s2 = add_base_slide("Pengantar", "Pengertian Diferensiasi Numerik", 2,
        "Turunan menyatakan laju perubahan. Kadang fungsi sulit diperoleh secara analitis eksak, atau data yang tersedia berupa tabel pengukuran diskret. Karena itu kita menggunakan pendekatan diferensiasi numerik. Bab ini memperkenalkan dua metode utama: pendekatan deret dan ekstrapolasi Richardson.")
    add_card(s2, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.7), "Pengertian", [
        "Memperkirakan nilai turunan fungsi f'(x) dari titik-titik diskret.",
        "Dipakai saat turunan analitis sulit diperoleh secara eksak.",
        "Metode utama saat data berupa tabel pengukuran eksperimen."
    ], "A", accent_color=COLOR_PRIMARY)
    add_card(s2, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.7), "Tujuan Utama", [
        "Memperkirakan laju perubahan sesaat pada sistem fisik/teknik.",
        "Menghitung turunan dari data tabel diskret tanpa rumus analitik.",
        "Membantu penyelesaian persamaan diferensial dan optimasi numerik."
    ], "B", accent_color=COLOR_BLUE)
    add_card(s2, Inches(8.8), Inches(1.8), Inches(3.733), Inches(4.7), "Analitis vs Numerik", [
        "Analitis: Hasil diferensiasi matematis formal menghasilkan fungsi kontinu eksak.",
        "Numerik: Hasil hampiran (pendekatan) bernilai numerik di titik spesifik.",
        "Memerlukan pemahaman atas galat hampiran (truncation & round-off error)."
    ], "C", accent_color=COLOR_EMERALD)

    # =========================================================================
    # SLIDE 3: APA KEGUNAAN DIFERENSIASI NUMERIK?
    # =========================================================================
    s3 = add_base_slide("Pengantar Fungsional", "Apa Kegunaan Diferensiasi Numerik?", 3,
        "Diferensiasi numerik membantu kita memperkirakan seberapa cepat suatu nilai berubah ketika data yang tersedia hanya berupa hasil pengukuran. Contohnya pada kecepatan dari posisi, percepatan dari kecepatan, atau gradien suhu. Kita tidak harus mengetahui persamaan fungsinya terlebih dahulu.")

    add_card(s3, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.3), "Contoh Penerapan Nyata", [
        "Posisi Kendaraan: Memperkirakan kecepatan (v = ds/dt) dari sensor GPS.",
        "Kecepatan Kendaraan: Menghitung percepatan (a = dv/dt) saat melaju.",
        "Perubahan Suhu: Melihat laju perpindahan panas (dT/dx) antar-posisi.",
        "Laju Reaksi: Memperkirakan perubahan konsentrasi zat terhadap waktu."
    ], "Aplikasi", accent_color=COLOR_PRIMARY)

    add_card(s3, Inches(6.8), Inches(1.8), Inches(5.733), Inches(4.3), "Kapan Diperlukan?", [
        "Data Tabel: Saat kita hanya memiliki data pengukuran eksperimen.",
        "Tanpa Rumus: Saat fungsi analitis tidak diketahui sama sekali.",
        "Fungsi Rumit: Saat persamaan analitis terlalu sulit diturunkan eksak.",
        "Prinsip Utama: Cukup gunakan perubahan nilai data untuk menghitung turunan!"
    ], "Urgensi", accent_color=COLOR_EMERALD)

    add_callout_banner(s3, Inches(0.8), Inches(6.25), Inches(11.733), Inches(0.48),
        "Intinya: Kita tidak harus mengetahui fungsi analitis terlebih dahulu. Diferensiasi numerik mengestimasi turunan langsung dari data.")

    # =========================================================================
    # SLIDE 4: MENGENAL DATA DAN TITIK YANG DIGUNAKAN
    # =========================================================================
    s4 = add_base_slide("Konsep Data", "Mengenal Data dan Titik yang Digunakan", 4,
        "Bayangkan kita mengukur posisi benda setiap 1 detik. Untuk mencari kecepatan di detik ke-2, kita perlu melihat data di sekitarnya. Titik yang dianalisis disebut x, jarak pengukuran disebut h, titik sebelumnya x-h, dan sesudahnya x+h.")

    add_table_data(s4, Inches(0.8), Inches(1.8), Inches(5.6), Inches(2.2),
        ["Waktu t (detik)", "Posisi s(t) (meter)", "Peran Titik"],
        [
            ["1", "1", "Titik sebelum (x − h)"],
            ["2", "8", "Titik evaluasi (x) ⭐"],
            ["3", "27", "Titik sesudah (x + h)"]
        ])

    add_custom_card(s4, Inches(0.8), Inches(4.2), Inches(5.6), Inches(1.9), "Cara Membacanya", [
        "Jika x = 2, maka f(x) adalah posisi pada detik ke-2, yaitu 8 meter.",
        "Jarak antar-pengukuran h = 1 detik (langkah tetap).",
        "Data di sekitar x = 2 menjadi dasar estimasi kecepatan."
    ], border_color=COLOR_BLUE, title_color=COLOR_BLUE)

    add_card(s4, Inches(6.8), Inches(1.8), Inches(5.733), Inches(4.3), "Memahami Notasi Titik & Langkah", [
        "x : Titik yang ingin dianalisis (misalnya x = 2 detik).",
        "h : Jarak antarwaktu pengukuran yang konstan (h = 1 detik).",
        "x − h : Titik satu langkah sebelum titik analisis (1 detik).",
        "x + h : Titik satu langkah setelah titik analisis (3 detik).",
        "f(x) : Nilai data pada titik analisis (s(2) = 8 meter)."
    ], "Notasi", accent_color=COLOR_PRIMARY)

    add_callout_banner(s4, Inches(0.8), Inches(6.25), Inches(11.733), Inches(0.48),
        "Kunci Perbedaan: Tiga metode diferensiasi numerik berbeda terutama pada data tetangga mana yang dipakai.")

    # =========================================================================
    # SLIDE 5: METODE SELISIH MAJU (FORWARD DIFFERENCE)
    # =========================================================================
    s5 = add_base_slide("Metode Dasar", "Selisih Maju: Menggunakan Data Setelah Titik", 5,
        "Selisih maju memperkirakan turunan dengan membandingkan nilai titik sekarang dengan titik berikutnya. Pada contoh detik ke-2, kita pakai posisi detik ke-3 (27) dikurangi detik ke-2 (8) dibagi 1, menghasilkan 19 m/s. Sangat praktis untuk titik awal tabel.")

    add_math_box(s5, Inches(0.8), Inches(1.8), Inches(11.733), Inches(1.6),
        "Rumus Selisih Maju (Forward Difference)",
        latex=r"f'(x) \approx \frac{f(x+h) - f(x)}{h}",
        subtext="Membandingkan nilai pada titik evaluasi dengan nilai satu langkah di depannya")

    add_card(s5, Inches(0.8), Inches(3.6), Inches(5.6), Inches(2.5), "Cara Memahami Rumus", [
        "f'(x) : Laju perubahan yang ingin diperkirakan pada titik x.",
        "f(x+h) : Nilai data satu langkah setelah titik observasi.",
        "f(x) : Nilai data pada titik observasi saat ini.",
        "Pembilang : Perubahan nilai ke depan [f(x+h) - f(x)].",
        "Penyebut h : Mengubahnya menjadi laju per satuan waktu/jarak."
    ], "Bedah Rumus", accent_color=COLOR_PRIMARY)

    add_custom_card(s5, Inches(6.8), Inches(3.6), Inches(5.733), Inches(2.5),
        "Contoh Hitungan (t = 2, h = 1)", [
            "Data: s(2) = 8 meter,  s(3) = 27 meter",
            "v(2) ≈ (27 − 8) / 1 = 19 m/s",
            "",
            "Kapan digunakan: Saat data sesudah titik tersedia.",
            "Sangat praktis untuk titik paling awal (ujung kiri) tabel.",
            "Orde Galat: O(h) (penurunan linear terhadap h)."
        ], border_color=COLOR_EMERALD, title_color=COLOR_EMERALD,
        latex=r"v(2) \approx \frac{27 - 8}{1} = 19\text{ m/s}")

    add_callout_banner(s5, Inches(0.8), Inches(6.25), Inches(11.733), Inches(0.48),
        "Karakteristik Maju: Memakai titik x dan x+h | Orde galat O(h) | Pilihan utama untuk ujung kiri data.")

    # =========================================================================
    # SLIDE 6: METODE SELISIH MUNDUR (BACKWARD DIFFERENCE)
    # =========================================================================
    s6 = add_base_slide("Metode Dasar", "Selisih Mundur: Menggunakan Data Sebelum Titik", 6,
        "Selisih mundur membandingkan nilai saat ini dengan nilai sebelumnya. Pada detik ke-2, kita kurangkan posisi detik ke-2 (8) dengan detik ke-1 (1) dibagi 1, menghasilkan 7 m/s. Cocok untuk titik paling akhir dalam tabel.")

    add_math_box(s6, Inches(0.8), Inches(1.8), Inches(11.733), Inches(1.6),
        "Rumus Selisih Mundur (Backward Difference)",
        latex=r"f'(x) \approx \frac{f(x) - f(x-h)}{h}",
        subtext="Membandingkan nilai pada titik evaluasi dengan nilai satu langkah di belakangnya")

    add_card(s6, Inches(0.8), Inches(3.6), Inches(5.6), Inches(2.5), "Cara Memahami Rumus", [
        "f'(x) : Laju perubahan yang ingin diperkirakan pada titik x.",
        "f(x) : Nilai data pada titik observasi saat ini.",
        "f(x-h) : Nilai data satu langkah sebelum titik observasi.",
        "Pembilang : Perubahan nilai dari belakang [f(x) - f(x-h)].",
        "Penyebut h : Jarak selang antara kedua pengukuran."
    ], "Bedah Rumus", accent_color=COLOR_BLUE)

    add_custom_card(s6, Inches(6.8), Inches(3.6), Inches(5.733), Inches(2.5),
        "Contoh Hitungan (t = 2, h = 1)", [
            "Data: s(2) = 8 meter,  s(1) = 1 meter",
            "v(2) ≈ (8 − 1) / 1 = 7 m/s",
            "",
            "Kapan digunakan: Saat data sebelum titik tersedia.",
            "Sangat praktis untuk titik paling akhir (ujung kanan) tabel.",
            "Orde Galat: O(h) (penurunan linear terhadap h)."
        ], border_color=COLOR_AMBER, title_color=COLOR_AMBER,
        latex=r"v(2) \approx \frac{8 - 1}{1} = 7\text{ m/s}")

    add_callout_banner(s6, Inches(0.8), Inches(6.25), Inches(11.733), Inches(0.48),
        "Karakteristik Mundur: Memakai titik x-h dan x | Orde galat O(h) | Pilihan utama untuk ujung kanan data.")

    # =========================================================================
    # SLIDE 7: METODE SELISIH TENGAH (CENTRAL DIFFERENCE)
    # =========================================================================
    s7 = add_base_slide("Metode Dasar", "Selisih Tengah: Menggunakan Dua Sisi", 7,
        "Selisih tengah menggunakan titik di kiri dan kanan titik yang diamati. Jarak keduanya adalah 2h, sehingga penyebutnya 2h. Pada detik ke-2, (27 - 1)/2 = 13 m/s. Lebih teliti untuk titik di bagian tengah karena simetris.")

    add_math_box(s7, Inches(0.8), Inches(1.8), Inches(11.733), Inches(1.6),
        "Rumus Selisih Tengah (Central Difference)",
        latex=r"f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}",
        subtext="Menggunakan data simetris mengapit titik evaluasi (rentang total 2h)")

    add_card(s7, Inches(0.8), Inches(3.6), Inches(5.6), Inches(2.5), "Mengapa Penyebutnya 2h?", [
        "Jarak dari titik kiri (x − h) ke titik tengah (x) adalah h.",
        "Jarak dari titik tengah (x) ke titik kanan (x + h) adalah h.",
        "Total rentang jarak titik kiri ke titik kanan adalah 2h.",
        "Keistimewaan: Nilai f(x) sendiri tidak perlu dihitung!",
        "Orde Galat: O(h²) — jauh lebih teliti dan simetris."
    ], "Konsep 2h", accent_color=COLOR_EMERALD)

    add_custom_card(s7, Inches(6.8), Inches(3.6), Inches(5.733), Inches(2.5),
        "Contoh Hitungan (t = 2, h = 1)", [
            "Data: s(3) = 27 meter,  s(1) = 1 meter",
            "v(2) ≈ (27 − 1) / (2 × 1) = 26 / 2 = 13 m/s",
            "",
            "Kapan digunakan: Saat data sebelum dan sesudah tersedia.",
            "Pilihan terbaik untuk titik interior (bagian dalam tabel).",
            "Orde Galat: Kuadratik O(h²) ⭐."
        ], border_color=COLOR_EMERALD, title_color=COLOR_EMERALD,
        latex=r"v(2) \approx \frac{27 - 1}{2(1)} = 13\text{ m/s}")

    add_callout_banner(s7, Inches(0.8), Inches(6.25), Inches(11.733), Inches(0.48),
        "Karakteristik Tengah: Memakai x-h dan x+h | Orde galat O(h²) ⭐ | Pilihan terbaik untuk titik dalam tabel.")

    # =========================================================================
    # SLIDE 8: BAGAIMANA MEMILIH METODE YANG TEPAT?
    # =========================================================================
    s8 = add_base_slide("Panduan Praktis", "Bagaimana Memilih Metode yang Tepat?", 8,
        "Pemilihan metode bergantung pada data yang tersedia di sekitar titik evaluasi. Jangan pilih rumus hanya karena terlihat mudah. Cek posisinya: di awal gunakan maju, di akhir gunakan mundur, di tengah gunakan selisih tengah.")

    add_table_data(s8, Inches(0.8), Inches(1.8), Inches(11.733), Inches(2.1),
        ["Situasi Data", "Metode yang Digunakan", "Alasan & Logika Penggunaan"],
        [
            ["Data setelah titik tersedia", "Selisih Maju", "Membandingkan titik sekarang dengan titik berikutnya"],
            ["Data sebelum titik tersedia", "Selisih Mundur", "Membandingkan titik sekarang dengan titik sebelumnya"],
            ["Data sebelum & sesudah tersedia", "Selisih Tengah ⭐", "Menggunakan informasi simetris dari kedua sisi titik"]
        ])

    add_card(s8, Inches(0.8), Inches(4.1), Inches(11.733), Inches(1.9), "Ilustrasi Praktis pada Data Waktu t = 1, 2, 3", [
        "Pada t = 1 : Data sebelumnya tidak tersedia → Gunakan Selisih Maju.",
        "Pada t = 3 : Data sesudahnya tidak tersedia → Gunakan Selisih Mundur.",
        "Pada t = 2 : Data sebelum (t=1) dan sesudah (t=3) lengkap → Gunakan Selisih Tengah ⭐.",
        "Aturan Emas: Periksa ketersediaan data tetangga sebelum memilih metode!"
    ], "Panduan", accent_color=COLOR_PRIMARY)

    add_callout_banner(s8, Inches(0.8), Inches(6.15), Inches(11.733), Inches(0.55),
        "Peringatan: Jangan memilih metode hanya karena rumusnya mudah; periksa dahulu posisi data dalam tabel!", is_amber=True)

    # =========================================================================
    # SLIDE 9: APA PERBEDAAN KETELITIAN KETIGA METODE?
    # =========================================================================
    s9 = add_base_slide("Analisis Galat", "Apa Perbedaan Ketelitian Ketiga Metode?", 9,
        "Ketiga metode sama-sama menghasilkan pendekatan, tetapi laju penurunan galatnya berbeda. Selisih maju dan mundur berorde O(h), jika h dibagi dua galat turun separuhnya. Selisih tengah berorde O(h^2), jika h dibagi dua galat turun empat kali lipat.")

    add_table_data(s9, Inches(0.8), Inches(1.8), Inches(11.733), Inches(2.1),
        ["Metode", "Orde Galat Pemotongan", "Makna Sederhana", "Pengaruh Jika h Dibagi 2"],
        [
            ["Selisih Maju", "O(h)", "Galat dominan sebanding dengan langkah h", "Galat berkurang ≈ 2×"],
            ["Selisih Mundur", "O(h)", "Galat dominan sebanding dengan langkah h", "Galat berkurang ≈ 2×"],
            ["Selisih Tengah", "O(h²) ⭐", "Galat dominan sebanding kuadrat langkah h²", "Galat berkurang ≈ 4×! ⭐"]
        ])

    add_card(s9, Inches(0.8), Inches(4.1), Inches(5.6), Inches(2.1), "Makna dalam Praktik", [
        "Jika h diperkecil 1/2, galat maju/mundur turun ≈ 50%.",
        "Pada selisih tengah, galat turun menjadi 1/4 (≈ 25%)!",
        "Berlaku selama fungsi cukup mulus dan pembulatan aman."
    ], "Praktik", accent_color=COLOR_PRIMARY)

    add_card(s9, Inches(6.8), Inches(4.1), Inches(5.733), Inches(2.1), "Kesimpulan Praktis", [
        "Selisih Tengah: Keunggulan akurasi tinggi, wajib 2 sisi data.",
        "Maju & Mundur: Tetap esensial di batas batas ujung interval data.",
        "Kombinasi keduanya biasa dipakai melengkapi tabel penuh."
    ], "Intisari", accent_color=COLOR_EMERALD)

    add_callout_banner(s9, Inches(0.8), Inches(6.35), Inches(11.733), Inches(0.42),
        "Kesimpulan: Selisih tengah lebih unggul secara teoritis, tetapi selisih maju dan mundur tak tergantikan di batas ujung.")

    # =========================================================================
    # SLIDE 10: STUDI KASUS: MENGHITUNG KECEPATAN
    # =========================================================================
    s10 = add_base_slide("Studi Kasus", "Studi Kasus: Menghitung Kecepatan dari Data Posisi", 10,
        "Kita bandingkan ketiga metode langsung pada data posisi yang sama di t=2. Selisih maju menghasilkan 19 m/s, selisih mundur menghasilkan 7 m/s, dan selisih tengah menghasilkan 13 m/s. Ketiganya berbeda karena memakai pasangan data yang berbeda.")

    add_callout_banner(s10, Inches(0.8), Inches(1.8), Inches(11.733), Inches(0.48),
        "Data Diketahui: s(1) = 1 m,  s(2) = 8 m (titik evaluasi t = 2),  s(3) = 27 m, dengan langkah waktu h = 1 detik.")

    add_custom_card(s10, Inches(0.8), Inches(2.45), Inches(3.6), Inches(3.7),
        "1. Selisih Maju", [
            "Data: Waktu t = 2 dan t = 3",
            "v(2) ≈ [s(3) − s(2)] / h",
            "= (27 − 8) / 1",
            "= 19 m/s",
            "",
            "Mengamati laju perubahan pada interval depan [2, 3]."
        ], border_color=COLOR_PRIMARY, title_color=COLOR_PRIMARY,
        latex=r"v(2) \approx \frac{27-8}{1} = 19\text{ m/s}")

    add_custom_card(s10, Inches(4.8), Inches(2.45), Inches(3.6), Inches(3.7),
        "2. Selisih Mundur", [
            "Data: Waktu t = 1 dan t = 2",
            "v(2) ≈ [s(2) − s(1)] / h",
            "= (8 − 1) / 1",
            "= 7 m/s",
            "",
            "Mengamati laju perubahan pada interval belakang [1, 2]."
        ], border_color=COLOR_BLUE, title_color=COLOR_BLUE,
        latex=r"v(2) \approx \frac{8-1}{1} = 7\text{ m/s}")

    add_custom_card(s10, Inches(8.8), Inches(2.45), Inches(3.733), Inches(3.7),
        "3. Selisih Tengah", [
            "Data: Waktu t = 1 dan t = 3",
            "v(2) ≈ [s(3) − s(1)] / (2h)",
            "= (27 − 1) / 2",
            "= 13 m/s ⭐",
            "",
            "Merata-ratakan interval penuh [1, 3] sebesar 2h."
        ], border_color=COLOR_EMERALD, title_color=COLOR_EMERALD,
        latex=r"v(2) \approx \frac{27-1}{2} = 13\text{ m/s}")

    add_callout_banner(s10, Inches(0.8), Inches(6.3), Inches(11.733), Inches(0.45),
        "Observasi: Ketiga hasil berbeda (19, 7, 13 m/s) karena setiap metode menggunakan pasangan titik observasi yang berbeda.")

    # =========================================================================
    # SLIDE 11: MEMBACA DAN MENAFSIRKAN HASIL
    # =========================================================================
    s11 = add_base_slide("Evaluasi Hasil", "Membaca dan Menafsirkan Hasil Perhitungan", 11,
        "Perbedaan hasil bukan karena salah hitung. Benda ini dipercepat, sehingga wajar kecepatan interval awal (7 m/s) lebih lambat dibanding interval berikutnya (19 m/s). Selisih tengah merata-ratakannya menjadi 13 m/s.")

    add_table_data(s11, Inches(0.8), Inches(1.8), Inches(5.6), Inches(2.3),
        ["Metode", "Hasil Kecepatan", "Rentang Data yang Dipakai"],
        [
            ["Selisih Maju", "19 m/s", "Detik ke-2 menuju detik ke-3"],
            ["Selisih Mundur", "7 m/s", "Detik ke-1 menuju detik ke-2"],
            ["Selisih Tengah", "13 m/s ⭐", "Detik ke-1 menuju ke-3 (rentang 2s)"]
        ])

    add_card(s11, Inches(6.8), Inches(1.8), Inches(5.733), Inches(4.3), "Apa yang Dapat Kita Pahami?", [
        "Bukan Salah Hitung: Perbedaan muncul murni karena rentang pengamatan berbeda.",
        "Gerak Dipercepat: Laju benda bertambah cepat seiring berjalannya waktu.",
        "Laju Awal vs Akhir: Wajar bila interval awal (7 m/s) lebih lambat dari interval akhir (19 m/s).",
        "Selisih Tengah: Bertindak merata-ratakan kedua perubahan menjadi 13 m/s.",
        "Pesan Penting: Hasil diferensiasi numerik adalah perkiraan; pahami konteks data sebelum menafsirkan!"
    ], "Interpretasi Fisis", accent_color=COLOR_PRIMARY)

    add_card(s11, Inches(0.8), Inches(4.3), Inches(5.6), Inches(1.8), "Rangkuman Rentang", [
        "Maju: Mencerminkan tren ke masa depan [2, 3].",
        "Mundur: Mencerminkan tren dari masa lalu [1, 2].",
        "Tengah: Keseimbangan simetris dua arah [1, 3] ⭐."
    ], "Karakter", accent_color=COLOR_EMERALD)

    add_callout_banner(s11, Inches(0.8), Inches(6.25), Inches(11.733), Inches(0.48),
        "Pesan Utama: Hasil diferensiasi numerik merupakan perkiraan. Selalu pahami rentang data sebelum menafsirkan!")

    # =========================================================================
    # SLIDE 12: MEMERIKSA GALAT DAN MENARIK KESIMPULAN
    # =========================================================================
    s12 = add_base_slide("Evaluasi Galat", "Memeriksa Galat dan Menarik Kesimpulan", 12,
        "Karena data dibuat dari fungsi s(t) = t^3, kita tahu nilai eksaknya adalah 12 m/s. Galat selisih maju 7, mundur 5, dan tengah hanya 1. Selisih tengah terbukti paling teliti, namun tetap perhatikan ketersediaan data di lapangan.")

    add_math_box(s12, Inches(0.8), Inches(1.8), Inches(5.6), Inches(1.5),
        "Nilai Eksak & Rumus Galat",
        latex=r"s'(2) = 3(2)^2 = 12\text{ m/s}, \quad E = |v_{num} - v_{eksak}|",
        subtext="Fungsi posisi s(t) = t³ -> Kecepatan eksak s'(t) = 3t²")

    add_table_data(s12, Inches(0.8), Inches(3.45), Inches(5.6), Inches(2.5),
        ["Metode", "Perkiraan", "Nilai Eksak", "Galat Absolut"],
        [
            ["Maju", "19 m/s", "12 m/s", "7 m/s"],
            ["Mundur", "7 m/s", "12 m/s", "5 m/s"],
            ["Tengah", "13 m/s", "12 m/s", "1 m/s ⭐"]
        ])

    add_card(s12, Inches(6.8), Inches(1.8), Inches(5.733), Inches(4.15), "Ringkasan yang Perlu Diingat", [
        "Maju: Gunakan data titik saat ini dan sesudahnya (x, x+h).",
        "Mundur: Gunakan data titik sebelumnya dan saat ini (x-h, x).",
        "Tengah: Gunakan data sebelum dan sesudah (x-h, x+h).",
        "Pilih Metode: Sesuaikan dengan posisi titik data yang tersedia di tabel.",
        "Evaluasi: Jika nilai eksak ada, hitung galat untuk mengukur kedekatan.",
        "Catatan: Selisih tengah paling dekat ke eksak (E = 1 m/s), namun data harus lengkap di kedua sisi!"
    ], "Pedoman Inti", accent_color=COLOR_EMERALD)

    add_callout_banner(s12, Inches(0.8), Inches(6.15), Inches(11.733), Inches(0.55),
        "Kesimpulan Akhir: Selisih tengah paling teliti (galat 1 m/s), tetapi pemilihan metode di lapangan harus selalu realistis terhadap ketersediaan data!")

        # =========================================================================
    # SLIDE 13: KONSEP DASAR TURUNAN DARI DATA TABEL
    # =========================================================================
    s13 = add_base_slide("Rumus Titik Data", "Konsep Dasar Turunan dari Data Tabel", 13,
        "Pengantar konsep diferensiasi dari data tabel diskrit. Tekankan dua pembeda utama: jumlah titik (3 atau 5) dan posisi titik (akhir atau tengah). Lima titik memerlukan lebih banyak data tabel tetapi menghasilkan ketelitian jauh lebih tinggi.")
    add_card(s13, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), "Representasi Kisi Data Seragam", [
        "Sering kali kita tidak memiliki rumus fungsi kontinu, hanya data diskrit (x, f(x)) berjarak seragam h.",
        "Contoh Titik Utama: x₀ = 2,0 dengan langkah h = 0,1.",
        "Data Mengapit: x₀ - 2h (1,8), x₀ - h (1,9), x₀ (2,0), x₀ + h (2,1), x₀ + 2h (2,2).",
        "Tujuan: Mengestimasi nilai turunan f'(x₀) menggunakan kombinasi linear nilai fungsi di titik-titik sekitar."
    ], "Data Diskrit", accent_color=COLOR_PRIMARY)
    add_table_data(s13, Inches(1.1), Inches(4.3), Inches(5.0), Inches(1.4),
        ["x₀-2h", "x₀-h", "x₀", "x₀+h", "x₀+2h"],
        [
            ["1,8", "1,9", "2,0", "2,1", "2,2"]
        ])

    add_card(s13, Inches(6.8), Inches(1.8), Inches(5.733), Inches(4.8), "Dua Aspek Pembeda Metode", [
        "1. Berdasarkan Jumlah Posisi Titik Data:",
        "   • Tiga Titik: Menggunakan 3 data, galat O(h²), hemat titik data.",
        "   • Lima Titik: Menggunakan 5 data, galat O(h⁴), akurasi sangat tinggi.",
        "",
        "2. Berdasarkan Posisi Titik Evaluasi (x₀):",
        "   • Akhir (Endpoint): Dipakai bila x₀ di ujung batas tabel (hanya data satu sisi yang tersedia).",
        "   • Tengah (Midpoint): Dipakai bila data tersedia mengapit simetris di kiri dan kanan x₀."
    ], "Klasifikasi", accent_color=COLOR_EMERALD)

    # =========================================================================
    # SLIDE 14: RUMUS TIGA TITIK: AKHIR & TENGAH
    # =========================================================================
    s14 = add_base_slide("Rumus Titik Data", "Rumus Tiga Titik: Akhir & Tengah", 14,
        "Rumus tiga titik tengah memakai tiga POSISI data: x₀−h, x₀, x₀+h. Koefisien f(x₀) adalah 0, sehingga hanya f(x₀+h) dan f(x₀−h) yang muncul di rumus. Itulah alasan disebut tiga titik walaupun hanya dua nilai fungsi yang dihitung. Rumus akhir dengan h negatif menjadi versi mundur dari ujung kanan data.")
    add_math_box(s14, Inches(0.8), Inches(1.8), Inches(5.6), Inches(2.3),
        "A. Tiga Titik Akhir (Endpoint)",
        latex=r"f'(x_0) \approx \frac{-3f(x_0) + 4f(x_0+h) - f(x_0+2h)}{2h}",
        subtext="Galat: (h²/3) f'''(ξ₀)  =>  Orde O(h²)")
    add_table_data(s14, Inches(0.8), Inches(4.2), Inches(5.6), Inches(1.4),
        ["Bobot Koefisien", "-3", "+4", "-1"],
        [
            ["Posisi Titik", "x₀", "x₀ + h", "x₀ + 2h"]
        ])
    add_callout_banner(s14, Inches(0.8), Inches(5.75), Inches(5.6), Inches(0.7),
        "Faktor: x 1/(2h) | Dipakai di batas ujung tabel data (satu sisi).")

    add_math_box(s14, Inches(6.8), Inches(1.8), Inches(5.733), Inches(2.3),
        "B. Tiga Titik Tengah (Midpoint)",
        latex=r"f'(x_0) \approx \frac{f(x_0+h) - f(x_0-h)}{2h}",
        subtext="Galat: -(h²/6) f'''(ξ₁)  =>  Orde O(h²)")
    add_table_data(s14, Inches(6.8), Inches(4.2), Inches(5.733), Inches(1.4),
        ["Bobot Koefisien", "-1", "0", "+1"],
        [
            ["Posisi Titik", "x₀ - h", "x₀", "x₀ + h"]
        ])
    add_callout_banner(s14, Inches(6.8), Inches(5.75), Inches(5.733), Inches(0.7),
        "Simetris kiri-kanan. Koefisien f(x₀)=0 sehingga nilainya tidak dihitung.")

    # =========================================================================
    # SLIDE 15: RUMUS LIMA TITIK: AKHIR & TENGAH
    # =========================================================================
    s15 = add_base_slide("Rumus Titik Data", "Rumus Lima Titik: Akhir & Tengah", 15,
        "Memakai polinomial Lagrange melalui lima titik sehingga galat turun ke orde h⁴. Lima titik akhir: x₀ sampai x₀+4h. Lima titik tengah: x₀−2h sampai x₀+2h, f(x₀) berkoefisien 0.")
    add_math_box(s15, Inches(0.8), Inches(1.8), Inches(5.6), Inches(2.3),
        "A. Lima Titik Akhir (Endpoint)",
        latex=r"f'(x_0) \approx \frac{-25f_0 + 48f_1 - 36f_2 + 16f_3 - 3f_4}{12h}",
        subtext="Galat: (h⁴/5) f⁽⁵⁾(ξ)  =>  Orde O(h⁴)")
    add_table_data(s15, Inches(0.8), Inches(4.2), Inches(5.6), Inches(1.4),
        ["Bobot", "-25", "+48", "-36", "+16", "-3"],
        [
            ["Posisi", "x₀", "x₀+h", "x₀+2h", "x₀+3h", "x₀+4h"]
        ])
    add_callout_banner(s15, Inches(0.8), Inches(5.75), Inches(5.6), Inches(0.7),
        "Faktor: x 1/(12h) | Butuh 4 titik data di depan x₀ (ujung data).")

    add_math_box(s15, Inches(6.8), Inches(1.8), Inches(5.733), Inches(2.3),
        "B. Lima Titik Tengah (Midpoint)",
        latex=r"f'(x_0) \approx \frac{f_{-2} - 8f_{-1} + 8f_1 - f_2}{12h}",
        subtext="Galat: (h⁴/30) f⁽⁵⁾(ξ)  =>  Orde O(h⁴)")
    add_table_data(s15, Inches(6.8), Inches(4.2), Inches(5.733), Inches(1.4),
        ["Bobot", "+1", "-8", "0", "+8", "-1"],
        [
            ["Posisi", "x₀-2h", "x₀-h", "x₀", "x₀+h", "x₀+2h"]
        ])
    add_callout_banner(s15, Inches(6.8), Inches(5.75), Inches(5.733), Inches(0.7),
        "Simetris penuh. Bobot f(x₀)=0. Konstanta galat 1/30 sangat kecil!")

    # =========================================================================
    # SLIDE 16: TIGA TITIK VS LIMA TITIK
    # =========================================================================
    s16 = add_base_slide("Rumus Titik Data", "Perbandingan: Tiga Titik vs Lima Titik", 16,
        "Gambar memakai contoh tengah x₀ = 2.0, h = 0.1. Pada tiga titik hanya 2 nilai fungsi dihitung (1.9 dan 2.1), pada lima titik 4 nilai (1.8, 1.9, 2.1, 2.2). Orde galat O(h²) dan O(h⁴) cukup disebut sekilas; analisis galat dibahas anggota lain.")
    add_table_data(s16, Inches(0.8), Inches(1.8), Inches(6.0), Inches(4.7),
        ["Karakteristik", "Rumus Tiga Titik", "Rumus Lima Titik"],
        [
            ["Orde Galat", "O(h²)", "O(h⁴) ⭐"],
            ["Kebutuhan Titik", "3 posisi data", "5 posisi data"],
            ["Evaluasi Fungsi", "2 atau 3 nilai", "4 atau 5 nilai"],
            ["Kesesuaian", "Tabel pendek / batas data", "Data padat / akurasi tinggi"],
            ["Reduksi Galat (h/2)", "Turun 4x lipat", "Turun 16x lipat ⭐"]
        ])
    add_card(s16, Inches(7.1), Inches(1.8), Inches(5.433), Inches(4.7), "Bukti Numerik pada f(x) = x eˣ", [
        "Kondisi Uji: x₀ = 2,0 ; h = 0,1 (Metode Tengah)",
        "Nilai Eksak f'(2,0) = 3e² ≈ 22,167168",
        "",
        "• Tiga Titik Tengah: Hasil 22,228790",
        "  Galat Absolut = 6,16 x 10⁻² (0,061622)",
        "",
        "• Lima Titik Tengah: Hasil 22,166999",
        "  Galat Absolut = 1,69 x 10⁻⁴ (0,000169)",
        "",
        "Kesimpulan: Lima titik menghasilkan ketelitian > 364x LEBIH AKURAT pada nilai langkah h yang persis sama!"
    ], "Studi Kasus Komparasi", accent_color=COLOR_EMERALD)

    # =========================================================================
    # SLIDE 17: PANDUAN MEMILIH RUMUS
    # =========================================================================
    s17 = add_base_slide("Rumus Titik Data", "Panduan Memilih Rumus", 17,
        "Pilih rumus berdasarkan posisi titik yang dicari: ujung data memakai rumus akhir, di dalam data memakai rumus tengah. Untuk f′(1.5) data hanya ada di kiri, maka rumus akhir dipakai dengan h negatif (memakai 1.5, 1.4, 1.3 untuk tiga titik).")
    add_table_data(s17, Inches(0.8), Inches(1.8), Inches(11.733), Inches(3.6),
        ["Rumus", "Posisi Titik yang Dipakai", "Distribusi Data", "Kriteria Penggunaan"],
        [
            ["Tiga Titik Akhir", "x₀, x₀+h, x₀+2h", "Satu sisi", "Titik berada di batas ujung tabel (O(h²))"],
            ["Tiga Titik Tengah", "x₀-h, x₀, x₀+h (f₀ koef 0)", "Simetris", "Ada 1 data di kiri & kanan (O(h²))"],
            ["Lima Titik Akhir", "x₀ s.d. x₀+4h", "Satu sisi", "Ujung tabel & minimal 4 data di satu sisi (O(h⁴))"],
            ["Lima Titik Tengah", "x₀-2h s.d. x₀+2h (f₀ koef 0)", "Simetris", "Ada minimal 2 data di kiri & kanan (O(h⁴))"]
        ])
    add_callout_banner(s17, Inches(0.8), Inches(5.65), Inches(11.733), Inches(0.95),
        "Aturan Penggunaan Nilai h:\\n"
        "• Titik di ujung kiri: gunakan rumus akhir dengan h > 0 (bergerak maju ke kanan).\\n"
        "• Titik di ujung kanan (mis. x = 1,5): gunakan rumus akhir dengan h < 0 (bergerak mundur ke kiri).")

    # =========================================================================
    # SLIDE 18: CARA MENGHITUNG: PROSEDUR 4 LANGKAH
    # =========================================================================
    s18 = add_base_slide("Rumus Titik Data", "Cara Menghitung: Prosedur 4 Langkah", 18,
        "Empat langkah yang sama untuk keempat rumus. h adalah jarak antar-data, bukan nilai fungsi dan bukan hasil turunan. h negatif dipakai saat rumus akhir diterapkan dari ujung kanan data.")
    add_card(s18, Inches(0.8), Inches(1.8), Inches(5.6), Inches(2.2), "Langkah 1: Tentukan x₀ dan h", [
        "x₀ adalah absis titik yang dicari turunannya.",
        "h = x_{i+1} - x_i adalah jarak seragam antar-data tabel (misal 2,1 - 2,0 = 0,1)."
    ], "Step 1", accent_color=COLOR_PRIMARY)
    add_card(s18, Inches(6.8), Inches(1.8), Inches(5.733), Inches(2.2), "Langkah 2: Pilih Rumus yang Sesuai", [
        "Data satu sisi: gunakan rumus akhir.",
        "Data simetris mengapit: gunakan rumus tengah.",
        "Pilih orde presisi: Tiga Titik (O(h²)) atau Lima Titik (O(h⁴))."
    ], "Step 2", accent_color=COLOR_PRIMARY)
    add_card(s18, Inches(0.8), Inches(4.2), Inches(5.6), Inches(2.2), "Langkah 3: Substitusi Nilai Fungsi", [
        "Ambil nilai f(x) dari tabel sesuai posisi titik yang dipersyaratkan.",
        "Kalikan masing-masing nilai dengan koefisien bobotnya."
    ], "Step 3", accent_color=COLOR_EMERALD)
    add_card(s18, Inches(6.8), Inches(4.2), Inches(5.733), Inches(2.2), "Langkah 4: Hitung dan Lakukan Pembagian", [
        "Jumlahkan seluruh hasil kali nilai fungsi.",
        "Bagi dengan faktor pembagi: 2h (tiga titik) atau 12h (lima titik)."
    ], "Step 4", accent_color=COLOR_EMERALD)

    # =========================================================================
    # SLIDE 19: SOAL 1: TIGA TITIK AKHIR
    # =========================================================================
    s19 = add_base_slide("Rumus Titik Data", "Soal 1: Tiga Titik Akhir", 19,
        "Soal 1. Pastikan siswa membaca dulu: rumus apa (tiga titik akhir), x₀ berapa, h berapa. Empat instruksi di slide ini sama urutannya dengan empat langkah di slide penyelesaian. Beri waktu sekitar 3 menit sebelum membuka slide berikutnya.")
    add_table_data(s19, Inches(0.8), Inches(1.8), Inches(11.733), Inches(1.4),
        ["x", "1,8", "1,9", "2,0 (x₀)", "2,1", "2,2"],
        [
            ["f(x)", "10,889365", "12,703199", "14,778112", "17,148957", "19,855030"]
        ])
    add_card(s19, Inches(0.8), Inches(3.4), Inches(5.6), Inches(3.2), "Deskripsi Soal", [
        "Fungsi: f(x) = x eˣ",
        "Titik Evaluasi: x₀ = 2,0 ; Ukuran Langkah: h = 0,1",
        "Nilai Eksak: f'(2,0) = 3e² ≈ 22,167168",
        "",
        "Soal: Hitunglah hampiran turunan f'(2,0) menggunakan rumus tiga titik akhir dan tentukan galatnya terhadap nilai eksak!"
    ], "Soal 1", accent_color=COLOR_PRIMARY)
    add_card(s19, Inches(6.8), Inches(3.4), Inches(5.733), Inches(3.2), "Instruksi Pengerjaan (4 Langkah)", [
        "1. Substitusi f(2,0), f(2,1), f(2,2) ke rumus [-3f₀ + 4f₁ - f₂] / 2h.",
        "2. Kalikan nilai fungsi dengan bobot: -3, +4, dan -1.",
        "3. Jumlahkan ketiga hasil kali, lalu bagi dengan 2h = 0,2.",
        "4. Hitung galat absolut = |nilai eksak - nilai hampiran|."
    ], "Instruksi", accent_color=COLOR_EMERALD)

    # =========================================================================
    # SLIDE 20: PENYELESAIAN 1: TIGA TITIK AKHIR
    # =========================================================================
    s20 = add_base_slide("Rumus Titik Data", "Penyelesaian 1: Tiga Titik Akhir", 20,
        "Dengan h = −0.1 hasilnya 22.054525, galat 1.13×10⁻¹. Langkah sama: masukkan nilai, kalikan, jumlahkan, bagi 2h.")
    add_math_box(s20, Inches(0.8), Inches(1.8), Inches(11.733), Inches(1.6),
        "Rumus Tiga Titik Akhir (x₀ = 2,0 ; h = 0,1)",
        latex=r"f'(2.0) \approx \frac{-3f(2.0) + 4f(2.1) - f(2.2)}{2(0.1)}",
        subtext="Nilai Eksak: f'(2,0) = 3e² ≈ 22,167168")
    add_card(s20, Inches(0.8), Inches(3.6), Inches(6.0), Inches(3.0), "Tahapan Perhitungan", [
        "1. Masukkan Nilai dari Tabel:",
        "   = [-3(14,778112) + 4(17,148957) - 19,855030] / 0,2",
        "",
        "2. Kalikan Bobot Koefisien:",
        "   = [-44,334336 + 68,595828 - 19,855030] / 0,2",
        "",
        "3. Jumlahkan & Bagi 2h:",
        "   = 4,406462 / 0,2 = 22,032310"
    ], "Langkah 1-3", accent_color=COLOR_PRIMARY)
    add_card(s20, Inches(7.1), Inches(3.6), Inches(5.433), Inches(3.0), "Evaluasi Hasil & Galat", [
        "Hasil Hampiran = 22,032310",
        "Nilai Eksak     = 22,167168",
        "",
        "Galat Absolut:",
        "|22,167168 - 22,032310| = 1,35 x 10⁻¹  (0,134858)",
        "",
        "Catatan: Dengan h = -0,1 hasilnya 22,054525 (galat 1,13 x 10⁻¹)."
    ], "Langkah 4", accent_color=COLOR_EMERALD)

    # =========================================================================
    # SLIDE 21: SOAL 2: TIGA TITIK TENGAH
    # =========================================================================
    s21 = add_base_slide("Rumus Titik Data", "Soal 2: Tiga Titik Tengah", 21,
        "Soal 2. Pertanyaan pancingan: mengapa f(2.0) tidak muncul padahal x₀ = 2.0? Jawaban: koefisiennya 0. Minta siswa membandingkan galat dengan Soal 1 sebelum melihat penyelesaian.")
    add_table_data(s21, Inches(0.8), Inches(1.8), Inches(11.733), Inches(1.4),
        ["x", "1,8", "1,9 (x₀-h)", "2,0 (x₀)", "2,1 (x₀+h)", "2,2"],
        [
            ["f(x)", "10,889365", "12,703199", "14,778112", "17,148957", "19,855030"]
        ])
    add_card(s21, Inches(0.8), Inches(3.4), Inches(5.6), Inches(3.2), "Deskripsi Soal", [
        "Fungsi: f(x) = x eˣ ; Titik Tengah: x₀ = 2,0 ; h = 0,1",
        "Nilai Eksak: f'(2,0) = 3e² ≈ 22,167168",
        "",
        "Soal: Dengan tabel data yang sama, hitunglah hampiran f'(2,0) menggunakan rumus tiga titik tengah dan bandingkan galatnya dengan Soal 1!",
        "",
        "Pertanyaan: Mengapa f(2,0) tidak muncul dalam rumus? Koefisiennya = 0!"
    ], "Soal 2", accent_color=COLOR_PRIMARY)
    add_card(s21, Inches(6.8), Inches(3.4), Inches(5.733), Inches(3.2), "Instruksi Pengerjaan (4 Langkah)", [
        "1. Substitusi f(2,1) dan f(1,9) ke rumus [f(x₀+h) - f(x₀-h)] / 2h.",
        "2. Kurangkan f(2,1) - f(1,9). Nilai f(2,0) tidak dipakai.",
        "3. Bagi hasil selisih dengan 2h = 0,2.",
        "4. Tentukan galat dan bandingkan dengan Soal 1 (1,35 x 10⁻¹): mana yang lebih teliti?"
    ], "Instruksi", accent_color=COLOR_EMERALD)

    # =========================================================================
    # SLIDE 22: PENYELESAIAN 2: TIGA TITIK TENGAH
    # =========================================================================
    s22 = add_base_slide("Rumus Titik Data", "Penyelesaian 2: Tiga Titik Tengah", 22,
        "Dengan h = 0.2 hasilnya 22.414163, galat −2.47×10⁻¹. Galat naik sekitar 4 kali saat h dua kali lebih besar (sesuai orde h²). f(2.0) tidak dipakai karena koefisiennya 0.")
    add_math_box(s22, Inches(0.8), Inches(1.8), Inches(11.733), Inches(1.6),
        "Rumus Tiga Titik Tengah (x₀ = 2,0 ; h = 0,1)",
        latex=r"f'(2.0) \approx \frac{f(2.1) - f(1.9)}{2(0.1)}",
        subtext="Nilai Eksak: f'(2,0) = 3e² ≈ 22,167168")
    add_card(s22, Inches(0.8), Inches(3.6), Inches(6.0), Inches(3.0), "Tahapan Perhitungan", [
        "1. Masukkan Nilai dari Tabel:",
        "   = (17,148957 - 12,703199) / 0,2",
        "",
        "2. Kurangkan Pembilang:",
        "   = 4,445758 / 0,2",
        "",
        "3. Bagi dengan 2h = 0,2:",
        "   = 22,228790"
    ], "Langkah 1-3", accent_color=COLOR_PRIMARY)
    add_card(s22, Inches(7.1), Inches(3.6), Inches(5.433), Inches(3.0), "Evaluasi & Komparasi Galat", [
        "Hasil Hampiran = 22,228790",
        "Nilai Eksak     = 22,167168",
        "",
        "Galat Bertanda = -6,16 x 10⁻²",
        "Galat Absolut  = 0,061622",
        "",
        "Perbandingan: Galat tiga titik tengah LEBIH DARI 2x LEBIH KECIL dibanding tiga titik akhir (0,134858)!"
    ], "Langkah 4", accent_color=COLOR_EMERALD)

    # =========================================================================
    # SLIDE 23: SOAL 3: LIMA TITIK AKHIR
    # =========================================================================
    s23 = add_base_slide("Rumus Titik Data", "Soal 3: Lima Titik Akhir", 23,
        "Soal 3. Jawaban pertanyaan 'mengapa bukan 2.0': rumus lima titik akhir membutuhkan x₀ sampai x₀+4h, yaitu 2.0 sampai 2.4, sedangkan tabel hanya sampai 2.2. Hanya x₀ = 1.8 yang punya empat data di kanannya.")
    add_table_data(s23, Inches(0.8), Inches(1.8), Inches(11.733), Inches(1.4),
        ["x", "1,8 (x₀)", "1,9", "2,0", "2,1", "2,2"],
        [
            ["f(x)", "10,889365", "12,703199", "14,778112", "17,148957", "19,855030"]
        ])
    add_card(s23, Inches(0.8), Inches(3.4), Inches(5.6), Inches(3.2), "Deskripsi Soal", [
        "Fungsi: f(x) = x eˣ ; Titik Ujung: x₀ = 1,8 ; h = 0,1",
        "Nilai Eksak: f'(1,8) = 2,8 e^{1,8} ≈ 16,939013",
        "",
        "Soal: Hitunglah hampiran f'(1,8) dengan rumus lima titik akhir!",
        "",
        "Diskusi: Mengapa x₀ = 2,0 tidak dapat dipakai? Rumus butuh x₀ s.d. x₀+4h (2,0 s.d. 2,4), data hanya sampai 2,2!"
    ], "Soal 3", accent_color=COLOR_PRIMARY)
    add_card(s23, Inches(6.8), Inches(3.4), Inches(5.733), Inches(3.2), "Instruksi Pengerjaan (4 Langkah)", [
        "1. Ambil 5 nilai data f(1,8) s.d. f(2,2).",
        "2. Kalikan dengan bobot: -25, +48, -36, +16, dan -3.",
        "3. Jumlahkan kelima hasil kali, lalu bagi dengan 12h = 1,2.",
        "4. Hitung galat dan bandingkan dengan tiga titik akhir di x₀=1,8 (1,06 x 10⁻¹)."
    ], "Instruksi", accent_color=COLOR_EMERALD)

    # =========================================================================
    # SLIDE 24: PENYELESAIAN 3: LIMA TITIK AKHIR
    # =========================================================================
    s24 = add_base_slide("Rumus Titik Data", "Penyelesaian 3: Lima Titik Akhir", 24,
        "Contoh tambahan di x₀ = 1.8 karena x₀ = 2.0 tidak punya empat titik di kanannya. Rumus sama dengan Contoh 6.1.3 buku untuk f′(1.1).")
    add_math_box(s24, Inches(0.8), Inches(1.8), Inches(11.733), Inches(1.6),
        "Rumus Lima Titik Akhir (x₀ = 1,8 ; h = 0,1)",
        latex=r"f'(1.8) \approx \frac{-25f(1.8) + 48f(1.9) - 36f(2.0) + 16f(2.1) - 3f(2.2)}{12(0.1)}",
        subtext="Nilai Eksak: f'(1,8) = 2,8 e^{1,8} ≈ 16,939013")
    add_card(s24, Inches(0.8), Inches(3.6), Inches(6.2), Inches(3.0), "Tahapan Perhitungan", [
        "1. Masukkan Nilai dari Tabel:",
        "   = [-25(10,889365) + 48(12,703199) - 36(14,778112)",
        "      + 16(17,148957) - 3(19,855030)] / 1,2",
        "2. Kalikan Bobot: = 20,325617 / 1,2",
        "3. Bagi dengan 12h = 1,2:",
        "   = 16,938014"
    ], "Langkah 1-3", accent_color=COLOR_PRIMARY)
    add_card(s24, Inches(7.3), Inches(3.6), Inches(5.233), Inches(3.0), "Evaluasi & Komparasi Galat", [
        "Hasil Lima Titik Akhir = 16,938014",
        "Nilai Eksak            = 16,939013",
        "",
        "Galat Absolut:",
        "|16,939013 - 16,938014| = 9,99 x 10⁻⁴ (0,000999)",
        "",
        "Komparasi: Tiga titik akhir di x₀=1,8 bergalat 1,06 x 10⁻¹. Lima titik akhir > 106x LEBIH TELITI!"
    ], "Langkah 4", accent_color=COLOR_EMERALD)

    # =========================================================================
    # SLIDE 25: SOAL 4: LIMA TITIK TENGAH
    # =========================================================================
    s25 = add_base_slide("Rumus Titik Data", "Soal 4: Lima Titik Tengah", 25,
        "Soal 4. Tekankan kesimpulan: dengan data dan h yang sama, lima titik tengah memberi galat sekitar 10⁻⁴, sedangkan tiga titik tengah sekitar 10⁻².")
    add_table_data(s25, Inches(0.8), Inches(1.8), Inches(11.733), Inches(1.4),
        ["x", "1,8 (x₀-2h)", "1,9 (x₀-h)", "2,0 (x₀)", "2,1 (x₀+h)", "2,2 (x₀+2h)"],
        [
            ["f(x)", "10,889365", "12,703199", "14,778112", "17,148957", "19,855030"]
        ])
    add_card(s25, Inches(0.8), Inches(3.4), Inches(5.6), Inches(3.2), "Deskripsi Soal", [
        "Fungsi: f(x) = x eˣ ; Titik Tengah: x₀ = 2,0 ; h = 0,1",
        "Nilai Eksak: f'(2,0) = 3e² ≈ 22,167168",
        "",
        "Soal: Hitunglah hampiran f'(2,0) menggunakan rumus lima titik tengah dan bandingkan ketelitiannya dengan tiga titik tengah (Soal 2)!",
        "",
        "Kondisi: Tersedia 2 data di kiri dan 2 data di kanan x₀ (simetris)."
    ], "Soal 4", accent_color=COLOR_PRIMARY)
    add_card(s25, Inches(6.8), Inches(3.4), Inches(5.733), Inches(3.2), "Instruksi Pengerjaan (4 Langkah)", [
        "1. Ambil 4 nilai data: f(1,8), f(1,9), f(2,1), f(2,2).",
        "2. Kalikan dengan bobot: +1, -8, +8, dan -1 (f(2,0) berbobot 0).",
        "3. Jumlahkan keempat hasil kali, lalu bagi dengan 12h = 1,2.",
        "4. Tentukan galat dan bandingkan dengan Soal 2 (-6,16 x 10⁻²)."
    ], "Instruksi", accent_color=COLOR_EMERALD)

    # =========================================================================
    # SLIDE 26: PENYELESAIAN 4: LIMA TITIK TENGAH
    # =========================================================================
    s26 = add_base_slide("Rumus Titik Data", "Penyelesaian 4: Lima Titik Tengah", 26,
        "Contoh 6.1.2 buku. Perbandingan: galat lima titik sekitar 10⁻⁴, tiga titik sekitar 10⁻².")
    add_math_box(s26, Inches(0.8), Inches(1.8), Inches(11.733), Inches(1.6),
        "Rumus Lima Titik Tengah (x₀ = 2,0 ; h = 0,1)",
        latex=r"f'(2.0) \approx \frac{f(1.8) - 8f(1.9) + 8f(2.1) - f(2.2)}{12(0.1)}",
        subtext="Nilai Eksak: f'(2,0) = 3e² ≈ 22,167168")
    add_card(s26, Inches(0.8), Inches(3.6), Inches(6.2), Inches(3.0), "Tahapan Perhitungan", [
        "1. Masukkan Nilai dari Tabel:",
        "   = [10,889365 - 8(12,703199) + 8(17,148957) - 19,855030] / 1,2",
        "2. Kalikan Bobot: = 26,600399 / 1,2",
        "3. Bagi dengan 12h = 1,2:",
        "   = 22,166999"
    ], "Langkah 1-3", accent_color=COLOR_PRIMARY)
    add_card(s26, Inches(7.3), Inches(3.6), Inches(5.233), Inches(3.0), "Evaluasi & Komparasi Galat", [
        "Hasil Lima Titik Tengah = 22,166999",
        "Nilai Eksak             = 22,167168",
        "",
        "Galat Absolut:",
        "|22,167168 - 22,166999| = 1,69 x 10⁻⁴ (0,000169)",
        "",
        "Perbandingan: Tiga titik tengah bergalat 6,16 x 10⁻². Lima titik tengah > 364x LEBIH AKURAT!"
    ], "Langkah 4", accent_color=COLOR_EMERALD)

# =========================================================================
    # SLIDE 27: ANALISIS GALAT
    # =========================================================================
    s27 = add_base_slide("Analisis Galat", "Galat atau Kesalahan Pendekatan", 27,
        "Setiap rumus yang kita pakai hanya pendekatan. Galat pemotongan muncul karena suku dibuang. Orde O(h), O(h²), O(h⁴) menunjukkan kecepatan galat mengecil.")
    add_card(s27, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.7), "Konsep Dasar Galat", [
        "Turunan numerik selalu berupa hampiran / pendekatan.",
        "Galat Pemotongan (Truncation Error): Akibat memutus deret tak hingga Taylor.",
        "Galat Bertanda = Eksak - Pendekatan.",
        "Galat Absolut = |Eksak - Pendekatan|.",
        "Pengaruh h: h makin kecil -> galat pemotongan umumnya turun."
    ], "Teori", accent_color=COLOR_PRIMARY)
    add_card(s27, Inches(6.8), Inches(1.8), Inches(5.733), Inches(4.7), "Perbandingan Orde Galat O(h^p)", [
        "Selisih Maju  : O(h)    [Linear, penurunan lambat]",
        "Selisih Mundur: O(h)    [Linear, penurunan lambat]",
        "Selisih Tengah: O(h²)   [Kuadratik, h/2 -> galat / 4]",
        "3 Titik Ujung : O(h²)   [Kuadratik, h/2 -> galat / 4]",
        "5 Titik Tengah: O(h⁴)   [Kuartik, h/2 -> galat / 16! ⭐]",
        "5 Titik Ujung : O(h⁴)   [Kuartik, h/2 -> galat / 16! ⭐]",
        "Notasi Big-O adalah perilaku asimtotik saat h cukup kecil."
    ], "Orde", accent_color=COLOR_EMERALD)

    # =========================================================================
    # SLIDE 28: PENGARUH h & DILEMA PEMBULATAN
    # =========================================================================
    s28 = add_base_slide("Analisis Galat Tambahan", "Pengaruh Nilai h dan Sumber Galat", 28,
        "Ada dua sumber galat berlawanan: pemotongan (mengecil saat h turun) vs pembulatan/noise (membesar saat h turun). Tabel dihitung sendiri dengan e^x di x=1.")
    add_card(s28, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.7), "Trade-off Komputasi", [
        "Galat Pemotongan ~ h^p: Turun saat h mengecil.",
        "Galat Pembulatan / Noise ~ δ/h: Naik saat h mengecil!",
        "Total Galat (Tengah): E(h) ≤ (M h² / 6) + (δ / h)",
        "Langkah Optimum: h* ≈ ³√(3δ / M)",
        "Peringatan: Nilai h yang terlalu kecil TIDAK SELALU lebih akurat!"
    ], "Model", accent_color=COLOR_AMBER)
    add_table_data(s28, Inches(6.8), Inches(1.8), Inches(5.733), Inches(4.7),
        ["Langkah h", "Galat Maju", "Galat Tengah"],
        [
            ["10⁻¹", "1,41 × 10⁻¹", "4,53 × 10⁻³"],
            ["10⁻⁴", "1,36 × 10⁻⁴", "4,53 × 10⁻⁹"],
            ["10⁻⁶", "1,36 × 10⁻⁶", "1,63 × 10⁻¹⁰ (Optimum Tengah) ⭐"],
            ["10⁻⁸", "6,60 × 10⁻⁹ (Optimum Maju) ⭐", "6,60 × 10⁻⁹"],
            ["10⁻¹²", "4,32 × 10⁻⁴ (Naik kembali)", "2,10 × 10⁻⁴ (Naik kembali)"],
            ["10⁻¹⁴", "9,34 × 10⁻³ (Naik kembali)", "9,34 × 10⁻³ (Naik kembali)"]
        ])

    # =========================================================================
    # SLIDE 29: GALAT ABSOLUT, RELATIF, PERSENTASE
    # =========================================================================
    s29 = add_base_slide("Analisis Galat Tambahan", "Galat Absolut, Relatif, dan Persentase", 29,
        "Slide ini melengkapi slide galat: Ea memberi satuan turunan, Er membandingkan dengan besar turunan, E_% adalah Er x 100. Jika turunan nol, Er tidak terdefinisi.")
    add_math_box(s29, Inches(0.8), Inches(1.8), Inches(3.6), Inches(2.2),
        "Galat Absolut (Ea)",
        latex=r"E_a = |f'(x) - D(h)|",
        subtext="Satuan sama dengan turunan f'")
    add_math_box(s29, Inches(4.8), Inches(1.8), Inches(3.6), Inches(2.2),
        "Galat Relatif (Er)",
        latex=r"E_r = \frac{|f'(x) - D(h)|}{|f'(x)|}",
        subtext="Ukuran proporsional tanpa satuan")
    add_math_box(s29, Inches(8.8), Inches(1.8), Inches(3.733), Inches(2.2),
        "Galat Persentase (E%)",
        latex=r"E_{\%} = E_r \times 100\%",
        subtext="Format persentase praktis")

    add_card(s29, Inches(0.8), Inches(4.3), Inches(11.733), Inches(2.3), "Contoh Aplikasi: Kasus ln x di x = 1,8 (h = 0,1)", [
        "Dh = 0,5406722  dan  f'(1,8) = 0,5555556",
        "Ea = |0,5555556 - 0,5406722| = 0,0148834",
        "Er = 0,0148834 / 0,5555556 ≈ 0,0267901",
        "E% ≈ 2,679%",
        "Perhatian Khusus: Jika f'(x) = 0, Er tidak terdefinisi (pembagian nol). Gunakan Ea!"
    ], "Aplikasi", accent_color=COLOR_PRIMARY)

    # =========================================================================
    # SLIDE 30: METODE EKSTRAPOLASI RICHARDSON
    # =========================================================================
    s30 = add_base_slide("Ekstrapolasi Richardson", "Metode Ekstrapolasi Richardson", 30,
        "Richardson tidak membuat rumus turunan baru dari data; ia menggabungkan dua hasil yang sudah ada. Hitung D(h) dan D(2h), lalu tambahkan koreksi [D(h) − D(2h)]/(2ⁿ − 1). Untuk selisih tengah galatnya O(h²), jadi n = 2 dan rumusnya (4D(h) − D(2h))/3 dengan orde O(h⁴). Untuk selisih maju n = 1. Di buku, langkah besar ditulis h dan langkah kecil h/2, jadi D(h) di slide ini sama dengan N₁(h/2) di buku. Pilih n sesuai bentuk galat pendekatan awal.")

    add_custom_card(s30, Inches(0.8), Inches(1.8), Inches(5.6), Inches(1.8), "Pengertian", [
        "Menggabungkan dua pendekatan dengan ukuran langkah berbeda untuk membuang suku galat utama, sehingga hasilnya lebih teliti."
    ], border_color=COLOR_EMERALD, title_color=COLOR_EMERALD)

    add_custom_card(s30, Inches(0.8), Inches(3.8), Inches(5.6), Inches(2.6), "Prinsip kerja", [
        "1. Hitung pendekatan turunan dengan langkah h → D(h)",
        "2. Hitung pendekatan dengan langkah 2h → D(2h)",
        "3. Gabungkan keduanya untuk mengurangi galat utama"
    ], border_color=COLOR_EMERALD, title_color=COLOR_EMERALD)

    add_custom_card(s30, Inches(6.8), Inches(1.8), Inches(5.733), Inches(3.1), "Rumus umum", [
        "• f′₀ : nilai turunan di x₀ setelah ekstrapolasi",
        "• D(h) : hasil pendekatan turunan langkah h (lebih kecil)",
        "• D(2h) : hasil pendekatan turunan langkah 2h (dua kali lebih besar)",
        "• n : orde galat awal, yaitu O(hⁿ)",
        "Kedua hasil digabung untuk menghilangkan suku galat utama."
    ], border_color=COLOR_EMERALD, title_color=COLOR_EMERALD,
    latex=r"f'_0 \approx D(h) + \frac{D(h) - D(2h)}{2^n - 1}")

    add_custom_card(s30, Inches(6.8), Inches(5.05), Inches(5.733), Inches(1.35), "Contoh: selisih tengah (n = 2)", [
        "Orde galat naik secara signifikan: O(h²) → O(h⁴) ⭐"
    ], border_color=COLOR_AMBER, title_color=COLOR_AMBER,
    latex=r"f'_0 \approx \frac{4 D(h) - D(2h)}{3}")

    fn_box = s30.shapes.add_textbox(Inches(0.8), Inches(6.5), Inches(11.733), Inches(0.25))
    fn_tf = fn_box.text_frame
    fn_p = fn_tf.paragraphs[0]
    fn_p.text = "Kaitan notasi slide berikut: D(h) = N₁(h/2), D(2h) = N₁(h). Untuk n = 1 (selisih maju): 2D(h) − D(2h)."
    fn_p.font.name = FONT_MAIN
    fn_p.font.size = Pt(9.5)
    fn_p.font.color.rgb = COLOR_MUTED

    # =========================================================================
    # SLIDE 31: CONTOH 6.2.1 RICHARDSON f(x) = ln x
    # =========================================================================
    s31 = add_base_slide("Contoh 6.2.1", "Contoh Richardson pada f(x) = ln x", 31,
        "Galat awal selisih maju berorde h, jadi pakai rumus n = 1: dua kali hasil yang lebih teliti dikurangi hasil yang kurang teliti. Hitung: 2 × 0,5479795 = 1,0959590; dikurangi 0,5406722 menghasilkan 0,5553968. Galat tiap hasil dihitung dari nilai eksak 0,5555556. Buku menulis hasil 0,555397 dan galat 0,000258; hitung ulang dari angka buku memberi 0,0002688, dan kami memakai angka yang konsisten dengan digit di slide.")

    add_custom_card(s31, Inches(0.8), Inches(1.8), Inches(5.6), Inches(1.6), "Diketahui:", [
        "f(x) = ln x,  x₀ = 1,8",
        "N₁(0,1) = 0,5406722  ·  N₁(0,05) = 0,5479795",
        "Selisih maju: galat O(h), jadi n = 1"
    ], border_color=COLOR_EMERALD, title_color=COLOR_EMERALD)

    add_custom_card(s31, Inches(0.8), Inches(3.6), Inches(5.6), Inches(2.1), "Perhitungan", [
        "= 2(0,5479795) - 0,5406722",
        "= 0,5553968 ⭐ (39x lebih teliti dari N₁(0,05))"
    ], border_color=COLOR_EMERALD, title_color=COLOR_EMERALD,
    latex=r"N_2(0.1) = 2 N_1(0.05) - N_1(0.1)")

    add_table_data(s31, Inches(6.8), Inches(1.8), Inches(5.733), Inches(1.9),
        ["Metode", "Hasil", "Galat absolut"],
        [
            ["Selisih maju, h = 0,1", "0,5406722", "0,0148834"],
            ["Selisih maju, h = 0,05", "0,5479795", "0,0075761"],
            ["Richardson", "0,5553968", "0,0002688 ⭐"],
            ["Nilai eksak", "0,5555556", "—"]
        ])

    buf_chart, chart_w, chart_h = generate_error_bar_chart()
    chart_card = s31.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(3.9), Inches(5.733), Inches(1.85))
    chart_card.fill.solid()
    chart_card.fill.fore_color.rgb = COLOR_CARD
    chart_card.line.color.rgb = COLOR_BORDER
    chart_card.line.width = Pt(1)

    chart_target_w = 5.5
    chart_target_h = chart_target_w * (chart_h / chart_w)
    s31.shapes.add_picture(buf_chart, Inches(6.9), Inches(3.95), Inches(chart_target_w), Inches(chart_target_h))

    add_callout_banner(s31, Inches(0.8), Inches(5.95), Inches(11.733), Inches(0.68),
        "Kesimpulan: Richardson mengurangi galat sekitar 39 kali dibanding selisih maju dengan h = 0,05 (0,0075761 ÷ 0,0002688 ≈ 39).")

    # =========================================================================
    # SLIDE 32: CONTOH 6.1.2 DATA TABEL f(x) = x e^x
    # =========================================================================
    s32 = add_base_slide("Contoh 6.1.2", "Perbandingan Metode Diferensiasi pada Data Tabel", 32,
        "Semua hasil dihitung dari lima nilai tabel, bukan dari rumus fungsi. Nilai eksak 3e² ≈ 22,167168 hanya dipakai sebagai pembanding. Galat absolut dihitung |eksak − pendekatan|: 0,134858; 0,061622; 0,000169. Lima titik tengah paling dekat karena galatnya O(h⁴), sedangkan dua rumus lain O(h²). Tiga titik tengah dengan h berbeda nantinya menjadi bahan Richardson pada slide 23.")

    left_box = s32.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(4.6), Inches(4.7))
    left_box.fill.solid()
    left_box.fill.fore_color.rgb = COLOR_CARD
    left_box.line.color.rgb = COLOR_BORDER

    tb_fn = s32.shapes.add_textbox(Inches(1.0), Inches(1.95), Inches(4.2), Inches(0.4))
    tf_fn = tb_fn.text_frame
    p_fn = tf_fn.paragraphs[0]
    p_fn.text = "f(x) = xeˣ,  x₀ = 2,0,  h = 0,1"
    p_fn.font.name = FONT_MAIN
    p_fn.font.size = Pt(13)
    p_fn.font.bold = True
    p_fn.font.color.rgb = COLOR_PRIMARY

    add_table_data(s32, Inches(1.0), Inches(2.45), Inches(4.2), Inches(3.8),
        ["x", "f(x)"],
        [
            ["1,8", "10,889365"],
            ["1,9", "12,703199"],
            ["2,0", "14,778112"],
            ["2,1", "17,148957"],
            ["2,2", "19,855030"]
        ])

    add_table_data(s32, Inches(5.8), Inches(1.8), Inches(6.733), Inches(2.1),
        ["Metode", "f′(2)", "Galat absolut"],
        [
            ["Tiga titik ujung", "22,032310", "0,134858"],
            ["Tiga titik tengah", "22,239790", "0,061622"],
            ["Lima titik tengah", "22,166999", "0,000169 ⭐"],
            ["Nilai eksak 3e²", "22,167168", "—"]
        ])

    add_callout_banner(s32, Inches(5.8), Inches(4.15), Inches(6.733), Inches(0.65),
        "Kesimpulan: di antara ketiga metode, lima titik tengah paling akurat.")

    add_custom_card(s32, Inches(5.8), Inches(5.0), Inches(6.733), Inches(1.5),
        "Kaitan dengan Richardson:", [
            "Hasil pendekatan turunan dapat dipakai sebagai dasar (N₁) untuk meningkatkan ketelitian lewat ekstrapolasi (slide 23)."
        ], border_color=COLOR_AMBER, title_color=COLOR_AMBER)

    # =========================================================================
    # SLIDE 33: CONTOH 6.1.3 STRATEGI PEMILIHAN RUMUS
    # =========================================================================
    s33 = add_base_slide("Contoh 6.1.3", "Strategi Pemilihan Rumus Diferensiasi", 33,
        "Lihat posisi titik dulu. Di ujung tidak ada data di salah satu sisi, jadi pakai rumus ujung. Di titik dalam bisa pakai rumus tengah, dan lima titik tengah hanya pada x = 1,3 karena butuh dua titik di tiap sisi. Hitungan memakai nilai tabel penuh; buku menampilkannya dibulatkan. Hubungan dengan Richardson: untuk membentuk N₁ dengan h dan h/2, data pada kedua ukuran langkah itu harus ada; ini akan terlihat jelas di slide 24.")

    add_table_data(s33, Inches(0.8), Inches(1.8), Inches(5.3), Inches(2.1),
        ["x", "f(x)", "Posisi titik"],
        [
            ["1,1", "9,025013", "ujung kiri"],
            ["1,2", "11,02318", "interior"],
            ["1,3", "13,46374", "tengah penuh"],
            ["1,4", "16,44465", "interior"],
            ["1,5", "20,08554", "ujung kanan"]
        ])

    tb_h = s33.shapes.add_textbox(Inches(0.8), Inches(3.95), Inches(5.3), Inches(0.3))
    tf_h = tb_h.text_frame
    p_h = tf_h.paragraphs[0]
    p_h.text = "h = 0,1; di ujung kanan h dibuat negatif"
    p_h.font.name = FONT_MAIN
    p_h.font.size = Pt(10)
    p_h.font.color.rgb = COLOR_MUTED

    add_table_data(s33, Inches(6.4), Inches(1.8), Inches(6.133), Inches(2.2),
        ["Titik", "Rumus yang tersedia"],
        [
            ["1,1 (ujung kiri)", "Tiga titik ujung (6.4) · lima titik ujung (6.6)"],
            ["1,2 (interior)", "Tiga titik ujung · tiga titik tengah (6.5)"],
            ["1,3 (tengah penuh)", "6.4 · 6.5 · lima titik tengah (6.7) ⭐"],
            ["1,4 (interior)", "6.4 (h negatif) · 6.5"],
            ["1,5 (ujung kanan)", "6.4 · 6.6 (h negatif)"]
        ])

    add_custom_card(s33, Inches(0.8), Inches(4.35), Inches(5.6), Inches(1.35),
        "Tiga titik ujung, x = 1,1:", [
            "[-3(9,025013) + 4(11,02318) - 13,46374] / 0,2",
            "= 17,76971"
        ], border_color=COLOR_EMERALD, title_color=COLOR_EMERALD)

    add_custom_card(s33, Inches(6.8), Inches(4.35), Inches(5.733), Inches(1.35),
        "Lima titik tengah, x = 1,3:", [
            "[9,025013 - 8(11,02318) + 8(16,44465) - 20,08554] / 1,2",
            "= 26,92603 ⭐"
        ], border_color=COLOR_EMERALD, title_color=COLOR_EMERALD)

    add_callout_banner(s33, Inches(0.8), Inches(5.85), Inches(11.733), Inches(0.75),
        "Kesimpulan: pilih rumus menurut posisi titik dan ketersediaan data. Kaitan dengan Richardson: ekstrapolasi membutuhkan data yang sesuai dengan ukuran langkah yang dipakai (h dan setengahnya).")

    # =========================================================================
    # SLIDE 34: CONTOH 6.2.2 RICHARDSON BERTINGKAT PADA f(x) = xeˣ
    # =========================================================================
    s34 = add_base_slide("Contoh 6.2.2", "Richardson Bertingkat pada f(x) = xeˣ", 34,
        "Tiga tahap: (1) hitung N₁ dengan selisih tengah untuk h = 0,2; 0,1; 0,05; (2) gabungkan pasangan yang bertetangga dengan pembagi 3 → N₂(0,2) dan N₂(0,1); (3) gabungkan kedua N₂ dengan pembagi 15 → N₃(0,2). Angka dalam kurung adalah ukuran langkah. Ini angka buku; hitung ulang dari tabel Contoh 6.1.2 memberi N₁(0,2) = 22,414163 dan N₁(0,1) = 22,239790 (selisih kecil di digit ke-6). Rumus N₃ di buku tertulis memakai N₁(0,2), tetapi angkanya cocok dengan N₂(0,2). Galat N₃ nol hanya pada enam desimal yang ditampilkan, bukan bukti kesamaan matematis.")

    tb_sub = s34.shapes.add_textbox(Inches(0.8), Inches(1.4), Inches(11.733), Inches(0.35))
    tf_sub = tb_sub.text_frame
    p_sub = tf_sub.paragraphs[0]
    p_sub.text = "x = 2, nilai eksak f′(2) = 22,167168  ·  N₁: selisih tengah, galat pangkat genap"
    p_sub.font.name = FONT_MAIN
    p_sub.font.size = Pt(11)
    p_sub.font.color.rgb = COLOR_MUTED

    add_custom_card(s34, Inches(0.8), Inches(1.8), Inches(3.4), Inches(2.4),
        "Tahap 1 — N₁", [
            "N₁(0,2) = 22,414160",
            "N₁(0,1) = 22,239786",
            "N₁(0,05) = 22,182564",
            "Nilai N₁(0,05) dihitung menggunakan f(x) = xeˣ karena titik x = 1,95 dan 2,05 tidak ada pada tabel."
        ], border_color=COLOR_BLUE, title_color=COLOR_BLUE)

    arr1 = s34.shapes.add_textbox(Inches(4.25), Inches(2.7), Inches(0.5), Inches(0.5))
    arr1.text_frame.paragraphs[0].text = "→"
    arr1.text_frame.paragraphs[0].font.size = Pt(22)
    arr1.text_frame.paragraphs[0].font.bold = True
    arr1.text_frame.paragraphs[0].font.color.rgb = COLOR_MUTED

    add_custom_card(s34, Inches(4.75), Inches(1.8), Inches(3.7), Inches(2.4),
        "Tahap 2 — N₂ (÷3)", [
            "N₂(0,2) = 22,239786 + (22,239786 − 22,414160)/3 = 22,166995",
            "",
            "N₂(0,1) = 22,182564 + (22,182564 − 22,239786)/3 = 22,167157"
        ], border_color=COLOR_EMERALD, title_color=COLOR_EMERALD)

    arr2 = s34.shapes.add_textbox(Inches(8.5), Inches(2.7), Inches(0.5), Inches(0.5))
    arr2.text_frame.paragraphs[0].text = "→"
    arr2.text_frame.paragraphs[0].font.size = Pt(22)
    arr2.text_frame.paragraphs[0].font.bold = True
    arr2.text_frame.paragraphs[0].font.color.rgb = COLOR_MUTED

    add_custom_card(s34, Inches(9.0), Inches(1.8), Inches(3.533), Inches(2.4),
        "Tahap 3 — N₃ (÷15)", [
            "N₃(0,2) = 22,167157 + (22,167157 − 22,166995)/15",
            "",
            "= 22,167168 ⭐ (Identik Eksak)"
        ], border_color=COLOR_AMBER, title_color=COLOR_AMBER)

    add_table_data(s34, Inches(0.8), Inches(4.35), Inches(11.733), Inches(1.35),
        ["Tingkat", "N₁(0,2)", "N₁(0,1)", "N₁(0,05)", "N₂(0,2)", "N₂(0,1)", "N₃(0,2)", "Eksak"],
        [
            ["Hasil", "22,414160", "22,239786", "22,182564", "22,166995", "22,167157", "22,167168 ⭐", "22,167168"],
            ["Galat absolut", "0,246992", "0,061618", "0,015396", "0,000173", "0,000011", "0,000000", "—"]
        ])

    add_callout_banner(s34, Inches(0.8), Inches(5.85), Inches(11.733), Inches(0.75),
        "Kesimpulan: Richardson bertingkat meningkatkan ketelitian secara bertahap: N₁ → N₂ → N₃ (N₃ sama dengan eksak pada enam desimal yang ditampilkan).")

    # =========================================================================
    # SLIDE 35: CONTOH 6.2.3 RICHARDSON DENGAN KETERBATASAN DATA
    # =========================================================================
    s35 = add_base_slide("Contoh 6.2.3", "Richardson dengan Keterbatasan Data", 35,
        "Titik x₀ = 1,3 dengan h = 0,2 dan 0,1; N₁(0,2) memakai f(1,5) dan f(1,1), N₁(0,1) memakai f(1,4) dan f(1,2). Gabungkan dengan pembagi 3 untuk N₂(0,2). Tingkat ketiga butuh N₁(0,05) dengan f(1,35) dan f(1,25), yang tidak ada di tabel, sehingga berhenti di N₂. Catatan untuk penyaji: Slide menampilkan hasil hitung ulang 26,926027 (dari data tabel yang tersedia); angka 26,920273 adalah yang tercetak di buku.")

    add_table_data(s35, Inches(0.8), Inches(1.8), Inches(4.5), Inches(2.4),
        ["x", "f(x)"],
        [
            ["1,1", "9,025013"],
            ["1,2", "11,02318"],
            ["1,3", "13,46374"],
            ["1,4", "16,44465"],
            ["1,5", "20,08554"]
        ])

    tb_x0 = s35.shapes.add_textbox(Inches(0.8), Inches(4.25), Inches(4.5), Inches(0.35))
    tb_x0.text_frame.paragraphs[0].text = "x₀ = 1,3;  h = 0,2"
    tb_x0.text_frame.paragraphs[0].font.name = FONT_MAIN
    tb_x0.text_frame.paragraphs[0].font.size = Pt(11)
    tb_x0.text_frame.paragraphs[0].font.bold = True
    tb_x0.text_frame.paragraphs[0].font.color.rgb = COLOR_PRIMARY

    add_custom_card(s35, Inches(5.6), Inches(1.8), Inches(6.933), Inches(1.2),
        "Tahap 1 — N₁", [
            "N₁(0,2) = (20,08554 − 9,025013) / 0,4 = 27,651318",
            "N₁(0,1) = (16,44465 − 11,02318) / 0,2 = 27,107350"
        ], border_color=COLOR_BLUE, title_color=COLOR_BLUE)

    add_custom_card(s35, Inches(5.6), Inches(3.1), Inches(6.933), Inches(1.2),
        "Tahap 2 — N₂", [
            "N₂(0,2) = 27,107350 + (27,107350 − 27,651318) / 3",
            "= 26,926027 ⭐ (Orde O(h⁴))"
        ], border_color=COLOR_EMERALD, title_color=COLOR_EMERALD)

    add_custom_card(s35, Inches(0.8), Inches(4.65), Inches(11.733), Inches(0.95),
        "Mengapa N₃ tidak dapat dihitung?", [
            "N₃ membutuhkan N₁(0,05) = [f(1,35) − f(1,25)] / 0,1, sedangkan f(1,25) dan f(1,35) tidak tersedia pada tabel."
        ], border_color=COLOR_AMBER, title_color=COLOR_AMBER)

    add_callout_banner(s35, Inches(0.8), Inches(5.8), Inches(11.733), Inches(0.8),
        "Kesimpulan: Richardson tidak dapat dilanjutkan ke tingkat berikutnya bila data yang diperlukan tidak tersedia.\nCatatan: Hasil perhitungan menggunakan data tabel yang tersedia.")

    # =========================================================================
    # SLIDE 36: RINGKASAN METODE: PERBANDINGAN
    # =========================================================================
    s36 = add_base_slide("Ringkasan Metode", "Perbandingan Metode Diferensiasi Numerik", 36,
        "Gunakan tabel ini untuk merangkum. Maju/mundur O(h), tengah & 3 titik ujung O(h²), lima titik O(h⁴). Richardson memperbaiki hasil rumus lain.")
    add_table_data(s36, Inches(0.8), Inches(1.8), Inches(11.733), Inches(4.8),
        ["Metode", "Titik / Data", "Galat", "Kelebihan", "Keterbatasan"],
        [
            ["Selisih Maju", "x, x+h", "O(h)", "Sederhana, 2 nilai", "Kurang teliti"],
            ["Selisih Mundur", "x-h, x", "O(h)", "Cocok di ujung kanan", "Kurang teliti"],
            ["Selisih Tengah", "x-h, x+h", "O(h²)", "Simetris, lebih teliti", "Perlu data 2 sisi"],
            ["3 Titik Ujung", "x₀, x₀+h, x₀+2h", "O(h²)", "Di ujung interval", "Butuh 3 nilai"],
            ["5 Titik Tengah", "x₀±h, x₀±2h", "O(h⁴) ⭐", "Sangat teliti & presisi", "Butuh 5 nilai simetris"],
            ["5 Titik Ujung", "x₀ ... x₀+4h", "O(h⁴) ⭐", "Teliti di ujung satu sisi", "Butuh 5 nilai"],
            ["Richardson", "N₁(h), N₁(h/2)", "Tinggi", "Mendongkrak ketelitian", "Bentuk galat harus sesuai"]
        ])

    # =========================================================================
    # SLIDE 37: MEMILIH METODE & KONDISI
    # =========================================================================
    s37 = add_base_slide("Ringkasan Metode", "Memilih Metode: Rumus & Kondisi Penggunaan", 37,
        "Slide ini fokus pada kapan rumus dipakai. Pesan penutup: jangan menyimpulkan satu metode selalu paling baik. Lima titik memiliki koefisien besar sehingga lebih sensitif terhadap noise.")
    add_table_data(s37, Inches(0.8), Inches(1.8), Inches(11.733), Inches(4.3),
        ["Metode", "Rumus Dasar", "Orde", "Kondisi Penggunaan"],
        [
            ["Selisih Maju", "[f(x+h) - f(x)] / h", "O(h)", "Ujung kiri data; hanya ada data ke depan"],
            ["Selisih Mundur", "[f(x) - f(x-h)] / h", "O(h)", "Ujung kanan data; hanya ada data ke belakang"],
            ["Selisih Tengah", "[f(x+h) - f(x-h)] / 2h", "O(h²)", "Titik dalam; pilihan umum paling seimbang"],
            ["3 Titik Ujung", "[-3f₀ + 4f₁ - f₂] / 2h", "O(h²)", "Ujung interval yang membutuhkan akurasi orde 2"],
            ["5 Titik Tengah", "[f₋₂ - 8f₋₁ + 8f₁ - f₂] / 12h", "O(h⁴)", "Titik dalam; data rapat dan fungsi mulus"],
            ["5 Titik Ujung", "[-25f₀ + 48f₁ - 36f₂ + 16f₃ - 3f₄]/12h", "O(h⁴)", "Ujung interval yang membutuhkan akurasi orde 4"],
            ["Richardson", "Eliminasi galat N₁(h) & N₁(h/2)", "Tinggi", "Tersedia multi-langkah & bentuk galat sesuai"]
        ])
    add_card(s37, Inches(0.8), Inches(6.2), Inches(11.733), Inches(0.55), "Keterangan", [
        "Tidak ada metode yang selalu terbaik di segala situasi: perhatikan noise data dan kestabilan pembulatan!"
    ], accent_color=COLOR_PRIMARY)

    # =========================================================================
    # SLIDE 38: KESIMPULAN
    # =========================================================================
    s38 = add_base_slide("Penutup", "Kesimpulan", 38,
        "Rangkum perjalanan dari definisi, deret, rumus 2, 3, 5 titik, galat, lalu Richardson. Tutup dengan kutipan penting.")
    add_card(s38, Inches(0.8), Inches(1.8), Inches(6.0), Inches(4.7), "Poin-Poin Kunci", [
        "Diferensiasi numerik memperkirakan turunan dari nilai fungsi diskret.",
        "Pendekatan deret (Lagrange & Taylor) menjadi fondasi matematis utama.",
        "Selisih maju dan mundur: galat pemotongan O(h).",
        "Selisih tengah dan tiga titik ujung: galat O(h²).",
        "Lima titik (tengah dan ujung): ketelitian tinggi O(h⁴).",
        "Ekstrapolasi Richardson meningkatkan ketelitian secara signifikan.",
        "Pilih h dengan cermat mengingat trade-off pemotongan vs pembulatan."
    ], "Ringkasan", accent_color=COLOR_PRIMARY)
    add_card(s38, Inches(7.2), Inches(1.8), Inches(5.333), Inches(4.7), "Prinsip Utama", [
        "\"Ketelitian diferensiasi numerik tidak hanya ditentukan oleh rumus yang digunakan, tetapi juga oleh ukuran langkah, data yang tersedia, dan sifat fungsi.\"",
        "",
        "Keseimbangan Komputasi:",
        "• Orde tinggi butuh lebih banyak data & sensitif terhadap noise.",
        "• Nilai h terlalu kecil memperbesar galat pembulatan komputer.",
        "• Selalu sesuaikan metode dengan posisi titik data!"
    ], "Intisari", accent_color=COLOR_EMERALD)

    # =========================================================================
    # SLIDE 39: PENUTUP / TERIMA KASIH (HERO CENTERED & MINIMALIST)
    # =========================================================================
    s39 = prs.slides.add_slide(blank_layout)
    bg39 = s39.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg39.fill.solid()
    bg39.fill.fore_color.rgb = COLOR_BG
    bg39.line.fill.background()

    notes_slide39 = s39.notes_slide
    tf_notes39 = notes_slide39.notes_text_frame
    tf_notes39.text = "Ucapkan terima kasih kepada dosen pengampu dan rekan-rekan mahasiswa atas perhatian selama presentasi berlangsung. Buka kesempatan bagi audiens untuk sesi tanya jawab dan diskusi mengenai materi diferensiasi numerik."

    pill39 = s39.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.3), Inches(1.1), Inches(4.733), Inches(0.42))
    pill39.fill.solid()
    pill39.fill.fore_color.rgb = COLOR_PRIMARY_SOFT
    pill39.line.color.rgb = COLOR_BORDER
    p_pill = pill39.text_frame.paragraphs[0]
    p_pill.text = "DIFERENSIASI NUMERIK & EKSTRAPOLASI RICHARDSON"
    p_pill.font.name = FONT_MAIN
    p_pill.font.size = Pt(10)
    p_pill.font.bold = True
    p_pill.font.color.rgb = COLOR_PRIMARY
    p_pill.alignment = PP_ALIGN.CENTER

    hero_box = s39.shapes.add_textbox(Inches(1.0), Inches(1.85), Inches(11.333), Inches(3.2))
    htf = hero_box.text_frame
    htf.word_wrap = True
    htf.margin_top = Inches(0)
    htf.margin_bottom = Inches(0)

    hp1 = htf.paragraphs[0]
    hp1.text = "TERIMA KASIH"
    hp1.font.name = FONT_MAIN
    hp1.font.size = Pt(56)
    hp1.font.bold = True
    hp1.font.color.rgb = COLOR_PRIMARY
    hp1.alignment = PP_ALIGN.CENTER
    hp1.space_after = Pt(14)

    hp2 = htf.add_paragraph()
    hp2.text = "Sesi Tanya Jawab & Diskusi"
    hp2.font.name = FONT_MAIN
    hp2.font.size = Pt(22)
    hp2.font.bold = True
    hp2.font.color.rgb = COLOR_TEXT
    hp2.alignment = PP_ALIGN.CENTER
    hp2.space_after = Pt(10)

    hp3 = htf.add_paragraph()
    hp3.text = "Silakan ajukan pertanyaan atau tanggapan terkait materi yang telah dipaparkan."
    hp3.font.name = FONT_MAIN
    hp3.font.size = Pt(13.5)
    hp3.font.color.rgb = COLOR_MUTED
    hp3.alignment = PP_ALIGN.CENTER

    credit_box = s39.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.2), Inches(5.35), Inches(8.933), Inches(0.95))
    credit_box.fill.solid()
    credit_box.fill.fore_color.rgb = COLOR_CARD
    credit_box.line.color.rgb = COLOR_BORDER
    ctf = credit_box.text_frame
    ctf.word_wrap = True
    ctf.margin_top = Inches(0.12)

    cp1 = ctf.paragraphs[0]
    cp1.text = "Kelompok: Farel Luther S.   •   Fatih Taqiyyuddin   •   Siti Zulayka M. A.   •   Keegan Gibran J."
    cp1.font.name = FONT_MAIN
    cp1.font.size = Pt(11.5)
    cp1.font.bold = True
    cp1.font.color.rgb = COLOR_TEXT
    cp1.alignment = PP_ALIGN.CENTER
    cp1.space_after = Pt(3)

    cp2 = ctf.add_paragraph()
    cp2.text = "Dosen Pengampu: Debi Yandra Niska, S.Kom., M.Kom.    |    Tahun Akademik: 2026"
    cp2.font.name = FONT_MAIN
    cp2.font.size = Pt(10.5)
    cp2.font.color.rgb = COLOR_MUTED
    cp2.alignment = PP_ALIGN.CENTER

    line39 = s39.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(6.8), Inches(11.733), Inches(0.015))
    line39.fill.solid()
    line39.fill.fore_color.rgb = COLOR_BORDER
    line39.line.fill.background()

    footer39 = s39.shapes.add_textbox(Inches(0.8), Inches(6.85), Inches(11.733), Inches(0.4))
    ftf39 = footer39.text_frame
    ftf39.margin_top = Inches(0)
    fp39 = ftf39.paragraphs[0]
    fp39.text = "Metode Numerik — Imron dkk. (2022) | Slide 39 dari 39"
    fp39.font.name = FONT_MAIN
    fp39.font.size = Pt(10)
    fp39.font.color.rgb = COLOR_MUTED
    fp39.alignment = PP_ALIGN.CENTER

    # Save presentation
    output_path = "Diferensiasi_Numerik.pptx"
    prs.save(output_path)
    print(f"Base presentation (39 slides) saved successfully to: {output_path}")

    # Apply slide transitions & shape build animations
    abs_path = os.path.abspath(output_path)
    apply_powerpoint_animations(abs_path)
    print(f"Presentation with full animations & transitions ready: {output_path}")

def apply_powerpoint_animations(pptx_path):
    """
    Applies native PowerPoint 3D slide transitions & shape build entrance animations.
    Uses PowerPoint COM automation on Windows with graceful fallback.
    """
    ps_script = f'''
$ErrorActionPreference = "Stop"
try {{
    $ppt = New-Object -ComObject PowerPoint.Application
    $pres = $ppt.Presentations.Open("{pptx_path}", [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoFalse)
    
    # 39 Transition sequence matching web presentation 3D effects
    $effects = @(
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectFadeSmoothly,          # 1: Cover
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectPageCurlSingleRight,   # 2: Center-fold
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectPeelOffRight,          # 3: Bottom-right curl
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectCurtains,              # 4: Curtain roll
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectBoxLeft,               # 5: 3D Box / Cube
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectDoorsVertical,         # 6: Doors 3D
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectWipeRight,             # 7: Diagonal wipe
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectPageCurlSingleRight,   # 8: Center-fold
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectPeelOffRight,          # 9: Bottom-right curl
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectCurtains,              # 10: Curtain roll
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectBoxLeft,               # 11: 3D Box / Cube
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectDoorsVertical,         # 12: Doors 3D
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectPageCurlSingleRight,   # 13: Center-fold
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectPeelOffRight,          # 14: Bottom-right curl
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectCurtains,              # 15: Curtain roll
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectBoxLeft,               # 16: 3D Box / Cube
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectPageCurlSingleRight,   # 17: Center-fold
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectPeelOffRight,          # 18: Bottom-right curl
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectCurtains,              # 19: Curtain roll
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectDoorsVertical,         # 20: Doors 3D
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectPageCurlSingleRight,   # 21: Center-fold
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectPeelOffRight,          # 22: Bottom-right curl
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectCurtains,              # 23: Curtain roll
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectWipeRight,             # 24: Diagonal wipe
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectBoxLeft,               # 25: 3D Box / Cube
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectPageCurlSingleRight,   # 26: Center-fold
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectBoxLeft,               # 27: 3D Box / Cube
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectCurtains               # 39: Curtain roll
    )
    
    for ($i = 1; $i -le $pres.Slides.Count; $i++) {{
        $slide = $pres.Slides.Item($i)
        $effIdx = ($i - 1) % $effects.Count
        $slide.SlideShowTransition.EntryEffect = $effects[$effIdx]
        $slide.SlideShowTransition.Duration = 1.0
        
        $shapeCount = $slide.Shapes.Count
        if ($shapeCount -gt 3) {{
            for ($s = 4; $s -le $shapeCount; $s++) {{
                $shape = $slide.Shapes.Item($s)
                try {{
                    $anim = $slide.TimeLine.MainSequence.AddEffect($shape, 10, 0, 3)
                    $anim.Timing.Duration = 0.4
                }} catch {{}}
            }}
        }}
    }}
    
    $pres.Save()
    
    # --- Pixel-perfect PDF: export each slide as high-res PNG ---
    $exportDir = Join-Path (Split-Path "{pptx_path}") "_slide_exports"
    if (Test-Path $exportDir) {{ Remove-Item $exportDir -Recurse -Force }}
    New-Item -ItemType Directory -Path $exportDir | Out-Null
    
    for ($i = 1; $i -le $pres.Slides.Count; $i++) {{
        $slide = $pres.Slides.Item($i)
        $pngPath = Join-Path $exportDir ("slide_{{0:D2}}.png" -f $i)
        $slide.Export($pngPath, "PNG", 1920, 1080)
    }}
    Write-Output "PowerPoint COM: Exported $($pres.Slides.Count) slides as PNG to $exportDir"
    
    $pres.Close()
    $ppt.Quit()
    Write-Output "PowerPoint COM: Applied slide transitions and entrance animations to all 39 slides."
}} catch {{
    if ($ppt) {{ $ppt.Quit() }}
    Write-Warning "PowerPoint COM unavailable or encountered error: $_"
}}
'''
    try:
        import subprocess
        res = subprocess.run(["powershell", "-NoProfile", "-Command", ps_script], capture_output=True, text=True)
        if res.stdout:
            print(res.stdout.strip())
        if res.returncode != 0 and res.stderr:
            print("Note (COM fallback):", res.stderr.strip())
    except Exception as e:
        print(f"COM animation helper skipped: {e}")

    # --- Assemble PNGs into pixel-perfect PDF ---
    import glob
    export_dir = os.path.join(os.path.dirname(pptx_path), "_slide_exports")
    png_files = sorted(glob.glob(os.path.join(export_dir, "slide_*.png")))
    
    if png_files:
        try:
            import pymupdf
            pdf_path = pptx_path.replace(".pptx", ".pdf")
            doc = pymupdf.open()
            
            for png_file in png_files:
                img = pymupdf.open(png_file)
                img_page = img[0]
                rect = img_page.rect
                
                page = doc.new_page(width=rect.width, height=rect.height)
                page.insert_image(page.rect, filename=png_file)
                img.close()
            
            doc.save(pdf_path, deflate=True, garbage=4)
            doc.close()
            print(f"Pixel-perfect PDF assembled: {pdf_path} ({len(png_files)} pages)")
        except Exception as e:
            print(f"PDF assembly error: {e}")
        finally:
            import shutil
            if os.path.exists(export_dir):
                shutil.rmtree(export_dir)
                print("Cleaned up temporary PNG exports.")
    else:
        print("Warning: No PNG exports found, PDF not generated.")

if __name__ == "__main__":
    create_presentation()
