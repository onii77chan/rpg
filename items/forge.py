from foundation import (
    Weapon, Armor, Consumable

)

class Sword(Weapon):
    def __init__(self, name, price):
        super().__init__(name, price)

class Potion(Consumable):
    def __init__(self, name, price):
        super().__init__(name, price)

