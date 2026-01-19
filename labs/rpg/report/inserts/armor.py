class Armor(Item):
    def __init__(self, name, physical_res=0, magic_res=0, **kwargs):
        super().__init__(name, item_type="armor", **kwargs)
        self.physical_res = physical_res
        self.magic_res = magic_res