import time 
my_time = int(input("Enter the time in seconds : "))   
 
for x in range (my_time,0,-1):
    secondS  = x % 60
    minutes = int(x/60) % 60
    hours = int(x/3600)   
    print(f"{hours:02}:{minutes:02}:{secondS:02}")

time.sleep(0.5)

print("wake up")