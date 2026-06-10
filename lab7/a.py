import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# Load Glass dataset
columns = ['Id', 'RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'Type']

data = pd.read_csv(
    "https://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data",
    names=columns
)

# Remove Id column
X = data.drop(['Id', 'Type'], axis=1)
y = data['Type']

splits = [0.1, 0.3]
k_values = [3, 5, 7]
metrics = ['euclidean', 'manhattan']

for test_size in splits:
    print("\n================================")
    print(f"Train-Test Split = {int((1-test_size)*100)}-{int(test_size*100)}")
    print("================================")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    for metric in metrics:
        print("\nDistance Metric:", metric)

        for k in k_values:
            model = KNeighborsClassifier(n_neighbors=k, metric=metric)
            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)

            print("\nK =", k)
            print("Accuracy:", accuracy_score(y_test, y_pred))
            
# ================================
# Train-Test Split = 90-10
# ================================

# Distance Metric: euclidean

# K = 3
# Accuracy: 0.9090909090909091

# K = 5
# Accuracy: 0.7272727272727273

# K = 7
# Accuracy: 0.7727272727272727

# Distance Metric: manhattan

# K = 3
# Accuracy: 0.8636363636363636

# K = 5
# Accuracy: 0.8636363636363636

# K = 7
# Accuracy: 0.8181818181818182

# ================================
# Train-Test Split = 70-30
# ================================

# Distance Metric: euclidean

# K = 3
# Accuracy: 0.6461538461538462

# K = 5
# Accuracy: 0.6307692307692307

# K = 7
# Accuracy: 0.6615384615384615

# Distance Metric: manhattan

# K = 3
# Accuracy: 0.676923076923077

# K = 5
# Accuracy: 0.7230769230769231

# K = 7
# Accuracy: 0.676923076923077
            