#Task_10

stud_list = [("Анна", [5, 4, 5]), ("Иван", [3, 4, 4]), ("Мария", [5, 5, 5])]

stud_dict = dict()

for x,y in stud_list:
    stud_dict[x] = (sum(i for i in y) / len(y)).__round__(3)

prime_char = sorted(stud_dict, key=lambda x : x[1])[0]
print(f'Лучший ученик : {prime_char}, его(её) средний балл : {stud_dict[prime_char]}')