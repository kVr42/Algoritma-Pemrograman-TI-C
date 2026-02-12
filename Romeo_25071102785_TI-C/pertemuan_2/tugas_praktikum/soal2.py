'''
Soal 2 (Range dan Pola Bilangan)
  Buat sebuah fungsi bernama bilangan_prima(n) yang:
  1. Menggunakan range()
  2. Mengembalikan list bilangan prima dari 1 sampai n
  Kemudian:
  1. Panggil fungsi untuk n = 50
  2. Tampilkan hasilnya
'''

def bilangan_prima(n):
    prima = []
    for num in range(2, n + 1):
        is_prima = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prima = False
                break
        if is_prima:
            prima.append(num)
    return prima
  
# Memanggil fungsi untuk n = 50
n = 50
hasil = bilangan_prima(n)
print("Bilangan prima dari 1 sampai", n, "adalah:", hasil)
def bilangan_prima(n):
    prima = []
    for num in range(2, n + 1):
        is_prima = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prima = False
                break
        if is_prima:
            prima.append(num)
    return prima