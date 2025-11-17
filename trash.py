def help(x):
    min1=min(x, key=x.get)
    max1=max(x, key=x.get)
    return min1, max1

products={"apple":100,"banana":80,"orange":120,"grape":90}
print(help(products))