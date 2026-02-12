'''
Soal 1 (Function dan Validasi Data)
  Buat sebuah fungsi bernama rata_rata(nilai) yang:
  1. Menerima sebuah list berisi nilai mahasiswa
  2. Menghitung rata-rata nilai
  3. Jika list kosong, kembalikan pesan: "Data kosong"
  Kemudian:
  1. Panggil fungsi dengan list: [80, 75, 90, 60, 85]
  2. Tampilkan hasilnya
'''
def rata_rata(nilai):
    if not nilai:
        return "Data kosong"
    return sum(nilai) / len(nilai)
  
# Memanggil fungsi dengan list nilai mahasiswa
nilai_mahasiswa = [80, 75, 90, 60, 85]
hasil = rata_rata(nilai_mahasiswa)
print("Rata-rata nilai mahasiswa:", hasil)
