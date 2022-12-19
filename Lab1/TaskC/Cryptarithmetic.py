from random import randint
from copy import deepcopy


class Cryptarithmetic:
    def __init__(self):
        self.words, self.operator, self.result, self.codes = [], "", "", {}

    def read(self, sentence):
        aux = sentence[:sentence.find("=")]
        self.result = sentence[sentence.find("=") + 1:]

        if aux.find("+") != -1:
            self.operator = aux[aux.find("+")]
            self.words = aux.split("+")
        elif aux.find("-"):
            self.operator = aux[aux.find("-")]
            self.words = aux.split("-")

        letters = set()
        for i in self.words:
            for j in i:
                letters.add(j)
        for j in self.result:
            letters.add(j)
        self.codes = dict.fromkeys(letters, '0x0')

    def checkGame(self, obj):
        for word in obj.words:
            if obj.codes[word[0]] == '0x0':
                return False
        if obj.codes[obj.result[0]] == '0x0':
            return False

        aux_words = []
        temp = ""
        for word in obj.words:
            for letter in list(word):
                temp += obj.codes[letter][2]
            aux_words.append(temp)
            temp = ""

        aux_result = ""
        for letter in list(obj.result):
            aux_result += obj.codes[letter][2]

        int_words = []
        for word in aux_words:
            int_words.append(int(word, 16))

        int_result = int(aux_result, 16)

        if (obj.operator == "+" and sum(int_words) == int_result) or \
                (obj.operator == "-" and int_words[0] - sum(int_words[1:]) == int_result):
            return True
        return False

    def generate(self):
        copy = deepcopy(self)
        for key in copy.codes:
            copy.codes[key] = hex(randint(0, 15))

        if not self.checkGame(copy):
            return False
        else:
            print(copy.codes)
            return True
