# Tugas A — Hitung Total Ukuran
def total_ukuran(folder: dict) -> int:
    total = 0
    for key, value in folder.items():
        if isinstance(value, dict):
            total += total_ukuran(value)
        else:
            total += value
    return total

# Tugas B — Hitung Jumlah File
def hitung_file(folder: dict) -> int:
    count = 0
    for key, value in folder.items():
        if isinstance(value, dict):
            count += hitung_file(value)
        else:
            count += 1
    return count

# Tugas C — Cari File Terbesar
def cari_terbesar(folder: dict) -> tuple:
    terbesar = ("", 0)  # (nama_file, ukuran_kb)
    for key, value in folder.items():
        if isinstance(value, dict):
            kandidat = cari_terbesar(value)
            if kandidat[1] > terbesar[1]:
                terbesar = kandidat
        else:
            if value > terbesar[1]:
                terbesar = (key, value)
    return terbesar

# Tugas D — Cetak Struktur Folder
def tampilkan_tree(folder: dict, nama: str = "root", level: int = 0):
    indent = "  " * level
    if level == 0:
        print(f"{indent}📁 {nama}")
    for key, value in folder.items():
        if isinstance(value, dict):
            print(f"{indent}  📁 {key}")
            tampilkan_tree(value, key, level + 1)
        else:
            print(f"{indent}  📄 {key} ({value} KB)")

# Contoh penggunaan
struktur = {
    "Skripsi Alek": {
        "Bab 1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
        },
        "Bab 2": {
            "landasan_teori.docx": 118,
            "referensi": {
                "paper_A.pdf": 340,
                "paper_B.pdf": 210
            }
        },
        "Bab 3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "erd.png": 278,
                "arsitektur": {
                    "sistem.png": 430
                }
            }
        },
        "sidang": {
            "presentasi.pptx": 2048,
            "catatan_revisi.txt": 15
        },
        "README.txt": 8
    }
}

print(f"Total ukuran: {total_ukuran(struktur)} KB")
print(f"Jumlah file: {hitung_file(struktur)}")
terbesar = cari_terbesar(struktur)
print(f"File terbesar: {terbesar[0]} ({terbesar[1]} KB)")
tampilkan_tree(struktur)
print("coba lagi tahun depan")
