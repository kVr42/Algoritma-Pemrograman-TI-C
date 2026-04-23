#=== BAGIAN A : FUNGSI INTI GAME ===
DAFTAR_PILIHAN = ["gunting", "batu", "kertas", "batu", "gunting", "kertas", "gunting", "batu"]

# Fungsi untuk menentukan pemenang berdasarkan pilihan pemain dan komputer
def tentukan_pemenang(pilihan_pemain, pilihan_komputer):
    """Tentukan pemenang berdasarkan pilihan pemain dan komputer."""
    if pilihan_pemain == pilihan_komputer:
        return "seri"
    elif (pilihan_pemain == "gunting" and pilihan_komputer == "kertas") or \
         (pilihan_pemain == "batu" and pilihan_komputer == "gunting") or \
         (pilihan_pemain == "kertas" and pilihan_komputer == "batu"):
        return "pemain"
    else:
        return "komputer"

# Fungsi untuk menjalankan satu giliran permainan suit
def main_satu_giliran(nomor_giliran):
    pilihan_komputer = DAFTAR_PILIHAN[nomor_giliran % len(DAFTAR_PILIHAN)]
    
    while True:
        pilihan_pemain = input("Pilih (gunting, batu, kertas): ").lower()
        if pilihan_pemain in ["gunting", "batu", "kertas"]:
            break
        print("Pilihan tidak valid. Silakan coba lagi.")
    
    hasil = tentukan_pemenang(pilihan_pemain, pilihan_komputer)
    print(f"Komputer memilih: {pilihan_komputer}")
    if hasil == "pemain":
        print(f"Pemain menang giliran {nomor_giliran}!")
    elif hasil == "komputer":
        print(f"Komputer menang giliran {nomor_giliran}!")
    else:
        print(f"Giliran {nomor_giliran} berakhir seri!")
    return hasil

# Fungsi untuk menjalankan satu ronde permainan suit
def main_satu_ronde(nama, nomor_ronde):
    """Jalankan satu ronde permainan suit."""
    kemenangan_pemain = 0
    kemenangan_komputer = 0
    
    while kemenangan_pemain < 3 and kemenangan_komputer < 3:
        hasil_giliran = main_satu_giliran(nomor_ronde)
        if hasil_giliran == "pemain":
            kemenangan_pemain += 1
        elif hasil_giliran == "komputer":
            kemenangan_komputer += 1
    
    if kemenangan_pemain > kemenangan_komputer:
        print(f"{nama} menang ronde {nomor_ronde}!")
        skor = kemenangan_pemain * 10
    elif kemenangan_komputer > kemenangan_pemain:
        print(f"Komputer menang ronde {nomor_ronde}!")
        skor = 0
    else:
        print(f"Ronde {nomor_ronde} berakhir seri!")
        skor = 0
    
    return [nama, skor]


#=== BAGIAN B : RIWAYAT SKOR DENGAN MATRIX 2D ===
def tampilkan_riwayat(riwayat):
    """Tampilkan riwayat skor dalam format tabel."""
    if not riwayat:
        print("Belum ada riwayat.")
        return
    
    print(f"{'No.':<5} {'Nama':<20} {'Skor':<10}")
    print("-" * 35)
    for index, (nama, skor) in enumerate(riwayat, start=1):
        print(f"{index:<5} {nama:<20} {skor:<10}")


#=== BAGIAN C : LEADERBOARD DENGAN BUBBLE SORT ===

# Fungsi untuk mengurutkan riwayat berdasarkan skor menggunakan Bubble Sort
def bubble_sort_riwayat(riwayat):
    sorted_riwayat = riwayat.copy() # Membuat salinan dari list riwayat agar data asli tidak berubah
    n = len(sorted_riwayat)

    # Bubble Sort untuk mengurutkan dari skor tertinggi ke terendah
    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_riwayat[j][1] < sorted_riwayat[j+1][1]:
                sorted_riwayat[j], sorted_riwayat[j+1] = sorted_riwayat[j+1], sorted_riwayat[j]
    
    return sorted_riwayat



#=== PROGRAM UTAMA ===

# Minta nama pemain
nama_pemain = input("Masukkan nama pemain: ")
nomor_ronde = 1
riwayat = []

while True:
    print(f"\n--- Ronde {nomor_ronde} ---")
    hasil_ronde = main_satu_ronde(nama_pemain, nomor_ronde)
    riwayat.append(hasil_ronde)
    
    # Tanyakan apakah pemain ingin bermain lagi
    lanjut = input("Apakah Anda ingin bermain lagi? (ya/tidak): ").lower()
    if lanjut != "ya":
        break
    
    nomor_ronde += 1

print("\n--- Selesai ---")
tampilkan_riwayat(riwayat)
sorted_riwayat = bubble_sort_riwayat(riwayat)
tampilkan_leaderboard(sorted_riwayat)