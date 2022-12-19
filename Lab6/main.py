from Problem import Problem
from math import floor
from random import shuffle


def readData():
    d = []
    with open("balance-scale.data", 'r') as f:
        for line in f.readlines():
            i = line.split(',')
            classType = i.pop(0)
            i = [int(value) for value in i]
            i.append(classType)
            d.append(i)
    return d


data = readData()
dataSplit = floor(0.8 * len(data))
shuffle(data)

test = data[dataSplit:]
data = data[:dataSplit]

problem = Problem()
tree = problem.buildTree(data)

total, correct = 0, 0

for row in test:
    predict = problem.prediction(row, tree)
    predict = max(predict.items(), key=lambda x: x[1])
    total += 1
    if predict[0] == row[-1]:
        correct += 1

print(round(float(correct / total), 2))
