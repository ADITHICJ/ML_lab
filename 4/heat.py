import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

X = load_iris().data

sns.heatmap(X, cmap="viridis")

plt.title("Heat Map of Iris Dataset")

plt.show()