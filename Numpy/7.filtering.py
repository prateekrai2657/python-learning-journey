import numpy as np

#filtering= refers to the process of selecting elements from an array that match a given condition
ages = np.array([[15,24,35,45,52,65,75],
                 [99,22,16,19,20,21,43]])

teenagers= ages[ages<18]
adults = ages[(ages>18)&(ages<65)]
seniors = ages[ages>65]
even_ages = ages[ages % 2 == 0]

print(teenagers)
print(adults)
print(seniors)
print(even_ages)

# if you want to preserve the shape of the array you may use where function

adults=np.where(ages>=24,ages,0)
print(adults)