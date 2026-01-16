# items/item_classes.py

class Item:
    def __init__(self, name, item_type="misc", lvl_required=1, clas_required=None):
        self.name = name
        self.item_type = item_type
        self.lvl_required = lvl_required
        self.clas_required = clas_required

    def can_equip(self, hero):
        return (
            hero.lvl >= self.lvl_required and
            (self.clas_required is None or self.clas_required == hero.__class__.__name__)
        )


class HealingPotion(Item):
    def __init__(self, heal_amount, name):
        super().__init__(name, item_type="potion")
        self.heal_amount = heal_amount

    def use(self, hero):
        hero.heal(self.heal_amount)
        print(f"{hero.name} восстановил {self.heal_amount} HP.")


class ManaPotion(Item):
    def __init__(self, mana_amount, name):
        super().__init__(name, item_type="potion")
        self.mana_amount = mana_amount

    def use(self, hero):
        hero.heal_mana(self.mana_amount)
        print(f"{hero.name} восстановил {self.mana_amount} маны.")


class Weapon(Item):
    def __init__(self, name, weapon_type, physical_dmg=0, piercing_dmg=0, magic_dmg=0, **kwargs):
        super().__init__(name, item_type="weapon", **kwargs)
        self.weapon_type = weapon_type
        self.physical_dmg = physical_dmg
        self.piercing_dmg = piercing_dmg
        self.magic_dmg = magic_dmg


class Armor(Item):
    def __init__(self, name, physical_res=0, magic_res=0, **kwargs):
        super().__init__(name, item_type="armor", **kwargs)
        self.physical_res = physical_res
        self.magic_res = magic_res


class Gold(Item):
    def __init__(self, amount):
        super().__init__(f"{amount} золота", item_type="gold")
        self.amount = amount