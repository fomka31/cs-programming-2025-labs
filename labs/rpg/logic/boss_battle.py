# logic/boss_battle.py

import random
from characters.enemy import Enemy
from items.item_classes import Gold
from utils.utils import big_line

def create_boss(floor):
    base_hp = 200 + floor * 50
    base_dmg = 20 + floor * 5
    bosses = [
        ("Минотавр", 1.5, 1.3),
        ("Лич", 1.2, 1.8),
        ("Драконид", 1.7, 1.4),
        ("Архидемон", 1.4, 1.6),
    ]
    name, hp_mult, dmg_mult = bosses[(floor - 1) % len(bosses)]
    hp = int(base_hp * hp_mult)
    dmg = int(base_dmg * dmg_mult)
    boss = Enemy(name, floor, hp, physical_dmg=dmg)
    boss.evade_chance = 0.1 + floor * 0.02  # Боссы могут уклоняться
    return boss

def start_boss_battle(hero, floor):
    boss = create_boss(floor)
    print(f"\n🔥🔥🔥 БОСС-БИТВА! 🔥🔥🔥")
    print(f"Этаж {floor}: {boss.name} (ур. {boss.lvl}) выходит против вас!")
    big_line()

    while not hero.is_dead and not boss.is_dead:
        print(f"\n{hero.name}: {hero.current_hp}/{hero.max_hp} HP | Мана: {hero.current_mana}/{hero.max_mana}")
        print(f"{boss.name}: {boss.current_hp}/{boss.max_hp} HP")
        print("\n1. Атаковать")
        print("2. Инвентарь")
        print("3. Попытаться уклониться")
        choice = input("> ").strip()

        if choice == "1":
            if hero.weapon and hero.weapon.weapon_type == "melee":
                dmg = hero.physical_attack(boss)
            elif hero.weapon and hero.weapon.weapon_type == "ranged":
                dmg = hero.piercing_hit(boss)
            elif hero.weapon and hero.weapon.weapon_type == "magic":
                dmg = hero.magic_hit(boss)
            else:
                dmg = hero.physical_attack(boss)
            print(f"Вы нанесли {dmg} урона.")

        elif choice == "2":
            hero.open_inventory()
            continue

        elif choice == "3":
            hero.evade_chance += 0.3
            print("Вы готовитесь к уклонению!")

        else:
            print("Неизвестная команда.")
            continue

        # Сброс бонуса уклонения
        hero.evade_chance = max(0, hero.evade_chance - 0.3)

        if boss.is_dead:
            exp = 200 + floor * 100
            gold = 100 + floor * 50
            print(f"\n👑 {boss.name} повержен! +{exp} опыта, +{gold} золота!")
            hero.plus_exp(exp)
            hero.add_to_inventory(Gold(gold))
            return True

        # Ход босса
        dmg = boss.physical_attack(hero)
        print(f"{boss.name} нанёс {dmg} урона.")

        if hero.is_dead:
            print("\n💀 Вы погибли в бою с боссом!")
            return False

    return not hero.is_dead