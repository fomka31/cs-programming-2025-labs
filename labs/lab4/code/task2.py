# Task_2

num = int(input('Введите номер месяца: '))
if num in [1,2,12]:
    print('Сейчас зима')
elif num in [3,4,5]:
    print('Сейчас весна')
elif num in [6,7,8]:
    print('Сейчас лeто')
elif num in [9,10,11]:
    print('Сейчас осень')
else:
    print("Введён неверный номер месяца")