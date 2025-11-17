#Task 10

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

try:
    num = int(input('Введите число: ')) 
    res = is_prime(num)
    print(f'{num} - {"простое число" if res else "составное число"}')
except ValueError:   
    print('Неверный ввод')