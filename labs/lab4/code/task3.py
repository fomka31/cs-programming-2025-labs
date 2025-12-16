# Task_3

dog_age = input()

try:
    dog_age = int(dog_age)
    current_age = dog_age
    human_age = 0
    if dog_age > 22 or dog_age < 1:
        print('Введён некорректный возраст')
    else:
        while current_age != 0:
            if dog_age - current_age < 2:
                human_age += 10.5
            else:
                human_age += 4
            current_age -= 1
        print(human_age)
except:
    print('введено не число')