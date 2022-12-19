from LeastSquares import LeastSquares
import numpy as np


def read():
    with open("data.txt", 'r') as f:
        lines = f.readlines()
        lines = [line.split() for line in lines]

        input = []
        output = []
        for row in lines:
            input.append([float(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4])])
            output.append(float(row[5]))

        return np.array(input), np.array(output)


def computeLoss(output, fx):
    return (np.square(output - fx)).mean()


input, output = read()
regression = LeastSquares()
regression.fit(input, output)

output_pred = [regression.predict(row) for row in input]

print(computeLoss(output, output_pred))
