import numpy as np


def identical(x):
    return x


def dIdentical(x):
    return 1


class Network:
    def __init__(self, structure):
        self.structure = structure

        self.weights1 = np.random.randn(self.structure[0], self.structure[1])
        self.weights2 = np.random.randn(self.structure[1], self.structure[2])

        self.result = None

    def feedForward(self, input):
        self.result = identical(np.dot(input, self.weights1))
        output = np.dot(self.result, self.weights2)

        return output

    def backProp(self, input, output, fx):
        error = output - fx
        delta = error * np.ones(fx.shape)

        result_error = np.dot(delta, self.weights2.transpose())
        result_delta = result_error * dIdentical(self.result)

        self.weights1 -= np.dot(input.transpose(), result_delta)
        self.weights2 -= np.dot(self.result.transpose(), delta)

    def train(self, input, output):
        result = self.feedForward(input)
        self.backProp(input, output, result)

    def predict(self, input):
        return self.feedForward(input)
