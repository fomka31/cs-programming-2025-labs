# logic/battle.py

import random
from characters.enemy import Enemy
from items.item_classes import Gold
from utils.utils import big_line

def create_enemy(floor):
    base_hp = 30 + floor * 8
    base_dmg = 8 + floor * 3
    templates = [
        ("Гоблин", 1.0, 0.8),
        ("Орк", 1.3, 1.0),
        ("Тролль", 1.6, 1.2),
        ("Демон", 1.9, 1.4),
    ]
    name, hp_mult, dmg_mult = random.choices(
        templates,
        weights=[4, 3, 2, 1],
        k=1
    )[0]
    hp = int(base_hp * hp_mult)
    dmg = int(base_dmg * dmg_mult)
    return Enemy(name, floor, hp, physical_dmg=dmg)

def start_battle(hero, floor):
    enemy = create_enemy(floor)
    print(f"\n⚔️  {enemy.name} (ур. {enemy.lvl}) атакует!")
    big_line()

    while not hero.is_dead and not enemy.is_dead:
        print(f"\n{hero.name}: {hero.current_hp}/{hero.max_hp} HP")
        print(f"{enemy.name}: {enemy.current_hp}/{enemy.max_hp} HP")
        print("\n1. Атаковать")
        print("2. Инвентарь")
        print("3. Попытаться уклониться")
        choice = input("> ").strip()

        if choice == "1":
            if hero.weapon and hero.weapon.weapon_type == "melee":
                dmg = hero.physical_attack(enemy)
            elif hero.weapon and hero.weapon.weapon_type == "ranged":
                dmg = hero.piercing_hit(enemy)
            elif hero.weapon and hero.weapon.weapon_type == "magic":
                dmg = hero.magic_hit(enemy)
            else:
                dmg = hero.physical_attack(enemy)
            print(f"Вы нанесли {dmg} урона.")

        elif choice == "2":
            hero.open_inventory()
            continue  # пропустить ход врага

        elif choice == "3":
            hero.evade_chance += 0.3
            print("Вы готовитесь к уклонению!")
        else:
            print("Неизвестная команда.")
            continue

        # Сброс бонуса уклонения
        hero.evade_chance = max(0, hero.evade_chance - 0.3)

        if enemy.is_dead:
            exp = 30 + enemy.lvl * 20
            gold = 15 + enemy.lvl * 5
            print(f"\n💀 {enemy.name} повержен! +{exp} опыта, +{gold} золота.")
            hero.plus_exp(exp)
            hero.add_to_inventory(Gold(gold))
            return True

        # Ход врага
        dmg = enemy.physical_attack(hero)
        print(f"{enemy.name} нанёс {dmg} урона.")

    return not hero.is_dead