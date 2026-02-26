
'''
Buatlah sebuah class bernama Vehicle yang memiliki tiga atribut, yaitu jenis, merk, dan tahun_rilis. Kelas ini juga harus memiliki sebuah method bernama sound() yang mengembalikan string "suara".
Selanjutnya, buatlah dua class turunan (child class) yang mewarisi class Vehicle. Kedua class tersebut harus merepresentasikan jenis kendaraan (bebas, misalnya mobil, motor, dan lain-lain). Setiap class turunan wajib memiliki satu atribut private (menggunakan konvensi private di Python).
Terakhir, buat dan panggil tiga objek dalam program, yaitu satu objek dari class Vehicle dan masing-masing satu objek dari kedua class turunan tersebut.
setidaknya masing-masing class ada getter atau setter.
'''

class Vehicle:
    def __init__(self, jenis, merk, tahun_rilis):
          self.jenis = jenis
          self.merk = merk
          self.tahun_rilis = tahun_rilis

    def sound(self):
          return "suara not exist"

    def get_merk(self):
          return self.merk

    def set_tahun_rilis(self, tahun):
          self.tahun_rilis = tahun


# Child Class 1
class Mobil(Vehicle):
    def __init__(self, jenis, merk, tahun_rilis, jumlah_pintu):
        super().__init__(jenis, merk, tahun_rilis)
        self.__jumlah_pintu = jumlah_pintu

    # Getter untuk atribut private
    def get_jumlah_pintu(self):
        return self.__jumlah_pintu
    
    # Setter untuk atribut private
    def set_jumlah_pintu(self, jumlah):
        self.__jumlah_pintu = jumlah


# Child Class 2
class Motor(Vehicle):
    def __init__(self, jenis, merk, tahun_rilis, tipe_mesin):
        super().__init__(jenis, merk, tahun_rilis)
        self.__tipe_mesin = tipe_mesin

    def get_tipe_mesin(self):
        return self.__tipe_mesin

    def set_tipe_mesin(self, tipe):
        self.__tipe_mesin = tipe

# Membuat Objek
kendaraan_umum = Vehicle("Kendaraan Umum", "Generic", 2020)
mobil = Mobil("Mobil", "Toyota", 2022, 4)
motor = Motor("Motor", "Honda", 2021, "150cc")


print("Vehicle:", kendaraan_umum.get_merk(),"-", kendaraan_umum.sound())

print("Mobil:", mobil.get_merk(),
      "| Pintu:", mobil.get_jumlah_pintu(),
      "| Sound:", mobil.sound())

print("Motor:", motor.get_merk(),
      "| Tipe Mesin:", motor.get_tipe_mesin(),
      "| Sound:", motor.sound())
