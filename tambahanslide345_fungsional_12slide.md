# Materi Tambahan Slide 3–5 — Memahami dan Menggunakan Diferensiasi Numerik
## Versi Fungsional: 12 Slide

Materi ini dirancang agar audiens memahami **untuk apa setiap metode digunakan, data apa yang dibutuhkan, bagaimana memilih metode, dan bagaimana melakukan perhitungannya**. Penurunan matematis dibuat singkat; fokus utama adalah pemahaman dan penggunaan.

---

# Slide 3 — Apa Kegunaan Diferensiasi Numerik?

Diferensiasi numerik membantu kita memperkirakan **seberapa cepat suatu nilai berubah** ketika data yang tersedia hanya berupa hasil pengukuran.

Contoh:
- Data posisi kendaraan dapat digunakan untuk memperkirakan kecepatan.
- Data kecepatan kendaraan dapat digunakan untuk memperkirakan percepatan.
- Data suhu pada beberapa lokasi dapat digunakan untuk melihat perubahan suhu terhadap jarak.
- Data konsentrasi zat dari waktu ke waktu dapat digunakan untuk memperkirakan laju perubahan konsentrasi.

**Kapan diperlukan?**

Ketika kita memiliki tabel atau kumpulan data pengukuran, tetapi tidak memiliki persamaan fungsi yang bisa langsung diturunkan.

**Intinya:** kita tidak harus mengetahui persamaan fungsi terlebih dahulu. Kita dapat menggunakan perubahan nilai pada data untuk memperkirakan turunannya.

---

# Slide 4 — Mengenal Data dan Titik yang Digunakan

Bayangkan kita mengukur posisi benda setiap satu detik. Untuk memperkirakan kecepatannya pada detik kedua, kita perlu melihat data di sekitar waktu tersebut.

Misalnya:

| Waktu (detik) | Posisi (meter) |
|---:|---:|
| 1 | 1 |
| 2 | 8 |
| 3 | 27 |

Pada contoh ini:
- \(x\) adalah titik yang ingin dianalisis. Misalnya \(x=2\).
- \(h\) adalah jarak antarwaktu pengukuran. Di sini \(h=1\) detik.
- \(x-h\) adalah titik sebelum titik yang dianalisis. Di sini \(1\).
- \(x+h\) adalah titik setelah titik yang dianalisis. Di sini \(3\).
- \(f(x)\) adalah nilai data pada titik yang sedang dianalisis.

**Cara membacanya:** jika \(x=2\), maka \(f(x)\) adalah posisi pada detik kedua, yaitu 8 meter.

Tiga metode berikut berbeda terutama pada **data tetangga mana yang dipakai**.

---

# Slide 5 — Selisih Maju: Menggunakan Data Setelah Titik yang Diamati

Selisih maju (*forward difference*) digunakan untuk memperkirakan laju perubahan pada suatu titik dengan membandingkan nilai di titik tersebut dan nilai pada titik setelahnya.

\[
f'(x)\approx\frac{f(x+h)-f(x)}{h}
\]

### Cara memahami rumus

- \(f'(x)\): laju perubahan yang ingin diperkirakan pada titik \(x\).
- \(f(x+h)\): nilai data satu langkah setelah titik yang diamati.
- \(f(x)\): nilai data pada titik yang diamati.
- \(h\): jarak antara kedua pengukuran.
- Pembilang \(f(x+h)-f(x)\): perubahan nilai dari titik sekarang ke titik berikutnya.
- Pembagian dengan \(h\): mengubah perubahan tersebut menjadi perubahan per satuan waktu atau jarak.

### Cara menggunakannya

1. Tentukan titik yang ingin dihitung.
2. Ambil nilai data pada titik tersebut.
3. Ambil nilai data satu langkah setelahnya.
4. Kurangkan nilai berikutnya dengan nilai saat ini.
5. Bagi hasilnya dengan jarak langkah \(h\).

### Contoh

Ingin memperkirakan kecepatan pada detik ke-2:
- Posisi pada detik ke-2 = 8 meter.
- Posisi pada detik ke-3 = 27 meter.
- Jarak waktu \(h=1\) detik.

\[
v(2)\approx\frac{27-8}{1}=19\text{ m/s}
\]

Artinya, berdasarkan perubahan posisi dari detik ke-2 ke detik ke-3, perkiraan kecepatan pada detik ke-2 adalah 19 m/s.

**Kapan cocok digunakan?** Ketika data setelah titik yang ingin dianalisis tersedia. Metode ini juga praktis untuk titik paling awal dalam tabel karena belum ada data sebelumnya.

---

# Slide 6 — Selisih Mundur: Menggunakan Data Sebelum Titik yang Diamati

Selisih mundur (*backward difference*) memperkirakan laju perubahan dengan membandingkan nilai pada titik yang diamati dan nilai pada titik sebelumnya.

\[
f'(x)\approx\frac{f(x)-f(x-h)}{h}
\]

### Cara memahami rumus

- \(f'(x)\): laju perubahan yang ingin diperkirakan pada titik \(x\).
- \(f(x)\): nilai data pada titik yang diamati.
- \(f(x-h)\): nilai data satu langkah sebelum titik tersebut.
- \(h\): jarak antara kedua pengukuran.
- Pembilang \(f(x)-f(x-h)\): perubahan nilai dari titik sebelumnya ke titik sekarang.

### Cara menggunakannya

1. Tentukan titik yang ingin dihitung.
2. Ambil nilai data pada titik tersebut.
3. Ambil nilai data satu langkah sebelumnya.
4. Kurangkan nilai saat ini dengan nilai sebelumnya.
5. Bagi hasilnya dengan jarak langkah \(h\).

### Contoh

Memperkirakan kecepatan pada detik ke-2:
- Posisi pada detik ke-2 = 8 meter.
- Posisi pada detik ke-1 = 1 meter.
- Jarak waktu \(h=1\) detik.

\[
v(2)\approx\frac{8-1}{1}=7\text{ m/s}
\]

Artinya, berdasarkan perubahan posisi dari detik ke-1 ke detik ke-2, perkiraan laju perubahan pada titik tersebut adalah 7 m/s.

**Kapan cocok digunakan?** Ketika data sebelum titik yang ingin dianalisis tersedia. Metode ini praktis untuk titik paling akhir dalam tabel karena belum ada data setelahnya.

---

# Slide 7 — Selisih Tengah: Menggunakan Data Sebelum dan Sesudah

Selisih tengah (*central difference*) menggunakan dua data sekaligus: satu titik sebelum dan satu titik sesudah titik yang ingin dianalisis.

\[
f'(x)\approx\frac{f(x+h)-f(x-h)}{2h}
\]

### Cara memahami rumus

- \(f'(x)\): laju perubahan yang ingin diperkirakan pada titik tengah \(x\).
- \(f(x+h)\): nilai data satu langkah setelah titik yang diamati.
- \(f(x-h)\): nilai data satu langkah sebelum titik yang diamati.
- \(2h\): jarak dari titik sebelum ke titik sesudah.
- Pembilang \(f(x+h)-f(x-h)\): perubahan nilai antara dua titik yang mengapit titik evaluasi.

### Mengapa penyebutnya \(2h\)?

Karena perhitungan menggunakan titik di kiri dan kanan:
- Jarak dari \(x-h\) ke \(x\) adalah \(h\).
- Jarak dari \(x\) ke \(x+h\) adalah \(h\).
- Jadi jarak total dari \(x-h\) ke \(x+h\) adalah \(2h\).

### Contoh

Memperkirakan kecepatan pada detik ke-2:
- Posisi pada detik ke-3 = 27 meter.
- Posisi pada detik ke-1 = 1 meter.
- \(h=1\) detik.

\[
v(2)\approx\frac{27-1}{2(1)}
=\frac{26}{2}=13\text{ m/s}
\]

**Kapan cocok digunakan?** Ketika data tersedia di kedua sisi titik yang ingin dianalisis. Metode ini sering memberikan perkiraan lebih baik untuk titik di bagian tengah tabel.

---

# Slide 8 — Bagaimana Memilih Metode yang Tepat?

Pemilihan metode terutama bergantung pada ketersediaan data di sekitar titik yang ingin dianalisis.

| Situasi data | Metode yang dapat digunakan | Alasannya |
|---|---|---|
| Data setelah titik tersedia | Selisih maju | Membandingkan titik sekarang dengan titik berikutnya |
| Data sebelum titik tersedia | Selisih mundur | Membandingkan titik sekarang dengan titik sebelumnya |
| Data sebelum dan sesudah tersedia | Selisih tengah | Menggunakan informasi dari kedua sisi titik |

### Ilustrasi sederhana

Untuk data waktu 1, 2, dan 3:
- Jika ingin menghitung pada waktu 1, data sebelumnya tidak tersedia. Selisih maju dapat digunakan.
- Jika ingin menghitung pada waktu 3, data sesudahnya tidak tersedia. Selisih mundur dapat digunakan.
- Jika ingin menghitung pada waktu 2, data waktu 1 dan 3 tersedia. Selisih tengah dapat digunakan.

**Hal penting:** jangan memilih metode hanya karena rumusnya terlihat lebih mudah. Periksa dahulu data mana yang tersedia.

---

# Slide 9 — Apa Perbedaan Ketelitian Ketiga Metode?

Ketiga metode sama-sama menghasilkan perkiraan turunan, tetapi tingkat galat pemotongannya berbeda.

| Metode | Orde galat pemotongan | Makna sederhana |
|---|---|---|
| Selisih maju | \(O(h)\) | Galat dominan sebanding dengan ukuran langkah |
| Selisih mundur | \(O(h)\) | Galat dominan sebanding dengan ukuran langkah |
| Selisih tengah | \(O(h^2)\) | Galat dominan sebanding dengan kuadrat ukuran langkah |

### Apa artinya dalam praktik?

Jika ukuran langkah \(h\) diperkecil menjadi setengah:
- Pada selisih maju dan mundur, galat pemotongan secara teori kira-kira menjadi setengah.
- Pada selisih tengah, galat pemotongan secara teori kira-kira menjadi seperempat.

Ini berlaku dengan asumsi fungsi cukup mulus dan galat pembulatan belum mendominasi.

**Kesimpulan praktis:** selisih tengah memiliki keunggulan ketelitian teoritis, tetapi membutuhkan data pada kedua sisi titik evaluasi. Selisih maju dan mundur tetap berguna ketika data hanya tersedia pada satu sisi.

---

# Slide 10 — Studi Kasus: Menghitung Kecepatan dari Data Posisi

Gunakan kembali data posisi berikut:

| Waktu \(t\) (detik) | Posisi \(s(t)\) (meter) |
|---:|---:|
| 1 | 1 |
| 2 | 8 |
| 3 | 27 |

Tentukan perkiraan kecepatan pada \(t=2\).

**Data yang diketahui:**
- \(s(1)=1\) meter.
- \(s(2)=8\) meter.
- \(s(3)=27\) meter.
- \(h=1\) detik.

### Selisih maju

Gunakan data waktu 2 dan 3:

\[
v(2)\approx\frac{s(3)-s(2)}{h}
=\frac{27-8}{1}=19\text{ m/s}
\]

### Selisih mundur

Gunakan data waktu 1 dan 2:

\[
v(2)\approx\frac{s(2)-s(1)}{h}
=\frac{8-1}{1}=7\text{ m/s}
\]

### Selisih tengah

Gunakan data waktu 1 dan 3:

\[
v(2)\approx\frac{s(3)-s(1)}{2h}
=\frac{27-1}{2}=13\text{ m/s}
\]

Ketiga hasil berbeda karena setiap metode menggunakan pasangan titik yang berbeda.

---

# Slide 11 — Membaca dan Menafsirkan Hasil

Hasil perhitungan studi kasus:

| Metode | Perkiraan kecepatan |
|---|---:|
| Selisih maju | 19 m/s |
| Selisih mundur | 7 m/s |
| Selisih tengah | 13 m/s |

Apa yang dapat kita pahami?

- Selisih maju melihat perubahan posisi dari detik ke-2 menuju detik ke-3.
- Selisih mundur melihat perubahan posisi dari detik ke-1 menuju detik ke-2.
- Selisih tengah melihat perubahan posisi dari detik ke-1 menuju detik ke-3, lalu membaginya dengan total selang waktu 2 detik.

Jadi, perbedaan hasil bukan karena salah hitung. Setiap metode menggunakan rentang data yang berbeda untuk memperkirakan laju perubahan di detik kedua.

**Pesan utama:** hasil diferensiasi numerik merupakan perkiraan. Kita perlu memahami data yang dipakai sebelum menafsirkan hasilnya.

---

# Slide 12 — Memeriksa Galat dan Menarik Kesimpulan

Untuk contoh ini, fungsi posisi yang menghasilkan data tersebut adalah:

\[
s(t)=t^3
\]

Jika fungsi diketahui, kecepatan eksak dapat dihitung:

\[
s'(t)=3t^2
\]

Pada \(t=2\):

\[
s'(2)=3(2)^2=12\text{ m/s}
\]

Galat absolut adalah jarak antara hasil perkiraan dan nilai eksak:

\[
E=|\text{hasil perkiraan}-\text{nilai eksak}|
\]

| Metode | Hasil perkiraan | Nilai eksak | Galat absolut |
|---|---:|---:|---:|
| Maju | 19 m/s | 12 m/s | 7 m/s |
| Mundur | 7 m/s | 12 m/s | 5 m/s |
| Tengah | 13 m/s | 12 m/s | 1 m/s |

Pada contoh ini, selisih tengah paling dekat dengan nilai eksak. Namun, bukan berarti metode tengah selalu menjadi pilihan terbaik dalam semua situasi. Ketersediaan data, kualitas pengukuran, dan kondisi fungsi tetap perlu diperhatikan.

### Ringkasan yang perlu diingat

- **Maju:** gunakan data sekarang dan sesudahnya.
- **Mundur:** gunakan data sebelumnya dan sekarang.
- **Tengah:** gunakan data sebelum dan sesudah titik yang dianalisis.
- **Pilih metode:** sesuaikan dengan posisi titik dan data yang tersedia.
- **Periksa hasil:** jika nilai eksak diketahui, hitung galat untuk menilai kedekatan hasil pendekatan.

---

## Catatan untuk Pemateri

Tekankan cara memilih dan menggunakan rumus, bukan menghafalkan penurunan matematisnya. Saat menjelaskan satu metode, tunjukkan:
1. Titik mana yang sedang dicari turunannya.
2. Data mana yang dipakai.
3. Mengapa data tersebut dipilih.
4. Bagaimana memasukkan angka ke rumus.
5. Apa arti hasil dan satuannya.

Dengan alur ini, audiens memahami fungsi setiap rumus dan dapat menentukan metode yang sesuai ketika menghadapi tabel data yang berbeda.
