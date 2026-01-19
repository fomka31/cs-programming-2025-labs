def apply_stats_grow(self):
    self.str += 5
    self.dex += 2
    self.int += 1
    self.max_hp = 120 + self.str * 3
    self.current_hp = self.max_hp
    self.max_mana = 20 + self.int
    self.current_mana = self.max_mana
    self.base_physical_dmg = 10 + self.str * 0.7
    self.base_physical_res = 5 + self.str * 0.3
    self.block_chance = 0.02 + 0.01 * self.lvl