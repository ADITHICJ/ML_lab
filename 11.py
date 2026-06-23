import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

class Perceptron:
    def __init__(self, n):
        self.w = np.random.rand(n)
        self.b = np.random.rand()

    def forward(self, x):
        return sigmoid(np.dot(x, self.w) + self.b)

    def train(self, X, y, epochs=1000, lr=0.1):
        for _ in range(epochs):
            for i in range(len(X)):
                error = y[i] - self.forward(X[i])
                self.w += lr * error * X[i]
                self.b += lr * error

X = np.array([[0,0],[0,1],[1,0],[1,1]])

data = {
    "AND": np.array([0,0,0,1]),
    "OR":  np.array([0,1,1,1])
}

for gate, y in data.items():
    p = Perceptron(2)
    p.train(X, y)

    print(f"\n{gate} Gate:")
    for x in X:
        print(x, "->", round(p.forward(x)))


# AND Gate:
# [0 0] -> 0
# [0 1] -> 0
# [1 0] -> 0
# [1 1] -> 1

# OR Gate:
# [0 0] -> 0
# [0 1] -> 1
# [1 0] -> 1
# [1 1] -> 1