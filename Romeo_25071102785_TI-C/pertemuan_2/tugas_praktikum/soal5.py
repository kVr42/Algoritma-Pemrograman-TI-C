'''
Soal 5 (Python Module dan Algoritma)
  Buat sebuah program Python yang:
  1. Menggunakan module math
  2. Membuat fungsi jarak(x1, y1, x2, y2) untuk menghitung jarak dua titik pada bidang Kartesius
  3. Menggunakan rumus:
  d =√((x2 − x1)^2 + (y2 − y1)^2)
  Contoh keluaran:
  Jarak = 5.0
'''

import math

def jarak(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)

# Contoh penggunaan fungsi
x1, y1 = 0, 0
x2, y2 = 3, 4
hasil = jarak(x1, y1, x2, y2)
print(f"Jarak = {hasil}")