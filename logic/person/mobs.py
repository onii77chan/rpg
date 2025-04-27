from logic.person.person_creator import (
    Warrior, Mage, Archer, Healer, Tank
)


class GoblinWarrior(Warrior):
    def __init__(self, name, health, mana, defence, damage, bonus_health):
        super().__init__(name, health, mana, defence, damage, bonus_health)


class GoblinMage(Mage):
    def __init__(self, name, health, mana, defence, damage, bonus_mana):
        super().__init__(name, health, mana, defence, damage, bonus_mana)


class GoblinArcher(Archer):
    def __init__(self, name, health, mana, defence, damage, bonus_damage):
        super().__init__(name, health, mana, defence, damage, bonus_damage)

