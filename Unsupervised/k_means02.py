import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


X = np.array([[random.uniform(-1, 1), random.uniform(-1, 1)]
            for i in range(50)])
y = np.array([[random.uniform(-1, 1), random.uniform(-1, 1)]
            for i in range(50)])


def calculate_WSS(points, kmax):
    sse = []
    for k in range(1, kmax+1):
        KMeans = KMeans(n_clusters=k).fit(points)
        centroids = KMeans.cluster_centers_
        pred_clusters = KMeans
        predict(points)
        curr_sse = 0

    for i in range(len(points)):
        curr_center = centroids[pred_clusters[i]]
        curr_sse += (points[i, 0] - curr_center[0]) * 2 + \
          (points[i, 1] - curr_center[1]) * 2

    sse.append(curr_sse)
    return sse


kmeans.fit(X, y)


plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_)
plt.scatter(y[:, 0], y[:, 1], c=kmeans.labels_)
plt.show()
