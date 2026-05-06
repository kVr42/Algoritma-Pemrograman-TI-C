# Tugas Praktikum 12 - Struktur Data
# Binary Search Tree (BST) - Sistem Katalog Perpustakaan "Ilmu Terang"

class Node:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None

# Class BinarySearchTree untuk mengelola koleksi buku
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Menambahkan data buku
    def menambahkan(self, id_buku, judul):
        new_node = Node(id_buku, judul)

        # Jika root kosong
        if self.root is None:
            self.root = new_node
            print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current, new_node):
        # Masuk ke kiri
        if new_node.id_buku < current.id_buku:
            if current.left is None:
                current.left = new_node
                print(f"[INSERT] Berhasil memasukkan: ID {new_node.id_buku} - {new_node.judul}")
            else:
                self._insert_recursive(current.left, new_node)

        # Masuk ke kanan
        elif new_node.id_buku > current.id_buku:
            if current.right is None:
                current.right = new_node
                print(f"[INSERT] Berhasil memasukkan: ID {new_node.id_buku} - {new_node.judul}")
            else:
                self._insert_recursive(current.right, new_node)

        # Jika ID sama
        else:
            print(f"[WARNING] ID {new_node.id_buku} sudah ada dalam katalog.")

    # Mencari data buku
    def mencari(self, id_buku):
        return self._search_recursive(self.root, id_buku)

    def _search_recursive(self, current, id_buku):
        if current is None:
            return None

        if id_buku == current.id_buku:
            return current

        elif id_buku < current.id_buku:
            return self._search_recursive(current.left, id_buku)

        else:
            return self._search_recursive(current.right, id_buku)

    # Traversal InOrder
    def traversal_inorder(self):
        print("\n[INFO] Koleksi Buku :")
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, current):
        if current is not None:
            self._inorder_recursive(current.left)
            print(f"{current.id_buku} - {current.judul}")
            self._inorder_recursive(current.right)

    # mendapatkan ID terkecil
    def get_min(self):
        current = self.root

        if current is None:
            return None

        while current.left is not None:
            current = current.left

        return current

    # mendapatkan ID terbesar
    def get_max(self):
        current = self.root

        if current is None:
            return None

        while current.right is not None:
            current = current.right

        return current

    # menghitung height tree
    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, current):
        if current is None:
            return -1

        left_height = self._height_recursive(current.left)
        right_height = self._height_recursive(current.right)

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1


# Program Utama
print("SISTEM KATALOG PERPUSTAKAAN 'ILMU TERANG'")
print("=========================================")

# Membuat instance Binary Search Tree
katalog = BinarySearchTree()

#  data buku
katalog.menambahkan(50, "Dasar Pemrograman")
katalog.menambahkan(30, "Struktur Data")
katalog.menambahkan(70, "Kecerdasan Buatan")
katalog.menambahkan(20, "Matematika Dasar")
katalog.menambahkan(40, "Basis Data")
katalog.menambahkan(60, "Jaringan Komputer")
katalog.menambahkan(80, "Sistem Operasi")
katalog.menambahkan(100, "sejarah geosentrisme")

# Traversal InOrder
katalog.traversal_inorder()

# Search data
print("\n[SEARCH] Mencari ID 60...")
hasil = katalog.mencari(60)

if hasil:
    print(f"Ditemukan! Judul: {hasil.judul}")
else:
    print("Data tidak ditemukan.")

print("\n[SEARCH] Mencari ID 100...")
hasil = katalog.mencari(100)

if hasil:
    print(f"Ditemukan! Judul: {hasil.judul}")
else:
    print("Data tidak ditemukan.")

# Statistik
min_buku = katalog.get_min()
max_buku = katalog.get_max()

print(f"\n[STATISTIK] ID Terkecil: {min_buku.id_buku} - {min_buku.judul}")
print(f"[STATISTIK] ID Terbesar: {max_buku.id_buku} - {max_buku.judul}")

# Height
print(f"\n[INFO] Height Tree: {katalog.height()}")

print("=========================================")
print("Simulasi Selesai!")