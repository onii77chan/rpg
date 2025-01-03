
class Logger:
    def __init__(self):
        pass


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Weapon(Item):
    def __init__(self, name, price):
        super().__init__(name, price)


class Armor(Item):
    def __init__(self, name, price):
        super().__init__(name, price)


class Consumable(Item):
    def __init__(self, name, price):
        super().__init__(name, price)

