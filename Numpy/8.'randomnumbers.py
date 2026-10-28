import numpy as np

rng = np.random.default_rng()
# array=np.array([1,2,3,4,5])
# rng.shuffle(array)
# print(array)
# print(rng.integers(low=1,high=7))
# print(rng.integers(low=1,high=101,size=(5,5)))

# print(np.random.uniform(low=-1,high=1,size=3))

fruits =["apple","orange","mango","banana","grapes"]
fruits =rng.choice(fruits,size=2)

print(fruits)