'''
#selectio sort
def selectionSort(arr):
  for i in range(len(arr)):
    min_idx = i
    for j in range(i + 1, len(arr)):
      if arr[min_idx] > arr[j]:
        min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
  return arr

#contoh penggunaan
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = selectionSort(arr)
print("Hasil pengurutan:", sorted_arr)
'''

#setiap sekali swapped lakukan print

def selectionSort(arr):
  total_swapped = 0
  for i in range(len(arr)):
    min_idx = i
    for j in range(i + 1, len(arr)):
      if arr[min_idx] > arr[j]:
        min_idx = j
        total_swapped += 1
        print(arr)
        print("Swapped", arr[i], "and", arr[j])
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
  return arr, total_swapped

#contoh penggunaan
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr, total_swapped = selectionSort(arr)
print("Hasil pengurutan:", sorted_arr)
print("Total swapped:", total_swapped)

