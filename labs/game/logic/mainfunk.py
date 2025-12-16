from characters.heroCreate import *


def gameover():
    if hero.is_dead:
        print(f'{hero.name} пал, игра окончена.')
        flag = False


def main_funk():
    hero.lvl_up()
    gameover()