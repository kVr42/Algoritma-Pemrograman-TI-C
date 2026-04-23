mylist = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", mylist) # Output: Original array: [170, 45, 75, 90, 802, 24, 2, 66]
radixArray = [[], [], [], [], [], [], [], [], [], []] # Output: [[], [], [], [], [], [], [], [], [], []]
maxVal = max(mylist) # untuk menentukan jumlah digit terbesar dalam angka-angka yang akan diurutkan, sehingga kita tahu berapa kali kita perlu melakukan proses pengelompokan berdasarkan digit.
exp = 1 # untuk menentukan digit yang sedang diproses, mulai dari satuan (1), puluhan (10), ratusan (100), dan seterusnya

while maxVal // exp > 0: # untuk melakukan proses pengelompokan sebanyak jumlah digit terbesar dalam angka-angka yang akan diurutkan.

  while len(mylist) > 0: # untuk memindahkan elemen-elemen dari mylist ke bucket yang sesuai berdasarkan digit yang sedang diproses dalam proses pengelompokan.
        val = mylist.pop() # untuk mengambil elemen terakhir dari mylist dan menyimpannya dalam variabel val, kemudian menghapus elemen tersebut dari mylist.
        radixIndex = (val // exp) % 10 # untuk menentukan bucket yang sesuai berdasarkan digit yang sedang diproses dalam proses pengelompokan.
        radixArray[radixIndex].append(val) # untuk menambahkan elemen val ke bucket yang sesuai dalam radixArray berdasarkan digit yang sedang diproses dalam proses pengelompokan.

  for bucket in radixArray: # untuk menggabungkan elemen-elemen dari bucket yang telah diproses dalam proses pengelompokan ke dalam mylist
    while len(bucket) > 0: 
      val = bucket.pop() # untuk mengambil elemen terakhir dari bucket yang telah diproses dalam proses pengelompokan dan menyimpannya dalam variabel val, kemudian menghapus elemen tersebut dari bucket.
      mylist.append(val) # untuk menambahkan elemen val ke dalam mylist setelah diambil dari bucket yang telah diproses dalam proses pengelompokan.

  exp *= 10 # untuk meningkatkan nilai exp dengan faktor 10, sehingga proses pengelompokan akan berlanjut ke digit berikutnya (puluhan, ratusan, dll.) pada iterasi selanjutnya dalam proses pengelompokan.

print(mylist)