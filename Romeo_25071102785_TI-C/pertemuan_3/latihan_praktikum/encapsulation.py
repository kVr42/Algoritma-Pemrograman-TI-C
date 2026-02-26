#encapsulation.py

'''
Getter dan Setter adalah metode yang digunakan untuk mengakses dan memodifikasi atribut privat dalam sebuah kelas.
Getter adalah metode yang digunakan untuk mendapatkan nilai dari atribut privat, sedangkan Setter adalah metode yang digunakan untuk mengubah nilai dari atribut privat.
Dengan menggunakan Getter dan Setter, kita dapat mengontrol akses ke atribut privat dan memastikan bahwa nilai yang diberikan valid.
Contoh:
get_ adalah metode untuk mengambil nilai atribut privat
set_ adalah metode untuk mengubah nilai atribut privat
'''

# Contoh implementasi enkapsulasi dalam Python
# Dalam enkapsulasi, atribut kelas dibuat privat dengan menambahkan dua garis bawah (__) di depan nama atribut.
# Akses ke atribut tersebut dilakukan melalui metode publik (getter dan setter).
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number  # private attribute
        self.__balance = initial_balance        # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

 #open private
    def set_account_number(self, new_account_number):
        self.__account_number = new_account_number
#contoh penggunaan
if __name__ == "__main__":
    account = BankAccount("123456789", 1000)
    account.deposit(500)
    account.withdraw(200)
    print(f"Account Number: {account.get_account_number()}")
    print(f"Balance: {account.get_balance()}")
    account.set_account_number("987654321")
    print(f"Updated Account Number: {account.get_account_number()}")


# Membuat kelas Student dengan atribut privat untuk nilai (grade)
class Student:
  def __init__(self, name):
    self.name = name
    self.__grade = 0

  def set_grade(self, grade):
    if 0 <= grade <= 100:
      self.__grade = grade
    else:
      print("Grade must be between 0 and 100")

  def get_grade(self):
    return self.__grade

  def get_status(self):
    if self.__grade >= 60:
      return "Passed"
    else:
      return "Failed"

student = Student("Emil")
student.set_grade(85)
print(student.get_grade())
print(student.get_status())
