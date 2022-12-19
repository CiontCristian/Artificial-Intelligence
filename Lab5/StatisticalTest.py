from matplotlib import pyplot

from Controller import Controller


class StatisticalTest:
    def __init__(self, size):
        self.__size = size
        self.__noEpoch = 100
        self.__runs = 30
        self.__controller = Controller()

    def testACO(self):
        top30 = []
        for i in range(self.__runs):
            trace = [[[1 for _ in range(self.__size)] for _ in range(self.__size)] for _
                     in range(2 * self.__size)]
            bestAnt = None
            for j in range(self.__noEpoch):
                result = self.__controller.iteration(trace)

                if bestAnt is None:
                    bestAnt = result

                if result.fitness() < bestAnt.fitness():
                    bestAnt = result

            top30.append(bestAnt.fitness())

        mean = sum(top30) / len(top30)
        variance = sum([((x - mean) ** 2) for x in top30]) / len(top30)
        standardDeviation = variance ** 0.5
        print("Average: ", round(mean, 2))
        print("Standard deviation: ", round(standardDeviation, 2))
        pyplot.plot(top30, 'ro')
        pyplot.show()


aco = StatisticalTest(3)
aco.testACO()
