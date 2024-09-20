import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
import numpy as np

list = [
    [5.11 , 3.51 , 1.41 , 0.51 , "AAA"],
    [4.92, 2.71, 1.13, 0.62, "BAA"],
    [4.75, 2.81, 0.91, 0.42, "CAA"],
    [4.64, 3.21, 1.33, 0.35, "DAA"],
    [5.03, 3.11, 1.51, 0.24, "EAA"],
    [5.42, 3.93, 1.42, 0.12, "ABA"],
    [5.04, 3.03, 1.41, 0.53, "ACA"],
    [4.83, 2.63, 1.15, 0.65, "AEA"],
    [4.51, 2.93, 0.94, 0.46, "ADA"],
    [4.31, 3.12, 1.32, 0.37, "AAB"],
    [5.41, 3.31, 1.53, 0.28, "AAC"],
    [5.11, 3.93, 1.42, 0.11, "AAE"],
]

df = pd.DataFrame(list , columns=["cats" , "dogs" , "monkey" , "lion" , "label"])

# DATA CLEANING OR PREPROSCESSING 
df = df.drop(["label"], axis=1)

c_num = []
j = []

# for i in range(1,10):
#     model = KMeans(n_clusters = i)
#     model.fit(dataset)
#     c_num.append(i)
#     j.append(model.inertia_)

# plt.plot(c_num ,j)
# plt.show()

model = KMeans(n_clusters=5)
label = model.fit(df)

print(label)

