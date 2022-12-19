from collections import Counter
from Leaf import Leaf


class Node:
    def __init__(self, nodes, question):
        self.__nodes = nodes
        self.__question = question

    def getNodes(self):
        return self.__nodes

    def getQuestion(self):
        return self.__question

    def classAppearances(self):
        d = {}
        for node in self.__nodes:
            if isinstance(self.__nodes[node], Leaf):
                counter = Counter([row[-1] for row in self.__nodes[node].getNodes()])
                for k in counter:
                    if k in d:
                        d[k] += counter[k]
                    else:
                        d[k] = counter[k]
            else:
                counter = self.__nodes[node].classAppearances()
                for k in counter:
                    if k in d:
                        d[k] += counter[k]
                    else:
                        d[k] = counter[k]
        return d

    def __str__(self):
        s = ""
        s += str(self.__question) + '\n'
        for i in self.__nodes:
            s += str(self.__nodes[i]) + '\n'
        return s
