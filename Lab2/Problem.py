from State import State


class Problem:
    def __init__(self, state):
        self.state = state

    def isWon(self, state):
        total = 0
        for row in state.data:
            total += sum(row)

        return total == state.size

    def expand(self, state):
        for row in state.data:
            if 0 in row:
                return state.nextConfig()
        return None

    def heuristic(self, state):
        if not state.checkBoard():
            return -1

        count = 0
        for i in state.size:
            for j in state.size:
                if state.data[i][j] == 1:
                    count += 2
        return count
