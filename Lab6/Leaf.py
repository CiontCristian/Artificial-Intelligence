from collections import Counter


class Leaf:
    def __init__(self, nodes):
        self.__nodes = nodes

    def getNodes(self):
        return self.__nodes

    def classAppearances(self):
        counter = Counter([row[-1] for row in self.__nodes])

        return dict(counter.items())

    def __str__(self):
        return str(self.__nodes)
