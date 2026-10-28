# Static methods = A method that belong to a class rather than any objects from that class (instances)usually used  for general utility function
# Instance methods = Best for operations on instances of the class(objects)

# Static method = best for utility functions that do not need access to class data

class Employee:
    
    def __init__(self,name,position):
        self.name=name
        self.position = position
    
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions  = ["manager","cashier","cook","janitor"]
        return position in valid_positions
    
employee1 = Employee("harshit","manager")
employee2 = Employee("ganesh","cook")
employee3 = Employee("prateek","cashier")

print(Employee.is_valid_position("Pilot"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())