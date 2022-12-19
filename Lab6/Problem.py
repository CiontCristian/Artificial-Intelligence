import math
from collections import Counter
from Node import Node
from Leaf import Leaf


class Problem:

    def createNodes(self, data, question):
        d = {}
        for row in data:
            if row[question] in d:
                d[row[question]].append(row)
            else:
                d[row[question]] = [row]

        aux = {}
        for key in sorted(d.keys()):
            aux[key] = d[key]

        return aux

    def computeClassEntropy(self, classR, classL, classB, total):
        val1, val2, val3 = 0, 0, 0
        if classR != 0:
            val1 = -(classR / total * math.log2(classR / total))
        if classL != 0:
            val2 = -(classL / total * math.log2(classL / total))
        if classB != 0:
            val3 = -(classB / total * math.log2(classB / total))

        return val1 + val2 + val3

    def computeInformationGain(self, data, column):
        d = self.createNodes(data, column)
        columnEntropy = 0
        columnCounter = []
        for node in d:
            columnCounter.append(Counter([row[-1] for row in d[node]]))
            columnEntropy += (len(d[node]) / len(data)) * self.computeClassEntropy(columnCounter[-1]['R'],
                                                                                   columnCounter[-1]['L'],
                                                                                   columnCounter[-1]['B'],
                                                                                   len(d[node]))
        dataCounter = Counter(row[-1] for row in data)
        dataEntropy = self.computeClassEntropy(dataCounter["R"], dataCounter["L"], dataCounter["B"], len(data))

        return dataEntropy - columnEntropy

    def findBestRoot(self, data):
        bestQuestion = 0
        bestInfoGain = self.computeInformationGain(data, 0)

        for i in range(1, 4):
            infoGain = self.computeInformationGain(data, i)
            if infoGain > bestInfoGain:
                bestInfoGain = infoGain
                bestQuestion = i

        return bestInfoGain, bestQuestion

    def buildTree(self, data):
        infoGain, question = self.findBestRoot(data)

        if infoGain == 0:
            return Leaf(data)

        nodes = self.createNodes(data, question)
        children = {}
        for node in nodes:
            children[node] = self.buildTree(nodes[node])

        return Node(children, question)

    def prediction(self, row, tree):
        if isinstance(tree, Leaf):
            return tree.classAppearances()

        question = tree.getQuestion()
        if row[question] - 1 in tree.getNodes():
            return self.prediction(row, tree.getNodes()[row[question] - 1])
        else:
            return tree.classAppearances()
