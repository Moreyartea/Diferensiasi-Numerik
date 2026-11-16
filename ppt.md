Metode Numerik — Bab 6

# DIFERENSIASI NUMERIK

Metode Numerik — Bab 6

**Penyusun:** \[Nama anggota kelompok\]\
**Dosen:** \[Nama dosen\]\
**Program Studi / Universitas:** \[Program studi, Universitas\]\
**Tahun:** 2026

Sumber: Imron, Mardlijah & Asfihani (2022)Slide 1 dari 28

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

Sumber: Imron dkk. (2022), hlm. 185Slide 2 dari 28

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

Sumber: Imron dkk. (2022) & Materi FungsionalSlide 3 dari 28

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

Sumber: Imron dkk. (2022) & Materi FungsionalSlide 4 dari 28

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

Sumber: Imron dkk. (2022) & Materi FungsionalSlide 5 dari 28

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

Sumber: Imron dkk. (2022) & Materi FungsionalSlide 6 dari 28

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

Sumber: Imron dkk. (2022) & Materi FungsionalSlide 7 dari 28

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

Sumber: Imron dkk. (2022) & Materi FungsionalSlide 8 dari 28

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

Sumber: Imron dkk. (2022) & Materi FungsionalSlide 9 dari 28

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

Sumber: Imron dkk. (2022) & Materi FungsionalSlide 10 dari 28

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

Sumber: Imron dkk. (2022) & Materi FungsionalSlide 11 dari 28

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

Sumber: Imron dkk. (2022) & Materi FungsionalSlide 12 dari 28

Karena data dibuat dari fungsi s(t) = t^3, kita tahu nilai eksaknya adalah 12 m/s. Galat selisih maju 7, mundur 5, dan tengah hanya 1. Selisih tengah terbukti paling teliti, namun tetap perhatikan ketersediaan data di lapangan.

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

Sumber: Imron dkk. (2022), hlm. 189Slide 13 dari 28

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

Sumber: Imron dkk. (2022), hlm. 189Slide 14 dari 28

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

Sumber: Imron dkk. (2022), hlm. 186Slide 15 dari 28

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

Sumber: Imron dkk. (2022), hlm. 186–189Slide 16 dari 28

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

Tambahan: hitungan sendiri; konsep: Burden & Faires \[1\], catatan UMD \[2\]Slide 17 dari 28

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

Tambahan: definisi umum \[1\] §1.2; contoh dari data Contoh 6.1.1 (hitungan sendiri)Slide 18 dari 28

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

Sumber: Imron dkk. (2022), hlm. 196–199Slide 19 dari 28

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

Sumber: Imron dkk. (2022), hlm. 197–198Slide 20 dari 28

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

**Kaitan dengan Richardson:** hasil pendekatan turunan dapat dipakai sebagai dasar (N₁) untuk meningkatkan ketelitian lewat ekstrapolasi (slide 16).

Sumber: Imron dkk. (2022), hlm. 190–191Slide 21 dari 28

Semua hasil dihitung dari lima nilai tabel, bukan dari rumus fungsi. Nilai eksak 3e² ≈ 22,167168 hanya dipakai sebagai pembanding. Galat absolut dihitung |eksak − pendekatan|: 0,134858; 0,061622; 0,000169. Lima titik tengah paling dekat karena galatnya O(h⁴), sedangkan dua rumus lain O(h²). Tiga titik tengah dengan h berbeda nantinya menjadi bahan Richardson pada slide 16.

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

Sumber: Imron dkk. (2022), hlm. 191–195Slide 22 dari 28

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

Sumber: Imron dkk. (2022), hlm. 200–201Slide 23 dari 28

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

Sumber: Imron dkk. (2022), hlm. 201–202Slide 24 dari 28

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

Sumber: Imron dkk. (2022), Bab 6 (ringkasan)Slide 25 dari 28

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

Rumus dan orde: Imron dkk. (2022), hlm. 186–189; kolom kondisi: tambahan \[1\]Slide 26 dari 28

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

Sumber: Imron dkk. (2022), Bab 6 (ringkasan)Slide 27 dari 28

Rangkum perjalanan: dari definisi, dasar deret, rumus maju/mundur/tengah, rumus tiga dan lima titik, galat, lalu Richardson. Tekankan tiga hal: orde galat menentukan kecepatan perbaikan saat h mengecil, rumus harus cocok dengan posisi titik dan data yang ada, dan h tidak boleh terlalu kecil. Tutup dengan kalimat di bawah slide, lalu buka sesi tanya jawab.

Penutup

# TERIMA KASIH

**Sesi Tanya Jawab & Diskusi**  
*Diferensiasi Numerik & Ekstrapolasi Richardson*

Silakan ajukan pertanyaan atau tanggapan terkait materi yang telah dipaparkan.

**Tim Penyaji:**  
Farel Luther Siagian · Fatih Taqiyyuddin · Siti Zulayka Maulida Amali · Keegan Gibran Jehian  
**Dosen Pengampu:** Debi Yandra Niska, S.Kom., M.Kom. (2026)

Slide 28 dari 28

Ucapkan terima kasih kepada dosen pengampu dan rekan-rekan mahasiswa atas perhatian selama presentasi berlangsung. Buka kesempatan bagi audiens untuk sesi tanya jawab dan diskusi mengenai materi diferensiasi numerik.