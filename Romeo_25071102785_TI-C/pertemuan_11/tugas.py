data = [78, 90, 65, 97, 882, 360, 21, 9, 1, 36, 67, 99, 420, 510, 443, 38, 505, 123, 404, 45, 5, 300, 250, 220, 15, 5, 33, 256, 10, 20, 44, 421, 234, 42, 32, 37, 80, 0, 54, 14, 71, 19, 121, 96, 126, 84, 155, 110, 18, 76, 166, 2, 6, 51, 31, 59, 98, 55, 99, 280, 303, 16, 25, 321]

# Radix Sort
def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)

    for i in range(0, n):
        index = int(arr[i] / exp1)
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = int(arr[i] / exp1)
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1

    for i in range(0, len(arr)):
        arr[i] = output[i]

    return arr

def radixSort(arr):
    max1 = max(arr)

    exp = 1
    while max1 / exp >= 1:
        arr = countingSort(arr, exp)
        exp *= 10

    return arr

# Merge Sort
def merge(arr1, arr2):
    merged = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)

# linear search
def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# binary search
def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

print("Data sebelum diurutkan:", data)
sorted_data_radix = radixSort(data.copy())
sorted_data_merge = mergeSort(data.copy())
print("Data setelah diurutkan menggunakan radix sort:", sorted_data_radix)
print("Data setelah diurutkan menggunakan merge sort:", sorted_data_merge)

target = int(input("Masukkan angka yang ingin dicari: "))
index_radix = linearSearch(sorted_data_radix, target)
index_merge = binarySearch(sorted_data_merge, target)

if index_radix != -1:
    print(f"Angka ditemukan menggunakan linear search pada radix sort di index {index_radix} dengan nilai {sorted_data_radix[index_radix]}")
else:    print("Angka tidak ditemukan menggunakan linear search pada radix sort.")

if index_merge != -1:
    print(f"Angka ditemukan menggunakan binary search pada merge sort di index {index_merge} dengan nilai {sorted_data_merge[index_merge]}")
else:    print("Angka tidak ditemukan menggunakan binary search pada merge sort.")