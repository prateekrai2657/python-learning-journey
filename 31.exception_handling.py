# exception = An event that interupts the flow of a program | (zerodividion error ,type error,value error) | 1. try,2.except 3. finally
try:
    number = int(input("enter a number : "))
    print(1/number)  
except ZeroDivisionError:
    print("You can't divide by zero IDIOT!")

except ValueError:
    print("enter only numbers plzz")

finally:
    print("DO some cleanup here ")
    
