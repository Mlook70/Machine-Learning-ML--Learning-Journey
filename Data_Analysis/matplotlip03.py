import numpy as np
import matplotlib.pyplot as plt

# The percentage of cars in the show

plt.style.use('dark_background')
numbers = [2, 1, 3, 4]
cars = ['Merceds', 'BMW', 'Audi', 'Kia']

plt.pie(
    numbers, labels=cars, autopct='%1.0f%%'
)

plt.show()
