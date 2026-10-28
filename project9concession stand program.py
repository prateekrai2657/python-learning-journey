menu = {"pizza":3.00,
        "nachos":4.50,
        "popcorn":9.00,
        "fires":3.20,
        "chips":6.00,
        "soda":1.00,
        "lemonade":7.00,}

cart=[]
total=0

print("------------Menu------------")
for key,value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------")

while True:
    food = input("select an item(q to quit): ").lower()
    if food =="q":
       break
    elif menu.get(food) is not None:
        cart.append(food)
        
print("------------YOUR ORDER--------------")
for food in cart:
    total +=menu.get(food)
    print(food,end=" ")
    
print()
print(f"total is : ${total:.2f}")
