# main.py

from characters.hero_create import create_hero
from game.game_flow import play_dungeon
from persistence.save_load import get_save_info, load_game
from items.item_list import small_heal, small_mana

def show_slots():
    """Показывает состояние слотов."""
    info = get_save_info()
    print("\nСлоты сохранений:")
    for i, status in enumerate(info, 1):
        print(f"  {i}. {status}")

def select_slot(action="загрузить"):
    """Позволяет выбрать слот (1-3)."""
    while True:
        try:
            choice = int(input(f"Выберите слот (1-3) для {action}: ")) - 1
            if 0 <= choice <= 2:
                return choice
            else:
                print("Введите число от 1 до 3.")
        except ValueError:
            print("Введите число.")

def main_menu():
    """Главное меню."""
    while True:
        print("\n" + "="*50)
        print("        🎮 RPG ПОДЗЕМЕЛЬЕ 🎮")
        print("="*50)
        show_slots()
        print("\n1. Новая игра")
        print("2. Загрузить игру")
        print("3. Выход")
        choice = input("> ").strip()

        if choice == "1":
            show_slots()
            slot = select_slot("новой игры")
            hero = create_hero()
            hero.add_to_inventory(small_heal)
            hero.add_to_inventory(small_mana)
            return hero, slot
        elif choice == "2":
            show_slots()
            slot = select_slot("загрузки")
            hero, dungeon = load_game(slot)
            if hero and dungeon:
                return hero, slot, dungeon
            else:
                print("Невозможно загрузить игру.")
        elif choice == "3":
            print("До свидания!")
            return None
        else:
            print("Неверный выбор.")

def main():
    result = main_menu()
    if result is None:
        return

    if len(result) == 2:  # Новая игра
        hero, slot = result
        from game.dungeon import Dungeon
        dungeon = Dungeon()
        play_dungeon(hero, dungeon, slot)
    else:  # Загрузка
        hero, slot, dungeon = result
        play_dungeon(hero, dungeon, slot)

if __name__ == "__main__":
    main()