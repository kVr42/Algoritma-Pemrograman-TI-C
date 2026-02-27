'''
Buatlah program python (tanpa NumPy) yang:
a Menjumlahkan matriks A dan B, simpan hasilnya dalam variabel C_tambah
b Mengurangkan matriks A dikurangi B, simpan dalam variabel C_kurang
c Mengalikan setiap elemen matriks A dengan skalar k = 4 , simpan dalam C_skalar
d Hitunglah deteminan matriks A dan B menggunakan Metode Sarrus
e Menampilkan keempat hasil dengan format rapi baris per baris
'''


A = [[5, 3, 1],
    [2, 8, 4],
    [6, 0, 7]]
B = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

#a.Menjumlahkan matriks A dan B, simpan hasilnya dalam variabel C_tambah
def tambah_matriks(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print('Error: ukuran matriks tidak sama')
        return None
    baris, kolom = len(A), len(A[0])
    hasil = [[A[i][j] + B[i][j] for j in range(kolom)] for i in
             range(baris)]
    return hasil

C = tambah_matriks(A, B)
if C is not None:
    for baris in C:
        print(baris)

#b.Mengurangkan matriks A dikurangi B, simpan dalam variabel C_kurang
def kurang_matriks(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print('Error: ukuran matriks tidak sama')
        return None
    baris, kolom = len(A), len(A[0])
    hasil = [[A[i][j] - B[i][j] for j in range(kolom)] for i in
             range(baris)]
    return hasil

D = kurang_matriks(A, B)
if D is not None:
    for baris in D:
        print(baris)

#c.Mengalikan setiap elemen matriks A dengan skalar k = 4 , simpan dalam C_skalar
def kali_matriks(A, k):
    baris, kolom = len(A), len(A[0])
    C_skalar = [[A[i][j] * k for j in range(kolom)] for i in range(baris)]
    return C_skalar

C_skalar = kali_matriks(A, 4)
for baris in C_skalar :
    print(baris)

#d.Menampilkan deteminan matriks A dan B menggunakan Metode Sarrus
def determinan_3x3(M):
    # Diagonal utama: dijumlahkan
    d1 = M[0][0] * M[1][1] * M[2][2]
    d2 = M[0][1] * M[1][2] * M[2][0]
    d3 = M[0][2] * M[1][0] * M[2][1]
    # Diagonal sekunder: dikurangkan
    d4 = M[0][2] * M[1][1] * M[2][0]
    d5 = M[0][0] * M[1][2] * M[2][1]
    d6 = M[0][1] * M[1][0] * M[2][2]
    return (d1 + d2 + d3) - (d4 + d5 + d6)

det_A = determinan_3x3(A)
det_B = determinan_3x3(B)

print("Deteminan matriks A:", det_A)
print("Deteminan matriks B:", det_B)

#e.Menampilkan keempat hasil dengan format rapi baris per baris
print("C_tambah:")
for baris in C:
    print(baris)

print("C_kurang:")
for baris in D:
    print(baris)

print("C_skalar:")
for baris in C_skalar:
    print(baris)

print("Deteminan matriks A:", det_A)
print("Deteminan matriks B:", det_B)








#a.Menjumlahkan matriks A dan B, simpan hasilnya dalam variabel C_tambah
C_tambah = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

#b.Mengurangkan matriks A dikurangi B, simpan dalam variabel C_kurang
C_kurang = [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

#c.Mengalikan setiap elemen matriks A dengan skalar k = 4 , simpan dalam C_skalar
C_skalar = [[A[i][j] * 4 for j in range(len(A[0]))] for i in range(len(A))]

#d Hitunglah deteminan matriks A dan B menggunakan Metode Sarrus
det_A = A[0][0] * A[1][1] * A[2][2] + A[0][1] * A[1][2] * A[2][0] + A[0][2] * A[1][0] * A[2][1] - A[0][2] * A[1][1] * A[2][0] - A[0][0] * A[1][2] * A[2][1] - A[0][1] * A[1][0] * A[2][2]
det_B = B[0][0] * B[1][1] * B[2][2] + B[0][1] * B[1][2] * B[2][0] + B[0][2] * B[1][0] * B[2][1] - B[0][2] * B[1][1] * B[2][0] - B[0][0] * B[1][2] * B[2][1] - B[0][1] * B[1][0] * B[2][2]

#e Menampilkan keempat hasil dengan format rapi baris per baris
print("Hasil penjumlahan matriks A dan B:")
for row in C_tambah:
    print(row)

print("\nHasil pengurangan matriks A dikurangi B:")
for row in C_kurang:
    print(row)

print("\nHasil perkalian setiap elemen matriks A dengan skalar k = 4:")
for row in C_skalar:
    print(row)

print("\nDeteminan matriks A:", det_A)
print("Deteminan matriks B:", det_B)
