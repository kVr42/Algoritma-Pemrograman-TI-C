 #for loops
print('for loops')
for i in range(5):
    print('Perulangan ke-', i + 1)
for j in range(1, 6):
    print('Perulangan ke-', j)
for k in range(1, 11, 2):
    print('Perulangan ke-', k)
for l in 'Python':
    print('Huruf:', l)
for m in ['apel', 'pisang', 'cherry']:
    print('Buah:', m)
for n in ('satu', 'dua', 'tiga'):
    print('Angka:', n)
for o in {'nama': 'Andi', 'umur': 20}:
    print('Key:', o, 'Value:', {'nama': 'Andi', 'umur': 20}[o])
for p in range(5):
    if p == 3:
        break
    print('Perulangan ke-', p)
for q in range(5):
    if q == 3:
        continue
    print('Perulangan ke-', q)
for r in range(3):
    for s in range(2):
        print('Perulangan luar ke-', r, 'Perulangan dalam ke-', s)
for t in range(5):
    print('Perulangan ke-', t)
else:
    print('Perulangan selesai.')
for u in range(5):
    if u == 3:
        break
    print('Perulangan ke-', u)
else:
    print('Perulangan selesai.')
for v in range(5):
    if v == 3:
        continue
    print('Perulangan ke-', v)
else:
    print('Perulangan selesai.')
for w in range(1, 6):
    print('Perulangan ke-', w)
for x in range(10, 0, -2):
    print('Perulangan ke-', x)
for y in 'Algoritma':
    print('Huruf:', y)
for z in ['satu', 'dua', 'tiga']:
    print('Angka:', z)
for aa in ('merah', 'hijau', 'biru'):
    print('Warna:', aa)

