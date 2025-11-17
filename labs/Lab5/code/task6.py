#Tack_6

lst = [11, 'kfl', True, 5.5, 'dawd','dcvf', [1,2], None]
dct = dict()
for i in lst:
    try:
        dct[i] = i
    except:
        pass
print(dct)