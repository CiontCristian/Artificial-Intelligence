from texttable import Texttable
from copy import deepcopy
from random import randint

FORM1 = ((1, 1, 1, 1, 0, 0),
         (0, 0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0, 0))

FORM2 = ((2, 0, 2, 0, 0, 0),
         (2, 2, 2, 0, 0, 0),
         (0, 0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0, 0))

FORM3 = ((0, 3, 0, 0, 0, 0),
         (3, 3, 3, 0, 0, 0),
         (0, 0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0, 0))

FORM4 = ((4, 0, 0, 0, 0, 0),
         (4, 4, 4, 0, 0, 0),
         (0, 0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0, 0))

FORM5 = ((5, 5, 5, 0, 0, 0),
         (0, 0, 5, 0, 0, 0),
         (0, 0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0, 0),
         (0, 0, 0, 0, 0, 0))

FORMS = [FORM1, FORM2, FORM3, FORM4, FORM5]


class GeometricForms:
    def __init__(self):
        self.table = Texttable()
        self.rows = 5
        self.cols = 6
        self.data = []
        for i in range(self.rows):
            self.data.append([])
            for j in range(self.cols):
                self.data[i].append(0)

    def printBoard(self):
        self.table.add_rows(self.data, [])
        return self.table.draw()

    def getFormDimension(self, form):
        length, width = 0, 0
        for i in range(self.rows):
            for j in range(self.cols):
                if form[i][j] != 0:
                    length = max(i, length)
                    width = max(j, width)
        return length + 1, width + 1

    def checkBoard(self, board):
        cnt1, cnt2, cnt3, cnt4, cnt5 = 0, 0, 0, 0, 0
        for i in range(board.rows):
            for j in range(board.cols):
                if board.data[i][j] == 1:
                    cnt1 += 1
                elif board.data[i][j] == 2:
                    cnt2 += 1
                elif board.data[i][j] == 3:
                    cnt3 += 1
                elif board.data[i][j] == 4:
                    cnt4 += 1
                elif board.data[i][j] == 5:
                    cnt5 += 1
        if cnt1 == 4 and cnt2 == 5 and cnt3 == 4 and cnt4 == 4 and cnt5 == 4:
            return True
        return False

    def generate(self):
        copy = deepcopy(self)

        for form in FORMS:
            dimensions = self.getFormDimension(form)
            row = randint(0, self.rows - dimensions[0])
            col = randint(0, self.cols - dimensions[1])

            for i in range(dimensions[0]):
                for j in range(dimensions[1]):
                    try:
                        if form[i][j] != 0:
                            copy.data[row + i][col + j] = form[i][j]
                    except IndexError:
                        pass

        if not self.checkBoard(copy):
            return False
        else:
            print(copy.printBoard())
            return True
