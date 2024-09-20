import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Today's sales FOR A SHOPE

plt.style.use('dark_background')

month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
users = [120,200, 150, 200, 150, 300, 450, 200, 10, 155, 500, 233]

plt.title("ONLINE BOOKING SYSTEM")
plt.xlabel("Month")
plt.ylabel("Users")

plt.bar(month, users, edgecolor='black', facecolor='white')

plt.show()
