from person_factory import Person


class Goblin(Person):
    def __init__(self):
        Person.__init__(self, "goblin", 2, 20)


class Slime(Person):
    def __init__(self):
        Person.__init__(self, "slime", 2, 20)
