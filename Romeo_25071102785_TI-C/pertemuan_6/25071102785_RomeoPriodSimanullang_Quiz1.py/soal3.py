'''
Soal 3. Perhitungan Denda Keterlambatan
Deskripsi:
Setelah data peminjaman diketahui, petugas perlu menghitung total denda jika anggota terlambat mengembalikan buku.
Ketentuan Program:
  1. Minta pengguna menginput jumlah hari keterlambatan.
  2. Gunakan while loop untuk memastikan hari keterlambatan tidak kurang dari 0. Jika < 0, tampilkan pesan error dan minta input ulang.
  3. Hitung total denda berdasarkan buku yang dipinjam dan hari keterlambatan.
    • Gunakan if-else untuk menampilkan pesan:
    • "Tidak ada denda" jika hari keterlambatan = 0, atau
    • "Total denda Anda: Rp ..." jika ada keterlambatan.
'''

# Input jumlah hari keterlambatan
hari_keterlambatan = int(input("Masukkan jumlah hari keterlambatan: "))

# Validasi jumlah hari keterlambatan
while hari_keterlambatan < 0:
    print("Jumlah hari keterlambatan tidak valid.")
    hari_keterlambatan = int(input("Masukkan jumlah hari keterlambatan: "))

# Hitung total denda
if hari_keterlambatan == 0:
    print("Tidak ada denda.")
else:
    total_denda = hari_keterlambatan * 2000
    print(f"Total denda Anda: Rp {total_denda}")