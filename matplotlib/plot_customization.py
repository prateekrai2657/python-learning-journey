import matplotlib.pyplot as plt
import numpy as np
x = np.array([2023,2024,2025,2026])
y1= np.array([15,25,30,20])
y2= np.array([17,23,38,5])
y3= np.array([2,34,49,50])

line_style = dict(marker=".",
                markersize=20,
                markerfacecolor="red",
                markeredgecolor="blue",
                linestyle="solid",
                linewidth=4,)

plt.plot(x , y1, color="#6e93f0",**line_style)

plt.plot(x , y2, color="#90ed88",**line_style)

plt.plot(x,y3, color="#ed45e5",**line_style)

plt.show()