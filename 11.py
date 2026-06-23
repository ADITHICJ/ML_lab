import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

class Perceptron:
    def __init__(self, input_size):
        self.weights = np.random.rand(input_size)
        self.bias = np.random.rand()   # Scalar bias

    def forward(self, inputs):
        total_input = np.dot(inputs, self.weights) + self.bias
        output = sigmoid(total_input)
        return output

    def train(self, X, y, epochs=1000, learning_rate=0.1):
        for epoch in range(epochs):
            for i in range(X.shape[0]):
                output = self.forward(X[i])
                error = y[i] - output

                self.weights += learning_rate * error * X[i]
                self.bias += learning_rate * error

# Input data
X_and = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# AND outputs
y_and = np.array([0, 0, 0, 1])

# OR outputs
y_or = np.array([0, 1, 1, 1])

# Create perceptrons
perceptron_and = Perceptron(input_size=2)
perceptron_or = Perceptron(input_size=2)

# Train perceptrons
perceptron_and.train(X_and, y_and, epochs=1000, learning_rate=0.1)
perceptron_or.train(X_and, y_or, epochs=1000, learning_rate=0.1)

# Test AND gate
print("AND Function Predictions:")
for i in range(X_and.shape[0]):
    prediction = round(perceptron_and.forward(X_and[i]))
    print("Input:", X_and[i], "- Predicted Output:", prediction)

# Test OR gate
print("\nOR Function Predictions:")
for i in range(X_and.shape[0]):
    prediction = round(perceptron_or.forward(X_and[i]))
    print("Input:", X_and[i], "- Predicted Output:", prediction)