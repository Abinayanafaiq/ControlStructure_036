n = int(input("Inputkan Batas Print: "))

if n <= 0:
    n = 1

for i in range(1, n + 1):
    print(f'{str(i) * i}')