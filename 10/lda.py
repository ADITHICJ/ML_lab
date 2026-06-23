import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Unique classes
classes = np.unique(y_train)

# Overall mean
overall_mean = np.mean(X_train, axis=0)

# Within-class scatter matrix
SW = np.zeros((X_train.shape[1], X_train.shape[1]))

# Between-class scatter matrix
SB = np.zeros((X_train.shape[1], X_train.shape[1]))

for c in classes:
    X_c = X_train[y_train == c]

    class_mean = np.mean(X_c, axis=0)

    # Within-class scatter
    SW += (X_c - class_mean).T.dot(X_c - class_mean)

    # Between-class scatter
    n_c = X_c.shape[0]
    mean_diff = (class_mean - overall_mean).reshape(-1, 1)
    SB += n_c * mean_diff.dot(mean_diff.T)

# Solve eigenvalue problem
A = np.linalg.inv(SW).dot(SB)
eigenvalues, eigenvectors = np.linalg.eig(A)

# Sort eigenvectors by descending eigenvalues
idx = np.argsort(eigenvalues)[::-1]
eigenvectors = eigenvectors[:, idx]

# Select first 2 discriminant components
W = eigenvectors[:, :2]

# Transform data
X_train_lda = X_train.dot(W)
X_test_lda = X_test.dot(W)

print("Original Training Shape :", X_train.shape)
print("Reduced Training Shape  :", X_train_lda.shape)

print("\nFirst 5 transformed samples:")
print(X_train_lda[:5])