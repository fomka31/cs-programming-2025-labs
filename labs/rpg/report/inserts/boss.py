def start_boss_battle(hero, floor):
    boss = create_boss(floor)
    print(f"\n🔥🔥🔥 БОСС-БИТВА! 🔥🔥🔥")
    print(f"Этаж {floor}: {boss.name} (ур. {boss.lvl}) выходит против вас!")
    big_line()


if dungeon.advance_room():
            print(f"\n{'='*50}")
            print(f"🏆 Вы прошли все комнаты этажа {dungeon.floor}!")
            print(f"Последний страж — БОСС! Готовьтесь к битве!")
            print(f"{'='*50}")

            from logic.boss_battle import start_boss_battle
            if not start_boss_battle(hero, dungeon.floor):
                break  # Герой погиб

            # Переход на следующий этаж
            dungeon.finish_floor()
            print(f"\n🌌 Вы победили босса и спустились на этаж {dungeon.floor}!")