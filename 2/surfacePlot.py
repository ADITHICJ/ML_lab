import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

X = load_iris().data

x = np.linspace(min(X[:, 2]), max(X[:, 2]), 50)
y = np.linspace(min(X[:, 3]), max(X[:, 3]), 50)

x, y = np.meshgrid(x, y)

z = np.sin(x) * np.cos(y)

ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z)

plt.title("3D Surface Plot")
plt.show()