from texttable import Texttable
from copy import deepcopy


class State:
    def __init__(self, size):
        self.size = size
        self.table = Texttable()
        self.data = []
        for row in range(self.size):
            self.data.append([])
            for col in range(self.size):
                self.data[row].append(0)

    def drawBoard(self):
        self.table.add_rows(self.data, [])
        return self.table.draw()

    def checkSquare(self, row, col):
        for i in range(self.size):
            for j in range(self.size):
                if self.data[i][j] == 1:
                    if i == row or j == col or (abs(i - row) == abs(j - col)):
                        return False
        return True

    def checkBoard(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.data[i][j] == 1 and not self.checkSquare(i, j):
                    return False
        return True

    def nextConfig(self):
        res = []
        for i in range(self.size):
            for j in range(self.size):
                if self.data[i][j] != 1 and self.checkSquare(i, j):
                    aux_board = deepcopy(self.data)
                    aux_board[i][j] = 1
                    aux_state = State(self.size)
                    aux_state.data = aux_board
                    res.append(aux_state)
        return res

#s = State(5)
#print(s.drawBoard())
