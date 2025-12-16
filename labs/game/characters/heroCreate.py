from .charClasses import *


list_of_classes = ['маг','воин','лучник']


    
while True:
    print('Выберите имя (от 3 до 10 символов) : ')
    name = input()
    if 3 <= len(name) <= 10:
        break
    else:
        print('Неверная длинна имени')
        print('')


while True: 
        print('Выберите класс: Воин Лучник Маг')
        clas = input().lower()
        if clas in list_of_classes:
            break
        else:
            print('Выберите класс их имеющихся')
            print('')

if clas == 'воин':
    hero = Melee(name)
elif clas == 'лучник':
    hero = Ranger(name)
elif clas == 'маг':
    hero = Mage(name)