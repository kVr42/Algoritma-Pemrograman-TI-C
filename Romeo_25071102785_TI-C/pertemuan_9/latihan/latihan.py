'''
Buatlah sebuah program Python yang berjalan di terminal dengan ketentuan sebagai berikut:

Program meminta pengguna untuk memasukkan jumlah elemen yang akan dimasukkan ke dalam array.
Selanjutnya, pengguna memasukkan sejumlah bilangan bulat non-negatif sesuai jumlah yang telah ditentukan, satu per satu.
Setelah semua elemen dimasukkan, program akan mengurutkan array tersebut menggunakan tiga algoritma pengurutan, yaitu Insertion Sort , Quick Sort dan Counting Sort secara terpisah.
Program menampilkan hasil pengurutan dari masing-masing algoritma ke layar terminal.
  -Input yang diterima hanya bilangan bulat non-negatif (≥ 0). Program harus menangani input yang tidak valid.
  -Implementasikan fungsi terpisah untuk Insertion Sort , Quick Sort dan Counting Sort.
  -Tampilkan array sebelum dan sesudah diurutkan untuk setiap algoritma.
'''


#program meminta pengguna untuk memasukkan jumlah elemen yang akan dimasukkan ke dalam array
while True:
    try:
        jumlah_elemen = int(input("Masukkan jumlah elemen yang akan dimasukkan ke dalam array: "))
        if jumlah_elemen < 0:
            print("Jumlah elemen harus berupa bilangan bulat non-negatif. Silakan coba lagi.")
            continue
        break
    except ValueError:
        print("Input tidak valid. Harap masukkan bilangan bulat non-negatif. Silakan coba lagi.")

#program meminta pengguna untuk memasukkan sejumlah bilangan bulat non-negatif sesuai jumlah yang telah ditentukan, satu per satu
elemen = []
for i in range(jumlah_elemen):
    while True:
        try:
            bilangan = int(input(f"Masukkan elemen ke-{i+1}: "))
            if bilangan < 0:
                print("Elemen harus berupa bilangan bulat non-negatif. Silakan coba lagi.")
                continue
            elemen.append(bilangan)
            break
        except ValueError:
            print("Input tidak valid. Harap masukkan bilangan bulat non-negatif. Silakan coba lagi.")



#--------------------------------------------------------------------------------------------------------



#insetion sort
def insertion_sort(arr): #fungsi untuk melakukan insertion sort, arr adalah array yang akan diurutkan
  for i in range(1, len(arr)): #loop melalui array dari index 1 hingga panjang array - 1
    key = arr[i] #key adalah elemen saat ini yang akan diurutkan
    j = i - 1 #j adalah index elemen sebelumnya

    while j >= 0 and arr[j] > key: #loop selama j masih lebih besar atau sama dengan 0 dan elemen pada index j lebih besar dari key
      arr[j + 1] = arr[j] #geser elemen pada index j ke index j + 1
      j -= 1 #decrement/kurangi index j dengan 1

    arr[j + 1] = key #menyisipkan key ke dalam array pada index j + 1

  return arr

#-----------------------------------------------------------------------------

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

#--------------------------------------------------------------------------------

#counting sort
def countingSort(arr):
    if not arr:
        return

    max_val = max(arr) # untuk menentukan ukuran count array

    count = [0] * (max_val + 1) # membuat count array dengan ukuran max_val + 1, diinisialisasi dengan 0

#untuk menghitung jumlah kemunculan setiap elemen dalam arr
    for num in arr:
        count[num] += 1

#untuk membangun kembali arr dengan elemen yang sudah diurutkan berdasarkan count array
    index = 0
    for i in range(len(count)):
        while count[i] > 0: #selama count[i] masih lebih besar dari 0, berarti masih ada elemen i yang belum dimasukkan ke arr
            arr[index] = i 
            index += 1
            count[i] -= 1

    return arr


#====================================================================================



#program menampilkan hasil pengurutan dari masing-masing algoritma ke layar terminal
print("Array sebelum diurutkan:")
print(elemen)

print("\nHasil pengurutan menggunakan Insertion Sort:")
insertion_sort(elemen)
print(elemen)

print("\nHasil pengurutan menggunakan Quick Sort:")
quicksort(elemen)
print(elemen)

print("\nHasil pengurutan menggunakan Counting Sort:")
countingSort(elemen)
print(elemen)