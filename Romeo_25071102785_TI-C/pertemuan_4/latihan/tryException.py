#try exception

x = -5
try:
  print(x)
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("The 'try except' is finished")

try:
  result = 10 / 0
  print(result)
except ZeroDivisionError:
  print("Tidak dapat membagi dengan nol")


try:
  result = 10 / 0
  print(result)
except ZeroDivisionError:#guananya untuk menangkap error
  print("Tidak dapat membagi dengan nol")
finally:#gunanya untuk menutup program
  print("Program selesai")