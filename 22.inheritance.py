# inheritance = Allow you to inherit attributes and methods from another class | helps wuth code reusability and extensibility | class Child (Parent)

class Animal :
    def __init__(self,name):
        self.name = name 
        self.is_alive = True 
        
    def eat(self):
        print(f"{self.name} is eating ")
        
    def sleeping(self):
        print(f"{self.name} is sleeping ")
        
class Dog(Animal):
    def speak(self):
        print("Woof! OR Bark!") 
 
class Cat(Animal):
     def speak(self):
            print("Meow !") 
 
class Mouse(Animal):
     def speak(self):
            print("Squeek!")  

dog = Dog("Scooby") 
cat = Cat("Gimmy") 
mouse = Mouse("Mickey") 


print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleeping()
cat.speak()