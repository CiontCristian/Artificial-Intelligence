import time
from Sudoku import Sudoku
from GeometricForms import GeometricForms
from Cryptarithmetic import Cryptarithmetic


class UI:
    def __init__(self):
        self.sudoku = Sudoku()
        self.geom = GeometricForms()
        self.crypt = Cryptarithmetic()

    def menu(self):
        print("Choose game: ")
        print("1.Sudoku")
        print("2.Cryptarithmetic game")
        print("3.Geometric Forms")
        print("0.Exit")

    def run(self):
        self.menu()
        option = int(input("<:"))

        if option == 1:
            maxAttempts = int(input("Enter max attempts: "))
            startTime = time.time()
            for _ in range(maxAttempts):
                if self.sudoku.generate():
                    print("Time: {0} \n".format(time.time() - startTime))
                    exit(0)

            print("Unable to solve in less than " + str(maxAttempts) + " attempts")
            print("Time: {0} \n".format(time.time() - startTime))

        elif option == 2:
            maxAttempts = int(input("Enter max attempts: "))
            sentence = input("Enter sentence: ")
            startTime = time.time()
            self.crypt.read(sentence)
            for _ in range(maxAttempts):
                if self.crypt.generate():
                    print("Time: {0} \n".format(time.time() - startTime))
                    exit(0)

            print("Unable to solve in less than " + str(maxAttempts) + " attempts")
            print("Time: {0} \n".format(time.time() - startTime))

        elif option == 3:
            maxAttempts = int(input("Enter max attempts: "))
            startTime = time.time()
            for _ in range(maxAttempts):
                if self.geom.generate():
                    print("Time: {0} \n".format(time.time() - startTime))
                    exit(0)

            print("Unable to solve in less than " + str(maxAttempts) + " attempts")
            print("Time: {0} \n".format(time.time() - startTime))
        else:
            exit(0)
