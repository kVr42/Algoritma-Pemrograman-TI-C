#pyton if
print("pyton if")

nilai = 75
if nilai >= 60:
    print("Selamat, Anda lulus!")
else:
    print("Maaf, Anda tidak lulus.")


#pyton elif
print("pyton elif")
nilai = 85
if nilai >= 85:
    print("Selamat, Anda mendapatkan nilai A!")
elif nilai >= 70:
    print("Selamat, Anda mendapatkan nilai B!")
elif nilai >= 60:
    print("Selamat, Anda mendapatkan nilai C!")
else:
    print("Maaf, Anda mendapatkan nilai D.")


#pyton else
print("pyton else")
nilai = 50
if nilai >= 60:
    print("Selamat, Anda lulus!")
else:
    print("Maaf, Anda tidak lulus.")


#shorthand if
print("shorthand if")

nilai = 90
if nilai >= 75: print("Selamat, Anda lulus!")


#logical operator
print("logical operator")

nilai = 80
kehadiran = 85
if nilai >= 75 and kehadiran >= 80:
    print("Selamat, Anda lulus!")
else:
    print("Maaf, Anda tidak lulus.")


#nested if
print("nested if")

nilai = 90
kehadiran = 95
if nilai >= 75:
    if kehadiran >= 80:
        print("Selamat, Anda lulus!")
    else:
        print("Maaf, Anda tidak lulus karena kehadiran kurang.")
else:
    print("Maaf, Anda tidak lulus karena nilai kurang.")


#pass statement
print("pass statement")

nilai = 70
if nilai >= 75:
    pass  # Belum ada tindakan untuk nilai lulus
else:
    print("Maaf, Anda tidak lulus.")

