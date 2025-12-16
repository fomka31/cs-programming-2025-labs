from Items.itemsClasses import *

#WEAPONS


##MELEE
sword = melee_weapon('меч',1,'воин',10,5,5,15)

##PIERCING
bow = range_weapon('лук',1,'лучник',5,10,5,10)

##MAGIC
staff = magic_weapon('посох',1,'маг',0,5,10,15)

#POTION


##HEAL
small_heal = HealingPotion(50,item_name='Малое зелье лечения')
medium_heal = HealingPotion(100,item_name='Среднее лечебное залье')
big_heal = HealingPotion(150,item_name='Большое лечебное залье')
greater_heal = HealingPotion(200,item_name='Великое лечебное залье')

##MANA
small_mana = ManaPotion(50,item_name='Малое зелье маны')
medium_mana = ManaPotion(100,item_name='Среднее зелье маны')
big_mana = ManaPotion(150,item_name='Большое зелье маны')
greater_mana = ManaPotion(200,item_name='Великое зелье маны')