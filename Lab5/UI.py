import time


class UI:
    def __init__(self, controller):
        self.__controller = controller

    def run(self):
        trace = [[[1 for _ in range(self.__controller.getSize())] for _ in range(self.__controller.getSize())] for _ in range(2 * self.__controller.getSize())]

        bestAnt = None

        startTime = time.time()

        try:
            for i in range(self.__controller.getNoEpoch()):
                result = self.__controller.iteration(trace)

                if bestAnt is None:
                    bestAnt = result

                if result.fitness() < bestAnt.fitness():
                    bestAnt = result
        except RuntimeError:
            print("Error!")

        print(bestAnt)
        print("Problems: " + str(bestAnt.fitness()))
        print("Time: {0} \n".format(time.time() - startTime))
