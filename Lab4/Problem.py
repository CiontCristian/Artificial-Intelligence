from State import State
import random
import itertools
import copy

MAX = 1000


class Problem:
    def __init__(self, size, populationCount, mutateProb):
        self.__populationCount = populationCount
        self.__size = size
        self.__mutationProb = mutateProb
        self.__population = []
        self.__permutations = []
        self.__bestFitness = MAX
        self.__bestIndivid = []

    def getPopulation(self):
        return self.__population

    def clearPopulation(self):
        self.__population.clear()

    def generatePopulationEA(self):
        for i in range(self.__populationCount):
            self.__population.append(State(self.__size, "EA"))

    def generatePopulationHC(self):
        self.__population.append(State(self.__size, "HC"))
        self.__permutations = itertools.permutations(range(1, self.__size + 1))

    def generatePopulationPSO(self):
        for i in range(self.__populationCount):
            self.__population.append(State(self.__size, "PSO", True))

    def mutate(self, state):
        """
        Gives a random valid value to a square at a random position
        of an individual with a given probability
        :param state:
        :return:
        """
        if self.__mutationProb > random.random():
            i = random.randint(0, self.__size - 1)
            j = random.randint(0, self.__size - 1)
            val1 = random.randint(1, self.__size)
            val2 = random.randint(1, self.__size)
            state.setSquare(i, j, [val1, val2])

    def crossover(self, parent1, parent2):
        """
        Creates a new individual with attributes from 2 given individuals
        :param parent1:
        :param parent2:
        :return:
        """
        child = State(self.__size, "EA", False)
        for i in range(self.__size):
            for j in range(self.__size):
                child.setSquare(i, j, random.choice([parent1.getSquare(i, j), parent2.getSquare(i, j)]))
        return child

    def iterationEA(self):
        """
        Selects a better part of the population to go in the next
        generation
        :return:
        """
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
        """
        Creates a set of solutions from an individual
        by changing random rows from it with valid permutations
        :return:
        """
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
        """
        Selects a better part of the population to go in the next
        generation
        :return:
        """
        self.expand()
        for i in self.__population:
            if i.getFitness() < self.__bestFitness:
                self.__bestIndivid = copy.deepcopy(i)
                self.__bestFitness = self.__bestIndivid.getFitness()

        self.clearPopulation()
        self.__population.append(self.__bestIndivid)

    def selectNeighbours(self):
        """
        Selects random positions in the population space
        for each particle
        :return:
        """
        neighbours = []
        for i in range(self.__populationCount):
            local = []
            for j in range(self.__populationCount // 5):
                x = random.randint(0, self.__populationCount - 1)
                while x in local:
                    x = random.randint(0, self.__populationCount - 1)
                local.append(x)
            neighbours.append(local)
        return neighbours

    def limit(self, square):
        if square > self.__size:
            square = self.__size
        if square < 1:
            square = 1
        return square

    def iterationPSO(self, w, c1, c2):
        bestNeighbours = []
        neighbours = self.selectNeighbours()
        # Best neighbour for each particle
        for i in range(self.__populationCount):
            bestNeighbours.append(neighbours[i][0])
            for j in range(1, len(neighbours[i])):
                if self.__population[bestNeighbours[i]].getFitness() > self.__population[neighbours[i][j]].getFitness():
                    bestNeighbours[i] = neighbours[i][j]
        # Updates the velocities for both the sets S and T
        for i in range(self.__populationCount):
            for j in range(self.__size):
                for k in range(self.__size):
                    newVelocityS = w * self.__population[i].getVelocityS()[j][k]
                    newVelocityS += c1 * random.random() * (self.__population[bestNeighbours[i]].getSetS()[j][k] -
                                                            self.__population[i].getSetS()[j][k])
                    newVelocityS += c2 * random.random() * (
                            self.__population[i].getBestPositionsS()[j][k] - self.__population[i].getSetS()[j][k])
                    self.__population[i].getVelocityS()[j][k] = newVelocityS

                    newVelocityT = w * self.__population[i].getVelocityT()[j][k]
                    newVelocityT += c1 * random.random() * (self.__population[bestNeighbours[i]].getSetT()[j][k] -
                                                            self.__population[i].getSetT()[j][k])
                    newVelocityT += c2 * random.random() * (
                            self.__population[i].getBestPositionsT()[j][k] - self.__population[i].getSetT()[j][k])
                    self.__population[i].getVelocityT()[j][k] = newVelocityT
        # Updates the positions for both the sets S and T
        for i in range(self.__populationCount):
            newSetS = []
            newSetT = []
            for j in range(self.__size):
                auxS = []
                auxT = []
                for k in range(self.__size):
                    squareS = self.__population[i].getSetS()[j][k] + round(self.__population[i].getVelocityS()[j][k])
                    squareT = self.__population[i].getSetT()[j][k] + round(self.__population[i].getVelocityT()[j][k])
                    auxS.append(self.limit(squareS))
                    auxT.append(self.limit(squareT))
                newSetS.append(auxS)
                newSetT.append(auxT)
            self.__population[i].setSetS(newSetS)
            self.__population[i].setSetT(newSetT)
