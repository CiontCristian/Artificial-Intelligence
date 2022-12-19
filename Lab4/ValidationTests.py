from Problem import Problem
from matplotlib import pyplot


class Validation:
    def __init__(self, size):
        self.__size = size
        self.__iterations = 1000
        self.__runs = 30
        self.__population = 40
        self.__mutationProb = 0.01
        self.__problem = Problem(self.__size, self.__population, self.__mutationProb)

    def validateEA(self):
        top30 = []

        for i in range(self.__runs):
            self.__problem.generatePopulationEA()
            for j in range(self.__iterations):
                self.__problem.iterationEA()

            population = self.__problem.getPopulation()
            result = [x.getFitness() for x in population]
            result.sort()
            best = result[0]
            top30.append(best)
            self.__problem.clearPopulation()

        mean = sum(top30) / len(top30)
        variance = sum([((x - mean) ** 2) for x in top30]) / len(top30)
        standardDeviation = variance ** 0.5
        print("Average: ", round(mean, 2))
        print("Standard deviation: ", round(standardDeviation, 2))
        pyplot.plot(top30, 'ro')
        pyplot.show()

    def validateHC(self):
        top30 = []

        for i in range(self.__runs):
            self.__problem.generatePopulationHC()
            for j in range(self.__iterations):
                self.__problem.iterationHC()

            population = self.__problem.getPopulation()
            result = [x.getFitness() for x in population]
            result.sort()
            best = result[0]
            top30.append(best)
            self.__problem.clearPopulation()

        mean = sum(top30) / len(top30)
        variance = sum([((x - mean) ** 2) for x in top30]) / len(top30)
        standardDeviation = variance ** 0.5
        print("Average: ", round(mean, 2))
        print("Standard deviation: ", round(standardDeviation, 2))
        pyplot.plot(top30, 'ro')
        pyplot.show()

    def validatePSO(self):
        top30 = []
        w = 1.0
        c1 = 1.5
        c2 = 1.0
        for i in range(self.__runs):
            self.__problem.generatePopulationPSO()
            for j in range(self.__iterations):
                self.__problem.iterationPSO(w / (i + 1), c1, c2)

            population = self.__problem.getPopulation()
            result = [x.getFitness() for x in population]
            result.sort()
            best = result[0]
            top30.append(best)
            self.__problem.clearPopulation()

        mean = sum(top30) / len(top30)
        variance = sum([((x - mean) ** 2) for x in top30]) / len(top30)
        standardDeviation = variance ** 0.5
        print("Average: ", round(mean, 2))
        print("Standard deviation: ", round(standardDeviation, 2))
        pyplot.plot(top30, 'ro')
        pyplot.show()


validate = Validation(3)
validate.validatePSO()
