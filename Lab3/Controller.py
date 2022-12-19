from Problem import Problem


class Controller:
    def __init__(self, size, populationCount, mutateProb, iterations):
        self.__problem = Problem(size, populationCount, mutateProb)
        self.__iterations = iterations

    def EA(self):
        self.__problem.generatePopulationEA()
        for i in range(self.__iterations):
            self.__problem.iterationEA()

        population = self.__problem.getPopulation()
        result = [(x.getFitness(), x) for x in population]
        result.sort(key=lambda g: g[0])
        best = result[0]

        return best


    def HC(self):
        self.__problem.generatePopulationHC()
        for i in range(self.__iterations):
            self.__problem.iterationHC()

        population = self.__problem.getPopulation()
        result = [(x.getFitness(), x) for x in population]
        result.sort(key=lambda g: g[0])
        best = result[0]

        return best
