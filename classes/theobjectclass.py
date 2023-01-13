class Animal:
    def __init__(self):
        self.age=1
    def eat(self):
        print("EAT")

class Mammal(Animal):
    pass

m=Mammal()
print(isinstance(m, Animal))
o=object()
print(issubclass(Mammal,Animal))