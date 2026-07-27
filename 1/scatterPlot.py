import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()

X = iris.data
y = iris.target

# Scatter plot
plt.scatter(X[:, 0], X[:, 1], c=y)

plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Iris Dataset Scatter Plot")

plt.show()