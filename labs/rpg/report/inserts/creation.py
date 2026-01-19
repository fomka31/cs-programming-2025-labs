class Hero(Entity): 
    def __init__(self, name):
        super().__init__()
        self.name = name.capitalize()
        self.str = random.randint(10, 15) 
        self.dex = random.randint(10, 15) 
        self.int = random.randint(10, 15) 
        self.inventory = []
        self.inventory_size = 10
        self.exp = 0
        self.exp_to_lvlup = ((1.15) ** self.lvl) * 100
        self.gold = 0