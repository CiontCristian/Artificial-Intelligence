import itertools
import random
from texttable import Texttable


class State:
    '''
    Holds information about 1 individ
    '''

    def __init__(self, size, generate=True):
        self.table = Texttable()
        self.__size = size
        self.__setS = []
        self.__setT = []
        self.__fitness = 0

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
        self.fitness()

    def getSquare(self, i, j):
        return self.__setS[i][j], self.__setT[i][j]

    def setSquare(self, i, j, value):
        self.__setS[i][j] = value[0]
        self.__setT[i][j] = value[1]
        self.fitness()

    def setRowSetS(self, i, perm):
        self.__setS[i] = perm
        self.fitness()

    def setRowSetT(self, i, perm):
        self.__setT[i] = perm
        self.fitness()

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