# game.py

from dungeon import Dungeon
from utils import big_line
from save_load import save_game

def pause_menu(hero, dungeon, current_slot):
    """Меню паузы с выбором слота для сохранения."""
    while True:
        print("\n" + "="*40)
        print("         ⏸️  МЕНЮ ПАУЗЫ")
        print("="*40)
        print("1. Продолжить игру")
        print("2. Сохранить игру")
        print("3. Выйти в главное меню")
        choice = input("> ").strip()

        if choice == "1":
            return "continue", current_slot
        elif choice == "2":
            from save_load import get_save_info
            info = get_save_info()
            print("\nСлоты для сохранения:")
            for i, status in enumerate(info, 1):
                marker = " ← ТЕКУЩИЙ" if i-1 == current_slot else ""
                print(f"  {i}. {status}{marker}")
            slot = select_slot_for_save()
            if save_game(hero, dungeon, slot):
                return "continue", slot
            else:
                return "continue", current_slot
        elif choice == "3":
            return "exit", current_slot
        else:
            print("Неверный выбор.")

def select_slot_for_save():
    """Выбор слота для сохранения."""
    while True:
        try:
            choice = int(input("Выберите слот (1-3): ")) - 1
            if 0 <= choice <= 2:
                return choice
            else:
                print("Введите число от 1 до 3.")
        except ValueError:
            print("Введите число.")

def play_dungeon(hero, dungeon, current_slot):
    print("\nВы входите в тёмное подземелье...\n")

    while not hero.is_dead:
        big_line()
        print(f"Этаж: {dungeon.floor} | Комнат пройдено: {dungeon.room_count}/{dungeon.rooms_until_next_floor}")

        left, right = dungeon.generate_room_pair()
        visible = dungeon.is_visible()

        if visible:
            print(f"\nВы видите:\n ← {dungeon.get_room_description(left)}\n → {dungeon.get_room_description(right)}")
        else:
            print("\nТьма... Невозможно разглядеть, что впереди.")

        print("\nКоманды:")
        print("  л/п — выбрать путь")
        print("  и   — открыть инвентарь")
        print("  м   — меню (сохранить, выйти)")
        choice = input("> ").strip().lower()

        if choice in ("и", "инвентарь", "i"):
            hero.open_inventory()
            continue
        elif choice in ("м", "menu", "m"):
            action, new_slot = pause_menu(hero, dungeon, current_slot)
            current_slot = new_slot
            if action == "continue":
                continue
            elif action == "exit":
                return
        elif choice in ("л", "лево", "left", "l"):
            room_type = left
        elif choice in ("п", "право", "прав", "right", "r"):
            room_type = right
        else:
            print("Неверная команда.")
            continue

        success = dungeon.resolve_room(hero, room_type)
        if not success:
            break

        dungeon.advance()
        if hero.is_dead:
            break

    if hero.is_dead:
        big_line()
        print("💀 ВЫ ПОГИБЛИ В ПОДЗЕМЕЛЬЕ")
        big_line()