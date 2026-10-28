# function = a block of reusable Code 
#             place()after the function name to invoke it 

# def happy_birthday(name):
#     print(f"Happy birthday to {name}!")
#     print("may god bless you")
#     print("happy birthday to you")
#     print()

# happy_birthday("prateek")

# def display_invoice(username,amount,due_date):
#     print(f"hello {username}")
#     print(f"your bill is ${amount:.2f} is due : {due_date}")

# display_invoice("Prateek",780.09,"26 jan 26") 

# default arguments = a default value for certain parameters,default is used when that arguments is ommitted  make your functions more flexible ,reduces # of argumnents
# 1.positional 2. default 3.keyword 4. arbitrary

#default arguments

# def net_price(list_price,discount =0,tax=0.05):
#     return list_price*(1-discount)*(1+tax)

# print(net_price(500))  
# print(net_price(500,0.1))  

# import time 
# def count(end,start=0):
#     for x in range(start,end+1):
#         print(x)
#         time.sleep(1)
#     print("done")
        
# count(15)

# keyword agruments 

# def hello(greeting,title,first,last):
#     print(f"{greeting} {title}{first} {last}")
# hello("hello",title="Mr",last="rai",first="prateek")

#arbitrary arguments
# args = allows you to pass multiple non - key arguments {tupple}
#kwargs=allows you to pass multiple arguments{dict} *unpacking operator 
#*args
def add(*args):
    total=0
    for arg in args:
        total +=arg
    return total
print(add(1,2,3))

def display_name(*args):
    for arg in args :
        print(arg,end=" ")
display_name("prateek","rai","dr.")