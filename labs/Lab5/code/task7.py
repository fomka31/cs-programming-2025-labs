#Task_7

trans_dict = {
    'apple':'Яблоко',
    'peach':'Груша',
    'ball':'Мяч',
    'snow':'Снег',
    'wood':'Дерево'
}

word = input('Введите слово: ')
try:
    print(f'Перевод слова {word} : {trans_dict[word.lower()]}')
except:
    print(f'Слово {word} отсутсвует в словаре')