import matplotlib.pyplot as plt

import numpy as np

#Histogram = A visual representation of the distribution of quantitative data.|| they group values into bins(intervals) and counts how many fall in each range 

scores = np.random.normal(loc=80,scale=10,size=100)
scores=np.clip(scores,0,100)

plt.hist(scores,bins=10,
                color="skyblue",
                edgecolor="black",
                alpha=0.7)


plt.title("exam scores")
plt.xlabel("score")
plt.ylabel("# of students ")


plt.show()