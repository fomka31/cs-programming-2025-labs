num = int(input())
summ_div_3 = True if sum(int(x) for x in list(str(num))) % 3 == 0 else False
print(summ_div_3)