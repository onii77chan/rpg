from person_factory import Person


class TheBoss(Person):
    def __init__(self):
        Person.__init__(self, "theBoss", 6, 60, 30, 6)
