# dungeon.py

import random
from items.item_list import CHEST_LOOT, small_heal, big_heal

ROOM_TYPES = ["battle", "rest", "chest"]

class Dungeon:
    def __init__(self):
        self.floor = 1
        self.room_count = 0
        self.rooms_until_next_floor = 5

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
            loot = random.choice(CHEST_LOOT)
            hero.add_to_inventory(loot)
            return True

    def advance(self):
        self.room_count += 1
        if self.room_count >= self.rooms_until_next_floor:
            self.floor += 1
            self.room_count = 0
            print(f"\n🌌 Вы достигли этажа {self.floor}!")