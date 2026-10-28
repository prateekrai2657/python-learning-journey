import numpy as np

#comparison operator 

scores = np.array([78,53,89,90,98,43,67,32])

scores[scores<60] = 0 
print(scores)


#airthmetic operation

array1=np.array([1,2,3])
array2=np.array([5,6,9])

print(array1+array2)

print(array1-array2)
print(array1*array2)
print(array1 / array2)
print(array1 **array2)

#exercise

radii = np.array([1,2,3])

print(np.pi * radii**2)

# vectiorized math function

array = np.array([1.01,  9.7, 16.2, ])
print(np.sqrt(array))
print(np.round(array))
print(np.pi)
