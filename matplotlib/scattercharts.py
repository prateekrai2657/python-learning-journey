import matplotlib.pyplot as plt

import numpy as np

x1=np.array([0,1,1,2,3,4,5,6,7,8])
y1=np.array([20,40,45,50,60,70,83,85,92,96])

x2=np.array([0,1,2,2,4,5,6,6,7,8])
y2=np.array([20,34,65,34,50,70,89,85,92,96])

plt.scatter(x1,y1,color="skyblue", s=200,label="Class A")
plt.scatter(x2,y2,color="red", s=200,label="Class B")

plt.title("Test scores")
plt.xlabel("Number of hours studied")
plt.ylabel("Grade")

plt.legend()

plt.show()