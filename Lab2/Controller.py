from Problem import Problem
from copy import deepcopy
from queue import PriorityQueue


class Controller:
    def __init__(self, problem):
        self.problem = problem

    def dfs(self):
        stack = [deepcopy(self.problem.state)]

        while stack:
            current = stack.pop(0)
            if self.problem.isWon(current):
                return current

            stack = self.problem.expand(current) + stack
        return None

    def gbfs(self):
        queue = [deepcopy(self.problem.state)]

        while queue:
            current = queue.pop(0)
            if self.problem.isWon(current):
                return current

            queue = self.problem.expand(current) + queue
            queue.sort(key=lambda state: self.problem.heuristic(state), reverse=True)

        return None
