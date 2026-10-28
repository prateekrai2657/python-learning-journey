# Object = A bundle of relative attributes (variables) and methods (functions) ex- phone,cup,book
# you need a class to create many objects 

# Class = A (blueprint) used to design the layout and structure of an object

class Car:
    def __init__(self,model,year,color,for_sale): #constructor and dunder used
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
    def drive(self): #methods
        print(f"You drive the {self.color} {self.model}")
        
    def stop(self): #methods
        print(f"Stop the car {self.model}")
    
    
        
car1 = Car("scorpio",2025,"black",False)
car2 = Car("bmw",2021,"blue",True)

print(car2.model)
print(car1.year)
print(car2.color)
print(car1.for_sale)

car1.drive()
car2.drive()
car1.stop()

