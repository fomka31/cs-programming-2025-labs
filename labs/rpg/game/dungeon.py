# game/dungeon.py

import random
from items.item_list import CHEST_LOOT, small_heal

ROOM_TYPES = ["battle", "rest", "chest"]

class Dungeon:
    def __init__(self):
        self.floor = 1
        self.room_count = 0
        self.rooms_until_next_floor = 5  # После 5 комнат — босс

    def generate_room_pair(self):
        left = random.choice(ROOM_TYPES)
        right = random.choice(ROOM_TYPES)
        return left, right

    def is_visible(self):
        return random.random() < 0.6

    def get_room_description(self, room_type):
        if room_type == "battle":
            return "Слышны звуки битвы... Враги!"
        elif room_type == "rest":
            return "Тишина. Место для отдыха."
        elif room_type == "chest":
            return "Блеск металла... Сундук!"

    def resolve_room(self, hero, room_type):
        print(f"\n>>> Вы вошли в комнату: {self.get_room_description(room_type)}")
        if room_type == "battle":
            from logic.battle import start_battle
            return start_battle(hero, self.floor)
        elif room_type == "rest":
            heal = min(hero.max_hp - hero.current_hp, 30)
            if heal > 0:
                hero.heal(heal)
                print(f"Вы отдохнули и восстановили {heal} HP.")
            else:
                print("Вы отдохнули, но не нуждались в лечении.")
            return True
        elif room_type == "chest":
            print("Вы нашли сундук!")
            available_loot = [
                item for item in CHEST_LOOT
                if getattr(item, 'lvl_required', 0) <= self.floor
            ]
            loot = random.choice(available_loot) if available_loot else small_heal
            hero.add_to_inventory(loot)
            return True

    def advance_room(self):
        """Переход к следующей комнате. Возвращает True, если пора драться с боссом."""
        self.room_count += 1
        return self.room_count >= self.rooms_until_next_floor

    def finish_floor(self):
        """Сброс счётчика комнат и переход на новый этаж."""
        self.room_count = 0
        self.floor += 1