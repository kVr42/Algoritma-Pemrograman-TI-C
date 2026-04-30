#towerOfHanoi

def towerOfHanoi(n, awal, target, pending):
    if n == 1:
        print(f"Pindahkan cakram 1 dari {awal} ke {target}")
        return
    towerOfHanoi(n - 1, awal, pending, target)
    print(f"Pindahkan cakram {n} dari {awal} ke {target}")
    towerOfHanoi(n - 1, pending, target, awal)
n = 3
towerOfHanoi(n, 'A', 'C', 'B')
