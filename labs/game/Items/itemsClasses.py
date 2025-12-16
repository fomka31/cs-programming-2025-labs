class items:
    def __init__(self,item_name, lvl_required=1,clas_required=None,str_required=0,dex_required=0,int_required=0) -> None:
        self.lvl_required = lvl_required
        self.clas_required = clas_required
        self.str_required = str_required
        self.dex_required = dex_required
        self.int_required = int_required
        self.item_name = item_name

    def show_stats(self):
        print(f'Требуемый уровень : {self.lvl_required}')
        print(f'Требуемый класс : {self.clas_required}')
        print(f'Требуемая сила : {self.str_required}')
        print(f'Требуемая ловкость : {self.dex_required}')
        print(f'Требуемый интеллект : {self.int_required}')
        


class magic_weapon(items):
    def __init__(self,item_name, lvl_required, clas_required, str_required, dex_required, int_required, dmg) -> None:
        super().__init__(item_name, lvl_required, clas_required,str_required, dex_required, int_required)

        self.weapon_magic_dmg = dmg


class melee_weapon(items):
    def __init__(self,item_name, lvl_required, clas_required, str_required, dex_required, int_required, dmg) -> None:
        super().__init__(item_name, lvl_required, clas_required,str_required, dex_required, int_required)

        self.weapon_physical_dmg = dmg


class range_weapon(items):
    def __init__(self,item_name, lvl_required, clas_required, str_required, dex_required, int_required, dmg) -> None:
        super().__init__(item_name, lvl_required, clas_required,str_required, dex_required, int_required)

        self.weapon_piersing_dmg = dmg


class potions(items):
    def __init__(self, stat, item_name, lvl_required=1, clas_required=None, str_required=0, dex_required=0, int_required=0) -> None:
        super().__init__(item_name, lvl_required, clas_required, str_required, dex_required, int_required)
        self.stat = stat



class HealingPotion(potions):
    def __init__(self, heal_amount, item_name, lvl_required=1, clas_required=None, str_required=0, dex_required=0, int_required=0):
        super().__init__(heal_amount, item_name, lvl_required, clas_required, str_required, dex_required, int_required)
        self.heal = heal_amount  

    def use(self, target):
        target.heal(self.heal)
        print('')
        print(f'Предмет "{self.item_name}" использован на сущность "{target.name}"')
        print(f'Текущие показатели :  HP {target.current_hp}/{target.max_hp}  MANA : {target.current_mana}/{target.max_mana}')



class ManaPotion(potions):
    def __init__(self, mana_amount, item_name, lvl_required=1, clas_required=None, str_required=0, dex_required=0, int_required=0):
        super().__init__(mana_amount, item_name, lvl_required, clas_required, str_required, dex_required, int_required)
        self.mana_restore = mana_amount  

    def use(self, target):
        target.heal_mana(self.mana_restore)
        print('')
        print(f'Предмет "{self.item_name}" использован на сущность "{target.name}"')