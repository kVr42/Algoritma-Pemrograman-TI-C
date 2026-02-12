#function
print('function')

def sapa(nama):
    print('Halo,', nama + '!')
sapa('Andi')

#argument
print('argument')

def tambah(a, b):
    return a + b
hasil = tambah(5, 3)
print('Hasil penjumlahan:', hasil)

#*args and **kwargs
print('*args and **kwargs')

def info_siswa(nama, *nilai):
    print('Nama siswa:', nama)
    print('Nilai siswa:', nilai)
info_siswa('Budi', 80, 90, 85)
def info_guru(nama, **data):
    print('Nama guru:', nama)
    for key, value in data.items():
        print(f'{key}: {value}')
info_guru('Ibu Sari', mata_pelajaran='Matematika', umur=30)

#scope
print('scope')

x = 10  # variabel global
def tampilkan_x():
    global x
    x = 20  # mengubah variabel global
    print('Nilai x di dalam fungsi:', x)
tampilkan_x()
print('Nilai x di luar fungsi:', x)
def fungsi_lokal():
    y = 5  # variabel lokal
    print('Nilai y di dalam fungsi:', y)
fungsi_lokal()

#decorator
print('decorator')
def pembungkus(fungsi):
    def wrapper():
        print('Sebelum menjalankan fungsi.')
        fungsi()
        print('Setelah menjalankan fungsi.')
    return wrapper
@pembungkus
def sapa_dekorasi():
    print('Halo, selamat datang!')
sapa_dekorasi()


#lambda
print('lambda')

tambah = lambda a, b: a + b
hasil = tambah(7, 3)
print('Hasil penjumlahan dengan lambda:', hasil)

#rekursif
def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)
print('Faktorial dari 5:', faktorial(5))

#generator
print('generator')

def hitung_mundur(n):
    while n > 0:
        yield n
        n -= 1
for angka in hitung_mundur(5):
    print(angka)

