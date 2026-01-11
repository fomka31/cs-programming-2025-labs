# save_load.py

import json
import os
from characters.char_classes import Melee, Ranger, Mage
from items.item_list import (
    starter_sword, starter_bow, starter_staff, starter_armor,
    iron_sword, hunting_bow, mage_staff, leather_armor, chain_mail,
    small_heal, big_heal, small_mana, big_mana,
    gold_20, gold_50, gold_100
)

# Список слотов
SAVE_SLOTS = ["save_1.json", "save_2.json", "save_3.json"]

ITEM_MAP = {
    "Ржавый меч": starter_sword,
    "Простой лук": starter_bow,
    "Деревянный посох": starter_staff,
    "Тканевая одежда": starter_armor,
    "Железный меч": iron_sword,
    "Охотничий лук": hunting_bow,
    "Посох мага": mage_staff,
    "Кожаная броня": leather_armor,
    "Кольчуга": chain_mail,
    "Малое зелье лечения": small_heal,
    "Большое зелье лечения": big_heal,
    "Малое зелье маны": small_mana,
    "Большое зелье маны": big_mana,
    "20 золота": gold_20,
    "50 золота": gold_50,
    "100 золота": gold_100,
}

def get_save_info():
    """Возвращает информацию о слотах: пусто/занято + имя героя."""
    info = []
    for slot in SAVE_SLOTS:
        if os.path.exists(slot):
            try:
                with open(slot, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    name = data.get("hero", {}).get("name", "???")
                    floor = data.get("dungeon", {}).get("floor", 1)
                    info.append(f"{name} (этаж {floor})")
            except:
                info.append("Повреждено")
        else:
            info.append("Пусто")
    return info

def save_game(hero, dungeon, slot_index):
    """Сохраняет игру в указанный слот (0, 1, 2)."""
    if not (0 <= slot_index < 3):
        print("❌ Неверный слот.")
        return False

    filename = SAVE_SLOTS[slot_index]
    
    # Данные героя
    hero_data = {
        "name": hero.name,
        "class": hero.__class__.__name__,
        "lvl": hero.lvl,
        "exp": hero.exp,
        "exp_to_lvlup": hero.exp_to_lvlup,
        "current_hp": hero.current_hp,
        "max_hp": hero.max_hp,
        "current_mana": hero.current_mana,
        "max_mana": hero.max_mana,
        "str": hero.str,
        "dex": hero.dex,
        "int": hero.int,
        "gold": hero.gold,
        "weapon_name": hero.weapon.name if hero.weapon else None,
        "armor_name": hero.armor.name if hero.armor else None,
        "inventory_names": [item.name for item in hero.inventory if item.item_type != "gold"]
    }

    # Данные подземелья
    dungeon_data = {
        "floor": dungeon.floor,
        "room_count": dungeon.room_count,
        "rooms_until_next_floor": dungeon.rooms_until_next_floor
    }

    save_data = {
        "hero": hero_data,
        "dungeon": dungeon_data
    }

    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(save_data, f, ensure_ascii=False, indent=2)
        print(f"✅ Игра сохранена в слот {slot_index + 1}!")
        return True
    except Exception as e:
        print(f"❌ Ошибка сохранения: {e}")
        return False

def load_game(slot_index):
    """Загружает игру из указанного слота."""
    if not (0 <= slot_index < 3):
        print("❌ Неверный слот.")
        return None, None

    filename = SAVE_SLOTS[slot_index]
    if not os.path.exists(filename):
        print("❌ Слот пуст.")
        return None, None

    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        hero_data = data["hero"]
        dungeon_data = data["dungeon"]

        # Восстановление героя
        name = hero_data["name"]
        cls_name = hero_data["class"]
        cls = {"Melee": Melee, "Ranger": Ranger, "Mage": Mage}[cls_name]
        hero = cls(name)

        hero.lvl = hero_data["lvl"]
        hero.exp = hero_data["exp"]
        hero.exp_to_lvlup = hero_data["exp_to_lvlup"]
        hero.current_hp = hero_data["current_hp"]
        hero.max_hp = hero_data["max_hp"]
        hero.current_mana = hero_data["current_mana"]
        hero.max_mana = hero_data["max_mana"]
        hero.str = hero_data["str"]
        hero.dex = hero_data["dex"]
        hero.int = hero_data["int"]
        hero.gold = hero_data["gold"]

        weapon_name = hero_data.get("weapon_name")
        armor_name = hero_data.get("armor_name")
        hero.weapon = ITEM_MAP.get(weapon_name) if weapon_name else None
        hero.armor = ITEM_MAP.get(armor_name) if armor_name else None

        inventory_names = hero_data.get("inventory_names", [])
        hero.inventory = [ITEM_MAP[name] for name in inventory_names if name in ITEM_MAP]

        # Восстановление подземелья
        from dungeon import Dungeon
        dungeon = Dungeon()
        dungeon.floor = dungeon_data["floor"]
        dungeon.room_count = dungeon_data["room_count"]
        dungeon.rooms_until_next_floor = dungeon_data["rooms_until_next_floor"]

        print(f"✅ Игра загружена из слота {slot_index + 1}!")
        return hero, dungeon

    except Exception as e:
        print(f"❌ Ошибка загрузки: {e}")
        return None, None