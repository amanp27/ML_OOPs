class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):

    def speak   (self):
        print(f"{self.name} barks")

animal = Animal('Generic Animals')
animal.speak()

dog = Dog('Leo')
dog.speak()