#Task 6

def visikos(god):
    print(f"{god} - {'високосный год' if ((god % 4 == 0 and god % 100 != 0) or god % 400 == 0) else 'не високосный год'}")

num = int(input('Введите год :'))
visikos(num)