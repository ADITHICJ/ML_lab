import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

X = load_iris().data

plt.boxplot(X, labels=["Sepal L", "Sepal W", "Petal L", "Petal W"])

plt.title("Box Plot of Iris Dataset")
plt.show()