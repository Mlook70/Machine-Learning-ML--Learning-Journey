# NAME : ABDULMALEK MARWAN MOHAMMED AKEL
# NUMBER : B2005.090015
# ISTANBUL AYDIN UNIVERSITY
# AI FINAL EXAM CANSER PROJECT USING K-MEANS ALGORTHIM
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

# Load cancer patient data
df = pd.read_csv('C:/Users/mlook/ML/Data/cancer_data.csv', header=0)
df.head()

print(df)

plt.scatter(df.Age, df.Tumor)
plt.xlabel('Age')
plt.show()

c_num = []
j = []
for i in range(1, 10):
    km = KMeans(n_clusters=i)
    km.fit(df[["Age", "Tumor"]])
    c_num.append(i)
    j.append(km.inertia_)

plt.plot(c_num, j)
plt.show()

km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df[['Age', 'Tumor']])
y_predicted

df['cluster'] = y_predicted
df.head()

km.cluster_centers_

df1 = df[df.cluster == 0]
df2 = df[df.cluster == 1]
df3 = df[df.cluster == 2]
plt.scatter(df1.Age, df1['Tumor'], color='green')
plt.scatter(df2.Age, df2['Tumor'], color='red')
plt.scatter(df3.Age, df3['Tumor'], color='blue')
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[
            :, 1], color='purple', marker='*', label='centroid')
plt.xlabel('Age')
plt.ylabel('Tumor Size')
plt.legend()

plt.show()