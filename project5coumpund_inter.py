# Python compund interest calculator 

principle = 0
rate=0
time=0

while principle <=0 :
    principle=float(input("Enter the principle amount : "))
    if principle <=0:
        print("PI cannot be less than zero")
        
while time <=0 :
    time =int(input("Enter the time : "))
    if time <=0:
        print("time cannot be less than zero")

while rate <=0 :
    rate=float(input("Enter the rate : "))
    if rate <=0:
        print(" rate cannot be less than zero")
total  = principle *pow((1+rate/100),time)
print(f"Balance after {time} years : ${total:.2f}")