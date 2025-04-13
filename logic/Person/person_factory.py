
class Person:
    def __init__(self, name, damage, health_point, mana_point=10, defence_point=5):
        self.name = name
        self.damage = damage
        self.health_point = health_point
        self.mana_point = mana_point
        self.defence_point = defence_point

    def attack(self, target, enemies_list):
        # default attack system
        if target not in enemies_list:
            return "person not in list"
        target_index = enemies_list.index(target)
        target.health_point -= self.damage

    def first_skill(self, target, enemies_list):
        pass

    def second_skill(self, target, enemies_list):
        pass

    def passive_skill(self, **kwargs):
        pass

    def __str__(self):
        return (f"{self.name} | HP: {self.health_point} | DMG: {self.damage} | "
                f"Mana: {self.mana_point} | DEF: {self.defence_point}\n")
