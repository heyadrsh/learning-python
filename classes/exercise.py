class Person:
    def __init__(self, name):
        self.name=name
    def talk(self):
        print(f"Hey I am {self.name} .")

john=Person("John Smilth")
john.talk()

