'''
Soal 5. Class Buku dan Peminjaman
Topik: OOP| Estimasi waktu: 20 menit
Deskripsi:
Buat versi OOP dari sistem peminjaman buku menggunakan dua class sederhana.
Ketentuan Program:
  1. Buat class Buku dengan atribut judul dan denda_per_hari, serta method tampilkan() yang mencetak informasi buku dalam format: "Judul Buku - Denda Rp .../hari".
  2. Buat class Peminjaman dengan atribut total_denda (awalnya 0) dan method tambah(buku, hari_terlambat) untuk menambahkan denda ke total, serta method ringkasan() untuk menampilkan total denda.
  3. Pada program utama, buat minimal 3 objek Buku dan tampilkan semuanya menggunakan for loop.
  4. Buat satu objek Peminjaman, minta pengguna memilih buku dan input hari keterlambatan, lalu panggil method tambah() dan tampilkan ringkasan akhir dengan method ringkasan().
'''

class Buku:
    def __init__(self, judul, denda_per_hari):
        self.judul = judul
        self.denda_per_hari = denda_per_hari

    def tampilkan(self):
        print(f"Judul Buku: {self.judul}")
        print(f"Denda per hari: {self.denda_per_hari}")

class Peminjaman:
    def __init__(self):
        self.total_denda = 0

    def tambah(self, buku, hari_terlambat):
        self.total_denda += buku.denda_per_hari * hari_terlambat

    def ringkasan(self):
        print(f"Total denda: {self.total_denda}")

# Contoh penggunaan
buku1 = Buku("Buku 1", 1000)
buku2 = Buku("Buku 2", 1500)
buku3 = Buku("Buku 3", 2000)

peminjaman = Peminjaman()
for buku in [buku1, buku2, buku3]:
    buku.tampilkan()

hari_keterlambatan = int(input("Masukkan hari keterlambatan: "))
peminjaman.tambah(buku1, hari_keterlambatan)
peminjaman.ringkasan()