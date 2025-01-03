

class Person:
    def __init__(self, name, health, armor, damage, damage_type):
        self.name = name
        self.health = health
        self.armor = armor
        self.damage = damage
        self.damage_type = damage_type

    def attack(self):
        pass

    def use(self, focus_stat):
        pass

    def first_skill(self):
        pass

    def second_skill(self):
        pass

    def passive_skill(self):
        pass

    def person_stats(self, stats=None):
        pass

    def __str__(self):
        pass
