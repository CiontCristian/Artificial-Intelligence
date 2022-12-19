import itertools
import random
from texttable import Texttable
import copy


class State:
    """
    Holds information about 1 individual
    """

    def __init__(self, size, algorithm, generate=True):
        self.table = Texttable()
        self.__size = size
        self.__setS = []
        self.__setT = []
        self.__fitness = 0
        self.__algorithm = algorithm

        if generate:
            range_list = range(1, self.__size + 1)
            all_perm = list(itertools.permutations(range_list))

            for i in range(self.__size):
                self.__setS.append(list(random.choice(all_perm)))
                self.__setT.append(list(random.choice(all_perm)))
        else:
            for i in range(self.__size):
                self.__setS.append([0] * self.__size)
                self.__setT.append([0] * self.__size)

        if self.__algorithm == "EA" or self.__algorithm == "HC":
            self.fitness()
        if self.__algorithm == "PSO":
            self.__bestFitness = 0
            self.__bestPositionsS = []
            self.__bestPositionsT = []
            self.__velocityS = []
            self.__velocityT = []
            self.fitness()
            for i in range(self.__size):
                self.__velocityS.append([0] * self.__size)
                self.__velocityT.append([0] * self.__size)
            self.__bestFitness = self.__fitness
            self.__bestPositionsS = copy.deepcopy(self.__setS)
            self.__bestPositionsT = copy.deepcopy(self.__setT)

    def getSquare(self, i, j):
        return self.__setS[i][j], self.__setT[i][j]

    def setSquare(self, i, j, value):
        self.__setS[i][j] = value[0]
        self.__setT[i][j] = value[1]
        self.fitness()

    def getSetS(self):
        return self.__setS

    def setSetS(self, newSetS):
        self.__setS = newSetS
        self.fitness()

    def getSetT(self):
        return self.__setT

    def setSetT(self, newSetT):
        self.__setT = newSetT
        self.fitness()

    def getVelocityS(self):
        return self.__velocityS

    def getVelocityT(self):
        return self.__velocityT

    def getBestPositionsS(self):
        return self.__bestPositionsS

    def getBestPositionsT(self):
        return self.__bestPositionsT

    def setRowSetS(self, i, perm):
        self.__setS[i] = perm
        self.fitness()

    def setRowSetT(self, i, perm):
        self.__setT[i] = perm
        self.fitness()

    def __constraint1(self):
        """
        Both of the sets S and T must be latin squares(each symbol
        appears only once in each row and each column
        :return:number of problems
        """
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
        """
        Each square formed by one symbol of S and one of T must be unique
        :return: number of problems
        """
        aux = []
        for i in range(self.__size):
            for j in range(self.__size):
                aux.append((self.__setS[i][j], self.__setT[i][j]))

        return self.__size * self.__size - len(set(aux))

    def fitness(self):
        """
        Calculates how close each individual is to being correct(smaller is better)
        :return: int
        """
        self.__fitness = 0
        self.__fitness += self.__constraint1()
        self.__fitness += self.__constraint2()
        if self.__algorithm == "PSO":
            if self.__fitness < self.__bestFitness:
                self.__bestFitness = self.__fitness
                self.__bestPositionsS = copy.deepcopy(self.__setS)
                self.__bestPositionsT = copy.deepcopy(self.__setT)

    def getFitness(self):
        return self.__fitness

    def __str__(self):
        matrix = []
        for i in range(self.__size):
            aux = []
            for j in range(self.__size):
                aux.append((self.__setS[i][j], self.__setT[i][j]))
            matrix.append(aux)

        self.table.add_rows(matrix, [])
        return self.table.draw()
