from plagiat.deteksi import Deteksi

""" Menggunakan URL """
teks_1 = 'https://raw.githubusercontent.com/novay/amikom/main/datasets/text/kalimat-1.txt'
teks_2 = 'https://raw.githubusercontent.com/novay/amikom/main/datasets/text/kalimat-2.txt'
cek = Deteksi(teks_1, teks_2, url=True).hitung()
# print('Persentase plagiarisme = {0}%'.format(cek))

""" Menggunakan File """
# file_1 = '/content/kalimat-1.txt'
# file_2 = '/content/kalimat-2.txt'
# cek = Deteksi(file_1, file_2, url=True).hitung()
# print('Persentase plagiarisme = {0}%'.format(cek))

""" Rabin Karp Method """
rabin = Deteksi("Aku sedang belajar kecerdasan buatan", "Mahasiswa yang cerdas selalu siap menerima tantangan", text=True).hitung()
print('Rabin Karp Similarity = {0}%'.format(rabin))

""" Jaccard Method """
jaccard = Deteksi("Aku sedang belajar kecerdasan buatan", "Mahasiswa yang cerdas selalu siap menerima tantangan", text=True, method='Jaccard').hitung()
print('Jaccard Similarity = {0}%'.format(jaccard))

""" Cosine Method """
cosine = Deteksi("Aku sedang belajar kecerdasan buatan", "Mahasiswa yang cerdas selalu siap menerima tantangan", text=True, method='Cosine').hitung()
print('Cosine Similarity = {0}%'.format(cosine))