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