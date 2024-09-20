import numpy as np

ra1 = np.random.rand(3,3)

ra2 = np.random.randint(100,200,(3,3))

no_shape = np.random.randint(100, 200, 10)

shape = no_shape.reshape(5,2)

print(ra1)
print(ra2)

print("\n")
print(shape)
