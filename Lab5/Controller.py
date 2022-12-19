from Ant import Ant
from Problem import Problem


class Controller:
    def __init__(self):
        self.__problem = Problem("size.txt", "params.txt")
        self.__size = self.__problem.readSize()
        self.__noEpoch = 0
        self.__noAnts = 0
        self.__alpha = 0
        self.__beta = 0
        self.__rho = 0
        self.__q0 = 0
        self.updateParams()

    def updateParams(self):
        params = self.__problem.readParams()
        self.__noEpoch = params[0]
        self.__noAnts = params[1]
        self.__alpha = params[2]
        self.__beta = params[3]
        self.__rho = params[4]
        self.__q0 = params[5]

    def getSize(self):
        return self.__size

    def getNoEpoch(self):
        return self.__noEpoch

    def iteration(self, trace):
        antSet = [Ant() for _ in range(self.__noAnts)]

        for i in range(2 * self.__size * self.__size):
            for ant in antSet:
                ant.addMove(trace, self.__alpha, self.__beta, self.__q0)

        dTrace = []
        for i in range(len(antSet)):
            if antSet[i].fitness() == 0:
                dTrace.append(1.0)
            else:
                dTrace.append(1.0 / antSet[i].fitness())

        for i in range(2 * self.__size):
            for j in range(self.__size):
                for k in range(self.__size):
                    trace[i][j][k] = (1 - self.__rho) * trace[i][j][k]

        for i in range(len(antSet)):
            for j in range(2 * self.__size):
                for k in range(self.__size - 1):
                    x = antSet[i].getBothSets()[j][k] - 1
                    y = antSet[i].getBothSets()[j][k + 1] - 1
                    trace[j][x][y] = trace[j][x][y] + dTrace[i]

        f = [[antSet[i].fitness(), i] for i in range(len(antSet))]
        f = min(f)

        return antSet[f[1]]
