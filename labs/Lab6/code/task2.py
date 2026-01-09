def calculate_vklad(summa:int,srok:int) -> float:
    if summa <30000:
        return 'Минимальная сумма вклада 30 000 рублей'
    if srok < 1:
        return "Минимальный срок вклада 1 месяц"
    
    bonus = min(summa // 10000 * 0.003, 0.05)
    stavka = 0.03 if srok <=3 else 0.05 if 4<srok<=7 else 0.02
    
    result = summa * (1+stavka+bonus) ** srok - summa
    return f'Прибыль : {result.round(2)}'



x, y = [int(i) for i in input('Введите сумму и срок : ').split()]
print(calculate_vklad(x, y))