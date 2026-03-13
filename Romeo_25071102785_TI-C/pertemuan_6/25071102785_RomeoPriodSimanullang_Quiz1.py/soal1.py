'''
Studi Kasus : Sistem Peminjaman Buku Perpustakaan “Cerdas Ilmu”
  Perpustakaan Cerdas Ilmu ingin membuat program sistem peminjaman buku sederhana 
  menggunakan Python. Setiap soal di bawah ini merupakan bagian dari sistem tersebut yang 
  dikerjakan secara bertahap.

Soal 1. Menampilkan Daftar Buku
Deskripsi:
  Buat program untuk menampilkan daftar buku yang tersedia dan meminta anggota memilih satu buku.
Ketentuan Program:
  1. Buat list buku berisi 5 item buku beserta denda per hari keterlambatan, contoh: 
  [["Algoritma", 2000], ["Basis Data", 2500], ...].
  2. Tampilkan seluruh daftar buku beserta denda menggunakan for loop dengan penomoran.
  3. Minta pengguna memasukkan nomor buku yang dipilih.
  4. Gunakan if-else untuk memvalidasi input: jika nomor tidak valid, tampilkan pesan error; 
  jika valid, tampilkan judul buku dan denda per hari
'''

daftar_buku = [
    ["Legenda Cina", 2000],
    ["Resep Obat Kuat", 2500],
    ["Malin Kansai", 3000],
    ["CEO yang Menyamar", 3500],
    ["Adventure of Duda", 4000],
]

print("Daftar Buku:")
for index, buku in enumerate(daftar_buku, start=1):
    print(f"{index}. {buku[0]} - Denda per hari: {buku[1]}")

nomor_buku = int(input("Masukkan nomor buku: "))

if nomor_buku < 1 or nomor_buku > len(daftar_buku):
    print("Nomor buku tidak valid.")
else:
    judul_buku, denda = daftar_buku[nomor_buku - 1]
    print(f"Judul buku: {judul_buku}")
    print(f"Denda per hari: {denda}")