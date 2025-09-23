# Task_1

a = 1
b = 'a'
c = 1.1
d = True

# Task_2

name = "Fedor"
age = 19

print(name, age)

# Task_3

first = 342
second = 56.2
third = '43'

result = first + second + int(third)
print(result)

# Task_4

a = 3
b = 8
result = (a + 4 * b) * (a - 3 * b) + a ** 2
print(result)

# Task_5

# lenth = int(input('Введите длинну '))
# width = int(input('Введите ширину '))
#
# P = 2 * (lenth + width)
# S = lenth * width
#
# print('Периметр равен ', P)
# print('Площадь равна ', S)

# Task_6

print("*   *   *\n"
      " * * * * \n"
      "  *   * ")

# Task_7

uno = 1
des = 2

print(uno > des)
print(uno < des)
print(uno == des)
print(uno >= des)
print(uno <= des)
print(uno != des)

print(uno + des)
print(uno - des)
print(uno * des)
print(uno / des)
print(uno ** des)
print(uno // des)
print(uno % des)

# Task_8

name = "Федя"
age = 19
print(f'Меня зовут {name}, мне {age} лет.')

# Task_9

a = 'Съешь ещё '
b = 'этих мягких '
c = 'французских булок, '
d = 'да выпей '
e = 'чаю.'

print(a + b + c + d + e)

# Task_10

text = 'Нет! Да! '
print(text * 4)

# Task_11

a, b, c = input().split(',')

result = (int(a)+int(c)) // int(b)
print('Результат вычисления : ', result)

#Task_12

# text = input()
text = 'abcdefghij'
print(text)
print(text[:4])
print(text[-2:])
print(text[4:8])
print(text[::-1])