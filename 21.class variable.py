# class variablesc = shared among all  instances of a class 
# define outside the constructor
# allows you to share data among all abjects created form that class

class Student:
    class_year=2069
    num_students = 0 
    
    def __init__(self,name,age):
        self.name = name    
        self.age = age
        Student.num_students += 1
    
student1 = Student("prateek",19)
student2 = Student("haaland",26)
    
print(f"My garduating class of {Student.class_year} has {Student.num_students } students")    
print(student1.name)
print(student2.name)