# Task_1

age = input('Введите возраст: ')
name = input('Введите имя: ')
for i in range(10):
    print(f"Меня зовут {name} и мне {age} лет.")

# Task_2

num = int(input('Введите число: '))
print(f"\nТаблица умножения для числа {num}:")  
for i in range(1, 11):  
    print(f"{num} × {i} = {num * i}")

# Task_3

gen = [i for i in range(100) if i % 3 == 2]
print(gen)

# Task_4

fact = 1
num = int(input('Введите число: '))
for i in range(1, num + 1):
    fact *= i
print(f'Факториал числа {num} равен {fact}')

# Task_5

i = 20
while i >= 0:
    print(i)
    i-=1

# Task_6

num = int(input('Введите число: '))
a, b = 0, 1
while num >= a:
    print(a)
    a, b = b, a+b

# Task_7

text = input()
new_text = ''
for i in range(len(text)):
    new_text += text[i]
    new_text += str(i + 1)
print(new_text)

# Task_8

flag = True

while flag:
    try:
        a, b = input().split(' ')
        print(f'Сумма равна: {int(a)+int(b)}')
    except:
        print('Вводи нормально')
        flag = False