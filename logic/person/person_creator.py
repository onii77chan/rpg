

class Person:
    def __init__(self, name, health, mana, defence, damage):
        self.name = name
        self.health = health
        self.mana = mana
        self.defence = defence
        self.damage = damage

    def attack(self):
        pass

    def first_skill(self):
        pass

    def passive_skill(self):
        pass

    def __str__(self):
        return f'{self.name} {self.health} {self.mana} {self.defence} {self.damage}'


class Warrior(Person):
    def __init__(self, name, health, mana, defence, damage, bonus_health):
        super().__init__(name, health, mana, defence, damage)
        self.bonus_health = bonus_health


class Mage(Person):
    def __init__(self, name, health, mana, defence, damage, bonus_mana):
        super().__init__(name, health, mana, defence, damage)
        self.bonus_mana = bonus_mana


class Archer(Person):
    def __init__(self, name, health, mana, defence, damage, bonus_damage):
        super().__init__(name, health, mana, defence, damage)
        self.bonus_damage = bonus_damage


class Healer(Person):
    def __init__(self, name, health, mana, defence, damage, bonus_mana):
        super().__init__(name, health, mana, defence, damage)
        self.bonus_mana = bonus_mana


class Tank(Person):
    def __init__(self, name, health, mana, defence, damage, bonus_defence):
        super().__init__(name, health, mana, defence, damage)
        self.bonus_defence = bonus_defence
