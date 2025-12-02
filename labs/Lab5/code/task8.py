#Task_8
import random

rules = {
    'ножницы' : ['бумага','ящерица'],
    'бумага' : ['спок','камень'],
    'камень' : ['ножницы', 'ящерица'],
    'ящерица' : ['спок','бумага'],
    'спок' : ['камень','ножницы']
}


choices = [x for x in rules.keys()]

def print_choices():
    global ai_choice
    global player_choice
    print(f"Выбор ии : {ai_choice}")
    print(f'Выбор игрока : {player_choice}')

ai_choice = random.choice(choices)

print('Список знаков')
for i in choices:
    print(i.capitalize())
player_choice = input('Выберите знак : ')

try:
    if player_choice not in choices: raise

    if player_choice in rules[ai_choice]:
        print_choices()
        print("Ты проиграл")

    elif ai_choice in rules[player_choice]:
        print_choices()
        print('Ты победил')
    else:
       print_choices()
       print('Ничья')
except:
    print('Неверный знак')