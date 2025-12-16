# Task 7

a = [int(i) for i in input('Введите 3 числа :' ).split()]
minimal = a[0]
for i in a[1:]:
    minimal = int(i) if int(i) < minimal else minimal
print(minimal)