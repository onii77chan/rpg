from logic.person.person_creator import (
    Warrior, Mage, Archer, Healer, Tank

)


class Freid(Warrior):
    def __init__(self):
        Warrior.__init__(self, "Freid", 40, 20, 5, 4, 5)

