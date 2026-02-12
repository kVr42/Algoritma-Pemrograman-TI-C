#match.
print('match statement')
nilai = 85
match nilai:
    case 100:
        print("Nilai sempurna!")
    case 85:
        print("Nilai sangat baik!")
    case 70:
        print("Nilai baik!")
    case 60:
        print("Nilai cukup!")
    case _:
        print("Nilai kurang!")


