pricelist = {'Арбуз': 100,
             'Ананас': 200,
             'Кишмишь': 150,
             'Кунжут': 300}
minimal = min(pricelist.items(),key=lambda x:x[1])
maximal = max(pricelist.items(),key=lambda x:x[1])
print(minimal,maximal)