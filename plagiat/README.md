# Plagiat

Library untuk memeriksa tingkat Plagiarisme atau *Similarity* menggunakan Bahasa Python. Secara default library ini akan menggunakan Algoritma Rabin Karp sebagai perhitungan utamanya.

Pustaka ini dibuat hanya sebagai penunjang untuk membantu saya menguji-coba dan memahami semua konsep algoritma untuk menghitung similaritas.

### Instalasi
```
pip install plagiat
```

### Cara Penggunaan

#### Menggunakan File .txt
```Python
from plagiat.deteksi import Deteksi

file_1 = '/content/kalimat-1.txt'
file_2 = '/content/kalimat-2.txt'

cek = Deteksi(file_1, file_2, url=True).hitung()

print('Persentase plagiarisme = {0}%'.format(cek))
```

#### Menggunakan Text
```Python
from plagiat.deteksi import Deteksi

string_1 = "Aku sedang belajar kecerdasan buatan"
string_2 = "Mahasiswa yang cerdas selalu siap menerima tantangan"

cek = Deteksi(string_1, string_2, text=True).hitung()

print('Persentase plagiarisme = {0}%'.format(cek))
```

#### Menggunakan URL
```Python
from plagiat.deteksi import Deteksi

teks_1 = 'https://raw.githubusercontent.com/novay/amikom/main/datasets/text/kalimat-1.txt'
teks_2 = 'https://raw.githubusercontent.com/novay/amikom/main/datasets/text/kalimat-1.txt'

cek = Deteksi(teks_1, teks_2, url=True).hitung()

print('Persentase plagiarisme = {0}%'.format(cek))
```

#### Penggunaan Parameter
```Python
from plagiat.deteksi import Deteksi

Deteksi(teks_1, teks_2, text=True, url=True, bahasa='english', method='Cosine').hitung()
```
**Penjelasan**<br/>
- `text=True` digunakan untuk mendeteksi string<br/> default False
- `url=True` digunakan untuk mendeteksi dokumen melalui URL<br/> default False
- `bahasa='english'` digunakan untuk menentukan bahasa yang digunakan dalam proses stopwords<br/> default 'indonesian'
- `method='Cosine'` digunakan untuk mengubah metode yang ingin digunakan<br/>default 'Rabin Karp', pilihan 'Rabin Karp', 'Cosine', 'Jaccard'

### Referensi

**Rabin Karp**:
- **Ranti Eka Putri, Andysah Putera Utama Siahaan**<br/>https://www.researchgate.net/publication/319272358_Examination_of_Document_Similarity_Using_Rabin-Karp_Algorithm
- **Andysah Putera Utama Siahaan, Mesran, Robbi Rahim, Dodi Siregar**<br/>https://www.ijstr.org/final-print/july2017/K-gram-As-A-Determinant-Of-Plagiarism-Level-In-Rabin-karp-Algorithm.pdf

**Jaccard Similarity**:
- https://en.wikipedia.org/wiki/Jaccard_index

**Cosine Similarity**:
- **Jiapeng Wang, Yihong Dong**<br/>https://www.researchgate.net/publication/344010599_Measurement_of_Text_Similarity_A_Survey


### Disclaimer
Library ini di buat hanya untuk keperluan pembuatan tugas Data Science.

Output mungkin saja bisa berbeda dengan pustaka lain khususnya perhitungan Cosine, karena dalam implementasinya ada variasi dalam cara perhitungan vektor TF-IDF, tokenisasi kata, dan faktor-faktor lainnya. Agar hasil lebih maksimal, lebih baik handle dulu masalah stop word, n-gram, dan normalisasi secara mandiri karena perhitungan yang dilakukan dalam pustaka ini hanya melakukan normalisasi sederhana sebelum dieksekusi.

Salam hormat,<br/>
Novianto Rahmadi (22.55.2293)

#### Credit
- Paper Ranti Eka Putri, Andysah Putera Utama Siahaan, Mesran, Robbi Rahim & Dodi Siregar
- NLTK - corpus, tokenize, stem
- Numpy
- TheDhejavu - Rabin Karp Module <br/>https://gist.github.com/TheDhejavu/39d6cfec2b3f75a1ac111042cb8aebdb#file-rabin_karp-py
- Jiapeng Wang, Yihong Dong (Cosine Similarity)