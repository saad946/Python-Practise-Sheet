class Animal:
    pass

class Pets:
    pass

class Dog(Animal, Pets):
    @staticmethod
    def bark():
        print("Bow!")


d = Dog()
d.bark()