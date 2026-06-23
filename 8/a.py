import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Load Iris Dataset
iris = load_iris()
X = iris.data

k = 3

# Select first k points as initial centroids
centroids = X[:k]

for _ in range(100):

    # Calculate distances from each point to each centroid
    #distances = np.sqrt(((X[:, np.newaxis] - centroids) ** 2).sum(axis=2))
    distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)

    # Assign points to nearest centroid
    labels = np.argmin(distances, axis=1)

    # Compute new centroids
    new_centroids = []

    for i in range(k):
        cluster_points = X[labels == i]
        new_centroids.append(cluster_points.mean(axis=0))

    new_centroids = np.array(new_centroids)

    # Stop if centroids do not change
    if np.allclose(centroids, new_centroids):
        break

    centroids = new_centroids

print("\nFinal Centroids:")
for i in range(k):
    print(f"Cluster {i+1} Centroid: {centroids[i]}")

plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200)
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("K-Means Clustering on Iris Dataset")
plt.show()

# Final Centroids:
# Cluster 1 Centroid: [6.85384615 3.07692308 5.71538462 2.05384615]
# Cluster 2 Centroid: [5.88360656 2.74098361 4.38852459 1.43442623]
# Cluster 3 Centroid: [5.006 3.428 1.462 0.246]


#axis=0 → data points
#axis=1 → centroids
#axis=2 → features