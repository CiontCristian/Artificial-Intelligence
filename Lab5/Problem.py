class Problem:
    def __init__(self, fileSize, fileParam):
        self.fileSize = fileSize
        self.fileParam = fileParam

    def readSize(self):
        with open(self.fileSize, 'r') as f:
            size = int(f.readline())

        f.close()
        return size

    def readParams(self):
        with open(self.fileParam, 'r') as f:
            noEpoch = int(f.readline())
            noAnts = int(f.readline())
            alpha = float(f.readline())
            beta = float(f.readline())
            rho = float(f.readline())
            q0 = float(f.readline())

        f.close()
        return noEpoch, noAnts, alpha, beta, rho, q0
