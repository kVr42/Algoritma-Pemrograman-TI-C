def mergeSort(arr): 
  if len(arr) <= 1: #jika panjang array kurang dari atau sama dengan 1, maka array tersebut sudah dianggap terurut dan dapat langsung dikembalikan tanpa perlu dilakukan proses pengurutan lebih lanjut.
    return arr

  mid = len(arr) // 2 # untuk menentukan indeks tengah dari array, yang akan digunakan untuk membagi array menjadi dua bagian yang lebih kecil. Dalam proses merge sort, array akan dibagi menjadi dua bagian secara rekursif hingga mencapai ukuran 1 atau 0, yang dianggap sudah terurut.
  leftHalf = arr[:mid] # untuk membuat sub-array yang berisi elemen-elemen dari indeks 0 hingga indeks tengah (mid) dari array asli. Sub-array ini akan digunakan untuk proses pengurutan pada bagian kiri dari array.
  rightHalf = arr[mid:] # untuk membuat sub-array yang berisi elemen-elemen dari indeks tengah (mid) hingga akhir dari array asli. Sub-array ini akan digunakan untuk proses pengurutan pada bagian kanan dari array.

  sortedLeft = mergeSort(leftHalf) # untuk melakukan proses pengurutan secara rekursif pada sub-array bagian kiri (leftHalf) hingga mencapai ukuran 1 atau 0, yang dianggap sudah terurut. Hasil dari proses pengurutan ini akan disimpan dalam variabel sortedLeft.
  sortedRight = mergeSort(rightHalf) # untuk melakukan proses pengurutan secara rekursif pada sub-array bagian kanan (rightHalf) hingga mencapai ukuran 1 atau 0, yang dianggap sudah terurut. Hasil dari proses pengurutan ini akan disimpan dalam variabel sortedRight.

  return merge(sortedLeft, sortedRight) # untuk menggabungkan dua sub-array yang sudah terurut (sortedLeft dan sortedRight) menjadi satu array yang terurut secara keseluruhan. Fungsi merge akan membandingkan elemen-elemen dari kedua sub-array dan menggabungkannya dalam urutan yang benar untuk menghasilkan array yang terurut. Hasil dari proses penggabungan ini akan dikembalikan sebagai output dari fungsi mergeSort.

def merge(left, right): # untuk menggabungkan dua sub-array yang sudah terurut (left dan right) menjadi satu array yang terurut secara keseluruhan. Fungsi ini akan membandingkan elemen-elemen dari kedua sub-array dan menggabungkannya dalam urutan yang benar untuk menghasilkan array yang terurut.
  result = [] # untuk menyimpan hasil penggabungan dari kedua sub-array yang sudah terurut. Array result akan diisi dengan elemen-elemen dari kedua sub-array (left dan right) dalam urutan yang benar untuk menghasilkan array yang terurut secara keseluruhan.
  i = j = 0 # untuk menginisialisasi indeks i dan j yang akan digunakan untuk melacak posisi saat membandingkan elemen-elemen dari kedua sub-array (left dan right). Indeks i akan digunakan untuk melacak posisi dalam sub-array left, sedangkan indeks j akan digunakan untuk melacak posisi dalam sub-array right. Indeks ini akan digunakan untuk membandingkan elemen-elemen dari kedua sub-array dan menggabungkannya dalam urutan yang benar ke dalam array result.

  while i < len(left) and j < len(right): # selama indeks i masih kurang dari panjang sub-array left dan indeks j masih kurang dari panjang sub-array right, maka akan dilakukan perbandingan antara elemen-elemen dari kedua sub-array.
    if left[i] < right[j]: # jika elemen pada posisi i di sub-array left lebih kecil daripada elemen pada posisi j di sub-array right, maka elemen tersebut akan ditambahkan ke dalam array result, dan indeks i akan ditingkatkan untuk melacak posisi berikutnya dalam sub-array left.
      result.append(left[i]) # untuk menambahkan elemen pada posisi i di sub-array left ke dalam array result, karena elemen tersebut lebih kecil daripada elemen pada posisi j di sub-array right. Dengan menambahkan elemen ini ke dalam array result, kita memastikan bahwa elemen-elemen dalam array result tetap terurut secara keseluruhan.
      i += 1 # untuk meningkatkan indeks i setelah menambahkan elemen pada posisi i di sub-array left ke dalam array result. Dengan meningkatkan indeks i, kita akan melacak posisi berikutnya dalam sub-array left untuk dibandingkan dengan elemen-elemen berikutnya di sub-array right pada iterasi selanjutnya dalam proses penggabungan.
    else:
      result.append(right[j]) # untuk menambahkan elemen pada posisi j di sub-array right ke dalam array result, karena elemen tersebut lebih kecil daripada elemen pada posisi i di sub
      j += 1 

  result.extend(left[i:]) # untuk menambahkan sisa elemen-elemen yang belum diproses dari sub-array left ke dalam array result setelah proses perbandingan selesai. Jika masih ada elemen-elemen yang tersisa di sub-array left setelah proses perbandingan, maka elemen-elemen tersebut akan ditambahkan ke dalam array result untuk memastikan bahwa semua elemen dari kedua sub-array (left dan right) termasuk dalam array result yang terurut secara keseluruhan.
  result.extend(right[j:]) # untuk menambahkan sisa elemen-elemen yang belum diproses dari sub-array right ke dalam array result setelah proses perbandingan selesai. Jika masih ada elemen-elemen yang

  return result

mylist = [3, 7, 6, -10, 15, 23.5, 55, -13] 
mysortedlist = mergeSort(mylist) # untuk memanggil fungsi mergeSort dengan argumen mylist, yang berisi array yang ingin diurutkan. Hasil dari proses pengurutan ini akan disimpan dalam variabel mysortedlist, yang akan berisi array yang sudah terurut secara keseluruhan setelah proses merge sort selesai dilakukan pada mylist.
print("Sorted array:", mysortedlist)