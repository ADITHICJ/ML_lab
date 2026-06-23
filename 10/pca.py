import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

class PCA:
    def __init__(self, n_components):
        self.n_components = n_components

    def fit(self, X):
        self.mean = np.mean(X, axis=0)
        X = X - self.mean

        cov = np.cov(X.T)
        eigenvalues, eigenvectors = np.linalg.eig(cov)

        eigenvectors = eigenvectors.T[np.argsort(eigenvalues)[::-1]]
        self.components = eigenvectors[:self.n_components]

    def transform(self, X):
        return np.dot(X - self.mean, self.components.T)

iris = load_iris()
X = iris.data
y = iris.target

pca = PCA(2)
pca.fit(X)
X_pca = pca.transform(X)

print("Original Shape:", X.shape)
print("Reduced Shape:", X_pca.shape)

plt.scatter(X_pca[:,0], X_pca[:,1], c=y, cmap='jet')
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA")
plt.show()