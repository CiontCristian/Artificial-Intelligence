import numpy as np


class LeastSquares:
    def __init__(self):
        self.coefficients = []

    def fit(self, input, output):
        if len(input.shape) == 1:
            input = input.reshape(-1, 1)

        ones = np.ones(input.shape[0]).reshape(-1, 1)
        input = np.concatenate((ones, input), 1)

        self.coefficients = np.linalg.inv(input.transpose().dot(input)).dot(input.transpose()).dot(output)

    def predict(self, row):
        bias = self.coefficients[0]
        values = np.array(self.coefficients[1:])

        prediction = np.sum(np.multiply(row, values)) + bias

        return prediction
