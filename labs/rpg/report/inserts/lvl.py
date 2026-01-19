def plus_exp(self, num):
    
    self.exp += num
    print(f"+{num} опыта")
    self.lvl_up()

def lvl_up(self):
    while self.exp >= self.exp_to_lvlup:

        self.exp -= self.exp_to_lvlup
        self.lvl += 1
        print("\n" + "="*30 + " НОВЫЙ УРОВЕНЬ! " + "="*30)
        self.apply_stats_grow()
        self.current_hp = self.max_hp
        self.current_mana = self.max_mana
        self.exp_to_lvlup = ((1.15) ** self.lvl) * 100
        self.show_stats()
        print("="*70)