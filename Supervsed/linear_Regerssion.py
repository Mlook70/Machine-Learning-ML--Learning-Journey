import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
plt.style.use('dark_background')

lis = [ [65.0, 60.5], [50.0, 47.4], [15.0, 17.2], [38.0, 36.5], [87.0, 87.2], 
        [36.0, 32.4], [12.0, 10.7], [81.0, 80.7], [25.0, 24.6], [20.0, 20.6], 
        [70.0, 75.6], [78.0, 77.0], [85.0, 82.6], [90.0, 87.6],
    ]

dataset = pd.DataFrame(lis, columns=["X", "Y"])
print(dataset)

x = dataset.iloc[:, :-1]
y = dataset.iloc[:,-1]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7)

m = LinearRegression()
m.fit(x_train, y_train)

print("ACCURATELY = " + str(m.score(x_train, y_train)))
print("ACCURATELY = " + str(m.score(x_test, y_test)))

plt.title("Linear Regression { TRAIN DATASET }")
plt.scatter(x_train, y_train, color="red")
plt.plot(x_train, m.predict(x_train), color="yellow")
plt.show()

plt.title("Linear Regression { TEST DATASET }")
plt.scatter(x_test, y_test, color="red")
plt.plot(x_test, m.predict(x_test), color="green")
plt.show()

plt.title("Linear Regression { ALL DATASET }")
plt.scatter(x, y)
plt.plot(x, m.predict(x), color="red")
plt.show()
