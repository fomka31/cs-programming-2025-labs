# characters/hero_create.py

from characters.char_classes import Melee, Ranger, Mage

AVAILABLE_CLASSES = {
    'воин': Melee,
    'лучник': Ranger,
    'маг': Mage
}

def create_hero():
    while True:
        name = input('Введите имя героя (от 3 до 10 символов): ').strip()
        if 3 <= len(name) <= 10:
            break
        print('Имя должно содержать от 3 до 10 символов.\n')

    while True:
        print('\nДоступные классы: Воин, Лучник, Маг')
        clas_input = input('Выберите класс: ').strip().lower()
        if not clas_input:
            print('Пожалуйста, введите название класса.\n')
            continue
        if clas_input in AVAILABLE_CLASSES:
            hero_class = AVAILABLE_CLASSES[clas_input]
            break
        print('Такого класса нет. Попробуйте снова.\n')

    hero = hero_class(name)
    print(f'\nГерой {hero.name} создан!')
    return hero