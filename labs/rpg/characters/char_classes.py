# characters/char_classes.py

import random
from config.consts import *
from utils.utils import big_line
from items.item_list import starter_sword, starter_bow, starter_staff, starter_armor


class Entity:
    def __init__(self):
        self.base_physical_res = default_physical_res
        self.base_magic_res = default_magic_res
        self.base_physical_dmg = default_physical_dmg
        self.base_piercing_dmg = default_piercing_dmg
        self.base_magic_dmg = default_magic_dmg
        
        self.name = ''
        self.lvl = default_lvl
        self.max_hp = default_hp
        self.current_hp = self.max_hp
        self.max_mana = default_mana
        self.current_mana = self.max_mana
        self.crit_chance = default_crit_chance
        self.crit_dmg = default_crit_dmg
        self.evade_chance = 0
        self.weapon = None
        self.armor = None

    @property
    def physical_res(self):
        return self.base_physical_res + getattr(self.armor, 'physical_res', 0)

    @property
    def magic_res(self):
        return self.base_magic_res + getattr(self.armor, 'magic_res', 0)

    @property
    def physical_dmg(self):
        return self.base_physical_dmg + getattr(self.weapon, 'physical_dmg', 0)

    @property
    def piercing_dmg(self):
        return self.base_piercing_dmg + getattr(self.weapon, 'piercing_dmg', 0)

    @property
    def magic_dmg(self):
        return self.base_magic_dmg + getattr(self.weapon, 'magic_dmg', 0)

    @property
    def is_dead(self):
        return self.current_hp <= 0

    def get_dmg(self, dmg):
        self.current_hp = max(0, self.current_hp - dmg)

    def heal(self, amount):
        self.current_hp = min(self.max_hp, self.current_hp + amount)

    def heal_mana(self, amount):
        self.current_mana = min(self.max_mana, self.current_mana + amount)

    def _roll_crit(self):
        return random.random() < self.crit_chance

    def physical_attack(self, target):
        if random.random() < target.evade_chance:
            print(f"{target.name} уклонился!")
            return 0
        actual_dmg = max(0, self.physical_dmg - target.physical_res)
        if self._roll_crit():
            actual_dmg = int(actual_dmg * self.crit_dmg)
            print("КРИТИЧЕСКИЙ УДАР!")
        target.get_dmg(actual_dmg)
        return actual_dmg

    def magic_hit(self, target):
        effective_res = max(0, target.magic_res - (getattr(self, 'int', 0) * 0.1))
        actual_dmg = max(0, self.magic_dmg - effective_res)
        if self._roll_crit():
            actual_dmg = int(actual_dmg * self.crit_dmg)
            print("КРИТИЧЕСКИЙ МАГ. УДАР!")
        target.get_dmg(actual_dmg)
        return actual_dmg

    def piercing_hit(self, target):
        if random.random() < target.evade_chance:
            print(f"{target.name} уклонился!")
            return 0
        actual_dmg = self.piercing_dmg
        if self._roll_crit():
            actual_dmg = int(actual_dmg * self.crit_dmg)
            print("КРИТИЧЕСКИЙ ВЫСТРЕЛ!")
        target.get_dmg(actual_dmg)
        return actual_dmg


class Hero(Entity):
    def __init__(self, name):
        super().__init__()
        self.name = name.capitalize()
        self.str = random.randint(10, 15)
        self.dex = random.randint(10, 15)
        self.int = random.randint(10, 15)
        self.inventory = []
        self.inventory_size = 10
        self.exp = 0
        self.exp_to_lvlup = ((1.15) ** self.lvl) * 100
        self.gold = 0

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

    def apply_stats_grow(self):
        raise NotImplementedError

    def show_stats(self):
        big_line()
        print(f"Имя: {self.name} | Класс: {self.__class__.__name__}")
        big_line()
        print(f"Сила: {self.str} | Ловкость: {self.dex} | Интеллект: {self.int}")
        print(f"Уровень: {self.lvl} | Опыт: {round(self.exp)}/{round(self.exp_to_lvlup)}")
        print(f"Здоровье: {self.current_hp}/{self.max_hp}")
        print(f"Мана: {self.current_mana}/{self.max_mana}")
        print(f"Золото: {self.gold}")
        print(f"Оружие: {self.weapon.name if self.weapon else 'Нет'}")
        print(f"Броня: {self.armor.name if self.armor else 'Нет'}")
        print()

    def cheat(self):
        self.exp = self.exp_to_lvlup
        self.lvl_up()

    def add_to_inventory(self, item):
        if len(self.inventory) >= self.inventory_size:
            print("Инвентарь полон!")
            self.drop_item()
        self.inventory.append(item)
        if item.item_type == "gold":
            self.gold += item.amount
            print(f"Получено {item.amount} золота! Всего: {self.gold}")
        else:
            print(f'Предмет "{item.name}" добавлен.')

    def drop_item(self):
        self.show_inventory()
        try:
            idx = int(input("Номер предмета для выбрасывания (0 — отмена): ")) - 1
            if idx == -1:
                return
            if 0 <= idx < len(self.inventory):
                dropped = self.inventory.pop(idx)
                print(f'Выброшен: {dropped.name}')
            else:
                print("Неверный номер.")
        except ValueError:
            print("Введите число.")

    def show_inventory(self):
        if not self.inventory:
            print("Инвентарь пуст.")
            return
        print("\n=== ИНВЕНТАРЬ ===")
        for i, item in enumerate(self.inventory, 1):
            print(f"{i}. {item.name} ({item.item_type})")

    def open_inventory(self):
        """Полноценное меню инвентаря с действиями."""
        while True:
            self.show_inventory()
            if not self.inventory:
                input("Нажмите Enter, чтобы продолжить...")
                return

            print(f"\n{len(self.inventory) + 1}. Назад")
            big_line()
            try:
                choice = int(input("Выберите предмет: ")) - 1
                if choice == len(self.inventory):
                    return
                if 0 <= choice < len(self.inventory):
                    item = self.inventory[choice]
                    self._item_action_menu(item, choice)
                else:
                    print("Неверный номер.")
            except ValueError:
                print("Введите число.")

    def _item_action_menu(self, item, index):
        """Меню действий для выбранного предмета."""
        actions = []
        if item.item_type == "potion":
            actions.append("использовать")
        elif item.item_type == "weapon":
            if item.can_equip(self):
                actions.append("экипировать")
            actions.append("выбросить")
        elif item.item_type == "armor":
            if item.can_equip(self):
                actions.append("экипировать")
            actions.append("выбросить")
        elif item.item_type == "gold":
            actions.append("выбросить")
        else:
            actions.append("выбросить")

        actions.append("назад")

        print(f'\nПредмет: "{item.name}"')
        for i, action in enumerate(actions, 1):
            print(f"{i}. {action.capitalize()}")

        try:
            act_choice = int(input("Выберите действие: ")) - 1
            if 0 <= act_choice < len(actions):
                action = actions[act_choice]
                if action == "использовать":
                    item.use(self)
                    self.inventory.pop(index)
                elif action == "экипировать":
                    if item.item_type == "weapon":
                        self.equip_weapon(item)
                    elif item.item_type == "armor":
                        self.equip_armor(item)
                elif action == "выбросить":
                    self.inventory.pop(index)
                    print(f'Предмет "{item.name}" выброшен.')
                # "назад" — ничего не делаем
            else:
                print("Неверный выбор.")
        except ValueError:
            print("Введите число.")

    def equip_weapon(self, weapon):
        if not weapon.can_equip(self):
            print("Вы не можете экипировать это оружие!")
            return
        if self.weapon:
            self.inventory.append(self.weapon)
            print(f"Старое оружие '{self.weapon.name}' перемещено в инвентарь.")
        self.weapon = weapon
        if weapon in self.inventory:
            self.inventory.remove(weapon)
        print(f"Экипировано: {weapon.name}")

    def equip_armor(self, armor):
        if not armor.can_equip(self):
            print("Вы не можете экипировать эту броню!")
            return
        if self.armor:
            self.inventory.append(self.armor)
            print(f"Старая броня '{self.armor.name}' перемещена в инвентарь.")
        self.armor = armor
        if armor in self.inventory:
            self.inventory.remove(armor)
        print(f"Экипирована: {armor.name}")


class Melee(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.str += 4
        self.dex += 1
        self.int -= 2
        self.base_physical_dmg = 10 + self.str * 0.7
        self.base_piercing_dmg = 2
        self.base_magic_dmg = 0
        self.base_physical_res = 5 + self.str * 0.3
        self.base_magic_res = 0.25
        self.max_hp = 120 + self.str * 3
        self.current_hp = self.max_hp
        self.max_mana = 20 + self.int
        self.current_mana = self.max_mana
        self.crit_chance = 0.10
        self.crit_dmg = 1.8
        self.block_chance = 0.02 + 0.01 * self.lvl
        self.weapon = starter_sword
        self.armor = starter_armor

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


class Ranger(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.dex += 5
        self.int += 1
        self.str -= 2
        self.evade_chance = 0.1 + 0.01 * self.lvl
        self.base_piercing_dmg = 8 + self.dex * 0.9
        self.base_physical_dmg = 5 + self.str * 0.3
        self.base_magic_dmg = 1
        self.base_physical_res = 2 + self.str * 0.2
        self.base_magic_res = 2
        self.max_hp = 90 + self.str * 2
        self.current_hp = self.max_hp
        self.max_mana = 60 + self.int * 1.2
        self.current_mana = self.max_mana
        self.crit_chance = 0.20
        self.crit_dmg = 1.7
        self.weapon = starter_bow
        self.armor = starter_armor

    def apply_stats_grow(self):
        self.str += 1
        self.dex += 5
        self.int += 2
        self.max_hp = 90 + self.str * 2
        self.current_hp = self.max_hp
        self.max_mana = 60 + self.int * 1.2
        self.current_mana = self.max_mana
        self.base_piercing_dmg = 8 + self.dex * 0.9
        self.base_physical_dmg = 5 + self.str * 0.3
        self.base_physical_res = 2 + self.str * 0.2
        self.base_magic_res = 2 + self.int * 0.4
        self.evade_chance = 0.1 + 0.01 * self.lvl


class Mage(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.int += 5
        self.dex += 1
        self.str -= 3
        self.supress_spell_dmg = 0.2
        
        self.base_magic_dmg = 12 + self.int * 1.4
        self.base_physical_dmg = 2
        self.base_piercing_dmg = 1
        self.base_magic_res = 4 + self.int * 0.4
        self.base_physical_res = 1
        
        self.max_hp = 70 + self.str * 2
        self.current_hp = self.max_hp
        self.max_mana = 130 + self.int * 2
        self.current_mana = self.max_mana
        self.crit_chance = 0.12
        self.crit_dmg = 2.2
        self.weapon = starter_staff
        self.armor = starter_armor

    def apply_stats_grow(self):
        self.str += 1
        self.dex += 2
        self.int += 6
        self.max_hp = 70 + self.str * 2
        self.current_hp = self.max_hp
        self.max_mana = 130 + self.int * 2
        self.current_mana = self.max_mana
    
        self.base_magic_dmg = 12 + self.int * 1.4
        self.base_magic_res = 4 + self.int * 0.4