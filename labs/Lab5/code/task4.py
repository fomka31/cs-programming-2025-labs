tpl = (1,5,4,6,2,8)
tpl1= ''.join(map(str,tpl))
tpl = sorted(tpl) if tpl1.isdigit() else tpl
print(tpl)