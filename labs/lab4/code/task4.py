#Task 4

num = int(input())

def div_by_six(num):
    last_is_even = True if int(str(num)[-1]) % 2 == 0 else False
    summ_div_3 = True if sum(int(x) for x in list(str(num))) % 3 == 0 else False
    return True if (last_is_even and summ_div_3) else False

print(f'Результат того делиться ли число {num} на 6: {"да" if div_by_six(num) else "нет"}')