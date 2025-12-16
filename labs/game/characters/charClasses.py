import consts, random
from Items.item_list import *


class Entity:
    def __init__(self) -> None:
        self.name = ''
        self.lvl = consts.default_lvl
        self.mag_res = consts.default_magic_res
        self.physical_res = consts.default_phisic_res
        self.max_hp = consts.default_hp
        self.current_hp = self.max_hp
        self.max_mana = consts.default_mana
        self.current_mana = self.max_mana
        self.magic_dmg = consts.default_magic_dmg
        self.phisical_dmg = consts.default_phisic_dmg
        self.piercing_dmg = consts.default_piercing_dmg
        self.crit_chance = consts.default_crit_chance
        self.crit_dmg = consts.default_crit_dmg
        self.evade_chance = 0
        self.supress_spell_dmg = 0
        self.block_chance = 0
        self.is_dead = False



    def physical_attack(self, target):
        actual_dmg = max(0,self.phisical_dmg  - target.phisical_res)
        target.current_hp = max(0, target.current_hp - actual_dmg)


    def magic_hit(self, target):
        actual_dmg = max(0,self.magic_dmg  - target.magic_res)
        target.current_hp = max(0, target.current_hp - actual_dmg)
    

    def piercing_hit(self, target):
        actual_dmg = self.piercing_dmg
        target.current_hp = max(0, target.current_hp - actual_dmg)


    def heal(self, heal):
        self.current_hp = min(self.max_hp, self.current_hp + heal)


    def get_dmg(self, dmg):
        actual_dmg = dmg
        self.current_hp = max(0, self.current_hp - actual_dmg)

    
    def heal_mana(self, heal_mana):
        self.current_mana = min(self.max_mana, self.current_mana + heal_mana)



class Hero(Entity):
    def __init__(self, name) -> None:
        super().__init__()
        self.str = random.randint(10,15)
        self.dex = random.randint(10,15)
        self.int = random.randint(10,15)
        self.name = name.capitalize()
        self.phisic_bonus_dmg = 0
        self.magic_bonus_dmg = 0
        self.inventory_size = 3
        self.inventory = [big_heal,small_heal,small_mana]
        
        self.exp = 0
        self.exp_to_lvlup = ((1 + 0.15)**self.lvl)*100


    def plus_exp(self, num):
        self.exp += num
    

    def lvl_up(self):
        if self.exp >= self.exp_to_lvlup:
            self.exp = self.exp - self.exp_to_lvlup
            self.lvl += 1
            self.onlvl_up()


    def show_stats(self):
        print(f'======================================================================')
        print(f'            Имя героя : {self.name} | Класс : {self.__class__.__name__}               ')
        print(f'======================================================================')
        print(f'Сила : {self.str}  |  Ловкость : {self.dex}  |  Интеллект : {self.int}')
        print(f'Уровень : {self.lvl}  |  Текущий опыт : {round(self.exp)}/{round(self.exp_to_lvlup)} до следующего уровня')
        print(f'Текущее здоровье : {self.current_hp}/{self.max_hp}')
        print(f'Текущая мана  : {self.current_mana}/{self.max_mana}')
        print()


    def cheat(self):
        self.exp = self.exp_to_lvlup


    def onlvl_up(self):
        print('')
        print("НОВЫЙ УРОВЕНЬ")
        print('')
        print('ХАРАКТЕРИСТИКИ УЛУЧШЕНЫ')
        print('')
        print('ЗДОРОВЬЕ И МАНА ВОСПОЛНЕНЫ')
        print('')
       
        self.apply_stats_grow() # type: ignore
        self.current_hp = self.max_hp
        self.current_mana = int(self.max_mana)
        self.exp_to_lvlup = ((1.15) ** self.lvl) * 100
        self.show_stats()
        

    def add_to_inventory(self, item): 
        if len(self.inventory) >= self.inventory_size:
            print(f'Инвентарь полон')
            print('')
        else:
            self.inventory.append(item)
            print(f'Предмет "{item.name}" добавлен в инвентарь.')
            print('')

    
    def drop_from_inventory(self, item):
        self.inventory.remove(item)
        print(f"Предмет '{item.item_name}' использован и удалён.")


    def show_inventory(self):
        for i in range(self.inventory_size):
            try:
                print(f'{i+1}. {self.inventory[i].item_name}')
            except:
                print(f'{i+1}. ')


    def use_item(self):
        if not self.inventory:
            print('Инвентарь пуст')
            return

        bigLine()
        self.show_inventory()
        print(f'{self.inventory_size + 1}. Выход из инвентаря')
        bigLine()
        print(f'Выбор объекта/действия (1-{self.inventory_size + 1}) : ')

        while True:
            try:
                choice = int(input())
                if 1 <= choice <= self.inventory_size + 1:
                    break
                else:
                    print('Неверный ввод')
            except ValueError:
                print('Неверный ввод')

        if choice == self.inventory_size + 1:
            return

        try:
            item = self.inventory[choice - 1]
            if isinstance(item, HealingPotion):
                item.use(self)
            elif isinstance(item, ManaPotion):
                item.use(self)
            else:
                print("Этот предмет нельзя использовать.")
                # return

            self.inventory.pop(choice - 1)
            self.use_item()

        except IndexError:
            print('Предмета нет в инвентаре.')
        
        


class Melee(Hero):
    def __init__(self, name) -> None:
        super().__init__(name)
        # Усиливаем силу и здоровье
        self.str += 4
        self.dex += 1
        self.int -= 2  # воин не маг

        # Увеличиваем максимальное здоровье за счёт силы
        self.max_hp = 120 + self.str * 3
        self.current_hp = self.max_hp

        # Физический урон на основе силы
        self.phisical_dmg = 10 + self.str * 0.7

        # Пронзающий урон — низкий (воин рубит, не колет)
        self.piercing_dmg = 2

        # Мана — минимальная (воин редко использует заклинания)
        self.max_mana = 20 + self.int
        self.current_mana = self.max_mana

        # Защита выше среднего
        self.physical_res = 5 + self.str * 0.3

        self.block_chance = 0.02 + 0.01*self.lvl

        # Крит — ниже, чем у лучника, но урон выше
        self.crit_chance = 0.10  # 10%
        self.crit_dmg = 1.8      # крит наносит 180% урона

    
    def apply_stats_grow(self):
        self.str +=5
        self.dex +=2
        self.int +=1

        self.max_hp = 120 + self.str * 3
        self.current_hp = self.max_hp

        self.max_mana = 20 + self.int
        self.current_mana = self.max_mana

        self.phisical_dmg = 10 + self.str * 0.7

        self.physical_res = 5 + self.str * 0.3
        self.block_chance = 0.02 + 0.01*self.lvl


class Ranger(Hero):
    def __init__(self, name) -> None:
        super().__init__(name)
        # Лучник — ловкий и точный
        self.dex += 5
        self.int += 1
        self.str -= 2

        self.evade_chance = 0.1 + 0.01 * self.lvl

        # Среднее здоровье, умеренная мана (для умений)
        self.max_hp = 90 + self.str * 2
        self.current_hp = self.max_hp

        self.max_mana = 60 + self.int * 1.2
        self.current_mana = self.max_mana

        # Основной урон — пронзающий (стрелы)
        self.piercing_dmg = 8 + self.dex * 0.9
        # Немного физического урона (без оружия)
        self.phisical_dmg = 5 + self.str * 0.3

        # Магический урон — почти отсутствует
        self.magic_dmg = 1

        # Защита — ниже среднего, но уворачивается чаще (через ловкость)
        self.physical_res = 2 + self.str * 0.2
        self.mag_res = 2

        # Высокий шанс крита (точные выстрелы)
        self.crit_chance = 0.20  # 20% — один из самых высоких!
        self.crit_dmg = 1.7      # крит умножает пронзающий урон


    def apply_stats_grow(self):
        self.str +=1
        self.dex +=5
        self.int +=2

        self.max_hp = 90 + self.str * 2
        self.current_hp = self.max_hp

        self.max_mana = 60 + self.int * 1.2
        self.current_mana = self.max_mana

        self.piercing_dmg = 8 + self.dex * 0.9

        self.phisical_dmg = 5 + self.str * 0.3

        self.physical_res = 2 + self.str * 0.2
        self.mag_res = 2 + self.int * 0.4
        self.evade_chance = 0.1 + 0.01 * self.lvl

class Mage(Hero):
    def __init__(self, name) -> None:
        super().__init__(name)
        # Маг — умный, но слабый в ближнем бою
        self.int += 5
        self.dex += 1
        self.str -= 3

        self.supress_spell_dmg = 0.2

        # Мало здоровья, много маны
        self.max_hp = 70 + self.str * 2
        self.current_hp = self.max_hp

        self.max_mana = 130 + self.int * 2
        self.current_mana = self.max_mana

        # Основной урон — магический
        self.magic_dmg = 12 + self.int * 1.4

        # Физический урон почти отсутствует
        self.phisical_dmg = 2
        self.piercing_dmg = 1

        # Магическая защита выше среднего
        self.mag_res = 4 + self.int * 0.4
        # Физическая защита — низкая
        self.physical_res = 1

        # Крит — редкий, но может быть усилен заклинаниями (пока базовый)
        self.crit_chance = 0.08  # 8%
        self.crit_dmg = 2.0      # магический крит — очень сильный
    

    def apply_stats_grow(self):
        self.str +=1
        self.dex +=2
        self.int +=6

        self.max_hp = 70 + self.str * 2
        self.current_hp = self.max_hp

        self.max_mana = 130 + self.int * 2
        self.current_mana = self.max_mana

        self.magic_dmg = 12 + self.int * 1.4


class enemy(Entity):
    def __init__(self, name, lvl, hp, mana) -> None:
        super().__init__()
        self.name = name
        self.lvl = lvl
        self.max_hp = hp
        self.current_hp = self.max_hp
        self.max_mana = mana
        self.current_mana = self.max_mana




def bigLine():
    print(f'======================================================================')