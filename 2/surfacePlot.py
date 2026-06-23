import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    c: np.random.normal(size=100)
    for c in ['X', 'Y', 'Z']
})
data['Category'] = np.random.choice(['A', 'B', 'C'], 100)

x = y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# 3D Surface Plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title("3D Surface Plot")
plt.show()