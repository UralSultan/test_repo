

class Animal:
    name = None
    family = None
    sound = None


class Sound:

    def sounding(self):
        return self.sound


class Dog(Sound, Animal):

    def __init__(self, name, family, sound):
        self.name = name
        self.family = family
        self.sound = sound


dog = Dog('rex', 'dog', 'wow')
print(dog.sounding())
