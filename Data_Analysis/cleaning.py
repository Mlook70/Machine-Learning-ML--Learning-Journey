import pandas as pd 
import numpy as np 
from sklearn.impute import SimpleImputer

data = pd.read_csv('Data_Analysis\Data\data_cleaning.csv', header=0)
print(data)
print(data.shape)
print("\n")


# (1) THE FIRST WAY
# data = data.dropna()
# print(data)
# print(data.shape)
# print("\n")


# (2) THE SEC WAY
# imputer = SimpleImputer(missing_values= np.nan , strategy="mean")
# cleard_data = imputer.fit_transform(data)
# print(cleard_data)
# print(cleard_data.shape)
# print("\n")

# new_data = pd.DataFrame(cleard_data, columns=data.columns)
# print(new_data)


# (3) THE SEC WAY
# new_data = data.drop(["ID"] , axis=1)
# print(new_data)