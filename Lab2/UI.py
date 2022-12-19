from Controller import Controller
from State import State
from Problem import Problem
import time


class UI:
    def __init__(self):
        self.size = 4
        self.state = State(self.size)
        self.problem = Problem(self.state)
        self.controller = Controller(self.problem)

    def menu(self):
        print("0.Exit")
        print("1.Choose matrix size")
        print("2.Solve with DFS")
        print("3.Solver with GreedyBFS")

    def changeMatrixSize(self):
        n = 4
        try:
            n = int(input("Enter the matrix size: "))
            if n < 3:
                raise ValueError
        except ValueError:
            print("Invalid matrix size!")

        self.size = n
        self.state = State(self.size)
        self.problem = Problem(self.state)
        self.controller = Controller(self.problem)

    def run(self):
        self.menu()
        while True:
            try:
                command = int(input(">:"))
                if command == 0:
                    break
                elif command == 1:
                    self.changeMatrixSize()
                elif command == 2:
                    startTime = time.time()
                    res = self.controller.dfs()
                    print("Time: {0} \n".format(time.time() - startTime))
                    if res is None:
                        print("Could not find a solution!")
                    else:
                        print(res.drawBoard())
                elif command == 3:
                    startTime = time.time()
                    res = self.controller.gbfs()
                    print("Time: {0} \n".format(time.time() - startTime))
                    if res is None:
                        print("Could not find a solution!")
                    else:
                        print(res.drawBoard())
                else:
                    raise ValueError
            except ValueError:
                print("Error")
