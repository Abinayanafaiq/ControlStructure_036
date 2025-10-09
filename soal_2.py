a = float(input('First Number: '))
b = float(input('Second Number: '))
c = float(input('Third Number: '))

if a > b and a > c :
    largest = a
elif b > a and b > c:
    largest = b
elif c > a and c > b:
    largest = c
else: 
    largest = "Tidak ada yang lebih besar"


print(f"the largest number is {largest}")