# characters/enemy.py

from .char_classes import Entity

class Enemy(Entity):
    def __init__(self, name, lvl, hp, physical_dmg=10):
        super().__init__()
        self.name = name
        self.lvl = lvl
        self.max_hp = hp
        self.current_hp = hp
        self.base_physical_dmg = physical_dmg
        self.evade_chance = 0.05