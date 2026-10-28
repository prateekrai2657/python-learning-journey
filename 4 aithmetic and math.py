# x=2
# y=8
# z=-7
# result=round(x)
# # round function rounds the number to the nearest integer
# print(result)
# # abs function returns the absolute value of a number
# result=abs(z)
# print(result)
# result=pow(x,y)
# # pow function returns the value of x raised to the power of y
# print(result)

# result=max(x,y,z)
# # max function returns the largest value among the given numbers
# print(result)

import math

radius=float(input("Enter the radius of the circle: "))
area=math.pi*pow(radius,2)
circumference=2*math.pi*radius
print(f"The area of the circle is: {area} cm^2")
print(f"The circumference of the circle is: {round(circumference, 2)} cm")

a = float(input("Enter the first number: "))
b= float(input("Enter the second number: "))
c=math.sqrt(pow(a,2)+pow(b,2))
print(f"The length of the hypotenuse is: {c}")


