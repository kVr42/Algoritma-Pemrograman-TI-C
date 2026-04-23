
#quick sort

def partition(array, low, high): #fungsi partision
  pivot = array[high] #pivot adalah elemen terakhir
  i = low - 1 #index elemen yang lebih kecil dari pivot atau sama dengan pivot

  for j in range(low, high): #loop dari index low hingga high-1
     if array[j] <= pivot: #jika elemen saat ini lebih kecil atau sama dengan pivot
       i += 1 #increment index elemen yang lebih kecil
       array[i], array[j] = array[j], array[i] #tukar elemen pada index i dengan elemen pada index j

  array[i+1], array[high] = array[high], array[i+1] #tukar elemen pada index i+1 dengan elemen pada index high (pivot)
  return i+1 #kembalikan index pivot setelah partision

def quicksort(array, low=0, high=None): #fungsi utama untuk melakukan quicksort, low adalah index awal, high adalah index akhir
  if high is None: #jika high tidak diberikan, maka set high ke index terakhir dari array
    high = len(array) - 1 #index terakhir dari array adalah panjang array - 1

  if low < high: #jika index awal lebih kecil dari index akhir
    pivot_index = partition(array, low, high) #partision array dan dapatkan index pivot
    quicksort(array, low, pivot_index-1) #rekursif untuk subarray yang lebih kecil dari pivot
    quicksort(array, pivot_index+1, high) #rekursif untuk subarray yang lebih besar dari pivot

mylist = [64, 34, 25, 5, 22, 11, 90, 12]
quicksort(mylist) #panggil fungsi quicksort untuk mengurutkan mylist
print(mylist)

