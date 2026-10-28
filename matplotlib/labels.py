import matplotlib.pyplot as plt
import numpy as np
x = np.array([2023,2024,2025,2026])
y1= np.array([15,25,30,20])
y2= np.array([17,23,38,5])
y3= np.array([2,34,49,50])

plt.title("Class Size",fontsize=25,
                     family="Arial",
                     fontweight="bold",
                     color="Blue")

plt.xlabel("Year",fontsize=20,
           family="Arial",
           fontweight="bold",
           color="#2dbefc")

plt.ylabel("Number of Students",fontsize=20,
           family="Arial",
           fontweight="bold",
           color="#6fbcdf")

plt.tick_params(axis="both",
                colors="#b4cb1d")

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)

plt.show()