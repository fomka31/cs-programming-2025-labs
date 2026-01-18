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
        
        raw_dmg = self.physical_dmg
        defense = target.physical_res
        actual_dmg = max(1, int(raw_dmg - defense))  # Минимум 1 урона
        if self._roll_crit():
            actual_dmg = int(actual_dmg * self.crit_dmg)
            print("КРИТИЧЕСКИЙ УДАР!")

        target.get_dmg(actual_dmg)
        return actual_dmg
    
    def magic_hit(self, target):
        raw_dmg = self.magic_dmg

        # Магия частично игнорирует маг. защиту
        effective_res = min(target.magic_res, raw_dmg * 0.7)  # Не более 70% от урона
        actual_dmg = max(1, int(raw_dmg - effective_res))
        if self._roll_crit():
            actual_dmg = int(actual_dmg * self.crit_dmg)
            print("КРИТИЧЕСКИЙ МАГ. УДАР!")

        target.get_dmg(actual_dmg)
        return actual_dmg
    
    def piercing_hit(self, target):
        if random.random() < target.evade_chance:

            print(f"{target.name} уклонился!")
            return 0
        
        actual_dmg = max(1, int(self.piercing_dmg))  # Piercing всегда наносит урон
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

    def add_to_inventory(self, item):
        if len(self.inventory) >= self.inventory_size:
            print("Инвентарь полон!")
            if not self.drop_item():  # ← изменено
                print("Предмет не добавлен.")
                return
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
                return False  # ← отмена
            if 0 <= idx < len(self.inventory):
                dropped = self.inventory.pop(idx)
                print(f'Выброшен: {dropped.name}')
                return True
            else:
                print("Неверный номер.")
                return False
        except ValueError:
            print("Введите число.")
            return False

    def show_inventory(self):
        print("\n=== ЭКИПИРОВКА ===")
        print(f"Оружие: {self.weapon.name if self.weapon else '—'}")
        print(f"Броня:  {self.armor.name if self.armor else '—'}")
    
        print("\n=== ИНВЕНТАРЬ ===")
        if not self.inventory:
            print("Пусто")
        else:
            for i, item in enumerate(self.inventory, 1):
                print(f"{i}. {item.name} ({item.item_type})")

    def open_inventory(self):
        while True:
            self.show_inventory()
            print("\nДействия:")
            print("1. Экипировать предмет из инвентаря")
            print("2. Снять оружие")
            print("3. Снять броню")
            print("4. Использовать зелье")
            print("5. Выбросить предмет")
            print("6. Назад")
            big_line()
            try:
                choice = input("Выберите действие: ").strip()
                if choice == "1":
                    self._equip_from_inventory()
                elif choice == "2":
                    self._unequip_weapon()
                elif choice == "3":
                    self._unequip_armor()
                elif choice == "4":
                    self._use_potion()
                elif choice == "5":
                    self._drop_item()
                elif choice == "6":
                    return
                else:
                    print("Неверный выбор.")
            except Exception as e:
                print(f"Ошибка: {e}")

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

    def _equip_from_inventory(self):
        usable_items = [
            (i, item) for i, item in enumerate(self.inventory)
            if item.item_type in ("weapon", "armor") and item.can_equip(self)
        ]
        if not usable_items:
            print("Нет предметов для экипировки.")
            input("Нажмите Enter...")
            return

        print("\nДоступные предметы:")
        for idx, (pos, item) in enumerate(usable_items, 1):
            print(f"{idx}. {item.name}")

        try:
            sel = int(input("Номер предмета (0 — отмена): ")) - 1
            if sel == -1:
                return
            if 0 <= sel < len(usable_items):
                pos, item = usable_items[sel]
                if item.item_type == "weapon":
                    self.equip_weapon(item)
                elif item.item_type == "armor":
                    self.equip_armor(item)
                # Удаляем из инвентаря только если успешно экипировали
                if item not in self.inventory:
                    pass  # уже убрано в equip_*
            else:
                print("Неверный номер.")
        except ValueError:
            print("Введите число.")

    def _unequip_weapon(self):
        if not self.weapon:
            print("Оружие не экипировано.")
            return
        self.inventory.append(self.weapon)
        print(f"Оружие '{self.weapon.name}' перемещено в инвентарь.")
        self.weapon = None

    def _unequip_armor(self):
        if not self.armor:
            print("Броня не экипирована.")
            return
        self.inventory.append(self.armor)
        print(f"Броня '{self.armor.name}' перемещена в инвентарь.")
        self.armor = None

    def _use_potion(self):
        potions = [(i, item) for i, item in enumerate(self.inventory) if item.item_type == "potion"]
        if not potions:
            print("Нет зелий в инвентаре.")
            input("Нажмите Enter...")
            return

        print("\nВаши зелья:")
        for idx, (pos, item) in enumerate(potions, 1):
            print(f"{idx}. {item.name}")

        try:
            sel = int(input("Номер зелья (0 — отмена): ")) - 1
            if sel == -1:
                return
            if 0 <= sel < len(potions):
                pos, potion = potions[sel]
                potion.use(self)
                self.inventory.pop(pos)
            else:
                print("Неверный номер.")
        except ValueError:
            print("Введите число.")

    def _drop_item(self):
        if not self.inventory:
            print("Инвентарь пуст.")
            return
        self.show_inventory()
        try:
            idx = int(input(f"Номер предмета для выбрасывания (1-{len(self.inventory)}, 0 — отмена): ")) - 1
            if idx == -1:
                return
            if 0 <= idx < len(self.inventory):
                dropped = self.inventory.pop(idx)
                print(f'Выброшен: {dropped.name}')
            else:
                print("Неверный номер.")
        except ValueError:
            print("Введите число.")

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