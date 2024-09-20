from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn

list = [
    [111, 'Male', 19, 19000, 0],
    [111, 'Male', 35, 43000, 0],
    [111, 'Famale', 26, 20000, 0],
    [111, 'Famale', 27, 57000, 1],
    [111, 'Male', 19, 76000, 0],
    [111, 'Famale', 25, 50000, 0],
]
dataset = pd.DataFrame(list, columns=["User ID", "Gender", "Age", "Estimated Salary", "Purchased"])
X = dataset.iloc[:, [1, 2, 3]].values
y = dataset.iloc[:, -1].values

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X[:,0] = le.fit_transform(X[:,0])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
ac = accuracy_score(y_test, y_pred)
