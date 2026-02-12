'''
1. penambahan(a, b)
• Mengembalikan hasil penjumlahan dua bilangan.

2. pengurangan(a, b)
• Mengembalikan hasil pengurangan dua bilangan.

3. perkalian(a, b)
• Mengembalikan hasil perkalian dua bilangan.

4. pembagian(a, b)
• Mengembalikan hasil pembagian dua bilangan.
   • Jika b = 0, tampilkan pesan error:
     "Pembagian tidak dapat dilakukan karena pembagi bernilai 0".

5. modulus(a, b)
• Mengembalikan sisa hasil bagi dua bilangan.

6. fibonacci(n)
• Mengembalikan deret Fibonacci sebanyak n angka pertama.
   Contoh:
   Jika n = 5
   Output: [0, 1, 1, 2, 3]

--------------------------------------------------
CATATAN:
• Semua fungsi harus berada di dalam file myMath.py.
• Fungsi harus menggunakan return, bukan hanya print()
'''
#no 1
a=10
b=5
def penambahan(a, b):
    return a + b
print(penambahan(a, b))


#no 2
def pengurangan(a, b):
    return a - b
print(pengurangan(a, b))

#no 3
def perkalian(a, b):
    return a * b
print(perkalian(a, b))

#no 4
def pembagian(a, b):
    if b == 0:
        return 
    return a / b
print(pembagian(a, b))

#no 5
def modulus(a, b):
    return a % b
print(modulus(a, b))

#no 6

def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
print(fibonacci(5))
