from person_factory import Person


class Freid(Person):
    def __init__(self):
        Person.__init__(self, 'Freid', 5, 50, 12, 4)


class Luna(Person):
    def __init__(self):
        Person.__init__(self, 'Luna', 7, 30, 15, 2)


class Henry(Person):
    def __init__(self):
        Person.__init__(self, 'Henry', 3, 65, 10, 6)


class George(Person):
    def __init__(self):
        Person.__init__(self, 'George', 4, 20, 35, 2)


class Aurora(Person):
    def __init__(self):
        Person.__init__(self, 'Aurora', 5, 30, 15, 2)
