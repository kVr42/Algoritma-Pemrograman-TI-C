#counting sort

def countingSort(arr): #fungsi counting sort, arr adalah array yang akan diurutkan
  max_val = max(arr) #cari nilai maksimum dalam array untuk menentukan ukuran count array
  count = [0] * (max_val + 1) #buat count array dengan ukuran max_val + 1, inisialisasi dengan 0

  while len(arr) > 0: #selama masih ada elemen dalam arr
    num = arr.pop(0) #ambil elemen pertama dari arr dan simpan dalam num
    count[num] += 1 #increment count pada index num untuk menghitung frekuensi kemunculan num dalam arr

  for i in range(len(count)): #loop melalui count array untuk membangun kembali arr yang sudah diurutkan
    while count[i] > 0: #selama count pada index i masih lebih besar dari 0, berarti masih ada elemen dengan nilai i yang belum ditambahkan ke arr
      arr.append(i) #tambahkan nilai i ke arr
      count[i] -= 1 #decrement count pada index i setelah menambahkan nilai i ke arr

  return arr 

mylist = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
mysortedlist = countingSort(mylist)
print(mysortedlist)
