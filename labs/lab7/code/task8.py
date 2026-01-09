protocols = [
    ("Lockdown", 5),
    ("Evacuation", 4),
    ("Data Wipe", 3),
    ("Routine Scan", 1)
]

protocols = [*map(lambda obj: f'Protocol {obj[0]} - Criticality {obj[1]}', protocols)]