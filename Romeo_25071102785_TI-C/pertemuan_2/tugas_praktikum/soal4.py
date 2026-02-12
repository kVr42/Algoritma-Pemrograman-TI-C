'''
Soal 4 (Rekursi dan Deret)
Buat sebuah fungsi rekursif bernama pangkat_rekursif(a, b) yang:
1.Menghitung nilai a pangkat b
2. Tidak boleh menggunakan operator pangkat (**)
3. Harus menggunakan rekursi
Contoh:
Input: a = 2, b = 5
Output: 32
'''

def pangkat_rekursif(a, b):
    if b == 0:
        return 1
    else:
        return a * pangkat_rekursif(a, b - 1)

# Contoh penggunaan fungsi
a = 2
b = 5
hasil = pangkat_rekursif(a, b)
print(f"{a} pangkat {b} adalah: {hasil}")
def pangkat_rekursif(a, b):
    if b == 0:
        return 1
    else:
        return a * pangkat_rekursif(a, b - 1)