import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Load Fruit Dataset from URL
url = "https://raw.githubusercontent.com/susanli2016/Machine-Learning-with-Python/master/fruit_data_with_colors.txt"

fruit_df = pd.read_table(url)

# Features and Target
X = fruit_df[['mass', 'width', 'height', 'color_score']]
y = fruit_df['fruit_label']

# K values
k_values = [3, 5, 7]

# Train-Test Splits
test_sizes = [0.1, 0.3]

# Distance Metrics
distance_metrics = [
    ('Euclidean', 'euclidean'),
    ('Manhattan', 'manhattan')
]

for test_size in test_sizes:

    print("\n================================")
    print(f"Train-Test Split = {int((1-test_size)*100)}-{int(test_size*100)}")
    print("================================")

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=42
    )

    for name, metric in distance_metrics:

        print(f"\n--- Distance Metric: {name} ---")

        for k in k_values:

            knn = KNeighborsClassifier(
                n_neighbors=k,
                metric=metric
            )

            knn.fit(X_train, y_train)

            y_pred = knn.predict(X_test)

            acc = accuracy_score(y_test, y_pred)
            # cm = confusion_matrix(y_test, y_pred)

            print(f"\nK = {k}")
            print(f"Accuracy: {acc:.4f}")
            # print("Confusion Matrix:")
            # print(cm)
            
# ================================
# Train-Test Split = 90-10
# ================================

# --- Distance Metric: Euclidean ---

# K = 3
# Accuracy: 0.6667

# K = 5
# Accuracy: 0.6667

# K = 7
# Accuracy: 0.6667

# --- Distance Metric: Manhattan ---

# K = 3
# Accuracy: 0.6667

# K = 5
# Accuracy: 0.6667

# K = 7
# Accuracy: 0.6667

# ================================
# Train-Test Split = 70-30
# ================================

# --- Distance Metric: Euclidean ---

# K = 3
# Accuracy: 0.4444

# K = 5
# Accuracy: 0.3889

# K = 7
# Accuracy: 0.5556

# --- Distance Metric: Manhattan ---

# K = 3
# Accuracy: 0.4444

# K = 5
# Accuracy: 0.3889

# K = 7
# Accuracy: 0.5556