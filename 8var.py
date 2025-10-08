# value = input().split()
# x,y,z = [i == '1' for i in value]
# print(f'            {'_' if not x else ' '}     {'_' if not y else ' '}     {'_' if not z else ' '}')
# print(f'Результат : x and y and z')


num = int(input())
res = ('0' * (8 - len(bin(num)[2:]))) + bin(num)[2:]
print(f'Двоичный вектор десятичного числа {num} : {res}')
cnt = 0
full_res = ''
print(f'| x | y | z | f |')
for i in range(2):
    for j in range(2):
        for k in range(2):
            current_form = f'({'x' if i else '¬x'} ∧ {'y' if j else '¬y'} ∧ {'z' if k else '¬z'})'
            print(f"| {i} | {j} | {k} | {res[cnt]} | {current_form if bool(int(res[cnt])) else ''}")
            full_res += current_form if bool(int(res[cnt])) else ''
            full_res += 'V' if bool(int(res[cnt])) else ''
            cnt += 1

full_res = full_res[:-1] if full_res[-1:] == 'V' else full_res
print(f'Результат равен : {full_res}')