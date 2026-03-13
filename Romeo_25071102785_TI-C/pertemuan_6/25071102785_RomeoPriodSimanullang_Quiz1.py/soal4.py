'''
Soal 4. Rekap Peminjaman Menggunakan Matriks
Topik: Matriks, Nested For Loop| Estimasi waktu: 25 menit
Deskripsi:
Petugas ingin melihat rekap jumlah buku dipinjam selama beberapa minggu. Data disimpan dalam bentuk matriks di mana baris merepresentasikan minggu dan kolom merepresentasikan kategori buku.
Ketentuan Program:
  1. Tentukan jumlah minggu (baris) dan jumlah kategori buku (kolom) melalui input pengguna.
  2. Gunakan nested for loop untuk menginput jumlah buku dipinjam pada setiap minggu untuk setiap kategori.
  3. Tampilkan matriks data peminjaman dalam format tabel yang rapi.
  4. Hitung dan tampilkan:
    • total peminjaman per minggu (jumlah tiap baris) dan
    • total peminjaman per kategori (jumlah tiap kolom).
'''

# Input jumlah minggu dan kategori buku
minggu = int(input("Masukkan jumlah minggu: "))
kategori_buku = int(input("Masukkan jumlah kategori buku: "))

# Inisialisasi matriks data peminjaman
data_peminjaman = [[0 for _ in range(kategori_buku)] for _ in range(minggu)]

# Input data peminjaman
for i in range(minggu):
    for j in range(kategori_buku):
        data_peminjaman[i][j] = int(input(f"Masukkan jumlah buku dipinjam minggu {i + 1} kategori {j + 1}: "))

# Tampilkan matriks data peminjaman
print("Rekap Peminjaman:")
for i in range(minggu):
    for j in range(kategori_buku):
        print(f"{data_peminjaman[i][j]}", end="\t")
    print()

# Hitung dan tampilkan total peminjaman per minggu dan per kategori
total_minggu = [sum(data_peminjaman[i]) for i in range(minggu)]
total_kategori = [sum(data_peminjaman[i][j] for i in range(minggu)) for j in range(kategori_buku)]

print("Total peminjaman per minggu:")
for i in range(minggu):
    print(f"Minggu {i + 1}: {total_minggu[i]}")

print("Total peminjaman per kategori:")
for j in range(kategori_buku):
    print(f"Kategori {j + 1}: {total_kategori[j]}")