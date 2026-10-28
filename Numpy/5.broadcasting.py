import numpy as np

# broadcasting allows numpy to perform operations on array
# with different shapes by virtually expanding dimension
# it should have same size for ex 10 in row or column or it should have 1

array1=np.array([[1,2,3,4,5,6,7,8,9,10]])
array2=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

print(array1.shape)
print(array2.shape)
print(array1*array2)