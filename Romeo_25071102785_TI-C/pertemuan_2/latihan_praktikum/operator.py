#python operator
print('python operator')

sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)
print('hasil penjumlahan:', sum1)
print('hasil penjumlahan:', sum2)
print('hasil penjumlahan:', sum3)

diff1 = 100 - 50      # 50 (100 - 50)
diff2 = diff1 - 25    # 25 (50 - 25)
print('hasil pengurangan:', diff1)
print('hasil pengurangan:', diff2)

'''

'''
#operator aritmatika
print('operator aritmatika')

x = 15
y = 4

print('hasil penjumlahan:', x + y)
print('hasil pengurangan:', x - y)
print('hasil perkalian:', x * y)
print('hasil pembagian:', x / y)
print('hasil modulus:', x % y)
print('hasil pangkat:', x ** y)
print('hasil pembagian bulat:', x // y)


#operator penugasan
print('operator penugasan')

a = 10
a += 5
print('hasil penugasan penjumlahan:', a)
a -= 3
print('hasil penugasan pengurangan:', a)
a *= 2
print('hasil penugasan perkalian:', a)
a /= 4
print('hasil penugasan pembagian:', a)
a %= 3
print('hasil penugasan modulus:', a)
a **= 2
print('hasil penugasan pangkat:', a)
a //= 2
print('hasil penugasan pembagian bulat:', a)

#operator perbandingan
print('operator perbandingan')

b = 10
c = 5
print('hasil perbandingan b == c:', b == c)
print('hasil perbandingan b != c:', b != c)
print('hasil perbandingan b > c:', b > c)
print('hasil perbandingan b < c:', b < c)
print('hasil perbandingan b >= c:', b >= c)
print('hasil perbandingan b <= c:', b <= c)

#operator logika
print('operator logika')

d = True
e = False
print('hasil logika d and e:', d and e)
print('hasil logika d or e:', d or e)
print('hasil logika not d:', not d)
print('hasil logika not e:', not e)


#operator identitas
print('operator identitas')

f = [1, 2, 3]
g = f
print('hasil identitas f is g:', f is g)
print('hasil identitas f is not g:', f is not g)
h = [1, 2, 3]
print('hasil identitas f is h:', f is h)
print('hasil identitas f is not h:', f is not h)

#operator keanggotaan
i = [1, 2, 3]
print(1 in i)
print(4 in i)
print(1 not in i)
print(4 not in i)

#operator bitwise
print('operator bitwise')

j = 5  # 0101 dalam biner
k = 3  # 0011 dalam biner
print('hasil bitwise j & k:', j & k)  # AND
print('hasil bitwise j | k:', j | k)  # OR
print('hasil bitwise j ^ k:', j ^ k)  # XOR
print('hasil bitwise ~j:', ~j)     # NOT
print('hasil bitwise j << 1:', j << 1) # Shift kiri
print('hasil bitwise j >> 1:', j >> 1) # Shift kanan

