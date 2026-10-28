# python Temperature convertor program
unit = input("Is this temperature in Celsius or Fahrenhiet (C OR F) : ")
temperature = float(input("Enter the temperature : "))

if unit == "C":
    temperature = round((9* temperature) /5 +32,1)
    print(f"The temperature in Fahrenhiet is : {temperature} °F")
elif unit == "F":
    temperature = round((5*(temperature-32))/9,1)
    print(f"The temperature in Celsius is : {temperature} °C")
else:
    print(f"{unit} was not valid")