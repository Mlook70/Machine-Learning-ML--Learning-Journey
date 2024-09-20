from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('C:/Users/mlook/ML/Data/data_cancer.csv', header=0)
dataset.head()

plt.scatter(dataset["Age"], dataset["Smooking"])
plt.show()


cluster_num = []
j = []
for i in range(1,10):
    model = KMeans(n_clusters=i)
    model.fit(dataset[["Age" , "Smooking"]])
    cluster_num.append(i)
    j.append(model.inertia_)
    
plt.plot(cluster_num , j)  
plt.show()  

model = KMeans(n_clusters=3)
y_p = model.fit_predict(dataset[['Age', 'Smooking']])
y_p

dataset['c'] = y_p
dataset.head()
model.cluster_centers_

dataset_0 = dataset[dataset.c == 0]
dataset_1 = dataset[dataset.c == 1]
dataset_2 = dataset[dataset.c == 2]

plt.scatter(dataset_0.Age, dataset_0.Smooking, color='red')
plt.scatter(dataset_1.Age, dataset_1.Smooking, color='yellow')
plt.scatter(dataset_2.Age, dataset_2.Smooking, color='blue')

plt.scatter(model.cluster_centers_[:, 0],
             model.cluster_centers_[:, 1], color='black')
plt.legend()
plt.show()


