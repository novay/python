# Plagiat (Py)
Library untuk memeriksa tingkat Plagiarisme menggunakan Bahasa Python.

Referensi:
- **Ranti Eka Putri, Andysah Putera Utama Siahaan**<br/>https://www.researchgate.net/publication/319272358_Examination_of_Document_Similarity_Using_Rabin-Karp_Algorithm
- **Andysah Putera Utama Siahaan, Mesran, Robbi Rahim, Dodi Siregar**<br/>https://www.ijstr.org/final-print/july2017/K-gram-As-A-Determinant-Of-Plagiarism-Level-In-Rabin-karp-Algorithm.pdf

### Instalasi
```
pip install plagiat
```

### Menggunakan File .txt
```Python
from plagiat.deteksi import Deteksi

cek = Deteksi("./plagiat/dokumen/kalimat-1.txt", "./plagiat/dokumen/kalimat-2.txt")

print('Persentase plagiarisme = {0}%'.format(cek.hitung()))
```

### Menggunakan Text
```Python
from plagiat.deteksi import Deteksi

cek = Deteksi("Aku sedang belajar kecerdasan buatan", 
               "Mahasiswa yang cerdas selalu siap menerima tantangan", 
               text=True)

print('Persentase plagiarisme = {0}%'.format(cek.hitung()))
```

### Menggunakan URL
```Python
from plagiat.deteksi import Deteksi

teks_1 = 'https://raw.githubusercontent.com/novay/amikom/main/datasets/text/kalimat-1.txt'
teks_2 = 'https://raw.githubusercontent.com/novay/amikom/main/datasets/text/kalimat-1.txt'

cek = Deteksi(teks_1, teks_2, url=True)

print('Persentase plagiarisme = {0}%'.format(cek.hitung()))
```

### Penggunaan Parameter
```Python
from plagiat.deteksi import Deteksi

Deteksi(teks_1, teks_2, text=True, url=True, bahasa='english')
```
**Penjelasan**<br/>
- `text=True` digunakan untuk mendeteksi string<br/> default False
- `url=True` digunakan untuk mendeteksi dokumen melalui URL<br/> default False
- `bahasa='english'` digunakan untuk menentukan bahasa yang digunakan dalam proses stopwords<br/> default 'indonesian'

### Disclaimer
Library ini di buat hanya untuk keperluan pembuatan tugas Data Science.

Salam hormat,<br/>
Novianto Rahmadi (22.55.2293)

#### Credit
- Paper Ranti Eka Putri, Andysah Putera Utama Siahaan, Mesran, Robbi Rahim & Dodi Siregar
- NLTK - corpus, tokenize, stem
- Numpy
- TheDhejavu - Rabin Karp Module <br/>https://gist.github.com/TheDhejavu/39d6cfec2b3f75a1ac111042cb8aebdb#file-rabin_karp-py