import os
# Presentation generator script for Diferensiasi Numerik (Metode Numerik)
from pptx import Presentation  # type: ignore
from pptx.util import Inches, Pt  # type: ignore
from pptx.dml.color import RGBColor  # type: ignore
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR  # type: ignore
from pptx.enum.shapes import MSO_SHAPE  # type: ignore

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
        fp.text = f"Metode Numerik — Imron dkk. (2022) | Slide {slide_num} dari 21"
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

        tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.08), width - Inches(0.4), height - Inches(0.16))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0)
        tf.margin_bottom = Inches(0)
        p = tf.paragraphs[0]
        p.text = text
        p.font.name = FONT_MAIN
        p.font.size = Pt(11)
        p.font.color.rgb = RGBColor(120, 53, 15) if is_amber else RGBColor(6, 78, 59)

    def add_custom_card(slide, left, top, width, height, title, items, border_color=None, bg_color=None, title_color=None):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color if bg_color else COLOR_CARD
        card.line.color.rgb = border_color if border_color else COLOR_BORDER
        card.line.width = Pt(1.5 if border_color else 1)

        tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.12), width - Inches(0.4), height - Inches(0.24))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0)
        tf.margin_bottom = Inches(0)
        tf.margin_left = Inches(0)
        tf.margin_right = Inches(0)

        if title:
            p_title = tf.paragraphs[0]
            p_title.text = title
            p_title.font.name = FONT_MAIN
            p_title.font.size = Pt(13)
            p_title.font.bold = True
            p_title.font.color.rgb = title_color if title_color else COLOR_PRIMARY
            p_title.space_after = Pt(4)

        for i, item in enumerate(items):
            p = tf.paragraphs[0] if (not title and i == 0) else tf.add_paragraph()
            p.text = item
            p.font.name = FONT_MAIN
            p.font.size = Pt(11)
            p.font.color.rgb = COLOR_TEXT
            p.space_after = Pt(4)

    def add_card(slide, left, top, width, height, title, items, badge=""):
        # Card background
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD
        card.line.color.rgb = COLOR_BORDER
        card.line.width = Pt(1)

        # Content box
        tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.18), width - Inches(0.4), height - Inches(0.36))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0)
        tf.margin_bottom = Inches(0)
        tf.margin_left = Inches(0)
        tf.margin_right = Inches(0)

        # Card Title
        p_title = tf.paragraphs[0]
        p_title.text = (f"[{badge}] " if badge else "") + title
        p_title.font.name = FONT_MAIN
        p_title.font.size = Pt(14)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_PRIMARY
        p_title.space_after = Pt(8)

        # Items
        for item in items:
            p = tf.add_paragraph()
            p.text = f"•  {item}"
            p.font.name = FONT_MAIN
            p.font.size = Pt(12)
            p.font.color.rgb = COLOR_TEXT
            p.space_after = Pt(6)

    def add_math_box(slide, left, top, width, height, label, math_text, subtext=""):
        box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        box.fill.solid()
        box.fill.fore_color.rgb = COLOR_CARD
        box.line.color.rgb = COLOR_BLUE
        box.line.width = Pt(2)

        tb = slide.shapes.add_textbox(left + Inches(0.25), top + Inches(0.15), width - Inches(0.5), height - Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0)
        tf.margin_bottom = Inches(0)

        p1 = tf.paragraphs[0]
        p1.text = label.upper()
        p1.font.name = FONT_MAIN
        p1.font.size = Pt(10)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_BLUE
        p1.space_after = Pt(4)

        p2 = tf.add_paragraph()
        p2.text = math_text
        p2.font.name = FONT_MATH
        p2.font.size = Pt(16)
        p2.font.bold = True
        p2.font.color.rgb = COLOR_TEXT
        p2.alignment = PP_ALIGN.CENTER
        p2.space_after = Pt(4)

        if subtext:
            p3 = tf.add_paragraph()
            p3.text = subtext
            p3.font.name = FONT_MAIN
            p3.font.size = Pt(11)
            p3.font.color.rgb = COLOR_MUTED
            p3.alignment = PP_ALIGN.CENTER

    def add_table_data(slide, left, top, width, height, headers, rows):
        num_rows = len(rows) + 1
        num_cols = len(headers)
        table_shape = slide.shapes.add_table(num_rows, num_cols, left, top, width, height)
        table = table_shape.table

        # Format Header
        for c_idx, h in enumerate(headers):
            cell = table.cell(0, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_CARD
            p = cell.text_frame.paragraphs[0]
            p.text = str(h)
            p.font.name = FONT_MAIN
            p.font.bold = True
            p.font.size = Pt(11)
            p.font.color.rgb = COLOR_PRIMARY
            p.alignment = PP_ALIGN.CENTER

        # Format Rows
        for r_idx, row in enumerate(rows):
            for c_idx, val in enumerate(row):
                cell = table.cell(r_idx + 1, c_idx)
                cell.fill.solid()
                cell.fill.fore_color.rgb = COLOR_BG if r_idx % 2 == 0 else COLOR_CARD
                p = cell.text_frame.paragraphs[0]
                p.text = str(val)
                p.font.name = FONT_MONO if any(ch.isdigit() for ch in str(val)) else FONT_MAIN
                p.font.size = Pt(11)
                p.font.color.rgb = COLOR_TEXT
                p.alignment = PP_ALIGN.CENTER

    # =========================================================================
    # SLIDE 1: COVER
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = COLOR_BG
    bg1.line.fill.background()

    # Left Accent Bar
    bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.2), Inches(1.8), Inches(0.12), Inches(3.2))
    bar.fill.solid()
    bar.fill.fore_color.rgb = COLOR_PRIMARY
    bar.line.fill.background()

    tb1 = s1.shapes.add_textbox(Inches(1.5), Inches(1.6), Inches(9.5), Inches(2.2))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "METODE NUMERIK"
    p.font.name = FONT_MAIN
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLUE
    p.space_after = Pt(8)

    p2 = tf1.add_paragraph()
    p2.text = "DIFERENSIASI NUMERIK"
    p2.font.name = FONT_MAIN
    p2.font.size = Pt(44)
    p2.font.bold = True
    p2.font.color.rgb = COLOR_TEXT
    p2.space_after = Pt(6)

    p3 = tf1.add_paragraph()
    p3.text = "Pendekatan Nilai Turunan Fungsi melalui Polinomial Deret & Ekstrapolasi Richardson"
    p3.font.name = FONT_MAIN
    p3.font.size = Pt(16)
    p3.font.color.rgb = COLOR_MUTED

    # Meta box
    meta_box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(4.1), Inches(9.2), Inches(2.5))
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
    mp1.font.size = Pt(12)
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
    mp3.font.size = Pt(12)
    mp3.font.bold = True
    mp3.font.color.rgb = COLOR_TEXT

    # =========================================================================
    # SLIDE 2: PENGERTIAN
    # =========================================================================
    s2 = add_base_slide("Pengantar", "Pengertian Diferensiasi Numerik", 2,
        "Turunan menyatakan laju perubahan. Kadang fungsi sulit diturunkan, atau kita hanya punya tabel data. Contoh di awal pembahasan adalah fungsi jarak bola jatuh dengan ln cosh; kecepatannya sulit diturunkan secara analitik. Karena itu kita pakai pendekatan numerik.")
    add_card(s2, Inches(0.8), Inches(1.8), Inches(3.6), Inches(3.2), "Pengertian", [
        "Memperkirakan nilai turunan fungsi f'(x) dari titik-titik diskret.",
        "Dipakai saat turunan analitis sulit diperoleh secara eksak.",
        "Metode utama saat data berupa tabel pengukuran."
    ], "A")
    add_card(s2, Inches(4.8), Inches(1.8), Inches(3.6), Inches(3.2), "Tujuan", [
        "Memperkirakan laju perubahan sesaat fungsi.",
        "Menghitung turunan dari data tabel diskret.",
        "Membantu penyelesaian persamaan diferensial."
    ], "B")
    add_card(s2, Inches(8.8), Inches(1.8), Inches(3.733), Inches(3.2), "Analitis vs Numerik", [
        "Analitis: Hasil diferensiasi matematis formal (eksak).",
        "Numerik: Hasil hampiran (pendekatan) bernilai numerik.",
        "Memerlukan pemahaman atas galat hampiran."
    ], "C")
    add_math_box(s2, Inches(0.8), Inches(5.2), Inches(11.733), Inches(1.4),
        "Contoh Motivasi Fisika (hlm. 185)",
        "Jarak jatuh:  z(t) = (m / cd) · ln cosh( √(g·cd / m) · t )",
        "Kecepatan v(t) = z'(t) sulit diturunkan analitis pada model aerodinamika non-linier kompleks.")

    # =========================================================================
    # SLIDE 3: PENERAPAN DI DUNIA NYATA
    # =========================================================================
    s3 = add_base_slide("Pengantar Tambahan", "Penerapan di Dunia Nyata", 3,
        "Slide ini penjelasan tambahan agar audiens tahu untuk apa rumus diferensiasi numerik dipakai. Datanya sengaja dibuat sederhana dari s(t) = t^3 supaya kita tahu jawaban benarnya (12 m/s).")
    add_card(s3, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.7), "Contoh Aplikasi Rekayasa", [
        "Kecepatan: v(t) = ds/dt dari sensor posisi GPS / telemetri.",
        "Percepatan: a(t) = dv/dt dari data kecepatan kendaraan.",
        "Perpindahan Panas: Laju perubahan suhu dT/dx (Hukum Fourier).",
        "Data Eksperimen: Menghitung laju reaksi kimia dari sampel waktu.",
        "Data nyata tidak memiliki rumus fungsi kontinu eksak!"
    ], "Praktis")
    add_card(s3, Inches(6.8), Inches(1.8), Inches(5.733), Inches(4.7), "Studi Kasus: Posisi s(t) -> v(2)", [
        "Data t = 1, 2, 3 s -> s = 1, 8, 27 m (h = 1 s). Dicari v(2):",
        "Maju: (27 - 8)/1 = 19 m/s (Galat = 7)",
        "Mundur: (8 - 1)/1 = 7 m/s (Galat = 5)",
        "Tengah: (27 - 1)/2 = 13 m/s (Galat = 1)",
        "Eksak s(t)=t³ -> s'(2) = 3(2)² = 12 m/s.",
        "Kesimpulan: Selisih tengah O(h²) jauh lebih teliti daripada O(h)!"
    ], "Kasus")

    # =========================================================================
    # SLIDE 4: DASAR RUMUS: PENDEKATAN DERET
    # =========================================================================
    s4 = add_base_slide("Pendekatan Deret", "Dasar Rumus: Pendekatan Deret", 4,
        "Buku menurunkan rumus lewat polinomial Lagrange dan suku galatnya, bukan langsung lewat Taylor. Intinya: fungsi didekati dengan polinomial yang melalui titik data, lalu diturunkan.")
    add_card(s4, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.7), "Penurunan via Polinomial Lagrange", [
        "Interpolasi pada x₀ dan x₁ = x₀ + h:",
        "f(x) = P₀,₁(x) + [(x - x₀)(x - x₁)/2!] f''(ξ(x))",
        "P₀,₁(x) = [f(x₀)(x - x₀ - h)/(-h)] + [f(x₀+h)(x - x₀)/h]",
        "Turunkan terhadap x, lalu evaluasi di x = x₀.",
        "Suku koefisien D_x(f''(ξ(x))) bernilai 0 di x = x₀ sehingga galat dapat dirumuskan secara tegas."
    ], "Penurunan")
    add_math_box(s4, Inches(6.8), Inches(1.8), Inches(5.733), Inches(2.2),
        "Hasil Penurunan (Persamaan 6.1 Buku)",
        "f'(x₀) = [f(x₀ + h) - f(x₀)] / h  -  (h / 2) f''(ξ)",
        "Suku -(h/2)f''(ξ) adalah galat pemotongan (truncation error)")
    add_card(s4, Inches(6.8), Inches(4.3), Inches(5.733), Inches(2.2), "Sudut Pandang Deret Taylor", [
        "f(x+h) = f(x) + h f'(x) + (h²/2) f''(x) + ...",
        "f'(x) = [f(x+h) - f(x)] / h - O(h)",
        "Alur: Titik Data -> Polinomial -> Rumus -> Suku Galat"
    ], "Setara")

    # =========================================================================
    # SLIDE 5: SELISIH MAJU DAN MUNDUR
    # =========================================================================
    s5 = add_base_slide("Pendekatan Deret", "Metode Selisih Maju dan Mundur", 5,
        "Dua rumus ini adalah yang paling sederhana. Maju memakai titik di depan, mundur memakai titik di belakang. Keduanya hanya butuh dua nilai fungsi dan galatnya berorde h.")
    add_math_box(s5, Inches(0.8), Inches(1.8), Inches(5.6), Inches(2.6),
        "Selisih Maju (Forward Difference)",
        "f'(x) ≈ [f(x + h) - f(x)] / h",
        "Titik di depan | Cocok untuk ujung kiri data | Galat O(h)")
    add_math_box(s5, Inches(6.8), Inches(1.8), Inches(5.733), Inches(2.6),
        "Selisih Mundur (Backward Difference)",
        "f'(x) ≈ [f(x) - f(x - h)] / h",
        "Titik di belakang | Cocok untuk ujung kanan data | Galat O(h)")
    add_card(s5, Inches(0.8), Inches(4.7), Inches(11.733), Inches(1.8), "Karakteristik & Kesimpulan Praktis", [
        "Sederhana: Masing-masing hanya membutuhkan 2 nilai fungsi.",
        "Keterbatasan: Orde galat O(h) memerlukan nilai h yang sangat kecil untuk presisi tinggi.",
        "Buku teks: Beda mundur secara matematis adalah Persamaan 6.1 dengan nilai h negatif."
    ], "Evaluasi")

    # =========================================================================
    # SLIDE 6: SELISIH TENGAH
    # =========================================================================
    s6 = add_base_slide("Pendekatan Deret", "Metode Selisih Tengah (Central Difference)", 6,
        "Selisih tengah adalah rumus tiga titik tengah di buku (6.5), tanpa memakai f(x₀) itu sendiri. Karena simetris, suku galat orde pertama saling meniadakan, sehingga galatnya berorde h².")
    add_math_box(s6, Inches(0.8), Inches(1.8), Inches(11.733), Inches(2.5),
        "Rumus Tiga Titik Tengah (Persamaan 6.5)",
        "f'(x₀) ≈ [f(x₀ + h) - f(x₀ - h)] / (2h)",
        "Suku galat pemotongan:  -(h² / 6) f'''(ξ₁) ,  ξ₁ ∈ (x₀ - h, x₀ + h)  =>  O(h²)")
    add_card(s6, Inches(0.8), Inches(4.6), Inches(5.6), Inches(1.9), "Kelebihan", [
        "Simetris: Suku ganjil Taylor saling meniadakan.",
        "Orde O(h²): Jika h dibagi 2, galat turun 4 kali lipat!",
        "Nilai f(x₀) tidak perlu dihitung dalam rumus."
    ], "Kelebihan")
    add_card(s6, Inches(6.8), Inches(4.6), Inches(5.733), Inches(1.9), "Keterbatasan", [
        "Membutuhkan nilai fungsi di kedua sisi titik (kiri & kanan).",
        "Tidak dapat digunakan pada batas paling ujung data tabel.",
        "Memerlukan rumus titik ujung (slide 7)."
    ], "Keterbatasan")

    # =========================================================================
    # SLIDE 7: RUMUS TIGA TITIK DAN LIMA TITIK
    # =========================================================================
    s7 = add_base_slide("Pendekatan Deret", "Rumus Tiga Titik dan Lima Titik", 7,
        "Rumus tiga titik ujung dipakai saat titik ada di ujung data. Rumus lima titik tengah memakai koefisien 1, -8, 8, -1 dan penyebut 12h; galatnya berorde h⁴.")
    add_math_box(s7, Inches(0.8), Inches(1.8), Inches(3.6), Inches(2.3),
        "3 Titik Ujung (6.4)",
        "[-3f₀ + 4f₁ - f₂] / 2h",
        "Galat: (h²/3) f''' => O(h²)")
    add_math_box(s7, Inches(4.8), Inches(1.8), Inches(3.6), Inches(2.3),
        "5 Titik Tengah (6.7)",
        "[f₋₂ - 8f₋₁ + 8f₁ - f₂] / 12h",
        "Galat: (h⁴/30) f⁽⁵⁾ => O(h⁴)")
    add_math_box(s7, Inches(8.8), Inches(1.8), Inches(3.733), Inches(2.3),
        "5 Titik Ujung (6.6)",
        "[-25f₀ + 48f₁ - 36f₂ + 16f₃ - 3f₄] / 12h",
        "Galat: (h⁴/5) f⁽⁵⁾ => O(h⁴)")

    add_table_data(s7, Inches(0.8), Inches(4.4), Inches(11.733), Inches(2.1),
        ["Aspek", "Tiga Titik Ujung (6.4)", "Lima Titik Tengah (6.7)", "Lima Titik Ujung (6.6)"],
        [
            ["Jumlah Titik", "3 titik", "5 titik", "5 titik"],
            ["Posisi", "Ujung batas interval", "Titik dalam (interior)", "Ujung batas interval"],
            ["Orde Galat", "O(h²)", "O(h⁴) ⭐", "O(h⁴) ⭐"]
        ])

    # =========================================================================
    # SLIDE 8: CONTOH 6.1.1 f(x) = ln x
    # =========================================================================
    s8 = add_base_slide("Contoh 6.1.1", "Contoh: Selisih Maju untuk f(x) = ln x", 8,
        "Substitusikan x₀ = 1,8 dan h = 0,1 ke rumus beda maju: ln 1,9 dikurangi ln 1,8, dibagi 0,1, hasilnya 0,5406722. Bandingkan dengan eksak 1/1,8 = 0,5555556.")
    add_math_box(s8, Inches(0.8), Inches(1.8), Inches(11.733), Inches(1.8),
        "Perhitungan Kasus x₀ = 1,8 ; h = 0,1",
        "f'(1,8) ≈ [ln(1,9) - ln(1,8)] / 0,1 = (0,64185389 - 0,58778667) / 0,1 = 0,5406722",
        "Nilai Eksak: f'(x) = 1/x => f'(1,8) = 1/1,8 ≈ 0,5555556")
    add_table_data(s8, Inches(0.8), Inches(3.8), Inches(11.733), Inches(2.2),
        ["Langkah h", "Nilai Pendekatan", "Galat Aktual |Eksak - Pend.|", "Batas Atas Galat |h| / [2(1,8)²]"],
        [
            ["0,10", "0,5406722", "0,0148834", "0,0154321"],
            ["0,05", "0,5479795", "0,0075761", "0,0077160"],
            ["0,01", "0,5540180", "0,0015376 ⭐", "0,0015432"]
        ])
    add_card(s8, Inches(0.8), Inches(6.1), Inches(11.733), Inches(0.65), "Keterangan", [
        "Makin kecil h, pendekatan makin dekat ke eksak. Batas atas teoritis terbukti selalu lebih besar dari galat aktual."
    ])

    # =========================================================================
    # SLIDE 9: ANALISIS GALAT
    # =========================================================================
    s9 = add_base_slide("Analisis Galat", "Galat atau Kesalahan Pendekatan", 9,
        "Setiap rumus yang kita pakai hanya pendekatan. Galat pemotongan muncul karena suku dibuang. Orde O(h), O(h²), O(h⁴) menunjukkan kecepatan galat mengecil.")
    add_card(s9, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.7), "Konsep Dasar Galat", [
        "Turunan numerik selalu berupa hampiran / pendekatan.",
        "Galat Pemotongan (Truncation Error): Akibat memutus deret tak hingga Taylor.",
        "Galat Bertanda = Eksak - Pendekatan.",
        "Galat Absolut = |Eksak - Pendekatan|.",
        "Pengaruh h: h makin kecil -> galat pemotongan umumnya turun."
    ], "Teori")
    add_card(s9, Inches(6.8), Inches(1.8), Inches(5.733), Inches(4.7), "Perbandingan Orde Galat O(h^p)", [
        "Selisih Maju  : O(h)    [Linear, penurunan lambat]",
        "Selisih Mundur: O(h)    [Linear, penurunan lambat]",
        "Selisih Tengah: O(h²)   [Kuadratik, h/2 -> galat / 4]",
        "3 Titik Ujung : O(h²)   [Kuadratik, h/2 -> galat / 4]",
        "5 Titik Tengah: O(h⁴)   [Kuartik, h/2 -> galat / 16! ⭐]",
        "5 Titik Ujung : O(h⁴)   [Kuartik, h/2 -> galat / 16! ⭐]",
        "Notasi Big-O adalah perilaku asimtotik saat h cukup kecil."
    ], "Orde")

    # =========================================================================
    # SLIDE 10: PENGARUH h & DILEMA PEMBULATAN
    # =========================================================================
    s10 = add_base_slide("Analisis Galat Tambahan", "Pengaruh Nilai h dan Sumber Galat", 10,
        "Ada dua sumber galat berlawanan: pemotongan (mengecil saat h turun) vs pembulatan/noise (membesar saat h turun). Tabel dihitung sendiri dengan e^x di x=1.")
    add_card(s10, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.7), "Trade-off Komputasi", [
        "Galat Pemotongan ~ h^p: Turun saat h mengecil.",
        "Galat Pembulatan / Noise ~ δ/h: Naik saat h mengecil!",
        "Total Galat (Tengah): E(h) ≤ (M h² / 6) + (δ / h)",
        "Langkah Optimum: h* ≈ ³√(3δ / M)",
        "Peringatan: Nilai h yang terlalu kecil TIDAK SELALU lebih akurat!"
    ], "Model")
    add_table_data(s10, Inches(6.8), Inches(1.8), Inches(5.733), Inches(4.7),
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
    # SLIDE 11: GALAT ABSOLUT, RELATIF, PERSENTASE
    # =========================================================================
    s11 = add_base_slide("Analisis Galat Tambahan", "Galat Absolut, Relatif, dan Persentase", 11,
        "Slide ini melengkapi slide galat: Ea memberi satuan turunan, Er membandingkan dengan besar turunan, E_% adalah Er x 100. Jika turunan nol, Er tidak terdefinisi.")
    add_math_box(s11, Inches(0.8), Inches(1.8), Inches(3.6), Inches(2.2),
        "Galat Absolut (Ea)",
        "Ea = |f'(x) - Dh|",
        "Satuan sama dengan turunan f'")
    add_math_box(s11, Inches(4.8), Inches(1.8), Inches(3.6), Inches(2.2),
        "Galat Relatif (Er)",
        "Er = |f'(x) - Dh| / |f'(x)|",
        "Ukuran proporsional")
    add_math_box(s11, Inches(8.8), Inches(1.8), Inches(3.733), Inches(2.2),
        "Galat Persentase (E%)",
        "E% = Er × 100%",
        "Format persentase praktis")

    add_card(s11, Inches(0.8), Inches(4.3), Inches(11.733), Inches(2.3), "Contoh Aplikasi: Kasus ln x di x = 1,8 (h = 0,1)", [
        "Dh = 0,5406722  dan  f'(1,8) = 0,5555556",
        "Ea = |0,5555556 - 0,5406722| = 0,0148834",
        "Er = 0,0148834 / 0,5555556 ≈ 0,0267901",
        "E% ≈ 2,679%",
        "Perhatian Khusus: Jika f'(x) = 0, Er tidak terdefinisi (pembagian nol). Gunakan Ea!"
    ], "Aplikasi")

    # =========================================================================
    # SLIDE 12: METODE EKSTRAPOLASI RICHARDSON
    # =========================================================================
    s12 = add_base_slide("Ekstrapolasi Richardson", "Metode Ekstrapolasi Richardson", 12,
        "Richardson tidak membuat rumus turunan baru dari data; ia menggabungkan dua hasil yang sudah ada. Hitung D(h) dan D(2h), lalu tambahkan koreksi [D(h) − D(2h)]/(2ⁿ − 1). Untuk selisih tengah galatnya O(h²), jadi n = 2 dan rumusnya (4D(h) − D(2h))/3 dengan orde O(h⁴). Untuk selisih maju n = 1. Di buku, langkah besar ditulis h dan langkah kecil h/2, jadi D(h) di slide ini sama dengan N₁(h/2) di buku. Pilih n sesuai bentuk galat pendekatan awal.")

    # Left Top: Pengertian
    add_custom_card(s12, Inches(0.8), Inches(1.8), Inches(5.6), Inches(1.8), "Pengertian", [
        "Menggabungkan dua pendekatan dengan ukuran langkah berbeda untuk membuang suku galat utama, sehingga hasilnya lebih teliti."
    ], border_color=COLOR_EMERALD, title_color=COLOR_EMERALD)

    # Left Bottom: Prinsip kerja
    add_custom_card(s12, Inches(0.8), Inches(3.8), Inches(5.6), Inches(2.6), "Prinsip kerja", [
        "1. Hitung pendekatan turunan dengan langkah h → D(h)",
        "2. Hitung pendekatan dengan langkah 2h → D(2h)",
        "3. Gabungkan keduanya untuk mengurangi galat utama"
    ], border_color=COLOR_EMERALD, title_color=COLOR_EMERALD)

    # Right Top: Rumus umum
    add_custom_card(s12, Inches(6.8), Inches(1.8), Inches(5.733), Inches(3.1), "Rumus umum", [
        "f'_0 = D(h) + [ D(h) - D(2h) ] / (2ⁿ - 1)",
        "",
        "• f′₀ : nilai turunan di x₀ setelah ekstrapolasi",
        "• D(h) : hasil pendekatan turunan langkah h (lebih kecil)",
        "• D(2h) : hasil pendekatan turunan langkah 2h (dua kali lebih besar)",
        "• n : orde galat awal, yaitu O(hⁿ)",
        "",
        "Kedua hasil digabung untuk menghilangkan suku galat utama."
    ], border_color=COLOR_EMERALD, title_color=COLOR_EMERALD)

    # Right Bottom: Contoh: selisih tengah (n = 2)
    add_custom_card(s12, Inches(6.8), Inches(5.05), Inches(5.733), Inches(1.35), "Contoh: selisih tengah (n = 2)", [
        "f'_0 = [ 4 D(h) - D(2h) ] / 3",
        "Orde galat naik: O(h²) → O(h⁴) ⭐"
    ], border_color=COLOR_AMBER, title_color=COLOR_AMBER)

    # Footnote
    fn_box = s12.shapes.add_textbox(Inches(0.8), Inches(6.5), Inches(11.733), Inches(0.25))
    fn_tf = fn_box.text_frame
    fn_p = fn_tf.paragraphs[0]
    fn_p.text = "Kaitan notasi slide berikut: D(h) = N₁(h/2), D(2h) = N₁(h). Untuk n = 1 (selisih maju): 2D(h) − D(2h)."
    fn_p.font.name = FONT_MAIN
    fn_p.font.size = Pt(9.5)
    fn_p.font.color.rgb = COLOR_MUTED

    # =========================================================================
    # SLIDE 13: CONTOH 6.2.1 RICHARDSON f(x) = ln x
    # =========================================================================
    s13 = add_base_slide("Contoh 6.2.1", "Contoh Richardson pada f(x) = ln x", 13,
        "Galat awal selisih maju berorde h, jadi pakai rumus n = 1: dua kali hasil yang lebih teliti dikurangi hasil yang kurang teliti. Hitung: 2 × 0,5479795 = 1,0959590; dikurangi 0,5406722 menghasilkan 0,5552868. Galat tiap hasil dihitung dari nilai eksak 0,5555556. Buku menulis hasil 0,555287 dan galat 0,000258; hitung ulang dari angka buku memberi 0,0002688, dan kami memakai angka yang konsisten dengan digit di slide.")

    # Left Top: Diketahui
    add_custom_card(s13, Inches(0.8), Inches(1.8), Inches(5.6), Inches(1.6), "Diketahui:", [
        "f(x) = ln x,  x₀ = 1,8",
        "N₁(0,1) = 0,5406722  ·  N₁(0,05) = 0,5479795",
        "Selisih maju: galat O(h), jadi n = 1"
    ], border_color=COLOR_EMERALD, title_color=COLOR_EMERALD)

    # Left Bottom: Perhitungan
    add_custom_card(s13, Inches(0.8), Inches(3.6), Inches(5.6), Inches(2.1), "Perhitungan", [
        "N₂(0,1) = 2 N₁(0,05) - N₁(0,1)",
        "= 2(0,5479795) - 0,5406722",
        "= 0,5552868 ⭐"
    ], border_color=COLOR_EMERALD, title_color=COLOR_EMERALD)

    # Right: Table
    add_table_data(s13, Inches(6.8), Inches(1.8), Inches(5.733), Inches(1.9),
        ["Metode", "Hasil", "Galat absolut"],
        [
            ["Selisih maju, h = 0,1", "0,5406722", "0,0148834"],
            ["Selisih maju, h = 0,05", "0,5479795", "0,0075761"],
            ["Richardson", "0,5552868", "0,0002688 ⭐"],
            ["Nilai eksak", "0,5555556", "—"]
        ])

    # Right Bottom: Visual Bars
    bars_card = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(3.9), Inches(5.733), Inches(1.8))
    bars_card.fill.solid()
    bars_card.fill.fore_color.rgb = COLOR_CARD
    bars_card.line.color.rgb = COLOR_BORDER
    bars_card.line.width = Pt(1)

    tb_bars = s13.shapes.add_textbox(Inches(7.0), Inches(3.98), Inches(5.333), Inches(1.6))
    tf_bars = tb_bars.text_frame
    p_bl = tf_bars.paragraphs[0]
    p_bl.text = "Galat (makin pendek makin baik)"
    p_bl.font.name = FONT_MAIN
    p_bl.font.size = Pt(10)
    p_bl.font.bold = True
    p_bl.font.color.rgb = COLOR_MUTED
    p_bl.space_after = Pt(2)

    b1_label = tf_bars.add_paragraph()
    b1_label.text = "h = 0,1  ·  0,0148834"
    b1_label.font.name = FONT_MAIN
    b1_label.font.size = Pt(9.5)
    b1_label.font.color.rgb = COLOR_TEXT

    bar1 = s13.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(7.0), Inches(4.45), Inches(4.8), Inches(0.14))
    bar1.fill.solid()
    bar1.fill.fore_color.rgb = COLOR_BLUE
    bar1.line.fill.background()

    b2_label = tf_bars.add_paragraph()
    b2_label.text = "\nh = 0,05  ·  0,0075761"
    b2_label.font.name = FONT_MAIN
    b2_label.font.size = Pt(9.5)
    b2_label.font.color.rgb = COLOR_TEXT

    bar2 = s13.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(7.0), Inches(4.95), Inches(2.44), Inches(0.14))
    bar2.fill.solid()
    bar2.fill.fore_color.rgb = COLOR_BLUE
    bar2.line.fill.background()

    b3_label = tf_bars.add_paragraph()
    b3_label.text = "\nRichardson  ·  0,0002688"
    b3_label.font.name = FONT_MAIN
    b3_label.font.size = Pt(9.5)
    b3_label.font.bold = True
    b3_label.font.color.rgb = COLOR_AMBER

    bar3 = s13.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(7.0), Inches(5.45), Inches(0.15), Inches(0.14))
    bar3.fill.solid()
    bar3.fill.fore_color.rgb = COLOR_AMBER
    bar3.line.fill.background()

    # Bottom Banner
    add_callout_banner(s13, Inches(0.8), Inches(5.9), Inches(11.733), Inches(0.68),
        "Kesimpulan: Richardson mengurangi galat sekitar 28 kali dibanding selisih maju dengan h = 0,05 (0,0075761 ÷ 0,0002688 ≈ 28).")

    # =========================================================================
    # SLIDE 14: CONTOH 6.1.2 DATA TABEL f(x) = x e^x
    # =========================================================================
    s14 = add_base_slide("Contoh 6.1.2", "Perbandingan Metode Diferensiasi pada Data Tabel", 14,
        "Semua hasil dihitung dari lima nilai tabel, bukan dari rumus fungsi. Nilai eksak 3e² ≈ 22,167168 hanya dipakai sebagai pembanding. Galat absolut dihitung |eksak − pendekatan|: 0,134858; 0,061622; 0,000169. Lima titik tengah paling dekat karena galatnya O(h⁴), sedangkan dua rumus lain O(h²). Tiga titik tengah dengan h berbeda nantinya menjadi bahan Richardson pada slide 16.")

    # Left Box with Header text
    left_box = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(4.6), Inches(4.7))
    left_box.fill.solid()
    left_box.fill.fore_color.rgb = COLOR_CARD
    left_box.line.color.rgb = COLOR_BORDER

    tb_fn = s14.shapes.add_textbox(Inches(1.0), Inches(1.95), Inches(4.2), Inches(0.4))
    tf_fn = tb_fn.text_frame
    p_fn = tf_fn.paragraphs[0]
    p_fn.text = "f(x) = xeˣ,  x₀ = 2,0,  h = 0,1"
    p_fn.font.name = FONT_MAIN
    p_fn.font.size = Pt(13)
    p_fn.font.bold = True
    p_fn.font.color.rgb = COLOR_PRIMARY

    add_table_data(s14, Inches(1.0), Inches(2.45), Inches(4.2), Inches(3.8),
        ["x", "f(x)"],
        [
            ["1,8", "10,889365"],
            ["1,9", "12,703199"],
            ["2,0", "14,778112"],
            ["2,1", "17,148957"],
            ["2,2", "19,855030"]
        ])

    # Right Results Table
    add_table_data(s14, Inches(5.8), Inches(1.8), Inches(6.733), Inches(2.1),
        ["Metode", "f′(2)", "Galat absolut"],
        [
            ["Tiga titik ujung", "22,032310", "0,134858"],
            ["Tiga titik tengah", "22,228790", "0,061622"],
            ["Lima titik tengah", "22,166999", "0,000169 ⭐"],
            ["Nilai eksak 3e²", "22,167168", "—"]
        ])

    # Conclusion Banner
    add_callout_banner(s14, Inches(5.8), Inches(4.15), Inches(6.733), Inches(0.65),
        "Kesimpulan: di antara ketiga metode, lima titik tengah paling akurat.")

    # Amber card: Kaitan dengan Richardson
    add_custom_card(s14, Inches(5.8), Inches(5.0), Inches(6.733), Inches(1.5),
        "Kaitan dengan Richardson:", [
            "Hasil pendekatan turunan dapat dipakai sebagai dasar (N₁) untuk meningkatkan ketelitian lewat ekstrapolasi (slide 16)."
        ], border_color=COLOR_AMBER, title_color=COLOR_AMBER)

    # =========================================================================
    # SLIDE 15: CONTOH 6.1.3 STRATEGI PEMILIHAN RUMUS
    # =========================================================================
    s15 = add_base_slide("Contoh 6.1.3", "Strategi Pemilihan Rumus Diferensiasi", 15,
        "Lihat posisi titik dulu. Di ujung tidak ada data di salah satu sisi, jadi pakai rumus ujung. Di titik dalam bisa pakai rumus tengah, dan lima titik tengah hanya pada x = 1,3 karena butuh dua titik di tiap sisi. Hitungan memakai nilai tabel penuh; buku menampilkannya dibulatkan. Hubungan dengan Richardson: untuk membentuk N₁ dengan h dan h/2, data pada kedua ukuran langkah itu harus ada; ini akan terlihat jelas di slide 17.")

    # Top Left Table
    add_table_data(s15, Inches(0.8), Inches(1.8), Inches(5.3), Inches(2.1),
        ["x", "f(x)", "Posisi titik"],
        [
            ["1,1", "9,025013", "ujung kiri"],
            ["1,2", "11,02318", "interior"],
            ["1,3", "13,46374", "tengah penuh"],
            ["1,4", "16,44465", "interior"],
            ["1,5", "20,08554", "ujung kanan"]
        ])

    # Note under left table
    tb_h = s15.shapes.add_textbox(Inches(0.8), Inches(3.95), Inches(5.3), Inches(0.3))
    tf_h = tb_h.text_frame
    p_h = tf_h.paragraphs[0]
    p_h.text = "h = 0,1; di ujung kanan h dibuat negatif"
    p_h.font.name = FONT_MAIN
    p_h.font.size = Pt(10)
    p_h.font.color.rgb = COLOR_MUTED

    # Top Right Table
    add_table_data(s15, Inches(6.4), Inches(1.8), Inches(6.133), Inches(2.2),
        ["Titik", "Rumus yang tersedia"],
        [
            ["1,1 (ujung kiri)", "Tiga titik ujung (6.4) · lima titik ujung (6.6)"],
            ["1,2 (interior)", "Tiga titik ujung · tiga titik tengah (6.5)"],
            ["1,3 (tengah penuh)", "6.4 · 6.5 · lima titik tengah (6.7) ⭐"],
            ["1,4 (interior)", "6.4 (h negatif) · 6.5"],
            ["1,5 (ujung kanan)", "6.4 · 6.6 (h negatif)"]
        ])

    # Formula Cards
    add_custom_card(s15, Inches(0.8), Inches(4.35), Inches(5.6), Inches(1.35),
        "Tiga titik ujung, x = 1,1:", [
            "[-3(9,025013) + 4(11,02318) - 13,46374] / 0,2",
            "= 17,76971"
        ], border_color=COLOR_EMERALD, title_color=COLOR_EMERALD)

    add_custom_card(s15, Inches(6.8), Inches(4.35), Inches(5.733), Inches(1.35),
        "Lima titik tengah, x = 1,3:", [
            "[9,025013 - 8(11,02318) + 8(16,44465) - 20,08554] / 1,2",
            "= 26,92603 ⭐"
        ], border_color=COLOR_EMERALD, title_color=COLOR_EMERALD)

    # Bottom Banner
    add_callout_banner(s15, Inches(0.8), Inches(5.85), Inches(11.733), Inches(0.75),
        "Kesimpulan: pilih rumus menurut posisi titik dan ketersediaan data. Kaitan dengan Richardson: ekstrapolasi membutuhkan data yang sesuai dengan ukuran langkah yang dipakai (h dan setengahnya).")

    # =========================================================================
    # SLIDE 16: CONTOH 6.2.2 RICHARDSON BERTINGKAT PADA f(x) = xeˣ
    # =========================================================================
    s16 = add_base_slide("Contoh 6.2.2", "Richardson Bertingkat pada f(x) = xeˣ", 16,
        "Tiga tahap: (1) hitung N₁ dengan selisih tengah untuk h = 0,2; 0,1; 0,05; (2) gabungkan pasangan yang bertetangga dengan pembagi 3 → N₂(0,2) dan N₂(0,1); (3) gabungkan kedua N₂ dengan pembagi 15 → N₃(0,2). Angka dalam kurung adalah ukuran langkah. Ini angka buku; hitung ulang dari tabel Contoh 6.1.2 memberi N₁(0,2) = 22,414163 dan N₁(0,1) = 22,228790 (selisih kecil di digit ke-6). Rumus N₃ di buku tertulis memakai N₁(0,2), tetapi angkanya cocok dengan N₂(0,2). Galat N₃ nol hanya pada enam desimal yang ditampilkan, bukan bukti kesamaan matematis.")

    # Subtitle Text
    tb_sub = s16.shapes.add_textbox(Inches(0.8), Inches(1.4), Inches(11.733), Inches(0.35))
    tf_sub = tb_sub.text_frame
    p_sub = tf_sub.paragraphs[0]
    p_sub.text = "x = 2, nilai eksak f′(2) = 22,167168  ·  N₁: selisih tengah, galat pangkat genap"
    p_sub.font.name = FONT_MAIN
    p_sub.font.size = Pt(11)
    p_sub.font.color.rgb = COLOR_MUTED

    # 3 Step Boxes side-by-side
    add_custom_card(s16, Inches(0.8), Inches(1.8), Inches(3.4), Inches(2.4),
        "Tahap 1 — N₁", [
            "N₁(0,2) = 22,414160",
            "N₁(0,1) = 22,228786",
            "N₁(0,05) = 22,182564",
            "Nilai N₁(0,05) dihitung menggunakan f(x) = xeˣ karena titik x = 1,95 dan 2,05 tidak ada pada tabel."
        ], border_color=COLOR_BLUE, title_color=COLOR_BLUE)

    arr1 = s16.shapes.add_textbox(Inches(4.25), Inches(2.7), Inches(0.5), Inches(0.5))
    arr1.text_frame.paragraphs[0].text = "→"
    arr1.text_frame.paragraphs[0].font.size = Pt(22)
    arr1.text_frame.paragraphs[0].font.bold = True
    arr1.text_frame.paragraphs[0].font.color.rgb = COLOR_MUTED

    add_custom_card(s16, Inches(4.75), Inches(1.8), Inches(3.7), Inches(2.4),
        "Tahap 2 — N₂ (÷3)", [
            "N₂(0,2) = 22,228786 + (22,228786 − 22,414160)/3 = 22,166995",
            "",
            "N₂(0,1) = 22,182564 + (22,182564 − 22,228786)/3 = 22,167157"
        ], border_color=COLOR_EMERALD, title_color=COLOR_EMERALD)

    arr2 = s16.shapes.add_textbox(Inches(8.5), Inches(2.7), Inches(0.5), Inches(0.5))
    arr2.text_frame.paragraphs[0].text = "→"
    arr2.text_frame.paragraphs[0].font.size = Pt(22)
    arr2.text_frame.paragraphs[0].font.bold = True
    arr2.text_frame.paragraphs[0].font.color.rgb = COLOR_MUTED

    add_custom_card(s16, Inches(9.0), Inches(1.8), Inches(3.533), Inches(2.4),
        "Tahap 3 — N₃ (÷15)", [
            "N₃(0,2) = 22,167157 + (22,167157 − 22,166995)/15",
            "",
            "= 22,167168 ⭐ (Identik Eksak)"
        ], border_color=COLOR_AMBER, title_color=COLOR_AMBER)

    # Wide Table
    add_table_data(s16, Inches(0.8), Inches(4.35), Inches(11.733), Inches(1.35),
        ["Tingkat", "N₁(0,2)", "N₁(0,1)", "N₁(0,05)", "N₂(0,2)", "N₂(0,1)", "N₃(0,2)", "Eksak"],
        [
            ["Hasil", "22,414160", "22,228786", "22,182564", "22,166995", "22,167157", "22,167168 ⭐", "22,167168"],
            ["Galat absolut", "0,246992", "0,061618", "0,015396", "0,000173", "0,000011", "0,000000", "—"]
        ])

    # Bottom Banner
    add_callout_banner(s16, Inches(0.8), Inches(5.85), Inches(11.733), Inches(0.75),
        "Kesimpulan: Richardson bertingkat meningkatkan ketelitian secara bertahap: N₁ → N₂ → N₃ (N₃ sama dengan eksak pada enam desimal yang ditampilkan).")

    # =========================================================================
    # SLIDE 17: CONTOH 6.2.3 RICHARDSON DENGAN KETERBATASAN DATA
    # =========================================================================
    s17 = add_base_slide("Contoh 6.2.3", "Richardson dengan Keterbatasan Data", 17,
        "Titik x₀ = 1,3 dengan h = 0,2 dan 0,1; N₁(0,2) memakai f(1,5) dan f(1,1), N₁(0,1) memakai f(1,4) dan f(1,2). Gabungkan dengan pembagi 3 untuk N₂(0,2). Tingkat ketiga butuh N₁(0,05) dengan f(1,35) dan f(1,25), yang tidak ada di tabel, sehingga berhenti di N₂. Catatan untuk penyaji (dicek pada halaman buku 201–202): buku mencetak N₁(0,1) = (1/0,2)(f(1,4) − f(1,1)) = 27,10735 dan N₂(0,2) = 26,920273. Dua hal ini tidak cocok dengan substitusi yang tercetak: (16,44465 − 11,02318)/0,2 memakai f(1,2) dan menghasilkan 27,10735, sedangkan dengan f(1,1) hasilnya lain; dan 27,10735 + (27,10735 − 27,651318)/3 = 26,926027, bukan 26,920273. Nilai 26,926027 juga sama dengan hasil lima titik tengah 26,92603 pada Contoh 6.1.3. Penyebab selisih tidak dapat dipastikan dari buku. Slide menampilkan hasil hitung ulang 26,926027 (dari data tabel yang tersedia); angka 26,920273 adalah yang tercetak di buku.")

    # Left Data Table
    add_table_data(s17, Inches(0.8), Inches(1.8), Inches(4.5), Inches(2.4),
        ["x", "f(x)"],
        [
            ["1,1", "9,025013"],
            ["1,2", "11,02318"],
            ["1,3", "13,46374"],
            ["1,4", "16,44465"],
            ["1,5", "20,08554"]
        ])

    tb_x0 = s17.shapes.add_textbox(Inches(0.8), Inches(4.25), Inches(4.5), Inches(0.35))
    tb_x0.text_frame.paragraphs[0].text = "x₀ = 1,3;  h = 0,2"
    tb_x0.text_frame.paragraphs[0].font.name = FONT_MAIN
    tb_x0.text_frame.paragraphs[0].font.size = Pt(11)
    tb_x0.text_frame.paragraphs[0].font.bold = True
    tb_x0.text_frame.paragraphs[0].font.color.rgb = COLOR_PRIMARY

    # Right: Box 1 (Tahap 1)
    add_custom_card(s17, Inches(5.6), Inches(1.8), Inches(6.933), Inches(1.2),
        "Tahap 1 — N₁", [
            "N₁(0,2) = (20,08554 − 9,025013) / 0,4 = 27,651318",
            "N₁(0,1) = (16,44465 − 11,02318) / 0,2 = 27,107350"
        ], border_color=COLOR_BLUE, title_color=COLOR_BLUE)

    # Right: Box 2 (Tahap 2)
    add_custom_card(s17, Inches(5.6), Inches(3.1), Inches(6.933), Inches(1.2),
        "Tahap 2 — N₂", [
            "N₂(0,2) = 27,107350 + (27,107350 − 27,651318) / 3",
            "= 26,926027 ⭐ (Orde O(h⁴))"
        ], border_color=COLOR_EMERALD, title_color=COLOR_EMERALD)

    # Middle / Warning Card: Mengapa N3 tidak dapat dihitung
    add_custom_card(s17, Inches(0.8), Inches(4.65), Inches(11.733), Inches(0.95),
        "Mengapa N₃ tidak dapat dihitung?", [
            "N₃ membutuhkan N₁(0,05) = [f(1,35) − f(1,25)] / 0,1, sedangkan f(1,25) dan f(1,35) tidak tersedia pada tabel."
        ], border_color=COLOR_AMBER, title_color=COLOR_AMBER)

    # Bottom Banner
    add_callout_banner(s17, Inches(0.8), Inches(5.8), Inches(11.733), Inches(0.8),
        "Kesimpulan: Richardson tidak dapat dilanjutkan ke tingkat berikutnya bila data yang diperlukan tidak tersedia.\nCatatan: Hasil perhitungan menggunakan data tabel yang tersedia.")

    # =========================================================================
    # SLIDE 18: RINGKASAN METODE: PERBANDINGAN
    # =========================================================================
    s18 = add_base_slide("Ringkasan Metode", "Perbandingan Metode Diferensiasi Numerik", 18,
        "Gunakan tabel ini untuk merangkum. Maju/mundur O(h), tengah & 3 titik ujung O(h²), lima titik O(h⁴). Richardson memperbaiki hasil rumus lain.")
    add_table_data(s18, Inches(0.8), Inches(1.8), Inches(11.733), Inches(4.8),
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
    # SLIDE 19: MEMILIH METODE & KONDISI
    # =========================================================================
    s19 = add_base_slide("Ringkasan Metode", "Memilih Metode: Rumus & Kondisi Penggunaan", 19,
        "Slide ini fokus pada kapan rumus dipakai. Pesan penutup: jangan menyimpulkan satu metode selalu paling baik. Lima titik memiliki koefisien besar sehingga lebih sensitif terhadap noise.")
    add_table_data(s19, Inches(0.8), Inches(1.8), Inches(11.733), Inches(4.3),
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
    add_card(s19, Inches(0.8), Inches(6.2), Inches(11.733), Inches(0.55), "Keterangan", [
        "Tidak ada metode yang selalu terbaik di segala situasi: perhatikan noise data dan kestabilan pembulatan!"
    ])

    # =========================================================================
    # SLIDE 20: KESIMPULAN
    # =========================================================================
    s20 = add_base_slide("Penutup", "Kesimpulan", 20,
        "Rangkum perjalanan dari definisi, deret, rumus 2, 3, 5 titik, galat, lalu Richardson. Tutup dengan kutipan penting.")
    add_card(s20, Inches(0.8), Inches(1.8), Inches(6.0), Inches(4.7), "Poin-Poin Kunci", [
        "Diferensiasi numerik memperkirakan turunan dari nilai fungsi diskret.",
        "Pendekatan deret (Lagrange & Taylor) menjadi fondasi matematis utama.",
        "Selisih maju dan mundur: galat pemotongan O(h).",
        "Selisih tengah dan tiga titik ujung: galat O(h²).",
        "Lima titik (tengah dan ujung): ketelitian tinggi O(h⁴).",
        "Ekstrapolasi Richardson meningkatkan ketelitian secara signifikan.",
        "Pilih h dengan cermat mengingat trade-off pemotongan vs pembulatan."
    ], "Ringkasan")
    add_card(s20, Inches(7.2), Inches(1.8), Inches(5.333), Inches(4.7), "Prinsip Utama", [
        "\"Ketelitian diferensiasi numerik tidak hanya ditentukan oleh rumus yang digunakan, tetapi juga oleh ukuran langkah, data yang tersedia, dan sifat fungsi.\"",
        "",
        "Keseimbangan Komputasi:",
        "• Orde tinggi butuh lebih banyak data & sensitif terhadap noise.",
        "• Nilai h terlalu kecil memperbesar galat pembulatan komputer.",
        "• Selalu sesuaikan metode dengan posisi titik data!"
    ], "Intisari")

    # =========================================================================
    # SLIDE 21: PENUTUP / TERIMA KASIH (HERO CENTERED & MINIMALIST)
    # =========================================================================
    s21 = prs.slides.add_slide(blank_layout)
    bg21 = s21.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg21.fill.solid()
    bg21.fill.fore_color.rgb = COLOR_BG
    bg21.line.fill.background()

    # Notes slide
    notes_slide21 = s21.notes_slide
    tf_notes21 = notes_slide21.notes_text_frame
    tf_notes21.text = "Ucapkan terima kasih kepada dosen pengampu dan rekan-rekan mahasiswa atas perhatian selama presentasi berlangsung. Buka kesempatan bagi audiens untuk sesi tanya jawab dan diskusi mengenai materi diferensiasi numerik."

    # Top pill
    pill21 = s21.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.3), Inches(1.1), Inches(4.733), Inches(0.42))
    pill21.fill.solid()
    pill21.fill.fore_color.rgb = COLOR_PRIMARY_SOFT
    pill21.line.color.rgb = COLOR_BORDER
    p_pill = pill21.text_frame.paragraphs[0]
    p_pill.text = "DIFERENSIASI NUMERIK & EKSTRAPOLASI RICHARDSON"
    p_pill.font.name = FONT_MAIN
    p_pill.font.size = Pt(10)
    p_pill.font.bold = True
    p_pill.font.color.rgb = COLOR_PRIMARY
    p_pill.alignment = PP_ALIGN.CENTER

    # Hero Center Box (TERIMA KASIH dominates)
    hero_box = s21.shapes.add_textbox(Inches(1.0), Inches(1.85), Inches(11.333), Inches(3.2))
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

    # Compact Bottom Credit Card
    credit_box = s21.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.2), Inches(5.35), Inches(8.933), Inches(0.95))
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

    # Footer line & indicator
    line21 = s21.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(6.8), Inches(11.733), Inches(0.015))
    line21.fill.solid()
    line21.fill.fore_color.rgb = COLOR_BORDER
    line21.line.fill.background()

    footer21 = s21.shapes.add_textbox(Inches(0.8), Inches(6.85), Inches(11.733), Inches(0.4))
    ftf21 = footer21.text_frame
    ftf21.margin_top = Inches(0)
    fp21 = ftf21.paragraphs[0]
    fp21.text = "Metode Numerik — Imron dkk. (2022) | Slide 21 dari 21"
    fp21.font.name = FONT_MAIN
    fp21.font.size = Pt(10)
    fp21.font.color.rgb = COLOR_MUTED
    fp21.alignment = PP_ALIGN.CENTER

    # Save presentation
    output_path = "Diferensiasi_Numerik.pptx"
    prs.save(output_path)
    print(f"Base presentation saved successfully to: {output_path}")

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
    
    # 21 Transition sequence matching web presentation 3D effects
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
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectPageCurlSingleRight,   # 12: Center-fold
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectPeelOffRight,          # 13: Bottom-right curl
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectCurtains,              # 14: Curtain roll
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectDoorsVertical,         # 15: Doors 3D
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectPageCurlSingleRight,   # 16: Center-fold
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectPeelOffRight,          # 17: Bottom-right curl
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectCurtains,              # 18: Curtain roll
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectWipeRight,             # 19: Diagonal wipe
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectBoxLeft,               # 20: 3D Box / Cube
        [Microsoft.Office.Interop.PowerPoint.PpEntryEffect]::ppEffectCurtains               # 21: Curtain roll
    )
    
    for ($i = 1; $i -le $pres.Slides.Count; $i++) {{
        $slide = $pres.Slides.Item($i)
        $effIdx = ($i - 1) % $effects.Count
        $slide.SlideShowTransition.EntryEffect = $effects[$effIdx]
        $slide.SlideShowTransition.Duration = 1.0
        
        # Entrance animations for content cards & formula boxes (shapes after bg & header)
        $shapeCount = $slide.Shapes.Count
        if ($shapeCount -gt 3) {{
            for ($s = 4; $s -le $shapeCount; $s++) {{
                $shape = $slide.Shapes.Item($s)
                # msoAnimEffectFade = 10, msoAnimateLevelNone = 0, msoAnimTriggerAfterPrevious = 3
                try {{
                    $anim = $slide.TimeLine.MainSequence.AddEffect($shape, 10, 0, 3)
                    $anim.Timing.Duration = 0.4
                }} catch {{}}
            }}
        }}
    }}
    
    $pres.Save()
    $pdfPath = "{pptx_path}".Replace(".pptx", ".pdf")
    try {{
        $pres.SaveAs($pdfPath, 32)
        Write-Output "PowerPoint COM: Exported updated PDF to $pdfPath"
    }} catch {{
        Write-Output "PDF export note: $_"
    }}
    $pres.Close()
    $ppt.Quit()
    Write-Output "PowerPoint COM: Applied slide transitions and entrance animations to all slides."
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

if __name__ == "__main__":
    create_presentation()
