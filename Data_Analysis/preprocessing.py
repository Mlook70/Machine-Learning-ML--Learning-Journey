import pandas as pd
import numpy as np
from sklearn import preprocessing

users = [
    [1, "KSA"],
    [2, "USA"],
    [3, "KSA"],
    [4, "UAE"],
    [5, "USA"],
]

data = pd.DataFrame(users, columns=["ID", "COUNTRY"])

print(data)
print("\n")

le = preprocessing.LabelEncoder()
labeling = le.fit_transform(data["COUNTRY"])
print(labeling)
print("\n")

data["COUNTRY"] = labeling
print(data)
print("\n")

print(le.classes_)
