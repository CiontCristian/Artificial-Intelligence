from texttable import Texttable
from math import sqrt
from copy import deepcopy
from random import randint


class Sudoku:
    def __init__(self):
        self.table = Texttable()
        self.data = []
        self.size = 0
        self.readFile("input4x4.txt")

    def printBoard(self):
        self.table.add_rows(self.data, [])
        return self.table.draw()

    def setValue(self, row, col, token):
        self.data[row][col] = token

    def checkBoard(self, board):
        root = int(sqrt(board.size))
        correct = set(range(1, board.size + 1))

        for i in range(board.size):
            for j in range(board.size):
                if board.data[i][j] == 0:
                    return False

        for row in board.data:
            aux = set()
            for col in row:
                aux.add(col)
            if correct != aux:
                return False

        transpose = [[board.data[col][row] for col in range(board.size)] for row in range(board.size)]
        for col in transpose:
            aux = set()
            for row in col:
                aux.add(row)
            if correct != aux:
                return False

        for rootRow in range(root):
            for colRoot in range(root):
                aux = set()
                for row in range(root):
                    for col in range(root):
                        aux.add(board.data[rootRow * root + row][colRoot * root + col])
                if correct != aux:
                    return False
        return True

    def generate(self):
        copy = deepcopy(self)

        for row in range(copy.size):
            for col in range(copy.size):
                if copy.data[row][col] == 0:
                    copy.setValue(row, col, randint(1, copy.size))

        if not self.checkBoard(copy):
            return False
        else:
            print(copy.printBoard())
            return True

    def readFile(self, fileName):
        with open(fileName, 'r') as f:
            self.size = int(f.readline())

            self.data = [[] for _ in range(self.size)]

            cnt = 0
            rows = f.readlines()
            for line in rows:
                line = line.strip().split(" ")
                self.data[cnt] = line
                for j in range(0, self.size):
                    self.data[cnt][j] = int(line[j])
                    # if self.data[cnt][j] == 0:
                    #    self.data[cnt][j] = " "
                cnt += 1

        f.close()
