#super() = Fuhnction used in a child class to call method from a parent class (superclass) | Allows you to extend the functionality of the inherited methods

class Shape():
    def __init__(self,color,is_filled):
      self.color = color
      self.is_filled = is_filled
      
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'} ") 
      
class Circle (Shape):
    def __init__(self,color,is_filled,radius):
       super().__init__(color,is_filled)
       self.radius = radius
    
    def describe(self):
        super().describe()
        print(f"It is a cricle with an area of {3.14* self.radius *self.radius}cm2")
       
class Square (Shape):
     def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled)
        self.width = width
        
     def describe(self):
        super().describe()
        print(f"It is a square with an area of { self.width *self.width}cm2")

class Triangle (Shape):
      def __init__(self,color,is_filled,width,height):
       super().__init__(color,is_filled)
       self.width = width
       self.height = height
      def describe(self):
            super().describe()
            print(f"It is a triangle with an area of { self.width *self.height/2}cm2")
       


circle = Circle(color = "red",is_filled = True,radius = 5)
square = Square(color = "pink",is_filled = True,width=9)
triangle = Triangle(color = "black",is_filled = True,width = 9,height =2)


print(circle.color)
print(circle.radius)
print(circle.is_filled)

circle.describe()
triangle.describe()
square.describe()