#task_1

lst = [2,5,6,9,8,4,5,3,4,6]
print(*map(lambda x: int(str(x).replace('3','30')), lst))