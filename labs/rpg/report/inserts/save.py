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