#Task_9

lst = ["яблоко", "груша", "банан", "киви", "апельсин", "ананас",'киви']

letter_dict = dict()

for x in lst:
    letter = x[0]
    if letter not in letter_dict.keys():
        letter_dict[letter] = []
    letter_dict[letter].append(x)

print(letter_dict)