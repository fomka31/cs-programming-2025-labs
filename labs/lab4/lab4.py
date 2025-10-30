# # Task_1

# temp = int(input('Введите температуру: '))
# if temp >= 20:
#     print('Кондиционер выключается...')
# else:
#     print('Кондиционер включается...')

# # Task_2

# num = int(input('Введите номер месяца: '))
# if num in [1,2,12]:
#     print('Сейчас зима')
# elif num in [3,4,5]:
#     print('Сейчас весна')
# elif num in [6,7,8]:
#     print('Сейчас лeто')
# elif num in [9,10,11]:
#     print('Сейчас осень')
# else:
#     print("Введён неверный номер месяца")

# # Task_3

# dog_age = input()

# try:
#     dog_age = int(dog_age)
#     current_age = dog_age
#     human_age = 0
#     if dog_age > 22 or dog_age < 1:
#         print('Введён некорректный возраст')
#     else:
#         while current_age != 0:
#             if dog_age - current_age < 2:
#                 human_age += 10.5
#             else:
#                 human_age += 4
#             current_age -= 1
#         print(human_age)
# except:
#     print('введено не число')


# #Task 4

# num = int(input())

# def div_by_six(num):
#     last_is_even = True if int(str(num)[-1]) % 2 == 0 else False
#     summ_div_3 = True if sum(int(x) for x in list(str(num))) % 3 == 0 else False
#     return True if (last_is_even and summ_div_3) else False

# print(f'Результат того делиться ли число {num} на 6: {"да" if div_by_six(num) else "нет"}')


# #Task 5

# def check_password(password):  
#     length_ok = len(password) >= 8  
      
#     has_upper = any(char.isupper() for char in password)  
      
#     has_lower = any(char.islower() for char in password)  
      
#     has_digit = any(char.isdigit() for char in password)  
      
#     special_chars = "!@#$%^&*()_+-={}|;:,.<>?/~`"  
#     has_special = any(char in special_chars for char in password)  
      
#     conditions = {  
#         "длина": length_ok,  
#         "заглавные буквы": has_upper,  
#         "строчные буквы": has_lower,  
#         "цифры": has_digit,  
#         "специальные символы": has_special  
#     }  
      
#     if all(conditions.values()):  
#         return "Пароль надежный!"  
#     else:   
#         failed_conditions = [key for key, value in conditions.items() if not value]  
#         return f"Пароль не соответствует требованиям:\n" + "\n".join(f"- Нет {condition}" for condition in failed_conditions)  
  
# password = input("Введите пароль для проверки: ")  
# result = check_password(password)  
# print(result)  

# #Task 6

# def visikos(god):
#     print(f"{god} - {'високосный год' if ((god % 4 == 0 and god % 100 != 0) or god % 400 == 0) else 'не високосный год'}")

# num = int(input('Введите год :'))
# visikos(num)

#Task 7

# a = [int(i) for i in input('Введите 3 числа :' ).split()]
# minimal = a[0]
# for i in a[1:]:
#     minimal = int(i) if int(i) < minimal else minimal
# print(minimal)

#Task 8

# try:
#     num = int(input('Введите сумму покупки: '))
#     if num < 1000:
#         discount = 0
#     elif 1000<=num<5000:
#         discount = 5
#     elif 5000<=num<10000:
#         discount = 10
#     elif num <= 10000:
#         discount = 15
#     print(f'Ваша скидка: {discount}%')
#     print(f'К оплате: {num*((100-discount)/100)}')
# except:
#     print('Неверный ввод')

#Task 9

# try:
#     time = int(input('Введите час (0–23): '))
#     if time in [int(i) for i in range(6)]:
#         print('Сейчас ночь')
#     elif time in [int(i) for i in range(6,12)]:
#         print('Сейчас утро')
#     elif time in [int(i) for i in range(12,18)]:
#         print('Сейчас день')
#     elif time in [int(i) for i in range(18,24)]:
#         print('Сейчас вечер')
#     else:
#         int('s')
# except:
#     print('Неверный ввод')

#Task 10

def is_prime(number):
    if number in [0,2]:
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