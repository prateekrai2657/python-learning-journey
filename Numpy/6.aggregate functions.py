import numpy as np

#aggregate functions = summarize data and typically returns a single value 

array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])
# print(np.sum(array))
# print(np.mean(array))
# print(np.std(array)) #standard deviation
# print(np.sum(array)) # variance
# print(np.min(array))
# print(np.max(array))
# print(np.argmin(array))
# print(np.argmax(array))

print(np.sum(array, axis=0))#column
print(np.sum(array, axis=1))#row

