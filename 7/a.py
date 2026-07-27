from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np

glass = fetch_openml("glass", as_frame=True)

X = glass.data
y = glass.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Euclidean Distance Formula
def euclidean_distance(x, y):
    return np.sqrt(np.sum((x - y) ** 2))

# Manhattan Distance Formula
def manhattan_distance(x, y):
    return np.sum(np.abs(x - y))

metrics = {
    "Euclidean": euclidean_distance,
    "Manhattan": manhattan_distance
}

for name, distance_function in metrics.items():

    knn = KNeighborsClassifier(
        n_neighbors=3,
        metric=distance_function
    )

    knn.fit(X_train, y_train)

    y_pred = knn.predict(X_test)

    print(f"\nKNN using {name} Distance")
    print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

# KNN using Euclidean Distance
# Accuracy: 69.23%
# Confusion Matrix:
# [[14  3  0  0  0  1]
#  [ 8 18  1  0  0  0]
#  [ 0  1  4  0  0  0]
#  [ 0  2  0  7  1  0]
#  [ 0  0  0  0  1  0]
#  [ 3  0  0  0  0  1]]


# KNN using Manhattan Distance
# Accuracy: 72.31%
# Confusion Matrix:
# [[16  1  0  0  0  1]
#  [ 7 18  2  0  0  0]
#  [ 0  1  4  0  0  0]
#  [ 0  2  0  7  1  0]
#  [ 0  0  0  0  1  0]
#  [ 3  0  0  0  0  1]]