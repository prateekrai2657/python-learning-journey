import matplotlib.pyplot as plt

import numpy as np

# pie charts = Circular chart divided into slices to show percentages of the total || good for visualizing among categories 

categories = ["Freshers","juniors","seniors","super seniors"]
values=np.array([280,300,210,170])
colors = ["red","green","orange","blue"]

plt.pie(values, labels=categories,
                autopct="%1.1f%%",
                colors=colors,
                explode=[0,0,0,0.1],
                shadow = True,
                startangle=90)

plt.title("Haridwar University")

plt.show()