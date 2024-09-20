import numpy as np 
import matplotlib.pyplot as plt 

# THE PRICES AND AREAS FOR A TOWER WITH ROOMS COUNTERS

plt.style.use('dark_background')

ax = plt.axes(projection='3d')

x = np.array([100,200,300,400,500])
y = np.array([1000,2000,3000,4000,5000])
z = np.array([1,2,3,4,5])

ax.plot3D(x, y, z, c='r')
ax.scatter3D(x, y, z, c='k')

plt.show()