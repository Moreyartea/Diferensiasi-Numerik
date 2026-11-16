Metode Numerik — Bab 6

# DIFERENSIASI NUMERIK

Metode Numerik — Bab 6

**Penyusun:** \[Nama anggota kelompok\]\
**Dosen:** \[Nama dosen\]\
**Program Studi / Universitas:** \[Program studi, Universitas\]\
**Tahun:** 2026

Sumber: Imron, Mardlijah & Asfihani (2022)Slide 1 dari 39

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

Sumber: Imron dkk. (2022), hlm. 185Slide 2 dari 39

Turunan menyatakan laju perubahan. Kadang fungsi sulit diperoleh secara analitik eksak, atau data yang tersedia berupa tabel pengukuran diskret. Karena itu kita menggunakan pendekatan diferensiasi numerik. Bab ini memperkenalkan dua metode utama: pendekatan deret dan ekstrapolasi Richardson.

6 · Pengantar Fungsional

## Apa Kegunaan Diferensiasi Numerik?

Diferensiasi numerik membantu kita memperkirakan **seberapa cepat suatu nilai berubah** ketika data yang tersedia hanya berupa hasil pengukuran.

### Contoh Penerapan
- Data posisi kendaraan dapat digunakan untuk memperkirakan kecepatan ($v = ds/dt$)
- Data kecepatan kendaraan dapat digunakan untuk memperkirakan percepatan ($a = dv/dt$)
- Data suhu pada beberapa lokasi dapat digunakan untuk melihat perubahan suhu terhadap jarak ($dT/dx$)
- Data konsentrasi zat dari waktu ke waktu dapat digunakan untuk memperkirakan laju perubahan konsentrasi

### Kapan Diperlukan?
Ketika kita memiliki tabel atau kumpulan data pengukuran, tetapi tidak memiliki persamaan fungsi yang bisa langsung diturunkan.

**Intinya:** kita tidak harus mengetahui persamaan fungsi terlebih dahulu. Kita dapat menggunakan perubahan nilai pada data untuk memperkirakan turunannya.

Sumber: Imron dkk. (2022) & Materi FungsionalSlide 3 dari 39

Diferensiasi numerik membantu kita memperkirakan seberapa cepat suatu nilai berubah ketika data yang tersedia hanya berupa hasil pengukuran. Contohnya pada kecepatan dari posisi, percepatan dari kecepatan, atau gradien suhu. Kita tidak harus mengetahui persamaan fungsinya terlebih dahulu.


6 · Pengantar Fungsional

## Mengenal Data dan Titik yang Digunakan

Bayangkan kita mengukur posisi benda setiap satu detik. Untuk memperkirakan kecepatannya pada detik kedua, kita perlu melihat data di sekitar waktu tersebut.

| Waktu $t$ (detik) | Posisi $s(t)$ (meter) |
|---:|---:|
| 1 | 1 |
| 2 | 8 |
| 3 | 27 |

### Memahami Notasi Titik & Langkah
- $x$ adalah titik yang ingin dianalisis. Misalnya $x=2$.
- $h$ adalah jarak antarwaktu pengukuran. Di sini $h=1$ detik.
- $x-h$ adalah titik sebelum titik yang dianalisis. Di sini $1$ detik.
- $x+h$ adalah titik setelah titik yang dianalisis. Di sini $3$ detik.
- $f(x)$ adalah nilai data pada titik yang sedang dianalisis ($s(2) = 8$ meter).

**Cara membacanya:** jika $x=2$, maka $f(x)$ adalah posisi pada detik kedua, yaitu 8 meter. Tiga metode berikut berbeda terutama pada **data tetangga mana yang dipakai**.

Sumber: Imron dkk. (2022) & Materi FungsionalSlide 4 dari 39

Bayangkan kita mengukur posisi benda setiap 1 detik. Untuk mencari kecepatan di detik ke-2, kita perlu melihat data di sekitarnya. Titik yang dianalisis disebut x, jarak pengukuran disebut h, titik sebelumnya x-h, dan sesudahnya x+h.


6.1 · Pendekatan Deret

## Selisih Maju: Menggunakan Data Setelah Titik yang Diamati

Selisih maju (*forward difference*) digunakan untuk memperkirakan laju perubahan pada suatu titik dengan membandingkan nilai di titik tersebut dan nilai pada titik setelahnya.

\[f'(x)\approx\frac{f(x+h)-f(x)}{h}\]

### Cara Memahami Rumus
- $f'(x)$: laju perubahan yang ingin diperkirakan pada titik $x$.
- $f(x+h)$: nilai data satu langkah setelah titik yang diamati.
- $f(x)$: nilai data pada titik yang diamati.
- $h$: jarak antara kedua pengukuran.
- Pembilang $f(x+h)-f(x)$: perubahan nilai dari titik sekarang ke titik berikutnya.

### Contoh Perhitungan ($x=2, h=1$)
Posisi pada detik ke-2 = 8 m, detik ke-3 = 27 m:
\[v(2)\approx\frac{27-8}{1}=19\text{ m/s}\]

**Kapan cocok digunakan?** Ketika data setelah titik yang ingin dianalisis tersedia. Metode ini juga praktis untuk titik paling awal dalam tabel karena belum ada data sebelumnya. Orde galat $O(h)$.

Sumber: Imron dkk. (2022) & Materi FungsionalSlide 5 dari 39

Selisih maju memperkirakan turunan dengan membandingkan nilai titik sekarang dengan titik berikutnya. Pada contoh detik ke-2, kita pakai posisi detik ke-3 (27) dikurangi detik ke-2 (8) dibagi 1, menghasilkan 19 m/s. Sangat praktis untuk titik awal tabel.


6.1 · Pendekatan Deret

## Selisih Mundur: Menggunakan Data Sebelum Titik yang Diamati

Selisih mundur (*backward difference*) memperkirakan laju perubahan dengan membandingkan nilai pada titik yang diamati dan nilai pada titik sebelumnya.

\[f'(x)\approx\frac{f(x)-f(x-h)}{h}\]

### Cara Memahami Rumus
- $f'(x)$: laju perubahan yang ingin diperkirakan pada titik $x$.
- $f(x)$: nilai data pada titik yang diamati.
- $f(x-h)$: nilai data satu langkah sebelum titik tersebut.
- $h$: jarak antara kedua pengukuran.
- Pembilang $f(x)-f(x-h)$: perubahan nilai dari titik sebelumnya ke titik sekarang.

### Contoh Perhitungan ($x=2, h=1$)
Posisi pada detik ke-2 = 8 m, detik ke-1 = 1 m:
\[v(2)\approx\frac{8-1}{1}=7\text{ m/s}\]

**Kapan cocok digunakan?** Ketika data sebelum titik yang ingin dianalisis tersedia. Metode ini praktis untuk titik paling akhir dalam tabel karena belum ada data setelahnya. Orde galat $O(h)$.

Sumber: Imron dkk. (2022) & Materi FungsionalSlide 6 dari 39

Selisih mundur membandingkan nilai saat ini dengan nilai sebelumnya. Pada detik ke-2, kita kurangkan posisi detik ke-2 (8) dengan detik ke-1 (1) dibagi 1, menghasilkan 7 m/s. Cocok untuk titik paling akhir dalam tabel.


6.1 · Pendekatan Deret

## Selisih Tengah: Menggunakan Data Sebelum dan Sesudah

Selisih tengah (*central difference*) menggunakan dua data sekaligus: satu titik sebelum dan satu titik sesudah titik yang ingin dianalisis.

\[f'(x)\approx\frac{f(x+h)-f(x-h)}{2h}\]

### Cara Memahami Rumus
- $f'(x)$: laju perubahan yang ingin diperkirakan pada titik tengah $x$.
- $f(x+h)$: nilai data satu langkah setelah titik yang diamati.
- $f(x-h)$: nilai data satu langkah sebelum titik yang diamati.
- $2h$: jarak dari titik sebelum ke titik sesudah ($h + h = 2h$).
- Pembilang $f(x+h)-f(x-h)$: perubahan nilai antara dua titik yang mengapit titik evaluasi.

### Contoh Perhitungan ($x=2, h=1$)
Posisi detik ke-3 = 27 m, detik ke-1 = 1 m:
\[v(2)\approx\frac{27-1}{2(1)}=\frac{26}{2}=13\text{ m/s}\]

**Kapan cocok digunakan?** Ketika data tersedia di kedua sisi titik yang ingin dianalisis. Metode ini memberikan perkiraan lebih baik untuk titik di bagian tengah tabel dengan orde galat kuadratik $O(h^2)$.

Sumber: Imron dkk. (2022) & Materi FungsionalSlide 7 dari 39

Selisih tengah menggunakan titik di kiri dan kanan titik yang diamati. Jarak keduanya adalah 2h, sehingga penyebutnya 2h. Pada detik ke-2, (27 - 1)/2 = 13 m/s. Lebih teliti untuk titik di bagian tengah karena simetris.


6.1 · Pendekatan Deret

## Bagaimana Memilih Metode yang Tepat?

Pemilihan metode terutama bergantung pada ketersediaan data di sekitar titik yang ingin dianalisis.

| Situasi Data | Metode yang Digunakan | Alasan & Logika Penggunaan |
|---|---|---|
| Data setelah titik tersedia | Selisih maju | Membandingkan titik sekarang dengan titik berikutnya |
| Data sebelum titik tersedia | Selisih mundur | Membandingkan titik sekarang dengan titik sebelumnya |
| Data sebelum dan sesudah tersedia | Selisih tengah | Menggunakan informasi dari kedua sisi titik (simetris) |

### Ilustrasi Sederhana pada Waktu $t = 1, 2, 3$
- Jika ingin menghitung pada waktu 1, data sebelumnya tidak tersedia $\rightarrow$ **Selisih maju** dapat digunakan.
- Jika ingin menghitung pada waktu 3, data sesudahnya tidak tersedia $\rightarrow$ **Selisih mundur** dapat digunakan.
- Jika ingin menghitung pada waktu 2, data waktu 1 dan 3 tersedia $\rightarrow$ **Selisih tengah** dapat digunakan.

**Hal penting:** jangan memilih metode hanya karena rumusnya terlihat lebih mudah. Periksa dahulu data mana yang tersedia.

Sumber: Imron dkk. (2022) & Materi FungsionalSlide 8 dari 39

Pemilihan metode bergantung pada data yang tersedia di sekitar titik evaluasi. Jangan pilih rumus hanya karena terlihat mudah. Cek posisinya: di awal gunakan maju, di akhir gunakan mundur, di tengah gunakan selisih tengah.


6.1 · Pendekatan Deret

## Apa Perbedaan Ketelitian Ketiga Metode?

Ketiga metode sama-sama menghasilkan perkiraan turunan, tetapi tingkat galat pemotongannya berbeda.

| Metode | Orde Galat Pemotongan | Makna Sederhana | Pengaruh jika $h$ Dibagi 2 |
|---|---|---|---|
| Selisih maju | $O(h)$ | Galat dominan sebanding dengan ukuran langkah | Galat berkurang $\approx 2\times$ |
| Selisih mundur | $O(h)$ | Galat dominan sebanding dengan ukuran langkah | Galat berkurang $\approx 2\times$ |
| Selisih tengah | $O(h^2)$ ⭐ | Galat dominan sebanding dengan kuadrat ukuran langkah | Galat berkurang $\approx 4\times$! ⭐ |

### Apa Artinya dalam Praktik?
Jika ukuran langkah $h$ diperkecil menjadi setengah:
- Pada selisih maju dan mundur, galat pemotongan secara teori kira-kira menjadi setengah.
- Pada selisih tengah, galat pemotongan secara teori kira-kira menjadi seperempat.

Ini berlaku dengan asumsi fungsi cukup mulus dan galat pembulatan belum mendominasi.

**Kesimpulan praktis:** selisih tengah memiliki keunggulan ketelitian teoritis, tetapi membutuhkan data pada kedua sisi titik evaluasi. Selisih maju dan mundur tetap berguna ketika data hanya tersedia pada satu sisi.

Sumber: Imron dkk. (2022) & Materi FungsionalSlide 9 dari 39

Ketiga metode sama-sama menghasilkan pendekatan, tetapi laju penurunan galatnya berbeda. Selisih maju dan mundur berorde O(h), jika h dibagi dua galat turun separuhnya. Selisih tengah berorde O(h^2), jika h dibagi dua galat turun empat kali lipat.


6.1 · Pendekatan Deret

## Studi Kasus: Menghitung Kecepatan dari Data Posisi

Gunakan kembali data posisi benda:
- $s(1) = 1$ meter
- $s(2) = 8$ meter (titik evaluasi $t=2$)
- $s(3) = 27$ meter
- $h = 1$ detik

### 1. Selisih Maju (data waktu 2 dan 3)
\[v(2)\approx\frac{s(3)-s(2)}{h}=\frac{27-8}{1}=19\text{ m/s}\]

### 2. Selisih Mundur (data waktu 1 dan 2)
\[v(2)\approx\frac{s(2)-s(1)}{h}=\frac{8-1}{1}=7\text{ m/s}\]

### 3. Selisih Tengah (data waktu 1 dan 3)
\[v(2)\approx\frac{s(3)-s(1)}{2h}=\frac{27-1}{2}=13\text{ m/s}\]

Ketiga hasil berbeda (19, 7, 13 m/s) karena setiap metode menggunakan pasangan titik observasi yang berbeda.

Sumber: Imron dkk. (2022) & Materi FungsionalSlide 10 dari 39

Kita bandingkan ketiga metode langsung pada data posisi yang sama di t=2. Selisih maju menghasilkan 19 m/s, selisih mundur menghasilkan 7 m/s, dan selisih tengah menghasilkan 13 m/s. Ketiganya berbeda karena memakai pasangan data yang berbeda.


6.1 · Pendekatan Deret

## Membaca dan Menafsirkan Hasil

Hasil perhitungan studi kasus:

| Metode | Perkiraan Kecepatan | Rentang Data yang Dipakai |
|---|---:|---|
| Selisih maju | 19 m/s | Detik ke-2 menuju detik ke-3 |
| Selisih mundur | 7 m/s | Detik ke-1 menuju detik ke-2 |
| Selisih tengah | 13 m/s | Detik ke-1 menuju detik ke-3 (rentang 2s) |

### Apa yang Dapat Kita Pahami?
- Selisih maju melihat perubahan posisi dari detik ke-2 menuju detik ke-3.
- Selisih mundur melihat perubahan posisi dari detik ke-1 menuju detik ke-2.
- Selisih tengah melihat perubahan posisi dari detik ke-1 menuju detik ke-3, lalu membaginya dengan total selang waktu 2 detik.

Jadi, perbedaan hasil **bukan karena salah hitung**. Setiap metode menggunakan rentang data yang berbeda untuk memperkirakan laju perubahan di detik kedua.

**Pesan utama:** hasil diferensiasi numerik merupakan perkiraan. Kita perlu memahami data yang dipakai sebelum menafsirkan hasilnya.

Sumber: Imron dkk. (2022) & Materi FungsionalSlide 11 dari 39

Perbedaan hasil bukan karena salah hitung. Benda ini dipercepat, sehingga wajar kecepatan interval awal (7 m/s) lebih lambat dibanding interval berikutnya (19 m/s). Selisih tengah merata-ratakannya menjadi 13 m/s.


6.1 · Pendekatan Deret

## Memeriksa Galat dan Menarik Kesimpulan

Untuk contoh ini, fungsi posisi yang menghasilkan data tersebut adalah $s(t) = t^3$.
Kecepatan eksak dapat dihitung secara analitik:
\[s'(t) = 3t^2 \implies s'(2) = 3(2)^2 = 12\text{ m/s}\]

Galat absolut: $E = |\text{hasil perkiraan} - \text{nilai eksak}|$

| Metode | Hasil Perkiraan | Nilai Eksak | Galat Absolut |
|---|---:|---:|---:|
| Maju | 19 m/s | 12 m/s | 7 m/s |
| Mundur | 7 m/s | 12 m/s | 5 m/s |
| Tengah | 13 m/s | 12 m/s | 1 m/s ⭐ |

### Ringkasan yang Perlu Diingat
- **Maju:** gunakan data sekarang dan sesudahnya.
- **Mundur:** gunakan data sebelumnya dan sekarang.
- **Tengah:** gunakan data sebelum dan sesudah titik yang dianalisis.
- **Pilih metode:** sesuaikan dengan posisi titik dan data yang tersedia.
- **Periksa hasil:** jika nilai eksak diketahui, hitung galat untuk menilai kedekatan hasil pendekatan.

Sumber: Imron dkk. (2022) & Materi FungsionalSlide 12 dari 39

Karena data dibuat dari fungsi s(t) = t^3, kita tahu nilai eksaknya adalah 12 m/s. Galat selisih maju 7, mundur 5, dan tengah hanya 1. Selisih tengah terbukti paling teliti, namun tetap perhatikan ketersediaan data di lapangan.

6.1 · Rumus Titik Data

# Konsep Dasar Turunan dari Data Tabel

Sering kali kita hanya memiliki tabel nilai $x$ dan $f(x)$ diskrit. Turunan di titik $x_0$ diperkirakan dari beberapa nilai $f$ yang berjarak sama, yaitu $h$.

| 1,8 | 1,9 | 2,0 | 2,1 | 2,2 |
| :---: | :---: | :---: | :---: | :---: |
| $x_0 - 2h$ | $x_0 - h$ | $x_0$ | $x_0 + h$ | $x_0 + 2h$ |

Contoh: $x_0 = 2{,}0$ dan $h = 0{,}1$.

### Klasifikasi Berdasarkan Dua Aspek Utama:

- **Berdasarkan Jumlah Titik:**
  - **Tiga Titik:** Memakai 3 posisi data untuk memperkirakan turunan ($O(h^2)$).
  - **Lima Titik:** Memakai 5 posisi data. Pendekatan jauh lebih teliti ($O(h^4)$), namun membutuhkan data lebih banyak.
- **Berdasarkan Posisi Titik:**
  - **Akhir (Endpoint):** Dipakai bila $x_0$ di ujung data tabel (hanya data satu sisi yang tersedia).
  - **Tengah (Midpoint):** Dipakai bila ada data di kiri dan kanan $x_0$ secara simetris.

Sumber: Imron dkk. (2022) | Slide 13 dari 39

Pengantar. Tekankan dua pembeda: jumlah titik (3 atau 5) dan posisi titik (akhir atau tengah). Lima titik butuh lebih banyak data tetapi lebih teliti. Analisis galat dibahas anggota lain.

6.1 · Rumus Titik Data

## Rumus Tiga Titik: Akhir & Tengah

### A. Tiga Titik Akhir
Digunakan bila $x_0$ berada di ujung data (satu sisi):

$$f'(x_0) pprox \frac{1}{2h}\left[-3f(x_0) + 4f(x_0+h) - f(x_0+2h)\right]$$

$$\text{Galat} = \frac{h^2}{3} f^{(3)}(\xi_0), \quad \xi_0 \in (x_0, x_0+2h)$$

| $-3$ | $+4$ | $-1$ |
| :---: | :---: | :---: |
| $x_0$ | $x_0+h$ | $x_0+2h$ |

$\times \frac{1}{2h}$ · dipakai di ujung data (satu sisi) · orde galat $O(h^2)$

### B. Tiga Titik Tengah
Digunakan bila ada data di kiri dan kanan $x_0$ secara simetris:

$$f'(x_0) pprox \frac{1}{2h}\left[f(x_0+h) - f(x_0-h)\right]$$

$$\text{Galat} = -\frac{h^2}{6} f^{(3)}(\xi_1), \quad \xi_1 \in (x_0-h, x_0+h)$$

| $-1$ | $0$ | $+1$ |
| :---: | :---: | :---: |
| $x_0-h$ | $x_0$ | $x_0+h$ |

$\times \frac{1}{2h}$ · dipakai di dalam data (kiri–kanan) · orde galat $O(h^2)$

*Catatan Penting:* Tetap tiga posisi titik. Koefisien $f(x_0) = 0$, jadi nilainya tidak muncul dalam perhitungan.

Sumber: Imron dkk. (2022), hlm. 189 | Slide 14 dari 39

Rumus tiga titik tengah memakai tiga POSISI data: x₀−h, x₀, x₀+h. Koefisien f(x₀) adalah 0, sehingga hanya f(x₀+h) dan f(x₀−h) yang muncul di rumus. Itulah alasan disebut tiga titik walaupun hanya dua nilai fungsi yang dihitung. Rumus akhir dengan h negatif menjadi versi mundur dari ujung kanan data.

6.1 · Rumus Titik Data

## Rumus Lima Titik: Akhir & Tengah

### A. Lima Titik Akhir
Dipakai di ujung data tabel dengan 4 data ke depan:

$$f'(x_0) pprox \frac{1}{12h}\left[-25f(x_0) + 48f(x_0+h) - 36f(x_0+2h) + 16f(x_0+3h) - 3f(x_0+4h)\right]$$

$$\text{Galat} = \frac{h^4}{5} f^{(5)}(\xi), \quad \xi \in (x_0, x_0+4h)$$

| $-25$ | $+48$ | $-36$ | $+16$ | $-3$ |
| :---: | :---: | :---: | :---: | :---: |
| $x_0$ | $x_0+h$ | $x_0+2h$ | $x_0+3h$ | $x_0+4h$ |

$\times \frac{1}{12h}$ · dipakai di ujung data · orde galat $O(h^4)$

### B. Lima Titik Tengah
Dipakai di bagian dalam data secara simetris:

$$f'(x_0) pprox \frac{1}{12h}\left[f(x_0-2h) - 8f(x_0-h) + 8f(x_0+h) - f(x_0+2h)\right]$$

$$\text{Galat} = \frac{h^4}{30} f^{(5)}(\xi), \quad \xi \in (x_0-2h, x_0+2h)$$

| $+1$ | $-8$ | $0$ | $+8$ | $-1$ |
| :---: | :---: | :---: | :---: | :---: |
| $x_0-2h$ | $x_0-h$ | $x_0$ | $x_0+h$ | $x_0+2h$ |

$\times \frac{1}{12h}$ · dipakai di dalam data · orde galat $O(h^4)$

Sumber: Imron dkk. (2022), hlm. 189 | Slide 15 dari 39

Memakai polinomial Lagrange melalui lima titik sehingga galat turun ke orde h⁴. Lima titik akhir: x₀ sampai x₀+4h. Lima titik tengah: x₀−2h sampai x₀+2h, f(x₀) berkoefisien 0.

6.1 · Rumus Titik Data

## Perbandingan: Tiga Titik vs Lima Titik

| Aspek | Rumus Tiga Titik | Rumus Lima Titik |
| :--- | :--- | :--- |
| **Orde Galat** | $O(h^2)$ | $O(h^4)$ |
| **Kebutuhan Titik Data** | 3 posisi data (hemat data) | 5 posisi data (butuh data lebih banyak) |
| **Jumlah Evaluasi Fungsi** | 2 atau 3 nilai fungsi | 4 atau 5 nilai fungsi |
| **Tingkat Ketelitian** | Cukup teliti | Sangat teliti untuk $h$ kecil |

### 📌 Contoh Perbandingan pada $f(x) = x e^x$ (Tengah, $x_0 = 2{,}0, h = 0{,}1$):
- **Tiga Titik Tengah:** Galat $\approx 6{,}16 \times 10^{-2}$
- **Lima Titik Tengah:** Galat $\approx 1{,}69 \times 10^{-4}$
- **Kesimpulan:** Lima titik jauh lebih teliti (galat mengecil ratusan kali lipat), tetapi membutuhkan ketersediaan data yang lebih banyak.

Sumber: Analisis Komparasi Orde Galat | Slide 16 dari 39

Gambar memakai contoh tengah x₀ = 2.0, h = 0.1. Pada tiga titik hanya 2 nilai fungsi dihitung (1.9 dan 2.1), pada lima titik 4 nilai (1.8, 1.9, 2.1, 2.2). Orde galat O(h²) dan O(h⁴) cukup disebut sekilas; analisis galat dibahas anggota lain.

6.1 · Rumus Titik Data

## Panduan Memilih Rumus

| Rumus | Posisi Titik yang Dipakai | Ketersediaan Data | Dipakai Bila |
| :--- | :--- | :--- | :--- |
| **Tiga Titik Akhir** | $x_0, x_0+h, x_0+2h$ | Satu sisi | Titik di ujung batas data ($O(h^2)$) |
| **Tiga Titik Tengah** | $x_0-h, x_0, x_0+h$ ($f(x_0)$ koef. 0) | Simetris kiri & kanan | Ada data kiri dan kanan ($O(h^2)$) |
| **Lima Titik Akhir** | $x_0$ sampai $x_0+4h$ | Satu sisi | Ujung data & 4 data tersedia ($O(h^4)$) |
| **Lima Titik Tengah** | $x_0-2h$ sampai $x_0+2h$ ($f(x_0)$ koef. 0) | Simetris kiri & kanan | Ada 2 data kiri & 2 kanan ($O(h^4)$) |

### 💡 Catatan Pemakaian:
- Pilih rumus berdasarkan posisi titik yang dicari: ujung data memakai rumus akhir, di dalam data memakai rumus tengah.
- Untuk titik di ujung kanan tabel (mis. $f'(1{,}5)$), data hanya ada di sebelah kiri, maka rumus akhir dipakai dengan **$h$ bernilai negatif** (mis. memakai $1{,}5; 1{,}4; 1{,}3$ untuk tiga titik).

Sumber: Imron dkk. (2022) | Slide 17 dari 39

Pilih rumus berdasarkan posisi titik yang dicari: ujung data memakai rumus akhir, di dalam data memakai rumus tengah. Untuk f′(1.5) data hanya ada di kiri, maka rumus akhir dipakai dengan h negatif (memakai 1.5, 1.4, 1.3 untuk tiga titik).

6.1 · Rumus Titik Data

## Cara Menghitung: Prosedur 4 Langkah

1. **Tentukan $x_0$ dan $h$**
   Titik yang dicari turunannya adalah $x_0$. $h$ adalah jarak seragam antar-data ($h = x_{i+1} - x_i$).
2. **Pilih Rumus yang Sesuai**
   Data satu sisi: gunakan rumus **akhir**. Data mengapit simetris: gunakan rumus **tengah**. Lalu tentukan tiga atau lima titik.
3. **Substitusi Nilai Fungsi**
   Ambil nilai $f(x)$ dari tabel sesuai posisi titik, kalikan dengan masing-masing koefisien bobotnya.
4. **Hitung dan Lakukan Pembagian**
   Jumlahkan seluruh hasil kali, lalu bagi dengan $2h$ (untuk tiga titik) atau $12h$ (untuk lima titik).

> [!NOTE]
> **$h = \text{jarak antar-data}$**: Contoh: $h = 2{,}1 - 2{,}0 = 0{,}1$. Bukan nilai fungsi dan bukan hasil turunan.  
> **$h$ boleh bernilai negatif**: Rumus akhir dengan $h = -0{,}1$ memakai titik di sebelah kiri $x_0$ (dari ujung kanan data mundur ke kiri).

Sumber: Pedoman Prosedur Numerik | Slide 18 dari 39

Empat langkah yang sama untuk keempat rumus. h adalah jarak antar-data, bukan nilai fungsi dan bukan hasil turunan. h negatif dipakai saat rumus akhir diterapkan dari ujung kanan data.

6.1 · Rumus Titik Data

## Soal 1: Tiga Titik Akhir

| $x$ | 1,8 | 1,9 | 2,0 | 2,1 | 2,2 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | 10,889365 | 12,703199 | 14,778112 | 17,148957 | 19,855030 |

*Fungsi:* $f(x) = x e^x$ · *Nilai Eksak:* $f'(2{,}0) = 3e^2 \approx 22{,}167168$ (pembanding galat)

### 📝 Soal:
Diberikan tabel nilai $f(x) = x e^x$ di atas. Hitunglah hampiran turunan $f'(2{,}0)$ dengan **rumus tiga titik akhir** ($x_0 = 2{,}0, h = 0{,}1$), lalu tentukan galatnya terhadap nilai eksak!

### 🎯 Instruksi Pengerjaan (Langkah 1 s.d. 4):
1. Substitusikan $f(2{,}0), f(2{,}1), f(2{,}2)$ dari tabel ke rumus: $\frac{1}{2h}[-3f(x_0) + 4f(x_0+h) - f(x_0+2h)]$.
2. Kalikan setiap nilai $f$ dengan koefisiennya: $-3, 4,$ dan $-1$.
3. Jumlahkan ketiga hasil kali, lalu bagi dengan $2h = 0{,}2$.
4. Hitung $\text{galat} = \text{eksak} - \text{hampiran}$. Tulis hasil dengan 6 desimal dan galat dalam notasi $a \times 10^b$.

Sumber: Latihan Soal Terbimbing | Slide 19 dari 39

Soal 1. Pastikan siswa membaca dulu: rumus apa (tiga titik akhir), x₀ berapa, h berapa. Empat instruksi di slide ini sama urutannya dengan empat langkah di slide penyelesaian. Beri waktu sekitar 3 menit sebelum membuka slide berikutnya.

6.1 · Rumus Titik Data

## Penyelesaian 1: Tiga Titik Akhir

| $x$ | 1,8 | 1,9 | 2,0 | 2,1 | 2,2 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | 10,889365 | 12,703199 | 14,778112 | 17,148957 | 19,855030 |

$f(x) = x e^x$ · Nilai eksak $f'(2{,}0) = 3e^2 = 22{,}167168$

**Tiga Titik Akhir · $x_0 = 2{,}0, h = 0{,}1$**  
$$f'(2{,}0) \approx \frac{-3f(2{,}0) + 4f(2{,}1) - f(2{,}2)}{2(0{,}1)}$$

1. **Masukkan nilai tabel:**
   $$= \frac{-3(14{,}778112) + 4(17{,}148957) - 19{,}855030}{0{,}2}$$
2. **Kalikan setiap nilai:**
   $$= \frac{-44{,}334336 + 68{,}595828 - 19{,}855030}{0{,}2}$$
3. **Jumlahkan, lalu bagi:**
   $$= \frac{4{,}406462}{0{,}2} = \mathbf{22{,}032310}$$
4. **Bandingkan dengan eksak:**
   $$\text{Galat} = 22{,}167168 - 22{,}032310 = \mathbf{1{,}35 \times 10^{-1}}$$

Sumber: Imron dkk. (2022), hlm. 190 | Slide 20 dari 39

Dengan h = −0.1 hasilnya 22.054525, galat 1.13×10⁻¹. Langkah sama: masukkan nilai, kalikan, jumlahkan, bagi 2h.

6.1 · Rumus Titik Data

## Soal 2: Tiga Titik Tengah

| $x$ | 1,8 | 1,9 | 2,0 | 2,1 | 2,2 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | 10,889365 | 12,703199 | 14,778112 | 17,148957 | 19,855030 |

$f(x) = x e^x$ · Nilai eksak $f'(2{,}0) = 3e^2 = 22{,}167168$

### 📝 Soal:
Dengan tabel yang sama, hitunglah hampiran $f'(2{,}0)$ memakai **rumus tiga titik tengah** ($x_0 = 2{,}0, h = 0{,}1$), lalu tentukan galatnya. Bandingkan dengan galat tiga titik akhir pada Soal 1!

### 🎯 Instruksi Pengerjaan (Langkah 1 s.d. 4):
1. Substitusikan $f(2{,}1)$ dan $f(1{,}9)$ dari tabel ke rumus: $\frac{1}{2h}[f(x_0+h) - f(x_0-h)]$.
2. Kurangkan $f(2{,}1) - f(1{,}9)$. *Nilai $f(2{,}0)$ tidak dipakai karena koefisiennya 0.*
3. Bagi hasil pengurangan dengan $2h = 0{,}2$.
4. Hitung $\text{galat} = \text{eksak} - \text{hampiran}$. Bandingkan dengan galat Soal 1 ($1{,}35 \times 10^{-1}$): mana yang lebih kecil?

Sumber: Latihan Soal Terbimbing | Slide 21 dari 39

Soal 2. Pertanyaan pancingan: mengapa f(2.0) tidak muncul padahal x₀ = 2.0? Jawaban: koefisiennya 0. Minta siswa membandingkan galat dengan Soal 1 sebelum melihat penyelesaian.

6.1 · Rumus Titik Data

## Penyelesaian 2: Tiga Titik Tengah

| $x$ | 1,8 | 1,9 | 2,0 | 2,1 | 2,2 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | 10,889365 | 12,703199 | 14,778112 | 17,148957 | 19,855030 |

$f(x) = x e^x$ · Nilai eksak $f'(2{,}0) = 3e^2 = 22{,}167168$

**Tiga Titik Tengah · $x_0 = 2{,}0, h = 0{,}1$**  
$$f'(2{,}0) \approx \frac{f(2{,}1) - f(1{,}9)}{2(0{,}1)}$$

1. **Masukkan nilai tabel:**
   $$= \frac{17{,}148957 - 12{,}703199}{0{,}2}$$
2. **Kurangkan:**
   $$= \frac{4{,}445758}{0{,}2}$$
3. **Bagi dengan $2h$:**
   $$= \mathbf{22{,}228790}$$
4. **Bandingkan dengan eksak:**
   $$\text{Galat} = 22{,}167168 - 22{,}228790 = \mathbf{-6{,}16 \times 10^{-2}}$$  
   *(Lebih kecil dari tiga titik akhir: $1{,}35 \times 10^{-1}$)*

Sumber: Imron dkk. (2022), hlm. 190 | Slide 22 dari 39

Dengan h = 0.2 hasilnya 22.414163, galat −2.47×10⁻¹. Galat naik sekitar 4 kali saat h dua kali lebih besar (sesuai orde h²). f(2.0) tidak dipakai karena koefisiennya 0.

6.1 · Rumus Titik Data

## Soal 3: Lima Titik Akhir

| $x$ | 1,8 | 1,9 | 2,0 | 2,1 | 2,2 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | 10,889365 | 12,703199 | 14,778112 | 17,148957 | 19,855030 |

$f(x) = x e^x$ · Nilai eksak $f'(1{,}8) = 2{,}8 e^{1{,}8} \approx 16{,}939013$ (pembanding galat)

### 📝 Soal:
Hitunglah hampiran $f'(1{,}8)$ dengan **rumus lima titik akhir** ($x_0 = 1{,}8, h = 0{,}1$), lalu tentukan galatnya!  
*Diskusi:* Jelaskan mengapa $x_0 = 2{,}0$ tidak dapat dipakai pada rumus lima titik akhir ini.

### 🎯 Instruksi Pengerjaan (Langkah 1 s.d. 4):
1. Periksa data: rumus butuh $x_0$ sampai $x_0+4h = 1{,}8$ sampai $2{,}2$. Substitusikan kelima nilai $f$ dari tabel.
2. Kalikan setiap nilai $f$ dengan koefisiennya: $-25, 48, -36, 16,$ dan $-3$.
3. Jumlahkan kelima hasil kali, lalu bagi dengan $12h = 1{,}2$.
4. Hitung $\text{galat} = \text{eksak} - \text{hampiran}$. Bandingkan dengan galat tiga titik akhir di $x_0 = 1{,}8$ ($1{,}06 \times 10^{-1}$).

Sumber: Latihan Soal Terbimbing | Slide 23 dari 39

Soal 3. Jawaban pertanyaan "mengapa bukan 2.0": rumus lima titik akhir membutuhkan x₀ sampai x₀+4h, yaitu 2.0 sampai 2.4, sedangkan tabel hanya sampai 2.2. Hanya x₀ = 1.8 yang punya empat data di kanannya.

6.1 · Rumus Titik Data

## Penyelesaian 3: Lima Titik Akhir

| $x$ | 1,8 | 1,9 | 2,0 | 2,1 | 2,2 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | 10,889365 | 12,703199 | 14,778112 | 17,148957 | 19,855030 |

$f(x) = x e^x$ · Nilai eksak $f'(1{,}8) = 2{,}8 e^{1{,}8} = 16{,}939013$

**Lima Titik Akhir · $x_0 = 1{,}8, h = 0{,}1$**  
$$f'(1{,}8) \approx \frac{-25f(1{,}8) + 48f(1{,}9) - 36f(2{,}0) + 16f(2{,}1) - 3f(2{,}2)}{12(0{,}1)}$$

1. **Masukkan nilai tabel:**
   $$= \frac{-25(10{,}889365) + 48(12{,}703199) - 36(14{,}778112) + 16(17{,}148957) - 3(19{,}855030)}{1{,}2}$$
2. **Kalikan setiap nilai:**
   $$= \frac{-272{,}234125 + 609{,}753552 - 532{,}012032 + 274{,}383312 - 59{,}565090}{1{,}2}$$
3. **Jumlahkan, lalu bagi:**
   $$= \frac{20{,}325617}{1{,}2} = \mathbf{16{,}938014}$$
4. **Bandingkan dengan eksak:**
   $$\text{Galat} = 16{,}939013 - 16{,}938014 = \mathbf{9{,}99 \times 10^{-4}}$$  
   *(Tiga titik akhir: $1{,}06 \times 10^{-1}$ — lima titik $\approx 106\times$ lebih teliti!)*

Sumber: Imron dkk. (2022) | Slide 24 dari 39

Contoh tambahan di x₀ = 1.8 karena x₀ = 2.0 tidak punya empat titik di kanannya. Rumus sama dengan Contoh 6.1.3 buku untuk f′(1.1).

6.1 · Rumus Titik Data

## Soal 4: Lima Titik Tengah

| $x$ | 1,8 | 1,9 | 2,0 | 2,1 | 2,2 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | 10,889365 | 12,703199 | 14,778112 | 17,148957 | 19,855030 |

$f(x) = x e^x$ · Nilai eksak $f'(2{,}0) = 3e^2 = 22{,}167168$

### 📝 Soal:
Hitunglah hampiran $f'(2{,}0)$ dengan **rumus lima titik tengah** ($x_0 = 2{,}0, h = 0{,}1$), lalu tentukan galatnya! Bandingkan dengan galat tiga titik tengah pada Soal 2.

### 🎯 Instruksi Pengerjaan (Langkah 1 s.d. 4):
1. Substitusikan $f(1{,}8), f(1{,}9), f(2{,}1), f(2{,}2)$ dari tabel. *Data tersedia 2 di kiri dan 2 di kanan $x_0$.*
2. Kalikan setiap nilai $f$ dengan koefisiennya: $1, -8, 8,$ dan $-1$. Nilai $f(2{,}0)$ tidak dipakai (koefisien 0).
3. Jumlahkan keempat hasil kali, lalu bagi dengan $12h = 1{,}2$.
4. Hitung $\text{galat} = \text{eksak} - \text{hampiran}$. Bandingkan dengan galat Soal 2 ($-6{,}16 \times 10^{-2}$).

Sumber: Latihan Soal Terbimbing | Slide 25 dari 39

Soal 4. Tekankan kesimpulan: dengan data dan h yang sama, lima titik tengah memberi galat sekitar 10⁻⁴, sedangkan tiga titik tengah sekitar 10⁻².

6.1 · Rumus Titik Data

## Penyelesaian 4: Lima Titik Tengah

| $x$ | 1,8 | 1,9 | 2,0 | 2,1 | 2,2 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | 10,889365 | 12,703199 | 14,778112 | 17,148957 | 19,855030 |

$f(x) = x e^x$ · Nilai eksak $f'(2{,}0) = 3e^2 = 22{,}167168$

**Lima Titik Tengah · $x_0 = 2{,}0, h = 0{,}1$**  
$$f'(2{,}0) \approx \frac{f(1{,}8) - 8f(1{,}9) + 8f(2{,}1) - f(2{,}2)}{12(0{,}1)}$$

1. **Masukkan nilai tabel:**
   $$= \frac{10{,}889365 - 8(12{,}703199) + 8(17{,}148957) - 19{,}855030}{1{,}2}$$
2. **Kalikan setiap nilai:**
   $$= \frac{10{,}889365 - 101{,}625592 + 137{,}191656 - 19{,}855030}{1{,}2}$$
3. **Jumlahkan, lalu bagi:**
   $$= \frac{26{,}600399}{1{,}2} = \mathbf{22{,}166999}$$
4. **Bandingkan dengan eksak:**
   $$\text{Galat} = 22{,}167168 - 22{,}166999 = \mathbf{1{,}69 \times 10^{-4}}$$  
   *(Tiga titik tengah: $6{,}16 \times 10^{-2}$, lebih dari 360× lebih besar!)*

Sumber: Imron dkk. (2022), hlm. 190–191 | Slide 26 dari 39

Contoh 6.1.2 buku. Perbandingan: galat lima titik sekitar 10⁻⁴, tiga titik sekitar 10⁻².

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

Sumber: Imron dkk. (2022), hlm. 186–189Slide 27 dari 39

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

Tambahan: hitungan sendiri; konsep: Burden & Faires \[1\], catatan UMD \[2\]Slide 28 dari 39

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

Tambahan: definisi umum \[1\] §1.2; contoh dari data Contoh 6.1.1 (hitungan sendiri)Slide 29 dari 39

Slide ini melengkapi slide galat. E_a memberi besar kesalahan dalam satuan turunan. E_r membandingkannya dengan besar turunan, sehingga bisa dibandingkan antarfungsi. E\_% hanya E_r dikali 100. Contoh: pada Contoh 6.1.1, selisih maju dengan h = 0,1 memberi 0,5406722 sedangkan eksaknya 0,5555556, jadi E_a = 0,0148834; E_r = 0,0148834 / 0,5555556 ≈ 0,0267901; E\_% ≈ 2,679%. Bila turunan eksak nol atau mendekati nol, E_r tidak terdefinisi atau menjadi sangat besar; pakai E_a. Definisi galat absolut dan relatif adalah materi standar analisis numerik (mis. Burden & Faires §1.2). Contoh hitungan ini kami hitung sendiri dari angka buku.

Ekstrapolasi Richardson

## Metode Ekstrapolasi Richardson

### Pengertian

Menggabungkan **dua pendekatan** dengan ukuran langkah berbeda untuk membuang **suku galat utama**, sehingga hasilnya lebih teliti.

### Prinsip kerja

**1** Hitung pendekatan turunan dengan langkah h → D(h)

**2** Hitung pendekatan dengan langkah 2h → D(2h)

**3** Gabungkan keduanya untuk mengurangi galat utama

### Rumus umum

\(f'_0=D(h)+\dfrac{D(h)-D(2h)}{2^n-1}\)

- f′₀ : nilai turunan di x₀ setelah ekstrapolasi
- **D(h)** : hasil pendekatan turunan dengan ukuran langkah h yang **lebih kecil**
- **D(2h)** : hasil pendekatan turunan dengan ukuran langkah **dua kali lebih besar**
- n : orde galat awal, yaitu O(hⁿ)

Kedua hasil digabung untuk **menghilangkan suku galat utama**.

### Contoh: selisih tengah (n = 2)

\(f'_0=\dfrac{4D(h)-D(2h)}{3}\)

Orde galat naik: **O(h²) → O(h⁴)**

Kaitan notasi slide berikut: D(h) = N₁(h/2), D(2h) = N₁(h). Untuk n = 1 (selisih maju): 2D(h) − D(2h).

Sumber: Imron dkk. (2022), hlm. 196–199Slide 30 dari 39

Richardson tidak membuat rumus turunan baru dari data; ia menggabungkan dua hasil yang sudah ada. Hitung D(h) dan D(2h), lalu tambahkan koreksi [D(h) − D(2h)]/(2ⁿ − 1). Untuk selisih tengah galatnya O(h²), jadi n = 2 dan rumusnya (4D(h) − D(2h))/3 dengan orde O(h⁴). Untuk selisih maju n = 1. Di buku, langkah besar ditulis h dan langkah kecil h/2, jadi D(h) di slide ini sama dengan N₁(h/2) di buku. Pilih n sesuai bentuk galat pendekatan awal.

Contoh 6.2.1

## Contoh Richardson pada f(x) = ln x

**Diketahui:** f(x) = ln x, x₀ = 1,8\
N₁(0,1) = 0,5406722 · N₁(0,05) = 0,5479795\
Selisih maju: galat O(h), jadi n = 1

### Perhitungan

\(N_2(0{,}1)=2N_1(0{,}05)-N_1(0{,}1)\)

\(=2(0{,}5479795)-0{,}5406722\)

**= 0,5552868**

| Metode | Hasil | Galat absolut |
| --- | --- | --- |
| Selisih maju, h = 0,1 | 0,5406722 | 0,0148834 |
| Selisih maju, h = 0,05 | 0,5479795 | 0,0075761 |
| **Richardson** | **0,5552868** | **0,0002688** |
| Nilai eksak | 0,5555556 | — |

Galat (makin pendek makin baik)

h = 0,1 · 0,0148834

h = 0,05 · 0,0075761

Richardson · 0,0002688

**Kesimpulan:** Richardson mengurangi galat sekitar **28 kali** dibanding selisih maju dengan h = 0,05 (0,0075761 ÷ 0,0002688 ≈ 28).

Sumber: Imron dkk. (2022), hlm. 197–198Slide 31 dari 39

Galat awal selisih maju berorde h, jadi pakai rumus n = 1: dua kali hasil yang lebih teliti dikurangi hasil yang kurang teliti. Hitung: 2 × 0,5479795 = 1,0959590; dikurangi 0,5406722 menghasilkan 0,5552868. Galat tiap hasil dihitung dari nilai eksak 0,5555556. Buku menulis hasil 0,555287 dan galat 0,000258; hitung ulang dari angka buku memberi 0,0002688, dan kami memakai angka yang konsisten dengan digit di slide.

Contoh 6.1.2

## Perbandingan Metode Diferensiasi pada Data Tabel

**f(x) = xeˣ, x₀ = 2,0, h = 0,1**

| x | f(x) |
| --- | --- |
| 1,8 | 10,889365 |
| 1,9 | 12,703199 |
| 2,0 | 14,778112 |
| 2,1 | 17,148957 |
| 2,2 | 19,855030 |

| Metode | f′(2) | Galat absolut |
| --- | --- | --- |
| Tiga titik ujung | 22,032310 | 0,134858 |
| Tiga titik tengah | 22,228790 | 0,061622 |
| **Lima titik tengah** | **22,166999** | **0,000169** |
| Nilai eksak 3e² | 22,167168 | — |

**Kesimpulan:** di antara ketiga metode, **lima titik tengah** paling akurat.

**Kaitan dengan Richardson:** hasil pendekatan turunan dapat dipakai sebagai dasar (N₁) untuk meningkatkan ketelitian lewat ekstrapolasi (slide 34).

Sumber: Imron dkk. (2022), hlm. 190–191Slide 32 dari 39

Semua hasil dihitung dari lima nilai tabel, bukan dari rumus fungsi. Nilai eksak 3e² ≈ 22,167168 hanya dipakai sebagai pembanding. Galat absolut dihitung |eksak − pendekatan|: 0,134858; 0,061622; 0,000169. Lima titik tengah paling dekat karena galatnya O(h⁴), sedangkan dua rumus lain O(h²). Tiga titik tengah dengan h berbeda nantinya menjadi bahan Richardson pada slide 34.

Contoh 6.1.3

## Strategi Pemilihan Rumus Diferensiasi

| x | f(x) | Posisi titik |
| --- | --- | --- |
| 1,1 | 9,025013 | ujung kiri |
| 1,2 | 11,02318 | interior |
| 1,3 | 13,46374 | tengah penuh |
| 1,4 | 16,44465 | interior |
| 1,5 | 20,08554 | ujung kanan |

h = 0,1; di ujung kanan h dibuat negatif

| Titik | Rumus yang tersedia |
| --- | --- |
| 1,1 (ujung kiri) | Tiga titik ujung (6.4) · lima titik ujung (6.6) |
| 1,2 (interior) | Tiga titik ujung · tiga titik tengah (6.5) |
| 1,3 (tengah penuh) | 6.4 · 6.5 · lima titik tengah (6.7) |
| 1,4 (interior) | 6.4 (h negatif) · 6.5 |
| 1,5 (ujung kanan) | 6.4 · 6.6 (h negatif) |

Tiga titik ujung, x = 1,1:

\(\dfrac{-3(9{,}025013)+4(11{,}02318)-13{,}46374}{0{,}2}=17{,}76971\)

Lima titik tengah, x = 1,3:

\(\dfrac{9{,}025013-8(11{,}02318)+8(16{,}44465)-20{,}08554}{1{,}2}=26{,}92603\)

**Kesimpulan:** pilih rumus menurut posisi titik dan ketersediaan data. **Kaitan dengan Richardson:** ekstrapolasi membutuhkan data yang sesuai dengan ukuran langkah yang dipakai (h dan setengahnya).

Sumber: Imron dkk. (2022), hlm. 191–195Slide 33 dari 39

Lihat posisi titik dulu. Di ujung tidak ada data di salah satu sisi, jadi pakai rumus ujung. Di titik dalam bisa pakai rumus tengah, dan lima titik tengah hanya pada x = 1,3 karena butuh dua titik di tiap sisi. Hitungan memakai nilai tabel penuh; buku menampilkannya dibulatkan. Hubungan dengan Richardson: untuk membentuk N₁ dengan h dan h/2, data pada kedua ukuran langkah itu harus ada; ini akan terlihat jelas di slide 17.

Contoh 6.2.2

## Richardson Bertingkat pada f(x) = xeˣ

x = 2, nilai eksak f′(2) = 22,167168 · N₁: selisih tengah, galat pangkat genap

### Tahap 1 — N₁

N₁(0,2) = **22,414160**\
N₁(0,1) = **22,228786**\
N₁(0,05) = **22,182564**

Nilai N₁(0,05) dihitung menggunakan fungsi f(x) = xeˣ. Titik x = 1,95 dan x = 2,05 tidak tersedia pada tabel lima titik, sehingga perhitungan ini menggunakan fungsi yang diketahui, bukan hanya data tabel.

→

### Tahap 2 — N₂ (÷3)

N₂(0,2) = 22,228786 + (22,228786 − 22,414160)/3 = **22,166995**\
N₂(0,1) = 22,182564 + (22,182564 − 22,228786)/3 = **22,167157**

→

### Tahap 3 — N₃ (÷15)

N₃(0,2) = 22,167157 + (22,167157 − 22,166995)/15\
= **22,167168**

| Tingkat | N₁(0,2) | N₁(0,1) | N₁(0,05) | N₂(0,2) | N₂(0,1) | N₃(0,2) | Eksak |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Hasil | 22,414160 | 22,228786 | 22,182564 | 22,166995 | 22,167157 | **22,167168** | 22,167168 |
| Galat absolut | 0,246992 | 0,061618 | 0,015396 | 0,000173 | 0,000011 | 0,000000 | — |

**Kesimpulan:** Richardson bertingkat meningkatkan ketelitian secara bertahap: N₁ → N₂ → N₃ (N₃ sama dengan eksak pada enam desimal yang ditampilkan).

Sumber: Imron dkk. (2022), hlm. 200–201Slide 34 dari 39

Tiga tahap: (1) hitung N₁ dengan selisih tengah untuk h = 0,2; 0,1; 0,05; (2) gabungkan pasangan yang bertetangga dengan pembagi 3 → N₂(0,2) dan N₂(0,1); (3) gabungkan kedua N₂ dengan pembagi 15 → N₃(0,2). Angka dalam kurung adalah ukuran langkah. Ini angka buku; hitung ulang dari tabel Contoh 6.1.2 memberi N₁(0,2) = 22,414163 dan N₁(0,1) = 22,228790 (selisih kecil di digit ke-6). Rumus N₃ di buku tertulis memakai N₁(0,2), tetapi angkanya cocok dengan N₂(0,2). Galat N₃ nol hanya pada enam desimal yang ditampilkan, bukan bukti kesamaan matematis.

Contoh 6.2.3

## Richardson dengan Keterbatasan Data

| x | f(x) |
| --- | --- |
| 1,1 | 9,025013 |
| 1,2 | 11,02318 |
| 1,3 | 13,46374 |
| 1,4 | 16,44465 |
| 1,5 | 20,08554 |

x₀ = 1,3; h = 0,2

### Tahap 1 — N₁

\(N_1(0{,}2)=\frac{20{,}08554-9{,}025013}{0{,}4}=27{,}651318\)\
\(N_1(0{,}1)=\frac{16{,}44465-11{,}02318}{0{,}2}=27{,}107350\)

### Tahap 2 — N₂

\(N_2(0{,}2)=27{,}107350+\frac{27{,}107350-27{,}651318}{3}\)

\(=\mathbf{26{,}926027}\)

### Mengapa N₃ tidak dapat dihitung?

N₃ membutuhkan N₁(0,05) = [f(1,35) − f(1,25)]/0,1, sedangkan f(1,25) dan f(1,35) **tidak tersedia** pada tabel.

**Kesimpulan:** Richardson tidak dapat dilanjutkan ke tingkat berikutnya bila data yang diperlukan tidak tersedia.

Catatan: Hasil perhitungan menggunakan data tabel yang tersedia.

Sumber: Imron dkk. (2022), hlm. 201–202Slide 35 dari 39

Titik x₀ = 1,3 dengan h = 0,2 dan 0,1; N₁(0,2) memakai f(1,5) dan f(1,1), N₁(0,1) memakai f(1,4) dan f(1,2). Gabungkan dengan pembagi 3 untuk N₂(0,2). Tingkat ketiga butuh N₁(0,05) dengan f(1,35) dan f(1,25), yang tidak ada di tabel, sehingga berhenti di N₂. Catatan untuk penyaji (dicek pada halaman buku 201–202): buku mencetak N₁(0,1) = (1/0,2)(f(1,4) − f(1,1)) = 27,10735 dan N₂(0,2) = 26,920273. Dua hal ini tidak cocok dengan substitusi yang tercetak: (16,44465 − 11,02318)/0,2 memakai f(1,2) dan menghasilkan 27,10735, sedangkan dengan f(1,1) hasilnya lain; dan 27,10735 + (27,10735 − 27,651318)/3 = 26,926027, bukan 26,920273. Nilai 26,926027 juga sama dengan hasil lima titik tengah 26,92603 pada Contoh 6.1.3 butir 3(e). Penyebab pasti selisihnya tidak dapat dibuktikan dari buku; mungkin salah cetak, tetapi itu hanya dugaan. Slide menampilkan hasil hitung ulang 26,926027 (dari data tabel yang tersedia); angka 26,920273 adalah yang tercetak di buku.

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

Sumber: Imron dkk. (2022), Bab 6 (ringkasan)Slide 36 dari 39

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

Rumus dan orde: Imron dkk. (2022), hlm. 186–189; kolom kondisi: tambahan \[1\]Slide 37 dari 39

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

Sumber: Imron dkk. (2022), Bab 6 (ringkasan)Slide 38 dari 39

Rangkum perjalanan: dari definisi, dasar deret, rumus maju/mundur/tengah, rumus tiga dan lima titik, galat, lalu Richardson. Tekankan tiga hal: orde galat menentukan kecepatan perbaikan saat h mengecil, rumus harus cocok dengan posisi titik dan data yang ada, dan h tidak boleh terlalu kecil. Tutup dengan kalimat di bawah slide, lalu buka sesi tanya jawab.

Penutup

# TERIMA KASIH

**Sesi Tanya Jawab & Diskusi**  
*Diferensiasi Numerik & Ekstrapolasi Richardson*

Silakan ajukan pertanyaan atau tanggapan terkait materi yang telah dipaparkan.

**Tim Penyaji:**  
Farel Luther Siagian · Fatih Taqiyyuddin · Siti Zulayka Maulida Amali · Keegan Gibran Jehian  
**Dosen Pengampu:** Debi Yandra Niska, S.Kom., M.Kom. (2026)

Slide 39 dari 39

Ucapkan terima kasih kepada dosen pengampu dan rekan-rekan mahasiswa atas perhatian selama presentasi berlangsung. Buka kesempatan bagi audiens untuk sesi tanya jawab dan diskusi mengenai materi diferensiasi numerik.