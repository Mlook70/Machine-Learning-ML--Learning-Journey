import numpy as np 

numbers = np.arange(1, 10)

np.random.shuffle(numbers)

print(numbers)

maxmuim = numbers.max()
max_index = numbers.argmax()

print("Maxmuim : " + str(maxmuim))
print("Maxmuim Index: " + str(max_index))

ra = np.random.randint(100, 200, (3, 3))

shape = ra.shape

print(shape)
