# multiple inheritance = inherit from more than one parent class
#      C(A,B)

# multilevel inheritance = inherit from a parent which inherits another parent 
#      C(B) <- B(A) <- A
class Animal():
    def __init__(self,name):
        self.name = name
        
    def eat(self):
       print(f"This {self.name} is eating")    
    
    def sleep(self):
           print(f"This {self.name} is sleeping")  
           
class Prey(Animal): #parent
     def flee(self):
         print(f"This {self.name} is hunting")
 
class Predator(Animal): #parent
     def hunt(self):
         print(f"This {self.name} is hunting")
 
class Rabbit(Prey): #child
     pass
 
class Hawk(Predator):   #child
  pass
 
class Fish(Prey , Predator) :  #child
     pass
 
rabbit = Rabbit("rabbit")
hawk = Hawk("tony")
fish =Fish("fish")

hawk.hunt()
fish.flee()
rabbit.eat()
hawk.sleep()
 