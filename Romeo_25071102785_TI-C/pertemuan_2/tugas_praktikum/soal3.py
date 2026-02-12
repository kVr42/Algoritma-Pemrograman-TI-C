'''
Soal 3 (Rekursi - Penjumlahan Digit)
Buat sebuah fungsi rekursif bernama jumlah_digit(n) yang:
1. Menghitung jumlah seluruh digit dari sebuah bilangan
2. Menggunakan konsep rekursi
Contoh:
Input: 1234
Output: 10
'''

def jumlah_digit(n):
    if n == 0:
        return 0
    else:
        return n % 10 + jumlah_digit(n // 10)

# Contoh penggunaan fungsi
angka = 1234
hasil = jumlah_digit(angka)
print("Jumlah digit dari", angka, "adalah:", hasil)