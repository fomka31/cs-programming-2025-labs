#Task 9

try:
    time = int(input('Введите час (0–23): '))
    if time in [int(i) for i in range(6)]:
        print('Сейчас ночь')
    elif time in [int(i) for i in range(6,12)]:
        print('Сейчас утро')
    elif time in [int(i) for i in range(12,18)]:
        print('Сейчас день')
    elif time in [int(i) for i in range(18,24)]:
        print('Сейчас вечер')
    else:
        int('s')
except:
    print('Неверный ввод')