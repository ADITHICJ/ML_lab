import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

X = load_iris().data

x = np.linspace(min(X[:, 2]), max(X[:, 2]), 50)
y = np.linspace(min(X[:, 3]), max(X[:, 3]), 50)

x, y = np.meshgrid(x, y)

z = np.sin(x) * np.cos(y)

plt.contourf(x, y, z, cmap="viridis")

plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("Contour Plot of Iris Dataset")

plt.show()