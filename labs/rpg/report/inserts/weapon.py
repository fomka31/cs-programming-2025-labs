class Weapon(Item):
    def __init__(self, name, weapon_type, physical_dmg=0, piercing_dmg=0, magic_dmg=0, **kwargs):
        super().__init__(name, item_type="weapon", **kwargs)
        self.weapon_type = weapon_type
        self.physical_dmg = physical_dmg
        self.piercing_dmg = piercing_dmg
        self.magic_dmg = magic_dmg