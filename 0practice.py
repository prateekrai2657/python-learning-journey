# we can assign multiple variables at a time 
# name,age,height="prateek",18,5.10
# print(name,age,height)

# name = input("enter your name ")
# print(f"hello {name}")

# rate = 19.2
# rate = int(rate)

# print(type(rate))
# print(rate)

# name = input("Enter your name : ")
# age = int(input("Enter your age : "))
# height = float(input("Enter your height:"))

# print(f"hello {name}\n")
# print(f"your are {age} years old")
# print(f"you are {height} tall !")

# floor division 
# print(10//3)
# print(10%3)
# print(3**2)

# = vs == (= is assignment operatir in which value gets stores) (== and in this used as a comparison operator )

# logical operator
# 1. and 2 or 3 not
# age = 19 
# print(age>18 and age <25)

# membership operator (in , not in) 
# name = "prateek"
# print("p" in name )

 # 1. Calculate the area of a rectangle
# Length = float(input("Enter length:"))
# Width = float(input("Enter width: "))
# Area = Length * Width
# print(f"Area of rectangle is : {Area} square units:")

# 2. Calculate Simple Interest
# principal = float (input("Enter the principal amount:"))
# rate = float (input("Enter the rate :"))
# time = float (input("Enter the time:"))

# simple_interest=(principal *time*rate)/100

# print(f"Your simple interest is {simple_interest}")

# 3. Calculate Average of Three Numbers
# a = float(input("Enter the first number :"))
# b = float(input("Enter the first number :"))
# c = float(input("Enter the first number :"))
# avg_numbers = (a+b+c)/3
# print(f"Your average of three numbers is :{avg_numbers } ")

# 4. EVEN OR ODD
# number = int(input("Enter a number :"))
# if (number % 2 == 0):
#     print("The given number is even ")
# else:
#     print("It is a odd number") 

# 5. Create variables for:
# your name
# your age
# your height
# whether you are a student

# Print all four.

# name = "prateek"
# age = 19
# height = 5.10
# is_student = True
# print(name)
# print(age)
# print(height)
# print(is_student)

# price = 99.5
# price = int(price)
# print(type(print))
# print(price)

# Q6 Take two numbers from the user and print:
# addition
# subtraction
# multiplication
# division

# a = float(input("Enter the first number: "))
# b = float(input("Enter the second number: "))

# addtion = a+b
# subtraction = a-b
# multiplication = a*b
# division = a//b
# print(f"Additon of two numbers {addtion}")
# print(f"subtraction of two numbers {subtraction}")
# print(f"multiplication of two numbers {multiplication}")
# print(f"division of two numbers {division}")

# age = int(input("Enter the age :  "))
# age_after_5_years = age + 5

# print(f"Your current age is {age}")
# print(f"Your age after 5 years will be :  {age_after_5_years}")

# radius = float(input("Enter radius :"))
# area_of_circle = 3.14*radius*radius
# print(f"Area of circle is {area_of_circle}")




            #   Day - 2
            
            
            
# condtional statement  if-else,el-if
# age = int(input("Enter your age : "))
# has_id = True
# if age >= 18  and has_id  :
#     print("adult")
# else:
#     print("child")

# raining = False
# if not raining :
#     print("you can go outside")

# password = input("Enter password :")
# if password=="python12345":
#      print("login successfull")
# else:
#     print("login failed")
    
# num = int(input("Enter the number: "))
# if num>0:
#     print("positive")
# elif num<0:
#     print("negative")
# else:
#     print("zero")

# a=int(input("Enter the first number :"))
# b=int(input("Enter the second number :"))
# c=int(input("Enter the third number :"))

# if a>b and a>c:
#     print(f"{a} is greatest")
# elif b>a and b>c:
#     print(f"{b} is greatest")
# else:
#     print(f"{c} is the greatest")

# num = int(input("Enter the number : "))
# last_digit = num %10 
# print(f"Last digit of {num} is {last_digit}")

# a = float(input("Enter the first number :"))
# b = float(input("Enter the second number :"))
# operator = input("Enter operator (+ , - , * , / : ")

# if operator == "+":
#     result = a+b
#     print(result)
    
# elif operator == "-":
#     result = a-b
#     print(result)

# elif operator == "*":
#     result = a*b
#     print(result)

# elif operator == "/":
#     result = a/b
#     print(result)
    
# else:
#     print("Invalid operator")

# username= input("Enter username: ")
# password = input("Enter the password: ")

# if username == "admin"  and password == "vk_1818" :
#     print("Login successful !")
# else:
#     print("The password and user name you entered is invalid ")
    
# Q3. Take a person's age and print:

# Child if age < 13
# Teenager if age 13–19
# Adult if age ≥ 20

# user_age = int(input("Enter your age : "))
# if user_age >= 20:
#     print("The user is Adult") 
# elif user_age >= 13 and user_age <= 19:
#     print("The user is Teenager")
# else:
#     print("The user is child")

# Marks = int(input("Enter your marks : "))
# if Marks < 100 and Marks >= 90:
#     print("You obtained Grade A")
# elif Marks <= 89 and Marks>=75:
#     print("You obtained Grade B")
# elif Marks <= 74 and Marks >= 60:
#     print("You obtained Grade C")
# elif Marks <= 59 and Marks >= 45:
#     print("You obtained Grade D")
# else:
    # print("You obtained Grade F")
    
# number = int(input("Enter the number: "))
# if number%3==0 and number%5==0:
#     print("The number is divisible by both 3 and 5")
# else:
#     print("The number is not divisible by both 3 and 5")
 
# a=int(input("Enter the first number :"))
# b=int(input("Enter the second number :"))
# c=int(input("Enter the third number :"))

# if a<b and a<c:
#     print(f"{a} is smallest")
# elif b<a and b<c:
#     print(f"{b} is smallest")
# else:
#     print(f"{c} is the smallest")

# year = int(input("Enter the year:"))
# if year%4==0 and year%100!=0:
#     print("leap year")
# else:
#     print("not a leap year")

# ch = input("Enter any character : ")
# if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
#     print("It is a vowel")
# else :
#     print("it is consonant")

# num = int(input("Enter the number : ") )
# last_digit = num % 10 
# if last_digit % 2 == 0:
#     print("The last digit is even")
# else:
#     print("The last digit is odd")

# number = int(input("Enter the number: "))

# if number >= 100 and number <= 999:
#     print("3 digit number")
# else:
#     print("Not a 3 digit number")



#              day 3 loops - {while - when a condition is true}
# count=1
# while count<=5:
#     print(count)
#     count+=1    
# for i in range(7):
#     print("Hello world")

# i = 0 
# while i<=10:
#     print(i)
#     i+=1

# i = 10 
# while i>=1:
#     print(i)
#     i-=1 

# i = 2
# while i<=20:
#     print(i)
#     i+=2

# number = int(input("Enter the number : "))
# while number != 0 :
#     print("you entered:",number)
#     number = int(input("Enter the number : "))

# for i in range(1,6): # 6 will be excluded (start,stop)
#     print(i)

# for i in range(1,10,2): # 2 means increase by 2 (start,stop,step)
    # print(i)

# for i in range(10,0,-1):
#     print(i)

# for i in range(2, 21, 2):
#     print(i)

# name = "Prateek"
# for character in name:
#     print(character)

# name = "Prateek"
# count = 0 
# for charcter in name:
#     count +=1
# print(count)

# break is used to completely stop a loop.
# for i in range(1,11):
#     if i == 5:
#         break
#     print(i)           break = EXIT THE LOOP


# continue skips the current iteration and moves to the next iteration.
# for i in range(1,6):
#   if i ==3:
#     continue
#   print(i)

# for i in range(5,0,-1):
#     print("*" * i)

# number = int(input("Enter a number : "))
# for i in range (1,11):
#     print(number,"x",i,"=",number*i)

# total = 0
# for i in range(1,11):
#     total+= i
# print(f"sum is {total}")

# number = int(input("Enter the  number : "))
# factorial = 1
# for i in range(1,number+1):
#   factorial *=i
# print(f"factorial of {number} is {factorial}")


# for i in range (1,21):
#     print(i)
# for i in range (20,0,-1):
#     print(i)

# for i in range(1,10):
#     print("hello python")
# number = int(input("Enter the number : "))
# for i in range(1,11):
#     print(number,"x",i,"=",number*i)

# count = 1
# while count <= 50:
#     print(count)
#     count += 1
    
# for i in range (1,51):
#     if i % 5 == 0:
#         print(i)
# for i in range (1,101):
#     if i%5==0 and i%3==0:
#         print(i)

# number= int(input("Enter the number : "))
# for i in range(1,number+1):
#    if i%2==0:
#     print(i,":even")
    
#    else:
       
#     print(i,":odd")

# number= int(input("Enter the number : "))
# sum = 0
# for i in range(1,number+1):
#     sum+=i
# print(sum)

# number= int(input("Enter the number : "))
# factorial = 1
# for i in range(1, number+1):
#     factorial*=i
# print(f"factorial of {number} is {factorial}")

# number= int(input("Enter the number : "))
# for i in range(1,number+1):
#    if i%2==0:
#     print(i,":even")

# count = 10

# while count>=1:
#    print(count)
#    count-=1

# number = int(input("Enter the number : "))
# i = 1 
# while i <= 10:
#     print(number,"x",i,"=",number*i)
#     i+=1
    
# while True :
#     number = int(input("Enter a number: "))
#     if number == 0 :
#         break;
# print("You entered 0 now you will be out of loop")

        #   day - 4 {list,tuple,dictionaries,string}
        
#  string - a sequence of charcters 

# name = "python"
# print(type(name))

# string indexing
# print(name[0])
# print(name[1])
# print(name[4])
# print(name[-1])
# print(name[-5])
# #string indexing
# print(name[0:3])
# print(name[2:])
# #string mwthods
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# name=name.replace("python","Prateek")
# print(name.find("y"))


# print("py"in name)
# print("xyz"in name)

# String Concatenation
# first_name = "Prateek "
# last_name = "Rai"

 
# full_name = first_name + " " + last_name
 
# print(full_name)

# name = "Prateek"
# print(name[0])
# print(name[6])
# print(name[::-1])
# print(name.find("a"))
# print("python"in name)

#             lists [] used to store the values 
# fruits =["Apple","Banana","Strawberry","orange"]
# # print(type(fruits))
# # print(fruits)
# #  List indexing
# # print(fruits[0])
# # print(fruits[2])
# # fruits.remove("Banana")
# print("orange" in fruits)
# for fruit in fruits:
    # print(fruit) 

  #List Slicing
# numbers =[10,20,30,40,50]
# print (max(numbers)) # 4 will be excluded 
# numbers = [1,5,8,3,2,4]
# numbers.sort()
# print(numbers)
# print(len(numbers))

# print(numbers.count(20))
# # print(numbers[1:4])
# # numbers.append(60)
# numbers.insert(1,100)
# numbers.pop(2) using its index
# numbers.clear()

# print(numbers)

# lists are mutable unlike strings list can be changed 
# fruits[1]="Orange"
# print(fruits)

# numbers = [10, 15, 22, 33, 40, 51, 60]

# even = []
# odd = []

# for number in numbers:

#     if number % 2 == 0:
#         even.append(number)

#     else:
#         odd.append(number)

# print("Even:", even)
# print("Odd:", odd)

# Tuple () = A tuple is similar to a list but it is immutable, meaning its contents cannot be changed after creation.

# number =(10,20,30,40,10,10)
# print(type(number))

# print(number[2])
# print(number[-1])
# print(number[0:2])
# # tuple is immutable you cannot modify the tuple elements 
# print(len(number))
# print(number.count(10))
# print(number.index(20))
                 # unpacking tuple :
# person = ("Prateek", 19, "varanasi")

# name, age, city = person

# print(name)
# print(age)
# print(city)


        # Sets are another type of data structure which is used to stores unique values || duplicates values are automatically removed
# number = {1,2,3,4,5,6}
# print(number) 
# sets are unordered here it doesnot depend on position   
# number.add(69)
# number.remove(6)
# number.discard(2)
# number.pop()
# number.pop()
# print(number)

# a = {1,2,3,4}
# b={5,3,6,7,8,1}
# print(a|b) # UNION
# # print(a&b) # INTERSECTION

# x={}
# print(type(x))
# this creates a empty dictonary not a empty set #
# # for  an empty set 
# x = set()
# print(type(x))

  # dictionaries it stores value in key-value pair
# student = {
#     "name":"Prateek",
#     "age":19,
#     "branch":"CSE"
# }
# student["city"]="varanasi"
# print(student["name"])
# print(student.get("city"))
# print(student.get("age"))
# print(student.keys())
# print(student.values())
# print(student.items())
# for key in student:
#     print(key)
# for value in student.values():
#     print(value)
# students = [
#     {
#         "name": "Prateek",
#         "marks": [80, 85, 90]
#     },

#     {
#         "name": "Rahul",
#         "marks": [70, 75, 80]
#     }
# ]
# print(students[1]["name"])

# A function is a reusable block of code that performs a particular task.Instead of writing the same code again and again, we put it inside a function and call it whenever we need it.

# def greet(name):
#     print("Hello",name)
    
# greet("Prateek")
# greet("krish")
# greet("mohit")

# def function_name(dog):
#     print("bark",dog)

# function_name("rocky")
# def add(a,b):
#     print(a+b)
# add(10,20)
# def student(name,age,branch):
#     print("name :",name)
#     print("age :",age)
#     print("branch :",branch)
# student("Prateek",19,"cse")

# def greet():
#     user_name = input("Enter your name :")
#     print("hello!",user_name)

# greet()

# def square():
#     number = int(input("Enter your number:"))
#     print(f"square of your number is : {number**2}" )

# square()

# def square(number):
#     return number**2

# number = int(input("Enter your number : "))
# result = square(number)
# print(f"The square of number is : {result}")

# Local Variables

# A variable created inside a function is generally local to that function.

# def test():
#     x = 10
#     print(x)

# test()

# Global Variables

# A variable created outside the function is global.

# x = 10

# def test():
#     print(x)

# test()

# def check_number(number):
#     if number>0:
#         return"Positive"
#     elif number<0:
#         return "negative"
#     else:
#         return "zero"
# number = int(input("Enter the number: "))
# result = check_number(number)
# print(result)

# def factorial(n):

#     result = 1

#     for i in range(1, n + 1):
#         result *= i

#     return result


# number = int(input("Enter number: "))

# print(factorial(number))

# list comprehession
# A comprehension is a short and clean way to create a new collection from an existing iterable.
# numbers = [i for i in range(1,6)]
# print(numbers)
# square = [i**2 for i in range(1, 6)]
# print(square)

# even_number = [i for i in range(1,11) if i%2==0]
# print(even_number)
# odd_number = [i for i in range(1,11) if i%2!=0]
# print(odd_number)

# numbers = [1,2,3,4,5,8,12,45,67,89,17,7]
# results=[i for i in numbers if i>15]
# print(results)

# Dictionary Comprehension
# Now the same idea with dictionaries.
# number = [1, 2, 3, 4, 5]
# square_dict = {i: i**2 for i in number}
# print(square_dict)

# exception handling -- An exception is an error that occur while the program is running .

# a = 10
# b = 0
# print(a/b) # zero division error 
# try:
#     a=10
#     b=0
#     print(a/b)
    
# except:
#     print("something went wrong ")

# Handling a Specific Exception
# try:
#     a = 10
#     b = 0
#     print(a / b)

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# try:
#   number = int(input("Enter a number :"))
#   result = 10 / number
#   print(result)

# except ValueError:
#   print("Please enter a Valid number")
  
# except ZeroDivisionError:
#   print("Cannot divide by zero ")


# What is File Handling?

# File handling means creating, reading, writing, and modifying files using Pytho
       #reading,opening and closing files
# file=open("text.txt","r")
# read_file=file.read()
# print(read_file)
# file.close()
                      #Another Way
# with open("text.txt","r") as file:
#   content = file.read()
# print(content)

            # Writing to a File ---"w"->overwrite||||Old content is removed
# with open("text.txt","w")as file: 
#   file.write("Hello, this is a new line.")
#   file.write("Python\n")
#   file.write("SQL\n")  
#   file.write("Numpy\n")  

#append --- here old content remains and new content is added at the end.
# with open("text.txt", "a") as file:
#   file.write("this is appended line.\n")
#   file.write("this is also appended line.\n")

# Creating a File Using "x"
# with open("xyz.txt","x")as file:
#   file.write("This is new file")

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# course = input("Enter your course: ")

# # with open("student.txt", "a") as file:
# #     file.write(f"Name: {name}\n")
# #     file.write(f"Age: {age}\n")
# #     file.write(f"Course: {course}\n")

# # print("Student information saved.")



# while True:
  
  # print("1.WRITE THE NOTE")
  # print("2.READ THE NOTE")
  # print("3.EXIT THE NOTE")
  
#   choice=int(input("Enter the choice : "))
  
#   if choice==1:
#     note=input("Enter your note:")
#     with open("text.txt","a") as file:
#       file.write(note + "/n")
#       print("Note saved!")
      
#   elif choice==2:
#     with open("text.txt","r") as file:
#        print("\nYour Notes:")
#        print(file.read())
       
#   elif choice==3:
#     print("Goodbye!")
#     break
#   else:
    # ("Invalid Choice")
    
# print("hello")

# Class >>>>

# A class is a blueprint/template for creating objects.

# Object >>>

# An object is an actual instance of a class.
# class student:
#   name ="Prateek"
#   age = 19 
# student1= student()

# print(student1.name)
# print(student1.age)  
# __init__() Constructor

# __init__() is automatically called when an object is created.

# It is commonly used to initialize object data.
# class student:
#   def __init__(self,name,age):
#     self.name = name
#     self.age =age
# student1 = student("Prateek",19)
# student2 = student("Rahul",20)

# print(student1.name)
# print(student1.age)
# print(student2.name)
# print(student2.age)
# 8️⃣ Encapsulation 🔒

# Encapsulation means wrapping data and methods together and controlling access to data.
# class bankaccount:
#   def __init__(self,balance):
#     self.balance = balance
  
#   def show_balance(self):
#     print(f"Current balance: {self.balance}")
  
# account1= bankaccount(1000)
# account1.show_balance()
# account2= bankaccount(4000)
# account2.show_balance()


# ...............inheritance allows you ton inherit one class properties and methods from another class
# class animal:
#   def eat(self):
#     print("Animal is eating")
    
# class dog(animal):
#   def bark(self):
#     print("Dog is barking")
    
# d = dog()
# d.eat()
# d.bark()

# There are  3 types of inheritance:
#   single inheritance, multiple inheritance, and multilevel inheritance.

# ...........super() function is used to call the parent class methods from the child class.
# class Animal:

#     def __init__(self, name):
#         self.name = name


# class Dog(Animal):

#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed


# d = Dog("Bruno", "Labrador")

# print(d.name)
# print(d.breed)

# polymorphism ............................

# poly means many
# morphism means form

# same method/function name can behave differently for different objects .

# class Dog:
#   def sound(self):
#     print("Bark")

# class cat:
#   def sound(self):
#     print("Meow")
  
# dog = Dog()
# Cat= cat()

# dog.sound()
# Cat.sound()

# abstarction means hiding implementation details and showing only essesntial information 

# from abc import ABC, abstractmethod

# class animal(ABC):
  
#   def __init__(self, name):
#     self.name = name
  
#   @abstractmethod
#   def sound(self):
#     pass
  
#   def eat(self):
#     print(self.name,"is eating")

# class Dog(animal):

#   def sound(self):
#     print(self.name," barks")

# class Cat(animal):

#   def sound(self):
#     print(self.name," meows")
    
# dog=Dog("Bruno")
# cat=Cat("kitty")

# dog.sound()
# dog.eat()

# cat.sound()
# cat.eat()
# class student:
#  def __init__(self,name,age,branch):
#   self.name=name
#   self.age=age
#   self.branch=branch

# student1 = student("Prateek", 19, "CSE")

# print(student1.name)
# print(student1.age)
# print(student1.branch)

# class Car:
#   def __init__(self, brand, model, price):
#     self.brand = brand
#     self.model = model
#     self.price= price
 
#   def display(self):
#     print(f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}")

# car1 = Car("Toyota", "Camry", 25000)
# car2 = Car("Honda", "Civic", 22000)

# car1.display()
# car2.display()

# class Rectangle :
#   def __init__(self,length,width):  
#     self.length = length
#     self.width = width
    
#   def area(self):
#     return self.length * self.width
  
# length=float(input("Enter the length:"))
# width=float(input("Enter the width:"))

# rectangle=Rectangle(length,width)

# print("Area of rectangle:",rectangle.area())
  
# class person:
#   def __init__(self,name):
#     self.name=name
    
# class student(person):
#   def __init__(self,name,rollno):
#     super().__init__(name)
#     self.rollno=rollno
    
# student1=student("prateek",101)

# print("name:",student1.name)
# print("Roll no:",student1.rollno)

# class Animal:
#   def __init__(self,name):
#     self.name=name
  
# class Dog(Animal):

#   def sound(self):
#    print("Bark")
  
# class Cat(Animal):
#   def sound(self):
#     print("Meow")
  
# d=Dog("XRZ")
# c=Cat("SJDJ")
  
# c.sound()
# d.sound()

# class Vehicle:
#   def __init__(self,name):
#     self.name=name

# class Car(Vehicle):
  
  
#libraries revision 
# import numpy as np


# arr = np.array([1,2,3,4])

# print(arr)
# print(arr.shape)
# print(arr.ndim)
# print(arr.size)

# let's build 2-d array

# data = np.array([[10,20,30],
#                 [50,60,70]
#                 ])
# print(data)
# print(data.shape)


#indexing and slicing 
# arr=np.array([10,20,30,40,50])

# print(arr[0])
# print(arr[2])
# print(arr[1:4])

# arr = np.array([10,20,40,50])
# print(arr[0])
# print(arr[2])
# print(arr[1])

# # 4.Mathematical operator 
# arr=np.array([10,20,30,40,50])
# print(arr+5)
# print(arr+5)
# print(arr/5)

#5.Aggregation
# print(arr.sum())
# print(arr.mean())
# print(arr.max())

# #filtering 
# print(arr[arr>40])

# marks = np.array([45, 67, 89, 32, 76, 91, 55])
# print(marks.mean())# for average we use mean function
# print(f"Highest marks scored by student is {marks.max()}") 
# print(f"Lowest marks scored by student is {marks.min()}") 
# print(f"Marks greater than 60 scored by student is {marks[marks>60]}") 
# print(marks+5)

# import pandas as pd

# #creating a data frame
# data = {
#     "Player": ["Virat", "Rohit", "Gill"],
#     "Runs": [620, 580, 540],
#     "Matches": [10, 10, 10]
# }
# df=pd.DataFrame(data)
#print(df)

# df=pd.read_csv("cricket_data.csv")


# df.head()
# df.tail()
# df.shape
# df.columns
# df.info()
# df.describe()

#select columns
# df[["Player", "Runs"]]


#filtering
# df[df["Runs"]>570]


# df["Average"] = (df["Runs"] / df["Matches"]) 
# df.groupby("Team")["Runs"].sum()
# print(df)
# df.head()
# df.tail()
# df.shape
# df.columns
# df.info()
# df.describe()


# x=100;
# # y=29;
# # print(x**2)
# # print(x%y)

# print(type(x))

# print(type(29.5))
# print(int(x)+1)

# name1=input("ENter the user name ")
# print(f"Hello, {name1}!")

# Name = input("Enter your name: ")
# Age = int(input("Enter your age: "))
# college = input("Enter your college name: ")
# print(f"Hello {Name}, you are {Age} years old and you study at {college}.")

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# sum = num1 + num2
# print(f"The sum of {num1} and {num2} is: {sum}")

# product = num1*num2
# print(f"The  product of {num1} and {num2} is: {product}")

# difference = num1-num2
# print(f"The difference of {num1} and {num2} is: {difference}")

# quotient = num1/num2
# print(f"The quotient of {num1} and {num2} is: {quotient}")

# a = 10 
# b =20
# print(a==b)
# print(a>=b)
# print(a<=b)

# print(a<b)

# num = int(input("Enter a number:" ))

# if (num>0):
#   print("positive")

# elif(num<0):
#   print("negative")

# else:
#   print("zero")
  
# marks = int(input("Enter your marks: "))

# if marks>=30:
#   print("failed")
# elif marks>=90:
#   print("passed")
  

# and = both conditions must be true 
# or = at least one condition must be true 
# not =  reverse the boolean value 

# age = 18
# has_id = True

# if age >=18 and has_id:
#   print("allowed in our event ")

# else : 
#   print("not allowed")
# number = int(input("Enter a number: "))

# if (number %2== 0):
#   print("even")
# else :
#   print("odd")


# year_check = int(input("Enter the year: "))
# if (year_check % 4 == 0 and year_check % 100 != 0) or (year_check % 400 == 0):
#   print(f"{year_check} is a leap year")
  
# else :
#   print(f"{year_check} is not a leap year")
  
  
# num1= float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))  

# choice = input("Enter the operation (+, -, *, /): ")

# if choice == "+":
#   result=num1+num2
#   print(f"The sum of {num1} and {num2} is: {result}")
  
# elif choice == '-':
#   result=num1-num2
#   print(f"the difference of {num1} and {num2} is:{result}")
  
# elif choice == '*':
#   result=num1*num2
#   print(f"the product of {num1} and {num2} is:{result}")
  
# elif choice == '/':
#   result=num1/num2
#   print(f"the quotient of {num1} and {num2} is:{result}")
  
# else:
#   print("Invalid operation")  

# for i in range(1,21,3):
#   print(i)

# total = 0 
# for i in range (1,11):
#   total = total + i 
  
# 
# print(total)

# num = int(input("Enter a number: "))
# for i in range(1, 11):
#   print(f"{num} x {i} = {num*i}")\
    
for i in range(1,11):
  if i ==5 :
    break
  print(i)