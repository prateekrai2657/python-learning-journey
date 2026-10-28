import matplotlib.pyplot as plt
import numpy as np

# grid() = Helps make plots easier to read by adding reference lines.
x=[1,2,3,4,5]
y=[6,7,8,9,10]

plt.grid(axis="y",
         linewidth=2,
         color="yellow",
         linestyle="dashed")

plt.plot(x,y)
plt.show()