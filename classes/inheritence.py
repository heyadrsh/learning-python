class Animal:
    def eat(self):
        print("eat")

class Mammal(Animal):
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    def lazy(self):
        print("So Lazy")

class Fish(Animal):
    def swim(self):
        print("swim")

dog1=Dog()
dog1.bark()
cat1=Cat() 
cat1.walk()
cat1.lazy()
fish1=Fish()
fish1.swim()
