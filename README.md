
# SIMUTEH
### Sistem Informasi Mutu Daun Teh Berbasis Pengolahan Citra

**Identitas Mahasiswa**
- Nama: Syifa Humaira
- NIM: 2330511079
- Kelas: 7B
- SEED: 1079
- Program Studi: Teknik Informatika
- Universitas Muhammadiyah Sukabumi

## 1. Deskripsi Proyek

SIMUTEH merupakan proyek pengolahan citra digital untuk membantu proses penyortiran mutu daun teh berdasarkan kondisi bercak pada permukaan daun.

Sistem dirancang untuk mengolah citra daun teh dan menghasilkan informasi kelas mutu, yaitu:
- Sehat
- Bercak Ringan
- Bercak Berat

Proyek ini menggunakan dataset sintetis untuk menguji tahapan pengolahan citra.

## 2. Dataset

Dataset dibuat secara sintetis menggunakan script `src/buat_dataset_sintetis.py` dengan SEED 1079.

Jumlah dataset sebanyak 60 citra:
- 20 citra daun sehat
- 20 citra bercak ringan
- 20 citra bercak berat

Dataset memiliki lima kondisi pencahayaan:
- Normal
- Gelap
- Terang
- Kontras Rendah
- Bayangan

## 3. Tahapan Praktikum

Proyek SIMUTEH terdiri dari lima bagian:

1. **P1 - Persiapan Lingkungan:** persiapan lingkungan pemrograman dan pembuatan dataset sintetis.
2. **P2 - Citra dan Ruang Warna:** memahami pembentukan citra, sampling, kuantisasi, serta ruang warna.
3. **P3 - Histogram:** menganalisis histogram dan melakukan perbaikan kontras citra.
4. **P4 - Penapisan:** menguji berbagai metode penapisan untuk mengurangi derau.
5. **P5 - Prapemrosesan:** mengintegrasikan tahapan prapemrosesan ke dalam modul Python.

## 4. Teknologi yang Digunakan

- Python
- OpenCV
- NumPy
- Matplotlib
- Pandas
- Scikit-image
- Google Colab
- Git dan GitHub

## 5. Struktur Proyek

```text
simuteh-2330511079/
├── data/
│   └── sintetis/
├── notebook/
│   ├── B1_lingkungan.ipynb
│   ├── B2_citra_warna.ipynb
│   ├── B3_histogram.ipynb
│   ├── B4_penapisan.ipynb
│   └── B5_praproses.ipynb
├── src/
│   ├── buat_dataset_sintetis.py
│   ├── utils_cv.py
│   └── praproses.py
├── hasil/
├── laporan/
├── requirements.txt
└── README.md
