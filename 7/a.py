import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Load Glass Dataset
columns = [
    'Id', 'RI', 'Na', 'Mg', 'Al',
    'Si', 'K', 'Ca', 'Ba', 'Fe', 'Type'
]

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data"
glass_df = pd.read_csv(url, names=columns)

# Drop Id column
glass_df.drop('Id', axis=1, inplace=True)

# Features and Target
X = glass_df.drop('Type', axis=1)
y = glass_df['Type']

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Distance metrics to compare
distance_metrics = ['euclidean', 'manhattan']

for metric in distance_metrics:
    # Create and train KNN model
    knn = KNeighborsClassifier(
        n_neighbors=3,
        metric=metric
    )

    knn.fit(X_train, y_train)

    # Predict on test data
    y_pred = knn.predict(X_test)

    # Calculate accuracy and confusion matrix
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    print(f"KNN using {metric.capitalize()} Distance")
    print(f"Accuracy: {acc:.4f}")
    print("\nConfusion Matrix:")
    print(cm)
    