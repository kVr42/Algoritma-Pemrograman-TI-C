'''
Soal Latihan: Bubble Sort & Selection Sort
Tingkat: Menengah | Waktu: ≤ 40 menit

Soal
Diberikan list berikut:

python data = [ 290, 1012, 731, 801, 992, 1395, 367, 519, 795, 1385, 274, 154, 219, 1410, 83, 589, 553, 362, 594, 851, 173,657, 581, 397, 543, 791, 226, 81, 1459, 126, 941, 491, 1207, 1093,
1473, 951, 267, 1371, 864, 953, 1119, 212, 1266,120, 723, 643, 205, 130, 9, 16, 1053, 507, 1381, 1122, 1323, 758, 713, 1219, 375, 951, 98, 1011, 642, 1099, 1098, 453, 7, 1137, 53, 1352, 553,
380, 1324, 473, 519, 923, 13, 592, 10, 546, 65, 1440, 1002, 1444, 510, 1266, 901, 1444, 691, 650, 373, 896, 681, 916, 943, 323, 783, 1385, 891, 621, 687, 1384, 268, 211, 708, 1067, 736, 1223,
990, 1145, 448, 731, 486, 381, 1441, 312, 181, 785, 157, 793, 1029, 1273, 846, 1473, 57, 785, 588, 582, 920, 808, 644, 1182, 1101, 579, 623, 556, 858, 59, 163, 1236, 310, 1308, 962, 356, 1005,
883, 582, 786, 958, 321]

Kerjakan semua poin di bawah ini:

1. Implementasikan Bubble Sort untuk mengurutkan data dari kecil ke besar. Gunakan versi yang dioptimasi dengan flag swapped agar algoritma berhenti lebih awal jika array sudah terurut.

2. Implementasikan Selection Sort untuk mengurutkan data dari besar ke kecil.

3. Hitung berapa kali pertukaran (swap) terjadi pada masing-masing algoritma. Tampilkan jumlahnya.

4. Jalankan kedua algoritma pada list data yang sama persis (jangan gunakan hasil sort sebelumnya sebagai input).

---

Output yang Diharapkan
```
Bubble Sort (kecil → besar): 
Jumlah swap Bubble Sort: ...

Selection Sort (besar → kecil): 
Jumlah swap Selection Sort: ...
```

---

### Batasan
Dilarang menggunakan sort(), sorted(), atau library sorting bawaan Python.
Kedua fungsi harus dibuat dalam bentuk function masing-masing.
'''

data = [290, 1012, 731, 801, 992, 1395, 367, 519, 795, 1385, 274, 154, 219, 1410, 83, 589, 553, 362, 594, 851, 173,
657, 581, 397, 543, 791, 226, 81, 1459, 126, 941, 491, 1207, 1093, 1473, 951, 267, 1371, 864, 953, 1119, 212, 1266,
120, 723, 643, 205, 130, 9, 16, 1053, 507, 1381, 1122, 1323, 758, 713, 1219, 375, 951, 98, 1011, 642, 1099, 1098, 453,
7, 1137, 53, 1352, 553, 380, 1324, 473, 519, 923, 13, 592, 10, 546, 65, 1440, 1002, 1444, 510, 1266, 901, 1444, 691,
650, 373, 896, 681, 916, 943, 323, 783, 1385, 891, 621, 687, 1384, 268, 211, 708, 1067, 736, 1223, 990, 1145, 448, 731,
486, 381, 1441, 312, 181, 785, 157, 793, 1029, 1273, 846, 1473, 57, 785, 588, 582, 920, 808, 644, 1182, 1101, 579,
623, 556, 858, 59, 163, 1236, 310, 1308, 962, 356, 1005, 883, 582, 786, 958, 321]


def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    jumlah_swap = 0

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                jumlah_swap += 1
                swapped = True

        if not swapped:
            break

    return arr, jumlah_swap


def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)
    jumlah_swap = 0

    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j

        if max_index != i:
            arr[i], arr[max_index] = arr[max_index], arr[i]
            jumlah_swap += 1

    return arr, jumlah_swap


bubble_sorted, bubble_swaps = bubble_sort(data)
selection_sorted, selection_swaps = selection_sort(data)

print("Bubble Sort (kecil → besar):")
print(bubble_sorted)
print("Jumlah swap Bubble Sort:", bubble_swaps)

print("\nSelection Sort (besar → kecil):")
print(selection_sorted)
print("Jumlah swap Selection Sort:", selection_swaps)