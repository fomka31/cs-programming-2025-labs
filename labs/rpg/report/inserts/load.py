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
        from labs.rpg.game.dungeon import Dungeon
        dungeon = Dungeon()
        dungeon.floor = dungeon_data["floor"]
        dungeon.room_count = dungeon_data["room_count"]
        dungeon.rooms_until_next_floor = dungeon_data["rooms_until_next_floor"]

        print(f"✅ Игра загружена из слота {slot_index + 1}!")
        return hero, dungeon

    except Exception as e:
        print(f"❌ Ошибка загрузки: {e}")
        return None, None