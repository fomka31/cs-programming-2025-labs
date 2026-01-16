# items/item_list.py

from .item_classes import Weapon, Armor, HealingPotion, ManaPotion, Gold

# Стартовое снаряжение
starter_sword = Weapon("Ржавый меч", "melee", physical_dmg=8, lvl_required=1, clas_required="Melee")
starter_bow = Weapon("Простой лук", "ranged", piercing_dmg=10, lvl_required=1, clas_required="Ranger")
starter_staff = Weapon("Деревянный посох", "magic", magic_dmg=14, lvl_required=1, clas_required="Mage")
starter_armor = Armor("Тканевая одежда", physical_res=2, magic_res=1, lvl_required=1)

# Лучшее снаряжение
iron_sword = Weapon("Железный меч", "melee", physical_dmg=15, lvl_required=2, clas_required="Melee")
hunting_bow = Weapon("Охотничий лук", "ranged", piercing_dmg=16, lvl_required=2, clas_required="Ranger")
mage_staff = Weapon("Посох мага", "magic", magic_dmg=22, lvl_required=2, clas_required="Mage")
leather_armor = Armor("Кожаная броня", physical_res=5, magic_res=1, lvl_required=1)
chain_mail = Armor("Кольчуга", physical_res=9, magic_res=2, lvl_required=3)

# Зелья
small_heal = HealingPotion(50, "Малое зелье лечения")
big_heal = HealingPotion(150, "Большое зелье лечения")
small_mana = ManaPotion(50, "Малое зелье маны")
big_mana = ManaPotion(150, "Большое зелье маны")

# Золото
gold_20 = Gold(20)
gold_50 = Gold(50)
gold_100 = Gold(100)

# Все предметы для сундуков
CHEST_LOOT = [
    iron_sword, hunting_bow, mage_staff,
    leather_armor, chain_mail,
    small_heal, big_heal,
    small_mana, big_mana,
    gold_20, gold_50, gold_100
]