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


