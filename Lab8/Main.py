import numpy as np
from Network import Network

def read():
    with open("data.txt", 'r') as f:
        lines = f.readlines()
        lines = [line.split() for line in lines]

        input = []
        output = []
        for row in lines:
            input.append([float(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4])])
            output.append([float(row[5])])

        return np.array(input), np.array(output)


def computeLoss(output, fx):
    return (np.square(output - fx)).mean()


input_data, output_data = read()

network = Network([5, 3, 2])
for _ in range(2):
    network.train(input_data, output_data)

pred = network.predict(input_data)

print(computeLoss(output_data, pred))
