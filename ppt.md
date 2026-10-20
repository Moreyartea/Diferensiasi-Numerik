Metode Numerik — Bab 6

# DIFERENSIASI NUMERIK

Metode Numerik — Bab 6

**Penyusun:** \[Nama anggota kelompok\]\
**Dosen:** \[Nama dosen\]\
**Program Studi / Universitas:** \[Program studi, Universitas\]\
**Tahun:** 2026

Sumber: Imron, Mardlijah & Asfihani (2022)Slide 1 dari 21

Sapa audiens, sebut judul dan bab. Jelaskan bahwa hari ini kita membahas cara memperkirakan turunan fungsi hanya dari nilai-nilai fungsi. Gambar kurva dengan garis singgung mewakili ide utama: turunan adalah kemiringan garis singgung. Isi placeholder nama, dosen, dan program studi sebelum presentasi.

6 · Pengantar

## Pengertian Diferensiasi Numerik

### A. Pengertian

- Memperkirakan **nilai turunan** fungsi dari nilai fungsi di titik-titik tertentu
- Dipakai saat turunan analitis **sulit** diperoleh atau data berupa **tabel**

### B. Tujuan

- Memperkirakan laju perubahan fungsi
- Menghitung turunan dari data tabel
- Membantu penyelesaian masalah numerik

### C. Analitis vs numerik

- **Analitis:** hasil proses diferensiasi secara matematis
- **Numerik:** hasil pendekatan dari nilai fungsi

### Contoh motivasi (buku)

Jarak bola jatuh z(t) = (m/cd) ln cosh(√(g cd/m) t) — kecepatannya sulit diturunkan secara analitik.

Sumber: Imron dkk. (2022), hlm. 185Slide 2 dari 21

Turunan menyatakan laju perubahan. Kadang fungsi sulit diturunkan, atau kita hanya punya tabel data. Contoh di awal Bab 6 adalah fungsi jarak bola jatuh dengan ln cosh; kecepatannya sulit diturunkan secara analitik. Karena itu kita pakai pendekatan numerik. Bab ini memperkenalkan dua cara: pendekatan deret dan ekstrapolasi Richardson.

Pengantar Tambahan di luar buku

## Penerapan di Dunia Nyata

### Mengapa diperlukan?

- Fungsi **sulit diturunkan** secara analitis
- Data hanya dari **pengukuran atau tabel**, tanpa rumus fungsi

### Contoh penerapan

- Kecepatan dari data posisi terhadap waktu
- Percepatan dari data kecepatan
- Laju perubahan suhu
- Laju perubahan pada data eksperimen atau pengamatan

### Contoh: kecepatan dari data posisi

Data ilustrasi: t = 1, 2, 3 s → s = 1, 8, 27 m (h = 1 s). Dicari v(2) = s′(2).

| Metode | Perhitungan | v(2) | Galat absolut |
| --- | --- | --- | --- |
| Maju | (27 − 8)/1 | 19 m/s | 7 |
| Mundur | (8 − 1)/1 | 7 m/s | 5 |
| Tengah | (27 − 1)/2 | 13 m/s | 1 |

Tiap rumus memakai titik berbeda sehingga hasilnya berbeda; selisih tengah paling dekat ke nilai sebenarnya 12 m/s. Nilai itu hanya diketahui karena data dibuat dari s = t³ (s′ = 3t²); pada data nyata turunan eksak tidak diketahui. Rumus yang sama dipakai pada data kecepatan untuk percepatan.

Tambahan: ilustrasi dan hitungan sendiri; konteks umum: Burden & Faires \[1\]Slide 3 dari 21

Slide ini bukan dari buku; ini penjelasan tambahan agar audiens tahu untuk apa rumus-rumus Bab 6 dipakai. Datanya sengaja dibuat sederhana dari s(t) = t³ supaya kita tahu jawaban benarnya (12 m/s) dan bisa menilai galat. Pada data pengukuran nyata nilai eksak tidak diketahui, jadi kita hanya bisa membandingkan antarmetode atau memakai Richardson. Perhatikan: hasil maju 19 dan mundur 7 berbeda jauh karena h = 1 besar dan orde galatnya hanya O(h); selisih tengah O(h²) jauh lebih dekat. Rumus yang sama dipakai untuk menghitung percepatan dari data kecepatan. Semua angka dihitung sendiri dari rumus di slide.

6.1 · Pendekatan Deret

## Dasar Rumus: Pendekatan Deret

### Penurunan di buku

Polinomial Lagrange orde pertama dari x₀ dan x₁ = x₀+h:

\\(f(x)=P\_{0,1}(x)+\\frac{(x-x_0)(x-x_1)}{2!}f''(\\xi(x))\\)

\\(P\_{0,1}(x)=\\frac{f(x_0)(x-x_0-h)}{-h}+\\frac{f(x_0+h)(x-x_0)}{h}\\)

- Turunkan, lalu hapus suku ber-ξ(x)
- Di x = x₀ **koefisien** Dₓ(f″(ξ(x))), yaitu (x−x₀)(x−x₀−h)/2, bernilai 0 → galat dapat ditulis

### Hasil (Pers. 6.1)

\\(f'(x_0)=\\frac{f(x_0+h)-f(x_0)}{h}-\\frac h2 f''(\\xi)\\)

- Beda maju jika h > 0, beda mundur jika h \< 0
- Suku yang diabaikan = **galat pemotongan**

Pandangan setara (ekspansi Taylor): \\(f(x+h)=f(x)+hf'(x)+\\frac{h^2}{2!}f''(x)+\\cdots\\) — pelengkap, bukan penurunan di buku.

**Titik data**→**Polinomial Lagrange / deret**→**Rumus diferensiasi**→**Analisis galat**

Sumber: Imron dkk. (2022), hlm. 185–186Slide 4 dari 21

Buku menurunkan rumus lewat polinomial Lagrange dan suku galatnya, bukan langsung lewat Taylor. Intinya: fungsi didekati dengan polinomial yang melalui titik data, lalu diturunkan. Suku yang dibuang menjadi galat pemotongan. Rumus 6.1 adalah hasilnya: beda maju untuk h positif dan beda mundur untuk h negatif. Ekspansi Taylor saya tampilkan hanya sebagai sudut pandang setara yang umum dikenal.

6.1 · Pendekatan Deret

## Metode Selisih Maju dan Mundur

### Selisih Maju

\\(f'(x)\\approx\\frac{f(x+h)-f(x)}{h}\\)

- Memakai nilai di x dan x+h
- Titik berada **di depan** titik yang dihitung
- Galat pemotongan **O(h)**

### Selisih Mundur

\\(f'(x)\\approx\\frac{f(x)-f(x-h)}{h}\\)

- Memakai nilai di x dan x−h
- Titik berada **di belakang** titik yang dihitung
- Galat pemotongan **O(h)**

**Kesimpulan:** sederhana, tetapi ketelitiannya dipengaruhi ukuran langkah h. Orde O(h) berlaku untuk fungsi yang cukup mulus. (Di buku, beda mundur adalah Pers. 6.1 dengan h \< 0.)

Sumber: Imron dkk. (2022), hlm. 186Slide 5 dari 21

Dua rumus ini adalah yang paling sederhana. Maju memakai titik di depan, mundur memakai titik di belakang. Keduanya hanya butuh dua nilai fungsi dan galatnya berorde h, jadi h harus kecil. Di buku, rumus mundur tidak ditulis terpisah: ia adalah Persamaan 6.1 dengan h negatif.

6.1 · Pendekatan Deret

## Metode Selisih Tengah

\\(f'(x_0)\\approx\\frac{f(x_0+h)-f(x_0-h)}{2h}\\)

Pers. 6.5 (tiga titik tengah) memuat suku galat \\(-\\frac{h^2}{6}f'''(\\xi_1)\\), ξ₁ ∈ (x₀−h, x₀+h)

- Memakai titik di **kiri dan kanan** x
- Pendekatan simetris
- Galat pemotongan **O(h²)** untuk fungsi cukup mulus
- Umumnya lebih teliti daripada maju/mundur pada h yang sama

**Kelebihan:** lebih teliti untuk banyak fungsi mulus.\
**Keterbatasan:** perlu nilai fungsi di kedua sisi titik.

Sumber: Imron dkk. (2022), hlm. 189Slide 6 dari 21

Selisih tengah adalah rumus tiga titik tengah di buku (6.5), tanpa memakai f(x₀) itu sendiri. Karena simetris, suku galat orde pertama saling meniadakan, sehingga galatnya berorde h². Syaratnya, kita punya data di kiri dan kanan titik. Di ujung interval rumus ini tidak bisa dipakai, dan itulah alasan slide berikutnya.

6.1 · Pendekatan Deret

## Rumus Tiga Titik dan Lima Titik

### A. Tiga titik ujung (6.4)

\\(f'(x_0)\\approx\\frac{-3f(x_0)+4f(x_0+h)-f(x_0+2h)}{2h}\\)

- Tiga nilai fungsi, cocok di **ujung interval**
- Galat \\(\\frac{h^2}{3}f'''(\\xi_0)\\) → O(h²)

### B. Lima titik tengah (6.7)

\\(f'(x_0)\\approx\\frac{f(x_0-2h)-8f(x_0-h)+8f(x_0+h)-f(x_0+2h)}{12h}\\)

- Dua titik di kiri dan dua di kanan x₀
- Galat \\(\\frac{h^4}{30}f^{(5)}(\\xi)\\) → O(h⁴)

**C. Lima titik ujung (6.6)**

\\(f'(x_0)\\approx\\frac{-25f(x_0)+48f(x_0+h)-36f(x_0+2h)+16f(x_0+3h)-3f(x_0+4h)}{12h}\\)

- Lima nilai fungsi, semua di satu sisi x₀ (x₀ … x₀+4h)
- Galat \\(\\frac{h^4}{5}f^{(5)}(\\xi)\\) → O(h⁴)
- Berguna bila data di sisi lain ujung tidak ada

| Aspek | Tiga titik ujung | Lima titik tengah | Lima titik ujung |
| --- | --- | --- | --- |
| Jumlah nilai fungsi | 3 | 5 | 5 |
| Lokasi penggunaan | Ujung interval | Titik tengah | Ujung interval |
| Orde galat | O(h²) | O(h⁴) | O(h⁴) |

Sumber: Imron dkk. (2022), hlm. 189Slide 7 dari 21

Rumus tiga titik ujung dipakai saat titik yang dihitung ada di ujung data. Perhatikan koefisien −3, 4, −1 dan penyebut 2h. Rumus lima titik tengah memakai koefisien 1, −8, 8, −1 dan penyebut 12h; galatnya berorde h⁴. Rumus lima titik ujung (6.6) bekerja seperti tiga titik ujung tetapi memakai lima titik ke satu arah: koefisien −25, 48, −36, 16, −3 dan penyebut 12h. Untuk ujung kanan, pakai h negatif, seperti pada Contoh 6.1.3. Harga yang dibayar rumus lima titik adalah kebutuhan data yang lebih banyak.

Contoh 6.1.1

## Contoh: Selisih Maju untuk f(x) = ln x

**Diketahui:** f(x) = ln x, x₀ = 1,8

\\(f'(1{,}8)\\approx\\frac{\\ln 1{,}9-\\ln 1{,}8}{0{,}1}=\\frac{0{,}64185389-0{,}58778667}{0{,}1}=0{,}5406722\\)

**Nilai eksak:** f′(x) = 1/x → f′(1,8) = 1/1,8 ≈ **0,5555556**

| h | Pendekatan | Galat aktual | Batas atas \\(\|h\|/2(1{,}8)^2\\) |
| --- | --- | --- | --- |
| 0,1 | 0,5406722 | 0,0148834 | 0,0154321 |
| 0,05 | 0,5479795 | 0,0075761 | 0,0077160 |
| 0,01 | 0,5540180 | 0,0015376 | 0,0015432 |

Batas atas ≠ galat aktual; galat aktual = |eksak − pendekatan|.

- Nilai pendekatan berubah ketika h diubah.
- Pada contoh ini, h makin kecil → pendekatan makin dekat ke nilai eksak.
- Tetap bedakan nilai **pendekatan** dan nilai **eksak**.

Sumber: Imron dkk. (2022), hlm. 186Slide 8 dari 21

Substitusikan x₀ = 1,8 dan h = 0,1 ke rumus beda maju: ln 1,9 dikurangi ln 1,8, dibagi 0,1, hasilnya 0,5406722. Karena f″(x) = 1/x² dan ξ berada di antara 1,8 dan 1,9, galatnya dibatasi |h|/(2·1,8²) = 0,0154321. Ulangi untuk h = 0,05 dan 0,01. Bandingkan dengan nilai eksak 1/1,8 = 0,5555556: makin kecil h, makin dekat. Kolom terakhir adalah batas galat, bukan galat sebenarnya.

Analisis Galat

## Galat atau Kesalahan Pendekatan

### A. Pengertian

- Turunan numerik = **pendekatan**
- Selisih pendekatan dan nilai eksak = **galat**
- Galat pemotongan: suku ekspansi tertentu diabaikan
- Galat bertanda = eksak − pendekatan; galat absolut = nilainya tanpa tanda

### C. Pengaruh ukuran langkah

- h makin kecil → galat pemotongan umumnya turun
- h terlalu kecil → galat pembulatan bisa dominan
- Galat pemotongan ≠ seluruh galat komputasi

### B. Orde galat (makin panjang = makin kecil galat untuk h kecil)

Selisih maju — O(h)

Selisih mundur — O(h)

Selisih tengah — O(h²)

Tiga titik ujung — O(h²)

Lima titik tengah — O(h⁴)

Lima titik ujung — O(h⁴)

Notasi O(hp) menggambarkan perilaku galat saat h cukup kecil, **bukan** jaminan nilai galat sama untuk semua fungsi. Panjang batang bersifat ilustratif.

Sumber: Imron dkk. (2022), hlm. 186–189Slide 9 dari 21

Setiap rumus yang kita pakai hanya pendekatan. Galat pemotongan muncul karena suku-suku tertentu dibuang. Orde O(h), O(h²), O(h⁴) menunjukkan seberapa cepat galat mengecil ketika h dikecilkan: untuk orde empat, h dibagi 2 membuat galat turun sekitar 16 kali. Batang di slide hanya ilustrasi. Peringatan penting: h yang terlalu kecil memperbesar pengaruh galat pembulatan, jadi h perlu dipilih secara tepat.

Analisis Galat Tambahan di luar buku

## Pengaruh Nilai h dan Sumber Galat

- **Galat pemotongan** \~ hᵖ: **turun** saat h mengecil
- **Galat pembulatan / noise** pada data (besar δ): ± δ/h, **naik** saat h mengecil
- Total (selisih tengah): \\(E(h)\\lesssim\\frac{M h^2}{6}+\\frac{\\delta}{h}\\), dengan M ≥ |f‴|
- Ada h terbaik: \\(h^\*\\approx\\sqrt\[3\]{3\\delta/M}\\) — h yang makin kecil **tidak selalu** lebih akurat

Data pengukuran yang berisik membuat h kecil berbahaya: selisih dua nilai yang hampir sama dibagi bilangan kecil memperbesar gangguan.

| h | Galat selisih maju | Galat selisih tengah |
| --- | --- | --- |
| 10⁻¹ | 1,41×10⁻¹ | 4,53×10⁻³ |
| 10⁻² | 1,36×10⁻² | 4,53×10⁻⁵ |
| 10⁻⁴ | 1,36×10⁻⁴ | 4,53×10⁻⁹ |
| 10⁻⁶ | 1,36×10⁻⁶ | **1,63×10⁻¹⁰** |
| 10⁻⁸ | **6,60×10⁻⁹** | 6,60×10⁻⁹ |
| 10⁻¹⁰ | 1,55×10⁻⁶ | 6,73×10⁻⁷ |
| 10⁻¹² | 4,32×10⁻⁴ | 2,10×10⁻⁴ |
| 10⁻¹⁴ | 9,34×10⁻³ | 9,34×10⁻³ |

f(x) = eˣ di x = 1 (f′(1) = e), aritmetika double. Galat turun lalu naik kembali.

Tambahan: hitungan sendiri; konsep: Burden & Faires \[1\], catatan UMD \[2\]Slide 10 dari 21

Bagian ini di luar buku. Intinya: ada dua sumber galat yang bekerja berlawanan. Galat pemotongan mengecil bila h mengecil (O(h) untuk maju, O(h²) untuk tengah). Tetapi komputer menyimpan f dengan galat pembulatan; selisih f(x+h) − f(x−h) dibagi 2h memperbesar galat itu sekitar δ/h. Karena itu total galat turun lalu naik lagi. Tabel dihitung sendiri dengan f(x) = eˣ di x = 1 (eksak e) memakai aritmetika double: selisih maju terbaik sekitar h = 10⁻⁸, selisih tengah terbaik sekitar h = 10⁻⁶ pada kisi nilai di tabel. Angka persisnya dapat sedikit berbeda antar komputer karena pembulatan. Rumus E(h) dan h\* adalah turunan sederhana dari galat pemotongan (h²/6)·M dan galat data δ; bentuk umum argumen ini ada di Burden & Faires §4.1 \[1\] dan catatan kuliah \[2\], tetapi konstantanya kami tulis sendiri. Hubungkan dengan Slide 8: kalimat 'h terlalu kecil memperbesar galat pembulatan' ditunjukkan secara numerik di sini.

Analisis Galat Tambahan di luar buku

## Galat Absolut, Relatif, dan Persentase

\\(E_a=|f'(x)-D_h|\\)

\\(E_r=\\frac{|f'(x)-D_h|}{|f'(x)|}\\)

\\(E\_{\\%}=E_r\\times100\\%\\)

- Dh: hasil pendekatan dengan langkah h
- Ea: selisih dalam satuan f′
- Er, E%: ukuran relatif terhadap f′

### Contoh (Contoh 6.1.1)

f = ln x, x = 1,8, selisih maju h = 0,1:\
Dh = 0,5406722; f′(1,8) = 0,5555556

\\(E_a=0{,}0148834\\)

\\(E_r=\\frac{0{,}0148834}{0{,}5555556}\\approx0{,}0267901\\)

\\(E\_{\\%}\\approx2{,}679\\%\\)

**Hati-hati:** jika f′(x) = 0 (mis. sin x di x = π/2) Er tidak terdefinisi; jika f′(x) sangat dekat 0, Er membesar dan kurang informatif — gunakan Ea. Buku menghitung galat bertanda (eksak − pendekatan); Ea di sini selalu ≥ 0.

Tambahan: definisi umum \[1\] §1.2; contoh dari data Contoh 6.1.1 (hitungan sendiri)Slide 11 dari 21

Slide ini melengkapi slide galat. E_a memberi besar kesalahan dalam satuan turunan. E_r membandingkannya dengan besar turunan, sehingga bisa dibandingkan antarfungsi. E\_% hanya E_r dikali 100. Contoh: pada Contoh 6.1.1, selisih maju dengan h = 0,1 memberi 0,5406722 sedangkan eksaknya 0,5555556, jadi E_a = 0,0148834; E_r = 0,0148834 / 0,5555556 ≈ 0,0267901; E\_% ≈ 2,679%. Bila turunan eksak nol atau mendekati nol, E_r tidak terdefinisi atau menjadi sangat besar; pakai E_a. Definisi galat absolut dan relatif adalah materi standar analisis numerik (mis. Burden & Faires §1.2). Contoh hitungan ini kami hitung sendiri dari angka buku.

6.2 · Ekstrapolasi Richardson

## Metode Ekstrapolasi Richardson

### A. Pengertian

- Menggabungkan hasil dari **dua ukuran langkah**
- Menghilangkan suku galat utama
- Hasil berorde lebih tinggi bila bentuk galat sesuai

N₁(h): pendekatan awal · N₁(h/2): langkah setengahnya · N₂(h): hasil ekstrapolasi

### B. Galat berpangkat h, h², h³, …

\\(M=N_1(h)+K_1h+K_2h^2+\\cdots\\)

\\(N_2(h)=2N_1(h/2)-N_1(h)\\)

### C. Galat berpangkat genap

\\(M=N_1(h)+K_1h^2+K_2h^4+\\cdots\\)

\\(N_2(h)=\\frac{4N_1(h/2)-N_1(h)}{3}\\)

Rumus C menghilangkan suku h² sehingga hasilnya O(h⁴). Umum (galat pangkat genap): \\(N_j(h)=N\_{j-1}(h/2)+\\frac{1}{4^{j-1}-1}\\big\[N\_{j-1}(h/2)-N\_{j-1}(h)\\big\]\\). **Pilih rumus sesuai bentuk ekspansi galat**, tidak boleh sembarangan.

Sumber: Imron dkk. (2022), hlm. 196–199Slide 12 dari 21

Ide Richardson: kalau galat punya bentuk yang bisa diprediksi, dua hasil dengan h berbeda bisa digabung agar suku galat utama hilang. Untuk galat pangkat 1, 2, 3 dan seterusnya, kurangkan persamaan dengan h dan dua kali persamaan dengan h/2, sehingga K₁ hilang; hasilnya N₂ = 2N₁(h/2) − N₁(h). Untuk galat hanya pangkat genap, kalikan 4 lalu bagi 3 untuk menghilangkan h². Kunci: periksa dulu bentuk galat awalnya, baru pilih rumus.

Contoh 6.2.1

## Contoh Richardson untuk f(x) = ln x

Diketahui N₁(0,1) = 0,5406722 dan N₁(0,05) = 0,5479795. Selisih maju berorde O(h), maka:

\\(N_2(0{,}1)=2N_1(0{,}05)-N_1(0{,}1)\\)

\\(=2(0{,}5479795)-0{,}5406722\\approx0{,}5552868\\)

Galat = |0,5555556 − hasil|, dihitung dari digit yang tampil di slide. Buku menulis hasil 0,555287 dan galat Richardson 0,000258; hitung ulang kami 0,000269 (0,0002688). Lihat catatan pembicara.

| Metode | Hasil | Galat |
| --- | --- | --- |
| Selisih maju, h = 0,1 | 0,5406722 | 0,0148834 |
| Selisih maju, h = 0,05 | 0,5479795 | 0,0075761 |
| **Richardson** | **0,5552868** | **0,0002688** |
| Nilai eksak | 0,5555556 | — |

Jarak ke nilai eksak (makin pendek makin dekat)

h = 0,1 · 0,01488

h = 0,05 · 0,00758

Richardson · 0,00027

Sumber: Imron dkk. (2022), hlm. 197–198Slide 13 dari 21

Ambil dua hasil dari Slide 7. Karena galat awalnya berorde h, pakai N₂ = 2N₁(h/2) − N₁(h). Hitung: dua kali 0,5479795 adalah 1,0959590, dikurangi 0,5406722 menghasilkan 0,5552868. Hasil ini jauh lebih dekat ke 0,5555556 daripada kedua pendekatan awal. Soal pembulatan: buku menulis hasil 0,555287 (pembulatan 6 digit dari 0,5552868). Galat Richardson yang tercatat di buku adalah 0,000258, sedangkan hitung ulang dari angka buku sendiri memberi 0,0002688 (0,000269 bila memakai 0,555287). Galat untuk h = 0,1 dan h = 0,05 (0,01488 dan 0,007576) cocok dengan buku. Kami memakai angka yang konsisten dengan digit di slide dan tidak menyimpulkan penyebab selisihnya.

Contoh 6.1.2

## Penerapan pada Data Tabel: f(x) = x eˣ

| x | f(x) (data tabel) |
| --- | --- |
| 1,8 | 10,889365 |
| 1,9 | 12,703199 |
| 2,0 | 14,778112 |
| 2,1 | 17,148957 |
| 2,2 | 19,855030 |

**Eksak:** f′(x) = (1+x)eˣ → f′(2) = 3e² ≈ **22,167168**

| Rumus (h = 0,1) | Pendekatan f′(2) | Galat bertanda (eksak − pend.) | Galat absolut |
| --- | --- | --- | --- |
| Tiga titik ujung | 22,032310 | 1,35×10⁻¹ | 1,35×10⁻¹ |
| Tiga titik tengah | 22,228790 | −6,16×10⁻² | 6,16×10⁻² |
| Lima titik tengah | 22,166999 | 1,69×10⁻⁴ | 1,69×10⁻⁴ |

- Dihitung dari nilai **tabel**; tiap rumus memberi hasil berbeda.
- Lima titik tengah sangat dekat dengan nilai eksak — tetapi tetap **pendekatan**.
- Data yang sama dipakai untuk Richardson pada Contoh 6.2.2 (Contoh 6.2.2).

Sumber: Imron dkk. (2022), hlm. 190–191Slide 14 dari 21

Data hanya tabel lima titik. Tiga titik ujung: 5 × (−3(14,778112) + 4(17,148957) − 19,855030) = 22,032310. Tiga titik tengah: 5 × (17,148957 − 12,703199) = 22,228790. Lima titik tengah: (10,889365 − 8(12,703199) + 8(17,148957) − 19,855030)/1,2 = 22,166999. Nilai eksak 3e² = 22,167168 hanya dipakai sebagai pembanding. Di buku, teks galat nomor 5 tertulis "lima titik akhir", padahal yang dihitung adalah lima titik tengah; di slide ini sudah kita rapikan.

Contoh 6.1.3

## Contoh 6.1.3 — Menghitung Turunan dari Data Tabel

| x | f(x) |
| --- | --- |
| 1,1 | 9,025013 |
| 1,2 | 11,02318 |
| 1,3 | 13,46374 |
| 1,4 | 16,44465 |
| 1,5 | 20,08554 |

Soal: lengkapi kolom f′(x), h = 0,1. Turunan dihitung dari **nilai tabel**, bukan dengan menurunkan rumus fungsi.

| Titik | Rumus (h): 6.4, 6.6 = ujung; 6.5, 6.7 = tengah |
| --- | --- |
| 1,1 | 6.4 (0,1; 0,2) · 6.6 (0,1) |
| 1,2 | 6.4 (0,1) · 6.5 (0,1) |
| 1,3 | 6.4 (±0,1) · 6.5 (0,1; 0,2) · 6.7 (0,1) |
| 1,4 | 6.4 (−0,1) · 6.5 (0,1) |
| 1,5 | 6.4 (−0,1; −0,2) · 6.6 (−0,1) |

Pilihan rumus mengikuti posisi titik: ujung atau tengah.

f′(1,1), **titik ujung**, Pers. 6.4, h = 0,1: \\(\\frac{-3(9{,}025013)+4(11{,}02318)-13{,}46374}{0{,}2}=17{,}76971\\)

f′(1,3), **titik tengah**, Pers. 6.5, h = 0,1: \\(\\frac{16{,}44465-11{,}02318}{0{,}2}=27{,}10735\\)

f′(1,3), **titik tengah**, Pers. 6.7, h = 0,1: \\(\\frac{9{,}025013-8(11{,}02318)+8(16{,}44465)-20{,}08554}{1{,}2}=26{,}92603\\)

Hasil buku untuk f′(1,3): 26,5092 (6.4, h=0,1) · 26,61757 (6.4, h=−0,1) · 27,10735 (6.5, h=0,1) · 27,65132 (6.5, h=0,2) · 26,92603 (6.7).

Sumber: Imron dkk. (2022), hlm. 191–195Slide 15 dari 21

Berbeda dari Contoh 6.1.2, di sini yang diminta adalah melengkapi kolom turunan dari data tabel dengan h = 0,1. Langkahnya: lihat posisi titik. Di ujung (1,1 dan 1,5) tidak ada data di salah satu sisi, jadi pakai rumus ujung (6.4 atau 6.6; di ujung kanan h dibuat negatif). Di titik dalam, rumus tengah 6.5 bisa dipakai, dan lima titik tengah 6.7 hanya untuk 1,3 karena butuh dua titik di tiap sisi. Hitungan memakai nilai tabel penuh; buku menampilkannya dibulatkan (mis. 9,02501), tetapi hasil akhirnya sama dengan yang tertulis di buku, misalnya 17,76971 untuk f′(1,1) lewat 6.4. Hasil tiap rumus berbeda; slide ini tidak membandingkan dengan nilai eksak karena buku tidak memberikannya.

Contoh 6.2.2

## Contoh 6.2.2 — Ekstrapolasi Richardson pada f(x) = xeˣ

Hitung f′(2,0), h = 0,2. Awal: \\(N_1(h)=\\frac{f(x_0+h)-f(x_0-h)}{2h}\\) (galat pangkat genap). Lalu \\(N_2(h)=N_1(\\tfrac h2)+\\tfrac13\[N_1(\\tfrac h2)-N_1(h)\]\\), \\(N_3(h)=N_2(\\tfrac h2)+\\tfrac1{15}\[N_2(\\tfrac h2)-N_2(h)\]\\)

| Langkah | Perhitungan | Hasil |
| --- | --- | --- |
| N₁(0,2) | 2,5(19,855030 − 10,889365) | 22,414160 |
| N₁(0,1) | 5(17,148957 − 12,703199) | 22,228786 |
| N₂(0,2) | 22,228786 + (22,228786 − 22,414160)/3 | **22,166995** |
| N₁(0,05) | 10(15,924197 − 13,705941)\* | 22,182564 |
| N₂(0,1) | 22,182564 + (22,182564 − 22,228786)/3 | 22,167157 |
| N₃(0,2) | 22,167157 + (22,167157 − 22,166995)/15 | **22,167168** |

**Eksak:** f′(2) = 3e² ≈ 22,167168. N₃(0,2) sama dengan nilai eksak sampai enam angka desimal yang ditampilkan; N₂(0,2) sama sampai 22,167. \*f(2,05) dan f(1,95) dipakai buku (tidak ada di tabel lima titik). Angka di atas dari buku; hitung ulang dari tabel Contoh 6.1.2 memberi N₁(0,2) = 22,414163, N₁(0,1) = 22,228790, N₂(0,2) = 22,166999 (selisih ≤ 4×10⁻⁶).

Sumber: Imron dkk. (2022), hlm. 200–201Slide 16 dari 21

Rumus tengah punya galat berpangkat genap, jadi dipakai pembagi 3 (tingkat dua) lalu pembagi 15 (tingkat tiga; rumus umumnya 4^(j−1) − 1). Urutan: hitung N₁ untuk h = 0,2; 0,1; 0,05. Gabungkan N₁(0,1) dan N₁(0,2) menjadi N₂(0,2); gabungkan N₁(0,05) dan N₁(0,1) menjadi N₂(0,1); gabungkan kedua N₂ menjadi N₃(0,2). Jangan tertukar: angka dalam kurung adalah ukuran langkah. Di buku, rumus N₃ tertulis memakai N₂(0,1) − N₁(0,2); yang sesuai rumus umum adalah N₂(0,1) − N₂(0,2), dan angka buku 22,167168 cocok dengan itu. Angka N₁ di buku berbeda sedikit di digit ke-6 dari hitung ulang pada Contoh 6.1.2; kami menampilkan angka buku dan hitung ulang memberi N₂(0,2) = 22,166999, sama dengan hasil lima titik tengah.

Contoh 6.2.3

## Contoh 6.2.3 — Ekstrapolasi Richardson dari Data Tabel

| x | f(x) |
| --- | --- |
| 1,1 | 9,025013 |
| 1,2 | 11,02318 |
| 1,3 | 13,46374 |
| 1,4 | 16,44465 |
| 1,5 | 20,08554 |

Titik: x₀ = 1,3; h = 0,2. Beda dengan Contoh 6.1.3: di sini hasil **digabung** dengan Richardson, bukan memilih satu rumus.

**Pendekatan awal** (tiga titik tengah, O(h²))

\\(N_1(0{,}2)=\\frac{20{,}08554-9{,}025013}{0{,}4}=27{,}651318\\)

\\(N_1(0{,}1)=\\frac{16{,}44465-11{,}02318}{0{,}2}=27{,}10735\\)

**Richardson (galat genap)**

\\(N_2(0{,}2)=N_1(0{,}1)+\\tfrac13\[N_1(0{,}1)-N_1(0{,}2)\]\\)

\\(=27{,}10735+\\tfrac13(27{,}10735-27{,}651318)\\approx\\mathbf{26{,}926027}\\)

N₂ berorde O(h⁴), diharapkan lebih teliti dari kedua N₁. N₃ **tidak bisa** dihitung: butuh N₁(0,05), yaitu f(1,35) dan f(1,25) yang tidak tersedia. Buku tidak memberi nilai eksak.

**Catatan:** hasil hitung ulang dari angka di atas ≈ 26,926027, sedangkan buku mencantumkan 26,920273. Buku juga menulis N₁(0,1) dengan f(1,1); nilai 27,10735 sesuai dengan f(1,2). Rinciannya ada di catatan pembicara.

Sumber: Imron dkk. (2022), hlm. 201–202Slide 17 dari 21

Titik yang dihitung f′(1,3) dengan h = 0,2 dan 0,1; data hanya 1,1 sampai 1,5, jadi level ketiga tidak mungkin. Catatan penyaji (dicek pada halaman buku 201–202): buku mencetak N₁(0,1) = (1/0,2)(f(1,4) − f(1,1)) = 27,10735 dan N₂(0,2) = 26,920273. Dua hal ini tidak cocok dengan substitusi yang tercetak: (16,44465 − 11,02318)/0,2 memakai f(1,2) dan menghasilkan 27,10735, sedangkan dengan f(1,1) hasilnya lain; dan 27,10735 + (27,10735 − 27,651318)/3 = 26,926027, bukan 26,920273. Nilai 26,926027 juga sama dengan hasil lima titik tengah 26,92603 pada Contoh 6.1.3 butir 3(e). Penyebab pasti selisihnya tidak dapat dibuktikan dari buku; mungkin salah cetak, tetapi itu hanya dugaan. Slide menampilkan hasil hitung ulang dan menyebut angka buku secara terpisah. Hasil N₂ lebih teliti daripada kedua N₁ karena orde galatnya O(h⁴).

Ringkasan Metode

## Perbandingan Metode Diferensiasi Numerik

| Metode | Titik / data | Galat pemotongan | Kelebihan | Keterbatasan |
| --- | --- | --- | --- | --- |
| Selisih maju | x, x+h | O(h) | Sederhana, 2 nilai | Kurang teliti |
| Selisih mundur | x−h, x | O(h) | Cocok di ujung kanan data | Kurang teliti |
| Selisih tengah | x−h, x+h | O(h²) | Simetris, lebih teliti | Butuh data dua sisi |
| Tiga titik ujung | x₀, x₀+h, x₀+2h | O(h²) | Dipakai di ujung interval | Butuh 3 nilai |
| Lima titik tengah | x₀±h, x₀±2h | O(h⁴) | Sangat teliti | Butuh 5 nilai, kedua sisi |
| Lima titik ujung | x₀ … x₀+4h | O(h⁴) | Teliti, data satu sisi | Butuh 5 nilai |
| Ekstrapolasi Richardson\* | Hasil N₁ dari h dan h/2 | Bergantung orde awal & skema | Menaikkan ketelitian | Bentuk galat harus sesuai |

\*Richardson bukan rumus diferensiasi langsung; ia memperbaiki hasil rumus lain.

**Kesimpulan:** pemilihan metode bergantung pada posisi titik yang dihitung, ketersediaan data, bentuk galat, dan tingkat ketelitian yang dibutuhkan.

Sumber: Imron dkk. (2022), Bab 6 (ringkasan)Slide 18 dari 21

Gunakan tabel ini untuk merangkum. Maju dan mundur: sederhana tetapi O(h). Selisih tengah dan tiga titik ujung: O(h²). Lima titik tengah dan lima titik ujung: O(h⁴). Richardson berbeda jenis; ia tidak menurunkan rumus baru dari data, tetapi menggabungkan hasil rumus lain, sehingga ordenya bergantung pada orde awal dan skema ekstrapolasi (mis. O(h²) lalu O(h⁴) pada galat pangkat genap).

Ringkasan Metode Kolom kondisi: tambahan di luar buku

## Memilih Metode: Rumus dan Kondisi Penggunaan

| Metode | Rumus / prinsip dasar | Orde | Data | Kondisi penggunaan |
| --- | --- | --- | --- | --- |
| Selisih maju | \[f(x+h) − f(x)\]/h | O(h) | x, x+h | Ujung kiri data; hanya data ke depan |
| Selisih mundur | \[f(x) − f(x−h)\]/h | O(h) | x−h, x | Ujung kanan data; hanya data sebelumnya |
| Selisih tengah | \[f(x+h) − f(x−h)\]/(2h) | O(h²) | x±h | Titik dalam data; pilihan umum |
| Tiga titik ujung | \[−3f(x)+4f(x+h)−f(x+2h)\]/(2h) | O(h²) | 3 titik satu sisi | Ujung data, butuh orde 2 |
| Lima titik tengah | \[f(x−2h)−8f(x−h)+8f(x+h)−f(x+2h)\]/(12h) | O(h⁴) | 5 titik simetris | Titik dalam; data cukup dan fungsi mulus |
| Lima titik ujung | \[−25f(x)+48f(x+h)−36f(x+2h)+16f(x+3h)−3f(x+4h)\]/(12h) | O(h⁴) | 5 titik satu sisi | Ujung data, butuh orde 4 |
| Richardson | Gabungkan N₁(h) dan N₁(h/2) untuk membuang suku galat utama | Tergantung orde awal | ≥ 2 hasil N₁ | Memperbaiki hasil yang ada; bentuk galat harus diketahui |

Tidak ada metode yang selalu terbaik: ketelitian aktual bergantung pada fungsi, nilai h, dan kualitas data (noise membuat h kecil dan rumus berkoefisien besar kurang menguntungkan).

Rumus dan orde: Imron dkk. (2022), hlm. 186–189; kolom kondisi: tambahan \[1\]Slide 19 dari 21

Slide ini melengkapi slide 'Perbandingan Metode' sebelumnya: di sana fokus pada kelebihan dan keterbatasan, di sini pada rumus dasar dan kapan dipakai. Rumus dan orde galat berasal dari buku. Kolom 'kondisi penggunaan' adalah pengembangan penjelasan kami, mengikuti prinsip standar di buku analisis numerik (mis. Burden & Faires §4.1–4.2). Pesan penutup: jangan menyimpulkan satu metode selalu paling baik. Lima titik memiliki orde lebih tinggi, tetapi koefisiennya lebih besar (−25, 48, −36, …) sehingga lebih sensitif terhadap noise pada data, dan membutuhkan lebih banyak data; ini kesimpulan kualitatif, bukan klaim dari buku.

Penutup

## Kesimpulan

- Diferensiasi numerik memperkirakan turunan dari nilai fungsi.
- Pendekatan deret (polinomial Lagrange / Taylor) menjadi dasar rumus-rumusnya.
- Selisih maju dan mundur: galat pemotongan **O(h)**.
- Selisih tengah dan tiga titik ujung: **O(h²)**.
- Lima titik (tengah dan ujung): **O(h⁴)**.
- Richardson meningkatkan ketelitian bila bentuk galat dan rumusnya sesuai.
- Pilih h dengan mempertimbangkan galat pemotongan dan pembulatan; orde lebih tinggi tidak selalu terbaik di semua situasi.

“Ketelitian diferensiasi numerik tidak hanya ditentukan oleh rumus yang digunakan, tetapi juga oleh ukuran langkah, data yang tersedia, dan sifat fungsi.”

Sumber: Imron dkk. (2022), Bab 6 (ringkasan)Slide 20 dari 21

Rangkum perjalanan: dari definisi, dasar deret, rumus maju/mundur/tengah, rumus tiga dan lima titik, galat, lalu Richardson. Tekankan tiga hal: orde galat menentukan kecepatan perbaikan saat h mengecil, rumus harus cocok dengan posisi titik dan data yang ada, dan h tidak boleh terlalu kecil. Tutup dengan kalimat di bawah slide, lalu buka sesi tanya jawab.

Referensi

## Daftar Pustaka

Imron, C., Mardlijah, & Asfihani, T. (2022). *Metode Numerik*. Departemen Matematika ITS. ISBN 978-623-318-126-6.

**Referensi tambahan (di luar buku)**\
\[1\] Burden, R. L., & Faires, J. D. *Numerical Analysis*, 9th ed. Cengage Learning (hak cipta 2010) — §1.2 (galat), §4.1 (Numerical Differentiation), §4.2 (Richardson’s Extrapolation).\
\[2\] Catatan kuliah AMSC 466 (University of Maryland), “Numerical differentiation”: math.umd.edu/\~mariakc/AMSC466/LectureNotes/differentiation.pdf — pertukaran galat pemotongan dan pembulatan.

Data bibliografi diambil dari halaman identitas buku: “© 2022 Departemen Matematika ITS” dan ISBN 978-623-318-126-6. Kota terbit, edisi, DOI, dan URL buku utama tidak tercantum di halaman identitas, sehingga tidak ditulis. Materi bertanda “Tambahan di luar buku” dan angka hitungan sendiri dibedakan dari isi buku.

Sumber: halaman identitas bukuSlide 21 dari 21

Sebutkan sumber utama presentasi: buku Metode Numerik karya Chairul Imron, Mardlijah, dan Tahiyatul Asfihani (2022), Bab 6. Semua rumus, contoh, dan angka diambil dari bab ini. Penerbit di halaman identitas adalah Departemen Matematika ITS. Kota terbit dan edisi tidak tercantum di halaman identitas, jadi sengaja tidak ditulis.

1 / 21