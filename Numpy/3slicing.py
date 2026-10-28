import numpy as np

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

# array[start:end:step]

# print(array[0])
# print(array[2])
# print(array[0:3]) # end is exclusive if you need second row you have to type 3
print(array[0:3:2])
print(array[0:2,0:2])
