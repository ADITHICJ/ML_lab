import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# Load Titanic Dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
data = pd.read_csv(url)

# Select useful columns
data = data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Survived']]

# Handle missing values
data['Age'] = data['Age'].fillna(data['Age'].mean())

# Convert categorical data to numeric
le = LabelEncoder()
data['Sex'] = le.fit_transform(data['Sex'])

X = data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']]
y = data['Survived']

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
# Accuracy : 0.8111111111111111

# Confusion Matrix:
# [[44 10]
#  [ 7 29]]

# ================================
# Train-Test Split = 70-30
# ================================
# Accuracy : 0.7910447761194029

# Confusion Matrix:
# [[130  27]
#  [ 29  82]]