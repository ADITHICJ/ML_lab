import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import load_iris

iris = load_iris()
data = iris.data[:6]

def proximity_matrix(data):
  n = data.shape[0]
  proximity_matrix = np.zeros((n, n))
  for i in range(n):
    for j in range(i+1, n):
        proximity_matrix[i, j] = np.linalg.norm(data[i] - data[j])
        proximity_matrix[j, i] = proximity_matrix[i, j]
  return proximity_matrix

def plot_dendrogram(data, method):
  linkage_matrix = linkage(data, method=method)
  dendrogram(linkage_matrix)
  plt.title(f'Dendrogram - {method} linkage')
  plt.xlabel('Data Points')
  plt.ylabel('Distance')
  plt.show()

print("Proximity matrix:")
pm = proximity_matrix(data)
print(proximity_matrix(data))

plot_dendrogram(data, 'single')
plot_dendrogram(data, 'complete')

# Proximity matrix:
# [[0.         0.53851648 0.50990195 0.64807407 0.14142136 0.6164414 ]
#  [0.53851648 0.         0.3        0.33166248 0.60827625 1.09087121]
#  [0.50990195 0.3        0.         0.24494897 0.50990195 1.08627805]
#  [0.64807407 0.33166248 0.24494897 0.         0.64807407 1.16619038]
#  [0.14142136 0.60827625 0.50990195 0.64807407 0.         0.6164414 ]
#  [0.6164414  1.09087121 1.08627805 1.16619038 0.6164414  0.        ]]