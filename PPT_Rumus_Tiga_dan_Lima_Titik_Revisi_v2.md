4<!-- Slide 1 -->
# Konsep Dasar

Sering kali kita hanya punya tabel nilai x dan f(x). Turunan di x₀ diperkirakan dari beberapa nilai f yang jaraknya sama, yaitu h.

| 1.8 | 1.9 | 2.0 | 2.1 | 2.2 |
| --- | --- | --- | --- | --- |
| x₀−2h | x₀−h | x₀ | x₀+h | x₀+2h |

Contoh: x₀ = 2.0 dan h = 0.1

**Tiga titik**
Memakai 3 posisi data untuk memperkirakan turunan.

**Lima titik**
Memakai 5 posisi data. Pendekatan lebih teliti, tetapi butuh data lebih banyak.

**Akhir**
Dipakai bila x₀ di ujung data, sehingga semua data ada di satu sisi.

**Tengah**
Dipakai bila ada data di kiri dan kanan x₀ secara simetris.

1

**Catatan:** Pengantar. Tekankan dua pembeda: jumlah titik (3 atau 5) dan posisi titik (akhir atau tengah). Lima titik butuh lebih banyak data tetapi lebih teliti. Analisis galat dibahas anggota lain.

---

<!-- Slide 2 -->
# Rumus Tiga Titik

## Tiga Titik Akhir

$$f'(x_0) \approx \frac{1}{2h}\left[-3f(x_0) + 4f(x_0+h) - f(x_0+2h)\right]$$

$$\text{Galat} = \frac{h^2}{3} f^{(3)}(\xi_0), \quad \xi_0 \in (x_0, x_0+2h)$$

| −3 | 4 | −1 |
| --- | --- | --- |
| x₀ | x₀+h | x₀+2h |

× 1/(2h) · dipakai di ujung data (satu sisi) · orde galat O(h²)

## Tiga Titik Tengah

$$f'(x_0) \approx \frac{1}{2h}\left[f(x_0+h) - f(x_0-h)\right]$$

$$\text{Galat} = -\frac{h^2}{6} f^{(3)}(\xi_1), \quad \xi_1 \in (x_0-h, x_0+h)$$

| −1 | 0 | 1 |
| --- | --- | --- |
| x₀−h | x₀ | x₀+h |

× 1/(2h) · dipakai di dalam data (kiri–kanan) · orde galat O(h²)

Tetap tiga posisi titik. Koefisien f(x₀) = 0, jadi nilainya tidak muncul dalam perhitungan.

2

**Catatan:** Rumus tiga titik tengah memakai tiga POSISI data: x₀−h, x₀, x₀+h. Koefisien f(x₀) adalah 0, sehingga hanya f(x₀+h) dan f(x₀−h) yang muncul di rumus. Itulah alasan disebut tiga titik walaupun hanya dua nilai fungsi yang dihitung. Rumus akhir dengan h negatif menjadi versi mundur dari ujung kanan data.

---

<!-- Slide 3 -->
# Rumus Lima Titik

## Lima Titik Akhir

$$f'(x_0) \approx \frac{1}{12h}\left[-25f(x_0) + 48f(x_0+h) - 36f(x_0+2h) + 16f(x_0+3h) - 3f(x_0+4h)\right]$$

$$\text{Galat} = \frac{h^4}{5} f^{(5)}(\xi), \quad \xi \in (x_0, x_0+4h)$$

| −25 | 48 | −36 | 16 | −3 |
| --- | --- | --- | --- | --- |
| x₀ | x₀+h | x₀+2h | x₀+3h | x₀+4h |

× 1/(12h) · dipakai di ujung data · O(h⁴)

## Lima Titik Tengah

$$f'(x_0) \approx \frac{1}{12h}\left[f(x_0-2h) - 8f(x_0-h) + 8f(x_0+h) - f(x_0+2h)\right]$$

$$\text{Galat} = \frac{h^4}{30} f^{(5)}(\xi), \quad \xi \in (x_0-2h, x_0+2h)$$

| 1 | −8 | 0 | 8 | −1 |
| --- | --- | --- | --- | --- |
| x₀−2h | x₀−h | x₀ | x₀+h | x₀+2h |

× 1/(12h) · dipakai di dalam data · O(h⁴)

3

**Catatan:** Memakai polinomial Lagrange melalui lima titik sehingga galat turun ke orde h⁴. Lima titik akhir: x₀ sampai x₀+4h. Lima titik tengah: x₀−2h sampai x₀+2h, f(x₀) berkoefisien 0.

---

<!-- Slide 4 -->
# Tiga Titik vs Lima Titik

**Tiga titik**

| 1.8 | 1.9 | 2.0 | 2.1 | 2.2 |
| --- | --- | --- | --- | --- |

Orde galat O(h²)

Data lebih sedikit, perhitungan lebih singkat.

**Lima titik**

| 1.8 | 1.9 | 2.0 | 2.1 | 2.2 |
| --- | --- | --- | --- | --- |

Orde galat O(h⁴)

Data lebih banyak, pendekatan umumnya lebih teliti untuk h kecil.

Pada contoh f(x) = x·eˣ (tengah, h = 0.1): galat tiga titik ≈ 6.16×10⁻², galat lima titik ≈ 1.69×10⁻⁴. Lima titik lebih teliti, tetapi membutuhkan lebih banyak data.

4

**Catatan:** Gambar memakai contoh tengah x₀ = 2.0, h = 0.1. Pada tiga titik hanya 2 nilai fungsi dihitung (1.9 dan 2.1), pada lima titik 4 nilai (1.8, 1.9, 2.1, 2.2). Orde galat O(h²) dan O(h⁴) cukup disebut sekilas; analisis galat dibahas anggota lain.

---

<!-- Slide 5 -->
# Memilih Rumus

| Rumus | Posisi titik yang dipakai | Data | Dipakai bila |
| --- | --- | --- | --- |
| Tiga titik akhir | x₀, x₀+h, x₀+2h | Satu sisi | Titik di ujung data |
| Tiga titik tengah | x₀−h, x₀, x₀+h (f(x₀) koef. 0) | Simetris | Ada data kiri dan kanan |
| Lima titik akhir | x₀ sampai x₀+4h | Satu sisi | Ujung data, 4 titik tersedia |
| Lima titik tengah | x₀−2h sampai x₀+2h (f(x₀) koef. 0) | Simetris | Ada 2 data kiri dan 2 kanan |

5

**Catatan:** Pilih rumus berdasarkan posisi titik yang dicari: ujung data memakai rumus akhir, di dalam data memakai rumus tengah. Untuk f′(1.5) data hanya ada di kiri, maka rumus akhir dipakai dengan h negatif (memakai 1.5, 1.4, 1.3 untuk tiga titik).

---

<!-- Slide 6 -->
# Cara Menghitung

1. **Tentukan x₀ dan h**
   Titik yang dicari turunannya adalah x₀. h adalah jarak antar-data.

2. **Pilih rumus**
   Data satu sisi: akhir. Data mengapit x₀: tengah. Lalu pilih tiga atau lima titik.

3. **Substitusi**
   Ambil nilai f(x) dari tabel sesuai posisi titik, kalikan dengan koefisiennya.

4. **Hitung**
   Jumlahkan, lalu bagi dengan 2h (tiga titik) atau 12h (lima titik).

**h = jarak antar-data**
Contoh: h = 2.1 − 2.0 = 0.1. Bukan nilai fungsi dan bukan hasil turunan.

**h boleh negatif**
Rumus akhir dengan h = −0.1 memakai titik di sebelah kiri x₀ (dari ujung kanan data).

6

**Catatan:** Empat langkah yang sama untuk keempat rumus. h adalah jarak antar-data, bukan nilai fungsi dan bukan hasil turunan. h negatif dipakai saat rumus akhir diterapkan dari ujung kanan data.

---

<!-- Slide 7 -->
# Soal 1: Tiga Titik Akhir

| x | 1.8 | 1.9 | 2.0 | 2.1 | 2.2 |
| --- | --- | --- | --- | --- | --- |
| f(x) | 10.889365 | 12.703199 | 14.778112 | 17.148957 | 19.855030 |

f(x) = x·eˣ · nilai eksak f′(2.0) = 3e² = 22.167168 (pembanding galat)

**Soal**
Diberikan tabel nilai f(x) = x·eˣ. Hitunglah hampiran turunan f′(2.0) dengan rumus tiga titik akhir (x₀ = 2.0, h = 0.1), lalu tentukan galatnya terhadap nilai eksak.

**Instruksi**
Kerjakan secara berurutan, langkah 1 sampai 4:

1. Substitusikan f(2.0), f(2.1), f(2.2) dari tabel ke rumus [−3f(x₀) + 4f(x₀+h) − f(x₀+2h)] / 2h.
2. Kalikan setiap nilai f dengan koefisiennya: −3, 4, dan −1.
3. Jumlahkan ketiga hasil kali, lalu bagi dengan 2h = 0.2.
4. Hitung galat = eksak − hampiran. Tulis hasil dengan 6 angka desimal dan galat dalam bentuk a×10ᵇ.

7

**Catatan:** Soal 1. Pastikan siswa membaca dulu: rumus apa (tiga titik akhir), x₀ berapa, h berapa. Empat instruksi di slide ini sama urutannya dengan empat langkah di slide penyelesaian. Beri waktu sekitar 3 menit sebelum membuka slide berikutnya.

---

<!-- Slide 8 -->
# Penyelesaian 1: Tiga Titik Akhir

| x | 1.8 | 1.9 | 2.0 | 2.1 | 2.2 |
| --- | --- | --- | --- | --- | --- |
| f(x) | 10.889365 | 12.703199 | 14.778112 | 17.148957 | 19.855030 |

f(x) = x·eˣ · nilai eksak f′(2.0) = 3e² = 22.167168 (pembanding galat)

**Tiga titik akhir · x₀ = 2.0, h = 0.1**

f′(2.0) ≈ [−3f(2.0) + 4f(2.1) − f(2.2)] / (2·0.1)

1. **Masukkan nilai tabel**
   = [−3(14.778112) + 4(17.148957) − 19.855030] / 0.2

2. **Kalikan setiap nilai**
   = (−44.334336 + 68.595828 − 19.855030) / 0.2

3. **Jumlahkan, lalu bagi**
   = 4.406462 / 0.2 = 22.032310

4. **Bandingkan dengan eksak**
   Galat = 22.167168 − 22.032310 = 1.35×10⁻¹

8

**Catatan:** Dengan h = −0.1 hasilnya 22.054525, galat 1.13×10⁻¹. Langkah sama: masukkan nilai, kalikan, jumlahkan, bagi 2h.

---

<!-- Slide 9 -->
# Soal 2: Tiga Titik Tengah

| x | 1.8 | 1.9 | 2.0 | 2.1 | 2.2 |
| --- | --- | --- | --- | --- | --- |
| f(x) | 10.889365 | 12.703199 | 14.778112 | 17.148957 | 19.855030 |

f(x) = x·eˣ · nilai eksak f′(2.0) = 3e² = 22.167168 (pembanding galat)

**Soal**
Dengan tabel yang sama, hitunglah hampiran f′(2.0) memakai rumus tiga titik tengah (x₀ = 2.0, h = 0.1), lalu tentukan galatnya. Bandingkan dengan galat tiga titik akhir pada Soal 1.

**Instruksi**
Kerjakan secara berurutan, langkah 1 sampai 4:

1. Substitusikan f(2.1) dan f(1.9) dari tabel ke rumus [f(x₀+h) − f(x₀−h)] / 2h.
2. Kurangkan f(2.1) − f(1.9). Nilai f(2.0) tidak dipakai karena koefisiennya 0.
3. Bagi hasil pengurangan dengan 2h = 0.2.
4. Hitung galat = eksak − hampiran. Bandingkan dengan galat Soal 1 (1.35×10⁻¹): mana yang lebih kecil?

9

**Catatan:** Soal 2. Pertanyaan pancingan: mengapa f(2.0) tidak muncul padahal x₀ = 2.0? Jawaban: koefisiennya 0. Minta siswa membandingkan galat dengan Soal 1 sebelum melihat penyelesaian.

---

<!-- Slide 10 -->
# Penyelesaian 2: Tiga Titik Tengah

| x | 1.8 | 1.9 | 2.0 | 2.1 | 2.2 |
| --- | --- | --- | --- | --- | --- |
| f(x) | 10.889365 | 12.703199 | 14.778112 | 17.148957 | 19.855030 |

f(x) = x·eˣ · nilai eksak f′(2.0) = 3e² = 22.167168 (pembanding galat)

**Tiga titik tengah · x₀ = 2.0, h = 0.1**

f′(2.0) ≈ [f(2.1) − f(1.9)] / (2·0.1)

1. **Masukkan nilai tabel**
   = (17.148957 − 12.703199) / 0.2

2. **Kurangkan**
   = 4.445758 / 0.2

3. **Bagi dengan 2h**
   = 22.228790

4. **Bandingkan dengan eksak**
   Galat = 22.167168 − 22.228790 = −6.16×10⁻² (lebih kecil dari tiga titik akhir: 1.35×10⁻¹)

10

**Catatan:** Dengan h = 0.2 hasilnya 22.414163, galat −2.47×10⁻¹. Galat naik sekitar 4 kali saat h dua kali lebih besar (sesuai orde h²). f(2.0) tidak dipakai karena koefisiennya 0.

---

<!-- Slide 11 -->
# Soal 3: Lima Titik Akhir

| x | 1.8 | 1.9 | 2.0 | 2.1 | 2.2 |
| --- | --- | --- | --- | --- | --- |
| f(x) | 10.889365 | 12.703199 | 14.778112 | 17.148957 | 19.855030 |

f(x) = x·eˣ · nilai eksak f′(1.8) = 2.8e^1.8 = 16.939013 (pembanding galat)

**Soal**
Hitunglah hampiran f′(1.8) dengan rumus lima titik akhir (x₀ = 1.8, h = 0.1), lalu tentukan galatnya. Jelaskan mengapa x₀ = 2.0 tidak dapat dipakai pada rumus ini.

**Instruksi**
Kerjakan secara berurutan, langkah 1 sampai 4:

1. Periksa data: rumus butuh x₀ sampai x₀+4h = 1.8 sampai 2.2. Substitusikan kelima nilai f dari tabel.
2. Kalikan setiap nilai f dengan koefisiennya: −25, 48, −36, 16, dan −3.
3. Jumlahkan kelima hasil kali, lalu bagi dengan 12h = 1.2.
4. Hitung galat = eksak − hampiran. Bandingkan dengan galat tiga titik akhir di x₀ = 1.8 (1.06×10⁻¹).

11

**Catatan:** Soal 3. Jawaban pertanyaan "mengapa bukan 2.0": rumus lima titik akhir membutuhkan x₀ sampai x₀+4h, yaitu 2.0 sampai 2.4, sedangkan tabel hanya sampai 2.2. Hanya x₀ = 1.8 yang punya empat data di kanannya.

---

<!-- Slide 12 -->
# Penyelesaian 3: Lima Titik Akhir

| x | 1.8 | 1.9 | 2.0 | 2.1 | 2.2 |
| --- | --- | --- | --- | --- | --- |
| f(x) | 10.889365 | 12.703199 | 14.778112 | 17.148957 | 19.855030 |

f(x) = x·eˣ · nilai eksak f′(1.8) = 2.8e^1.8 = 16.939013 (pembanding galat)

**Lima titik akhir · x₀ = 1.8, h = 0.1**

f′(1.8) ≈ [−25f(1.8) + 48f(1.9) − 36f(2.0) + 16f(2.1) − 3f(2.2)] / (12·0.1)

1. **Masukkan nilai tabel**
   = [−25(10.889365) + 48(12.703199) − 36(14.778112) + 16(17.148957) − 3(19.855030)] / 1.2

2. **Kalikan setiap nilai**
   = (−272.234125 + 609.753552 − 532.012032 + 274.383312 − 59.565090) / 1.2

3. **Jumlahkan, lalu bagi**
   = 20.325617 / 1.2 = 16.938014

4. **Bandingkan dengan eksak**
   Eksak f′(1.8) = 2.8e^1.8 = 16.939013. Galat = 9.99×10⁻⁴ (tiga titik akhir: 1.06×10⁻¹)

12

**Catatan:** Contoh tambahan di x₀ = 1.8 karena x₀ = 2.0 tidak punya empat titik di kanannya. Rumus sama dengan Contoh 6.1.3 buku untuk f′(1.1).

---

<!-- Slide 13 -->
# Soal 4: Lima Titik Tengah

| x | 1.8 | 1.9 | 2.0 | 2.1 | 2.2 |
| --- | --- | --- | --- | --- | --- |
| f(x) | 10.889365 | 12.703199 | 14.778112 | 17.148957 | 19.855030 |

f(x) = x·eˣ · nilai eksak f′(2.0) = 3e² = 22.167168 (pembanding galat)

**Soal**
Hitunglah hampiran f′(2.0) dengan rumus lima titik tengah (x₀ = 2.0, h = 0.1), lalu tentukan galatnya. Bandingkan dengan galat tiga titik tengah pada Soal 2.

**Instruksi**
Kerjakan secara berurutan, langkah 1 sampai 4:

1. Substitusikan f(1.8), f(1.9), f(2.1), f(2.2) dari tabel. Data tersedia dua di kiri dan dua di kanan x₀.
2. Kalikan setiap nilai f dengan koefisiennya: 1, −8, 8, dan −1. Nilai f(2.0) tidak dipakai (koefisien 0).
3. Jumlahkan keempat hasil kali, lalu bagi dengan 12h = 1.2.
4. Hitung galat = eksak − hampiran. Bandingkan dengan galat Soal 2 (−6.16×10⁻²).

13

**Catatan:** Soal 4. Tekankan kesimpulan: dengan data dan h yang sama, lima titik tengah memberi galat sekitar 10⁻⁴, sedangkan tiga titik tengah sekitar 10⁻².

---

<!-- Slide 14 -->
# Penyelesaian 4: Lima Titik Tengah

| x | 1.8 | 1.9 | 2.0 | 2.1 | 2.2 |
| --- | --- | --- | --- | --- | --- |
| f(x) | 10.889365 | 12.703199 | 14.778112 | 17.148957 | 19.855030 |

f(x) = x·eˣ · nilai eksak f′(2.0) = 3e² = 22.167168 (pembanding galat)

**Lima titik tengah · x₀ = 2.0, h = 0.1**

f′(2.0) ≈ [f(1.8) − 8f(1.9) + 8f(2.1) − f(2.2)] / (12·0.1)

1. **Masukkan nilai tabel**
   = [10.889365 − 8(12.703199) + 8(17.148957) − 19.855030] / 1.2

2. **Kalikan setiap nilai**
   = (10.889365 − 101.625592 + 137.191656 − 19.855030) / 1.2

3. **Jumlahkan, lalu bagi**
   = 26.600399 / 1.2 = 22.166999

4. **Bandingkan dengan eksak**
   Galat = 22.167168 − 22.166999 = 1.69×10⁻⁴ (tiga titik tengah: 6.16×10⁻², lebih dari 300× lebih besar)

14

**Catatan:** Contoh 6.1.2 buku. Perbandingan: galat lima titik sekitar 10⁻⁴, tiga titik sekitar 10⁻².
