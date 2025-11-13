#Task 10

def is_prime(number):
    if number in [0,1, 2]:
        return False
    for i in range(2, number):
        if number%i == 0:
            return False
    return True

try:
    num = int(input('Введите число: ')) 
    res = is_prime(num)
    print(f'{num} - {'простое число' if res else 'составное число'}')
except ValueError:   
    print('Неверный ввод')