from plagiat.deteksi import Deteksi

# teks_1 = 'https://raw.githubusercontent.com/novay/amikom/main/datasets/text/kalimat-1.txt'
# teks_2 = 'https://raw.githubusercontent.com/novay/amikom/main/datasets/text/kalimat-1.txt'
# cek = Deteksi(teks_1, teks_2, url=True)
# print('Persentase plagiarisme = {0}%'.format(cek.hitung()))

cek = Deteksi("Aku sedang belajar kecerdasan buatan", "Mahasiswa yang cerdas selalu siap menerima tantangan", text=True)

print('Persentase plagiarisme = {0}%'.format(cek.hitung()))