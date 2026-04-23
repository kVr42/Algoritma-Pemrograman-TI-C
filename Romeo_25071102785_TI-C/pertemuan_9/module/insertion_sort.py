'''
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)#masukan jumlah elemen dalam list ke variabel n
for i in range(1,n):#mulai dari elemen kedua (index 1) hingga akhir list
  insert_index = i#inisialisasi insert_index dengan nilai i
  current_value = mylist.pop(i)#menghapus elemen pada index i dan menyimpannya dalam current_value
  for j in range(i-1, -1, -1):#mulai dari index i-1 hingga index 0, dengan langkah -1 (mundur)
    if mylist[j] > current_value:#jika elemen pada index j lebih besar dari current_value
      insert_index = j#update insert_index dengan nilai j
  mylist.insert(insert_index, current_value)#menyisipkan current_value ke dalam mylist pada posisi insert_index

print(mylist)

#print proses pengurutan
mylist = [64, 34, 25, 12, 22, 11, 90, 5]
for i in range(1, len(mylist)):
  insert_index = i
  current_value = mylist.pop(i)
  for j in range(i-1, -1, -1):
    if mylist[j] > current_value:
      insert_index = j
  mylist.insert(insert_index, current_value)
  print(mylist)
'''



mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist) #masukan jumlah elemen dalam list ke variabel n
for i in range(1,n): #mulai dari elemen kedua (index 1) hingga akhir list
  insert_index = i #inisialisasi insert_index dengan nilai i
  current_value = mylist[i] #mengambil elemen pada index i dan menyimpannya dalam current_value
  for j in range(i-1, -1, -1): #mulai dari index i-1 hingga index 0, dengan langkah -1 (mundur)
     if mylist[j] > current_value: #jika elemen pada index j lebih besar dari current_value
       mylist[j+1] = mylist[j] #geser elemen pada index j ke kanan (index j+1)
       insert_index = j #update insert_index dengan nilai j
     else: #jika elemen pada index j lebih kecil atau sama dengan current_value
       break #keluar dari loop jika sudah menemukan posisi yang tepat untuk current_value
  mylist[insert_index] = current_value #menyisipkan current_value ke dalam mylist pada posisi insert_index

print(mylist)
