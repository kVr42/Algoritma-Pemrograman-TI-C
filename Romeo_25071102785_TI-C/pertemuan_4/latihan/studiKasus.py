class StatusError(Exception):
    pass

try:
    nama = input("Masukkan nama karakter: ")
    hp = int(input("Masukkan jumlah HP: "))
    mana = int(input("Masukkan jumlah Mana: "))

    if hp <= 0 or mana <= 0:
        raise StatusError("HP dan Mana harus lebih dari 0!")

except ValueError:
    print("HP dan Mana harus berupa angka!")

except StatusError as e:
    print("Error:", e)

else:
    print("\n=== DATA KARAKTER ===")
    print(f"Nama  : {nama}")
    print(f"HP    : {hp}")
    print(f"Mana  : {mana}")
    print("Karakter berhasil dibuat!")

finally:
    print("\nProgram selesai.")