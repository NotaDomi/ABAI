import numpy as np


class Maze:
    def __init__(self, M, N, K, V):
        self.width = N
        self.height = M
        self.n_walls = K
        self.p_walls = V

    def create_environment(self):
        maze = np.ones((self.height, self.width), dtype=int)  # <- 1: reachable element
        for i in range(self.n_walls):
            maze[self.p_walls[i][0]][self.p_walls[i][1]] = 2  # <- 2: unreachable element

        return maze