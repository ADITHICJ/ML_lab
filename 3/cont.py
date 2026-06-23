import numpy as np
import matplotlib.pyplot as plt

x = y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

plt.contour(X, Y, Z)

plt.title("Contour Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()