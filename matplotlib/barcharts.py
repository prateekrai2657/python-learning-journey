import matplotlib.pyplot as plt

import numpy as np

#barcharts = compare categories of data by representing each category with a bar

categories = np.array(["Grains","Vegetables","Fruits","Protein","Sweets"])
values = np.array([25,30,15,20,10])

plt.bar(categories, values,color="skyblue")

plt.title("Daily Consumption")
plt.xlabel("Food Categories")
plt.ylabel("Consumption (grams)")

plt.show()
