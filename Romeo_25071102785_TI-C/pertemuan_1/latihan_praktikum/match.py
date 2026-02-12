# menyimpan data
hari = "Senin"

# pengecekan nilai
match hari:
    case "Senin":
        print("Masuk")
    case "Minggu":
        print("Libur")
    case _:
        print("Tidak diketahui")
