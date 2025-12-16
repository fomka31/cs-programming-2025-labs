from logic.mainfunk import main_funk
from characters.heroCreate import *


flag = True
while flag:
    main_funk()
    bigLine()
    print('Веберите действие\nВарианты: инвентарь, статы, чит')
    choice = input()
    match choice.lower():
        case 'инвентарь':
            hero.use_item()
        case 'статы':
            hero.show_stats()
        case 'чит':
            hero.cheat()