from State import State
import random
import itertools
import copy


class Problem:
    def __init__(self, size, populationCount, mutateProb):
        self.__populationCount = populationCount
        self.__size = size
        self.__mutationProb = mutateProb
        self.__population = []
        self.__permutations = []
        self.__bestFitness = 1000
        self.__bestIndivid = []

    def getPopulation(self):
        return self.__population

    def clearPopulation(self):
        self.__population.clear()

    def generatePopulationEA(self):
        for i in range(self.__populationCount):
            self.__population.append(State(self.__size))

    def generatePopulationHC(self):
        self.__population.append(State(self.__size))
        self.__permutations = itertools.permutations(range(1, self.__size + 1))

    def mutate(self, state):
        if self.__mutationProb > random.random():
            i = random.randint(0, self.__size - 1)
            j = random.randint(0, self.__size - 1)
            val1 = random.randint(1, self.__size)
            val2 = random.randint(1, self.__size)
            state.setSquare(i, j, [val1, val2])

    def crossover(self, parent1, parent2):
        child = State(self.__size, False)
        for i in range(self.__size):
            for j in range(self.__size):
                child.setSquare(i, j, random.choice([parent1.getSquare(i, j), parent2.getSquare(i, j)]))
        return child

    def iterationEA(self):
        i1 = random.randint(0, self.__populationCount - 1)
        i2 = random.randint(0, self.__populationCount - 1)
        if i1 != i2:
            c = self.crossover(self.__population[i1], self.__population[i2])
            self.mutate(c)
            f1 = self.__population[i1].getFitness()
            f2 = self.__population[i2].getFitness()
            fc = c.getFitness()
            if (f1 > f2) and (f1 > fc):
                self.__population[i1] = c
            if (f2 > f1) and (f2 > fc):
                self.__population[i2] = c

    def expand(self):
        self.__bestIndivid = self.__population[0]
        self.__bestFitness = self.__bestIndivid.getFitness()
        for perm in self.__permutations:
            index1 = random.randint(0, self.__size - 1)
            index2 = random.randint(0, self.__size - 1)
            auxS = copy.deepcopy(self.__bestIndivid)
            auxS.setRowSetS(index1, perm)
            auxT = copy.deepcopy(self.__bestIndivid)
            auxT.setRowSetT(index2, perm)
            self.__population.append(auxS)
            self.__population.append(auxT)

    def iterationHC(self):
        self.expand()
        for i in self.__population:
            if i.getFitness() < self.__bestFitness:
                self.__bestIndivid = copy.deepcopy(i)
                self.__bestFitness = self.__bestIndivid.getFitness()

        self.clearPopulation()
        self.__population.append(self.__bestIndivid)
