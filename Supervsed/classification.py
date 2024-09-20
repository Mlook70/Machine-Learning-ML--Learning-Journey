import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv('Datasets\diabetes.csv', header=0)

x = data.iloc[: , : -1]
y = data.iloc[: , -1]

print(x)

x_train , x_test , y_train , y_test = train_test_split(x,y , train_size=0.80)

model = LogisticRegression()
model.fit(x_train, y_train)

print(model.score(x_train, y_train))
print(model.score(x_test, y_test))
