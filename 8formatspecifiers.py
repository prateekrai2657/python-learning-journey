# format specifiers = {value:flags} format a value based on what flags are inserted 
price1 = 30000.2389273817
price2 = -9870.65
price3 = 1200.4567

print(f"price 1 is ${price1:+.2f}")  # comma as thousand separator and 2 decimal places
print(f"price 2 is ${price2:-.2f}")  # comma as thousand separator and 2 decimal places
print(f"price 3 is ${price3:+.2f}")  # comma as thousand separator and 2 decimal places
