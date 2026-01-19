ROOM_TYPES = ["battle", "rest", "chest"]

class Dungeon:
    def __init__(self):
        self.floor = 1
        self.room_count = 0
        self.rooms_until_next_floor = 5  # После 5 комнат — босс

    def generate_room_pair(self):
        left = random.choice(ROOM_TYPES)
        right = random.choice(ROOM_TYPES)
        return left, right