class Hero1:
    def __init__(self, name):
        self.name = name


class Hero2:
    def __init__(self, age):
        self.age = age


class Hero3:
    def names(self):
        return f'меня зовут {self.name}'


class Hero4:
    def ages(self):
        return f'мне {self.age} лет'


class Hero5(Hero1, Hero2, Hero3, Hero4):
    def __init__(self, name, age):
        Hero1.__init__(self, name),
        Hero2.__init__(self, age),


hero = Hero5('Dariga', 15)
print(hero.name)
print(hero.age)
print(hero.ages())
print(hero.names())
