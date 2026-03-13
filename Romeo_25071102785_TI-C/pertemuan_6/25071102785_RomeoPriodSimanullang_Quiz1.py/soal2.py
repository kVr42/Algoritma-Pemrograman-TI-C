'''
Soal 2. Menghitung Total Peminjaman
Deskripsi:
Berdasarkan Soal 1 kembangan kode agar anggota dapat meminjam lebih dari satu buku dan 
program menghitung estimasi denda.
Ketentuan Program:
  1. Gunakan while loop agar anggota dapat terus menambah buku pinjaman. Loop berhenti ketika anggota memasukkan angka 0.
  2. Simpan setiap buku yang dipinjam ke dalam list berisi judul buku dan lama pinjam (hari).
  3. Setelah selesai, tampilkan daftar buku yang dipinjam menggunakan for loop.
  4. Hitung total estimasi denda jika semua buku terlambat 1 hari (simulasi sederhana) dan tampilkan hasilnya..
'''

daftar_buku = [
    ["Legenda Cina", 2000],
    ["Resep Obat Kuat", 2500],
    ["Malin Kansai", 3000],
    ["CEO yang Menyamar", 3500],
    ["Adventure of Duda", 4000],
]

print (daftar_buku)
for index, buku in enumerate (daftar_buku, start=1):
    print(f"{index}. {buku[0]} - Denda per hari: {buku[1]}")


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