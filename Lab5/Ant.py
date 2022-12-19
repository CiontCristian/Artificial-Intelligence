import itertools
import random
from texttable import Texttable
import copy
from Problem import Problem


class Ant:
    def __init__(self):
        self.__problem = Problem("size.txt", "params.txt")
        self.__table = Texttable()
        self.__size = self.__problem.readSize()
        self.__setS = []
        self.__setT = []
        self.__fitness = 0
        self.__visited = []
        self.__values = []
        self.__positions = random.choice(list(itertools.permutations(range(0, self.__size))))
        self.__nrOfGraphs = 0

    def getBothSets(self):
        return self.__setS + self.__setT

    def isVisited(self, node):
        return node in self.__visited

    def nextMoves(self):
        available = []
        for perm in self.__positions:
            if not self.isVisited(perm):
                available.append(perm)

        return available

    def nextGraph(self):
        if len(self.__setS) < self.__size:
            self.__setS.append(copy.deepcopy(self.__values))
        else:
            self.__setT.append(copy.deepcopy(self.__values))

        self.__visited = []
        self.__values = []
        self.__nrOfGraphs += 1
        self.__positions = random.choice(list(itertools.permutations(range(0, self.__size))))

    def addMove(self, trace, alpha, beta, q0):
        if not self.__visited:
            rd = random.choice(self.__positions)
            self.__visited.append(rd)
            self.__values.append(rd + 1)
        else:
            if len(self.__visited) == self.__size - 1:
                for perm in self.__positions:
                    if not self.isVisited(perm):
                        self.__visited.append(perm)
                        self.__values.append(perm + 1)
                        self.nextGraph()
                        return
            else:
                availableMoves = self.nextMoves()

                p = [1 for _ in range(len(availableMoves))]
                p = [(p[i] ** beta) * (trace[self.__nrOfGraphs][self.__visited[-1]][availableMoves[i]] ** alpha) for i
                     in
                     range(len(availableMoves))]

                if random.random() < q0:
                    p = [[i, p[i]] for i in range(len(availableMoves))]
                    p = max(p, key=lambda x: x[1])
                    self.__visited.append(availableMoves[p[0]])
                    self.__values.append(availableMoves[p[0]] + 1)
                else:
                    s = sum(p)
                    if s == 0:
                        rd = random.choice(availableMoves)
                        self.__visited.append(rd)
                        self.__values.append(rd + 1)
                    else:
                        p = [p[i] / s for i in range(len(availableMoves))]
                        p = [sum(p[0:i + 1]) for i in range(len(availableMoves))]
                        r = random.random()

                        i = 0
                        while r > p[i] and i < len(availableMoves):
                            i = i + 1

                        self.__visited.append(availableMoves[i])
                        self.__values.append(availableMoves[i] + 1)

    def __constraint1(self):
        problems = 0
        correct = set(range(1, self.__size + 1))

        for i in range(self.__size):
            if set(self.__setS[i]) != correct:
                problems += 1
            if set(self.__setT[i]) != correct:
                problems += 1

        transposeSetS = [[self.__setS[j][i] for j in range(self.__size)] for i in range(self.__size)]
        transposeSetT = [[self.__setT[j][i] for j in range(self.__size)] for i in range(self.__size)]
        for i in range(self.__size):
            if set(transposeSetS[i]) != correct:
                problems += 1
            if set(transposeSetT[i]) != correct:
                problems += 1

        return problems

    def __constraint2(self):
        aux = []
        for i in range(self.__size):
            for j in range(self.__size):
                aux.append((self.__setS[i][j], self.__setT[i][j]))

        return self.__size * self.__size - len(set(aux))

    def fitness(self):
        self.__fitness = 0
        self.__fitness += self.__constraint1()
        self.__fitness += self.__constraint2()

        return self.__fitness

    def __str__(self):
        matrix = []
        for i in range(self.__size):
            aux = []
            for j in range(self.__size):
                aux.append((self.__setS[i][j], self.__setT[i][j]))
            matrix.append(aux)

        self.__table.add_rows(matrix, [])
        return self.__table.draw()
