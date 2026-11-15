Ekstrapolasi Richardson

## Metode Ekstrapolasi Richardson

### Pengertian

Menggabungkan **dua pendekatan** dengan ukuran langkah berbeda untuk membuang **suku galat utama**, sehingga hasilnya lebih teliti.

### Prinsip kerja

**1**Hitung pendekatan turunan dengan langkah h → D(h)

**2**Hitung pendekatan dengan langkah 2h → D(2h)

**3**Gabungkan keduanya untuk mengurangi galat utama

### Rumus umum

\\(f'\_0=D(h)+\\dfrac{D(h)-D(2h)}{2^n-1}\\)

- f′₀ : nilai turunan di x₀ setelah ekstrapolasi
- **D(h)** : hasil pendekatan turunan dengan ukuran langkah h yang **lebih kecil**
- **D(2h)** : hasil pendekatan turunan dengan ukuran langkah **dua kali lebih besar**
- n : orde galat awal, yaitu O(hⁿ)

Kedua hasil digabung untuk **menghilangkan suku galat utama**.

### Contoh: selisih tengah (n = 2)

\\(f'\_0=\\dfrac{4D(h)-D(2h)}{3}\\)

Orde galat naik: **O(h²) → O(h⁴)**

Kaitan notasi slide berikut: D(h) = N₁(h/2), D(2h) = N₁(h). Untuk n = 1 (selisih maju): 2D(h) − D(2h).

Sumber: Imron dkk. (2022), hlm. 196–199Slide 12 dari 17

Richardson tidak membuat rumus turunan baru dari data; ia menggabungkan dua hasil yang sudah ada. Hitung D(h) dan D(2h), lalu tambahkan koreksi \[D(h) − D(2h)\]/(2ⁿ − 1). Untuk selisih tengah galatnya O(h²), jadi n = 2 dan rumusnya (4D(h) − D(2h))/3 dengan orde O(h⁴). Untuk selisih maju n = 1. Di buku, langkah besar ditulis h dan langkah kecil h/2, jadi D(h) di slide ini sama dengan N₁(h/2) di buku. Pilih n sesuai bentuk galat pendekatan awal.

Contoh 6.2.1

## Contoh Richardson pada f(x) = ln x

**Diketahui:** f(x) = ln x, x₀ = 1,8\
N₁(0,1) = 0,5406722 · N₁(0,05) = 0,5479795\
Selisih maju: galat O(h), jadi n = 1

### Perhitungan

\\(N_2(0{,}1)=2N_1(0{,}05)-N_1(0{,}1)\\)

\\(=2(0{,}5479795)-0{,}5406722\\)

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

Sumber: Imron dkk. (2022), hlm. 197–198Slide 13 dari 17

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

Sumber: Imron dkk. (2022), hlm. 190–191Slide 14 dari 17

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

\\(\\dfrac{-3(9{,}025013)+4(11{,}02318)-13{,}46374}{0{,}2}=17{,}76971\\)

Lima titik tengah, x = 1,3:

\\(\\dfrac{9{,}025013-8(11{,}02318)+8(16{,}44465)-20{,}08554}{1{,}2}=26{,}92603\\)

**Kesimpulan:** pilih rumus menurut posisi titik dan ketersediaan data. **Kaitan dengan Richardson:** ekstrapolasi membutuhkan data yang sesuai dengan ukuran langkah yang dipakai (h dan setengahnya).

Sumber: Imron dkk. (2022), hlm. 191–195Slide 15 dari 17

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

Sumber: Imron dkk. (2022), hlm. 200–201Slide 16 dari 17

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

\\(N_1(0{,}2)=\\frac{20{,}08554-9{,}025013}{0{,}4}=27{,}651318\\)\
\\(N_1(0{,}1)=\\frac{16{,}44465-11{,}02318}{0{,}2}=27{,}107350\\)

### Tahap 2 — N₂

\\(N_2(0{,}2)=27{,}107350+\\frac{27{,}107350-27{,}651318}{3}\\)

\\(=\\mathbf{26{,}926027}\\)

### Mengapa N₃ tidak dapat dihitung?

N₃ membutuhkan N₁(0,05) = \[f(1,35) − f(1,25)\]/0,1, sedangkan f(1,25) dan f(1,35) **tidak tersedia** pada tabel.

**Kesimpulan:** Richardson tidak dapat dilanjutkan ke tingkat berikutnya bila data yang diperlukan tidak tersedia.

Catatan: Hasil perhitungan menggunakan data tabel yang tersedia.

Sumber: Imron dkk. (2022), hlm. 201–202Slide 17 dari 17

Titik x₀ = 1,3 dengan h = 0,2 dan 0,1; N₁(0,2) memakai f(1,5) dan f(1,1), N₁(0,1) memakai f(1,4) dan f(1,2). Gabungkan dengan pembagi 3 untuk N₂(0,2). Tingkat ketiga butuh N₁(0,05) dengan f(1,35) dan f(1,25), yang tidak ada di tabel, sehingga berhenti di N₂. Catatan untuk penyaji (dicek pada halaman buku 201–202): buku mencetak N₁(0,1) = (1/0,2)(f(1,4) − f(1,1)) = 27,10735 dan N₂(0,2) = 26,920273. Dengan f(1,2) hasil N₁(0,1) memang 27,10735, dan 27,10735 + (27,10735 − 27,651318)/3 = 26,926027, yang juga sama dengan lima titik tengah 26,92603 pada Contoh 6.1.3. Penyebab selisih tidak dapat dipastikan dari buku. Slide menampilkan hasil hitung ulang 26,926027 (dari data tabel yang tersedia); angka 26,920273 adalah yang tercetak di buku.