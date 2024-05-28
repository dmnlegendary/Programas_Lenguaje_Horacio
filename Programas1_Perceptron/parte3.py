# Perceptron implementation in Python

class Perceptron:
    def __init__(self, learning_rate=0.01, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.activation_func = self._unit_step
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape

        # init parameters
        self.weights = np.zeros(n_features)
        self.bias = 0

        y_ = np.array([1 if i > 0 else 0 for i in y])

        for _ in range(self.n_iters):
            for xi, yi in zip(X, y_):
                predicted = self.predict(xi)
                update = self.lr * (yi - predicted)
                self.weights += update * xi
                self.bias += update

    def predict(self, X):
        linear_model = np.dot(X, self.weights) + self.bias
        y_predicted = self.activation_func(linear_model)
        return y_predicted

    def _unit_step(self, x):
        return np.where(x>=0, 1, 0)

# Testing the Perceptron
if __name__ == "__main__":
    # Importing necessary libraries
    import numpy as np

    # Creating a sample dataset
    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])
    y = np.array([-1, 1, 1, -1])

    # Creating an instance of the Perceptron
    model = Perceptron()

    # Training the Perceptron
    model.fit(X, y)

    # Testing the Perceptron
    predicted = [model.predict(xi) for xi in X]
    print("Predicted labels:", predicted)