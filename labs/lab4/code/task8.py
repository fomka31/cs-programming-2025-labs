#Task 8

try:
    num = int(input('Введите сумму покупки: '))
    discount = 0
    if num < 1000:
        discount = 0
    elif 1000<=num<5000:
        discount = 5
    elif 5000<=num<10000:
        discount = 10
    elif num <= 10000:
        discount = 15
    print(f'Ваша скидка: {discount}%')
    print(f'К оплате: {num*((100-discount)/100)}')
except:
    print('Неверный ввод')