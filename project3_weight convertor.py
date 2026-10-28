# python weight convertor program
weight = float(input("Enter your weight: "))
unit = input("Enter the unit (kg or lb): ")

if (unit == "kg"):
    weight = weight* 2.205 
    unit = "Lbs"
    print(f"your weight is {round(weight,2)} {unit}")

elif (unit == "lb"):
    weight = weight/2.205 
    unit = "kg"
    print(f"your weight is {round(weight,2)} {unit}")

else:
    print(f"{unit} was not valid")