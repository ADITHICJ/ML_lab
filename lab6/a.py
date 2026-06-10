from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

iris = load_iris()

X = iris.data
y = iris.target

for test_size in [0.1, 0.3]:   # 90-10 and 70-30

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=test_size,
        random_state=42
    )

    model = GaussianNB()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("\n================================")
    print(f"Train-Test Split = {int((1-test_size)*100)}-{int(test_size*100)}")
    print("================================")

    print("Accuracy :", accuracy_score(y_test, y_pred))

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
# ================================
# Train-Test Split = 90-10
# ================================
# Accuracy : 1.0

# Confusion Matrix:
# [[6 0 0]
#  [0 6 0]
#  [0 0 3]]

# ================================
# Train-Test Split = 70-30
# ================================
# Accuracy : 0.9777777777777777

# Confusion Matrix:
# [[19  0  0]
#  [ 0 12  1]
#  [ 0  0 13]]