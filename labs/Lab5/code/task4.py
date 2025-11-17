tpl = (1,5,4,"6",True)
if all(x for x in tpl if type(x) == 'int'):
    tpl = sorted(tpl)
else:
    pass
print(tpl)