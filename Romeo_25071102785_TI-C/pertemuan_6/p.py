#1
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



#2
daftar_buku = [
    ["Legenda Cina", 2000],
    ["Resep Obat Kuat", 2500],
    ["Malin Kansai", 3000],
    ["CEO yang Menyamar", 3500],
    ["Adventure of Duda", 4000],
]

daftar_pinjaman = []

while True:
    nomor_buku = int(input("Masukkan nomor buku (0 untuk selesai): "))
    if nomor_buku == 0:
        break
    elif nomor_buku < 1 or nomor_buku > len(daftar_buku):
        print("Nomor buku tidak valid.")
    else:
        judul_buku, denda = daftar_buku[nomor_buku - 1]
        lama_pinjam = int(input(f"Masukkan lama pinjam buku {judul_buku} (hari): "))
        daftar_pinjaman.append((judul_buku, lama_pinjam))

total_denda = 0
for judul_buku, lama_pinjam in daftar_pinjaman:
    total_denda += lama_pinjam * denda

print("\nDaftar buku yang dipinjam:")
for index, (judul_buku, lama_pinjam) in enumerate(daftar_pinjaman, start=1):
    print(f"{index}. {judul_buku} - Lama pinjam: {lama_pinjam} hari")

print(f"\nTotal denda: {total_denda}")




#3
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



#4
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


#5
