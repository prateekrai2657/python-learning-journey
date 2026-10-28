# "Duck typing " = Another way to achieve polymorphism besides inheritance
# obejects must have the minimum neccessary attributes/methods
# "If it looks like a duck and quacks like a duck,it must be a duck.. "

class Animal:
    alive = True
    
class Dog(Animal):
    def speak(self):
        print("woof")
        
class Cat(Animal):
    def speak(self):
        print("Meow")

class Car :
    
    alive = False
    
    def speak(self):
        print("honk")
        
animals = [Dog(),Cat(),Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)